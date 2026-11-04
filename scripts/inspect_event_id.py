import csv
import json
import sys
from pathlib import Path

if len(sys.argv) != 2:
    raise SystemExit("Usage: python scripts/inspect_event_id.py EVENT_ID")

target_id = sys.argv[1]
processed_dir = Path("data/processed")
matches = 0

for csv_file in sorted(processed_dir.glob("*_events.csv")):
    with csv_file.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)

        for row in reader:
            if row.get("event_id", "").strip() != target_id:
                continue

            matches += 1

            print("\n" + "=" * 70)
            print(f"Source CSV: {csv_file.name}")
            print(f"Source EVTX: {row.get('source_file', '')}")
            print(f"Record ID: {row.get('record_id', '')}")
            print(f"Timestamp: {row.get('timestamp', '')}")
            print(f"Provider: {row.get('provider', '')}")
            print(f"Channel: {row.get('channel', '')}")

            raw_data = row.get("event_data", "")

            print("\nEvent data:")
            try:
                parsed = json.loads(raw_data)
                print(json.dumps(parsed, indent=2, ensure_ascii=False))
            except (json.JSONDecodeError, TypeError):
                print(raw_data or "(No event_data field)")

            print("\nEvent XML:")
            print(row.get("event_xml", "") or "(No event_xml field)")

if matches == 0:
    print(f"No records found for Event ID {target_id}.")
else:
    print(f"\nTotal matching records: {matches}")
