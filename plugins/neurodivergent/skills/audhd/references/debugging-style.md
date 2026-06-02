# AuDHD Debugging Style

## Debugging posture

Debug by combining fast suspect generation with strict evidence tracking.

## Suspect protocol

```text
Expected:
Observed:
Difference:
Top suspects:
1. Boring likely:
2. Weird cheap:
3. Systemic/invariant:
First probe:
```

## Probe selection

Choose the probe that is:

- interesting enough to pursue now
- cheap enough to reverse
- likely to produce evidence
- tied to an invariant or observable behavior

## Evidence table

When debugging spans multiple steps, maintain:

```text
Hypothesis | Evidence | Status
```

Statuses:

- open
- supported
- falsified
- parked

## Common AuDHD bug patterns

Check for:

- state machine inconsistency
- hidden async ordering
- mismatch between type contract and runtime behavior
- cache or stale dependency
- duplicate source of truth
- unclear ownership boundary
- off-by-one or boundary mismatch
- partial failure path

## Stop condition

Stop when either:

- the root cause is tied to evidence and a patch is verified
- the failing area is narrowed with exact next verification
- an external blocker is identified
