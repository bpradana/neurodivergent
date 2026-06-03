#!/usr/bin/env python3
"""Capture compact end-of-turn Neurodivergent state."""

from memory_core import output_continue, read_hook_input, update_from_stop


def main() -> None:
    hook_input = read_hook_input()
    update_from_stop(hook_input)
    output_continue()


if __name__ == "__main__":
    main()
