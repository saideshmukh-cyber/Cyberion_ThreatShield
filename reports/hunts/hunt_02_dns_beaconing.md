# Hunt 02 — Repeated DNS queries and possible beaconing

**Status:** Hypothesis/method template; not a confirmed finding.

## Hypothesis
A compromised endpoint may repeatedly query the same domain at regular intervals, potentially indicating DNS-based command and control.

## Data required
DNS query logs with timestamp, client/source host, query name, response code, resolved IP, resolver, and (if available) proxy/network connection metadata.

## Method
1. Group events by client and queried domain over a defined time window.
2. Measure event count, inter-arrival intervals, regularity, domain age/reputation, and response patterns.
3. Exclude known CDNs, browsers, software update agents, and endpoint security services using documented allowlist logic.
4. Correlate suspicious DNS with process and outbound network activity.

## Result
No real DNS dataset is included. Synthetic fixtures demonstrate schema only; no beaconing conclusion is made. Record a negative result honestly if the hypothesis is not supported.

## Conclusion
Pending real dataset analysis. Correlation rule is a draft and requires a compatible backend plus schema validation.
