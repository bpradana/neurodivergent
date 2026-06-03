#!/usr/bin/env python3
"""Track explicit Neurodivergent style requests."""

from memory_core import read_hook_input, update_from_prompt


def main() -> None:
    hook_input = read_hook_input()
    update_from_prompt(hook_input)


if __name__ == "__main__":
    main()
