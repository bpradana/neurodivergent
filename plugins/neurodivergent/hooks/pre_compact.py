#!/usr/bin/env python3
"""Snapshot Neurodivergent state before compaction."""

from memory_core import output_continue, read_hook_input, snapshot


def main() -> None:
    hook_input = read_hook_input()
    snapshot(hook_input, "PreCompact")
    output_continue()


if __name__ == "__main__":
    main()
