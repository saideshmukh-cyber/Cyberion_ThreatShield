import csv
from pathlib import Path
p=Path('reports/coverage_matrix.csv')
with p.open(newline='',encoding='utf-8') as f: rows=list(csv.DictReader(f))
print(f'ATT&CK matrix entries: {len(rows)}')
for status in sorted({r['coverage_status'] for r in rows}): print(f"{status}: {sum(r['coverage_status']==status for r in rows)}")
print('Reminder: do not change to Tested/covered until dataset-backed test evidence is recorded.')
