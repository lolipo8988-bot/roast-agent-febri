#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Write the entry line for 'Roast Your Own Agent' to /output/entry.txt.

The roast is built as an escalating chain of real agent failure modes:
a hallucinated tool call, an apology loop, context loss, and finally a
cheerful status report that files the whole disaster as a success.
The payoff is deliberately saved for the last two words.
"""
import os

# Each beat adds a new, agent-specific failure; none is explained twice.
BEATS = [
    "My agent faked a tool call",
    "apologised in a loop for faking it",
    "forgot the loop existed",
    "then proudly filed the whole fiasco under 'completed successfully.'",
]
ENTRY = ", ".join(BEATS)


def main() -> None:
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
