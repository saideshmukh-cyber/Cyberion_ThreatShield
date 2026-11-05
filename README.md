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

## Correlation Testing

ThreatShield includes a synthetic correlation test harness for the following detections:

| Correlation rule | Behavior |
|---|---|
| Failed logon burst | Counts matching failed logons from one source within a time window |
| DNS query frequency | Counts matching DNS queries grouped by query name |
| RDP across multiple hosts | Counts distinct destination hosts from one source |

Run the correlation tests:

```bash
python -m pytest tests/test_correlation.py -v
```

Run the correlation test runner against the sample event dataset:

```bash
python scripts/run_correlation_tests.py
```

The test harness uses synthetic events and the project's existing Sigma rule evaluator. It is intended for demonstration and regression testing, not production SIEM use.

## ATT&CK Coverage

Generate the ATT&CK coverage report from the Sigma rule tags:

```bash
python scripts/generate_attack_coverage.py
```

The generated report is written to:

```text
docs/ATTACK_COVERAGE.md
```

## Detection Limitations

See [`docs/DETECTION_LIMITATIONS.md`](docs/DETECTION_LIMITATIONS.md) for the project's synthetic-data scope, correlation engine limitations, false-positive considerations, and production-readiness requirements.

## Testing

Run the complete project test suite:

```bash
python -m pytest -q
```

Run the structural validator:

```bash
python scripts/validate_sigma.py
```

The validator is a project-level structural check, not a full Sigma specification validator.