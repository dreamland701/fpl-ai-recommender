# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 214.89
- Total actual points: 242.00
- Average predicted points: 53.72
- Average actual points: 60.50
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
- Predicted score: 60.59
- Actual score: 66.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 5.1 | 3.39 | 9.15 | 14.97 | 3.00 | 84.5 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.18 | 0.77 | 1.20 | 0.00 | 7.6 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.12 | 11.10 | 18.03 | 1.00 | 82.7 | 90.0 |
| XI | XI | Noussair Mazraoui | DEF | 14 | 4.6 | 3.75 | 10.21 | 15.92 | 2.00 | 83.8 | 90.0 |
| XI | XI | Ashley Young | DEF | 8 | 4.5 | 3.29 | 9.25 | 15.10 | 9.00 | 83.8 | 90.0 |
| Bench 4 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 2.26 | 7.06 | 11.61 | 0.00 | 81.6 | 0.0 |
| Bench 3 | Bench | Dara O'Shea | DEF | 10 | 4.0 | 2.49 | 6.70 | 10.86 | 2.00 | 79.8 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 15.2 | 7.44 | 20.51 | 34.40 | 2.00 | 82.7 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 5.46 | 14.87 | 23.35 | 2.00 | 84.1 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.8 | 4.24 | 12.51 | 20.83 | 16.00 | 82.1 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 7.44 | 20.74 | 34.16 | 13.00 | 82.7 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 5.50 | 14.91 | 24.09 | 2.00 | 82.7 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 4.70 | 12.49 | 20.19 | 1.00 | 83.3 | 58.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.4 | 3.81 | 10.96 | 17.45 | 2.00 | 79.0 | 81.0 |
| Bench 2 | Bench | Harry Winks | MID | 11 | 4.5 | 3.18 | 9.10 | 14.30 | 1.00 | 80.4 | 10.0 |

## GW13

- Train rows: 141592
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 61.36
- Actual score: 69.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.66) beats the best remaining Triple Captain opportunity (8.35).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.66) beats the best remaining Triple Captain opportunity (8.35).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 5.1 | 3.02 | 8.86 | 14.50 | 6.00 | 83.6 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.53 | 0.94 | 1.42 | 0.00 | 7.1 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.83 | 11.30 | 18.07 | 6.00 | 84.0 | 90.0 |
| XI | XI | Ashley Young | DEF | 8 | 4.5 | 3.05 | 9.00 | 14.96 | -1.00 | 81.1 | 72.0 |
| XI | XI | Noussair Mazraoui | DEF | 14 | 4.6 | 2.86 | 8.66 | 13.56 | 1.00 | 75.6 | 55.0 |
| Bench 2 | Bench | Dara O'Shea | DEF | 10 | 4.0 | 2.18 | 6.77 | 10.85 | 1.00 | 81.3 | 90.0 |
| Bench 4 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.76 | 3.15 | 5.85 | 0.00 | 34.8 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 15.1 | 5.79 | 18.05 | 31.13 | 2.00 | 81.3 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 5.52 | 15.98 | 24.98 | 2.00 | 82.7 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 4.11 | 13.15 | 21.18 | 1.00 | 65.6 | 21.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 7.66 | 22.75 | 36.38 | 13.00 | 82.7 | 83.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.89 | 13.33 | 21.68 | 9.00 | 76.0 | 65.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.4 | 3.18 | 9.76 | 16.27 | 2.00 | 72.4 | 65.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 3.12 | 9.72 | 16.30 | 2.00 | 63.9 | 85.0 |
| Bench 3 | Bench | Harry Winks | MID | 11 | 4.5 | 1.30 | 4.77 | 8.44 | 0.00 | 31.9 | 0.0 |

## GW14

- Train rows: 142282
- Bank: 0.00 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 55.10
- Actual score: 75.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (3.71) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Alexander Isak -> Nicolas Jackson (projected gain 7.15, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (3.71) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 5.1 | 2.19 | 7.19 | 12.50 | 2.00 | 79.0 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.18 | 0.66 | 1.14 | 0.00 | 7.6 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.73 | 11.12 | 18.35 | 1.00 | 82.7 | 90.0 |
| XI | XI | Ashley Young | DEF | 8 | 4.5 | 2.75 | 7.80 | 13.03 | 15.00 | 74.6 | 90.0 |
| Bench 2 | Bench Boost | Noussair Mazraoui | DEF | 14 | 4.6 | 2.24 | 7.61 | 12.94 | 1.00 | 68.1 | 90.0 |
| XI | XI | Dara O'Shea | DEF | 10 | 4.0 | 2.41 | 6.83 | 10.92 | 1.00 | 80.5 | 90.0 |
| Bench 4 | Bench Boost | Jan Bednarek | DEF | 17 | 4.0 | 0.40 | 1.90 | 3.81 | 0.00 | 23.8 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 15.0 | 6.13 | 18.82 | 32.12 | 5.00 | 80.2 | 90.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 8.1 | 5.17 | 14.71 | 22.95 | 0.00 | 80.0 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.23 | 13.76 | 21.16 | 2.00 | 77.5 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 7.42 | 22.78 | 36.90 | 18.00 | 82.7 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.65 | 13.03 | 22.31 | 2.00 | 75.2 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.7 | 3.30 | 9.81 | 16.63 | 2.00 | 71.4 | 70.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.3 | 2.98 | 8.60 | 14.44 | 8.00 | 65.4 | 86.0 |
| Bench 3 | Bench Boost | Harry Winks | MID | 11 | 4.5 | 0.89 | 2.96 | 5.53 | 0.00 | 17.9 | 0.0 |

## GW15

- Train rows: 142975
- Bank: 0.40 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Matheus Santos Carneiro Da Cunha
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 37.84
- Actual score: 32.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 5.1 | 2.57 | 7.53 | 12.75 | 1.00 | 80.4 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.39 | 0.74 | 1.21 | 0.00 | 6.4 | 0.0 |
| Bench 2 | Bench | Virgil van Dijk | DEF | 12 | 6.3 | 0.00 | 8.24 | 14.47 | 0.00 | 0.0 | 0.0 |
| XI | XI | Noussair Mazraoui | DEF | 14 | 4.6 | 2.74 | 8.06 | 12.77 | 1.00 | 74.1 | 24.0 |
| XI | XI | Dara O'Shea | DEF | 10 | 4.0 | 2.27 | 6.54 | 10.53 | 1.00 | 78.9 | 90.0 |
| XI | Bench | Ashley Young | DEF | 8 | 4.5 | 0.00 | 5.49 | 10.55 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.00 | 0.75 | 2.09 | 0.00 | 12.5 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.0 | 5.89 | 17.43 | 30.25 | 7.00 | 82.6 | 90.0 |
| Vice Captain | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.75 | 13.38 | 21.51 | 1.00 | 81.6 | 90.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 8.1 | 2.69 | 9.03 | 14.88 | 2.00 | 31.3 | 75.0 |
| Bench 4 | Bench | Mohamed Salah | MID | 12 | 13.1 | 0.00 | 21.77 | 36.75 | 0.00 | 0.0 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.00 | 12.68 | 21.84 | 9.00 | 79.6 | 75.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.3 | 4.20 | 11.27 | 17.97 | 2.00 | 77.7 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.6 | 2.65 | 8.90 | 14.79 | 1.00 | 62.9 | 59.0 |
| XI | Bench | Harry Winks | MID | 11 | 4.5 | 0.20 | 1.28 | 2.85 | 0.00 | 5.1 | 0.0 |