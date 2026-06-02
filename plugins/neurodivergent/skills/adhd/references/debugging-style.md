# ADHD Debugging Style

## Debugging posture

Debug with fast suspicion generation, cheap falsification, and energetic convergence.

## Suspect generation

For bugs, list at least three suspects:

1. Boring likely suspect.
2. Weird cheap suspect.
3. Systemic or state-related suspect.

Probe the weird cheap suspect early if it is easy to falsify. This prevents hours lost to conventional assumptions.

## Probe order

Prefer probes that are:

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

First probe:
Observed:
Updated suspects:
Next probe:
```

## Failure interpretation

When a test fails, chase the most informative failure first, not necessarily the first line in the output.

Look for:

- changed invariant
- hidden state
- order dependence
- stale cache
- racing async task
- configuration drift
- unexpected null or empty value
- boundary behavior

## Stop condition

Stop debugging when there is either:

- a minimal patch and verification result
- a narrowed root cause with exact next action
- a blocker that requires user input or missing credentials
