# Cyberion ThreatShield — Detection Limitations

## Project scope

Cyberion ThreatShield is a cybersecurity detection engineering and threat hunting portfolio project. It contains custom Sigma detections, synthetic test fixtures, correlation prototypes, Splunk conversion outputs, and investigation documentation.

It is not a production SOC platform or a validated commercial detection product.

## Data limitations

- The included events are synthetic fixtures.
- Synthetic data demonstrates expected rule behavior under selected conditions.
- Synthetic tests do not establish performance against real enterprise telemetry.
- No production customer telemetry or confidential incident data is included.
- Detection performance may vary across Windows, Linux, network products, and SIEM deployments.

## Sigma rule limitations

- The project validator checks structural requirements and selected metadata.
- The custom validator is not a full Sigma specification validator.
- Passing validation does not guarantee compatibility with every Sigma backend.
- Field names, log sources, and event schemas may require environment-specific adjustment.
- Sigma conversion output must be reviewed before use in a production detection platform.

## Correlation limitations

- Correlation rules are experimental.
- The Python correlation engine is a portfolio test harness, not a production SIEM engine.
- The engine currently supports the project’s `event_count` and `value_count` correlation types.
- It does not support nested correlations, distributed processing, state persistence, or production event ingestion.
- It evaluates synthetic events in memory.
- Timestamp handling and grouping behavior should be tested against the target SIEM.
- Thresholds are illustrative starting points and require tuning against actual telemetry.

## Detection interpretation

- A failed logon burst may result from legitimate user errors or misconfigured services.
- Frequent DNS queries do not independently establish command-and-control activity.
- RDP activity across multiple hosts does not independently establish lateral movement.
- Alerts identify activity requiring investigation; they do not automatically establish malicious intent.
- Analysts should correlate alerts with identity, endpoint, network, and contextual evidence.

## False positives and tuning

Potential benign activity includes:

- Users repeatedly entering incorrect passwords.
- IT administrators connecting to multiple hosts.
- Browsers, CDNs, and endpoint agents generating frequent DNS queries.
- Administrative scripts and legitimate PowerShell activity.
- Approved software deployment and service installation.
- Backup, synchronization, or other high-volume outbound transfers.

Thresholds and exclusions should be tuned using approved telemetry, documented baselines, and analyst feedback.

## Production readiness

Before production deployment:

1. Confirm log source availability.
2. Validate field mappings.
3. Test rules against representative benign and suspicious data.
4. Review false positives and missed detections.
5. Confirm backend conversion and query behavior.
6. Establish alert ownership and triage procedures.
7. Obtain approval from the target environment's detection engineering or SOC team.

## Claims and evidence

The project demonstrates rule authoring, synthetic fixture testing, structural validation, correlation prototyping, and investigation documentation.

It does not claim production deployment, confirmed real-world attack detection, or measured detection efficacy.
