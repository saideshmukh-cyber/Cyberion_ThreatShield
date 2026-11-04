# IOC Research Notes

## Purpose
Record indicators from trusted public reporting or directly analyzed artifacts. This document is a structure; no real IOC has been added by this pack.

## IOC record template
| Field | Value |
|---|---|
| IOC type | IP / domain / URL / hash / file path / registry / other |
| Indicator | **[insert exact value]** |
| Source report | **[URL and publisher]** |
| Publication date | **[date]** |
| First/last seen | **[if source supports it]** |
| Associated actor/campaign | **[only if source states it]** |
| ATT&CK technique | **[if supported]** |
| Confidence | High / Medium / Low + rationale |
| Context | **[what the IOC was used for]** |
| Expiration/relevance | **[time-bound assessment]** |
| Validation performed | **[checks and date]** |
| False-positive risk | **[shared hosting, CDN, benign reuse, etc.]** |

## Research standards
- Prefer primary vendor/incident reports and reputable threat intelligence sources.
- Preserve source URLs and dates.
- Do not treat an IOC as malicious forever; infrastructure can change ownership or usage.
- Do not include private credentials, personal data, or live victim data.
- Do not fabricate IOC values to make the report look complete.
