#!/usr/bin/env python3
"""Load Neurodivergent plugin-local memory into session context."""

from memory_core import output_additional_context, read_hook_input, session_context


def main() -> None:
    hook_input = read_hook_input()
    output_additional_context("SessionStart", session_context(hook_input))


if __name__ == "__main__":
    main()
