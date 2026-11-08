# Team-sheet mechanism check: h6 vs h5 on 1152 rows (eval.jsonl)

| slice | n | played | AUC classic | AUC h5 | AUC h6 | Brier classic | Brier h5 | Brier h6 | mean abs dP h5 | mean abs dP h6 |
|---|---|---|---|---|---|---|---|---|---|---|
| own fact | 104 | 0.83 | 0.740 | 0.860 | 0.877 | 0.1160 | 0.0771 | 0.0767 | 0.086 | 0.087 |
| team fact only | 475 | 0.90 | 0.657 | 0.731 | 0.738 | 0.0888 | 0.0688 | 0.0691 | 0.094 | 0.090 |
| no fact | 573 | 0.93 | 0.737 | 0.793 | 0.793 | 0.0595 | 0.0433 | 0.0435 | 0.078 | 0.078 |
| all | 1152 | 0.91 | 0.704 | 0.776 | 0.782 | 0.0767 | 0.0569 | 0.0571 | 0.086 | 0.084 |
| surprise rows | 59 | 0.20 | 0.000 | 0.037 | 0.041 | 0.7073 | 0.7078 | 0.7051 | 0.089 | 0.084 |
| surprise & own fact | 7 | 0.29 | nan | nan | nan | 0.7240 | 0.5630 | 0.5683 | 0.122 | 0.119 |
| surprise & team fact | 28 | 0.21 | 0.000 | 0.000 | 0.000 | 0.7188 | 0.7265 | 0.7201 | 0.089 | 0.079 |

## Movement toward the truth on surprise rows (mean of (p - b) * sign(y - b); positive = helped)

| slice | n | h5 | h6 |
|---|---|---|---|
| surprise rows | 59 | +0.023 | +0.021 |
| surprise & own fact | 7 | +0.122 | +0.114 |
| surprise & team fact | 28 | +0.020 | +0.021 |
| surprise & no fact | 24 | -0.002 | -0.006 |

Correlation of the two arms' availability deltas: 0.952; rows where they differ by > 0.1: 1.1% (own-fact rows: 1.9% of 104).
Points deltas: mean h5 -0.091 (sd 0.106), h6 -0.114 (sd 0.102); own-fact rows h6 -0.162 vs no-fact -0.111.

## Points 1GW: does the delta move where the sheet carries a fact, and toward the realised residual?

| slice | n | MAE classic / h5 / h6 | RMSE classic / h5 / h6 | mean dP h5 / h6 | sd dP h5 / h6 | corr(dP, residual) h5 / h6 | closer than classic h5 / h6 |
|---|---|---|---|---|---|---|---|
| own fact | 104 | 3.295 / 3.234 / 3.232 | 4.251 / 4.223 / 4.228 | -0.163 / -0.162 | 0.165 / 0.159 | +0.160 / +0.135 | 59% / 58% |
| own role fact | 9 | 3.217 / 3.157 / 3.171 | 3.669 / 3.666 / 3.675 | -0.119 / -0.122 | 0.075 / 0.070 | -0.239 / -0.398 | 67% / 78% |
| team fact only | 475 | 2.653 / 2.634 / 2.630 | 3.427 / 3.423 / 3.426 | -0.083 / -0.106 | 0.093 / 0.096 | +0.039 / +0.014 | 58% / 59% |
| no fact | 573 | 2.448 / 2.435 / 2.426 | 3.240 / 3.240 / 3.239 | -0.086 / -0.111 | 0.098 / 0.091 | +0.007 / +0.015 | 58% / 59% |
| all | 1152 | 2.609 / 2.589 / 2.583 | 3.420 / 3.415 / 3.416 | -0.091 / -0.114 | 0.106 / 0.102 | +0.047 / +0.037 | 58% / 59% |
