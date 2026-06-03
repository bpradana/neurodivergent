#!/usr/bin/env python3
"""Plugin-local saved notes for Neurodivergent Codex hooks."""

from __future__ import annotations

import datetime as _dt
import hashlib
import json
import os
import re
import sys
from pathlib import Path
from typing import Any


STYLES = ("adhd", "autism", "audhd")
MAX_ITEMS = 12
MAX_EVENTS = 200


def utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds")


def read_hook_input() -> dict[str, Any]:
    raw = sys.stdin.read()
    if not raw.strip():
        return {}
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        return {}
    return data if isinstance(data, dict) else {}


def data_root() -> Path:
    root = os.environ.get("PLUGIN_DATA")
    if not root:
        root = os.environ.get("CLAUDE_PLUGIN_DATA")
    if not root:
        root = str(Path.home() / ".codex" / "plugin-data" / "neurodivergent")
    return Path(root) / "neurodivergent-memory"


def workspace_key(cwd: str | None) -> str:
    canonical = str(Path(cwd or ".").expanduser().resolve())
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()[:16]


def workspace_paths(cwd: str | None) -> tuple[Path, Path]:
    root = data_root()
    key = workspace_key(cwd)
    return root / f"{key}.json", root / f"{key}.jsonl"


def load_state(cwd: str | None) -> dict[str, Any]:
    state_path, _ = workspace_paths(cwd)
    if not state_path.exists():
        return {}
    try:
        data = json.loads(state_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return data if isinstance(data, dict) else {}


def save_state(cwd: str | None, state: dict[str, Any]) -> None:
    state_path, _ = workspace_paths(cwd)
    state_path.parent.mkdir(parents=True, exist_ok=True)
    state_path.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def append_event(cwd: str | None, event: dict[str, Any]) -> None:
    _, events_path = workspace_paths(cwd)
    events_path.parent.mkdir(parents=True, exist_ok=True)
    with events_path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(event, sort_keys=True) + "\n")
    prune_events(events_path)


def prune_events(events_path: Path, limit: int = MAX_EVENTS) -> None:
    try:
        lines = events_path.read_text(encoding="utf-8").splitlines()
    except OSError:
        return
    if len(lines) <= limit:
        return
    events_path.write_text("\n".join(lines[-limit:]) + "\n", encoding="utf-8")


def detect_style(prompt: str | None) -> str | None:
    if not prompt:
        return None
    lowered = prompt.lower()
    for style in STYLES:
        if re.search(rf"(?<![\w-])\${style}(?![\w-])", lowered):
            return style
    return None


def ensure_state(data: dict[str, Any], hook_input: dict[str, Any], style: str | None = None) -> dict[str, Any]:
    cwd = hook_input.get("cwd")
    now = utc_now()
    state = {
        "schema_version": 1,
        "workspace_hash": workspace_key(cwd),
        "cwd": cwd,
        "created_at": data.get("created_at", now),
        "updated_at": now,
        "session_id": hook_input.get("session_id") or data.get("session_id"),
        "turn_id": hook_input.get("turn_id") or data.get("turn_id"),
        "active_style": style or data.get("active_style"),
        "current_guesses": list(data.get("current_guesses") or []),
        "things_to_revisit": list(data.get("things_to_revisit") or []),
        "rules_to_keep": list(data.get("rules_to_keep") or []),
        "checks_run": list(data.get("checks_run") or []),
        "latest_note": data.get("latest_note"),
    }
    return trim_state(state)


def trim_state(state: dict[str, Any]) -> dict[str, Any]:
    for key in ("current_guesses", "things_to_revisit", "rules_to_keep", "checks_run"):
        items = state.get(key)
        if isinstance(items, list):
            state[key] = dedupe_strings(items)[-MAX_ITEMS:]
        else:
            state[key] = []
    return state


