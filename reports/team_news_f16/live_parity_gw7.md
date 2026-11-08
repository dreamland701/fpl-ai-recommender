# F16 live parity, 2026-27 GW7

## 1. Category parity (live parser vs table builder)

```
article: Premier League team news: predicted lineups for the weekend action | published 2026-10-16T18:07:45+00:00 (15.9 h before the deadline) | https://www.theguardian.com/football/2026/oct/16/premier-league-team-news-predicted-lineups-for-the-weekend-action
```

live keys 667, table keys 634, identical 633/668; differences 35

| key | table | live |
|---|---|---|
| 2026-27|7|131 | None | XI |
| 2026-27|7|162 | None | sub |
| 2026-27|7|325 | None | doubtful |
| 2026-27|7|412 | None | XI |
| 2026-27|7|413 | None | XI |
| 2026-27|7|414 | None | injured |
| 2026-27|7|415 | None | injured |
| 2026-27|7|416 | None | injured |
| 2026-27|7|417 | None | sub |
| 2026-27|7|418 | None | XI |
| 2026-27|7|419 | None | XI |
| 2026-27|7|420 | None | XI |
| 2026-27|7|421 | None | XI |
| 2026-27|7|422 | None | injured |
| 2026-27|7|423 | None | doubtful |
| 2026-27|7|424 | None | sub |
| 2026-27|7|425 | None | XI |
| 2026-27|7|426 | None | XI |
| 2026-27|7|427 | None | XI |
| 2026-27|7|428 | None | XI |
| 2026-27|7|429 | None | XI |
| 2026-27|7|43 | None | XI |
| 2026-27|7|430 | None | sub |
| 2026-27|7|431 | None | XI |
| 2026-27|7|432 | None | doubtful |
| 2026-27|7|433 | None | injured |
| 2026-27|7|434 | None | XI |
| 2026-27|7|435 | None | sub |
| 2026-27|7|436 | None | XI |
| 2026-27|7|437 | None | XI |
| 2026-27|7|438 | None | XI |
| 2026-27|7|439 | None | injured |
| 2026-27|7|440 | None | sub |
| 2026-27|7|441 | None | XI |
| 2026-27|7|668 | sub | None |

## 2. Frame parity

feature columns 80, gn_* in model: ['gn_article', 'gn_xi', 'gn_sub', 'gn_doubtful', 'gn_out']

players in both frames 667; live gn_* means {'gn_article': 1.0, 'gn_xi': 0.532, 'gn_sub': 0.339, 'gn_doubtful': 0.036, 'gn_out': 0.093}; table week means {'gn_article': 0.949, 'gn_xi': 0.503, 'gn_sub': 0.331, 'gn_doubtful': 0.031, 'gn_out': 0.084}
mismatches per column: {'gn_article': 34, 'gn_xi': 19, 'gn_sub': 6, 'gn_doubtful': 3, 'gn_out': 6}
gn_* in the frame without the live file: {'gn_article': 0.0, 'gn_xi': 0.0, 'gn_sub': 0.0, 'gn_doubtful': 0.0, 'gn_out': 0.0} (expect all 0)

## 3. Forecast movement from the live categories (classic+F6+F16 with vs without the article)

| category | n | mean Δ GW pts | mean Δ minutes |
|---|---|---|---|
| XI | 355 | +0.066 | +1.6 |
| doubtful | 24 | -0.106 | -2.6 |
| out | 62 | -0.197 | -3.3 |
| sub | 226 | -0.114 | -4.2 |

Largest moves:

- Scott (out): GW -0.43, minutes -9.0 (now 1.79 / 23)
- Igor Jesus (out): GW -0.43, minutes -9.0 (now 0.55 / 8)
- Hincapie (out): GW -0.43, minutes -5.4 (now 0.08 / 0)
- Isak (out): GW -0.43, minutes -9.0 (now 1.77 / 18)
- Gravenberch (out): GW -0.43, minutes -9.0 (now 1.54 / 31)
- Ekitiké (out): GW -0.43, minutes -4.3 (now 0.47 / 0)
- Bentancur (out): GW -0.43, minutes -9.0 (now 1.42 / 25)
- Elanga (out): GW -0.43, minutes -8.1 (now 0.33 / 0)
- Tzolis (out): GW -0.43, minutes -9.0 (now 1.17 / 20)
- Dorgu (out): GW -0.43, minutes -9.0 (now 0.58 / 6)
- Gakpo (out): GW -0.43, minutes -9.0 (now 1.79 / 23)
- Ballard (out): GW -0.43, minutes -9.0 (now 0.98 / 23)
