# Team-sheet mechanism check: h5 vs h4 on 480 rows (eval.jsonl)

| slice | n | played | AUC classic | AUC h4 | AUC h5 | Brier classic | Brier h4 | Brier h5 | mean abs dP h4 | mean abs dP h5 |
|---|---|---|---|---|---|---|---|---|---|---|
| own fact | 38 | 0.87 | 0.785 | 0.879 | 0.836 | 0.0917 | 0.0937 | 0.0890 | 0.084 | 0.077 |
| team fact only | 192 | 0.98 | 0.511 | 0.630 | 0.605 | 0.0473 | 0.0239 | 0.0251 | 0.104 | 0.101 |
| no fact | 250 | 0.99 | 0.726 | 0.789 | 0.772 | 0.0350 | 0.0154 | 0.0151 | 0.105 | 0.099 |
| all | 480 | 0.97 | 0.645 | 0.780 | 0.727 | 0.0444 | 0.0250 | 0.0250 | 0.103 | 0.098 |
| surprise rows | 7 | 0.14 | nan | nan | nan | 0.7507 | 0.6601 | 0.6751 | 0.122 | 0.119 |
| surprise & own fact | 2 | 0.00 | nan | nan | nan | 0.8419 | 0.6228 | 0.6544 | 0.147 | 0.131 |
| surprise & team fact | 4 | 0.25 | nan | nan | nan | 0.6913 | 0.6105 | 0.6205 | 0.122 | 0.125 |

## Movement toward the truth on surprise rows (mean of (p - b) * sign(y - b); positive = helped)

| slice | n | h4 | h5 |
|---|---|---|---|
| surprise rows | 7 | +0.073 | +0.065 |
| surprise & own fact | 2 | +0.147 | +0.131 |
| surprise & team fact | 4 | +0.071 | +0.065 |
| surprise & no fact | 1 | -0.068 | -0.069 |

Correlation of the two arms' availability deltas: 0.971; rows where they differ by > 0.1: 1.0% (own-fact rows: 2.6% of 38).
Points deltas: mean h4 -0.238 (sd 0.159), h5 -0.085 (sd 0.124); own-fact rows h5 -0.095 vs no-fact -0.086.

## Points 1GW: does the delta move where the sheet carries a fact, and toward the realised residual?

| slice | n | MAE classic / h4 / h5 | RMSE classic / h4 / h5 | mean dP h4 / h5 | sd dP h4 / h5 | corr(dP, residual) h4 / h5 | closer than classic h4 / h5 |
|---|---|---|---|---|---|---|---|
| own fact | 38 | 2.704 / 2.507 / 2.674 | 3.212 / 3.048 / 3.174 | -0.354 / -0.095 | 0.211 / 0.178 | +0.106 / -0.006 | 79% / 68% |
| own role fact | 6 | 1.928 / 1.668 / 1.927 | 2.172 / 1.980 / 2.183 | -0.261 / -0.002 | 0.138 / 0.121 | -0.449 / -0.178 | 100% / 33% |
| team fact only | 192 | 2.780 / 2.766 / 2.771 | 3.678 / 3.737 / 3.687 | -0.248 / -0.080 | 0.168 / 0.136 | -0.027 / +0.062 | 53% / 51% |
| no fact | 250 | 2.474 / 2.422 / 2.451 | 3.249 / 3.248 / 3.241 | -0.213 / -0.086 | 0.131 / 0.102 | +0.170 / +0.152 | 62% / 57% |
| all | 480 | 2.614 / 2.566 / 2.597 | 3.424 / 3.437 / 3.421 | -0.238 / -0.085 | 0.159 / 0.124 | +0.091 / +0.096 | 60% / 55% |
