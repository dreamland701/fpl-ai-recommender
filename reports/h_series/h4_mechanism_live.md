# Team-sheet mechanism check: h4 vs h1 on 480 rows (eval.jsonl)

| slice | n | played | AUC classic | AUC h1 | AUC h4 | Brier classic | Brier h1 | Brier h4 | mean abs dP h1 | mean abs dP h4 |
|---|---|---|---|---|---|---|---|---|---|---|
| own fact | 30 | 0.83 | 0.808 | 0.840 | 0.864 | 0.1082 | 0.0892 | 0.1183 | 0.063 | 0.079 |
| team fact only | 175 | 0.98 | 0.509 | 0.677 | 0.630 | 0.0493 | 0.0294 | 0.0261 | 0.086 | 0.104 |
| no fact | 275 | 0.99 | 0.725 | 0.779 | 0.793 | 0.0343 | 0.0155 | 0.0142 | 0.090 | 0.105 |
| all | 480 | 0.97 | 0.645 | 0.760 | 0.780 | 0.0444 | 0.0252 | 0.0250 | 0.087 | 0.103 |
| surprise rows | 7 | 0.14 | nan | nan | nan | 0.7507 | 0.7160 | 0.6601 | 0.070 | 0.122 |
| surprise & own fact | 2 | 0.00 | nan | nan | nan | 0.8419 | 0.7950 | 0.6228 | 0.028 | 0.147 |
| surprise & team fact | 4 | 0.25 | nan | nan | nan | 0.6913 | 0.6245 | 0.6105 | 0.092 | 0.122 |

## Movement toward the truth on surprise rows (mean of (p - b) * sign(y - b); positive = helped)

| slice | n | h1 | h4 |
|---|---|---|---|
| surprise rows | 7 | +0.029 | +0.073 |
| surprise & own fact | 2 | +0.028 | +0.147 |
| surprise & team fact | 4 | +0.052 | +0.071 |
| surprise & no fact | 1 | -0.063 | -0.068 |

Correlation of the two arms' availability deltas: 0.876; rows where they differ by > 0.1: 3.1% (own-fact rows: 16.7% of 30).
Points deltas: mean h1 -0.243 (sd 0.120), h4 -0.238 (sd 0.159); own-fact rows h4 -0.416 vs no-fact -0.213.
