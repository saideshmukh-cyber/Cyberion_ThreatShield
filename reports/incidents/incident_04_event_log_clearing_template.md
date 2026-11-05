# Incident Case 02 — Security Event Log Cleared (Evidence-Limited Case)

**Case type:** Dataset-driven case only after event verification; otherwise mark as simulated  
**Status:** Pending local dataset validation

## 1. Case summary
Investigate a Security Event Log clearing event (commonly Event ID 1102) if one is present in the selected telemetry. Event ID and context must be verified in the actual log.

## 2. Alert / trigger
- Rule: Security Event Log Cleared (rule ID `66cbb0dc-6bdb-5e3d-a490-639942a6dd92`)
- Trigger: **[record only after event is found]**
- Source file and record ID: **[required]**

## 3. Timeline
| Time | Event | Source file / record ID | Verified? |
|---|---|---|---|
| | Log-clearing event | | Pending |
| | Nearby logon/process events | | Pending |
| | Analyst triage | | Pending |

## 4. Investigation checklist
- Verify event provider, channel, Event ID, timestamp, host, and subject account.
- Determine whether the action was authorized maintenance or suspicious activity.
- Examine surrounding logon, process, service, and administrative events.
- Assess logging gaps and whether other telemetry sources remain available.
- Preserve evidence and note limitations.

## 5. Root cause
**Pending evidence.** Do not infer an attacker or motive from Event ID 1102 alone.

## 6. Impact
**Pending evidence.** State what logs were cleared and what visibility was lost only if supported.

## 7. ATT&CK mapping
Potential mapping: **Indicator Removal: Clear Windows Event Logs (T1070.001)**. Confirm current ATT&CK mapping and evidence before finalizing.

## 8. Evidence traceability
| Evidence ID | Source file | Event record ID | Field(s) | Supports |
|---|---|---|---|---|
| | | | | |

## 9. Response and closure
Document containment, recovery, notification, and closure only after an evidence-based case review. If no event is found in the chosen dataset subset, record “not observed in analyzed subset” rather than claiming the technique is absent.
