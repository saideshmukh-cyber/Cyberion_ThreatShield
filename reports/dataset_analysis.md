# Dataset Analysis — EVTX-ATTACK-SAMPLES

## 1. Dataset Overview

This project uses the public EVTX-ATTACK-SAMPLES dataset for Windows security event analysis and detection engineering.

- **Dataset:** EVTX-ATTACK-SAMPLES
- **Repository:** https://github.com/sbousseaden/EVTX-ATTACK-SAMPLES
- **Local path:** `data/raw/EVTX-ATTACK-SAMPLES/`
- **Dataset commit:** `4ceed2f4706daf601c212a8f91c113dd85349a2c`
- **Download date:** 2026-11-04
- **Number of EVTX files:** 278
- **Inventory:** `reports/dataset_inventory.csv`
- **Inventory report:** `reports/dataset_inventory.md`

## 2. Dataset Distribution

| Category | EVTX Files |
|---|---:|
| Privilege Escalation | 66 |
| Lateral Movement | 47 |
| Credential Access | 39 |
| Defense Evasion | 36 |
| Execution | 34 |
| Persistence | 22 |
| Discovery | 11 |
| Command and Control | 6 |
| Other | 2 |
| Other/emotet | 6 |
| AutomatedTestingTools | 3 |
| AutomatedTestingTools/Malware | 5 |
| Root directory | 1 |
| **Total** | **278** |

The dataset contains samples categorized by attack behavior and testing tools. The categories provide a starting point for selecting logs for detection engineering and threat hunting.

## 3. Collection and Inventory Methodology

The dataset was cloned from its public GitHub repository using the project's download script.

A Python inventory script recursively searched for `.evtx` files and recorded:

- File name
- Relative path
- Parent folder
- File size in bytes
- File size in megabytes

The inventory was saved as CSV and Markdown for reproducibility.

## 4. Initial Observations

The largest file categories are:

1. Privilege Escalation
2. Lateral Movement
3. Credential Access
4. Defense Evasion
5. Execution

These categories will guide the initial selection of logs for event analysis.

**These observations describe dataset organization only. They do not establish that attacks were detected, successful, or malicious in a real environment.**

## 5. Analysis Status

| Activity | Status |
|---|---|
| Dataset download | Completed |
| Dataset commit recorded | Completed |
| EVTX file inventory | Completed |
| Dataset category distribution | Completed |
| Event-level parsing | Pending |
| Event field analysis | Pending |
| Detection rule testing against dataset | Pending |
| False-positive evaluation | Pending |
| Evidence-backed hunt findings | Pending |

## 6. Next Steps

1. Select an EVTX parsing tool.
2. Extract event records into a structured format.
3. Identify relevant Windows event IDs and fields.
4. Map observed events to applicable Sigma rules.
5. Record evidence using source file names and event record identifiers.
6. Document findings only after validating the underlying event data.

## 7. Limitations

The inventory does not include event-level analysis. File categories reflect the dataset's organization and should not be treated as verified ATT&CK mappings or confirmed attack outcomes.

The dataset is a collection of attack-related samples, not a representative sample of ordinary enterprise activity. Detection results and false-positive rates must not be generalized to production environments without additional validation.
