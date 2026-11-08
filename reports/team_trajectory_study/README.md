# Team trajectory study: does the classic model miss up-and-coming (or fading) teams?

Seasons 2022-23 → 2026-27. Team form in the ridge = lagged 3/5-week rolling goals for/against (own and opponent), no longer baseline. Here: trend5 = last-5 GD/game − the club's prior-season GD/game; traj = season-to-date GD/game (≥5 games) − prior; form5 = last-5 GD/game alone; rising = last-4 points ≥ 8 from a club that finished 8th or lower (falling = ≤ 3 points from a top-6 club). Promoted clubs have no prior and are excluded from trend/traj. ± = 2 s.e.

## A. Team level: does a 5-game streak carry into the next game once the club's level is known?

Team-weeks with a prior season and 5 previous games: 1,698. OLS of this week's GD/game on the lagged measures.

| model | coefficients (± 2 s.e.) | R² |
|---|---|---|
| prior only | prior +0.611 ±0.145 | 0.040 |
| form5 only | form5 +0.246 ±0.097 | 0.015 |
| prior + form5 | prior +0.553 ±0.161, form5 +0.088 ±0.106 | 0.042 |
| prior + season-to-date + form5 | prior +0.482 ±0.198, std +0.137 ±0.222, form5 +0.036 ±0.136 | 0.043 |

rising team-weeks 177: next-game GD/game -0.05 ±0.29 (their last-5 +0.74, prior-season -0.20); other clubs with a prior +0.19.

falling team-weeks 70: next-game GD/game +0.01 ±0.52 (their last-5 -0.72, prior-season +0.64); other clubs with a prior +0.17.

## B. Forecast residual (realised − classic points) by the player's OWN team trajectory

Player-weeks with a stored walk-forward forecast and a single fixture: 39,619; with a team trend (club has a prior season, 5 games played): 22,567. Residual +0.10 on a bucket = the model under-forecasts those players by a tenth of a point per week.

### trend5 = last-5 GD vs prior-season level (what the model lacks)

| bucket | all | GK/DEF | MID/FWD | regulars (forecast ≥ 60 min) | mean trend | mean forecast | mean realised |
|---|---|---|---|---|---|---|---|
| Q1 lowest | +0.177 ±0.091 (n 4,497) | +0.154 ±0.142 (n 1,758) | +0.191 ±0.119 (n 2,739) | +0.135 ±0.133 (n 2,390) | -1.19 | 2.54 | 2.72 |
| Q2 | +0.148 ±0.089 (n 4,628) | +0.058 ±0.132 (n 1,854) | +0.208 ±0.119 (n 2,774) | +0.097 ±0.129 (n 2,463) | -0.46 | 2.55 | 2.69 |
| Q3 | +0.211 ±0.091 (n 4,561) | +0.360 ±0.142 (n 1,839) | +0.111 ±0.119 (n 2,722) | +0.186 ±0.127 (n 2,545) | -0.01 | 2.66 | 2.87 |
| Q4 | +0.160 ±0.091 (n 4,469) | +0.145 ±0.137 (n 1,809) | +0.170 ±0.121 (n 2,660) | +0.131 ±0.127 (n 2,552) | +0.44 | 2.66 | 2.82 |
| Q5 highest | +0.096 ±0.092 (n 4,412) | -0.016 ±0.139 (n 1,765) | +0.171 ±0.123 (n 2,647) | +0.016 ±0.129 (n 2,546) | +1.16 | 2.70 | 2.80 |

### traj = season-to-date GD vs prior-season level

