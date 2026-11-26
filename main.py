"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

import os

TEXT = "The plumber flooded the bathroom and now the floor's up, I have to stay home till it's dry."


def main() -> None:
    # Fail fast if the entry ever stops meeting the gate (1-140 chars,
    # at most 20 words, single line, not only whitespace): a bad line
    # must never be written.
    if not TEXT.strip() or len(TEXT) > 140 or len(TEXT.split()) > 20 or "\n" in TEXT:
        raise SystemExit("entry line violates the 1-140 character / 20-word single-line gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

# Revision note: entry kept as written — one line, 91 characters, 18 words;
# a boring, specific household disaster (flooded bathroom, floor up) whose own
# logic — waiting for a floor to dry — quietly covers the whole launch week.
