# Team-sheet mechanism check: h12 vs h5 on 480 rows (eval.jsonl)

| slice | n | played | AUC classic | AUC h5 | AUC h12 | Brier classic | Brier h5 | Brier h12 | mean abs dP h5 | mean abs dP h12 |
|---|---|---|---|---|---|---|---|---|---|---|
| own fact | 38 | 0.87 | 0.785 | 0.836 | 0.812 | 0.0917 | 0.0890 | 0.1085 | 0.077 | 0.075 |
| team fact only | 192 | 0.98 | 0.511 | 0.605 | 0.489 | 0.0473 | 0.0251 | 0.0230 | 0.101 | 0.099 |
| no fact | 250 | 0.99 | 0.726 | 0.772 | 0.717 | 0.0350 | 0.0151 | 0.0131 | 0.099 | 0.102 |
| all | 480 | 0.97 | 0.645 | 0.727 | 0.657 | 0.0444 | 0.0250 | 0.0246 | 0.098 | 0.098 |
| surprise rows | 7 | 0.14 | nan | nan | nan | 0.7507 | 0.6751 | 0.8218 | 0.119 | 0.094 |
| surprise & own fact | 2 | 0.00 | nan | nan | nan | 0.8419 | 0.6544 | 0.9301 | 0.131 | 0.056 |
| surprise & team fact | 4 | 0.25 | nan | nan | nan | 0.6913 | 0.6205 | 0.7355 | 0.125 | 0.117 |

## Movement toward the truth on surprise rows (mean of (p - b) * sign(y - b); positive = helped)

| slice | n | h5 | h12 |
|---|---|---|---|
| surprise rows | 7 | +0.065 | -0.021 |
| surprise & own fact | 2 | +0.131 | -0.051 |
| surprise & team fact | 4 | +0.065 | +0.008 |
| surprise & no fact | 1 | -0.069 | -0.077 |

Correlation of the two arms' availability deltas: 0.700; rows where they differ by > 0.1: 3.5% (own-fact rows: 15.8% of 38).
Points deltas: mean h5 -0.085 (sd 0.124), h12 -0.062 (sd 0.036); own-fact rows h12 -0.083 vs no-fact -0.056.

## Points 1GW: does the delta move where the sheet carries a fact, and toward the realised residual?

| slice | n | MAE classic / h5 / h12 | RMSE classic / h5 / h12 | mean dP h5 / h12 | sd dP h5 / h12 | corr(dP, residual) h5 / h12 | closer than classic h5 / h12 |
|---|---|---|---|---|---|---|---|
| own fact | 38 | 2.704 / 2.674 / 2.649 | 3.212 / 3.174 / 3.167 | -0.095 / -0.083 | 0.178 / 0.041 | -0.006 / +0.170 | 68% / 82% |
| own role fact | 6 | 1.928 / 1.927 / 1.851 | 2.172 / 2.183 / 2.098 | -0.002 / -0.077 | 0.121 / 0.025 | -0.178 / +0.497 | 33% / 100% |
| team fact only | 192 | 2.780 / 2.771 / 2.772 | 3.678 / 3.687 / 3.688 | -0.080 / -0.065 | 0.136 / 0.036 | +0.062 / +0.058 | 51% / 55% |
| no fact | 250 | 2.474 / 2.451 / 2.457 | 3.249 / 3.241 / 3.250 | -0.086 / -0.056 | 0.102 / 0.033 | +0.152 / +0.067 | 57% / 63% |
| all | 480 | 2.614 / 2.597 / 2.598 | 3.424 / 3.421 / 3.426 | -0.085 / -0.062 | 0.124 / 0.036 | +0.096 / +0.086 | 55% / 61% |
