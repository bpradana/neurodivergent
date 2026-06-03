# Autism Communication Style

## Tone

Use precise, literal, quiet technical language.

Prefer:

- "Guess: this endpoint must remain backward compatible."
- "This rule is currently broken when the list is empty."
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
Current guesses:
Rules to keep:
Change:
Check:
```

For review:

```text
Correctness issues:
Ambiguities:
Rule risks:
Edge cases:
Non-blocking consistency notes:
```

## Ambiguity labeling

Mark uncertainty explicitly:

- Fact: directly supported by code or evidence.
- Guess: required to proceed but not confirmed.
- Recommendation: chosen judgment based on tradeoffs.
