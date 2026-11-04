# False-Positive Tuning Log

## Rule

Potential LSASS Credential Dumping via Process Access

## Dataset

EVTX-ATTACK-SAMPLES

## Test Evidence

- Sample: `babyshark_mimikatz_powershell.evtx`
- Sysmon Event ID: 10
- Matching records: 2
- TargetImage: `C:\Windows\system32\lsass.exe`
- SourceImage: PowerShell
- GrantedAccess: `0x00001010`
- Record IDs: 22 and 30
- Sample timestamps: 2019-04-18

## Pass 1 — Baseline Logic

**Status: Baseline evidence documented**

### Detection Logic

- Target process filter: `lsass.exe`
- Access-mask filter: `0x1010`, `0x1410`, `0x1438`, `0x143a`
- Expected positive: LSASS access with one of the configured masks
- Expected negative: access to a non-LSASS process
- Expected negative: LSASS access with an unlisted mask

### Observations

The two source records match the target process and access-mask conditions.

The source EVTX labels the activity as credential dumping.

### Limitations

- Historical controlled dataset; not live endpoint telemetry.
- Only two Event ID 10 records evaluated.
- No enterprise allowlist has been established.
- No SIEM alert-volume or production false-positive rate measured.
- Python logic tests do not replace Sigma or SIEM validation.

## Pass 2 — Qualitative Benign Activity Review

**Status: Qualitative review documented; empirical validation pending**

### Objective

Review potential legitimate causes of LSASS process-access alerts.

### Potential Benign Sources Considered

- Endpoint security and antivirus software
- Approved diagnostic tools
- Authorized security assessment tools
- Legitimate system administration activity

### Data Availability

The current evidence does not document actual benign LSASS-access events reviewed during this pass.

This pass is therefore a qualitative review, not a measured false-positive test.

### Findings

Potential benign sources were identified for future investigation.

No conclusion about actual benign-event frequency or false-positive reduction is established.

### Rule Changes

No rule changes are documented as part of this qualitative review.

### Limitations

- No confirmed benign telemetry sample documented.
- No before-and-after false-positive counts.
- No false-positive rate reduction claimed.

## Pass 3 — Python Matcher Regression Testing

**Status: Python regression tests completed; empirical false-positive tuning pending**

### Test Date

November 4, 2026

### Test Command

```bash
pytest -v tests/test_lsass_detection_logic.py
```

### Results

The LSASS detection logic tests completed successfully.

The five reported test cases passed:

- Detects PowerShell access to LSASS.
- Detects case-insensitive LSASS paths.
- Does not detect access to another process.
- Does not detect an unlisted access mask.
- Does not detect a missing target.

### Positive Cases

- LSASS process access with configured access-mask conditions.
- Case-insensitive LSASS path handling.

### Negative Cases

- Access to a non-LSASS process.
- Unlisted access mask.
- Missing target process field.

### Changes Since Pass 2

The custom event-testing harness was updated to normalize escaped backslashes in Sigma field values.

This fixed the LSASS rule's synthetic fixture matching issue.

The Sigma rule itself was not changed as part of this harness correction.

### Limitations

- These tests validate included Python matcher fixtures.
- They do not establish production detection performance.
- They do not establish a measured false-positive rate.
- They do not replace full Sigma or SIEM testing.
- Empirical benign telemetry evaluation remains pending.

## Overall Tuning Status

| Pass | Status |
|---|---|
| Pass 1 — Baseline logic | Evidence documented |
| Pass 2 — Qualitative benign review | Qualitative review documented |
| Pass 3 — Python matcher regression | Tests passed |
| Empirical false-positive measurement | Pending |

No production false-positive rate reduction is claimed.
