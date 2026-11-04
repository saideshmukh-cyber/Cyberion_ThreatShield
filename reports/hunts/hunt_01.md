# Threat Hunt 01 — Repeated Authentication Failures

**Status:** Hunt hypothesis / pending telemetry validation  
**Dataset:** EVTX-ATTACK-SAMPLES  
**ATT&CK mapping:** Credential Access / Brute Force (confirm exact technique and sub-technique before finalizing)

## 1. Hunt objective
Identify repeated failed authentication attempts that may indicate password guessing, while distinguishing attack-like bursts from benign causes such as mistyped credentials or service accounts.

## 2. Hypothesis
A source host or source IP generating a high volume of failed logons against one or more accounts within a short time window may indicate password guessing.

## 3. Data sources and prerequisites
- Windows Security logs, commonly including failed-logon Event ID 4625.
- Required fields must be verified in the parsed sample: timestamp, source address, account, logon type, host, and status/substatus where available.
- Record the actual file names and parser output used.

## 4. Hunt logic (conceptual)
Group failed logon events by source and time window. Review:
- failure count and distinct targeted accounts;
- whether successes follow the failures;
- logon type and target host;
- known service accounts or test activity.

**Do not report a positive hunt result until you have run this against the actual data.**

## 5. Evidence table
| Timestamp | Source file | Event record ID | Source IP/host | Account | Event ID | Evidence |
|---|---|---|---|---|---:|---|
| **[populate from parsed event]** | | | | | | |

## 6. Results
- Events reviewed: **[count]**
- Candidate clusters: **[count]**
- Confirmed suspicious clusters: **[count; explain evidence]**
- Benign/uncertain clusters: **[count; explain]**

## 7. False-positive considerations
- Users mistyping passwords.
- Shared NAT/VPN egress.
- Service accounts with expired passwords.
- Vulnerability scanners or authorized testing.
- Logon failures caused by policy or configuration.

## 8. Conclusion
**Pending execution.** If no qualifying cluster exists in the selected sample, state that no candidate was observed in this sample; do not generalize to production.
