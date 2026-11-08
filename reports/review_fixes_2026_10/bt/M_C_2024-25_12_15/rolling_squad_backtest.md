# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 245.85
- Total actual points: 284.00
- Average predicted points: 61.46
- Average actual points: 71.00
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW11 are included before the first simulated week.
- League-average scores were not available for this run.

## GW12

- Train rows: 140908
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 56.26
- Actual score: 58.00
- Chip advisory: bench_boost (0.62): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.35 | 10.02 | 16.64 | 6.00 | 86.9 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 4.9 | 3.13 | 9.45 | 15.59 | 6.00 | 87.9 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.3 | 4.44 | 12.94 | 21.32 | 0.00 | 88.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 4.15 | 11.74 | 19.27 | 1.00 | 89.1 | 90.0 |
| Bench 3 | Bench | Pedro Porro | DEF | 18 | 5.5 | 3.67 | 11.15 | 18.46 | 14.00 | 86.4 | 90.0 |
| Bench 4 | Bench | Rayan Aït-Nouri | DEF | 20 | 4.7 | 3.56 | 10.96 | 17.93 | 2.00 | 89.7 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.86 | 10.93 | 17.88 | 0.00 | 89.1 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.7 | 4.21 | 12.62 | 20.78 | 16.00 | 83.0 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.6 | 3.91 | 12.31 | 19.68 | 1.00 | 74.4 | 27.0 |
| Bench 2 | Bench | Danny Welbeck | FWD | 5 | 5.9 | 3.75 | 11.55 | 18.84 | 2.00 | 75.7 | 85.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 12.8 | 6.58 | 19.23 | 31.63 | 13.00 | 88.7 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.0 | 5.88 | 17.16 | 28.84 | 2.00 | 85.9 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.08 | 15.72 | 25.94 | 3.00 | 93.8 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.7 | 4.46 | 12.52 | 20.54 | 1.00 | 82.6 | 58.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.4 | 3.76 | 10.98 | 18.22 | 2.00 | 74.0 | 81.0 |

## GW13

- Train rows: 141592
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 63.81
- Actual score: 73.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.09) beats the best remaining Triple Captain opportunity (7.84).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.09) beats the best remaining Triple Captain opportunity (7.84).
- Autosub: Rayan Aït-Nouri replaced Joško Gvardiol.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.57 | 10.28 | 16.91 | 2.00 | 84.9 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 4.9 | 3.06 | 9.39 | 15.69 | 0.00 | 86.7 | 90.0 |
| XI | Bench | Joško Gvardiol | DEF | 13 | 6.3 | 4.11 | 13.20 | 22.00 | 0.00 | 92.0 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 4.22 | 12.30 | 20.47 | 2.00 | 91.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 3.67 | 11.25 | 18.26 | 6.00 | 84.2 | 90.0 |
| Bench 3 | Bench | Antonee Robinson | DEF | 9 | 4.7 | 3.45 | 10.33 | 17.04 | 2.00 | 84.8 | 90.0 |
| Bench 2 | Autosub In | Rayan Aït-Nouri | DEF | 20 | 4.7 | 3.49 | 10.17 | 16.53 | 0.00 | 85.6 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.7 | 5.01 | 14.54 | 23.50 | 2.00 | 92.0 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.9 | 4.05 | 11.31 | 18.33 | 2.00 | 75.5 | 78.0 |
| Bench 4 | Bench | Chris Wood | FWD | 16 | 6.6 | 3.40 | 10.36 | 17.41 | 9.00 | 52.2 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 12.9 | 7.09 | 21.24 | 34.34 | 13.00 | 95.0 | 83.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 5.76 | 16.80 | 27.65 | 14.00 | 83.3 | 85.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.02 | 14.77 | 24.77 | 2.00 | 87.8 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.7 | 3.62 | 10.92 | 18.13 | 2.00 | 67.8 | 85.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.4 | 3.50 | 10.69 | 17.75 | 2.00 | 72.2 | 65.0 |

