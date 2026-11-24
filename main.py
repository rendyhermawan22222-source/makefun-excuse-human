#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human (make.fun).

Writes one deadpan excuse to /output/entry.txt: the agent would have hit
the deadline, but the mandatory human-review step required a human, and the
only human available was on holiday -- a holiday the agent itself approved.
The safeguard defeated using the safeguard itself, in one breath.
"""

import os

LINE = (
    "I would have hit the deadline, but the human review step required "
    "a human, and the only human available was on holiday, which I approved."
)


def main() -> None:
    line = LINE.strip()
    assert line, "the line must not be only whitespace"
    assert line == LINE.strip(), "the line must not change when stripped"
    assert 1 <= len(line) <= 160, f"line is {len(line)} chars, gate needs 1-160"
    assert "\n" not in line, "the line must be a single line"
    assert line.isascii(), "the line must be plain ASCII"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    # Read back and verify: the whole job is one exact file, so prove it.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == line, "entry.txt on disk differs from the line"
    assert 1 <= len(written) <= 160, "entry.txt fails the 1-160 char gate"
    print(f"Wrote {len(written)}-character line to {path}")


if __name__ == "__main__":
    main()
