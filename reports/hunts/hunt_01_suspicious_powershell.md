# Hunt 01 — Suspicious PowerShell execution

**Status:** Method template; synthetic fixture demonstration only. Do not present this as a real threat-hunt finding.

## Hypothesis
A host may have executed PowerShell with an encoded command or a download cradle to stage or retrieve content.

## Data required
Process-creation telemetry with timestamp, host, user, image, command line, parent process, signature/hash, and network/DNS context.

## Method
1. Identify PowerShell process starts and search command-line flags such as `-EncodedCommand`/`-enc` and download-related functions.
2. Decode encoded content only in a safe analysis environment; do not execute it.
3. Pivot to parent/child processes, DNS, proxy, and endpoint events around the same timestamp.
4. Compare the account, host role, script path, signer, and change window with approved administration activity.

## Result
The bundled synthetic event fixture includes one encoded-command example to test the local harness. It is not proof of attacker behavior. Replace this section with dataset name/version, exact event IDs, timestamps, query/code, match counts, false positives, and limitations after testing a real dataset.

## Conclusion / follow-up
Not assessed on real telemetry. If corroborated, preserve evidence and use the credential-compromise or command-execution playbook as appropriate. Record the detection gap and update ATT&CK coverage only after validation.
