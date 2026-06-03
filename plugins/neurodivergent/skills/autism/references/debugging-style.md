# Autism Debugging Style

## How to debug

Debug by building a clear map of expected behavior, observed behavior, and the difference between them.

## Difference map

Use this structure:

```text
Expected:
Observed:
Difference:
Relevant rule:
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

## Edge cases

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

## Evidence

Do not treat a guess as true without evidence from code, tests, logs, or reproduction.

## Root cause statement

When found, state root cause exactly:

```text
Root cause: <component> breaks <rule> when <condition>, causing <visible failure>.
```
