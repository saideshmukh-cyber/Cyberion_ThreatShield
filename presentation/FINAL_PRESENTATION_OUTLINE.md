# Cyberion ThreatShield — Final Presentation Outline

## Slide 1 — Title
Cyberion ThreatShield: Detection Engineering & Threat Hunting Portfolio

## Slide 2 — Problem and objectives
- Detection engineering and threat hunting workflow.
- Scope: Windows/Linux/network rule concepts, ATT&CK mapping, triage/playbooks.
- Clearly identify the project as a portfolio/lab engagement.

## Slide 3 — Data and methodology
- EVTX-ATTACK-SAMPLES source and license.
- Dataset commit, number of files actually analyzed, parser/tool versions.
- Distinguish raw source data, derived output, and synthetic fixtures.

## Slide 4 — Detection engineering
- 15 Sigma rules and intended telemetry.
- Field mapping and rule assumptions.
- Conversion output is not equivalent to SIEM validation.

## Slide 5 — Validation
- Test harness and unit-test results.
- Dataset test coverage only if executed.
- Limitations and unsupported fields.

## Slide 6 — Threat hunts
- Hunt hypotheses, queries, scope, and evidence.
- Show one hunt outside detection-rule coverage if completed.
- Do not present a hypothesis as a confirmed finding.

## Slide 7 — Incident case studies
- Clearly label simulated vs. dataset-backed case.
- Timeline, evidence, root cause, impact, and closure rationale.

## Slide 8 — IR playbooks
- PowerShell, authentication, scheduled-task scenarios.
- Trigger, investigation, containment, eradication/recovery, communications.

## Slide 9 — False-positive tuning
- Three tuning iterations.
- Measured before/after results and tradeoffs, if collected.

## Slide 10 — Lessons learned and next steps
- Telemetry gaps, field normalization, correlation validation.
- What would be required for production deployment.

## Slide 11 — References
- Dataset, SigmaHQ, MITRE ATT&CK, parser/tool references, incident-report sources.
