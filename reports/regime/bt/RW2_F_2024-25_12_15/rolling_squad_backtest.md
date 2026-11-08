# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 233.18
- Total actual points: 269.00
- Average predicted points: 58.29
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
- Predicted score: 62.11
- Actual score: 55.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Sánchez | GK | 6 | 4.7 | 3.27 | 9.16 | 15.16 | 1.00 | 89.5 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.21 | 0.79 | 1.25 | 0.00 | 8.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.62 | 12.68 | 20.17 | 1.00 | 90.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.3 | 4.26 | 12.16 | 19.94 | 0.00 | 87.5 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 3.66 | 10.14 | 16.21 | 1.00 | 89.6 | 90.0 |
| Bench 2 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.42 | 7.75 | 12.59 | 1.00 | 81.3 | 90.0 |
| Bench 3 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 2.10 | 6.72 | 11.18 | 0.00 | 82.3 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 5.41 | 14.70 | 23.09 | 2.00 | 85.1 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.8 | 4.19 | 12.46 | 20.69 | 16.00 | 84.2 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 5.0 | 1.98 | 6.75 | 10.53 | 1.00 | 60.8 | 13.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 7.90 | 22.11 | 35.99 | 13.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.41 | 18.36 | 30.05 | 2.00 | 89.9 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 5.99 | 16.30 | 26.10 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 3.89 | 13.63 | 22.25 | 3.00 | 79.2 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 4.61 | 12.55 | 20.42 | 1.00 | 85.1 | 58.0 |

## GW13

- Train rows: 141592
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 66.24
- Actual score: 85.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.17) beats the best remaining Triple Captain opportunity (8.90).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.17) beats the best remaining Triple Captain opportunity (8.90).
- Autosub: Taylor Harwood-Bellis replaced Joško Gvardiol.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Sánchez | GK | 6 | 4.7 | 2.79 | 8.02 | 13.07 | 7.00 | 81.5 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.54 | 0.97 | 1.42 | 0.00 | 7.8 | 0.0 |
| XI | Bench | Joško Gvardiol | DEF | 13 | 6.3 | 3.70 | 11.56 | 19.31 | 0.00 | 87.3 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.76 | 11.11 | 17.91 | 6.00 | 86.2 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 2.74 | 8.37 | 13.56 | 2.00 | 73.9 | 90.0 |
| Bench 2 | Autosub In | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.56 | 7.95 | 12.94 | 1.00 | 83.8 | 90.0 |
| Bench 4 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.72 | 2.89 | 5.53 | 0.00 | 35.1 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 6.06 | 17.58 | 27.16 | 2.00 | 90.0 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 4.07 | 12.75 | 20.27 | 1.00 | 62.3 | 21.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 5.0 | 1.66 | 5.52 | 9.16 | 2.00 | 40.3 | 87.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 8.17 | 24.12 | 38.15 | 13.00 | 90.0 | 83.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.52 | 18.52 | 30.00 | 14.00 | 90.0 | 85.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.40 | 14.86 | 24.70 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.83 | 13.01 | 20.92 | 9.00 | 73.8 | 65.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 2.86 | 9.07 | 15.20 | 2.00 | 59.2 | 85.0 |

## GW14

- Train rows: 142282
- Bank: 0.00 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 61.91
- Actual score: 61.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (4.99) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Alexander Isak -> Nicolas Jackson (projected gain 9.28, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (4.99) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Sánchez | GK | 6 | 4.7 | 3.41 | 9.27 | 14.81 | 0.00 | 88.4 | 0.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.21 | 0.70 | 1.15 | 0.00 | 8.2 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.17 | 12.46 | 20.46 | 1.00 | 90.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 2.68 | 8.58 | 15.10 | 6.00 | 51.6 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 2.53 | 8.05 | 13.30 | 1.00 | 77.7 | 90.0 |
| Bench 3 | Bench Boost | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 1.88 | 5.89 | 9.81 | 0.00 | 69.7 | 0.0 |
| Bench 4 | Bench Boost | Jan Bednarek | DEF | 17 | 4.0 | 0.43 | 1.87 | 3.77 | 0.00 | 24.8 | 0.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 8.1 | 5.66 | 16.14 | 24.92 | 0.00 | 87.8 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.34 | 13.74 | 21.04 | 2.00 | 78.7 | 90.0 |
| Bench 2 | Bench Boost | Cameron Archer | FWD | 17 | 5.0 | 2.46 | 6.93 | 11.22 | 2.00 | 63.0 | 71.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 7.96 | 24.39 | 38.85 | 18.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 7.35 | 20.82 | 33.28 | 7.00 | 90.0 | 78.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.72 | 13.17 | 22.48 | 2.00 | 73.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.8 | 3.88 | 11.28 | 20.13 | 2.00 | 76.4 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.7 | 3.25 | 9.68 | 16.20 | 2.00 | 67.4 | 70.0 |

## GW15

- Train rows: 142975
- Bank: 0.40 -> 0.40
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Matheus Santos Carneiro Da Cunha
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 42.92
- Actual score: 68.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Sánchez | GK | 6 | 4.7 | 1.46 | 4.91 | 8.76 | 0.00 | 44.5 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.40 | 0.77 | 1.18 | 0.00 | 7.1 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 3.95 | 11.22 | 19.18 | 1.00 | 81.2 | 90.0 |
| Bench 2 | Bench | Virgil van Dijk | DEF | 12 | 6.3 | 0.00 | 9.82 | 16.73 | 0.00 | 0.0 | 0.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 2.71 | 7.73 | 12.61 | 1.00 | 78.1 | 82.0 |
| XI | XI | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 1.17 | 4.02 | 7.38 | 2.00 | 47.5 | 90.0 |
| Bench 3 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.00 | 0.90 | 2.32 | 0.00 | 13.7 | 0.0 |
| Vice Captain | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.69 | 13.28 | 21.39 | 1.00 | 83.8 | 90.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 8.1 | 2.74 | 8.98 | 14.65 | 2.00 | 33.0 | 75.0 |
| XI | XI | Cameron Archer | FWD | 17 | 5.0 | 2.32 | 6.68 | 11.22 | 2.00 | 61.9 | 72.0 |
| Bench 4 | Bench | Mohamed Salah | MID | 12 | 13.1 | 0.00 | 23.34 | 38.75 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 10.9 | 6.59 | 19.20 | 31.11 | 18.00 | 89.5 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.59 | 14.35 | 24.11 | 9.00 | 87.5 | 75.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 3.58 | 10.70 | 19.13 | 13.00 | 76.3 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.6 | 2.55 | 8.54 | 14.15 | 1.00 | 58.4 | 59.0 |