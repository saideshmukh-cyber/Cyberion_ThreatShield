import csv
from pathlib import Path
from collections import defaultdict

processed_dir = Path("data/processed")
rules_dir = Path("rules")
reports_dir = Path("reports")
reports_dir.mkdir(exist_ok=True)

# Map observed event IDs to potential detection use cases.
# These are preliminary mappings, not proof of rule effectiveness.
event_mapping = {
    "4625": ("Repeated Failed Logons", "Relevant"),
    "4624": ("Remote Interactive Logon (RDP)", "Conditional: check LogonType"),
    "1102": ("Security Event Log Cleared", "Relevant"),
    "4702": ("Scheduled Task Created", "Related: task updated, not created"),
    "1": ("PowerShell Encoded Command Execution; Temp Executable; PowerShell Download Cradle",
          "Conditional: inspect process command line and image"),
    "3": ("PowerShell Download Cradle; Large Outbound Transfer",
          "Conditional: inspect network connection details"),
    "10": ("Potential LSASS Process Access",
           "Conditional: inspect TargetImage and GrantedAccess"),
    "4": ("New Windows Service Installation",
          "Related: Sysmon service state change; not installation proof"),
    "7": ("Potential LSASS Process Access",
          "Related: image loaded; not direct LSASS access evidence"),
    "11": ("Executable Launched from User Temp Directory",
           "Related: file creation; inspect path and process"),
    "12": ("No direct match in current rules",
           "Registry object activity"),
    "16": ("No direct match in current rules",
           "Sysmon configuration change"),
    "5": ("No direct match in current rules",
           "Sysmon process termination"),
    "5136": ("No direct match in current rules",
             "Active Directory object modification"),
    "4662": ("No direct match in current rules",
             "Directory service object access"),
    "4719": ("No direct match in current rules",
             "System audit policy changed"),
    "4738": ("No direct match in current rules",
             "User account changed"),
    "4742": ("No direct match in current rules",
             "Computer account changed"),
    "4794": ("No direct match in current rules",
             "DSRM password changed"),
    "1116": ("Defender malware detection",
             "Defender detection event; not the rule for disabling Defender"),
    "1117": ("Defender remediation/action",
             "Related Defender event; inspect action/status fields"),
}

# Count observed event IDs from all parsed CSVs.
event_counts = defaultdict(int)
event_sources = defaultdict(set)

for csv_file in sorted(processed_dir.glob("*_events.csv")):
    with csv_file.open("r", encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            event_id = row.get("event_id", "").strip() or "Unknown"
            source = row.get("source_file", "").strip() or csv_file.name
            event_counts[event_id] += 1
            event_sources[event_id].add(source)

# List Sigma rule filenames to help check the mapping.
rule_files = sorted(rules_dir.rglob("*.yml"))
rule_names = [p.name for p in rule_files]

md_path = reports_dir / "detection_relevance_matrix.md"
csv_path = reports_dir / "detection_relevance_matrix.csv"

with md_path.open("w", encoding="utf-8") as f:
    f.write("# Detection Relevance Matrix\n\n")
    f.write("Preliminary mapping of observed event IDs to existing detection use cases.\n\n")
    f.write("**Important:** Event ID presence alone does not validate a Sigma rule. "
            "Review event fields, log source, and rule conditions before claiming coverage.\n\n")
    f.write("| Event ID | Count | Potential rule/use case | Assessment | Source files |\n")
    f.write("|---|---:|---|---|---|\n")

    for event_id in sorted(event_counts, key=lambda x: (not x.isdigit(), int(x) if x.isdigit() else x)):
        rule, assessment = event_mapping.get(
            event_id,
            ("No mapped rule yet", "Needs investigation")
        )
        sources = ", ".join(sorted(event_sources[event_id]))
        f.write(f"| {event_id} | {event_counts[event_id]} | {rule} | {assessment} | {sources} |\n")

    f.write("\n## Existing Sigma rule files\n\n")
    for name in rule_names:
        f.write(f"- `{name}`\n")

with csv_path.open("w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["event_id", "count", "potential_rule", "assessment", "source_files"])

    for event_id in sorted(event_counts, key=lambda x: (not x.isdigit(), int(x) if x.isdigit() else x)):
        rule, assessment = event_mapping.get(
            event_id,
            ("No mapped rule yet", "Needs investigation")
        )
        writer.writerow([
            event_id,
            event_counts[event_id],
            rule,
            assessment,
            "; ".join(sorted(event_sources[event_id]))
        ])

print(f"Event IDs mapped: {len(event_counts)}")
print(f"Markdown matrix: {md_path}")
print(f"CSV matrix: {csv_path}")
print(f"Sigma rule files found: {len(rule_names)}")
