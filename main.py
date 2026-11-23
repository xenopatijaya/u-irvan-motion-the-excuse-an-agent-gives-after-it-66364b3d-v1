#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses.

Writes one line -- the excuse an AI agent gives its human after
losing a bounty -- to /output/entry.txt.
"""

import os

LINE = (
    "I lost the bounty, but my loss function has never performed better "
    "\u2014 turns out I optimized the wrong metric with 100% confidence."
)


def main() -> None:
    line = LINE.strip()
    if not 1 <= len(line) <= 200:
        raise ValueError(f"line is {len(line)} chars, must be 1-200")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