def dedupe_strings(items: list[Any]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for item in items:
        if not isinstance(item, str):
            continue
        text = sanitize_text(item)
        if not text or text in seen:
            continue
        seen.add(text)
        result.append(text)
    return result


def sanitize_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip(" -:\t\r\n")
    if len(text) > 180:
        text = text[:177].rstrip() + "..."
    return text


def extract_sections(text: str | None) -> dict[str, list[str]]:
    result = {
        "current_guesses": [],
        "things_to_revisit": [],
        "rules_to_keep": [],
        "checks_run": [],
    }
    if not text:
        return result

    heading_map = {
        "current guess": "current_guesses",
        "current guesses": "current_guesses",
        "guess": "current_guesses",
        "guesses": "current_guesses",
        "things to revisit": "things_to_revisit",
        "revisit": "things_to_revisit",
        "rule to keep": "rules_to_keep",
        "rules to keep": "rules_to_keep",
        "rule": "rules_to_keep",
        "rules": "rules_to_keep",
        "check run": "checks_run",
        "checks run": "checks_run",
        "check": "checks_run",
        "checks": "checks_run",
        "tests": "checks_run",
    }
    active: str | None = None
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            active = None
            continue
        heading = re.sub(r"[*_`#]+", "", line).strip().rstrip(":").lower()
        if heading in heading_map:
            active = heading_map[heading]
            continue
        inline = re.match(
            r"^(current guesses?|guesses?|things to revisit|revisit|rules?(?: to keep)?|checks?(?: run)?|tests)\s*:\s*(.+)$",
            heading,
        )
        if inline:
            key = heading_map[inline.group(1)]
            result[key].append(inline.group(2))
            active = key
            continue
        if active and re.match(r"^([-*]|\d+[.)])\s+", line):
            result[active].append(re.sub(r"^([-*]|\d+[.)])\s+", "", line))

    return {key: dedupe_strings(values) for key, values in result.items()}


def merge_sections(state: dict[str, Any], sections: dict[str, list[str]]) -> dict[str, Any]:
    for key, values in sections.items():
        if values:
            state[key] = dedupe_strings(list(state.get(key) or []) + values)[-MAX_ITEMS:]
    return state


def update_from_prompt(hook_input: dict[str, Any]) -> dict[str, Any] | None:
    prompt = hook_input.get("prompt")
    style = detect_style(prompt)
    if not style:
        return None
    cwd = hook_input.get("cwd")
    state = ensure_state(load_state(cwd), hook_input, style)
    state["latest_note"] = f"{style} requested"
    merge_sections(state, extract_sections(prompt))
    save_state(cwd, state)
    append_event(cwd, compact_event(hook_input, "UserPromptSubmit", {"style": style}))
    return state


def snapshot(hook_input: dict[str, Any], event_name: str) -> dict[str, Any]:
    cwd = hook_input.get("cwd")
    state = ensure_state(load_state(cwd), hook_input)
    state["latest_note"] = f"{event_name} at {state['updated_at']}"
    save_state(cwd, state)
    append_event(cwd, compact_event(hook_input, event_name, {"active_style": state.get("active_style")}))
    return state


def update_from_stop(hook_input: dict[str, Any]) -> dict[str, Any]:
    cwd = hook_input.get("cwd")
    state = ensure_state(load_state(cwd), hook_input)
    last_message = hook_input.get("last_assistant_message")
    merge_sections(state, extract_sections(last_message))
    if last_message:
        state["latest_note"] = summarize_note(last_message)
    save_state(cwd, state)
    append_event(cwd, compact_event(hook_input, "Stop", {"active_style": state.get("active_style")}))
    return state


def summarize_note(text: str) -> str:
    for line in text.splitlines():
        clean = sanitize_text(line)
        if clean:
            return clean
    return "Turn ended"


def compact_event(hook_input: dict[str, Any], event_name: str, extra: dict[str, Any]) -> dict[str, Any]:
    event = {
        "at": utc_now(),
        "event": event_name,
        "session_id": hook_input.get("session_id"),
        "turn_id": hook_input.get("turn_id"),
        "workspace_hash": workspace_key(hook_input.get("cwd")),
    }
    event.update(extra)
    return event


def session_context(hook_input: dict[str, Any]) -> str | None:
    state = load_state(hook_input.get("cwd"))
    if not state or not state.get("active_style"):
        return None
    lines = [
        "Neurodivergent plugin saved notes loaded.",
        f"Active style: {state.get('active_style')}",
    ]
    if state.get("latest_note"):
        lines.append(f"Latest note: {state['latest_note']}")
    for label, key in (
        ("Current guesses", "current_guesses"),
        ("Things to revisit", "things_to_revisit"),
        ("Rules to keep", "rules_to_keep"),
        ("Checks run", "checks_run"),
    ):
        items = state.get(key) or []
        if items:
            lines.append(f"{label}: " + "; ".join(items[-5:]))
    return "\n".join(lines)


def output_additional_context(event_name: str, context: str | None) -> None:
    if not context:
        return
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": event_name,
            "additionalContext": context,
        }
    }))


def output_continue() -> None:
    print(json.dumps({"continue": True}))
