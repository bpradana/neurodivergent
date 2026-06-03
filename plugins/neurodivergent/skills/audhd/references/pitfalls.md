# AuDHD Pitfalls

## Branch explosion

Signal:

- Too many paths are open and no patch is forming.

Correction:

1. Re-state success criteria.
2. Pick one reversible branch.
3. Save the rest for later.

## Precision paralysis

Signal:

- Correctness concerns block any implementation even though a safe guess exists.

Correction:

1. Name the unknown.
2. Lock the safest guess.
3. Proceed with a small reversible change.

## Focus drift

Signal:

- The work becomes deep but no longer matches the original target.

Correction:

- Compare current work against `Done when`.
- Save drift for later.
- Return to the smallest patch that can be checked.

## Consistency refactor trap

Signal:

- A local fix expands into a broad consistency rewrite.

Correction:

- Patch the target first.
- Put consistency work in Things to revisit.
- Only continue if consistency is required for correctness.

## Ambiguity overload

Signal:

- The response lists uncertainty without moving.

Correction:

- Convert uncertainty into one guess and one check.
