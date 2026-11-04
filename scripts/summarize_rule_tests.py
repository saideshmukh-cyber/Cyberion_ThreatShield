
"""Combine Windows, Linux, and network rule-test results."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPORTS = ROOT / "reports"

INPUTS = {
    "Windows": REPORTS / "windows_rule_test_results.json",
    "Linux and Network": REPORTS / "linux_network_rule_test_results.json",
}

all_rules = []
summary = {}

for category, filepath in INPUTS.items():
    if not filepath.exists():
        raise FileNotFoundError(f"Missing report: {filepath}")

    results = json.loads(filepath.read_text(encoding="utf-8"))

    summary[category] = {
        "rules_evaluated": len(results),
        "rules_with_matches": sum(
            result["matches"] > 0 for result in results
        ),
        "rules_without_matches": sum(
            result["matches"] == 0 for result in results
        ),
    }

    for result in results:
        all_rules.append({
            "category": category,
            **result,
        })

total_rules = len(all_rules)
matched_rules = sum(rule["matches"] > 0 for rule in all_rules)
unmatched_rules = total_rules - matched_rules

report = {
    "project": "Cyberion ThreatShield",
    "report_type": "Synthetic Single-Event Rule Testing",
    "categories": summary,
    "overall": {
        "rules_evaluated": total_rules,
        "rules_with_matches": matched_rules,
        "rules_without_matches": unmatched_rules,
        "match_percentage": round(
            matched_rules / total_rules * 100, 2
        ) if total_rules else 0,
    },
    "rules": all_rules,
    "limitations": [
        "Results are based on synthetic fixtures.",
        "This is a custom smoke-test harness, not a full Sigma implementation.",
        "Correlation rules are not evaluated.",
        "Matches do not establish production detection effectiveness.",
    ],
}

output_path = REPORTS / "consolidated_rule_test_results.json"
output_path.write_text(
    json.dumps(report, indent=2) + "\n",
    encoding="utf-8",
)

print("Consolidated rule-testing report created.")
print(f"Output: {output_path.relative_to(ROOT)}")
print()
print("Category summary:")

for category, result in summary.items():
    print(
        f"{category}: "
        f"{result['rules_with_matches']}/"
        f"{result['rules_evaluated']} rules matched"
    )

print()
print(f"Total rules: {total_rules}")
print(f"Rules with matches: {matched_rules}")
print(f"Rules without matches: {unmatched_rules}")
