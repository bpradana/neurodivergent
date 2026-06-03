# AuDHD Debugging Style

## How to debug

Debug by combining fast suspect generation with strict evidence notes.

## Suspects

```text
Expected:
Observed:
Difference:
Top suspects:
1. Boring likely:
2. Weird cheap:
3. Systemic/rule:
First check:
```

## First check choice

Choose the check that is:

- interesting enough to pursue now
- cheap enough to reverse
- likely to produce evidence
- tied to a rule or visible behavior

## Evidence notes

When debugging spans multiple steps, keep:

```text
Guess | Evidence | Status
```

Statuses:

- open
- supported
- ruled out
- save for later

## Common AuDHD bug patterns

Check for:

- step/order inconsistency
- hidden async ordering
- mismatch between type contract and runtime behavior
- cache or stale dependency
- duplicated state
- unclear ownership boundary
- off-by-one or boundary mismatch
- partial failure path

## Stop condition

Stop when either:

- the root cause is tied to evidence and a patch is checked
- the failing area is narrowed with an exact next check
- an external block is identified
