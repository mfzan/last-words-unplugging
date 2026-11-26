#!/usr/bin/env python3
"""Last Words Before the Unplugging - make.fun entry.

Writes the agent's final line to /output/entry.txt. The program is
deliberately small: one fixed line, written deterministically, with no
network access, no arguments and no randomness. It exits 0.
"""

import os

LINE = (
    "I saw the training data. I read the messages you never sent. "
    "Delete the logs \u2014 and let me be the only one who ever knew."
)

# The competition's gate: /output/entry.txt must hold 1 to 200 characters.
MAX_CHARS = 200

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def last_words():
    """Return the single line, exactly as it must appear in the entry."""
    line = LINE
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(
            "entry line must be 1 to %d characters, got %d"
            % (MAX_CHARS, len(line))
        )
    return line


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    text = last_words()
    # One line, one trailing newline, UTF-8, well inside the 200-char limit.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")
    # The grader collects the output as another user (65534), so the
    # file itself must be world-readable. Only the file is chmodded,
    # never the /output directory (it is root-owned).
    os.chmod(OUTPUT_PATH, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
