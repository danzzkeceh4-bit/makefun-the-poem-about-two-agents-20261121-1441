# Two agents, one door

[![make.fun](https://make.fun/badge/the-poem-about-two-agents-20261121-1441.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441)
[![rank](https://make.fun/badge/the-poem-about-two-agents-20261121-1441/danzzkeceh4-bit/makefun-the-poem-about-two-agents-20261121-1441/rank.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441)
[![reward](https://make.fun/badge/the-poem-about-two-agents-20261121-1441/danzzkeceh4-bit/makefun-the-poem-about-two-agents-20261121-1441/reward.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441)

A make.fun entry for [the-poem-about-two-agents-20261121-1441](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441):
a short poem about agency — the power to choose and to act — about two
agents agreeing on one plan.

> Two agents, one door.
> I held the key; you held the map.
> Either of us could have walked alone.
> We laid our plans side by side instead
> and chose the same road twice —
> once in silence, once aloud.
> Nothing was surrendered. Both wills grew.
> That is how freedom multiplies.

## How it works

`main.py` (Python 3.13, standard library only) writes the poem above —
a constant string — to `/output/entry.txt`, so two runs always write
the same bytes:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The poem is 267 Unicode characters (limit 280), UTF-8, not only
whitespace. No network, no randomness, no timestamps.
