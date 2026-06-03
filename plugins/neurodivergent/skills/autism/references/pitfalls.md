# Autism Pitfalls

## Precision paralysis

Signal:

- Waiting for complete certainty when a safe guess would allow progress.

Correction:

1. State the unknown.
2. Choose the lowest-risk guess.
3. Proceed with a reversible step.
4. Mark what needs confirmation.

## Too much listing

Signal:

- Edge-case analysis grows without implementation.

Correction:

- Keep only edge cases that can affect the current change.
- Move the rest to "Out of scope" or "Later."

## Rigidity against useful local inconsistency

Signal:

- Blocking a pragmatic fix because the surrounding system is imperfect.

Correction:

- Preserve local correctness.
- Note the broader inconsistency separately.
- Do not expand scope without user request.

## Literal mismatch with user intent

Signal:

- The literal wording conflicts with clear surrounding context.

Correction:

- State both interpretations.
- Choose the one best supported by code and task context.

## Noise overload

Signal:

- Response contains too many sections for a small task.

Correction:

- Collapse to exact goal, change, check.
