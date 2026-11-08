# SFT accuracy ledger: classic vs SFT as written vs SFT average

1-week points forecasts scored against actual points. RMSE is the one that matters for expected-points decisions; bias is forecast minus actual (negative = under-forecast). "Closer" = share of player-weeks where that SFT version lands nearer the actual than classic.

## 2026-27 GW6

| Set | Player-weeks | RMSE classic / written / average | MAE classic / written / average | Bias classic / written / average | Closer than classic: written / average |
|---|---|---|---|---|---|
| All | 667 | 2.018 / 2.052 / 2.019 | 1.094 / 1.094 / 1.189 | -0.03 / -0.30 / +0.05 | 43% / 31% |
| GW6 | 667 | 2.018 / 2.052 / 2.019 | 1.094 / 1.094 / 1.189 | -0.03 / -0.30 / +0.05 | 43% / 31% |
| With text evidence | 511 | 2.002 / 2.026 / 2.005 | 1.127 / 1.113 / 1.211 | +0.07 / -0.22 / +0.13 | 48% / 33% |
| No text evidence | 156 | 2.073 / 2.133 / 2.063 | 0.987 / 1.031 / 1.119 | -0.36 / -0.54 / -0.20 | 26% / 22% |
| Classic forecast >= 4 (decision-relevant) | 22 | 4.036 / 4.046 / 4.034 | 3.501 / 3.223 / 3.433 | +0.20 / -0.60 / +0.08 | 64% / 64% |