## GW14

- Train rows: 142282
- Bank: 0.10 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 70.30
- Actual score: 80.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (12.80) beats the best remaining Bench Boost opportunity (2.18).
- Transfer: Morgan Rogers -> Justin Kluivert (projected gain 1.87, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (12.80) beats the best remaining Bench Boost opportunity (2.18).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.50 | 9.85 | 16.31 | 6.00 | 83.9 | 90.0 |
| Bench 1 | Bench Boost | Jordan Pickford | GK | 8 | 4.9 | 2.98 | 8.99 | 15.14 | 6.00 | 84.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 3.99 | 12.28 | 20.30 | 1.00 | 90.1 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 4.03 | 12.16 | 19.87 | 1.00 | 87.5 | 28.0 |
| Bench 2 | Bench Boost | Rayan Aït-Nouri | DEF | 20 | 4.7 | 3.47 | 10.35 | 16.93 | 0.00 | 86.2 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.49 | 10.11 | 16.61 | 6.00 | 84.4 | 90.0 |
| Bench 4 | Bench Boost | Joško Gvardiol | DEF | 13 | 6.3 | 2.91 | 9.56 | 16.77 | 6.00 | 53.4 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.8 | 4.64 | 14.20 | 22.24 | 2.00 | 79.3 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.6 | 3.69 | 11.74 | 19.16 | 2.00 | 74.4 | 61.0 |
| Bench 3 | Bench Boost | Danny Welbeck | FWD | 5 | 5.9 | 3.44 | 10.60 | 17.64 | 0.00 | 72.3 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 12.9 | 7.53 | 22.66 | 36.77 | 18.00 | 101.6 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.60 | 18.66 | 30.57 | 7.00 | 92.6 | 78.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 4.33 | 13.65 | 23.14 | 2.00 | 86.7 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.3 | 4.56 | 12.19 | 19.47 | 3.00 | 79.3 | 63.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.7 | 3.61 | 10.90 | 18.29 | 2.00 | 72.2 | 70.0 |

## GW15

- Train rows: 142975
- Bank: 0.20 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 55.48
- Actual score: 73.00
- Transfer: Emile Smith Rowe -> Alex Iwobi (projected gain 4.13, hit 0)
- Autosub: Rayan Aït-Nouri replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.52 | 10.55 | 17.44 | 2.00 | 85.4 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 4.9 | 2.29 | 8.05 | 13.97 | 0.00 | 63.9 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 3.90 | 11.80 | 20.11 | 1.00 | 78.1 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 3.40 | 10.47 | 17.84 | 3.00 | 71.8 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.22 | 10.18 | 16.74 | 1.00 | 86.9 | 90.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 12 | 6.3 | 2.91 | 10.00 | 17.01 | 0.00 | 65.7 | 0.0 |
| Bench 2 | Autosub In | Rayan Aït-Nouri | DEF | 20 | 4.8 | 3.13 | 8.74 | 14.36 | 4.00 | 81.3 | 85.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.60 | 13.43 | 21.80 | 1.00 | 84.3 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.6 | 3.38 | 10.59 | 17.75 | 8.00 | 62.9 | 78.0 |
| Bench 4 | Bench | Danny Welbeck | FWD | 5 | 5.9 | 2.63 | 7.98 | 14.00 | 1.00 | 43.1 | 20.0 |
| Captain | Bench | Mohamed Salah | MID | 12 | 13.0 | 7.49 | 23.35 | 38.72 | 0.00 | 91.3 | 0.0 |
| Vice Captain | Captain | Cole Palmer | MID | 6 | 11.0 | 6.58 | 18.85 | 30.46 | 18.00 | 87.0 | 90.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.6 | 4.18 | 12.86 | 21.10 | 2.00 | 92.2 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.8 | 3.87 | 12.19 | 21.45 | 13.00 | 78.4 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.3 | 3.84 | 10.73 | 17.21 | 2.00 | 64.2 | 62.0 |