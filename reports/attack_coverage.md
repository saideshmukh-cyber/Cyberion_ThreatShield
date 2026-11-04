# MITRE ATT&CK Coverage Report

## Coverage Summary

The current Sigma rule-tag scan identified **13 unique ATT&CK technique IDs** and **1 explicit tactic tag**.

The explicit tactic count reflects tactic tags directly present in the Sigma YAML files. It does not represent the total number of tactics associated with the tagged techniques.

The technique count remains below the original project target of 20 unique techniques. No additional techniques have been added merely to reach that target.

## Coverage Categories

### Rule-Tagged Techniques

List techniques explicitly tagged in Sigma rules.

Current result: 13 unique technique IDs.

### Explicit Tactic Tags

List tactic tags directly present in Sigma rules.

Current result: 1 explicit tactic tag — `attack.credential_access`.

### Technique-Associated Tactics

Technique IDs may map to additional ATT&CK tactics even when those tactic tags are not explicitly included in the Sigma YAML.

This category requires verification against the MITRE ATT&CK technique definitions before reporting a final tactic count.

### Techniques Tested Against Data

Include only techniques for which relevant rule logic has been tested against an appropriate fixture or dataset.

Current synthetic fixture testing covers 15 single-event rules. Rule-to-technique mapping and successful fixture matching do not independently establish detection effectiveness.

### Hunt-Only Techniques

List techniques investigated through threat hunting but not necessarily covered by a detection rule.

### Incident-Investigation Techniques

List techniques discussed in incident reports. Incident analysis does not automatically establish detection coverage.

## Limitations

- ATT&CK tags describe intended mapping, not proven detection effectiveness.
- A technique investigated in a hunt is not automatically detected by a Sigma rule.
- Unit tests do not establish real-world detection performance.
- The current coverage count is limited by techniques represented in existing rules and evidence.
- Correlation rules are not evaluated by the current single-event harness.