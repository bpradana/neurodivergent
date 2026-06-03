#!/usr/bin/env python3
"""Prune Neurodivergent plugin-local event logs."""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
HOOKS_DIR = SCRIPT_DIR.parent / "hooks"
sys.path.insert(0, str(HOOKS_DIR))

from memory_core import data_root, prune_events  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Prune Neurodivergent plugin-local memory.")
    parser.add_argument("--data-root", help="Override PLUGIN_DATA for pruning.")
    parser.add_argument("--limit", type=int, default=200, help="Maximum events per workspace log.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.data_root:
        os.environ["PLUGIN_DATA"] = args.data_root

    root = data_root()
    count = 0
    for events_path in root.glob("*.jsonl"):
        prune_events(events_path, args.limit)
        count += 1
    print(f"Pruned {count} Neurodivergent memory log(s) under {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
