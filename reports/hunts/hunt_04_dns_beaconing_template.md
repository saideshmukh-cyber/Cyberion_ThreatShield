# Threat Hunt 04 — DNS Beaconing Analysis Template

**Status:** Reusable methodology template  
**Real telemetry validation:** Pending  
**Purpose:** Future DNS beaconing investigations

## 1. Objective

Provide a repeatable method for investigating potential DNS-based command-and-control behavior.

## 2. Hypothesis

Repeated DNS queries from a client to the same domain, with suspicious timing and supporting process or network evidence, may indicate beaconing.

## 3. Required Data

- Timestamp.
- Client hostname or address.
- Query name.
- DNS response code.
- Resolved IP address.
- Resolver.
- Process or network context, where available.

## 4. Method

1. Identify repeated queries by client and domain.
2. Establish a defined time window.
3. Calculate inter-arrival intervals.
4. Examine timing consistency and response behavior.
5. Review domain reputation and contextual information.
6. Exclude or investigate known legitimate services.
7. Correlate with process and network activity.
8. Document evidence, uncertainty, and alternative explanations.

## 5. Evidence Record

| Timestamp | Client | Domain | Query count | Interval | Response | Assessment |
|---|---|---|---:|---|---|---|
| Pending | Pending | Pending | Pending | Pending | Pending | Not assessed |

Do not populate this table with invented observations.

## 6. Conclusion

This is a methodology template, not a completed hunt.

A conclusion must be based on actual DNS records and supporting evidence.
