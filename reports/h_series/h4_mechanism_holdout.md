# Team-sheet mechanism check: h4 vs h1 on 1152 rows (eval.jsonl)

| slice | n | played | AUC classic | AUC h1 | AUC h4 | Brier classic | Brier h1 | Brier h4 | mean abs dP h1 | mean abs dP h4 |
|---|---|---|---|---|---|---|---|---|---|---|
| own fact | 91 | 0.85 | 0.746 | 0.798 | 0.848 | 0.1029 | 0.0862 | 0.0628 | 0.063 | 0.100 |
| team fact only | 415 | 0.88 | 0.675 | 0.743 | 0.759 | 0.0928 | 0.0783 | 0.0740 | 0.076 | 0.100 |
| no fact | 646 | 0.93 | 0.717 | 0.780 | 0.793 | 0.0627 | 0.0454 | 0.0431 | 0.070 | 0.086 |
| all | 1152 | 0.91 | 0.704 | 0.771 | 0.788 | 0.0767 | 0.0604 | 0.0558 | 0.072 | 0.092 |
| surprise rows | 59 | 0.20 | 0.000 | 0.012 | 0.018 | 0.7073 | 0.7041 | 0.6998 | 0.074 | 0.091 |
| surprise & own fact | 6 | 0.33 | nan | nan | nan | 0.7333 | 0.6943 | 0.5531 | 0.053 | 0.142 |
| surprise & team fact | 25 | 0.20 | 0.000 | 0.000 | 0.000 | 0.7204 | 0.7027 | 0.7191 | 0.069 | 0.088 |

## Movement toward the truth on surprise rows (mean of (p - b) * sign(y - b); positive = helped)

| slice | n | h1 | h4 |
|---|---|---|---|
| surprise rows | 59 | +0.018 | +0.030 |
| surprise & own fact | 6 | +0.029 | +0.142 |
| surprise & team fact | 25 | +0.030 | +0.026 |
| surprise & no fact | 28 | +0.006 | +0.010 |

Correlation of the two arms' availability deltas: 0.818; rows where they differ by > 0.1: 5.1% (own-fact rows: 17.6% of 91).
Points deltas: mean h1 -0.246 (sd 0.112), h4 -0.267 (sd 0.134); own-fact rows h4 -0.378 vs no-fact -0.262.

## Points 1GW: does the delta move where the sheet carries a fact, and toward the realised residual?

| slice | n | MAE classic / h1 / h4 | RMSE classic / h1 / h4 | mean dP h1 / h4 | sd dP h1 / h4 | corr(dP, residual) h1 / h4 | closer than classic h1 / h4 |
|---|---|---|---|---|---|---|---|
| own fact | 91 | 3.226 / 3.146 / 3.107 | 4.004 / 3.962 / 3.941 | -0.277 / -0.378 | 0.117 / 0.193 | +0.226 / +0.250 | 60% / 60% |
| own role fact | 7 | 2.537 / 2.271 / 2.235 | 2.865 / 2.634 / 2.600 | -0.266 / -0.302 | 0.107 / 0.106 | +0.012 / +0.055 | 100% / 100% |
| team fact only | 415 | 2.656 / 2.612 / 2.599 | 3.459 / 3.468 / 3.457 | -0.248 / -0.251 | 0.113 / 0.120 | -0.031 / +0.065 | 61% / 60% |
| no fact | 646 | 2.492 / 2.438 / 2.426 | 3.303 / 3.304 / 3.300 | -0.241 / -0.262 | 0.110 / 0.125 | +0.045 / +0.085 | 61% / 62% |
| all | 1152 | 2.609 / 2.557 / 2.542 | 3.420 / 3.419 / 3.411 | -0.246 / -0.267 | 0.112 / 0.134 | +0.036 / +0.103 | 61% / 61% |
