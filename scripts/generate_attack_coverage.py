
"""Generate an ATT&CK coverage table from existing Sigma rule tags."""

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
RULES_DIR = ROOT / "rules"
OUTPUT = ROOT / "docs" / "ATTACK_COVERAGE.md"


def main():
    rows = []

    for path in sorted(RULES_DIR.rglob("*.yml")):
        rule = yaml.safe_load(path.read_text(encoding="utf-8"))

        if not isinstance(rule, dict):
            continue

        if rule.get("type") == "correlation":
            continue

        tags = rule.get("tags", [])
        attack_tags = [
            tag for tag in tags
            if isinstance(tag, str) and tag.startswith("attack.")
        ]

        techniques = ", ".join(attack_tags) if attack_tags else "Not tagged"

        rows.append(
            (
                rule.get("title", "Untitled"),
                str(path.relative_to(ROOT)).replace("\\", "/"),
                rule.get("id", "Missing ID"),
                techniques,
            )
        )

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    lines = [
        "# Cyberion ThreatShield — ATT&CK Coverage",
        "",
        "Generated from the ATT&CK tags in the project's Sigma YAML files.",
        "",
        "ATT&CK tags represent intended coverage, not proven production efficacy.",
        "",
        "| Rule | File | UUID | ATT&CK tags |",
        "|---|---|---|---|",
    ]

    for title, path, rule_id, techniques in rows:
        lines.append(
            f"| {title} | `{path}` | `{rule_id}` | {techniques} |"
        )

    lines.extend(
        [
            "",
            "## Limitations",
            "",
            "- Tags are read from Sigma metadata and are not independently verified.",
            "- Untagged rules are shown as `Not tagged`.",
            "- Technique mapping does not prove detection efficacy.",
            "- Correlation rules are excluded from this generated table.",
            "- Review ATT&CK mappings before using this report for formal coverage claims.",
            "",
        ]
    )

    OUTPUT.write_text("\n".join(lines), encoding="utf-8")

    print(f"Generated {OUTPUT.relative_to(ROOT)}")
    print(f"Included {len(rows)} single-event rules.")


if __name__ == "__main__":
    main()
