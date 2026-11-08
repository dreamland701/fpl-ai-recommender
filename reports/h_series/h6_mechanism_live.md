# Team-sheet mechanism check: h6 vs h5 on 480 rows (eval.jsonl)

| slice | n | played | AUC classic | AUC h5 | AUC h6 | Brier classic | Brier h5 | Brier h6 | mean abs dP h5 | mean abs dP h6 |
|---|---|---|---|---|---|---|---|---|---|---|
| own fact | 38 | 0.87 | 0.785 | 0.836 | 0.812 | 0.0917 | 0.0890 | 0.0789 | 0.077 | 0.089 |
| team fact only | 192 | 0.98 | 0.511 | 0.605 | 0.618 | 0.0473 | 0.0251 | 0.0240 | 0.101 | 0.108 |
| no fact | 250 | 0.99 | 0.726 | 0.772 | 0.753 | 0.0350 | 0.0151 | 0.0148 | 0.099 | 0.109 |
| all | 480 | 0.97 | 0.645 | 0.727 | 0.730 | 0.0444 | 0.0250 | 0.0235 | 0.098 | 0.107 |
| surprise rows | 7 | 0.14 | nan | nan | nan | 0.7507 | 0.6751 | 0.6939 | 0.119 | 0.110 |
| surprise & own fact | 2 | 0.00 | nan | nan | nan | 0.8419 | 0.6544 | 0.6619 | 0.131 | 0.127 |
| surprise & team fact | 4 | 0.25 | nan | nan | nan | 0.6913 | 0.6205 | 0.6441 | 0.125 | 0.109 |

## Movement toward the truth on surprise rows (mean of (p - b) * sign(y - b); positive = helped)

| slice | n | h5 | h6 |
|---|---|---|---|
| surprise rows | 7 | +0.065 | +0.050 |
| surprise & own fact | 2 | +0.131 | +0.127 |
| surprise & team fact | 4 | +0.065 | +0.044 |
| surprise & no fact | 1 | -0.069 | -0.080 |

Correlation of the two arms' availability deltas: 0.954; rows where they differ by > 0.1: 1.2% (own-fact rows: 5.3% of 38).
Points deltas: mean h5 -0.085 (sd 0.124), h6 -0.088 (sd 0.128); own-fact rows h6 -0.109 vs no-fact -0.081.

## Points 1GW: does the delta move where the sheet carries a fact, and toward the realised residual?

| slice | n | MAE classic / h5 / h6 | RMSE classic / h5 / h6 | mean dP h5 / h6 | sd dP h5 / h6 | corr(dP, residual) h5 / h6 | closer than classic h5 / h6 |
|---|---|---|---|---|---|---|---|
| own fact | 38 | 2.704 / 2.674 / 2.682 | 3.212 / 3.174 / 3.181 | -0.095 / -0.109 | 0.178 / 0.204 | -0.006 / -0.066 | 68% / 61% |
| own role fact | 6 | 1.928 / 1.927 / 1.940 | 2.172 / 2.183 / 2.195 | -0.002 / +0.012 | 0.121 / 0.120 | -0.178 / -0.186 | 33% / 67% |
| team fact only | 192 | 2.780 / 2.771 / 2.768 | 3.678 / 3.687 / 3.691 | -0.080 / -0.093 | 0.136 / 0.133 | +0.062 / +0.048 | 51% / 55% |
| no fact | 250 | 2.474 / 2.451 / 2.451 | 3.249 / 3.241 / 3.238 | -0.086 / -0.081 | 0.102 / 0.106 | +0.152 / +0.170 | 57% / 62% |
| all | 480 | 2.614 / 2.597 / 2.596 | 3.424 / 3.421 / 3.422 | -0.085 / -0.088 | 0.124 / 0.128 | +0.096 / +0.088 | 55% / 59% |
