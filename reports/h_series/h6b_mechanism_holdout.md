# Team-sheet mechanism check: h6b vs h5 on 1152 rows (eval.jsonl)

| slice | n | played | AUC classic | AUC h5 | AUC h6b | Brier classic | Brier h5 | Brier h6b | mean abs dP h5 | mean abs dP h6b |
|---|---|---|---|---|---|---|---|---|---|---|
| own fact | 104 | 0.83 | 0.740 | 0.860 | 0.878 | 0.1160 | 0.0771 | 0.0772 | 0.086 | 0.112 |
| team fact only | 475 | 0.90 | 0.657 | 0.731 | 0.762 | 0.0888 | 0.0688 | 0.0663 | 0.094 | 0.115 |
| no fact | 573 | 0.93 | 0.737 | 0.793 | 0.777 | 0.0595 | 0.0433 | 0.0412 | 0.078 | 0.103 |
| all | 1152 | 0.91 | 0.704 | 0.776 | 0.792 | 0.0767 | 0.0569 | 0.0548 | 0.086 | 0.109 |
| surprise rows | 59 | 0.20 | 0.000 | 0.037 | 0.062 | 0.7073 | 0.7078 | 0.7188 | 0.089 | 0.110 |
| surprise & own fact | 7 | 0.29 | nan | nan | nan | 0.7240 | 0.5630 | 0.5334 | 0.122 | 0.153 |
| surprise & team fact | 28 | 0.21 | 0.000 | 0.000 | 0.000 | 0.7188 | 0.7265 | 0.7404 | 0.089 | 0.095 |

## Movement toward the truth on surprise rows (mean of (p - b) * sign(y - b); positive = helped)

| slice | n | h5 | h6b |
|---|---|---|---|
| surprise rows | 59 | +0.023 | +0.024 |
| surprise & own fact | 7 | +0.122 | +0.153 |
| surprise & team fact | 28 | +0.020 | +0.016 |
| surprise & no fact | 24 | -0.002 | -0.005 |

Correlation of the two arms' availability deltas: 0.842; rows where they differ by > 0.1: 4.3% (own-fact rows: 16.3% of 104).
Points deltas: mean h5 -0.091 (sd 0.106), h6b -0.065 (sd 0.173); own-fact rows h6b -0.173 vs no-fact -0.059.

## Points 1GW: does the delta move where the sheet carries a fact, and toward the realised residual?

| slice | n | MAE classic / h5 / h6b | RMSE classic / h5 / h6b | mean dP h5 / h6b | sd dP h5 / h6b | corr(dP, residual) h5 / h6b | closer than classic h5 / h6b |
|---|---|---|---|---|---|---|---|
| own fact | 104 | 3.295 / 3.234 / 3.188 | 4.251 / 4.223 / 4.169 | -0.163 / -0.173 | 0.165 / 0.287 | +0.160 / +0.302 | 59% / 57% |
| own role fact | 9 | 3.217 / 3.157 / 3.176 | 3.669 / 3.666 / 3.629 | -0.119 / -0.059 | 0.075 / 0.180 | -0.239 / +0.186 | 67% / 56% |
| team fact only | 475 | 2.653 / 2.634 / 2.635 | 3.427 / 3.423 / 3.416 | -0.083 / -0.049 | 0.093 / 0.156 | +0.039 / +0.085 | 58% / 54% |
| no fact | 573 | 2.448 / 2.435 / 2.431 | 3.240 / 3.240 / 3.231 | -0.086 / -0.059 | 0.098 / 0.151 | +0.007 / +0.080 | 58% / 55% |
| all | 1152 | 2.609 / 2.589 / 2.584 | 3.420 / 3.415 / 3.402 | -0.091 / -0.065 | 0.106 / 0.173 | +0.047 / +0.123 | 58% / 55% |
