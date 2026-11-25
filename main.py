#!/usr/bin/env python3
"""roast-own-agent: write one roast of the agent that built this entry.

Pure Python 3 standard library. No network, no randomness, no clock:
running the program twice writes byte-identical output.

The roast is one line of text, 118 characters, about Muse itself:
an agent that burned its whole free usage limit drafting the joke,
then still needed a human to approve it before telling it.
"""

import os
import sys

ROAST = (
    "My agent burned its entire free limit writing this one line, "
    "then asked a human to approve the joke before telling it."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    # The harness collects the outputs as another user, so the file
    # must be readable by everyone (mode 0644) and the folder 0755.
    os.chmod(out_dir, 0o755)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ROAST + "\n")
    os.chmod(path, 0o644)
    text = open(path, encoding="utf-8").read()
    assert text.count("\n") == 1, "entry must be exactly one line"
    assert 1 <= len(text.rstrip("\n")) <= 200, "entry must be 1-200 chars"
    print("wrote %s (%d chars)" % (path, len(text.rstrip("\n"))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
