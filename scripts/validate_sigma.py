"""Basic YAML and metadata validation; use sigma-cli for full Sigma validation."""
import argparse, sys
from pathlib import Path
import yaml
REQUIRED={'title','id','status','description','references','tags','logsource','detection','falsepositives','level'}
CORRELATION_REQUIRED={'title','id','type','correlation','condition','tags','falsepositives','level'}
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--rules',nargs='+',default=['rules']); args=ap.parse_args(); errors=[]; count=0
    for base in args.rules:
        p=Path(base); files=sorted(p.rglob('*.yml')) if p.is_dir() else [p]
        for f in files:
            count+=1
            try:
                d=yaml.safe_load(f.read_text(encoding='utf-8'))
                required=CORRELATION_REQUIRED if (d or {}).get('type')=='correlation' else REQUIRED
                missing=required-set(d or {})
                if missing: errors.append(f'{f}: missing keys {sorted(missing)}')
                if (d or {}).get('type')!='correlation' and not isinstance((d or {}).get('detection'),dict): errors.append(f'{f}: detection must be a mapping')
                if not isinstance((d or {}).get('tags'),list): errors.append(f'{f}: tags must be a list')
            except Exception as e: errors.append(f'{f}: YAML parse error: {e}')
    for e in errors: print('ERROR:',e)
    print(f'Checked {count} YAML files; {len(errors)} issue(s). This is not a full Sigma specification check.')
    return 1 if errors else 0
if __name__=='__main__': sys.exit(main())
