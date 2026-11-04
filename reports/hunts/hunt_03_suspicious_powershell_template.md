# Threat Hunt 03 — Suspicious PowerShell Execution

**Status:** Method template; synthetic fixture demonstration only  
**Dataset:** Synthetic JSONL fixture  
**Real telemetry validation:** Pending  
**ATT&CK mapping:** PowerShell — T1059.001

## 1. Objective

Identify PowerShell execution patterns that may indicate suspicious command execution, encoded commands, or content retrieval.

## 2. Hypothesis

A host executing PowerShell with encoded commands or suspicious download-related behavior may be staging or retrieving content.

## 3. Data Requirements

Relevant telemetry may include:

- Process creation events.
- Timestamp and hostname.
- User and process image.
- Command line.
- Parent process.
- Process hash or signature.
- DNS and network connection context.

The actual field availability must be verified in the selected dataset.

## 4. Method

1. Identify PowerShell process starts.
2. Review command-line indicators such as `-EncodedCommand` and `-enc`.
3. Identify suspicious download-related functions or commands.
4. Decode encoded content in a safe analysis environment without executing it.
5. Correlate with parent processes, child processes, DNS, proxy, and endpoint events.
6. Compare findings with approved administration activity.

## 5. Current Evidence

The bundled synthetic event fixture contains an encoded-command example used to test the custom Python rule-testing harness.

This fixture demonstrates matching behavior only.

It does not establish attacker activity or a real threat-hunting finding.

## 6. Results

| Metric | Status |
|---|---|
| Synthetic fixture example | Present |
| Real dataset analyzed | Not established |
| Real event count | Pending |
| Confirmed suspicious events | Pending |
| Benign activity reviewed | Pending |

## 7. Limitations

- Synthetic fixture only.
- No real dataset hunt result documented.
- No production endpoint telemetry.
- No confirmed malicious PowerShell activity.
- Harness matching does not establish production detection effectiveness.

## 8. Conclusion

This report is a reusable hunt methodology template.

The hypothesis has not been validated against real telemetry.

Do not classify this hunt as a confirmed finding until supporting dataset evidence is recorded.
