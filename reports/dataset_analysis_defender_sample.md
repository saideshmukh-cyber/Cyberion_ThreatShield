# Dataset Analysis: Windows Defender Detection Events

## 1. Analysis Overview

This analysis examines a Windows Defender EVTX sample from the public EVTX-ATTACK-SAMPLES dataset.

| Attribute | Value |
|---|---|
| Dataset | EVTX-ATTACK-SAMPLES |
| Source file | `AutomatedTestingTools/WinDefender_Events_1117_1116_AtomicRedTeam.evtx` |
| Total event records | 11 |
| Event IDs observed | 1116, 1117 |
| Provider | Microsoft-Windows-Windows Defender |
| Channel | Microsoft-Windows-Windows Defender/Operational |
| Event dates | 2019-07-18 UTC |
| Parser | python-evtx 0.8.1 |
| Parsed output | `data/processed/WinDefender_Events_1117_1116_AtomicRedTeam_events.csv` |

## 2. Event ID Distribution

| Event ID | Count |
|---|---:|
| 1116 | 6 |
| 1117 | 5 |
| **Total** | **11** |

The sample contains Defender detection events and subsequent Defender events associated with several detection IDs.

## 3. Observed Event Details

The following observations are taken directly from the parsed event records.

| Record ID | Event ID | Threat name | Referenced artifact |
|---|---:|---|---|
| 1 | 1116 | Trojan:PowerShell/Powersploit.M | `T1056/Get-Keystrokes.ps1` |
| 2 | 1116 | Trojan:XML/Exeselrun.gen!A | `T1086/payloads/test.xsl` |
| 3 | 1116 | HackTool:JS/Jsprat | `T1100/shells/b.jsp` |
| 4 | 1116 | Backdoor:ASP/Ace.T | `T1100/shells/cmd.aspx` |
| 5 | 1116 | Trojan:Win32/Sehyioa.A!cl | `T1218-2.dll` |
| 6 | 1117 | Trojan:PowerShell/Powersploit.M | `T1056/Get-Keystrokes.ps1` |
| 7 | 1116 | HackTool:JS/Jsprat | `T1100/shells/b.jsp` |
| 8 | 1117 | Backdoor:ASP/Ace.T | `T1100/shells/cmd.aspx` |
| 9 | 1117 | Trojan:Win32/Sehyioa.A!cl | `T1218-2.dll` |
| 10 | 1117 | HackTool:JS/Jsprat | `T1100/shells/b.jsp` |
| 11 | 1117 | Trojan:XML/Exeselrun.gen!A | `T1086/payloads/test.xsl` |

The referenced paths contain Atomic Red Team test artifact names and technique identifiers. These identifiers should be checked against the current MITRE ATT&CK knowledge base before finalizing ATT&CK mappings.

## 4. Common Event Context

The parsed records share several characteristics:

- Process name: `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe`
- Detection user: `MSEDGEWIN10\IEUser`
- Defender provider and operational channel
- Multiple detection IDs recur across event records
- Event timestamps span approximately 13 minutes, from 20:40 to 20:53 UTC

The repeated detection IDs and common process context suggest that these events belong to a related test activity sequence. This is an analytical interpretation of the sample, not proof of a complete attack chain.

## 5. Detection and Remediation Fields

The records contain fields including:

- `Threat Name`
- `Severity Name`
- `Detection ID`
- `Process Name`
- `Detection User`
- `Path`
- `Action ID`
- `Error Code`
- `Error Description`
- `Additional Actions String`
- `Remediation User`

Several later events show changes in state, action, and error-code fields.

These fields should be retained during analysis. Numeric action and status values should not be assigned semantic labels without confirming their meanings against appropriate Microsoft event documentation.

## 6. Detection Engineering Implications

### Potential use cases

This sample can support analysis of:

- Defender detection telemetry
- Security-tool alert generation
- Detection and subsequent event relationships
- PowerShell-related detection context
- Event enrichment and investigation workflows

### Limitations

This sample does not directly validate the existing Sigma rules for:

- Encoded PowerShell execution
- PowerShell download cradles
- LSASS process access
- Windows service creation
- Scheduled task creation

The sample primarily contains Defender detection events, not the full process-creation or security-event telemetry needed to validate those rules.

The presence of a Defender detection does not establish that a separate Sigma rule successfully detected the same activity.

## 7. Evidence Traceability

| Evidence | Reference |
|---|---|
| Original EVTX | `data/raw/EVTX-ATTACK-SAMPLES/AutomatedTestingTools/WinDefender_Events_1117_1116_AtomicRedTeam.evtx` |
| Parsed CSV | `data/processed/WinDefender_Events_1117_1116_AtomicRedTeam_events.csv` |
| Event records | 1–11 |
| Inventory | `reports/dataset_inventory.csv` |
| Dataset overview | `reports/dataset_analysis.md` |

## 8. Conclusion

The selected EVTX file contains 11 Windows Defender Operational events associated with Atomic Red Team test artifacts.

The analysis demonstrates successful EVTX parsing, extraction of event-specific fields, event ID summarization, and preservation of evidence references.

This is an initial dataset analysis. It is not a production detection validation, a confirmed incident, or evidence of malicious activity on the analyst's own system.

Further work should correlate these Defender events with relevant process, PowerShell, and security telemetry before drawing conclusions about attack execution or detection coverage.
