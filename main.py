#!/usr/bin/env python3
"""The Vacuum's Alibi: one line, 200 characters.

Writes the excuse a robot vacuum gives for missing a spot to
/output/entry.txt (or $ENTRY_OUTPUT_DIR/entry.txt).

Standard library only, no network, deterministic.
"""

import os

LINE = (
    "I did not miss that spot. My sensors logged it as a rug, "
    "and rugs have diplomatic immunity in this house."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line must be 1-200 chars, got {len(text)}"
    assert text.strip(), "line must not be whitespace-only"
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
