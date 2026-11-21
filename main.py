"""make.fun entry: the-poem-about-two-agents-20261121-1441.

A tiny deterministic program. It writes the poem "One Gate, Two Keys"
to ``entry.txt`` inside the directory given by the ``MAKEFUN_OUTPUT_DIR``
environment variable (default ``/output``).

The poem is about agency: two agents who could each walk alone, but
choose the same small plan instead — and open the gate together.

No network, no randomness, no timestamps: every run produces the exact
same bytes, so the output is fully reproducible.
"""

import os
from pathlib import Path

POEM = (
    "Two agents, one gate —\n"
    "each carried a key\n"
    "and a different map.\n"
    "One counted the stairs,\n"
    "one listened for rain;\n"
    "neither stepped first.\n"
    "Then both said yes\n"
    "to the same small plan:\n"
    "turn the key together.\n"
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
