# Incident Case 001 — Potential LSASS Credential Access

**Case ID:** CDL-IR-001  
**Classification:** Historical controlled-sample analysis  
**Status:** Evidence observed; broader incident context unavailable  
**Environment:** Publicly available historical attack sample  
**Not a live incident or production compromise**

## 1. Executive Summary

This case documents Sysmon process-access events targeting the Local Security Authority Subsystem Service (LSASS) in a historical controlled attack sample associated with Mimikatz credential-dumping activity.

The analyzed sample, `babyshark_mimikatz_powershell.evtx`, contains two relevant Sysmon Event ID 10 records. Both report LSASS as the target process and a `GrantedAccess` value of `0x1010`.

These observations are consistent with potential LSASS memory access associated with credential dumping. They do not, by themselves, establish successful credential extraction, account compromise, or impact beyond the sample.

## 2. Scope and Data Source

- **Dataset:** `babyshark_mimikatz_powershell.evtx`
- **Log source:** Sysmon
- **Event type:** Event ID 10 — Process Access
- **Sample context:** Historical controlled attack telemetry
- **Analysis scope:** Two relevant process-access records identified in the dataset

The sample is historical and does not represent telemetry from a live organization.

## 3. Detection Context

The investigation relates to the Sigma rule:

`Potential LSASS Credential Dumping via Process Access`

- **Rule file:** `rules/windows/windows_lsass_access.yml`
- **ATT&CK technique:** T1003.001 — LSASS Memory
- **Detection behavior:** Process-access events targeting LSASS with selected access masks
- **Rule status:** Experimental

The access-mask selection is heuristic. A match indicates suspicious behavior requiring investigation, not definitive proof of credential dumping.

## 4. Evidence and Timeline

| Evidence reference | Event ID | Record ID | Timestamp | Target process | GrantedAccess |
|---|---:|---:|---|---|---|
| Historical sample record A | 10 | 22 | 2019-04-18 (exact time in source EVTX) | LSASS | `0x1010` |
| Historical sample record B | 10 | 30 | 2019-04-18 (exact time in source EVTX) | LSASS | `0x1010` |

**Evidence interpretation:** Both records are consistent with the rule’s selected LSASS-access conditions.

The exact source-process details, command line, parent process, signer, hash, and user context should be added only if verified from the original event records.

## 5. Investigation

The analysis identified:

1. Sysmon Event ID 10 process-access records.
2. LSASS as the target process.
3. `GrantedAccess` value `0x1010` in both records.
4. Historical dataset context associated with credential-dumping activity.

Additional investigation in a real environment would include:

- Source process image, hash, signer, and command line.
- Parent process and process ancestry.
- User and host context.
- Nearby process creation and authentication events.
- EDR or endpoint telemetry corroboration.
- Whether the access was performed by an authorized security or diagnostic tool.

## 6. ATT&CK Mapping

- **T1003.001 — OS Credential Dumping: LSASS Memory**

This mapping describes the behavior under investigation. It does not independently prove successful credential extraction.

## 7. Root Cause and Impact

**Root cause:** Not established from the available event records.

**Impact:** Not assessed. The analyzed records do not establish whether credentials were successfully extracted, reused, or exposed.

No production-system impact or affected organization is identified.

## 8. Response Recommendations

For a real environment, follow `reports/playbooks/credential_compromise.md` and applicable organizational procedures.

Recommended actions:

- Preserve original event records and relevant endpoint telemetry.
- Validate the source process and its legitimacy.
- Investigate related authentication activity.
- Determine whether credential exposure is supported by corroborating evidence.
- Escalate and contain only according to approved incident-response procedures.

These are recommendations, not actions performed against the historical sample.

## 9. Closure

**Disposition:** Historical controlled-sample detection analysis completed.

The sample contains two records consistent with the LSASS-access detection logic. The evidence supports a potential credential-access finding within the historical sample, but not a claim of successful credential theft or live compromise.

**Limitations:** Historical data, limited event subset, no live endpoint context, and no independent production impact assessment.