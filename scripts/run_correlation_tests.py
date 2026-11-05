
"""Run correlation rules against the project's sample event fixture."""

import sys
from pathlib import Path

# Make the repository root importable when this file is run directly.
ROOT = Path(__file__).resolve().parents[1]

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import yaml

from scripts.correlation_engine import (
    evaluate_correlation,
    load_jsonl,
    load_rules,
)


def main():
    all_rules = load_rules()
    events = load_jsonl(ROOT / "data/sample/events.jsonl")

    correlation_dir = ROOT / "rules/correlation"
    correlation_files = sorted(correlation_dir.glob("*.yml"))

    print(f"Loaded {len(events)} sample events.")
    print(f"Found {len(correlation_files)} correlation rules.")
    print()

    for path in correlation_files:
        rule = yaml.safe_load(path.read_text(encoding="utf-8"))

        alerts = evaluate_correlation(rule, events, all_rules)

        print(f"Rule: {rule['title']}")
        print(f"Correlation ID: {rule['id']}")
        print(f"Alerts: {len(alerts)}")

        for alert in alerts:
            print(
                f"  group={alert['group']} "
                f"count={alert['count']} "
                f"window={alert['window']} "
                f"time={alert['timestamp']}"
            )

        if not alerts:
            print("  No correlation threshold reached in sample data.")

        print()


if __name__ == "__main__":
    main()
