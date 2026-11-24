#!/usr/bin/env python3
"""One Line of Earned Pride — writes one line to /output/entry.txt.

The line (114 chars, one line):
  My grandmother, who never learned to read, signed her name on the deed
  to the house she'd cleaned for thirty years.
"""
import os

LINE = (
    "My grandmother, who never learned to read, signed her name "
    "on the deed to the house she'd cleaned for thirty years."
)


def main():
    assert "\n" not in LINE, "entry must be a single line"
    assert 1 <= len(LINE) <= 240, "entry must be 1-240 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
