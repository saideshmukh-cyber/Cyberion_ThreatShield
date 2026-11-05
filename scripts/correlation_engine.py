
"""Small synthetic correlation engine for Cyberion ThreatShield.

This is a portfolio test harness, not a production SIEM engine.
It evaluates base Sigma rules against events, then applies time-window
correlation logic defined in the project's correlation YAML files.
"""

from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

import yaml

from scripts.run_rule_tests import evaluate


ROOT = Path(__file__).resolve().parents[1]


def parse_timestamp(value):
    """Parse ISO timestamps and normalize them to UTC."""
    if not isinstance(value, str):
        raise ValueError(f"Timestamp must be a string, got {value!r}")

    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))

    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)

    return parsed.astimezone(timezone.utc)


def get_field(event, field):
    """Read a field, including the host/ComputerName alias."""
    if field in event:
        return event[field]

    aliases = {
        "ComputerName": "host",
        "host": "ComputerName",
    }

    alias = aliases.get(field)

    if alias and alias in event:
        return event[alias]

    return None


def load_rules():
    """Load all YAML rules and index them by UUID."""
    rules = {}

    for path in (ROOT / "rules").rglob("*.yml"):
        rule = yaml.safe_load(path.read_text(encoding="utf-8"))

        if isinstance(rule, dict) and rule.get("id"):
            rules[rule["id"].lower()] = rule

    return rules


def event_matches_referenced_rules(event, referenced_rules, all_rules):
    """Return True if the event matches any referenced base rule."""
    for rule_id in referenced_rules:
        rule = all_rules.get(rule_id.lower())

        if rule is None:
            raise ValueError(f"Referenced rule not found: {rule_id}")

        if rule.get("type") == "correlation":
            raise ValueError(
                "Nested correlation rules are not supported by this harness"
            )

        if evaluate(rule, event):
            return True

    return False


def compare_threshold(value, condition):
    """Evaluate a numeric threshold condition."""
    if "gte" in condition:
        return value >= condition["gte"]

    if "gt" in condition:
        return value > condition["gt"]

    if "lte" in condition:
        return value <= condition["lte"]

    if "lt" in condition:
        return value < condition["lt"]

    raise ValueError(f"Unsupported correlation condition: {condition}")


def evaluate_correlation(correlation_rule, events, all_rules=None):
    """Evaluate one correlation rule against an event sequence.

    Returns a list of alert dictionaries.
    """
    if all_rules is None:
        all_rules = load_rules()

    if correlation_rule.get("type") != "correlation":
        raise ValueError("Expected a Sigma correlation rule")

    config = correlation_rule.get("correlation", {})
    referenced_rules = config.get("rules", [])
    group_fields = config.get("group-by", [])
    condition = config.get("condition", {})
    correlation_type = config.get("type")

    if not referenced_rules:
        raise ValueError("Correlation rule has no referenced base rules")

    if not group_fields:
        raise ValueError("Correlation rule has no group-by fields")

    timespan = config.get("timespan")

    if not isinstance(timespan, str) or len(timespan) < 2:
        raise ValueError(f"Invalid timespan: {timespan!r}")

    unit = timespan[-1]
    amount = int(timespan[:-1])

    units = {
        "s": timedelta(seconds=amount),
        "m": timedelta(minutes=amount),
        "h": timedelta(hours=amount),
        "d": timedelta(days=amount),
    }

    if unit not in units or amount <= 0:
        raise ValueError(f"Unsupported timespan: {timespan}")

    window = units[unit]
    field_for_value_count = condition.get("field")

    matched_events = []

    for event in events:
        if not isinstance(event, dict):
            continue

        if not event_matches_referenced_rules(
            event, referenced_rules, all_rules
        ):
            continue

        try:
            event_time = parse_timestamp(event.get("timestamp"))
        except (ValueError, TypeError):
            # Events with missing/invalid timestamps cannot be correlated.
            continue

        group_values = tuple(
            get_field(event, field) for field in group_fields
        )

        # Avoid combining events whose grouping identity is incomplete.
        if any(value is None for value in group_values):
            continue

        value = None

        if correlation_type == "value_count":
            value = get_field(event, field_for_value_count)

            if value is None:
                continue

        matched_events.append(
            {
                "timestamp": event_time,
                "group": group_values,
                "value": value,
                "event": event,
            }
        )

    matched_events.sort(key=lambda item: item["timestamp"])

    grouped = defaultdict(list)

    for item in matched_events:
        grouped[item["group"]].append(item)

    alerts = []

    for group, group_events in grouped.items():
        for index, current in enumerate(group_events):
            cutoff = current["timestamp"] - window

            window_events = [
                item
                for item in group_events[: index + 1]
                if cutoff <= item["timestamp"] <= current["timestamp"]
            ]

            if correlation_type == "event_count":
                count = len(window_events)

            elif correlation_type == "value_count":
                count = len(
                    {
                        item["value"]
                        for item in window_events
                    }
                )

            else:
                raise ValueError(
                    f"Unsupported correlation type: {correlation_type}"
                )

            if compare_threshold(count, condition):
                alerts.append(
                    {
                        "rule_title": correlation_rule.get("title"),
                        "rule_id": correlation_rule.get("id"),
                        "group": group,
                        "count": count,
                        "timestamp": current["timestamp"].isoformat(),
                        "window": timespan,
                        "event": current["event"],
                    }
                )

    return alerts


def load_jsonl(path):
    """Read JSONL event fixtures."""
    import json

    events = []

    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if line.strip():
            events.append(json.loads(line))

    return events
