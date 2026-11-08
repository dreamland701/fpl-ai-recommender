# Team-sheet mechanism check: h5 vs h1 on 1152 rows (eval.jsonl)

| slice | n | played | AUC classic | AUC h1 | AUC h5 | Brier classic | Brier h1 | Brier h5 | mean abs dP h1 | mean abs dP h5 |
|---|---|---|---|---|---|---|---|---|---|---|
| own fact | 104 | 0.83 | 0.740 | 0.817 | 0.860 | 0.1160 | 0.0982 | 0.0771 | 0.072 | 0.086 |
| team fact only | 475 | 0.90 | 0.657 | 0.734 | 0.731 | 0.0888 | 0.0713 | 0.0688 | 0.074 | 0.094 |
| no fact | 573 | 0.93 | 0.737 | 0.781 | 0.793 | 0.0595 | 0.0446 | 0.0433 | 0.069 | 0.078 |
| all | 1152 | 0.91 | 0.704 | 0.771 | 0.776 | 0.0767 | 0.0604 | 0.0569 | 0.072 | 0.086 |
| surprise rows | 59 | 0.20 | 0.000 | 0.012 | 0.037 | 0.7073 | 0.7041 | 0.7078 | 0.074 | 0.089 |
| surprise & own fact | 7 | 0.29 | nan | nan | nan | 0.7240 | 0.6411 | 0.5630 | 0.081 | 0.122 |
| surprise & team fact | 28 | 0.21 | 0.000 | 0.000 | 0.000 | 0.7188 | 0.7003 | 0.7265 | 0.066 | 0.089 |

## Movement toward the truth on surprise rows (mean of (p - b) * sign(y - b); positive = helped)

| slice | n | h1 | h5 |
|---|---|---|---|
| surprise rows | 59 | +0.018 | +0.023 |
| surprise & own fact | 7 | +0.061 | +0.122 |
| surprise & team fact | 28 | +0.029 | +0.020 |
| surprise & no fact | 24 | -0.007 | -0.002 |

Correlation of the two arms' availability deltas: 0.825; rows where they differ by > 0.1: 4.1% (own-fact rows: 12.5% of 104).
Points deltas: mean h1 -0.246 (sd 0.112), h5 -0.091 (sd 0.106); own-fact rows h5 -0.163 vs no-fact -0.086.

## Points 1GW: does the delta move where the sheet carries a fact, and toward the realised residual?

| slice | n | MAE classic / h1 / h5 | RMSE classic / h1 / h5 | mean dP h1 / h5 | sd dP h1 / h5 | corr(dP, residual) h1 / h5 | closer than classic h1 / h5 |
|---|---|---|---|---|---|---|---|
| own fact | 104 | 3.295 / 3.225 / 3.234 | 4.251 / 4.232 / 4.223 | -0.288 / -0.163 | 0.134 / 0.165 | +0.130 / +0.160 | 58% / 59% |
| own role fact | 9 | 3.217 / 3.089 / 3.157 | 3.669 / 3.665 / 3.666 | -0.286 / -0.119 | 0.119 / 0.075 | -0.340 / -0.239 | 78% / 67% |
| team fact only | 475 | 2.653 / 2.600 / 2.634 | 3.427 / 3.429 / 3.423 | -0.248 / -0.083 | 0.111 / 0.093 | +0.016 / +0.039 | 62% / 58% |
| no fact | 573 | 2.448 / 2.400 / 2.435 | 3.240 / 3.241 / 3.240 | -0.237 / -0.086 | 0.107 / 0.098 | +0.025 / +0.007 | 61% / 58% |
| all | 1152 | 2.609 / 2.557 / 2.589 | 3.420 / 3.419 / 3.415 | -0.246 / -0.091 | 0.112 / 0.106 | +0.036 / +0.047 | 61% / 58% |
