# Dataset acquisition — next required step

The PRD specifies publicly documented security datasets or telemetry collected in a controlled lab. Do not treat the synthetic fixtures in this repository as satisfying that requirement.

## Candidate sources to review
- **EVTX-ATTACK-SAMPLES**: public Windows event-log samples mapped to attack techniques. Check the repository's current license and sample-specific provenance before use.
- **Splunk Boss of the SOC (BOTS)**: public security investigation datasets; review dataset release, terms, and download requirements.
- **Mordor / Open Threat Research Forge**: pre-recorded adversary emulation datasets; verify current availability and licensing.
- **Atomic Red Team**: optional authorized lab test framework for generating telemetry on a lab VM. Run only in a disposable, isolated environment with permission; some tests alter system state.

## Dataset register
For each chosen source, fill in `reports/dataset_register.csv`: URL/citation, dataset/release, acquisition date, license/terms, SHA-256, event types, time range, relevant ATT&CK techniques, known limitations, and transformation steps.

## Safe handling
1. Download only from the official project/source page.
2. Read the license and handling requirements before redistribution.
3. Store raw data locally in `data/raw/` (ignored by Git by default).
4. Generate a hash: PowerShell `Get-FileHash .\dataaw\yourfile -Algorithm SHA256`; macOS/Linux `sha256sum data/raw/yourfile`.
5. Never run Atomic Red Team tests on a production or personal daily-use host. Use a disposable lab VM, snapshots, and explicit authorization.
6. Do not commit private logs, credentials, personal data, or large third-party datasets to GitHub.
