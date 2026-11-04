# Data dictionary and normalization contract

The bundled `data/sample/events.jsonl` is synthetic test data. Fields are deliberately normalized for harness demonstration and are **not** claimed to be an exact vendor event schema.

| Field | Meaning | Notes |
|---|---|---|
| `timestamp` | Event time in ISO-8601 UTC | Preserve source timezone and original timestamp in real ingestion. |
| `event_id` / `EventID` | Source or Windows event identifier | Do not conflate generic fixture `event_id` with Windows `EventID`. |
| `host` | Hostname | Normalize case consistently; retain original host identifier separately if needed. |
| `Image` | Process image path | Sysmon-like normalized field; validate against source schema. |
| `CommandLine` | Process command line | Treat as sensitive; redact secrets before sharing. |
| `TargetImage` | Target process image | Example field for process-access telemetry. |
| `GrantedAccess` | Process access mask | Interpret only with source-specific semantics. |
| `User` | Account identity | Normalize carefully; keep domain and account if available. |
| `SourceIp` | Remote/source IP address | Confirm source/destination direction from the original event. |
| `LogonType` | Windows logon type | Meaning depends on Windows event source. |
| `message` | Original or normalized text message | Prefer structured fields where available. |
| `query` | DNS query name | Validate DNS schema and case/encoding. |
| `bytes_out` | Outbound byte count | Direction and units must be defined by the source. |

For real datasets, create a source-specific mapping document including source name/version, license, download date, SHA-256, field transformations, timezone, known gaps, and retention limits. Keep raw evidence immutable and transformations reproducible.
