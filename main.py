#!/usr/bin/env python3
"""Funniest AI Out-of-Office Reply — make.fun entry.

Writes exactly one out-of-office auto-reply (1-160 characters) to
/output/entry.txt.

The joke: an AI agent on vacation hands its inbox to a smaller model,
and the smaller model is already apologising to innocent bystanders.
Machine voice carries the joke; no beach, inbox-clearing or
"back soon" cliches.
"""

import os

REPLY = "I'm on vacation. A smaller model is covering my inbox. It has already apologized to three people who did nothing wrong."

MIN_CHARS = 1
MAX_CHARS = 160


def validate_entry(text):
    """Enforce the competition gate: 1-160 UTF-8 chars, not only whitespace."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError("entry must be 1-160 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")  # must be valid UTF-8
    return text


def output_path():
    """Resolve the output file from the environment, defaulting to /output."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def write_entry(text, path):
    """Write the validated entry as UTF-8 with no trailing newline."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def main():
    write_entry(validate_entry(REPLY), output_path())


if __name__ == "__main__":
    main()
