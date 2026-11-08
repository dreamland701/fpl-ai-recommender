# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 224.96
- Total actual points: 217.00
- Average predicted points: 56.24
- Average actual points: 54.25
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
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 63.13
- Actual score: 48.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 4.9 | 3.29 | 9.32 | 15.27 | 6.00 | 88.7 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.22 | 0.82 | 1.24 | 0.00 | 8.2 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.60 | 12.62 | 20.17 | 1.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.79 | 10.32 | 16.77 | 0.00 | 87.4 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 3.53 | 9.98 | 15.95 | 1.00 | 87.9 | 90.0 |
| Bench 3 | Bench | Wout Faes | DEF | 11 | 4.2 | 2.65 | 7.84 | 12.74 | 0.00 | 80.9 | 90.0 |
| Bench 4 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 2.21 | 7.09 | 11.70 | 0.00 | 83.2 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.2 | 8.04 | 22.27 | 36.77 | 2.00 | 90.0 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 5.37 | 14.79 | 23.24 | 2.00 | 84.7 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.8 | 4.17 | 12.49 | 20.83 | 16.00 | 83.3 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.0 | 7.92 | 22.23 | 36.20 | 13.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 5.95 | 16.34 | 26.08 | 2.00 | 90.0 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 4.62 | 12.45 | 20.17 | 1.00 | 84.2 | 58.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.4 | 3.81 | 11.00 | 17.66 | 2.00 | 77.0 | 81.0 |
| Bench 2 | Bench | Harry Winks | MID | 11 | 4.5 | 3.17 | 9.13 | 14.53 | 1.00 | 78.5 | 10.0 |

## GW13

- Train rows: 141592
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Matheus Santos Carneiro Da Cunha
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 62.72
- Actual score: 67.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.16) beats the best remaining Triple Captain opportunity (8.89).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.16) beats the best remaining Triple Captain opportunity (8.89).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 4.9 | 2.92 | 8.97 | 14.92 | 0.00 | 87.8 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.57 | 1.02 | 1.49 | 0.00 | 7.9 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.77 | 11.29 | 18.09 | 6.00 | 85.2 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.06 | 9.23 | 15.08 | 2.00 | 80.2 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 2.70 | 8.52 | 13.68 | 2.00 | 73.2 | 90.0 |
| Bench 2 | Bench | Wout Faes | DEF | 11 | 4.1 | 2.46 | 7.21 | 11.92 | 0.00 | 79.6 | 90.0 |
| Bench 4 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.83 | 3.30 | 5.98 | 0.00 | 36.2 | 0.0 |
| XI | XI | Erling Haaland | FWD | 13 | 15.1 | 5.92 | 18.42 | 31.74 | 2.00 | 81.4 | 90.0 |
| Vice Captain | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 5.95 | 17.38 | 26.93 | 2.00 | 90.0 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 4.03 | 12.99 | 20.80 | 1.00 | 61.7 | 21.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 8.16 | 24.32 | 38.52 | 13.00 | 90.0 | 83.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.80 | 13.14 | 21.28 | 9.00 | 72.1 | 65.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.4 | 3.11 | 9.58 | 15.89 | 2.00 | 68.7 | 65.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 2.97 | 9.32 | 15.62 | 2.00 | 59.7 | 85.0 |
| Bench 3 | Bench | Harry Winks | MID | 11 | 4.5 | 1.39 | 4.94 | 8.61 | 0.00 | 33.4 | 0.0 |

## GW14

- Train rows: 142282
- Bank: 0.00 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 59.45
- Actual score: 70.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (4.17) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Alexander Isak -> Nicolas Jackson (projected gain 8.09, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (4.17) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 4.9 | 3.03 | 8.75 | 14.56 | 6.00 | 86.0 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.22 | 0.72 | 1.20 | 0.00 | 8.3 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.72 | 13.97 | 22.71 | 1.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.31 | 9.41 | 15.29 | 6.00 | 82.5 | 90.0 |
| Bench 2 | Bench Boost | Lewis Hall | DEF | 15 | 4.4 | 2.50 | 8.16 | 13.42 | 1.00 | 77.7 | 90.0 |
| XI | XI | Wout Faes | DEF | 11 | 4.1 | 2.60 | 6.92 | 11.20 | 1.00 | 80.4 | 30.0 |
| Bench 4 | Bench Boost | Jan Bednarek | DEF | 17 | 4.0 | 0.46 | 2.03 | 3.94 | 0.00 | 25.0 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 15.0 | 6.18 | 19.11 | 32.47 | 5.00 | 83.1 | 90.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 8.1 | 5.62 | 16.14 | 24.91 | 0.00 | 86.1 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.21 | 13.79 | 21.37 | 2.00 | 75.6 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 7.90 | 24.29 | 38.90 | 18.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.66 | 13.13 | 22.58 | 2.00 | 73.7 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.7 | 3.24 | 9.69 | 16.30 | 2.00 | 68.0 | 70.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.3 | 2.91 | 8.42 | 14.04 | 8.00 | 61.5 | 86.0 |
| Bench 3 | Bench Boost | Harry Winks | MID | 11 | 4.5 | 0.98 | 3.16 | 5.72 | 0.00 | 19.5 | 0.0 |

## GW15

- Train rows: 142975
- Bank: 0.40 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Matheus Santos Carneiro Da Cunha
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 39.66
- Actual score: 32.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 4.9 | 0.00 | 7.80 | 13.53 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Killian Cahill | GK | 5 | 3.9 | 0.43 | 0.81 | 1.26 | 0.00 | 7.2 | 0.0 |
| Bench 2 | Bench | Virgil van Dijk | DEF | 12 | 6.3 | 0.00 | 9.83 | 16.64 | 0.00 | 0.0 | 0.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 2.86 | 9.18 | 15.04 | 1.00 | 82.8 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 2.64 | 7.64 | 12.51 | 1.00 | 77.3 | 82.0 |
| XI | XI | Wout Faes | DEF | 11 | 4.1 | 1.86 | 5.43 | 9.28 | 1.00 | 60.9 | 9.0 |
| Bench 3 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.00 | 0.87 | 2.21 | 0.00 | 13.6 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.0 | 6.45 | 19.16 | 32.54 | 7.00 | 90.0 | 90.0 |
| Vice Captain | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.69 | 13.41 | 21.58 | 1.00 | 83.1 | 90.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 8.1 | 2.76 | 9.20 | 15.04 | 2.00 | 32.7 | 75.0 |
| Bench 4 | Bench | Mohamed Salah | MID | 12 | 13.1 | 0.00 | 23.36 | 38.84 | 0.00 | 0.0 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.52 | 14.30 | 24.02 | 9.00 | 87.1 | 75.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.3 | 4.18 | 11.28 | 18.14 | 2.00 | 75.7 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.6 | 2.51 | 8.51 | 14.12 | 1.00 | 58.9 | 59.0 |
| XI | Bench | Harry Winks | MID | 11 | 4.5 | 0.29 | 1.45 | 3.03 | 0.00 | 6.6 | 0.0 |