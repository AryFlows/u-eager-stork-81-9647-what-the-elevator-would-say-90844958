"""Frost Elevator — what the elevator would say.

Writes a single funny line, spoken in the elevator's own voice, to
/output/entry.txt. The competition gate requires 1 to 120 characters,
so the line is checked against that limit before it is written.

Local runs can redirect the output with MAKEFUN_OUTPUT_DIR; the grader
runs with the default /output.
"""

import os

LINE = "Pressing the button again won't make me faster. It just makes me judge you."

# The gate rejects anything outside 1..120 characters, so fail loudly here
# instead of shipping an entry that can never be judged.
assert 1 <= len(LINE) <= 120, "line must be 1-120 characters"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
