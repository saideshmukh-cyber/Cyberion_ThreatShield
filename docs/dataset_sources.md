# Dataset Sources and Provenance

## Primary dataset: EVTX-ATTACK-SAMPLES

| Field | Value |
|---|---|
| Name | EVTX-ATTACK-SAMPLES / Windows Events Attack Samples |
| Maintainer | `sbousseaden` (upstream GitHub repository) |
| Source | https://github.com/sbousseaden/EVTX-ATTACK-SAMPLES |
| Format | Windows Event Log `.evtx` |
| Purpose | Detection engineering, DFIR practice, and ATT&CK-related telemetry familiarization |
| Upstream license | GPL-3.0; verify the repository's current license before reuse |
| Download method | `bash scripts/download_dataset.sh` from Git Bash |
| Local path | `data/raw/EVTX-ATTACK-SAMPLES/` |
| Analysis status | Not yet locally parsed by this documentation pack |

## Dataset caveats
- This is a collection of attack-related sample logs, not a continuous enterprise baseline.
- Folder/file labels can indicate the intended technique, but are not proof that a detector correctly identifies the behavior.
- The dataset may not contain every event type or field needed by each rule.
- Any reported count, hit rate, precision, or recall must be calculated from the actual local files and documented query/parser version.
- Do not publish raw `.evtx` files in the project repository unless you have reviewed the license and redistribution terms.

## Reproducibility checklist
- [ ] Dataset cloned successfully.
- [ ] Record the actual commit: `git -C data/raw/EVTX-ATTACK-SAMPLES rev-parse HEAD`
- [ ] Record download date.
- [ ] Record parser/tool versions.
- [ ] Record exactly which files were analyzed.
- [ ] Save scripts and commands used for analysis.
