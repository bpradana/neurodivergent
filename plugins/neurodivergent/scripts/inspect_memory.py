#!/usr/bin/env python3
"""Inspect Neurodivergent plugin-local memory."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
HOOKS_DIR = SCRIPT_DIR.parent / "hooks"
sys.path.insert(0, str(HOOKS_DIR))

from memory_core import data_root, load_state, workspace_paths  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Inspect Neurodivergent plugin-local memory.")
    parser.add_argument("--cwd", default=os.getcwd(), help="Workspace path to inspect.")
    parser.add_argument("--data-root", help="Override PLUGIN_DATA for inspection.")
    parser.add_argument("--events", action="store_true", help="Print the workspace event log too.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.data_root:
        os.environ["PLUGIN_DATA"] = args.data_root

    state = load_state(args.cwd)
    print(json.dumps({
        "data_root": str(data_root()),
        "cwd": str(Path(args.cwd).resolve()),
        "state": state,
    }, indent=2, sort_keys=True))

    if args.events:
        _, events_path = workspace_paths(args.cwd)
        if events_path.exists():
            print(events_path.read_text(encoding="utf-8"), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
