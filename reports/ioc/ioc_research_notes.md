# IOC research notes

## Purpose
Record indicators from a cited public incident report or authorized investigation and explain how each indicator should (or should not) be operationalized.

## IOC register template
| Indicator | Type | Source / citation | First seen | Confidence | Context | Suggested use | Expiry/review |
|---|---|---|---|---|---|---|---|
| `example.invalid` | Domain (placeholder) | None — illustrative only | N/A | None | Reserved placeholder domain; not a threat indicator | Do not block or alert on this placeholder | N/A |

## Rules
- Do not invent IOCs or label placeholder values malicious.
- Record source URL, publication date, retrieval date, and source reliability.
- Distinguish an indicator from a verdict; add context, confidence, prevalence, and expiration.
- Validate false-positive risk before blocking. Prefer detection/monitoring before disruption when confidence is low.
- Never put credentials, internal secrets, or sensitive victim data in this public repository.
