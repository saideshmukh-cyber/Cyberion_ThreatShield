"""Evaluate a deliberately small Sigma subset against JSONL fixtures.
This is a smoke-test harness, not a full Sigma/pySigma implementation.
"""
import argparse, json, sys
from pathlib import Path
import yaml

def values_match(event, field_expr, expected):
    parts=field_expr.split('|')
    field=parts[0]; modifiers=parts[1:]
    actual=event.get(field)
    candidates=expected if isinstance(expected,list) else [expected]
    if actual is None: return False
    for candidate in candidates:
        a=str(actual).lower(); e=str(candidate).lower()
        ok = (e in a if 'contains' in modifiers else a.endswith(e) if 'endswith' in modifiers else float(actual) >= float(candidate) if 'gte' in modifiers else actual == candidate or a == e)
        if ok: return True
    return False

def evaluate(rule,event):
    det=rule.get('detection',{})
    condition=str(det.get('condition','')).strip()
    selections={k:v for k,v in det.items() if k!='condition'}
    matched={}
    for name,sel in selections.items():
        if not isinstance(sel,dict): return False
        matched[name]=all(values_match(event,field,value) for field,value in sel.items())
    # Support selection names joined by `and`/`or`, or a single selection.
    import re
    if condition in matched: return matched[condition]
    tokens=re.split(r'\s+(and|or)\s+',condition)
    if len(tokens)>1:
        result=matched.get(tokens[0],False)
        for i in range(1,len(tokens),2):
            op=tokens[i]; rhs=matched.get(tokens[i+1],False)
            result=(result and rhs) if op=='and' else (result or rhs)
        return result
    return False

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--events',required=True); ap.add_argument('--rules',nargs='+',required=True); ap.add_argument('--output'); args=ap.parse_args()
    events=[json.loads(line) for line in Path(args.events).read_text(encoding='utf-8').splitlines() if line.strip()]
    rule_files=[]
    for base in args.rules:
        p=Path(base)
        rule_files.extend(sorted(p.rglob('*.yml')) if p.is_dir() else [p])
    results=[]
    for path in rule_files:
        rule=yaml.safe_load(path.read_text(encoding='utf-8'))
        if rule.get('type')=='correlation': continue
        matched=[e for e in events if evaluate(rule,e)]
        results.append({'rule':rule.get('title',path.name),'rule_id':rule.get('id'),'matches':len(matched),'events':[e.get('event_id',e.get('timestamp','unknown')) for e in matched]})
    for row in results: print(f"{row['matches']:>3} match(es) | {row['rule']} | events={row['events']}")
    if args.output: Path(args.output).write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8')
    print(f"\nEvaluated {len(results)} single-event rules against {len(events)} synthetic events. Correlation rules are not evaluated.")
    return 0
if __name__=='__main__': sys.exit(main())
