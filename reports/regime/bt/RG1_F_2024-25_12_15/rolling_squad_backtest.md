# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 224.63
- Total actual points: 228.00
- Average predicted points: 56.16
- Average actual points: 57.00
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
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 63.34
- Actual score: 59.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 4.9 | 3.30 | 9.34 | 15.30 | 6.00 | 86.2 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.28 | 1.02 | 1.56 | 0.00 | 6.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.63 | 12.71 | 20.36 | 1.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.80 | 10.38 | 16.90 | 0.00 | 88.6 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 3.58 | 10.09 | 16.15 | 1.00 | 89.1 | 90.0 |
| Bench 3 | Bench | Wout Faes | DEF | 11 | 4.2 | 2.62 | 7.78 | 12.68 | 0.00 | 82.1 | 90.0 |
| Bench 4 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 2.20 | 7.05 | 11.67 | 0.00 | 84.1 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 15.2 | 8.01 | 22.31 | 37.07 | 2.00 | 90.0 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 5.43 | 14.96 | 23.56 | 2.00 | 85.2 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.8 | 4.16 | 12.40 | 20.65 | 16.00 | 82.1 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 8.01 | 22.59 | 36.95 | 13.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 6.05 | 16.61 | 26.56 | 2.00 | 90.0 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 4.59 | 12.32 | 19.95 | 1.00 | 84.0 | 58.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.4 | 3.77 | 10.87 | 17.48 | 2.00 | 76.8 | 81.0 |
| Bench 2 | Bench | Harry Winks | MID | 11 | 4.5 | 3.09 | 8.85 | 14.02 | 1.00 | 77.1 | 10.0 |

## GW13

- Train rows: 141592
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Matheus Santos Carneiro Da Cunha
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 62.85
- Actual score: 67.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.23) beats the best remaining Triple Captain opportunity (8.97).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.23) beats the best remaining Triple Captain opportunity (8.97).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 4.9 | 2.92 | 8.96 | 14.90 | 0.00 | 85.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.63 | 1.20 | 1.79 | 0.00 | 5.6 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.77 | 11.30 | 18.17 | 6.00 | 86.9 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.06 | 9.22 | 15.10 | 2.00 | 81.1 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 2.71 | 8.55 | 13.78 | 2.00 | 73.8 | 90.0 |
| Bench 2 | Bench | Wout Faes | DEF | 11 | 4.1 | 2.44 | 7.19 | 11.94 | 0.00 | 81.0 | 90.0 |
| Bench 4 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.81 | 3.24 | 5.96 | 0.00 | 36.5 | 0.0 |
| XI | XI | Erling Haaland | FWD | 13 | 15.1 | 5.87 | 18.43 | 31.99 | 2.00 | 81.0 | 90.0 |
| Vice Captain | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 6.00 | 17.41 | 26.89 | 2.00 | 90.0 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 4.05 | 13.05 | 20.99 | 1.00 | 62.0 | 21.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 8.23 | 24.61 | 39.14 | 13.00 | 90.0 | 83.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.84 | 13.25 | 21.54 | 9.00 | 71.9 | 65.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.4 | 3.06 | 9.43 | 15.67 | 2.00 | 68.2 | 65.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 2.89 | 9.07 | 15.21 | 2.00 | 58.7 | 85.0 |
| Bench 3 | Bench | Harry Winks | MID | 11 | 4.5 | 1.30 | 4.64 | 8.11 | 0.00 | 31.3 | 0.0 |

## GW14

- Train rows: 142282
- Bank: 0.00 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 58.99
- Actual score: 70.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (4.13) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Alexander Isak -> Nicolas Jackson (projected gain 8.14, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (4.13) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 4.9 | 3.04 | 8.80 | 14.65 | 6.00 | 83.7 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.28 | 0.92 | 1.51 | 0.00 | 6.1 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.24 | 12.71 | 20.61 | 1.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.30 | 9.38 | 15.29 | 6.00 | 83.3 | 90.0 |
| Bench 2 | Bench Boost | Lewis Hall | DEF | 15 | 4.4 | 2.51 | 8.17 | 13.50 | 1.00 | 78.5 | 90.0 |
| XI | XI | Wout Faes | DEF | 11 | 4.1 | 2.59 | 6.92 | 11.24 | 1.00 | 81.8 | 30.0 |
| Bench 4 | Bench Boost | Jan Bednarek | DEF | 17 | 4.0 | 0.45 | 2.01 | 3.94 | 0.00 | 25.5 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 15.0 | 6.16 | 19.17 | 32.82 | 5.00 | 82.8 | 90.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 8.1 | 5.67 | 16.23 | 25.02 | 0.00 | 86.4 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.19 | 13.65 | 21.13 | 2.00 | 74.3 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 7.99 | 24.62 | 39.61 | 18.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.66 | 13.13 | 22.68 | 2.00 | 73.4 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.7 | 3.15 | 9.40 | 15.85 | 2.00 | 66.7 | 70.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.3 | 2.86 | 8.29 | 13.85 | 8.00 | 61.2 | 86.0 |
| Bench 3 | Bench Boost | Harry Winks | MID | 11 | 4.5 | 0.89 | 2.84 | 5.22 | 0.00 | 17.7 | 0.0 |

## GW15

- Train rows: 142975
- Bank: 0.40 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Matheus Santos Carneiro Da Cunha
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 39.46
- Actual score: 32.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 4.9 | 0.00 | 7.84 | 13.58 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Killian Cahill | GK | 5 | 3.9 | 0.49 | 1.00 | 1.58 | 0.00 | 5.0 | 0.0 |
| Bench 2 | Bench | Virgil van Dijk | DEF | 12 | 6.3 | 0.00 | 9.82 | 16.68 | 0.00 | 0.0 | 0.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 2.86 | 9.14 | 15.02 | 1.00 | 83.6 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 2.66 | 7.70 | 12.64 | 1.00 | 78.7 | 82.0 |
| XI | XI | Wout Faes | DEF | 11 | 4.1 | 1.85 | 5.43 | 9.34 | 1.00 | 62.3 | 9.0 |
| Bench 3 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.00 | 0.88 | 2.27 | 0.00 | 14.3 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.0 | 6.49 | 19.34 | 33.04 | 7.00 | 90.0 | 90.0 |
| Vice Captain | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.61 | 13.10 | 21.07 | 1.00 | 81.5 | 90.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 8.1 | 2.71 | 9.01 | 14.76 | 2.00 | 31.3 | 75.0 |
| Bench 4 | Bench | Mohamed Salah | MID | 12 | 13.1 | 0.00 | 23.55 | 39.33 | 0.00 | 0.0 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.52 | 14.29 | 24.07 | 9.00 | 87.0 | 75.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.3 | 4.16 | 11.17 | 17.97 | 2.00 | 75.6 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.6 | 2.42 | 8.23 | 13.66 | 1.00 | 57.6 | 59.0 |
| XI | Bench | Harry Winks | MID | 11 | 4.5 | 0.20 | 1.18 | 2.59 | 0.00 | 5.3 | 0.0 |