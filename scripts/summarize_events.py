import csv
from pathlib import Path
from collections import Counter, defaultdict

processed_dir = Path("data/processed")
reports_dir = Path("reports")
reports_dir.mkdir(exist_ok=True)

csv_files = sorted(processed_dir.glob("*_events.csv"))

if not csv_files:
    raise SystemExit("No parsed event CSV files found.")

event_counts = Counter()
source_counts = Counter()
provider_counts = Counter()
channel_counts = Counter()
event_sources = defaultdict(set)

total_events = 0

for csv_file in csv_files:
    with csv_file.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)

        for row in reader:
            event_id = row.get("event_id", "").strip() or "Unknown"
            provider = row.get("provider", "").strip() or "Unknown"
            channel = row.get("channel", "").strip() or "Unknown"
            source = row.get("source_file", "").strip() or csv_file.name

            event_counts[event_id] += 1
            source_counts[source] += 1
            provider_counts[provider] += 1
            channel_counts[channel] += 1
            event_sources[event_id].add(source)

            total_events += 1

# Event ID summary
event_summary = reports_dir / "event_id_summary.csv"

with event_summary.open("w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["event_id", "event_count", "source_files"])

    for event_id, count in event_counts.most_common():
        writer.writerow([
            event_id,
            count,
            "; ".join(sorted(event_sources[event_id]))
        ])

# Source file summary
source_summary = reports_dir / "event_source_summary.csv"

with source_summary.open("w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["source_file", "event_count"])

    for source, count in source_counts.most_common():
        writer.writerow([source, count])

# Markdown report
markdown_report = reports_dir / "event_id_summary.md"

with markdown_report.open("w", encoding="utf-8") as f:
    f.write("# EVTX Event ID Summary\n\n")
    f.write("## Dataset scope\n\n")
    f.write(f"- Parsed CSV files: {len(csv_files)}\n")
    f.write(f"- Total event records: {total_events}\n\n")

    f.write("## Event ID counts\n\n")
    f.write("| Event ID | Count | Source files |\n")
    f.write("|---|---:|---|\n")

    for event_id, count in event_counts.most_common():
        sources = ", ".join(sorted(event_sources[event_id]))
        f.write(f"| {event_id} | {count} | {sources} |\n")

    f.write("\n## Provider counts\n\n")
    f.write("| Provider | Count |\n|---|---:|\n")

    for provider, count in provider_counts.most_common():
        f.write(f"| {provider} | {count} |\n")

    f.write("\n## Channel counts\n\n")
    f.write("| Channel | Count |\n|---|---:|\n")

    for channel, count in channel_counts.most_common():
        f.write(f"| {channel} | {count} |\n")

    f.write("\n## Source file counts\n\n")
    f.write("| Source file | Count |\n|---|---:|\n")

    for source, count in source_counts.most_common():
        f.write(f"| {source} | {count} |\n")

print(f"Parsed CSV files: {len(csv_files)}")
print(f"Total event records: {total_events}")
print(f"Unique event IDs: {len(event_counts)}")
print(f"Event ID summary: {event_summary}")
print(f"Source summary: {source_summary}")
print(f"Markdown report: {markdown_report}")