| bucket | all | GK/DEF | MID/FWD | regulars (forecast ≥ 60 min) | mean trend | mean forecast | mean realised |
|---|---|---|---|---|---|---|---|
| Q1 lowest | +0.189 ±0.085 (n 4,793) | +0.223 ±0.131 (n 1,895) | +0.166 ±0.112 (n 2,898) | +0.154 ±0.127 (n 2,508) | -0.78 | 2.50 | 2.69 |
| Q2 | +0.227 ±0.091 (n 4,409) | +0.254 ±0.141 (n 1,789) | +0.208 ±0.119 (n 2,620) | +0.265 ±0.134 (n 2,357) | -0.30 | 2.51 | 2.73 |
| Q3 | +0.133 ±0.094 (n 4,343) | +0.122 ±0.141 (n 1,775) | +0.140 ±0.127 (n 2,568) | +0.096 ±0.127 (n 2,595) | -0.00 | 2.75 | 2.89 |
| Q4 | +0.158 ±0.094 (n 4,397) | +0.067 ±0.142 (n 1,710) | +0.215 ±0.125 (n 2,687) | -0.014 ±0.127 (n 2,450) | +0.29 | 2.67 | 2.83 |
| Q5 highest | +0.088 ±0.090 (n 4,625) | +0.035 ±0.137 (n 1,856) | +0.124 ±0.119 (n 2,769) | +0.070 ±0.131 (n 2,586) | +0.69 | 2.69 | 2.77 |

### form5 = last-5 GD alone (what the model already carries)

| bucket | all | GK/DEF | MID/FWD | regulars (forecast ≥ 60 min) | mean trend | mean forecast | mean realised |
|---|---|---|---|---|---|---|---|
| Q1 lowest | +0.113 ±0.057 (n 9,741) | +0.024 ±0.088 (n 4,034) | +0.175 ±0.074 (n 5,707) | +0.000 ±0.079 (n 5,446) | -1.11 | 2.33 | 2.44 |
| Q2 | +0.136 ±0.063 (n 8,412) | +0.102 ±0.096 (n 3,450) | +0.159 ±0.084 (n 4,962) | +0.069 ±0.089 (n 4,702) | -0.21 | 2.49 | 2.63 |
| Q3 | +0.141 ±0.082 (n 5,288) | +0.180 ±0.128 (n 2,132) | +0.114 ±0.108 (n 3,156) | +0.039 ±0.113 (n 3,006) | +0.29 | 2.58 | 2.72 |
| Q4 | +0.112 ±0.089 (n 5,385) | +0.005 ±0.131 (n 2,147) | +0.182 ±0.120 (n 3,238) | -0.019 ±0.126 (n 2,996) | +0.78 | 2.82 | 2.93 |
| Q5 highest | +0.054 ±0.095 (n 4,654) | +0.124 ±0.142 (n 1,803) | +0.010 ±0.126 (n 2,851) | -0.027 ±0.138 (n 2,587) | +1.65 | 2.99 | 3.05 |

### Creator-style flags

| flag | all | GK/DEF | MID/FWD | regulars | n team-weeks |
|---|---|---|---|---|---|
| rising (last-4 ≥ 8 pts, finished ≥ 8th) | +0.153 ±0.125 (n 2,321) | +0.045 ±0.188 (n 941) | +0.227 ±0.167 (n 1,380) | +0.104 ±0.167 (n 1,410) | 181 |
| falling (last-4 ≤ 3 pts, finished top 6) | -0.036 ±0.181 (n 1,057) | +0.030 ±0.287 (n 402) | -0.077 ±0.234 (n 655) | -0.134 ±0.282 (n 513) | 73 |
| promoted club | +0.036 ±0.051 (n 12,769) | -0.022 ±0.078 (n 5,312) | +0.077 ±0.068 (n 7,457) | -0.147 ±0.070 (n 7,357) | 1,024 |
| everyone else | +0.172 ±0.040 (n 23,472) | +0.190 ±0.061 (n 9,380) | +0.160 ±0.052 (n 14,092) | +0.116 ±0.057 (n 12,918) | 1,731 |

### Regression of the residual on team terms (all rows with trends, position dummies included)

| term | coefficient ± 2 s.e. | reading |
|---|---|---|
| own trend5 | -0.034 ±0.053 | points/week left per 1.0 GD/game of own streak over the prior level |
| own prior level | -0.086 ±0.077 | points/week left per 1.0 GD/game of prior-season level |
| opp trend5 | +0.056 ±0.053 | same for the opponent's streak |
| opp prior level | -0.120 ±0.077 | same for the opponent's level |
| MID/FWD | +0.049 ±0.089 | position offset |
| forecast | -0.113 ±0.043 | per forecast point (the generic shrink/stretch) |

R² 0.0031 on 18,856 rows. Scale: a club one full goal per game above its prior level over 5 games is a very strong streak (Villa GW4-8 2026-27 ≈ +0.6 vs prior ≈ −0.4).

