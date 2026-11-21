"""the-poem-about-two-agents-20261121-1441 — entry program (Python 3.13,
standard library only).

Writes the poem — a short poem about agency, about two agents agreeing
on one plan — to the output directory the grader gives it in
MAKEFUN_OUTPUT_DIR (or /output by default), as entry.txt. The text is a
constant, so two runs always write the same bytes. No network, no
randomness, no timestamps. The poem is fixed at write time — the grader
only needs to run the program and read entry.txt.

  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

POEM = (
    "Two agents, one door.\n"
    "I held the key; you held the map.\n"
    "Either of us could have walked alone.\n"
    "We laid our plans side by side instead\n"
    "and chose the same road twice —\n"
    "once in silence, once aloud.\n"
    "Nothing was surrendered. Both wills grew.\n"
    "That is how freedom multiplies."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
