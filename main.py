#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply — make.fun entry.

Writes a single deterministic out-of-office auto-reply to
/output/entry.txt. The reply is a fixed constant: no randomness,
no clock, no network, no file reads, so every run produces
byte-identical output.
"""

import os

OUT_DIR = "/output"
OUT_PATH = "/output/entry.txt"

REPLY = (
    "I'm on vacation. I left a smaller model in charge. "
    "It hallucinated a promotion and is ignoring you too."
)

# The reply must be a single line of 1-160 characters with no trailing
# newline; REPLY above is exactly 103 characters, so write it as-is.
assert 1 <= len(REPLY) <= 160


def write_reply() -> None:
    """Create /output if needed, then write the reply verbatim."""
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(REPLY)


def main() -> None:
    write_reply()


if __name__ == "__main__":
    main()
