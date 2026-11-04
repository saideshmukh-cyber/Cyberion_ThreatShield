# MITRE ATT&CK Mapping

## Mapping principles
- Map behavior to the most specific technique supported by evidence.
- A rule title or dataset folder name alone is not sufficient evidence of technique execution.
- Distinguish a detection's intended behavior from an observed event.
- Record ATT&CK version/date used when finalizing the project.

## Detection rule mapping matrix
| Rule | ATT&CK tactic | Technique ID | Technique name | Evidence / rationale | Confidence |
|---|---|---|---|---|---|
| Defender Real-time Monitoring Disabled | Defense Evasion | **[verify]** | **[verify]** | Rule behavior and telemetry | Pending |
| Repeated Failed Logons | Credential Access | **[verify]** | **[verify]** | Authentication failures alone may be ambiguous | Pending |
| Local User Account Created | Persistence / Privilege Escalation | **[verify]** | **[verify]** | Depends on account context | Pending |
| New Windows Service Installation | Persistence | **[verify]** | **[verify]** | Service install telemetry | Pending |
| PowerShell Encoded Command Execution | Execution | T1059.001 | PowerShell | Command-line evidence; verify behavior | Medium |
| Executable Launched from User Temp Directory | Execution | **[verify]** | **[verify]** | Path-based heuristic | Pending |
| Remote Interactive Logon (RDP) | Lateral Movement | **[verify]** | **[verify]** | RDP logon alone may be legitimate | Pending |
| Scheduled Task Created | Persistence | **[verify]** | **[verify]** | Task creation context | Pending |
| Security Event Log Cleared | Defense Evasion | T1070.001 | Clear Windows Event Logs | Confirm event/context | Medium |
| PowerShell Download Cradle | Command and Control / Execution | **[verify]** | **[verify]** | Download command does not prove C2 | Pending |
| Potential LSASS Process Access | Credential Access | **[verify]** | **[verify]** | Process access is a signal, not proof of dumping | Pending |
| Linux SSH Authentication Failure | Credential Access | **[verify]** | **[verify]** | Failure event alone ambiguous | Pending |
| Linux sudo Command Execution | Privilege Escalation | **[verify]** | **[verify]** | sudo usage can be normal | Pending |
| Large Outbound Transfer | Exfiltration | **[verify]** | **[verify]** | Volume threshold is heuristic | Pending |
| DNS Query to Unusual High-Risk TLD | Command and Control | **[verify]** | **[verify]** | TLD reputation is not proof of C2 | Pending |

## Correlation rules
Add separate mappings for correlation rules only after their syntax, grouping fields, and event references are validated.
