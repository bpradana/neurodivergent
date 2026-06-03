# Neurodivergent Codex Plugin

`neurodivergent` is a Codex plugin that bundles three diagnosis-shaped coding styles:

- `$adhd`: divergent momentum, focused work bursts, save extra tasks for later, keep moving when stuck.
- `$autism`: literal interpretation, system mapping, rules that must stay true, edge-case precision, ambiguity rejection.
- `$audhd`: fast branching plus strict correctness, focused work, explicit rules, controlled finish.

It gives Codex diagnosis-shaped ways to work on code.

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
$adhd debug this with top suspects, one weird cheap check, then converge.
$autism review this PR for rules that must stay true, edge cases, and ambiguous behavior.
$audhd implement this feature with fast branches, explicit success criteria, and a checked patch.
```

## Design notes

Each skill has a compact `SKILL.md` entrypoint and detailed reference files under `references/`:

- `working-style.md`
- `execution-loop.md`
- `debugging-style.md`
- `communication-style.md`
- `pitfalls.md`

This keeps the skill trigger lightweight while allowing Codex to load more detail after a skill activates.

## Plugin-local memory hooks

The plugin includes Codex hooks that maintain lightweight plugin-local saved notes. This is separate from Codex global Memories and does not write to `~/.codex/memories/`.

The hooks persist compact state under `PLUGIN_DATA/neurodivergent-memory/`:

- active style requested with `$adhd`, `$autism`, or `$audhd`
- current guesses
- things to revisit
- rules to keep
- checks run
- latest note

Codex plugin hooks must be reviewed and trusted before they run. After installing or updating the plugin, open `/hooks` in Codex, review the Neurodivergent hook definitions, and trust them if they match this repository.

The hook file is `hooks/hooks.json`. The scripts are Python stdlib-only:

- `hooks/session_start.py`: injects recent plugin-local state as session context.
- `hooks/user_prompt_submit.py`: tracks explicit style activation.
- `hooks/pre_compact.py`: snapshots state before compaction.
- `hooks/stop.py`: captures compact end-of-turn state.

Utility scripts:

```bash
python3 plugins/neurodivergent/scripts/inspect_memory.py --cwd "$PWD"
python3 plugins/neurodivergent/scripts/prune_memory.py --limit 200
```

For local testing without Codex, pass `--data-root /tmp/some-dir` to either utility.
