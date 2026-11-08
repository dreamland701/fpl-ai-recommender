# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 227.37
- Total actual points: 230.00
- Average predicted points: 56.84
- Average actual points: 57.50
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
- Predicted score: 63.18
- Actual score: 59.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 4.9 | 3.28 | 9.30 | 15.26 | 6.00 | 88.5 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.23 | 0.85 | 1.28 | 0.00 | 8.4 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.63 | 12.69 | 20.29 | 1.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.80 | 10.36 | 16.84 | 0.00 | 87.6 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 3.57 | 10.06 | 16.08 | 1.00 | 88.4 | 90.0 |
| Bench 3 | Bench | Wout Faes | DEF | 11 | 4.2 | 2.63 | 7.81 | 12.72 | 0.00 | 80.8 | 90.0 |
| Bench 4 | Bench | Dara O'Shea | DEF | 10 | 4.0 | 2.43 | 6.72 | 10.95 | 2.00 | 81.1 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 15.2 | 7.95 | 22.10 | 36.66 | 2.00 | 90.0 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 5.40 | 14.89 | 23.44 | 2.00 | 85.4 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.8 | 4.18 | 12.52 | 20.91 | 16.00 | 83.5 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 7.95 | 22.33 | 36.42 | 13.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 6.02 | 16.50 | 26.35 | 2.00 | 90.0 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 4.64 | 12.50 | 20.27 | 1.00 | 84.6 | 58.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.4 | 3.80 | 10.99 | 17.69 | 2.00 | 77.0 | 81.0 |
| Bench 2 | Bench | Harry Winks | MID | 11 | 4.5 | 3.17 | 9.13 | 14.55 | 1.00 | 78.5 | 10.0 |

## GW13

- Train rows: 141592
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Matheus Santos Carneiro Da Cunha
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 62.60
- Actual score: 67.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.17) beats the best remaining Triple Captain opportunity (8.91).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.17) beats the best remaining Triple Captain opportunity (8.91).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 4.9 | 2.91 | 8.94 | 14.90 | 0.00 | 87.6 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.57 | 1.02 | 1.50 | 0.00 | 7.9 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.76 | 11.28 | 18.10 | 6.00 | 85.2 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.06 | 9.22 | 15.08 | 2.00 | 80.1 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 2.69 | 8.49 | 13.67 | 2.00 | 72.9 | 90.0 |
| Bench 2 | Bench | Wout Faes | DEF | 11 | 4.1 | 2.45 | 7.20 | 11.92 | 0.00 | 79.5 | 90.0 |
| Bench 3 | Bench | Dara O'Shea | DEF | 10 | 4.0 | 2.18 | 6.83 | 11.11 | 1.00 | 79.5 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 15.1 | 5.79 | 18.11 | 31.40 | 2.00 | 79.5 | 90.0 |
| Vice Captain | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 6.03 | 17.57 | 27.22 | 2.00 | 90.0 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 4.01 | 12.93 | 20.76 | 1.00 | 61.5 | 21.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 8.17 | 24.35 | 38.63 | 13.00 | 90.0 | 83.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.79 | 13.10 | 21.26 | 9.00 | 71.9 | 65.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.4 | 3.09 | 9.53 | 15.85 | 2.00 | 68.4 | 65.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 2.93 | 9.23 | 15.50 | 2.00 | 59.2 | 85.0 |
| Bench 4 | Bench | Harry Winks | MID | 11 | 4.5 | 0.74 | 4.12 | 7.75 | 0.00 | 18.0 | 0.0 |

## GW14

- Train rows: 142282
- Bank: 0.00 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 60.80
- Actual score: 71.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.06) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Alexander Isak -> Nicolas Jackson (projected gain 8.20, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.06) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 4.9 | 3.02 | 8.73 | 14.54 | 6.00 | 85.8 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.23 | 0.74 | 1.22 | 0.00 | 8.4 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.24 | 12.70 | 20.55 | 1.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.30 | 9.39 | 15.30 | 6.00 | 82.4 | 90.0 |
| Bench 2 | Bench Boost | Lewis Hall | DEF | 15 | 4.4 | 2.50 | 8.14 | 13.43 | 1.00 | 77.5 | 90.0 |
| XI | XI | Wout Faes | DEF | 11 | 4.1 | 2.60 | 6.91 | 11.20 | 1.00 | 80.3 | 30.0 |
| Bench 3 | Bench Boost | Dara O'Shea | DEF | 10 | 4.0 | 2.40 | 6.86 | 11.15 | 1.00 | 78.7 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 15.0 | 6.07 | 18.81 | 32.16 | 5.00 | 81.4 | 90.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 8.1 | 5.68 | 16.29 | 25.14 | 0.00 | 87.3 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.22 | 13.79 | 21.40 | 2.00 | 75.7 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 7.93 | 24.36 | 39.10 | 18.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.64 | 13.06 | 22.55 | 2.00 | 73.3 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.7 | 3.20 | 9.59 | 16.20 | 2.00 | 67.4 | 70.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.3 | 2.89 | 8.38 | 14.01 | 8.00 | 61.3 | 86.0 |
| Bench 4 | Bench Boost | Harry Winks | MID | 11 | 4.5 | 0.94 | 3.04 | 5.60 | 0.00 | 18.7 | 0.0 |

## GW15

- Train rows: 142975
- Bank: 0.40 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Matheus Santos Carneiro Da Cunha
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 40.80
- Actual score: 33.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 4.9 | 0.00 | 7.79 | 13.52 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Killian Cahill | GK | 5 | 3.9 | 0.44 | 0.82 | 1.28 | 0.00 | 7.3 | 0.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 12 | 6.3 | 0.00 | 9.81 | 16.64 | 0.00 | 0.0 | 0.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 2.86 | 9.17 | 15.05 | 1.00 | 82.7 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 2.65 | 7.65 | 12.54 | 1.00 | 77.5 | 82.0 |
| XI | XI | Dara O'Shea | DEF | 10 | 4.0 | 2.27 | 6.57 | 10.76 | 1.00 | 77.1 | 90.0 |
| XI | XI | Wout Faes | DEF | 11 | 4.1 | 1.20 | 4.78 | 8.63 | 1.00 | 39.5 | 9.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.0 | 6.40 | 19.01 | 32.42 | 7.00 | 90.0 | 90.0 |
| Vice Captain | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.67 | 13.36 | 21.55 | 1.00 | 82.8 | 90.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 8.1 | 2.73 | 9.11 | 14.95 | 2.00 | 32.2 | 75.0 |
| Bench 4 | Bench | Mohamed Salah | MID | 12 | 13.1 | 0.00 | 23.34 | 38.92 | 0.00 | 0.0 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.51 | 14.26 | 24.00 | 9.00 | 87.0 | 75.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.3 | 4.19 | 11.30 | 18.19 | 2.00 | 75.9 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.6 | 2.47 | 8.41 | 14.01 | 1.00 | 58.3 | 59.0 |
| Bench 2 | Bench | Harry Winks | MID | 11 | 4.5 | 0.14 | 1.16 | 2.66 | 0.00 | 3.3 | 0.0 |