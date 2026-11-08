# Team-sheet mechanism check: h12 vs h5 on 1152 rows (eval.jsonl)

| slice | n | played | AUC classic | AUC h5 | AUC h12 | Brier classic | Brier h5 | Brier h12 | mean abs dP h5 | mean abs dP h12 |
|---|---|---|---|---|---|---|---|---|---|---|
| own fact | 104 | 0.83 | 0.740 | 0.860 | 0.749 | 0.1160 | 0.0771 | 0.1107 | 0.086 | 0.106 |
| team fact only | 475 | 0.90 | 0.657 | 0.731 | 0.662 | 0.0888 | 0.0688 | 0.0731 | 0.094 | 0.108 |
| no fact | 573 | 0.93 | 0.737 | 0.793 | 0.738 | 0.0595 | 0.0433 | 0.0442 | 0.078 | 0.098 |
| all | 1152 | 0.91 | 0.704 | 0.776 | 0.707 | 0.0767 | 0.0569 | 0.0621 | 0.086 | 0.103 |
| surprise rows | 59 | 0.20 | 0.000 | 0.037 | 0.000 | 0.7073 | 0.7078 | 0.7691 | 0.089 | 0.109 |
| surprise & own fact | 7 | 0.29 | nan | nan | nan | 0.7240 | 0.5630 | 0.7168 | 0.122 | 0.108 |
| surprise & team fact | 28 | 0.21 | 0.000 | 0.000 | 0.000 | 0.7188 | 0.7265 | 0.7655 | 0.089 | 0.105 |

## Movement toward the truth on surprise rows (mean of (p - b) * sign(y - b); positive = helped)

| slice | n | h5 | h12 |
|---|---|---|---|
| surprise rows | 59 | +0.023 | -0.007 |
| surprise & own fact | 7 | +0.122 | +0.038 |
| surprise & team fact | 28 | +0.020 | +0.002 |
| surprise & no fact | 24 | -0.002 | -0.031 |

Correlation of the two arms' availability deltas: 0.692; rows where they differ by > 0.1: 5.0% (own-fact rows: 22.1% of 104).
Points deltas: mean h5 -0.091 (sd 0.106), h12 -0.079 (sd 0.031); own-fact rows h12 -0.090 vs no-fact -0.074.

## Points 1GW: does the delta move where the sheet carries a fact, and toward the realised residual?

| slice | n | MAE classic / h5 / h12 | RMSE classic / h5 / h12 | mean dP h5 / h12 | sd dP h5 / h12 | corr(dP, residual) h5 / h12 | closer than classic h5 / h12 |
|---|---|---|---|---|---|---|---|
| own fact | 104 | 3.295 / 3.234 / 3.273 | 4.251 / 4.223 / 4.248 | -0.163 / -0.090 | 0.165 / 0.027 | +0.160 / -0.016 | 59% / 61% |
| own role fact | 9 | 3.217 / 3.157 / 3.152 | 3.669 / 3.666 / 3.637 | -0.119 / -0.087 | 0.075 / 0.032 | -0.239 / +0.504 | 67% / 78% |
| team fact only | 475 | 2.653 / 2.634 / 2.632 | 3.427 / 3.423 / 3.424 | -0.083 / -0.083 | 0.093 / 0.029 | +0.039 / +0.051 | 58% / 62% |
| no fact | 573 | 2.448 / 2.435 / 2.428 | 3.240 / 3.240 / 3.236 | -0.086 / -0.074 | 0.098 / 0.032 | +0.007 / +0.083 | 58% / 61% |
| all | 1152 | 2.609 / 2.589 / 2.588 | 3.420 / 3.415 / 3.417 | -0.091 / -0.079 | 0.106 / 0.031 | +0.047 / +0.060 | 58% / 62% |
