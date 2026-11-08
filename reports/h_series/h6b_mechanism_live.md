# Team-sheet mechanism check: h6b vs h5 on 480 rows (eval.jsonl)

| slice | n | played | AUC classic | AUC h5 | AUC h6b | Brier classic | Brier h5 | Brier h6b | mean abs dP h5 | mean abs dP h6b |
|---|---|---|---|---|---|---|---|---|---|---|
| own fact | 38 | 0.87 | 0.785 | 0.836 | 0.873 | 0.0917 | 0.0890 | 0.0806 | 0.077 | 0.088 |
| team fact only | 192 | 0.98 | 0.511 | 0.605 | 0.602 | 0.0473 | 0.0251 | 0.0231 | 0.101 | 0.111 |
| no fact | 250 | 0.99 | 0.726 | 0.772 | 0.681 | 0.0350 | 0.0151 | 0.0150 | 0.099 | 0.110 |
| all | 480 | 0.97 | 0.645 | 0.727 | 0.696 | 0.0444 | 0.0250 | 0.0234 | 0.098 | 0.109 |
| surprise rows | 7 | 0.14 | nan | nan | nan | 0.7507 | 0.6751 | 0.6661 | 0.119 | 0.139 |
| surprise & own fact | 2 | 0.00 | nan | nan | nan | 0.8419 | 0.6544 | 0.6516 | 0.131 | 0.132 |
| surprise & team fact | 4 | 0.25 | nan | nan | nan | 0.6913 | 0.6205 | 0.6013 | 0.125 | 0.157 |

## Movement toward the truth on surprise rows (mean of (p - b) * sign(y - b); positive = helped)

| slice | n | h5 | h6b |
|---|---|---|---|
| surprise rows | 7 | +0.065 | +0.080 |
| surprise & own fact | 2 | +0.131 | +0.132 |
| surprise & team fact | 4 | +0.065 | +0.093 |
| surprise & no fact | 1 | -0.069 | -0.079 |

Correlation of the two arms' availability deltas: 0.957; rows where they differ by > 0.1: 1.7% (own-fact rows: 7.9% of 38).
Points deltas: mean h5 -0.085 (sd 0.124), h6b -0.076 (sd 0.180); own-fact rows h6b -0.197 vs no-fact -0.059.

## Points 1GW: does the delta move where the sheet carries a fact, and toward the realised residual?

| slice | n | MAE classic / h5 / h6b | RMSE classic / h5 / h6b | mean dP h5 / h6b | sd dP h5 / h6b | corr(dP, residual) h5 / h6b | closer than classic h5 / h6b |
|---|---|---|---|---|---|---|---|
| own fact | 38 | 2.704 / 2.674 / 2.601 | 3.212 / 3.174 / 3.112 | -0.095 / -0.197 | 0.178 / 0.231 | -0.006 / +0.098 | 68% / 68% |
| own role fact | 6 | 1.928 / 1.927 / 1.818 | 2.172 / 2.183 / 2.087 | -0.002 / -0.110 | 0.121 / 0.128 | -0.178 / -0.140 | 33% / 83% |
| team fact only | 192 | 2.780 / 2.771 / 2.774 | 3.678 / 3.687 / 3.687 | -0.080 / -0.074 | 0.136 / 0.179 | +0.062 / +0.047 | 51% / 53% |
| no fact | 250 | 2.474 / 2.451 / 2.448 | 3.249 / 3.241 / 3.225 | -0.086 / -0.059 | 0.102 / 0.164 | +0.152 / +0.191 | 57% / 53% |
| all | 480 | 2.614 / 2.597 / 2.590 | 3.424 / 3.421 / 3.409 | -0.085 / -0.076 | 0.124 / 0.180 | +0.096 / +0.141 | 55% / 54% |
