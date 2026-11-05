
"""Project-level YAML, metadata, and correlation validation.

This is a custom structural check, not a full Sigma specification validator.
"""
import argparse
import sys
import re
import uuid
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

VALID_CORRELATION_TYPES = {
    "event_count",
    "value_count",
    "temporal",
    "temporal_ordered",
}

VALID_COMPARATORS = {"gte", "gt", "lte", "lt"}
TIMESPAN_PATTERN = re.compile(r"^\d+[smhd]$")


def valid_uuid(value):
    """Return True when value is a valid UUID string."""
    if not isinstance(value, str):
        return False

    try:
        uuid.UUID(value)
        return True
    except (ValueError, AttributeError):
        return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--rules", nargs="+", default=["rules"])
    args = parser.parse_args()

    errors = []
    count = 0
    parsed_rules = []
    seen_ids = {}

    # First pass: parse files and collect IDs.
    for base in args.rules:
        path = Path(base)
        files = sorted(path.rglob("*.yml")) if path.is_dir() else [path]

        for file in files:
            count += 1

            try:
                rule = yaml.safe_load(file.read_text(encoding="utf-8"))
            except Exception as error:
                errors.append(f"{file}: YAML parse error: {error}")
                continue

            if not isinstance(rule, dict):
                errors.append(f"{file}: YAML document must be a mapping")
                continue

            parsed_rules.append((file, rule))

            rule_id = rule.get("id")

            if not valid_uuid(rule_id):
                errors.append(
                    f"{file}: id must be a valid UUID; got {rule_id!r}"
                )
            else:
                normalized_id = str(uuid.UUID(rule_id))

                if normalized_id in seen_ids:
                    errors.append(
                        f"{file}: duplicate UUID {rule_id}; "
                        f"also used in {seen_ids[normalized_id]}"
                    )
                else:
                    seen_ids[normalized_id] = file

    # Second pass: validate metadata and correlation references.
    known_ids = set(seen_ids)

    for file, rule in parsed_rules:
        is_correlation = rule.get("type") == "correlation"

        required = (
            CORRELATION_REQUIRED if is_correlation else REQUIRED
        )

        missing = required - set(rule)
        if missing:
            errors.append(f"{file}: missing keys {sorted(missing)}")

        if not isinstance(rule.get("tags"), list):
            errors.append(f"{file}: tags must be a list")

        if is_correlation:
            correlation = rule.get("correlation")

            if not isinstance(correlation, dict):
                errors.append(
                    f"{file}: correlation must be a mapping"
                )
                continue

            correlation_type = correlation.get("type")
            if correlation_type not in VALID_CORRELATION_TYPES:
                errors.append(
                    f"{file}: unsupported correlation.type "
                    f"{correlation_type!r}"
                )

            references = correlation.get("rules")

            if not isinstance(references, list) or not references:
                errors.append(
                    f"{file}: correlation.rules must be a non-empty list"
                )
            else:
                for reference in references:
                    if not valid_uuid(reference):
                        errors.append(
                            f"{file}: correlation rule reference "
                            f"must be a UUID; got {reference!r}"
                        )
                    elif str(uuid.UUID(reference)) not in known_ids:
                        errors.append(
                            f"{file}: correlation references unknown "
                            f"rule UUID {reference}"
                        )

            group_by = correlation.get("group-by")
            if not isinstance(group_by, list) or not group_by:
                errors.append(
                    f"{file}: correlation.group-by "
                    "must be a non-empty list"
                )
            elif not all(
                isinstance(field, str) and field.strip()
                for field in group_by
            ):
                errors.append(
                    f"{file}: correlation.group-by entries "
                    "must be non-empty strings"
                )

            timespan = correlation.get("timespan")
            if (
                not isinstance(timespan, str)
                or not TIMESPAN_PATTERN.fullmatch(timespan)
            ):
                errors.append(
                    f"{file}: correlation.timespan must use "
                    "a format such as 5m, 1h, or 30s"
                )

            condition = correlation.get("condition")
            if not isinstance(condition, dict):
                errors.append(
                    f"{file}: correlation.condition must be a mapping"
                )
            else:
                comparator_keys = VALID_COMPARATORS.intersection(condition)

                if not comparator_keys:
                    errors.append(
                        f"{file}: correlation.condition must include "
                        "one of gte, gt, lte, or lt"
                    )

                for key in comparator_keys:
                    threshold = condition[key]

                    if (
                        isinstance(threshold, bool)
                        or not isinstance(threshold, (int, float))
                        or threshold <= 0
                    ):
                        errors.append(
                            f"{file}: correlation.condition.{key} "
                            "must be a positive number"
                        )

                if correlation_type == "value_count":
                    field = condition.get("field")

                    if not isinstance(field, str) or not field.strip():
                        errors.append(
                            f"{file}: value_count condition "
                            "requires a non-empty field"
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

    for error in errors:
        print("ERROR:", error)

    print(
        f"Checked {count} YAML files; {len(errors)} issue(s). "
        "This is not a full Sigma specification check."
    )

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
