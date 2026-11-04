import sys
import csv
import json
import xml.etree.ElementTree as ET
from pathlib import Path

from Evtx.Evtx import Evtx

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATASET_DIR = PROJECT_ROOT / "data" / "raw" / "EVTX-ATTACK-SAMPLES"
OUTPUT_DIR = PROJECT_ROOT / "data" / "processed"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

NS = {
    "e": "http://schemas.microsoft.com/win/2004/08/events/event"
}


def get_text(root, path):
    element = root.find(path, NS)
    return element.text if element is not None and element.text else ""


def parse_evtx(file_path):
    records = []

    with Evtx(str(file_path)) as log:
        for record in log.records():
            try:
                xml_data = record.xml()
                root = ET.fromstring(xml_data)

                system = root.find("e:System", NS)

                event_data = {}

                for item in root.findall(".//e:EventData/e:Data", NS):
                    name = item.attrib.get("Name", "Unnamed")
                    value = item.text or ""

                    # Preserve duplicate field names rather than overwrite.
                    if name in event_data:
                        if not isinstance(event_data[name], list):
                            event_data[name] = [event_data[name]]
                        event_data[name].append(value)
                    else:
                        event_data[name] = value

                provider = system.find("e:Provider", NS) if system is not None else None
                time_created = system.find("e:TimeCreated", NS) if system is not None else None
                execution = system.find("e:Execution", NS) if system is not None else None

                records.append({
                    "source_file": file_path.name,
                    "source_path": file_path.relative_to(DATASET_DIR).as_posix(),
                    "record_id": record.record_num(),
                    "timestamp": time_created.attrib.get("SystemTime", "") if time_created is not None else "",
                    "event_id": get_text(root, ".//e:System/e:EventID"),
                    "provider": provider.attrib.get("Name", "") if provider is not None else "",
                    "channel": get_text(root, ".//e:System/e:Channel"),
                    "computer": get_text(root, ".//e:System/e:Computer"),
                    "process_id": execution.attrib.get("ProcessID", "") if execution is not None else "",
                    "thread_id": execution.attrib.get("ThreadID", "") if execution is not None else "",
                    "event_data": json.dumps(event_data, ensure_ascii=False),
                    "event_xml": xml_data,
                })

            except Exception as error:
                print(
                    f"WARNING: Failed record in {file_path.name}: {error}",
                    file=sys.stderr,
                )

    return records


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/parse_evtx.py <path-to-evtx>")
        sys.exit(1)

    input_file = Path(sys.argv[1])

    if not input_file.is_absolute():
        input_file = PROJECT_ROOT / input_file

    if not input_file.exists():
        print(f"ERROR: File not found: {input_file}")
        sys.exit(1)

    if input_file.suffix.lower() != ".evtx":
        print("ERROR: Input must be an .evtx file")
        sys.exit(1)

    print(f"Parsing: {input_file.name}")

    try:
        records = parse_evtx(input_file)
    except Exception as error:
        print(f"ERROR: Could not parse EVTX: {error}")
        sys.exit(1)

    output_file = OUTPUT_DIR / f"{input_file.stem}_events.csv"

    if records:
        with output_file.open("w", newline="", encoding="utf-8-sig") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=records[0].keys())
            writer.writeheader()
            writer.writerows(records)

    print(f"Events extracted: {len(records)}")
    print(f"Output: {output_file.relative_to(PROJECT_ROOT)}")


if __name__ == "__main__":
    main()
