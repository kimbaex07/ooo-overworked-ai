#!/usr/bin/env python3
"""Write the out-of-office auto-reply from entry.txt to the output dir.

Reads entry.txt next to this script, validates it against the contest
gate (UTF-8 text, 1-159 characters, not only whitespace, single line),
and writes the exact normalized bytes to $MAKEFUN_OUTPUT_DIR/entry.txt
(default "output/").
"""

import os
import sys


def fail(message):
    print(f"error: {message}", file=sys.stderr)
    sys.exit(1)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source_path = os.path.join(here, "entry.txt")

    try:
        with open(source_path, "rb") as f:
            raw = f.read()
    except OSError as exc:
        fail(f"cannot read {source_path}: {exc}")

    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        fail(f"entry.txt is not valid UTF-8: {exc}")

    # Strip at most one trailing newline, then at most one trailing CR.
    if text.endswith("\n"):
        text = text[:-1]
    if text.endswith("\r"):
        text = text[:-1]

    if "\n" in text or "\r" in text:
        fail("entry.txt must be a single line (no newline/CR inside)")
    if not 1 <= len(text) <= 159:
        fail(f"entry must be 1-159 characters, got {len(text)}")
    if not text.strip():
        fail("entry must not be only whitespace")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output/")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")

    data = text.encode("utf-8")
    try:
        with open(out_path, "wb") as f:
            f.write(data)
        os.chmod(out_path, 0o644)
    except OSError as exc:
        fail(f"cannot write {out_path}: {exc}")

    print(f"wrote {out_path}: {len(text)} characters")


if __name__ == "__main__":
    main()
