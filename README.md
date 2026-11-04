# Cyberion ThreatShield
## Detection Engineering & Threat Hunting Portfolio

This project demonstrates detection engineering, threat hunting,
event-log analysis, and incident response documentation.

## Project components
- Sigma detection rules for Windows, Linux, and network telemetry
- Python EVTX parser and analysis scripts
- Dataset inventory and event ID summaries
- Detection relevance mapping
- Splunk query conversions
- Rule testing and false-positive tuning records
- Threat hunt reports
- Incident case reports
- Incident response playbooks
- IOC research notes
- Final presentation materials

## Dataset
EVTX-ATTACK-SAMPLES is used as a historical/controlled dataset.
Raw EVTX files are not included in this repository.

## Validation status
Rule conversion, Python tests, and SIEM validation are tracked separately.
A successful conversion does not imply production readiness.

## Testing Limitations

The Python harness evaluates a limited subset of Sigma detection
logic against JSONL fixtures.

It is not a complete Sigma execution engine and does not replace
Sigma CLI validation or SIEM testing.

The LSASS unit tests verify a separate Python matching function.
They do not prove the Sigma rule's effectiveness in Splunk.

## Disclaimer
This is a defensive security portfolio and lab project.
Dataset findings are not claims of a live compromise or customer incident.
