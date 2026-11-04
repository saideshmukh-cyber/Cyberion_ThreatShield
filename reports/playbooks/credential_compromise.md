# Playbook — Suspected credential compromise

## Trigger
High-confidence credential dumping or suspicious identity use, supported by endpoint/authentication evidence.

## Triage and investigation
1. Record alert ID, UTC time, host, account, source, and analyst.
2. Validate endpoint event and process lineage; check signer/hash and approved security tooling.
3. Review recent authentication, privilege changes, remote access, and related hosts.
4. Determine likely scope and preserve logs/volatile evidence under policy.

## Containment
- With incident commander/identity owner approval, disable or restrict affected accounts and revoke sessions/tokens.
- Isolate affected endpoint using approved EDR/network controls when justified.
- Avoid destructive remediation before evidence preservation unless active harm requires immediate action.

## Eradication and recovery
Remove confirmed malicious persistence, patch root cause, rotate exposed credentials/secrets, restore from trusted state if needed, and verify telemetry/controls before reconnecting.

## Communications
Notify SOC lead, identity owner, endpoint owner, incident commander, and privacy/legal contacts as required by policy. Share only minimum necessary details.

## Closure criteria
Scope is understood, credentials/session exposure addressed, systems validated, evidence retained, and follow-up actions assigned.
