# IR Playbook 01 — Suspicious PowerShell Execution

## Trigger
A high-confidence alert or analyst report involving suspicious PowerShell execution. A single encoded command is a triage lead, not proof of compromise.

## 1. Triage
- Record alert ID, host, user, timestamp, process image, command line, parent process, and detection rule.
- Confirm telemetry source and event integrity.
- Determine whether the activity matches approved administration or software deployment.

## 2. Investigation
- Review process ancestry and neighboring process events.
- Check script/command context, file paths, signatures, hashes, and network connections where available.
- Identify affected host/user scope.
- Preserve relevant logs and evidence metadata.

## 3. Containment
- Follow incident policy and obtain required authorization.
- Isolate the endpoint if risk justifies it and business impact is understood.
- Disable or restrict compromised accounts only when evidence supports compromise.

## 4. Eradication
- Remove confirmed malicious scripts, files, tasks, or persistence.
- Do not delete artifacts before preservation and approval.

## 5. Recovery
- Restore from trusted sources if needed.
- Re-enable connectivity after validation.
- Monitor for recurrence.

## 6. Communications
- Notify SOC/IR lead, system owner, and relevant stakeholders according to severity and policy.
- Use factual language; separate confirmed facts from hypotheses.

## 7. Closure criteria
- Scope documented.
- Evidence preserved.
- Root cause or unresolved uncertainty recorded.
- Recovery validated.
- Detection tuning/action items assigned.

## 8. References
- Internal rule: PowerShell Encoded Command Execution.
- ATT&CK: PowerShell T1059.001 (verify current mapping).
