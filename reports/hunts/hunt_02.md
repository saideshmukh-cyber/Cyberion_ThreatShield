# Threat Hunt 02 — Repeated DNS Queries and Possible Beaconing

**Status:** Hypothesis and methodology documented; real telemetry validation pending  
**Dataset:** No real DNS dataset currently documented  
**ATT&CK mapping:** Application Layer Protocol — T1071.004 (DNS)

## 1. Executive Summary

This hunt investigates whether repeated DNS queries from a host to the same domain could indicate DNS-based command-and-control activity.

The current project includes a synthetic DNS fixture and a draft correlation rule.

No real DNS dataset analysis has been documented for this hunt.

Therefore, no DNS beaconing finding is confirmed.

## 2. Hunt Hypothesis

A compromised endpoint may repeatedly query the same domain at regular or semi-regular intervals.

Repeated DNS activity may be suspicious when supported by:

- Repeated queries from the same client.
- Consistent or unusual timing.
- Unusual domain characteristics.
- Suspicious response patterns.
- Related process or network activity.

Regular DNS queries alone do not prove command and control.

## 3. Data Requirements

The hunt requires DNS query telemetry with, where available:

- Timestamp.
- Client or source host.
- Queried domain.
- DNS response code.
- Resolved IP address.
- DNS resolver.
- Associated process.
- Proxy or network connection metadata.

The available fields must be verified before executing the hunt.

## 4. Hunt Method

1. Group DNS events by client and queried domain.
2. Define a specific analysis time window.
3. Calculate query counts and inter-arrival intervals.
4. Examine timing regularity and response patterns.
5. Review domain characteristics and reputation using appropriately dated sources.
6. Identify common legitimate sources such as browsers, CDNs, software updates, and endpoint security services.
7. Correlate suspicious DNS activity with process and outbound network telemetry.
8. Record evidence supporting or refuting the hypothesis.

Do not label a domain malicious based solely on its top-level domain or query frequency.

## 5. Current Evidence

| Evidence source | Status |
|---|---|
| Real DNS dataset | Not documented |
| Synthetic fixture | Available for harness demonstration |
| DNS correlation rule | Draft |
| Real beaconing observations | None documented |
| Confirmed command-and-control activity | None |

The synthetic fixture demonstrates schema and detection-testing behavior only.

## 6. Results

| Metric | Current status |
|---|---|
| Real DNS events reviewed | Not established |
| Candidate periodic query groups | Not established |
| Confirmed beaconing clusters | None documented |
| Benign clusters reviewed | Not established |
| Production telemetry | Not used |

These entries reflect the current evidence available in the project documentation, not a claim that beaconing does not exist.

## 7. False-Positive Considerations

Potential benign explanations include:

- Browser activity.
- Content delivery networks.
- Software update services.
- Endpoint security products.
- Monitoring and telemetry services.
- Legitimate application polling.

A meaningful assessment requires context and corroborating evidence.

## 8. ATT&CK Mapping

| Technique | ID | Status |
|---|---|---|
| DNS | T1071.004 | Hypothesis and detection mapping; real hunt validation pending |

This mapping represents the behavior under investigation, not a confirmed finding.

## 9. Limitations

- No real DNS dataset is documented for this hunt.
- Synthetic fixture results do not establish beaconing.
- The correlation rule is a draft.
- Backend compatibility and correlation semantics require validation.
- No production command-and-control activity is established.

## 10. Conclusion

The hunt hypothesis and analysis methodology are documented.

The available evidence is insufficient to confirm or refute DNS beaconing in real telemetry.

**Conclusion: Pending real DNS dataset analysis.**

## 11. Follow-up Actions

1. Obtain a suitable DNS dataset.
2. Verify the actual schema and available fields.
3. Execute the documented analysis.
4. Record positive and negative results.
5. Correlate suspicious DNS with process and network telemetry.
6. Validate the correlation rule against a compatible backend.
