# Playbook — Suspected command-and-control beaconing

## Trigger
Repeated periodic DNS/network activity to a suspicious destination, corroborated by endpoint or network evidence.

## Triage and investigation
1. Preserve DNS, proxy, firewall, and endpoint events with timestamps and query details.
2. Assess domain/IP reputation and context using approved threat-intelligence sources; record source and lookup time.
3. Test periodicity, host prevalence, process ownership, data volume, and related destinations.
4. Separate a suspicious indicator from a confirmed compromise; check known SaaS/CDN and update-agent traffic.

## Containment
If confidence and risk justify, block destination via approved controls and isolate affected host with authorization. Consider collateral impact and alternate domains/IPs.

## Eradication and recovery
Identify and remove confirmed persistence, patch initial access vector, validate host integrity, and monitor for re-resolution or alternate infrastructure.

## Communications
Notify SOC lead, network/DNS owner, endpoint owner, incident commander, and business service owner. Record block scope, expiration/review, and customer impact.

## Closure criteria
Traffic is explained or contained, host disposition is documented, controls are verified, and detection improvements are tracked.
