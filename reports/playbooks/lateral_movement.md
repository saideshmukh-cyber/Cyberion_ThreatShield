# Playbook — Suspected lateral movement via remote services

## Trigger
Unusual RDP/remote-service activity or correlated logons across multiple hosts.

## Triage and investigation
1. Validate source/destination, account, logon type, time window, and approved jump-host use.
2. Correlate identity-provider, Windows Security, endpoint, VPN, and network telemetry.
3. Map affected hosts and privilege level; inspect remote process/service/task creation.

## Containment
With incident commander approval, restrict source host/network path, suspend suspected account or revoke sessions, and preserve relevant logs. Coordinate before disrupting critical servers.

## Eradication and recovery
Remove unauthorized remote access/persistence, rotate credentials if exposure is plausible, validate patching and access policies, and restore only from trusted state.

## Communications
Notify SOC lead, server owners, identity team, and incident commander; provide scope, confidence, business impact, and next update time.

## Closure criteria
Remote path is controlled, affected hosts reviewed, credentials remediated as required, and monitoring gaps assigned.
