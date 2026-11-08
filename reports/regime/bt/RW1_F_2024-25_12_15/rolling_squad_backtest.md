# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 237.34
- Total actual points: 269.00
- Average predicted points: 59.33
- Average actual points: 67.25
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
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 62.29
- Actual score: 55.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Sánchez | GK | 6 | 4.7 | 3.25 | 9.16 | 15.40 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.19 | 0.74 | 1.21 | 0.00 | 7.6 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.61 | 12.75 | 20.15 | 1.00 | 90.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.3 | 4.31 | 12.33 | 20.29 | 0.00 | 88.3 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 3.70 | 10.11 | 16.18 | 1.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.42 | 7.69 | 12.59 | 1.00 | 81.4 | 90.0 |
| Bench 2 | Bench | Dara O'Shea | DEF | 10 | 4.0 | 2.50 | 6.82 | 11.08 | 2.00 | 81.7 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 5.42 | 14.58 | 22.89 | 2.00 | 84.8 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.8 | 4.23 | 12.58 | 20.71 | 16.00 | 85.0 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 5.0 | 2.03 | 6.94 | 10.65 | 1.00 | 61.7 | 13.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 7.92 | 22.11 | 35.93 | 13.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.45 | 18.49 | 30.25 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 5.93 | 16.13 | 25.81 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 3.97 | 13.79 | 22.36 | 3.00 | 80.9 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 4.57 | 12.62 | 20.62 | 1.00 | 85.7 | 58.0 |

## GW13

- Train rows: 141592
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 66.78
- Actual score: 85.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.22) beats the best remaining Triple Captain opportunity (8.96).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.22) beats the best remaining Triple Captain opportunity (8.96).
- Autosub: Taylor Harwood-Bellis replaced Joško Gvardiol.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Sánchez | GK | 6 | 4.7 | 2.79 | 7.98 | 13.13 | 7.00 | 81.9 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.51 | 0.93 | 1.37 | 0.00 | 7.6 | 0.0 |
| XI | Bench | Joško Gvardiol | DEF | 13 | 6.3 | 3.79 | 11.75 | 19.64 | 0.00 | 88.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.77 | 10.99 | 17.83 | 6.00 | 86.9 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 2.81 | 8.28 | 13.48 | 2.00 | 74.7 | 90.0 |
| Bench 2 | Autosub In | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.55 | 7.94 | 13.01 | 1.00 | 84.1 | 90.0 |
| Bench 3 | Bench | Dara O'Shea | DEF | 10 | 4.0 | 2.19 | 6.62 | 10.80 | 1.00 | 78.7 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 6.05 | 17.55 | 27.08 | 2.00 | 90.0 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 4.21 | 12.82 | 20.22 | 1.00 | 63.4 | 21.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 5.0 | 1.70 | 5.72 | 9.38 | 2.00 | 40.4 | 87.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 8.22 | 23.98 | 37.89 | 13.00 | 90.0 | 83.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.53 | 18.43 | 29.99 | 14.00 | 90.0 | 85.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.38 | 14.91 | 24.76 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.92 | 13.02 | 20.73 | 9.00 | 75.2 | 65.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 2.86 | 9.07 | 15.11 | 2.00 | 59.2 | 85.0 |

## GW14

- Train rows: 142282
- Bank: 0.00 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 64.09
- Actual score: 62.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.82) beats the best remaining Bench Boost opportunity (1.07).
- Transfer: Alexander Isak -> Nicolas Jackson (projected gain 9.14, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.82) beats the best remaining Bench Boost opportunity (1.07).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Sánchez | GK | 6 | 4.7 | 3.34 | 9.11 | 14.63 | 0.00 | 88.4 | 0.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.20 | 0.65 | 1.11 | 0.00 | 7.8 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.11 | 12.22 | 20.38 | 1.00 | 90.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 2.70 | 8.70 | 15.50 | 6.00 | 51.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 2.55 | 7.97 | 13.21 | 1.00 | 78.1 | 90.0 |
| Bench 3 | Bench Boost | Dara O'Shea | DEF | 10 | 4.0 | 2.27 | 6.33 | 10.68 | 1.00 | 77.6 | 90.0 |
| Bench 4 | Bench Boost | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 1.89 | 5.85 | 9.70 | 0.00 | 70.5 | 0.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 8.1 | 5.68 | 16.07 | 24.77 | 0.00 | 88.0 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.51 | 13.89 | 20.97 | 2.00 | 80.7 | 90.0 |
| Bench 2 | Bench Boost | Cameron Archer | FWD | 17 | 5.0 | 2.47 | 6.97 | 11.35 | 2.00 | 63.9 | 71.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 8.01 | 24.40 | 38.67 | 18.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 7.31 | 20.78 | 33.20 | 7.00 | 90.0 | 78.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.82 | 13.33 | 22.47 | 2.00 | 73.7 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.8 | 3.94 | 11.24 | 20.10 | 2.00 | 76.4 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.7 | 3.29 | 9.84 | 16.32 | 2.00 | 68.1 | 70.0 |

## GW15

- Train rows: 142975
- Bank: 0.40 -> 0.40
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Matheus Santos Carneiro Da Cunha
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 44.18
- Actual score: 67.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Sánchez | GK | 6 | 4.7 | 1.43 | 4.77 | 8.66 | 0.00 | 43.7 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.36 | 0.73 | 1.10 | 0.00 | 6.8 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 3.87 | 11.03 | 19.23 | 1.00 | 81.7 | 90.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 12 | 6.3 | 0.00 | 9.85 | 16.80 | 0.00 | 0.0 | 0.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 2.74 | 7.79 | 12.66 | 1.00 | 78.6 | 82.0 |
| XI | XI | Dara O'Shea | DEF | 10 | 4.0 | 2.14 | 6.14 | 10.31 | 1.00 | 76.1 | 90.0 |
| Bench 2 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 1.15 | 3.95 | 7.27 | 2.00 | 46.2 | 90.0 |
| Vice Captain | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.75 | 13.31 | 21.35 | 1.00 | 84.6 | 90.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 8.1 | 2.84 | 9.03 | 14.58 | 2.00 | 32.8 | 75.0 |
| XI | XI | Cameron Archer | FWD | 17 | 5.0 | 2.39 | 6.81 | 11.46 | 2.00 | 62.6 | 72.0 |
| Bench 4 | Bench | Mohamed Salah | MID | 12 | 13.1 | 0.00 | 23.41 | 38.64 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 10.9 | 6.60 | 18.98 | 30.73 | 18.00 | 88.7 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.64 | 14.38 | 24.16 | 9.00 | 88.0 | 75.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 3.59 | 10.63 | 19.17 | 13.00 | 77.0 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.6 | 2.61 | 8.70 | 14.37 | 1.00 | 58.7 | 59.0 |