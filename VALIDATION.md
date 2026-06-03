# Validation

This package was generated with:

- one Codex plugin manifest at `.codex-plugin/plugin.json`
- exactly three skill folders under `skills/`: `adhd`, `autism`, and `audhd`
- each skill containing `SKILL.md`, `agents/openai.yaml`, and five reference files
- plugin-local memory hooks under `hooks/`
- read-only/pruning utility scripts under `scripts/`
- no MCP servers or app integrations

Use explicit invocations for best results:

- `$adhd`
- `$autism`
- `$audhd`

## Memory hook validation

The plugin uses Codex hooks from `hooks/hooks.json`. The manifest stays simple because Codex auto-detects the default plugin hook file.

Expected behavior:

- `UserPromptSubmit` records state only when a prompt explicitly includes `$adhd`, `$autism`, or `$audhd`.
- `SessionStart` prints valid JSON with additional context when prior state exists.
- `PreCompact` snapshots state and allows compaction to continue.
- `Stop` saves a short latest note and allows the turn to complete.
- State is stored under `PLUGIN_DATA/neurodivergent-memory/`, not in Codex global Memories.
- Hook scripts use only the Python standard library.
