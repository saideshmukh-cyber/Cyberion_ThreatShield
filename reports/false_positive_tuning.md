# False-Positive Tuning Log

## Rule
Potential LSASS Credential Dumping via Process Access

## Dataset
EVTX-ATTACK-SAMPLES

## Test evidence
- Sample: babyshark_mimikatz_powershell.evtx
- Sysmon Event ID: 10
- Matching records: 2
- TargetImage: C:\Windows\system32\lsass.exe
- SourceImage: PowerShell
- GrantedAccess: 0x00001010
- Record IDs: 22 and 30
- Sample timestamps: 2019-04-18

## Pass 1 — Baseline logic
- Target process filter: lsass.exe
- Access-mask filter: 0x1010, 0x1410, 0x1438, 0x143a
- Expected positive: LSASS access with one of the configured masks
- Expected negative: access to a non-LSASS process
- Expected negative: LSASS access with an unlisted mask

## Observations
The two source records match the target process and access mask conditions.
The source EVTX labels the activity as credential dumping.

## Limitations
- Historical controlled dataset; not live endpoint telemetry.
- Only two Event ID 10 records evaluated.
- No enterprise allowlist has been established.
- No SIEM alert-volume or production false-positive rate measured.
- Python logic tests do not replace Sigma or SIEM validation.

## Next tuning passes
Pass 2: Review legitimate LSASS access examples and candidate exclusions.
Pass 3: Re-test the revised rule against positive and negative samples.

Do not mark these passes complete until their evidence is recorded.
