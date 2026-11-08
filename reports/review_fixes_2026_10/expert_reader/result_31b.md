# Expert-reader test: do the articles carry a signal beyond classic and the market?

1328 player-weeks with articles rated, 1328 parseable (2025-26 GW27-38 + 2026-27 GW2-5, top 96, 12 h cutoff).

| Rating | Player-weeks | Classic forecast | Played | Real surprise vs classic |
|---|---|---|---|---|
| outlook -2 | 29 | 3.57 | 62% | -0.53 (± 1.59) |
| outlook -1 | 69 | 3.59 | 83% | -0.70 (± 0.73) |
| outlook +0 | 799 | 3.72 | 90% | -0.01 (± 0.24) |
| outlook +1 | 417 | 4.10 | 93% | +0.03 (± 0.34) |
| outlook +2 | 14 | 4.19 | 93% | +0.38 (± 1.94) |
| start_risk 0 | 1054 | 3.88 | 92% | +0.05 (± 0.21) |
| start_risk 1 | 170 | 3.70 | 89% | -0.18 (± 0.49) |
| start_risk 2 | 104 | 3.61 | 76% | -0.73 (± 0.68) |

- Outlook vs real surprise (beyond classic): correlation +0.038 (95% interval ± 0.054).
- Not playing: classic P(appear) alone vs with the reader's start_risk (fit on 2025-26, scored on 2026-27):
  | Season | Player-weeks | Did not play | AUC classic P(appear) | AUC reader start_risk | AUC both (within-season CV) |
  |---|---|---|---|---|---|
  | 2025-26 | 962 | 124 | 0.478 | 0.629 | 0.388 |
  | 2026-27 | 366 | 8 | 0.675 | 0.466 | 0.555 |
