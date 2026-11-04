# Threat Hunt 01 — Potential LSASS Credential Access

**Status:** Historical controlled-sample analysis completed; broader validation pending  
**Dataset:** EVTX-ATTACK-SAMPLES  
**Sample:** `babyshark_mimikatz_powershell.evtx`  
**Log source:** Sysmon Event ID 10 — Process Access  
**ATT&CK mapping:** Credential Access — OS Credential Dumping (T1003.001)

## 1. Executive Summary

This hunt examined historical Sysmon process-access telemetry for activity targeting the Local Security Authority Subsystem Service (LSASS).

Two Event ID 10 records in the selected controlled sample matched the documented LSASS target-process and access-mask conditions.

The sample identifies PowerShell as the source process and LSASS as the target. The dataset labels the activity as credential dumping.

These observations support a suspicious credential-access assessment within the selected sample. They do not establish a live compromise, production detection effectiveness, or the presence of an active threat.

## 2. Hunt Hypothesis

A process accessing LSASS with permissions commonly associated with memory reading may indicate attempted credential dumping.

The hypothesis is supported when process-access telemetry identifies:

- LSASS as the target process.
- A source process requiring investigation.
- An access mask associated with potentially sensitive memory access.
- Additional context supporting suspicious behavior.

An LSASS access event alone does not prove malicious intent.

## 3. Scope and Data Source

| Attribute | Value |
|---|---|
| Dataset | EVTX-ATTACK-SAMPLES |
| Sample | `babyshark_mimikatz_powershell.evtx` |
| Event source | Sysmon |
| Event ID | 10 |
| Analysis type | Historical controlled-sample review |
| Live telemetry | Not used |
| Production SIEM | Not used |

The analysis was restricted to the selected historical sample and documented event records.

## 4. Detection Logic

The investigation examined process-access events using the following conditions:

- Target image ends with `\lsass.exe`.
- Granted access matches one of the configured values:
  - `0x1010`
  - `0x1410`
  - `0x1438`
  - `0x143a`

These access masks are detection heuristics. They are not universal indicators of credential dumping.

The corresponding Sigma detection is:

`rules/windows/windows_lsass_access.yml`

## 5. Evidence

| Evidence | Observation |
|---|---|
| Event ID | Sysmon 10 |
| Matching records | 2 |
| Record IDs | 22 and 30 |
| Target process | `C:\Windows\system32\lsass.exe` |
| Source process | PowerShell |
| Granted access | `0x00001010` |
| Sample date | April 18, 2019 |

Both records matched the configured target-process and access-mask conditions.

The sample's historical context identifies the activity as credential dumping.

The source records are historical evidence from a controlled dataset, not telemetry from a currently compromised system.

## 6. Findings

### Observed

- Two process-access records matched the LSASS detection conditions.
- Both records targeted LSASS.
- PowerShell was identified as the source process.
- Both records contained access mask `0x00001010`.
- The dataset labels the activity as credential dumping.

### Not Established

- Whether the same activity occurs in a current environment.
- Whether an enterprise endpoint security product would generate an alert.
- Whether any additional credential material was successfully extracted.
- Whether the activity resulted in credential compromise.
- Whether the behavior would be malicious in every environment.

## 7. False-Positive Considerations

Potential benign explanations for LSASS access include:

- Endpoint security and antivirus products.
- Authorized diagnostic tools.
- Approved security assessment tools.
- Legitimate administrative or troubleshooting activity.

The current dataset does not establish the frequency of these benign behaviors.

No enterprise allowlist or measured false-positive rate was established during this hunt.

## 8. ATT&CK Mapping

| Technique | ID | Evidence |
|---|---|---|
| OS Credential Dumping | T1003.001 | Historical sample labels the LSASS activity as credential dumping |

This mapping reflects the dataset's context and the observed behavior. It is not evidence of a complete attack chain.

## 9. Conclusion

The hunt identified two suspicious LSASS process-access records in a historical controlled sample.

The observed activity is consistent with the documented credential-dumping scenario.

**Conclusion:** The hypothesis is supported within the selected historical sample.

This conclusion does not establish live compromise, successful credential extraction, or production detection effectiveness.

## 10. Follow-up Actions

1. Validate the Sigma rule against a full Sigma-compatible backend.
2. Review benign LSASS process-access telemetry.
3. Correlate LSASS access with process creation and endpoint security events.
4. Test additional positive and negative samples.
5. Preserve the distinction between historical sample evidence and current operational telemetry.
