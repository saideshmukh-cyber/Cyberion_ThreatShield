# Incident Case 01 — Suspicious PowerShell Execution (Simulated Case)

**Case type:** Simulated training scenario  
**Status:** Not an observed incident from the dataset  
**Evidence:** Synthetic case narrative; replace or supplement only with traceable telemetry

## 1. Executive summary
A hypothetical endpoint generates a suspicious PowerShell command line containing encoded content. This case is designed to demonstrate triage and response workflow, not to claim a real compromise.

## 2. Trigger
- Alert: encoded PowerShell command execution.
- Rule: PowerShell Encoded Command Execution (rule ID `6bd0193f-3d2f-5a99-b625-4250928f5d66`).
- Trigger time: **[scenario timestamp]**

## 3. Timeline
| Time (UTC) | Event | Evidence reference | Confidence |
|---|---|---|---|
| T0 | Alert generated in scenario | SIM-01 | Simulated |
| T+5m | Analyst validates process/user/parent context | SIM-02 | Simulated |
| T+15m | Endpoint isolation considered under policy | SIM-03 | Simulated |
| T+30m | Scope and recovery decision documented | SIM-04 | Simulated |

## 4. Investigation
- Validate command line, process image, parent process, user, host, and timestamp.
- Determine whether the command is authorized administration or suspicious activity.
- Review adjacent process/network events if available.
- Preserve relevant logs and record chain-of-custody metadata.

## 5. Root cause
**Not established.** This is a simulated case; no real root cause can be inferred.

## 6. Impact
**Not measured.** Do not claim data theft, persistence, or lateral movement without evidence.

## 7. ATT&CK mapping
- PowerShell: **T1059.001** (validate against the current ATT&CK version when publishing).
- Additional techniques only if supported by evidence.

## 8. Evidence traceability
| Evidence ID | Source | What it supports | Integrity / notes |
|---|---|---|---|
| SIM-01 | Synthetic scenario | Alert trigger | Not real telemetry |
| SIM-02 | Synthetic scenario | Investigation checklist | Not real telemetry |

## 9. Containment / eradication / recovery
- Follow organizational authorization and incident policy.
- Isolate only when justified by risk and operational impact.
- Remove unauthorized persistence only after confirming it exists.
- Recover from trusted state and validate endpoint health.

## 10. Closure rationale
**Training case only.** Closure is illustrative; no actual incident was investigated.
