# Detection Relevance Matrix

Preliminary mapping of observed event IDs to existing detection use cases.

**Important:** Event ID presence alone does not validate a Sigma rule. Review event fields, log source, and rule conditions before claiming coverage.

| Event ID | Count | Potential rule/use case | Assessment | Source files |
|---|---:|---|---|---|
| 1 | 7 | PowerShell Encoded Command Execution; Temp Executable; PowerShell Download Cradle | Conditional: inspect process command line and image | babyshark_mimikatz_powershell.evtx |
| 3 | 1 | PowerShell Download Cradle; Large Outbound Transfer | Conditional: inspect network connection details | babyshark_mimikatz_powershell.evtx |
| 4 | 1 | New Windows Service Installation | Related: Sysmon service state change; not installation proof | babyshark_mimikatz_powershell.evtx |
| 5 | 2 | No direct match in current rules | Sysmon process termination | babyshark_mimikatz_powershell.evtx |
| 7 | 11 | Potential LSASS Process Access | Related: image loaded; not direct LSASS access evidence | babyshark_mimikatz_powershell.evtx |
| 10 | 2 | Potential LSASS Process Access | Conditional: inspect TargetImage and GrantedAccess | babyshark_mimikatz_powershell.evtx |
| 11 | 3 | Executable Launched from User Temp Directory | Related: file creation; inspect path and process | babyshark_mimikatz_powershell.evtx |
| 12 | 4 | No direct match in current rules | Registry object activity | babyshark_mimikatz_powershell.evtx |
| 16 | 2 | No direct match in current rules | Sysmon configuration change | babyshark_mimikatz_powershell.evtx |
| 1102 | 2 | Security Event Log Cleared | Relevant | ACL_ForcePwd_SPNAdd_User_Computer_Accounts.evtx, CA_chrome_firefox_opera_4663.evtx |
| 1116 | 6 | Defender malware detection | Defender detection event; not the rule for disabling Defender | WinDefender_Events_1117_1116_AtomicRedTeam.evtx |
| 1117 | 5 | Defender remediation/action | Related Defender event; inspect action/status fields | WinDefender_Events_1117_1116_AtomicRedTeam.evtx |
| 4624 | 3 | Remote Interactive Logon (RDP) | Conditional: check LogonType | CA_4624_4625_LogonType2_LogonProc_chrome.evtx |
| 4625 | 1 | Repeated Failed Logons | Relevant | CA_4624_4625_LogonType2_LogonProc_chrome.evtx |
| 4662 | 14 | No direct match in current rules | Directory service object access | ACL_ForcePwd_SPNAdd_User_Computer_Accounts.evtx |
| 4663 | 4 | No mapped rule yet | Needs investigation | CA_chrome_firefox_opera_4663.evtx |
| 4702 | 4 | Scheduled Task Created | Related: task updated, not created | ACL_ForcePwd_SPNAdd_User_Computer_Accounts.evtx |
| 4719 | 8 | No direct match in current rules | System audit policy changed | ACL_ForcePwd_SPNAdd_User_Computer_Accounts.evtx |
| 4738 | 5 | No direct match in current rules | User account changed | ACL_ForcePwd_SPNAdd_User_Computer_Accounts.evtx |
| 4742 | 1 | No direct match in current rules | Computer account changed | ACL_ForcePwd_SPNAdd_User_Computer_Accounts.evtx |
| 4794 | 1 | No direct match in current rules | DSRM password changed | 4794_DSRM_password_change_t1098.evtx |
| 5136 | 22 | No direct match in current rules | Active Directory object modification | ACL_ForcePwd_SPNAdd_User_Computer_Accounts.evtx |

## Existing Sigma rule files

- `correlation_dns_beaconing.yml`
- `correlation_failed_logon_burst.yml`
- `correlation_multi_host_rdp.yml`
- `linux_ssh_auth_failures.yml`
- `linux_sudo_privilege_use.yml`
- `large_outbound_transfer.yml`
- `suspicious_dns_tld.yml`
- `defender_detection_disabled.yml`
- `multiple_failed_logons.yml`
- `new_local_user.yml`
- `new_service_install.yml`
- `powershell_encoded_command.yml`
- `process_from_temp.yml`
- `remote_logon_rdp.yml`
- `scheduled_task_creation.yml`
- `security_log_cleared.yml`
- `suspicious_powershell_download.yml`
- `windows_lsass_access.yml`
