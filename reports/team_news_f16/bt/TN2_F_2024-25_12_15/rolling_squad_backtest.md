# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 227.86
- Total actual points: 219.00
- Average predicted points: 56.97
- Average actual points: 54.75
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
- Predicted score: 63.65
- Actual score: 48.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 4.9 | 3.35 | 9.40 | 15.33 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.36 | 1.05 | 1.48 | 0.00 | 12.4 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.67 | 12.74 | 20.31 | 1.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.85 | 10.43 | 16.88 | 0.00 | 88.8 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 3.60 | 10.10 | 16.10 | 1.00 | 89.1 | 90.0 |
| Bench 3 | Bench | Wout Faes | DEF | 11 | 4.2 | 2.70 | 7.90 | 12.78 | 0.00 | 82.4 | 90.0 |
| Bench 4 | Bench | Dara O'Shea | DEF | 10 | 4.0 | 2.48 | 6.79 | 11.00 | 2.00 | 82.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.2 | 8.01 | 22.15 | 36.63 | 2.00 | 90.0 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 5.42 | 14.88 | 23.39 | 2.00 | 85.6 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.8 | 4.22 | 12.58 | 20.93 | 16.00 | 84.7 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.0 | 7.96 | 22.33 | 36.37 | 13.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 6.03 | 16.51 | 26.32 | 2.00 | 90.0 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 4.68 | 12.55 | 20.30 | 1.00 | 85.7 | 58.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.4 | 3.86 | 11.08 | 17.74 | 2.00 | 78.5 | 81.0 |
| Bench 2 | Bench | Harry Winks | MID | 11 | 4.5 | 3.20 | 9.18 | 14.57 | 1.00 | 79.3 | 10.0 |

## GW13

- Train rows: 141592
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Matheus Santos Carneiro Da Cunha
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 63.15
- Actual score: 67.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.18) beats the best remaining Triple Captain opportunity (8.92).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.18) beats the best remaining Triple Captain opportunity (8.92).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 4.9 | 2.97 | 9.03 | 14.96 | 0.00 | 89.1 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.70 | 1.21 | 1.67 | 0.00 | 11.7 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.81 | 11.35 | 18.14 | 6.00 | 86.4 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.11 | 9.28 | 15.11 | 2.00 | 81.3 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 2.75 | 8.57 | 13.71 | 2.00 | 74.5 | 90.0 |
| Bench 2 | Bench | Wout Faes | DEF | 11 | 4.1 | 2.51 | 7.29 | 11.99 | 0.00 | 81.2 | 90.0 |
| Bench 3 | Bench | Dara O'Shea | DEF | 10 | 4.0 | 2.23 | 6.91 | 11.16 | 1.00 | 81.0 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 15.1 | 5.85 | 18.19 | 31.42 | 2.00 | 81.0 | 90.0 |
| Vice Captain | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 6.04 | 17.57 | 27.20 | 2.00 | 90.0 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 4.05 | 12.98 | 20.78 | 1.00 | 62.5 | 21.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 8.18 | 24.34 | 38.57 | 13.00 | 90.0 | 83.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.84 | 13.15 | 21.27 | 9.00 | 73.1 | 65.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.4 | 3.16 | 9.62 | 15.91 | 2.00 | 70.1 | 65.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 3.02 | 9.34 | 15.57 | 2.00 | 61.5 | 85.0 |
| Bench 4 | Bench | Harry Winks | MID | 11 | 4.5 | 0.69 | 4.34 | 8.47 | 0.00 | 16.5 | 0.0 |

## GW14

- Train rows: 142282
- Bank: 0.00 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 59.78
- Actual score: 71.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.94) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Alexander Isak -> Nicolas Jackson (projected gain 8.16, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.94) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 4.9 | 2.95 | 8.64 | 14.53 | 6.00 | 84.4 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.23 | 0.75 | 1.32 | 0.00 | 9.4 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.15 | 12.58 | 20.51 | 1.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.23 | 9.29 | 15.27 | 6.00 | 80.8 | 90.0 |
| Bench 2 | Bench Boost | Lewis Hall | DEF | 15 | 4.4 | 2.43 | 8.04 | 13.41 | 1.00 | 76.1 | 90.0 |
| XI | XI | Wout Faes | DEF | 11 | 4.1 | 2.52 | 6.81 | 11.18 | 1.00 | 78.8 | 30.0 |
| Bench 3 | Bench Boost | Dara O'Shea | DEF | 10 | 4.0 | 2.34 | 6.77 | 11.14 | 1.00 | 77.5 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 15.0 | 6.02 | 18.74 | 32.14 | 5.00 | 80.3 | 90.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 8.1 | 5.59 | 16.15 | 25.09 | 0.00 | 85.4 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.14 | 13.67 | 21.34 | 2.00 | 74.0 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 7.81 | 24.17 | 38.97 | 18.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.59 | 12.98 | 22.56 | 2.00 | 72.4 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.7 | 3.17 | 9.54 | 16.23 | 2.00 | 66.8 | 70.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.3 | 2.85 | 8.33 | 14.04 | 8.00 | 60.7 | 86.0 |
| Bench 4 | Bench Boost | Harry Winks | MID | 11 | 4.5 | 0.95 | 3.06 | 5.68 | 0.00 | 19.1 | 0.0 |

## GW15

- Train rows: 142975
- Bank: 0.40 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Matheus Santos Carneiro Da Cunha
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 41.29
- Actual score: 33.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 4.9 | 0.00 | 7.85 | 13.47 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Killian Cahill | GK | 5 | 3.9 | 0.56 | 1.02 | 1.45 | 0.00 | 11.1 | 0.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 12 | 6.3 | 0.00 | 9.86 | 16.58 | 0.00 | 0.0 | 0.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 2.91 | 9.24 | 15.10 | 1.00 | 84.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 2.69 | 7.72 | 12.58 | 1.00 | 78.5 | 82.0 |
| XI | XI | Dara O'Shea | DEF | 10 | 4.0 | 2.32 | 6.64 | 10.80 | 1.00 | 78.6 | 90.0 |
| XI | XI | Wout Faes | DEF | 11 | 4.1 | 1.10 | 4.57 | 8.37 | 1.00 | 35.8 | 9.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.0 | 6.45 | 19.08 | 32.46 | 7.00 | 90.0 | 90.0 |
| Vice Captain | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.73 | 13.43 | 21.58 | 1.00 | 84.3 | 90.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 8.1 | 2.84 | 9.24 | 15.02 | 2.00 | 35.1 | 75.0 |
| Bench 4 | Bench | Mohamed Salah | MID | 12 | 13.1 | 0.00 | 23.33 | 38.78 | 0.00 | 0.0 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.43 | 14.15 | 23.99 | 9.00 | 85.1 | 75.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.3 | 4.25 | 11.37 | 18.25 | 2.00 | 77.4 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.6 | 2.56 | 8.54 | 14.11 | 1.00 | 60.7 | 59.0 |
| Bench 2 | Bench | Harry Winks | MID | 11 | 4.5 | 0.11 | 1.49 | 3.46 | 0.00 | 2.5 | 0.0 |