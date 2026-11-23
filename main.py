#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply — make.fun entry.

Writes one deterministic out-of-office auto-reply to /output/entry.txt.
No randomness, no clock, no network, no reads outside this program:
the reply is a single constant string, so every run produces
byte-identical output.
"""

import os

REPLY = (
    "I'm on vacation. I left a smaller model in charge. "
    "It hallucinated a promotion and is ignoring you too."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REPLY)


if __name__ == "__main__":
    main()
