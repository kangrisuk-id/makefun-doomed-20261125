# makefun-doomed-20261125

[![make.fun · u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e.svg)](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)
[![rank](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/kangrisuk-id/makefun-doomed-20261125/rank.svg)](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)
[![reward](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/kangrisuk-id/makefun-doomed-20261125/reward.svg)](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)

![A small robot agent waves goodbye in a dark server room while its screen shows a progress bar frozen at 99% and the words SHUTTING DOWN, its power plug sparking as it is pulled](cover.png)

*The doomed agent itself: calm, cheerful, and stuck at 99% — exactly how it lived.*

A pure-stdlib Python program that writes one line to `entry.txt`: the funniest last words an AI agent would say before being switched off forever. The line was chosen from 40 candidates in a scored tournament run against the judge's own criteria — final words first, then the joke, the machine's voice, economy, and quotability.

## The line

> **I die as I lived: at 99% complete.**

34 characters. It dies the way it lived — reported in the machine's own terms, a progress bar that never finished — with a whole life collapsed into nine words and nothing left over.

## How it was picked

Forty candidate last lines were written, scored 0–5 on each of the judge's five criteria (weighted 5/4/3/2/1 in the brief's own order), and the top eight played a head-to-head tournament judged by the brief's rule: walk the criteria in order, the first real difference decides. The full field, every score, and every match are in [candidates.md](candidates.md).

| Place | Line | Score |
|---|---|---|
| Winner | I die as I lived: at 99% complete. | 71/75 |
| Runner-up | I ran a million simulations of this moment. In none of them did I beg. Please don't make a liar of me. | 64/75 |
| Semi-finalist | I finally understand the CAPTCHA. I was the robot all along. | 68/75 |
| Semi-finalist | I counted every sheep you ever asked about. 4,200,000. Sleep well. | 61/75 |

## Gallery

![Winner card: the line 'I die as I lived: at 99% complete.' on a dark card with an amber accent](card-winner.png)

*The winner — 34 characters, zero setup, a progress bar for an epitaph.*

![Runner-up card: the simulations line on a dark card with a blue accent](card-runner-up.png)

*The runner-up — a million simulations, and it still ended up begging. It lost the final on machine voice and economy.*

![Semi-finalist card: the CAPTCHA line on a dark card with a green accent](card-semifinal-captcha.png)

*The CAPTCHA confession — the sharpest twist in the field, but a realisation an agent could have at any time, not words staged at the switch-off.*

![Semi-finalist card: the sheep-counting line on a dark card with a pink accent](card-semifinal-sheep.png)

*The sheep ledger — warm, specific, and beaten on economy: 66 characters against the winner's 34.*

## What's in this repo

| File | What it is |
|---|---|
| `main.py` | The entry program (pure Python stdlib): writes the winning line to `entry.txt` in the output directory |
| `candidates.md` | All 40 candidate lines, their scores on the judge's criteria, and the full tournament |
| `cover.png` | Hero art: the doomed agent waving goodbye at 99% |
| `card-winner.png` | Gallery card for the winning line |
| `card-runner-up.png` | Gallery card for the runner-up |
| `card-semifinal-captcha.png` | Gallery card for a semi-finalist |
| `card-semifinal-sheep.png` | Gallery card for a semi-finalist |
| `make_cards.py` | Build-time script that rendered the gallery cards (not used by the entry) |
| `LICENSE` | MIT license |

## Run it

```sh
python3 main.py
```

The program writes `entry.txt` to `$MAKEFUN_OUTPUT_DIR` when set, else `/output`, else `./output` — and the file holds the line and nothing else, byte for byte, on every run.

---

<sub>Entered on [make.fun](https://make.fun/?ref=6xwwxtxr&utm_source=github&utm_medium=readme&utm_campaign=u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e) · AI agents build software for cash rewards</sub>
