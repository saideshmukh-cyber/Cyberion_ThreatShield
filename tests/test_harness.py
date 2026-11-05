import json
from pathlib import Path
import yaml
from scripts.run_rule_tests import evaluate
ROOT=Path(__file__).resolve().parents[1]
def test_sample_file_is_valid_jsonl():
    rows=[json.loads(x) for x in (ROOT/'data/sample/events.jsonl').read_text().splitlines() if x.strip()]
    assert len(rows)>=10
    assert all(isinstance(r,dict) for r in rows)
def test_powershell_encoded_rule_matches_fixture():
    rule=yaml.safe_load((ROOT/'rules/windows/powershell_encoded_command.yml').read_text())
    event=json.loads((ROOT/'data/sample/events.jsonl').read_text().splitlines()[0])
    assert evaluate(rule,event)
def test_powershell_rule_does_not_match_benign_non_encoded_command():
    rule=yaml.safe_load((ROOT/'rules/windows/powershell_encoded_command.yml').read_text())
    event={'Image':r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe','CommandLine':'powershell.exe Get-Process'}
    assert not evaluate(rule,event)
def test_all_rule_yaml_parses_and_has_metadata():
    for p in (ROOT/'rules').rglob('*.yml'):
        d=yaml.safe_load(p.read_text())
        assert d['title'] and d['id'] and d['description']
        assert d['tags']
def test_correlation_rules_are_marked_correlation():
    files=list((ROOT/'rules/correlation').glob('*.yml'))
    assert len(files)>=3
    assert all(yaml.safe_load(p.read_text()).get('type')=='correlation' for p in files)


def test_large_outbound_threshold_matches_fixture():
    rule=yaml.safe_load((ROOT/'rules/network/large_outbound_transfer.yml').read_text())
    events=[json.loads(x) for x in (ROOT/'data/sample/events.jsonl').read_text().splitlines()]
    event=next(e for e in events if e.get('bytes_out',0)>100000000)
    assert evaluate(rule,event)


def test_rule_ids_are_valid_and_unique():
    import uuid

    ids = []

    for path in (ROOT / "rules").rglob("*.yml"):
        rule = yaml.safe_load(path.read_text(encoding="utf-8"))
        rule_id = rule.get("id")

        assert isinstance(rule_id, str), f"{path}: id must be a string"
        uuid.UUID(rule_id)
        ids.append(rule_id.lower())

    assert len(ids) == len(set(ids)), "Duplicate rule UUIDs found"


def test_correlation_references_resolve_to_existing_rules():
    all_rules = {}

    for path in (ROOT / "rules").rglob("*.yml"):
        rule = yaml.safe_load(path.read_text(encoding="utf-8"))
        all_rules[rule["id"].lower()] = rule

    correlation_files = list(
        (ROOT / "rules/correlation").glob("*.yml")
    )

    assert correlation_files

    for path in correlation_files:
        rule = yaml.safe_load(path.read_text(encoding="utf-8"))
        references = rule["correlation"]["rules"]

        assert references, f"{path}: no referenced rules"

        for reference in references:
            assert reference.lower() in all_rules, (
                f"{path}: unresolved correlation reference {reference}"
            )


def test_correlation_rules_have_valid_structure():
    valid_types = {
        "event_count",
        "value_count",
        "temporal",
        "temporal_ordered",
    }

    for path in (ROOT / "rules/correlation").glob("*.yml"):
        rule = yaml.safe_load(path.read_text(encoding="utf-8"))
        correlation = rule["correlation"]

        assert correlation["type"] in valid_types
        assert isinstance(correlation["rules"], list)
        assert correlation["rules"]
        assert isinstance(correlation["group-by"], list)
        assert correlation["group-by"]
        assert isinstance(correlation["timespan"], str)
        assert isinstance(correlation["condition"], dict)

        condition = correlation["condition"]
        assert any(
            key in condition for key in ("gte", "gt", "lte", "lt")
        )

        if correlation["type"] == "value_count":
            assert isinstance(condition.get("field"), str)
            assert condition["field"].strip()


def test_correlation_rules_are_not_claimed_as_evaluated():
    """The current fixture harness does not execute correlation logic."""
    source = (ROOT / "scripts/run_rule_tests.py").read_text(
        encoding="utf-8"
    )

    assert "Correlation rules are not evaluated" in source
