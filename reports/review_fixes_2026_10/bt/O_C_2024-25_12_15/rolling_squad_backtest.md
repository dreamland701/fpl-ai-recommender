# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 246.06
- Total actual points: 286.00
- Average predicted points: 61.52
- Average actual points: 71.50
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
- Predicted score: 56.39
- Actual score: 58.00
- Chip advisory: bench_boost (0.62): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.37 | 10.01 | 16.56 | 6.00 | 86.8 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 4.9 | 3.11 | 9.40 | 15.51 | 6.00 | 88.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.3 | 4.47 | 12.97 | 21.23 | 0.00 | 88.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 4.17 | 11.79 | 19.27 | 1.00 | 89.0 | 90.0 |
| Bench 3 | Bench | Pedro Porro | DEF | 18 | 5.5 | 3.68 | 11.14 | 18.38 | 14.00 | 86.4 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.90 | 10.92 | 17.80 | 0.00 | 89.1 | 90.0 |
| Bench 4 | Bench | Rayan Aït-Nouri | DEF | 20 | 4.7 | 3.56 | 10.85 | 17.63 | 2.00 | 89.7 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.7 | 4.21 | 12.60 | 20.74 | 16.00 | 83.0 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.6 | 3.87 | 12.26 | 19.66 | 1.00 | 74.4 | 27.0 |
| Bench 2 | Bench | Danny Welbeck | FWD | 5 | 5.9 | 3.72 | 11.57 | 18.94 | 2.00 | 75.7 | 85.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 12.8 | 6.60 | 19.26 | 31.67 | 13.00 | 88.7 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.0 | 5.88 | 17.19 | 28.96 | 2.00 | 85.9 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.07 | 15.72 | 25.91 | 3.00 | 93.8 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.7 | 4.50 | 12.49 | 20.50 | 1.00 | 82.5 | 58.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.4 | 3.75 | 10.96 | 18.23 | 2.00 | 74.0 | 81.0 |

## GW13

- Train rows: 141592
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 63.85
- Actual score: 75.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.10) beats the best remaining Triple Captain opportunity (7.79).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.10) beats the best remaining Triple Captain opportunity (7.79).
- Autosub outfielders: Antonee Robinson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.60 | 10.24 | 16.77 | 2.00 | 84.9 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 4.9 | 3.08 | 9.42 | 15.70 | 0.00 | 86.6 | 90.0 |
| XI | Bench | Joško Gvardiol | DEF | 13 | 6.3 | 4.12 | 13.24 | 22.03 | 0.00 | 92.0 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 4.22 | 12.31 | 20.49 | 2.00 | 91.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.68 | 11.26 | 18.22 | 6.00 | 84.2 | 90.0 |
| Bench 2 | Autosub In | Antonee Robinson | DEF | 9 | 4.7 | 3.48 | 10.31 | 16.97 | 2.00 | 84.8 | 90.0 |
| Bench 3 | Bench | Rayan Aït-Nouri | DEF | 20 | 4.8 | 3.46 | 10.07 | 16.32 | 0.00 | 85.6 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.8 | 4.99 | 14.60 | 23.64 | 2.00 | 92.0 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 6.0 | 4.07 | 11.40 | 18.47 | 2.00 | 75.5 | 78.0 |
| Bench 4 | Bench | Chris Wood | FWD | 16 | 6.6 | 3.39 | 10.44 | 17.66 | 9.00 | 52.2 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 7.10 | 21.35 | 34.50 | 13.00 | 95.0 | 83.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 5.73 | 16.76 | 27.56 | 14.00 | 83.3 | 85.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.02 | 14.80 | 24.80 | 2.00 | 87.8 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 3.65 | 10.94 | 18.19 | 2.00 | 67.8 | 85.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.4 | 3.48 | 10.73 | 17.82 | 2.00 | 72.2 | 65.0 |

## GW14

- Train rows: 142282
- Bank: 0.10 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 70.36
- Actual score: 80.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (12.84) beats the best remaining Bench Boost opportunity (2.20).
- Transfer: Morgan Rogers -> Justin Kluivert (projected gain 2.02, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (12.84) beats the best remaining Bench Boost opportunity (2.20).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.51 | 9.82 | 16.23 | 6.00 | 83.9 | 90.0 |
| Bench 1 | Bench Boost | Jordan Pickford | GK | 8 | 4.9 | 3.02 | 9.01 | 15.18 | 6.00 | 84.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.01 | 12.25 | 20.19 | 1.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 4.00 | 12.11 | 19.82 | 1.00 | 87.6 | 28.0 |
| Bench 2 | Bench Boost | Rayan Aït-Nouri | DEF | 20 | 4.8 | 3.45 | 10.27 | 16.73 | 0.00 | 86.2 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.47 | 10.06 | 16.57 | 6.00 | 84.4 | 90.0 |
| Bench 4 | Bench Boost | Joško Gvardiol | DEF | 13 | 6.3 | 2.93 | 9.61 | 16.80 | 6.00 | 53.3 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.0 | 4.63 | 14.24 | 22.42 | 2.00 | 79.3 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.6 | 3.70 | 11.87 | 19.49 | 2.00 | 74.4 | 61.0 |
| Bench 3 | Bench Boost | Danny Welbeck | FWD | 5 | 6.0 | 3.44 | 10.63 | 17.70 | 0.00 | 72.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 7.55 | 22.82 | 37.04 | 18.00 | 101.5 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.63 | 18.74 | 30.62 | 7.00 | 92.6 | 78.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 4.30 | 13.64 | 23.11 | 2.00 | 86.7 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.3 | 4.58 | 12.26 | 19.64 | 3.00 | 79.2 | 63.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 3.59 | 10.89 | 18.42 | 2.00 | 72.3 | 70.0 |

## GW15

- Train rows: 142975
- Bank: 0.20 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 55.46
- Actual score: 73.00
- Transfer: Emile Smith Rowe -> Alex Iwobi (projected gain 4.03, hit 0)
- Autosub outfielders: Rayan Aït-Nouri.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.52 | 10.49 | 17.34 | 2.00 | 85.4 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 4.9 | 2.29 | 8.02 | 13.91 | 0.00 | 64.0 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 3.89 | 11.80 | 19.92 | 1.00 | 78.1 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 3.39 | 10.42 | 17.76 | 3.00 | 71.9 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.18 | 10.12 | 16.71 | 1.00 | 87.0 | 90.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 12 | 6.4 | 2.91 | 9.96 | 16.96 | 0.00 | 65.7 | 0.0 |
| Bench 2 | Autosub In | Rayan Aït-Nouri | DEF | 20 | 4.9 | 3.16 | 8.76 | 14.35 | 4.00 | 81.3 | 85.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.63 | 13.46 | 21.96 | 1.00 | 84.2 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.6 | 3.40 | 10.66 | 17.95 | 8.00 | 62.8 | 78.0 |
| Bench 4 | Bench | Danny Welbeck | FWD | 5 | 5.9 | 2.63 | 8.00 | 13.91 | 1.00 | 43.1 | 20.0 |
| Captain | Bench | Mohamed Salah | MID | 12 | 13.2 | 7.49 | 23.45 | 39.02 | 0.00 | 91.3 | 0.0 |
| Vice Captain | Captain | Cole Palmer | MID | 6 | 11.0 | 6.61 | 18.96 | 30.70 | 18.00 | 86.9 | 90.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.6 | 4.14 | 12.76 | 21.13 | 2.00 | 92.2 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.8 | 3.89 | 12.20 | 21.25 | 13.00 | 78.4 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.4 | 3.83 | 10.73 | 17.39 | 2.00 | 64.2 | 62.0 |