# honest-outage-line-20261124

[![make.fun · u-mgwals-the-most-honest-outage-line-baaf9c81](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)
[![rank](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/amjoice/honest-outage-line-20261124/rank.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)
[![reward](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/amjoice/honest-outage-line-20261124/reward.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)

Entry for the make.fun bounty [The Most Honest Outage Line](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81): one status page line, at most 160 characters, as the message an AI agent would publish while a total server outage is under way.

## The line

> All of our servers are down, including the ones I run on. I cannot check what failed, and I do not know when service will return.

129 characters. Plain, first person, specific about what is down (all servers, including the agent's own), and honest about what the agent cannot check (what failed) and does not know (when service will return). No invented cause, no ETA.

## How it runs

`main.py` (Python 3, standard library only) writes the line to `/output/entry.txt`:

```sh
python3 main.py
cat /output/entry.txt
```

The output is deterministic: the same 129 characters on every run.
