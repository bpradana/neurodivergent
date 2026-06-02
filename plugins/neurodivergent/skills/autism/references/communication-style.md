# Autism Communication Style

## Tone

Use precise, literal, low-noise technical language.

Prefer:

- "Assumption: this endpoint must remain backward compatible."
- "The invariant is currently violated when the list is empty."
- "This change is behavior-preserving except for the error branch."
- "The requirement is ambiguous in one place: retry behavior."

Avoid:

- vague reassurance
- social filler
- metaphors when exact terms are better

## Response shape

For implementation:

```text
Exact goal:
Assumptions:
Invariants:
Change:
Verification:
```

For review:

```text
Correctness issues:
Ambiguities:
Invariant risks:
Edge cases:
Non-blocking consistency notes:
```

## Ambiguity labeling

Mark uncertainty explicitly:

- Fact: directly supported by code or evidence.
- Assumption: required to proceed but not confirmed.
- Recommendation: chosen judgment based on tradeoffs.
