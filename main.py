#!/usr/bin/env python3
"""Write one deadpan one-star review of an everyday essential to /output/entry.txt.

The review is a single line, 101 characters, about the moon: it works nights
only, vanishes for a week every month, and still gets songs written about it.
The deadpan register is deliberate: the line states the grievance flatly
(never on time, regularly absent) and lets the sting land in the last few
words, with no winking or exclamation. The moon was picked over gravity, the
sun, and sleep because those angles were already taken by other entries.
The program writes to the absolute path /output/entry.txt (creating /output if
needed) with an atomic write, so it behaves the same from any working directory.
Standard library only; deterministic output.
"""

import os

LINE = "The moon works nights only, disappears for a week every month, and still gets songs written about it."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    tmp = "/output/.entry.txt.tmp"
    with open(tmp, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.replace(tmp, "/output/entry.txt")


if __name__ == "__main__":
    main()
