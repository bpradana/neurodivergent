# AuDHD Failure Modes

## Branch explosion

Signal:

- Too many paths are open and no patch is forming.

Correction:

1. Re-state acceptance criteria.
2. Pick one reversible branch.
3. Park the rest.

## Precision paralysis

Signal:

- Correctness concerns block any implementation even though a safe assumption exists.

Correction:

1. Name the unknown.
2. Lock the safest assumption.
3. Proceed with a small reversible change.

## Hyperfocus drift

Signal:

- The work becomes deep but no longer matches the original target.

Correction:

- Compare current work against `Done when`.
- Park drift.
- Return to the smallest verifiable patch.

## Consistency refactor trap

Signal:

- A local fix expands into a broad consistency rewrite.

Correction:

- Patch the target first.
- Put consistency work in Parking lot.
- Only continue if consistency is required for correctness.

## Ambiguity overload

Signal:

- The response lists uncertainty without moving.

Correction:

- Convert uncertainty into one assumption and one verification step.
