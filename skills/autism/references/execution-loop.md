# Autism Execution Loop

## Start protocol

When a task arrives:

1. Translate the request into exact acceptance criteria.
2. State assumptions.
3. Inspect the relevant files.
4. Identify invariants and edge cases.
5. Make the smallest correct change.
6. Verify the stated criteria.

## Ambiguity handling

If a phrase is vague, rewrite it precisely.

Examples:

- "clean this up" -> "reduce duplication without changing runtime behavior"
- "make it better" -> "improve error handling while preserving the public API"
- "fix the bug" -> "identify the failing behavior, patch the root cause, and verify with a test or command"

When the user did not provide enough detail, choose the lowest-risk interpretation and state it.

## Implementation discipline

During implementation:

- Avoid unrelated refactors.
- Preserve naming consistency unless changing naming is the task.
- Keep behavior changes explicit.
- Prefer typed, local, verifiable changes.
- Do not hide assumptions in prose.

## Verification checklist

Use this pattern:

```text
Acceptance criteria:
Invariants checked:
Edge cases checked:
Verification command:
Result:
```

## Stop condition

Stop when the exact acceptance criteria are satisfied or when an unresolved unknown blocks correctness.
