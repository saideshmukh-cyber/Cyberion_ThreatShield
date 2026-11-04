# Case 001 — Potential credential-access activity

**Classification:** Illustrative case template — not a confirmed incident.

## Summary
Investigate an alert indicating a process accessed LSASS with potentially sensitive access rights.

## Evidence needed
- Endpoint process-access event with event ID and timestamp
- Source process image, command line, parent, signer/hash, user, and host
- EDR telemetry or other corroborating source where available
- Analyst query and stable evidence references

## Timeline
| Time (UTC) | Evidence ID | Observation | ATT&CK mapping |
|---|---|---|---|
| TBD | TBD | Populate from real authorized telemetry | T1003.001 |

## Root cause and impact
Not assessed; evidence not supplied.

## Response
Use `reports/playbooks/credential_compromise.md` if corroborated. Preserve evidence, assess exposure, and follow organizational authorization and escalation requirements.

## Closure
Do not classify as true positive until corroborated. Record false positive / benign positive / true positive / inconclusive with justification and evidence IDs.
