# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 236.09
- Total actual points: 269.00
- Average predicted points: 59.02
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
- Predicted score: 62.14
- Actual score: 55.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Sánchez | GK | 6 | 4.7 | 3.29 | 9.21 | 15.22 | 1.00 | 87.1 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.27 | 0.97 | 1.54 | 0.00 | 5.8 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.61 | 12.67 | 20.17 | 1.00 | 90.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.3 | 4.26 | 12.17 | 20.00 | 0.00 | 89.1 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 3.67 | 10.17 | 16.25 | 1.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.41 | 7.75 | 12.60 | 1.00 | 82.5 | 90.0 |
| Bench 2 | Bench | Dara O'Shea | DEF | 10 | 4.0 | 2.46 | 6.76 | 10.99 | 2.00 | 83.2 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 5.44 | 14.78 | 23.23 | 2.00 | 85.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.8 | 4.19 | 12.41 | 20.56 | 16.00 | 83.1 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 5.0 | 1.98 | 6.70 | 10.39 | 1.00 | 59.7 | 13.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 7.92 | 22.28 | 36.36 | 13.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.41 | 18.40 | 30.14 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 6.02 | 16.40 | 26.29 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 3.86 | 13.48 | 21.98 | 3.00 | 78.7 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 4.57 | 12.40 | 20.14 | 1.00 | 84.4 | 58.0 |

## GW13

- Train rows: 141592
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 66.28
- Actual score: 85.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.18) beats the best remaining Triple Captain opportunity (8.92).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.18) beats the best remaining Triple Captain opportunity (8.92).
- Autosub: Taylor Harwood-Bellis replaced Joško Gvardiol.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Sánchez | GK | 6 | 4.7 | 2.83 | 8.13 | 13.23 | 7.00 | 79.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.60 | 1.16 | 1.73 | 0.00 | 5.6 | 0.0 |
| XI | Bench | Joško Gvardiol | DEF | 13 | 6.3 | 3.71 | 11.62 | 19.46 | 0.00 | 88.8 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.75 | 11.09 | 17.91 | 6.00 | 87.7 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 2.75 | 8.40 | 13.62 | 2.00 | 74.8 | 90.0 |
| Bench 2 | Autosub In | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.54 | 7.90 | 12.87 | 1.00 | 84.8 | 90.0 |
| Bench 3 | Bench | Dara O'Shea | DEF | 10 | 4.0 | 2.16 | 6.68 | 10.89 | 1.00 | 80.6 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 6.05 | 17.49 | 26.96 | 2.00 | 90.0 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 4.09 | 12.84 | 20.45 | 1.00 | 62.9 | 21.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 5.0 | 1.66 | 5.49 | 9.07 | 2.00 | 39.2 | 87.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 8.18 | 24.26 | 38.48 | 13.00 | 90.0 | 83.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.52 | 18.53 | 30.03 | 14.00 | 90.0 | 85.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.34 | 14.66 | 24.34 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.87 | 13.13 | 21.16 | 9.00 | 73.9 | 65.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 2.83 | 8.94 | 14.94 | 2.00 | 58.5 | 85.0 |

## GW14

- Train rows: 142282
- Bank: 0.00 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 63.79
- Actual score: 62.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.90) beats the best remaining Bench Boost opportunity (1.15).
- Transfer: Alexander Isak -> Nicolas Jackson (projected gain 9.31, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.90) beats the best remaining Bench Boost opportunity (1.15).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Sánchez | GK | 6 | 4.7 | 3.45 | 9.38 | 14.97 | 0.00 | 85.7 | 0.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.27 | 0.89 | 1.47 | 0.00 | 6.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.16 | 12.43 | 20.44 | 1.00 | 90.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 2.68 | 8.62 | 15.20 | 6.00 | 53.2 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 2.53 | 8.05 | 13.33 | 1.00 | 78.7 | 90.0 |
| Bench 3 | Bench Boost | Dara O'Shea | DEF | 10 | 4.0 | 2.31 | 6.54 | 10.84 | 1.00 | 79.6 | 90.0 |
| Bench 4 | Bench Boost | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 1.87 | 5.85 | 9.77 | 0.00 | 70.5 | 0.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 8.1 | 5.67 | 16.12 | 24.89 | 0.00 | 87.1 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.33 | 13.67 | 20.88 | 2.00 | 77.6 | 90.0 |
| Bench 2 | Bench Boost | Cameron Archer | FWD | 17 | 5.0 | 2.45 | 6.86 | 11.06 | 2.00 | 61.8 | 71.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 7.98 | 24.54 | 39.16 | 18.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 7.34 | 20.81 | 33.25 | 7.00 | 90.0 | 78.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.74 | 13.23 | 22.61 | 2.00 | 73.7 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.8 | 3.83 | 11.08 | 19.78 | 2.00 | 76.3 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.7 | 3.21 | 9.53 | 15.91 | 2.00 | 66.6 | 70.0 |

## GW15

- Train rows: 142975
- Bank: 0.40 -> 0.40
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Matheus Santos Carneiro Da Cunha
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 43.86
- Actual score: 67.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Sánchez | GK | 6 | 4.7 | 1.49 | 5.02 | 8.92 | 0.00 | 42.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.45 | 0.96 | 1.49 | 0.00 | 5.0 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 3.95 | 11.26 | 19.28 | 1.00 | 82.6 | 90.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 12 | 6.3 | 0.00 | 9.79 | 16.70 | 0.00 | 0.0 | 0.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 2.70 | 7.73 | 12.64 | 1.00 | 79.3 | 82.0 |
| XI | XI | Dara O'Shea | DEF | 10 | 4.0 | 2.18 | 6.29 | 10.46 | 1.00 | 78.1 | 90.0 |
| Bench 2 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 1.15 | 3.98 | 7.34 | 2.00 | 48.8 | 90.0 |
| Vice Captain | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.65 | 13.11 | 21.07 | 1.00 | 82.8 | 90.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 8.1 | 2.73 | 8.93 | 14.54 | 2.00 | 32.3 | 75.0 |
| XI | XI | Cameron Archer | FWD | 17 | 5.0 | 2.30 | 6.60 | 11.06 | 2.00 | 60.7 | 72.0 |
| Bench 4 | Bench | Mohamed Salah | MID | 12 | 13.1 | 0.00 | 23.45 | 38.97 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 10.9 | 6.60 | 19.27 | 31.24 | 18.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.60 | 14.39 | 24.18 | 9.00 | 87.7 | 75.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 3.53 | 10.50 | 18.77 | 13.00 | 75.8 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.6 | 2.51 | 8.40 | 13.86 | 1.00 | 57.6 | 59.0 |