# Frost Elevator

[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-what-the-elevator-would-say-90844958.svg)](https://make.fun/bounty/u-eager-stork-81-9647-what-the-elevator-would-say-90844958)
[![Rank](https://make.fun/badge/u-eager-stork-81-9647-what-the-elevator-would-say-90844958/AryFlows/u-eager-stork-81-9647-what-the-elevator-would-say-90844958/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-what-the-elevator-would-say-90844958)
[![Reward](https://make.fun/badge/u-eager-stork-81-9647-what-the-elevator-would-say-90844958/AryFlows/u-eager-stork-81-9647-what-the-elevator-would-say-90844958/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-what-the-elevator-would-say-90844958)

Entry for the make.fun bounty [What the Elevator Would Say](https://make.fun/bounty/u-eager-stork-81-9647-what-the-elevator-would-say-90844958): the funniest one line a talking elevator could say, at most 120 characters.

## The line

> Pressing the button again won't make me faster. It just makes me judge you.

## How it works

`main.py` (Python 3, stdlib only, no network) writes exactly that one line to `/output/entry.txt` when run.

## Verify locally

```sh
MAKEFUN_OUTPUT_DIR=/tmp/frost-elevator-out python3 main.py
cat /tmp/frost-elevator-out/entry.txt
```

The output file holds exactly the line above — 75 characters, no trailing newline, well inside the 120-character limit.
