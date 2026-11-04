# IR Playbook 03 — Suspected Scheduled-Task Persistence

## Trigger
An unexpected scheduled task is created or modified, especially with unusual execution paths, users, or timing.

## 1. Triage
- Record host, task name, task creator, timestamp, task action/command, and event source.
- Verify whether the task is expected maintenance or software management.

## 2. Investigation
- Inspect task configuration and execution history.
- Correlate task creation with process, logon, service, and network events.
- Identify related hosts and accounts.
- Preserve task XML/configuration and relevant logs before removal.

## 3. Containment
- Isolate host or restrict account only if risk warrants it.
- Disable the task only after evidence preservation and operational impact review.

## 4. Eradication
- Remove confirmed malicious task and associated payload/persistence.
- Check for alternate persistence mechanisms.

## 5. Recovery
- Restore legitimate scheduled functionality.
- Validate system integrity and monitor for recreation.

## 6. Communications
- Coordinate with endpoint owner, SOC/IR, and service owner.
- Clearly distinguish confirmed malicious persistence from unapproved but benign administration.

## 7. Closure
- Record evidence, remediation, root cause confidence, and follow-up detection tuning.
