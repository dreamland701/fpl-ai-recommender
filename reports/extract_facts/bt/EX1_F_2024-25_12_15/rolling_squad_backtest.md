# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 224.65
- Total actual points: 217.00
- Average predicted points: 56.16
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
| XI | XI | Jordan Pickford | GK | 8 | 4.9 | 3.30 | 9.36 | 15.33 | 6.00 | 88.9 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.22 | 0.82 | 1.24 | 0.00 | 8.2 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.61 | 12.64 | 20.20 | 1.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.80 | 10.35 | 16.82 | 0.00 | 87.6 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 3.55 | 10.02 | 16.01 | 1.00 | 88.1 | 90.0 |
| Bench 3 | Bench | Wout Faes | DEF | 11 | 4.2 | 2.66 | 7.87 | 12.78 | 0.00 | 81.2 | 90.0 |
| Bench 4 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 2.22 | 7.10 | 11.72 | 0.00 | 83.3 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.2 | 8.01 | 22.24 | 36.72 | 2.00 | 90.0 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 5.36 | 14.79 | 23.23 | 2.00 | 84.7 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.8 | 4.18 | 12.52 | 20.88 | 16.00 | 83.5 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.0 | 7.91 | 22.24 | 36.21 | 13.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 5.95 | 16.36 | 26.07 | 2.00 | 90.0 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 4.63 | 12.49 | 20.22 | 1.00 | 84.5 | 58.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.4 | 3.81 | 11.02 | 17.69 | 2.00 | 77.1 | 81.0 |
| Bench 2 | Bench | Harry Winks | MID | 11 | 4.5 | 3.18 | 9.16 | 14.58 | 1.00 | 78.7 | 10.0 |

## GW13

- Train rows: 141592
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Matheus Santos Carneiro Da Cunha
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 62.78
- Actual score: 67.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.16) beats the best remaining Triple Captain opportunity (8.89).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.16) beats the best remaining Triple Captain opportunity (8.89).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 4.9 | 2.93 | 9.00 | 14.97 | 0.00 | 88.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.57 | 1.02 | 1.48 | 0.00 | 7.9 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.77 | 11.30 | 18.12 | 6.00 | 85.3 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.08 | 9.26 | 15.14 | 2.00 | 80.3 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 2.72 | 8.54 | 13.71 | 2.00 | 73.3 | 90.0 |
| Bench 2 | Bench | Wout Faes | DEF | 11 | 4.1 | 2.46 | 7.23 | 11.96 | 0.00 | 79.8 | 90.0 |
| Bench 4 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.84 | 3.31 | 6.02 | 0.00 | 36.4 | 0.0 |
| XI | XI | Erling Haaland | FWD | 13 | 15.1 | 5.90 | 18.37 | 31.69 | 2.00 | 81.5 | 90.0 |
| Vice Captain | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 5.96 | 17.42 | 26.96 | 2.00 | 90.0 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 4.04 | 12.99 | 20.80 | 1.00 | 61.8 | 21.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 8.16 | 24.35 | 38.51 | 13.00 | 90.0 | 83.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.81 | 13.15 | 21.30 | 9.00 | 72.2 | 65.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.4 | 3.11 | 9.59 | 15.90 | 2.00 | 68.8 | 65.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 2.98 | 9.36 | 15.68 | 2.00 | 60.0 | 85.0 |
| Bench 3 | Bench | Harry Winks | MID | 11 | 4.5 | 1.40 | 4.97 | 8.65 | 0.00 | 33.7 | 0.0 |

## GW14

- Train rows: 142282
- Bank: 0.00 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 59.04
- Actual score: 70.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (4.20) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Alexander Isak -> Nicolas Jackson (projected gain 7.99, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (4.20) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 4.9 | 3.04 | 8.77 | 14.60 | 6.00 | 86.1 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.22 | 0.72 | 1.19 | 0.00 | 8.3 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.23 | 12.68 | 20.51 | 1.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.32 | 9.43 | 15.33 | 6.00 | 82.7 | 90.0 |
| Bench 2 | Bench Boost | Lewis Hall | DEF | 15 | 4.4 | 2.52 | 8.17 | 13.46 | 1.00 | 77.8 | 90.0 |
| XI | XI | Wout Faes | DEF | 11 | 4.1 | 2.61 | 6.93 | 11.23 | 1.00 | 80.5 | 30.0 |
| Bench 4 | Bench Boost | Jan Bednarek | DEF | 17 | 4.0 | 0.47 | 2.05 | 3.96 | 0.00 | 25.1 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 15.0 | 6.17 | 19.06 | 32.41 | 5.00 | 83.3 | 90.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 8.1 | 5.62 | 16.16 | 24.93 | 0.00 | 86.2 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.22 | 13.80 | 21.37 | 2.00 | 75.5 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 7.90 | 24.30 | 38.92 | 18.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.68 | 13.14 | 22.64 | 2.00 | 73.9 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.7 | 3.25 | 9.70 | 16.34 | 2.00 | 68.2 | 70.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.3 | 2.91 | 8.42 | 14.06 | 8.00 | 61.6 | 86.0 |
| Bench 3 | Bench Boost | Harry Winks | MID | 11 | 4.5 | 1.00 | 3.17 | 5.75 | 0.00 | 19.8 | 0.0 |

## GW15

- Train rows: 142975
- Bank: 0.40 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Matheus Santos Carneiro Da Cunha
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 39.71
- Actual score: 32.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 4.9 | 0.00 | 7.83 | 13.57 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Killian Cahill | GK | 5 | 3.9 | 0.43 | 0.81 | 1.26 | 0.00 | 7.2 | 0.0 |
| Bench 2 | Bench | Virgil van Dijk | DEF | 12 | 6.3 | 0.00 | 9.84 | 16.66 | 0.00 | 0.0 | 0.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 2.88 | 9.21 | 15.10 | 1.00 | 83.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 2.65 | 7.66 | 12.54 | 1.00 | 77.5 | 82.0 |
| XI | XI | Wout Faes | DEF | 11 | 4.1 | 1.86 | 5.44 | 9.30 | 1.00 | 61.0 | 9.0 |
| Bench 3 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.00 | 0.87 | 2.22 | 0.00 | 13.7 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.0 | 6.45 | 19.14 | 32.53 | 7.00 | 90.0 | 90.0 |
| Vice Captain | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.69 | 13.41 | 21.58 | 1.00 | 83.0 | 90.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 8.1 | 2.77 | 9.19 | 15.03 | 2.00 | 32.7 | 75.0 |
| Bench 4 | Bench | Mohamed Salah | MID | 12 | 13.1 | 0.00 | 23.37 | 38.85 | 0.00 | 0.0 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.53 | 14.30 | 24.02 | 9.00 | 87.3 | 75.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.3 | 4.19 | 11.30 | 18.17 | 2.00 | 75.9 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.6 | 2.52 | 8.52 | 14.15 | 1.00 | 59.2 | 59.0 |
| XI | Bench | Harry Winks | MID | 11 | 4.5 | 0.29 | 1.46 | 3.05 | 0.00 | 6.8 | 0.0 |