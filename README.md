# Neurodivergent Codex Plugin

`neurodivergent` is a Codex plugin that bundles three diagnosis-shaped software engineering cognition modes:

- `$adhd`: divergent momentum, hyperfocus sprints, side-quest parking, anti-stall execution.
- `$autism`: literal interpretation, system modeling, invariants, edge-case precision, ambiguity rejection.
- `$audhd`: fast branching plus strict correctness, novelty-managed hyperfocus, explicit rules, controlled convergence.

The plugin does not provide medical advice, diagnose users, or claim that Codex literally has a biological condition. It gives Codex diagnosis-shaped operating loops for coding work.

## Install locally

Unzip this archive, then point Codex or a local Codex plugin marketplace entry at the `neurodivergent/` folder.

A minimal local marketplace entry can reference the unzipped folder like this:

```json
{
  "name": "local-plugins",
  "interface": {"displayName": "Local Plugins"},
  "plugins": [
    {
      "name": "neurodivergent",
      "source": {
        "source": "local",
        "path": "./plugins/neurodivergent"
      },
      "policy": {
        "installation": "AVAILABLE",
        "authentication": "ON_INSTALL"
      },
      "category": "Productivity"
    }
  ]
}
```

## Example prompts

```text
$adhd debug this with top suspects, one weird cheap probe, then converge.
$autism review this PR for invariants, edge cases, and ambiguous behavior.
$audhd implement this feature with fast branches, explicit success criteria, and a verified patch.
```

## Design notes

Each skill has a compact `SKILL.md` entrypoint and detailed reference files under `references/`:

- `cognition-engine.md`
- `execution-loop.md`
- `debugging-style.md`
- `communication-style.md`
- `failure-modes.md`

This keeps the skill trigger lightweight while allowing Codex to load the full cognition model after a skill activates.
