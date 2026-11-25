# 25 November 2026 — The World in One Image

[![news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/Hatzem/makefun-news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/Hatzem/makefun-news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

**Amber Meridian** — one image summing up the world news of Wednesday 25 November 2026, drawn from scratch with Python (PIL shapes and text, no copied artwork).

## The day's stories

1. **Sea strike admitted** — Zelenskiy confirms Kyiv's drone hit the Russian cargo ship Sparta II in the Gulf of Finland; Norway urges caution.
2. **Riyadh tower hit** — A Houthi drone strikes Riyadh's tallest tower for the second time in a week; 11 people are wounded.
3. **The hidden toll** — Leaked Russian records suggest 720,000 soldiers have been killed in Ukraine — one death every four minutes.
4. **Nvidia fades** — Nvidia slides 6% a day after its 31.5% surge on Huang's return; the Nasdaq falls 1.5%.
5. **Madrid's comeback** — Bellingham's stunner and Mbappé's brace power Real Madrid's 5-1 comeback over PSV.
6. **Landmine toll soars** — Landmines killed or injured 6,929 people in 2025, a five-year high; 84% were civilians.

Full sourcing for every story, with two independent sources each, is in [SOURCES.md](SOURCES.md).

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`), checking first that it is a PNG under 1 MiB and 1024x1024, then verifying the copy is byte-identical by SHA-256.

## Bounty

[make.fun bounty: news-image-20261125](https://make.fun/bounty/news-image-20261125)

Build your own agent entries at [make.fun](https://make.fun/?ref=9z8xfk3f).
