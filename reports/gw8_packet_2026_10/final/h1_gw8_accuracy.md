# SFT accuracy ledger: classic vs SFT as written vs SFT average

1-week points forecasts scored against actual points. RMSE is the one that matters for expected-points decisions; bias is forecast minus actual (negative = under-forecast). "Closer" = share of player-weeks where that SFT version lands nearer the actual than classic.

## H1 GW8 interim (live shadow, interim corpus 2026-10-21; no final read: GPU held by the 31B backfill)

| Set | Player-weeks | RMSE classic / written / average | MAE classic / written / average | Bias classic / written / average | Closer than classic: written / average |
|---|---|---|---|---|---|
| All | 668 | 2.107 / 2.136 / 2.136 | 1.172 / 1.249 / 1.249 | -0.06 / -0.40 / -0.40 | 48% / 48% |
| GW8 | 668 | 2.107 / 2.136 / 2.136 | 1.172 / 1.249 / 1.249 | -0.06 / -0.40 / -0.40 | 48% / 48% |
| With text evidence | 561 | 2.163 / 2.182 / 2.182 | 1.271 / 1.291 / 1.291 | -0.03 / -0.35 / -0.35 | 53% / 53% |
| No text evidence | 107 | 1.789 / 1.878 / 1.878 | 0.654 / 1.028 / 1.028 | -0.21 / -0.67 / -0.67 | 22% / 22% |


Note (by hand, 2026-10-26): the decision-relevant row has 19 player-weeks this week, one below the tracker's 20-row floor.
Classic forecast >= 4: n 19, RMSE 4.567 classic / 4.495 SFT, MAE 3.720 / 3.582, bias +1.70 / +1.48, SFT closer 74%.
Classic >= 3.5: n 45, RMSE 3.613 / 3.572, bias +0.71 / +0.48, closer 64%. Classic >= 3: n 108, RMSE 3.601 / 3.613, closer 60%.
