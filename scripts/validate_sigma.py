
"""Basic YAML and metadata validation.

This is a project-level structural check, not a full Sigma
specification validator.
"""
import argparse
import sys
from pathlib import Path

import yaml

REQUIRED = {
    "title", "id", "status", "description", "references",
    "tags", "logsource", "detection", "falsepositives", "level",
}

CORRELATION_REQUIRED = {
    "title", "id", "type", "correlation", "tags",
    "falsepositives", "level",
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--rules", nargs="+", default=["rules"])
    args = parser.parse_args()

    errors = []
    count = 0

    for base in args.rules:
        path = Path(base)
        files = sorted(path.rglob("*.yml")) if path.is_dir() else [path]

        for file in files:
            count += 1

            try:
                rule = yaml.safe_load(file.read_text(encoding="utf-8"))

                if not isinstance(rule, dict):
                    errors.append(f"{file}: YAML document must be a mapping")
                    continue

                is_correlation = rule.get("type") == "correlation"

                required = (
                    CORRELATION_REQUIRED if is_correlation else REQUIRED
                )

                missing = required - set(rule)
                if missing:
                    errors.append(
                        f"{file}: missing keys {sorted(missing)}"
                    )

                if not isinstance(rule.get("tags"), list):
                    errors.append(f"{file}: tags must be a list")

                if is_correlation:
                    correlation = rule.get("correlation")

                    if not isinstance(correlation, dict):
                        errors.append(
                            f"{file}: correlation must be a mapping"
                        )
                    elif not isinstance(
                        correlation.get("condition"), dict
                    ):
                        errors.append(
                            f"{file}: correlation.condition "
                            "must be a mapping"
                        )

                    if not isinstance(
                        correlation.get("rules", []) if isinstance(correlation, dict) else [],
                        list,
                    ):
                        errors.append(
                            f"{file}: correlation.rules must be a list"
                        )

                else:
                    detection = rule.get("detection")

                    if not isinstance(detection, dict):
                        errors.append(
                            f"{file}: detection must be a mapping"
                        )
                    elif "condition" not in detection:
                        errors.append(
                            f"{file}: detection.condition is missing"
                        )

            except Exception as error:
                errors.append(f"{file}: YAML parse error: {error}")

    for error in errors:
        print("ERROR:", error)

    print(
        f"Checked {count} YAML files; {len(errors)} issue(s). "
        "This is not a full Sigma specification check."
    )

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
