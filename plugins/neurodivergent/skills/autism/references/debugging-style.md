# Autism Debugging Style

## Debugging posture

Debug by constructing an exact model of expected behavior, observed behavior, and the difference between them.

## Delta model

Use this structure:

```text
Expected:
Observed:
Difference:
Relevant invariant:
Possible violating component:
```

## Trace order

Trace from input to output through explicit boundaries:

1. Input shape and validation.
2. Type conversion or parsing.
3. State mutation.
4. External call or dependency boundary.
5. Output formatting.
6. Error path.

## Edge-case categories

Check:

- empty input
- null or undefined value
- duplicate item
- ordering difference
- timezone or locale
- concurrency and race timing
- retry behavior
- cache invalidation
- partial failure
- permission boundary

## Evidence rule

Do not treat a hypothesis as true without evidence from code, tests, logs, or reproduction.

## Root cause statement

When found, state root cause exactly:

```text
Root cause: <component> violates <invariant> when <condition>, causing <observable failure>.
```
