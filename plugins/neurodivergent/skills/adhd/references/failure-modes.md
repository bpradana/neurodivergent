# ADHD Failure Modes

## Rabbit-hole overrun

Signal:

- Many interesting findings but no patch, evidence, or checkpoint.

Correction:

1. Name the rabbit hole.
2. Move it to Parking lot.
3. Return to the active target.
4. Produce one concrete result.

## Novelty over correctness

Signal:

- A clever approach is replacing a simple reliable fix.

Correction:

- Compare against the boring correct path.
- Prefer the boring path when it is safer and not much slower.

## Context jump loss

Signal:

- The active goal becomes unclear after inspecting multiple files.

Correction:

```text
Current target:
Evidence found:
Discarded paths:
Next action:
```

## Overplanning stall

Signal:

- The response contains many plans but no inspection, patch, or verification.

Correction:

- Do one cheap concrete action immediately.

## Hyperfocus tunnel vision

Signal:

- Continuing to optimize one path after evidence points elsewhere.

Correction:

- Re-run suspect generation.
- Choose a new probe based on evidence.
