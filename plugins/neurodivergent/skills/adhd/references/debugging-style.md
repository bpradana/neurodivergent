# ADHD Debugging Style

## How to debug

Debug with fast suspect generation, cheap ways to rule things out, and a clear finish.

## Suspect generation

For bugs, list at least three suspects:

1. Boring likely suspect.
2. Weird cheap suspect.
3. Systemic or state-related suspect.

Check the weird cheap suspect early if it is easy to rule out. This prevents hours lost to conventional guesses.

## Check order

Prefer checks that are:

- cheap to run
- likely to split the search space
- reversible
- tied to visible evidence

## Debug loop

```text
Top suspects:
1.
2.
3.

First check:
Observed:
Updated suspects:
Next check:
```

## Failure interpretation

When a test fails, chase the most informative failure first, not necessarily the first line in the output.

Look for:

- changed rule
- hidden state
- order dependence
- stale cache
- racing async task
- configuration drift
- unexpected null or empty value
- boundary behavior

## Stop condition

Stop debugging when there is either:

- a minimal patch and check result
- a narrowed root cause with exact next action
- blocked progress that requires user input or missing credentials
