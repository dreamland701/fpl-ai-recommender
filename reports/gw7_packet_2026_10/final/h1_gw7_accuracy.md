# SFT accuracy ledger: classic vs SFT as written vs SFT average

1-week points forecasts scored against actual points. RMSE is the one that matters for expected-points decisions; bias is forecast minus actual (negative = under-forecast). "Closer" = share of player-weeks where that SFT version lands nearer the actual than classic.

## H1 GW7 final (live shadow, final corpus 2026-10-16)

| Set | Player-weeks | RMSE classic / written / average | MAE classic / written / average | Bias classic / written / average | Closer than classic: written / average |
|---|---|---|---|---|---|
| All | 667 | 1.995 / 2.028 / 2.028 | 1.113 / 1.193 / 1.193 | -0.02 / -0.35 / -0.35 | 49% / 49% |
| GW7 | 667 | 1.995 / 2.028 / 2.028 | 1.113 / 1.193 / 1.193 | -0.02 / -0.35 / -0.35 | 49% / 49% |
| With text evidence | 562 | 2.157 / 2.184 / 2.184 | 1.268 / 1.299 / 1.299 | -0.05 / -0.36 / -0.36 | 53% / 53% |
| No text evidence | 105 | 0.617 / 0.770 / 0.770 | 0.285 / 0.623 / 0.623 | +0.16 / -0.27 / -0.27 | 28% / 28% |
| Classic forecast >= 4 (decision-relevant) | 21 | 3.673 / 3.643 / 3.643 | 3.263 / 3.257 / 3.257 | +0.88 / +0.67 / +0.67 | 57% / 57% |

