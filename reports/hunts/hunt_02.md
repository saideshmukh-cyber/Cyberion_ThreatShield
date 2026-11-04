# Threat Hunt 02 — Persistence and Scheduled Task Activity

**Status:** Hunt hypothesis / pending telemetry validation  
**Dataset:** EVTX-ATTACK-SAMPLES

## 1. Objective
Look for scheduled-task creation or modification activity that could indicate persistence, and correlate it with process/user context when available.

## 2. Hypothesis
Unexpected scheduled-task creation, especially by unusual users or alongside suspicious command lines, may indicate persistence.

## 3. Data sources
- Windows Security event logs and/or Task Scheduler operational logs.
- Security Event ID 4698 may be relevant where auditing is enabled; validate actual dataset coverage.
- Process creation telemetry can provide supporting context but is not guaranteed in every file.

## 4. Hunt steps
1. Inventory relevant event IDs and channels in the actual data.
2. Extract task name, subject user, timestamp, host, and task content if available.
3. Identify unusual task names, execution paths, or account context.
4. Correlate with nearby process creation or logon events.
5. Compare candidates against known administrative activity only when supporting context exists.

## 5. Evidence
| Timestamp | File / record ID | Host | User | Task name | Command/action | Assessment |
|---|---|---|---|---|---|---|
| **[populate from actual event]** | | | | | | |

## 6. Results
- Relevant events found: **[count]**
- Candidates reviewed: **[count]**
- Confirmed/likely suspicious: **[count and rationale]**
- Benign/uncertain: **[count and rationale]**

## 7. Limitations
- Auditing may not be enabled in every sample.
- Event fields vary by provider and Windows version.
- A task creation event alone does not establish malicious intent.

## 8. Conclusion
**Pending execution.** Record no finding if no evidence is observed.
