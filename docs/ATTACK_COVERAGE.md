# Cyberion ThreatShield — ATT&CK Coverage

Generated from the ATT&CK tags in the project's Sigma YAML files.

ATT&CK tags represent intended coverage, not proven production efficacy.

| Rule | File | UUID | ATT&CK tags |
|---|---|---|---|
| Linux SSH Authentication Failure | `rules/linux/linux_ssh_auth_failures.yml` | `7a354b75-0212-5fc3-bfcb-b4bc2f4f8cd0` | attack.t1110 |
| Linux sudo Command Execution | `rules/linux/linux_sudo_privilege_use.yml` | `1b31d9fe-aa28-5166-baea-1e8a2e2c31d4` | attack.t1548.003 |
| Large Outbound Transfer | `rules/network/large_outbound_transfer.yml` | `c8cc97a8-4f6c-596c-9164-1cae8682ed32` | attack.t1041 |
| DNS Query to Unusual High-Risk TLD | `rules/network/suspicious_dns_tld.yml` | `cc36ae29-5546-57d5-b208-40302b8e495a` | attack.t1071.004 |
| Defender Real-time Monitoring Disabled | `rules/windows/defender_detection_disabled.yml` | `7a1a4ae2-e082-53bb-89bf-6efa2ab80bdd` | attack.t1562.001 |
| Repeated Failed Logons | `rules/windows/multiple_failed_logons.yml` | `29990db0-cd02-539a-bce8-b57aa78ec4e8` | attack.t1110 |
| Local User Account Created | `rules/windows/new_local_user.yml` | `4a36f413-70a4-5e78-a679-f5f474cbbfd3` | attack.t1136.001 |
| New Windows Service Installation | `rules/windows/new_service_install.yml` | `f6dc3a7e-ca72-5011-8664-0982884b8240` | attack.t1543.003 |
| PowerShell Encoded Command Execution | `rules/windows/powershell_encoded_command.yml` | `6bd0193f-3d2f-5a99-b625-4250928f5d66` | attack.t1059.001 |
| Executable Launched from User Temp Directory | `rules/windows/process_from_temp.yml` | `f374585b-4cc7-5274-8f52-b7e2a48c9881` | attack.t1036 |
| Remote Interactive Logon (RDP) | `rules/windows/remote_logon_rdp.yml` | `5719c6a7-51f9-511e-98a4-5cd1270fae1e` | attack.t1021.001 |
| Scheduled Task Created | `rules/windows/scheduled_task_creation.yml` | `c674665d-16c2-51f0-a870-b1ee745c8dc4` | attack.t1053.005 |
| Security Event Log Cleared | `rules/windows/security_log_cleared.yml` | `66cbb0dc-6bdb-5e3d-a490-639942a6dd92` | attack.t1070.001 |
| PowerShell Download Cradle | `rules/windows/suspicious_powershell_download.yml` | `b8676130-bb3d-5a00-a259-b2ecec2af38a` | attack.t1059.001 |
| Potential LSASS Credential Dumping via Process Access | `rules/windows/windows_lsass_access.yml` | `6b96f3d8-2db7-4db1-9ac4-7a36d7e6a001` | attack.credential_access, attack.t1003.001 |

## Limitations

- Tags are read from Sigma metadata and are not independently verified.
- Untagged rules are shown as `Not tagged`.
- Technique mapping does not prove detection efficacy.
- Correlation rules are excluded from this generated table.
- Review ATT&CK mappings before using this report for formal coverage claims.