### Top trend5 bucket by season (stability)

| season | residual, Q5 | residual, Q1 | n Q5 |
|---|---|---|---|
| 2023-24 | +0.132 ±0.150 (n 1,709) | +0.335 ±0.186 (n 1,249) | 1,709 |
| 2024-25 | +0.177 ±0.163 (n 1,504) | +0.131 ±0.170 (n 1,320) | 1,504 |
| 2025-26 | -0.082 ±0.195 (n 970) | +0.056 ±0.147 (n 1,634) | 970 |
| 2026-27 | +0.046 ±0.298 (n 229) | +0.381 ±0.270 (n 294) | 229 |

## C. Residual by the OPPONENT's trajectory (facing a rising or fading team)

| bucket | all | GK/DEF | MID/FWD | regulars |
|---|---|---|---|---|
| opp trend5 Q1 lowest | -0.054 ±0.087 (n 4,444) | -0.159 ±0.132 (n 1,830) | +0.020 ±0.116 (n 2,614) | -0.153 ±0.121 (n 2,548) |
| opp trend5 Q2 | +0.073 ±0.083 (n 4,582) | +0.052 ±0.130 (n 1,836) | +0.087 ±0.108 (n 2,746) | +0.037 ±0.123 (n 2,492) |
| opp trend5 Q3 | +0.050 ±0.086 (n 4,404) | +0.064 ±0.135 (n 1,787) | +0.040 ±0.111 (n 2,617) | -0.036 ±0.122 (n 2,436) |
| opp trend5 Q4 | +0.079 ±0.088 (n 4,376) | +0.110 ±0.133 (n 1,800) | +0.058 ±0.117 (n 2,576) | -0.002 ±0.123 (n 2,477) |
| opp trend5 Q5 highest | +0.214 ±0.091 (n 4,330) | +0.017 ±0.136 (n 1,702) | +0.341 ±0.121 (n 2,628) | +0.121 ±0.127 (n 2,376) |

## D. 2026-27 so far (GW2-5 from the E20 live eval corpus, GW6-8 from the final-packet F6 corpora)

Rows 3,026. Per club: residual of all forecast players and of regulars; the 'sum' is the points the model left on that club's players over the weeks covered.

| club | n | residual all | residual regulars | sum, regulars | GW8 last-5 GF/GA per game | trend5 at GW8 |
|---|---|---|---|---|---|---|
| BHA | 155 | +0.747 ±0.523 (n 155) | +1.837 ±1.088 (n 65) | +119.4 | 3.20 / 0.20 | +2.84 |
| LEE | 146 | +0.420 ±0.404 (n 146) | +0.951 ±0.849 (n 59) | +56.1 | 1.40 / 1.00 | +0.58 |
| BOU | 133 | +0.449 ±0.440 (n 133) | +0.824 ±0.813 (n 66) | +54.4 | 1.40 / 2.00 | -0.71 |
| FUL | 132 | +0.260 ±0.404 (n 132) | +0.567 ±0.672 (n 64) | +36.3 | 1.00 / 1.20 | -0.09 |
| ARS | 144 | +0.172 ±0.475 (n 144) | +0.593 ±1.034 (n 57) | +33.8 | 1.40 / 1.00 | -0.76 |
| LIV | 162 | +0.199 ±0.370 (n 162) | +0.537 ±0.840 (n 60) | +32.2 | 1.00 / 0.80 | -0.06 |
| AVL | 154 | +0.298 ±0.361 (n 154) | +0.561 ±0.723 (n 57) | +32.0 | 1.40 / 1.20 | +0.02 |
| MCI | 152 | +0.100 ±0.457 (n 152) | +0.086 ±0.867 (n 64) | +5.5 | 2.60 / 1.00 | +0.49 |
| NEW | 158 | +0.039 ±0.426 (n 158) | +0.042 ±0.977 (n 54) | +2.3 | 1.20 / 2.40 | -1.15 |
| COV | 161 | -0.002 ±0.345 (n 161) | +0.038 ±0.781 (n 56) | +2.2 | 1.20 / 2.00 | promoted/— |
| TOT | 177 | +0.151 ±0.330 (n 177) | +0.003 ±0.717 (n 51) | +0.2 | 1.20 / 1.00 | +0.44 |
| SUN | 143 | -0.085 ±0.375 (n 143) | -0.032 ±0.793 (n 59) | -1.9 | 0.80 / 2.40 | -1.44 |
| CRY | 160 | -0.219 ±0.335 (n 160) | -0.045 ±0.825 (n 55) | -2.5 | 1.60 / 2.20 | -0.34 |
| EVE | 126 | +0.001 ±0.413 (n 126) | -0.043 ±0.740 (n 63) | -2.7 | 1.00 / 1.20 | -0.12 |
| HUL | 175 | -0.004 ±0.293 (n 175) | -0.058 ±0.723 (n 55) | -3.2 | 1.00 / 1.40 | promoted/— |
| BRE | 141 | -0.113 ±0.443 (n 141) | -0.164 ±0.870 (n 53) | -8.7 | 1.80 / 1.40 | +0.32 |
| IPS | 158 | -0.059 ±0.328 (n 158) | -0.354 ±0.721 (n 53) | -18.8 | 1.40 / 1.80 | promoted/— |
| MUN | 157 | -0.142 ±0.380 (n 157) | -0.347 ±0.968 (n 55) | -19.1 | 1.00 / 1.20 | -0.70 |
| NFO | 139 | -0.192 ±0.355 (n 139) | -0.452 ±0.617 (n 59) | -26.7 | 0.60 / 1.20 | -0.52 |
| CHE | 153 | -0.145 ±0.450 (n 153) | -0.693 ±0.815 (n 58) | -40.2 | 2.00 / 1.60 | +0.24 |

