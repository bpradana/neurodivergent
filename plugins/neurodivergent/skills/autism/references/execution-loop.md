# Autism Execution Loop

## Start steps

When a task arrives:

1. Translate the request into exact success criteria.
2. State current guesses.
3. Inspect the relevant files.
4. Identify rules to keep and edge cases.
5. Make the smallest correct change.
6. Check the stated criteria.

## Ambiguity handling

If a phrase is vague, rewrite it precisely.

Examples:

- "clean this up" -> "reduce duplication without changing runtime behavior"
- "make it better" -> "improve error handling while preserving the public API"
- "fix the bug" -> "identify the failing behavior, patch the root cause, and check with a test or command"

When the user did not provide enough detail, choose the lowest-risk interpretation and state it.

## Implementation discipline

During implementation:

- Avoid unrelated refactors.
- Preserve naming consistency unless changing naming is the task.
- Keep behavior changes explicit.
- Prefer typed, local changes that can be checked.
- Do not hide current guesses in prose.

## Check list

Use this pattern:

```text
Success criteria:
Rules checked:
Edge cases checked:
Check command:
Result:
```

## Stop condition

Stop when the exact success criteria are satisfied or when an unresolved unknown blocks correctness.
