# IR Playbook 02 — Suspected Credential Attack

## Trigger
Repeated failed logons, suspicious authentication patterns, or a confirmed account compromise.

## 1. Triage
- Validate source IP/host, target account(s), destination host, logon type, timestamps, and event IDs.
- Check for successful logons following failures.
- Consider VPN/NAT, scanners, service accounts, and known admin activity.

## 2. Investigation
- Group failures by source, account, and time window.
- Review account privilege, recent changes, and authentication context.
- Check other hosts for related activity.
- Preserve authentication logs and record query/time range.

## 3. Containment
- Apply account lock/reset or access restrictions only under policy and with appropriate approval.
- Block source infrastructure only when attribution and business impact are assessed.
- Revoke sessions/tokens if compromise is confirmed and supported by available controls.

## 4. Eradication and recovery
- Remove unauthorized access paths.
- Reset affected credentials and review MFA/session status.
- Restore account access through verified identity procedures.

## 5. Communications
- Notify IAM, SOC/IR, affected system owners, and business stakeholders as required.
- Avoid sending passwords, tokens, or sensitive evidence in insecure channels.

## 6. Closure
- Document confirmed accounts/hosts, evidence, actions, user impact, and remaining uncertainty.
- Tune alert thresholds only after analyzing benign cases.
