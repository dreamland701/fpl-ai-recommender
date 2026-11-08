# Team-sheet mechanism check: h5 vs h4 on 1152 rows (eval.jsonl)

| slice | n | played | AUC classic | AUC h4 | AUC h5 | Brier classic | Brier h4 | Brier h5 | mean abs dP h4 | mean abs dP h5 |
|---|---|---|---|---|---|---|---|---|---|---|
| own fact | 104 | 0.83 | 0.740 | 0.857 | 0.860 | 0.1160 | 0.0784 | 0.0771 | 0.103 | 0.086 |
| team fact only | 475 | 0.90 | 0.657 | 0.749 | 0.731 | 0.0888 | 0.0671 | 0.0688 | 0.098 | 0.094 |
| no fact | 573 | 0.93 | 0.737 | 0.795 | 0.793 | 0.0595 | 0.0423 | 0.0433 | 0.086 | 0.078 |
| all | 1152 | 0.91 | 0.704 | 0.788 | 0.776 | 0.0767 | 0.0558 | 0.0569 | 0.092 | 0.086 |
| surprise rows | 59 | 0.20 | 0.000 | 0.018 | 0.037 | 0.7073 | 0.6998 | 0.7078 | 0.091 | 0.089 |
| surprise & own fact | 7 | 0.29 | nan | nan | nan | 0.7240 | 0.5647 | 0.5630 | 0.124 | 0.122 |
| surprise & team fact | 28 | 0.21 | 0.000 | 0.000 | 0.000 | 0.7188 | 0.7106 | 0.7265 | 0.088 | 0.089 |

## Movement toward the truth on surprise rows (mean of (p - b) * sign(y - b); positive = helped)

| slice | n | h4 | h5 |
|---|---|---|---|
| surprise rows | 59 | +0.030 | +0.023 |
| surprise & own fact | 7 | +0.124 | +0.122 |
| surprise & team fact | 28 | +0.031 | +0.020 |
| surprise & no fact | 24 | +0.002 | -0.002 |

Correlation of the two arms' availability deltas: 0.914; rows where they differ by > 0.1: 1.8% (own-fact rows: 12.5% of 104).
Points deltas: mean h4 -0.267 (sd 0.134), h5 -0.091 (sd 0.106); own-fact rows h5 -0.163 vs no-fact -0.086.

## Points 1GW: does the delta move where the sheet carries a fact, and toward the realised residual?

| slice | n | MAE classic / h4 / h5 | RMSE classic / h4 / h5 | mean dP h4 / h5 | sd dP h4 / h5 | corr(dP, residual) h4 / h5 | closer than classic h4 / h5 |
|---|---|---|---|---|---|---|---|
| own fact | 104 | 3.295 / 3.186 / 3.234 | 4.251 / 4.212 / 4.223 | -0.376 / -0.163 | 0.198 / 0.165 | +0.216 / +0.160 | 59% / 59% |
| own role fact | 9 | 3.217 / 3.060 / 3.157 | 3.669 / 3.645 / 3.666 | -0.312 / -0.119 | 0.115 / 0.075 | -0.201 / -0.239 | 78% / 67% |
| team fact only | 475 | 2.653 / 2.586 / 2.634 | 3.427 / 3.420 / 3.423 | -0.257 / -0.083 | 0.122 / 0.093 | +0.094 / +0.039 | 61% / 58% |
| no fact | 573 | 2.448 / 2.388 / 2.435 | 3.240 / 3.237 / 3.240 | -0.255 / -0.086 | 0.119 / 0.098 | +0.071 / +0.007 | 61% / 58% |
| all | 1152 | 2.609 / 2.542 / 2.589 | 3.420 / 3.411 / 3.415 | -0.267 / -0.091 | 0.134 / 0.106 | +0.103 / +0.047 | 61% / 58% |
