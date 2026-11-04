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
