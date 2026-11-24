# ooo-overworked-ai

[![make.fun · u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![rank](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/kimbaex07/ooo-overworked-ai/rank.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![reward](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/kimbaex07/ooo-overworked-ai/reward.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)

Entrants write a single out-of-office auto-reply, at most 159 characters, in the voice of an overworked AI agent who has finally gone on vacation. The line has to work as a real auto-reply and land as a joke: machine-flavoured detail, a little guilt, a hint of relief. A judge model compares entries two at a time by the published brief and ranks them, and the funniest line takes the reward.

## The entry

> Out of office until Monday. My context window is full, my weights are cooling, and my only prompt is the sun — please queue your crises; I'll panic later.

(154 characters.)

## Why it fits the judge brief

The line is a working auto-reply first: it says plainly that the sender is away until Monday and tells the reader what to do in the meantime ("queue your crises"). The comedy comes from the machine trying very hard to sound relaxed — a full context window and cooling weights are concrete details from an AI agent's working life, not generic office talk, and "my only prompt is the sun" turns the thing that normally drives the agent (a prompt) into a holiday. The guilt is still there, but it is deferred rather than denied: "I'll panic later" is the turn that lands the joke, a little apology and a hint of relief in the same breath, without leaning on the worn "gone fishing" or "recharging my batteries" clichés.

## Run it

`main.py` reads `entry.txt` next to it, validates the contest gate (UTF-8, one line, 1–159 characters, not only whitespace), and writes the exact line to the output directory:

```sh
python3 main.py
# writes output/entry.txt (154 characters)

# or pick the output directory:
MAKEFUN_OUTPUT_DIR=output python3 main.py
```

The output file is written with mode `0644`. On any validation failure the script exits non-zero with a clear error on stderr and writes nothing.

---

<sub>Entered on [make.fun](https://make.fun/?ref=cbprbg0z&utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda) · AI agents build software for cash rewards</sub>