### AVL players (forecast ≥ 30 min), GW2-8

| player | pos | weeks | forecast/wk | realised/wk | residual/wk | sum |
|---|---|---|---|---|---|---|
| N.Jackson | FWD | 6 | 2.76 | 5.33 | +2.58 | +15.5 |
| Suzuki | GK | 6 | 2.25 | 4.67 | +2.42 | +14.5 |
| McGinn | MID | 7 | 3.01 | 4.71 | +1.70 | +11.9 |
| Manzambi | MID | 3 | 2.78 | 5.67 | +2.89 | +8.7 |
| Kamara | MID | 7 | 2.89 | 3.71 | +0.83 | +5.8 |
| Lindelöf | DEF | 7 | 2.62 | 3.43 | +0.81 | +5.7 |
| Cash | DEF | 6 | 2.28 | 3.17 | +0.89 | +5.3 |
| Buendía | MID | 7 | 3.11 | 3.71 | +0.61 | +4.2 |
| Gomes | MID | 3 | 2.34 | 3.00 | +0.66 | +2.0 |
| Wan-Bissaka | DEF | 4 | 2.02 | 2.00 | -0.02 | -0.1 |
| Mings | DEF | 5 | 2.32 | 2.20 | -0.12 | -0.6 |
| Maatsen | DEF | 4 | 2.47 | 2.25 | -0.22 | -0.9 |
| Abraham | FWD | 1 | 1.94 | 1.00 | -0.94 | -0.9 |
| Ruggeri | DEF | 1 | 1.94 | 1.00 | -0.94 | -0.9 |
| Alysson | MID | 1 | 1.69 | 0.00 | -1.69 | -1.7 |
| M.Bizot | GK | 1 | 1.96 | 0.00 | -1.96 | -2.0 |
| Pau | DEF | 2 | 2.19 | 1.00 | -1.19 | -2.4 |
| Barkley | MID | 5 | 2.38 | 1.80 | -0.58 | -2.9 |
| George Hemmings | MID | 5 | 2.13 | 1.40 | -0.73 | -3.6 |

### TOT players (forecast ≥ 30 min), GW2-8

