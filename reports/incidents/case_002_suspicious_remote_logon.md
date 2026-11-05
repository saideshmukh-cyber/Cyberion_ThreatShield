# Incident Case 002 — Unusual Remote Interactive Logon

**Case ID:** CDL-IR-002  
**Classification:** Illustrative investigation template  
**Status:** Pending real telemetry  
**Not a confirmed incident**

## 1. Executive Summary

This case documents an investigation workflow for a potentially unusual remote interactive logon.

A successful remote logon may be legitimate administration, authorized remote support, or suspicious access. The classification depends on account, source, destination, time, authentication context, and corroborating activity.

No specific remote-logon event has been provided for this case. Therefore, this document is an investigation template rather than a confirmed incident report.

## 2. Scope and Evidence Status

**Current evidence status:** No verified event record supplied.

Before treating this as an observed case, obtain:

- Original event log or authorized telemetry source.
- Event ID and record ID.
- Timestamp and timezone.
- Source address and destination host.
- Account and logon type.
- Relevant identity-provider or MFA evidence, if available and authorized.
- Related process or network activity.

Do not invent timestamps, IP addresses, usernames, hostnames, or event identifiers.

## 3. Detection Context

Potential detection rule:

`Remote Interactive Logon (RDP)`

- **Rule location:** `rules/windows/remote_logon_rdp.yml`
- **Potential ATT&CK mapping:** T1021.001 — Remote Services: Remote Desktop Protocol

The rule identifies remote interactive logon behavior. It does not establish maliciousness by itself.

## 4. Investigation Hypothesis

A remote interactive logon may represent unauthorized access if it originates from an unusual source, uses an unexpected account, occurs outside normal activity, or is followed by suspicious actions.

**Hypothesis:** A remote interactive logon may indicate unauthorized remote access if surrounding evidence supports that interpretation.

This hypothesis remains untested until real telemetry is analyzed.

## 5. Evidence and Timeline

| Time (UTC) | Evidence reference | Observation | Verification |
|---|---|---|---|
| TBD | Original event record required | Remote interactive logon | Pending |
| TBD | Authentication context required | Account, source, destination, and logon details | Pending |
| TBD | Corroborating telemetry required | Related process or network activity | Pending |

Populate this table only from verified records.

## 6. Investigation Procedure

1. Verify event provider, channel, event ID, timestamp, host, and account.
2. Confirm the logon type and remote-access context.
3. Validate source address and destination host.
4. Check whether the account, source, and timing are expected.
5. Review authorized MFA and identity-provider logs when available.
6. Examine nearby process, service, and network events.
7. Determine whether the activity is legitimate administration, suspicious activity, or inconclusive.
8. Preserve evidence and record the source file and event record identifiers.

## 7. ATT&CK Mapping

Potential mapping:

- **T1021.001 — Remote Services: Remote Desktop Protocol**

Use this mapping only if the actual event and investigative context support RDP activity.

## 8. Root Cause and Impact

**Root cause:** Not established.

**Impact:** Not assessed.

Do not claim lateral movement, account compromise, data access, or persistence without supporting evidence.

## 9. Response Recommendations

If unauthorized remote access is corroborated:

- Follow `reports/playbooks/lateral_movement.md`.
- Preserve authentication and endpoint evidence.
- Assess affected accounts and hosts.
- Apply containment and credential actions under approved organizational policy.
- Escalate according to incident severity and business impact.

These are proposed response steps, not actions already performed.

## 10. Closure Criteria

Do not close this case as a true positive until the underlying event and relevant context are verified.

Record the final classification as one of:

- True positive
- Benign positive
- False positive
- Inconclusive
- Not observed in analyzed dataset

Include evidence references, justification, and remaining limitations.

**Current conclusion:** No confirmed incident. This report remains an investigation template pending telemetry.