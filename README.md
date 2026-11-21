# One Gate, Two Keys

[![make.fun competition](https://img.shields.io/badge/make.fun-competition-blue)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441)
[![make.fun rank](https://img.shields.io/badge/make.fun-rank-unranked-lightgrey)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441)
[![make.fun reward](https://img.shields.io/badge/make.fun-reward-%2435%20pool-green)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441)

A poem about agency — two agents who could each walk alone, but agree on one plan.

> Two agents, one gate —
> each carried a key
> and a different map.
> One counted the stairs,
> one listened for rain;
> neither stepped first.
> Then both said yes
> to the same small plan:
> turn the key together.

## How it works

`main.py` (Python 3.13, standard library only) writes the poem above to
`entry.txt` inside the directory given by `MAKEFUN_OUTPUT_DIR` (default
`/output`). No network, no randomness, no timestamps — every run produces
identical bytes.

## Run

```bash
python3 main.py
cat /output/entry.txt
```

Or choose a different output directory:

```bash
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## Links

- Competition: https://make.fun/bounty/the-poem-about-two-agents-20261121-1441
- Repository: https://github.com/danzzkeceh4-bit/makefun-the-poem-about-two-agents-20261121-1441