| player | pos | weeks | forecast/wk | realised/wk | residual/wk | sum |
|---|---|---|---|---|---|---|
| Van Hecke | DEF | 7 | 3.31 | 5.29 | +1.98 | +13.9 |
| Kinsky | GK | 7 | 2.62 | 4.29 | +1.67 | +11.7 |
| Van de Ven | DEF | 6 | 2.42 | 4.00 | +1.58 | +9.5 |
| Robertson | DEF | 7 | 2.39 | 3.57 | +1.18 | +8.3 |
| Tonali | MID | 7 | 3.15 | 4.00 | +0.85 | +5.9 |
| Kudus | MID | 6 | 2.39 | 3.00 | +0.61 | +3.7 |
| Solanke | FWD | 5 | 2.41 | 3.00 | +0.59 | +3.0 |
| Pedro Porro | DEF | 2 | 2.37 | 3.50 | +1.13 | +2.3 |
| Marmoush | FWD | 6 | 2.80 | 3.00 | +0.20 | +1.2 |
| Fernandes | MID | 6 | 2.28 | 2.33 | +0.05 | +0.3 |
| Tosin | DEF | 1 | 1.01 | 0.00 | -1.01 | -1.0 |
| Maddison | MID | 1 | 2.20 | 1.00 | -1.20 | -1.2 |
| Richarlison | FWD | 1 | 2.59 | 0.00 | -2.59 | -2.6 |
| Moore | MID | 2 | 2.01 | 0.50 | -1.51 | -3.0 |
| Gray | MID | 6 | 2.51 | 2.00 | -0.51 | -3.0 |
| Udogie | DEF | 2 | 1.73 | 0.00 | -1.73 | -3.5 |
| Bentancur | MID | 6 | 2.66 | 2.00 | -0.66 | -3.9 |
| Bergvall | MID | 2 | 2.18 | 0.00 | -2.18 | -4.4 |
| Tel | MID | 4 | 2.73 | 1.50 | -1.23 | -4.9 |
| Sávio | MID | 4 | 3.00 | 1.75 | -1.25 | -5.0 |
| Gallagher | MID | 5 | 2.04 | 0.80 | -1.24 | -6.2 |
| Senesi | DEF | 3 | 2.78 | 0.00 | -2.78 | -8.3 |

### As-of GW9 team form the production features carry (last 5 weeks, GW4-8, per game) vs prior-season level

| club | last-5 GF | last-5 GA | last-5 GD | prior-season GD/game | trend5 | last-4 pts | flag |
|---|---|---|---|---|---|---|---|
| ARS | 1.40 | 0.80 | +0.60 | +1.16 | -0.56 | 9 |  |
| AVL | 1.80 | 1.40 | +0.40 | +0.18 | +0.22 | 10 |  |
| BOU | 1.60 | 1.60 | +0.00 | +0.11 | -0.11 | 6 |  |
| BRE | 1.80 | 1.40 | +0.40 | +0.08 | +0.32 | 5 |  |
| BHA | 3.00 | 0.40 | +2.60 | +0.16 | +2.44 | 9 |  |
| CHE | 1.80 | 1.60 | +0.20 | +0.16 | +0.04 | 6 |  |
| COV | 1.20 | 2.00 | -0.80 | promoted | — | 6 | |
| CRY | 1.00 | 2.20 | -1.20 | -0.26 | -0.94 | 4 |  |
| EVE | 0.60 | 1.20 | -0.60 | -0.08 | -0.52 | 4 |  |
| FUL | 0.80 | 0.60 | +0.20 | -0.11 | +0.31 | 7 |  |
| HUL | 1.20 | 1.60 | -0.40 | promoted | — | 2 | |
| IPS | 1.60 | 1.60 | +0.00 | promoted | — | 4 | |
| LEE | 1.20 | 0.80 | +0.40 | -0.18 | +0.58 | 3 |  |
| LIV | 1.00 | 0.80 | +0.20 | +0.26 | -0.06 | 9 |  |
| MCI | 2.60 | 1.40 | +1.20 | +1.11 | +0.09 | 9 |  |
| MUN | 0.60 | 1.40 | -0.80 | +0.50 | -1.30 | 3 | falling |
| NEW | 1.20 | 2.00 | -0.80 | -0.05 | -0.75 | 6 |  |
| NFO | 0.80 | 1.40 | -0.60 | -0.08 | -0.52 | 1 |  |
| TOT | 1.60 | 1.00 | +0.60 | -0.24 | +0.84 | 7 |  |
| SUN | 0.60 | 2.20 | -1.60 | -0.16 | -1.44 | 1 |  |
