# Sigma Rule Review
## Validation Scope and Limitations

This project uses a basic structural YAML validator and a Python testing harness.

The structural validator checks YAML parsing and selected metadata requirements. It is not a complete Sigma specification validator.

Sigma CLI conversion confirms that SPL output can be generated for supported rules. Conversion alone does not establish that the query works correctly in a production SIEM.

Python unit tests validate the specific test cases included in the project. They do not establish that every Sigma rule has been tested against representative Windows, Linux, or network telemetry.

Validation status is tracked separately for YAML parsing, Sigma specification validation, SPL conversion, data testing, and false-positive review.


| Rule | YAML Valid | Sigma Validated | SPL Converted | Tested Against Data | FP Review |
|---|---|---|---|---|---|
| Defender Monitoring Disabled | Pending | Pending | Pending | Pending | Pending |
| Failed Logons | Pending | Pending | Pending | Pending | Pending |
| Local User Created | Pending | Pending | Pending | Pending | Pending |
| Windows Service Installed | Pending | Pending | Pending | Pending | Pending |
| Encoded PowerShell | Pending | Pending | Pending | Pending | Pending |
| Temp Directory Execution | Pending | Pending | Pending | Pending | Pending |
| RDP Logon | Pending | Pending | Pending | Pending | Pending |
| Scheduled Task | Pending | Pending | Pending | Pending | Pending |
| Security Log Cleared | Pending | Pending | Pending | Pending | Pending |
| PowerShell Download Cradle | Pending | Pending | Pending | Pending | Pending |
| LSASS Process Access | Pending | Pending | Pending | Pending | Pending |
| Linux SSH Failure | Pending | Pending | Pending | Pending | Pending |
| Linux sudo Execution | Pending | Pending | Pending | Pending | Pending |
| Large Outbound Transfer | Pending | Pending | Pending | Pending | Pending |
| Unusual DNS TLD | Pending | Pending | Pending | Pending | Pending |

## Notes
Successful YAML parsing or SPL conversion does not prove
detection effectiveness or production readiness.

## Custom Rule Testing Checkpoint — November , 2026

### Results

The custom Python event-testing harness was corrected to normalize escaped backslashes in Sigma field values.

The following rules were tested against the project's 16 synthetic JSONL events:

| Rule | Matches |
|---|---:|
| Potential LSASS Credential Dumping via Process Access | 1 |
| PowerShell Encoded Command Execution | 1 |

The LSASS match corresponds to the synthetic event timestamp `2026-10-28T10:10:00Z`. The PowerShell match corresponds to event ID 1.

The regression test suite completed successfully with 11 passing tests.

### Limitations

- The harness supports only a limited subset of Sigma syntax.
- Correlation rules are not evaluated by this harness.
- Results are based on synthetic fixtures, not production endpoint telemetry.
- A match indicates that the implemented harness conditions matched the event; it does not independently establish malicious activity.
- Full Sigma specification compliance and detection effectiveness remain separate validation tasks.

## Windows Rule Testing — November , 2026

### Test scope

- Dataset: `data/sample/events.jsonl`
- Dataset size: 16 synthetic events
- Rules evaluated: 11 Windows single-event Sigma rules
- Harness: `scripts/run_rule_tests.py`

### Results

All 11 Windows rules produced at least one match against the synthetic dataset.

| Metric | Result |
|---|---:|
| Windows rules evaluated | 11 |
| Rules with at least one match | 11 |
| Rules with zero matches | 0 |
| Synthetic events evaluated | 16 |

The results are recorded in `reports/windows_rule_test_results.json`.

### Limitations

These results establish basic matching against synthetic fixtures only. They do not demonstrate production detection performance, complete Sigma compatibility, comprehensive false-positive testing, or correlation-rule functionality.

## Linux and Network Rule Testing — November, 2026

### Test scope

- Dataset: `data/sample/events.jsonl`
- Dataset size: 16 synthetic events
- Rules evaluated: 4 single-event rules
- Harness: `scripts/run_rule_tests.py`

### Results

| Rule | Matches |
|---|---:|
| Linux SSH Authentication Failure | 1 |
| Linux sudo Command Execution | 1 |
| Large Outbound Transfer | 1 |
| DNS Query to Unusual High-Risk TLD | 1 |

All four rules produced at least one match against the synthetic fixtures.

Results are recorded in `reports/linux_network_rule_test_results.json`.

### Combined single-event testing summary

| Category | Rules evaluated | Rules with matches |
|---|---:|---:|
| Windows | 11 | 11 |
| Linux | 2 | 2 |
| Network | 2 | 2 |
| **Total** | **15** | **15** |

### Limitations

These results demonstrate basic matching against synthetic events only. They do not establish production detection effectiveness, complete Sigma specification compatibility, or false-positive performance.

Correlation rules are not evaluated by the current harness.