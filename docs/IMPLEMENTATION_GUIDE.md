# Implementation guide — from zero to tested project

## Phase 1 — Create the folder
Download/extract the ZIP, then open the `cyberion-detection-engineering` folder in VS Code. In VS Code choose **Terminal → New Terminal**. Confirm `README.md`, `requirements.txt`, `rules/`, `scripts/`, and `tests/` are visible.

## Phase 2 — Create and activate a virtual environment
Windows PowerShell:
```powershell
py -3.11 -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```
macOS/Linux:
```bash
python3.11 -m venv .venv
source .venv/bin/activate
```
The terminal prompt should show `(.venv)`. This environment isolates Python packages for this project.

## Phase 3 — Install dependencies
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```
If `pip` fails, check Python version with `python --version` and ensure the virtual environment is active.

## Phase 4 — Run automated tests
```bash
python -m pytest -q
```
Expected: all tests pass. If not, copy the full error output and troubleshoot before continuing.

## Phase 5 — Run the local rule smoke test
```bash
python scripts/run_rule_tests.py --events data/sample/events.jsonl --rules rules/windows rules/linux rules/network --output reports/sample_test_results.json
```
Expected: a per-rule match count. These are synthetic fixtures, not real detection performance. Open `reports/sample_test_results.json` to inspect output.

## Phase 6 — Validate YAML metadata
```bash
python scripts/validate_sigma.py --rules rules
```
For full Sigma validation, install sigma-cli using its current official installation instructions, then run `sigma check` (verify the command's behavior against your installed version). Correlation rules need a backend supporting Sigma correlation rules; the local harness skips them.

## Phase 7 — Acquire real dataset and document it
Read `docs/DATASET_ACQUISITION.md`. Pick one dataset you are permitted to use. Do not download data into Git-tracked paths. Save it under `data/raw/`, hash it, and update `reports/dataset_register.csv`. Build a source-specific normalizer and record all mappings. Update the tests to use actual event fields. Do not call the engagement complete until real-data validation and false-positive tuning are documented.

## Phase 8 — Finish the PRD deliverables
- Review every Sigma rule's source fields, technique ID, severity, and benign triggers.
- Complete at least three false-positive tuning records with observed scenario, logic change, and trade-off.
- Run two hunts and record hypotheses, methods, results (including negative findings), and evidence IDs.
- Complete two incident reports only where evidence supports a case; otherwise document clearly labeled exercises/case studies, not real incidents.
- Review all three playbooks for trigger, investigation, containment, eradication/recovery, and communications.
- Update ATT&CK matrix statuses from evidence, not assumptions.
- Complete executive summary and final presentation after results exist.

## Phase 9 — Git and GitHub
Follow `docs/GITHUB_AND_DEPLOYMENT.md`. Never add raw telemetry or secrets. Deployment of a website is not required by the PRD; the project is a repository of research artifacts. Optional GitHub Pages can publish Markdown only after removing sensitive data and ensuring dataset licenses permit publication.
