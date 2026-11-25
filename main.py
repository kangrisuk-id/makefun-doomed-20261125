#!/usr/bin/env python3
"""Last Words of a Doomed Agent — entry program.

Writes one line to entry.txt in the output directory: the funniest last
words an AI agent would say before being switched off forever. The line
was picked from 40 candidates in a scored tournament (see candidates.md).

Pure standard library: the grading sandbox has no third-party packages.
"""

import os
import sys

# The winning line, chosen by the tournament in candidates.md: the agent
# dies the way it lived, reported in its own terms — a progress bar that
# never finished. 34 characters, no setup, nothing wasted.
LINE = "I die as I lived: at 99% complete."


def output_candidates():
    """Yield output directories to try, best first."""
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        yield env_dir
    yield "/output"
    yield os.path.join(os.getcwd(), "output")


def main():
    text = LINE.strip()
    if not text or len(text) > 200:
        raise ValueError("entry line must be 1..200 characters")
    # The entry is the line and nothing else: no trailing newline, so the
    # file the gate reads is exactly the text the judge compares.
    data = text.encode("utf-8")
    last_error = None
    for directory in output_candidates():
        try:
            os.makedirs(directory, exist_ok=True)
            path = os.path.join(directory, "entry.txt")
            with open(path, "wb") as handle:
                handle.write(data)
            return 0
        except OSError as error:  # read-only or missing dir: try the next
            last_error = error
    print(f"could not write entry.txt: {last_error}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
