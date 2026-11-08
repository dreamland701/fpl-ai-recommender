# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 238.44
- Total actual points: 273.00
- Average predicted points: 59.61
- Average actual points: 68.25
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
- Predicted score: 57.27
- Actual score: 42.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 5.1 | 3.49 | 9.23 | 15.18 | 3.00 | 83.8 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 4.9 | 3.07 | 9.22 | 15.19 | 6.00 | 86.6 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.3 | 4.24 | 12.39 | 20.33 | 0.00 | 86.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 3.96 | 11.25 | 18.43 | 1.00 | 87.0 | 90.0 |
| Bench 2 | Bench | Pedro Porro | DEF | 18 | 5.5 | 3.48 | 10.61 | 17.53 | 14.00 | 83.1 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.66 | 10.17 | 16.63 | 0.00 | 85.3 | 90.0 |
| XI | XI | Noussair Mazraoui | DEF | 14 | 4.5 | 3.59 | 9.94 | 15.81 | 2.00 | 79.9 | 90.0 |
| Bench 3 | Bench | Danny Welbeck | FWD | 5 | 5.9 | 3.46 | 11.29 | 18.40 | 2.00 | 73.2 | 85.0 |
| XI | XI | Raúl Jiménez | FWD | 9 | 5.8 | 3.76 | 10.50 | 17.51 | 2.00 | 65.7 | 70.0 |
| Bench 4 | Bench | Iliman Ndiaye | FWD | 8 | 5.4 | 2.77 | 7.87 | 12.79 | 2.00 | 70.9 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 12.8 | 6.68 | 19.25 | 31.87 | 13.00 | 93.8 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.0 | 6.02 | 17.69 | 29.72 | 2.00 | 87.9 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 5.90 | 16.32 | 25.90 | 2.00 | 87.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.06 | 15.46 | 25.56 | 3.00 | 93.6 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.7 | 4.24 | 11.63 | 19.19 | 1.00 | 78.9 | 58.0 |

## GW13

- Train rows: 141592
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 63.10
- Actual score: 85.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.44) beats the best remaining Triple Captain opportunity (8.53).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.44) beats the best remaining Triple Captain opportunity (8.53).
- Autosub outfielders: Noussair Mazraoui.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 4.9 | 2.92 | 9.05 | 15.08 | 0.00 | 85.1 | 90.0 |
| XI | XI | André Onana | GK | 14 | 5.1 | 3.01 | 8.83 | 14.53 | 6.00 | 82.6 | 90.0 |
| XI | Bench | Joško Gvardiol | DEF | 13 | 6.3 | 3.83 | 12.49 | 20.87 | 0.00 | 88.0 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 3.96 | 11.62 | 19.39 | 2.00 | 87.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.63 | 11.13 | 18.02 | 6.00 | 82.9 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.23 | 9.67 | 15.94 | 2.00 | 81.7 | 90.0 |
| Bench 2 | Autosub In | Noussair Mazraoui | DEF | 14 | 4.6 | 3.11 | 8.88 | 14.17 | 1.00 | 75.4 | 55.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 6.0 | 3.92 | 11.01 | 17.85 | 2.00 | 73.2 | 78.0 |
| Bench 4 | Bench | Raúl Jiménez | FWD | 9 | 5.8 | 2.97 | 9.36 | 15.45 | 2.00 | 60.5 | 77.0 |
| Bench 3 | Bench | Iliman Ndiaye | FWD | 8 | 5.4 | 3.01 | 8.42 | 13.84 | 2.00 | 71.2 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 7.44 | 23.08 | 37.04 | 13.00 | 99.5 | 83.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.27 | 18.12 | 29.72 | 14.00 | 89.2 | 85.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 4.93 | 14.45 | 24.27 | 2.00 | 85.8 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.56 | 13.75 | 22.26 | 9.00 | 75.7 | 65.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 3.42 | 10.44 | 17.41 | 2.00 | 65.7 | 85.0 |

## GW14

- Train rows: 142282
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 63.94
- Actual score: 76.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.42) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Raúl Jiménez -> Jørgen Strand Larsen (projected gain 2.27, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.42) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 4.9 | 2.88 | 8.66 | 14.62 | 6.00 | 82.7 | 90.0 |
| Bench 1 | Bench Boost | André Onana | GK | 14 | 5.1 | 2.56 | 8.58 | 14.36 | 2.00 | 84.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.80 | 11.81 | 19.51 | 1.00 | 87.6 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 3.86 | 11.79 | 19.28 | 1.00 | 84.5 | 28.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.24 | 9.44 | 15.60 | 6.00 | 81.1 | 90.0 |
| Bench 3 | Bench Boost | Joško Gvardiol | DEF | 13 | 6.3 | 2.66 | 9.01 | 15.81 | 6.00 | 48.8 | 90.0 |
| Bench 4 | Bench Boost | Noussair Mazraoui | DEF | 14 | 4.6 | 2.10 | 7.25 | 12.40 | 1.00 | 62.9 | 90.0 |
| XI | XI | Jørgen Strand Larsen | FWD | 20 | 5.6 | 3.65 | 10.68 | 17.31 | 2.00 | 78.3 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 6.0 | 3.20 | 10.13 | 16.86 | 0.00 | 68.9 | 0.0 |
| Bench 2 | Bench Boost | Iliman Ndiaye | FWD | 8 | 5.4 | 3.11 | 8.42 | 13.76 | 2.00 | 74.6 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 7.36 | 22.66 | 36.83 | 18.00 | 103.8 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.70 | 19.26 | 31.40 | 7.00 | 94.7 | 78.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 4.58 | 13.66 | 23.23 | 2.00 | 87.6 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 3.54 | 12.85 | 22.13 | 2.00 | 72.1 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 3.34 | 10.32 | 17.50 | 2.00 | 69.4 | 70.0 |

## GW15

- Train rows: 142975
- Bank: 0.10 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 54.13
- Actual score: 70.00
- Transfer: Emile Smith Rowe -> Justin Kluivert (projected gain 2.58, hit 0)
- Autosub outfielders: Noussair Mazraoui, Danny Welbeck.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 5.2 | 2.92 | 8.70 | 14.34 | 1.00 | 84.1 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 4.9 | 2.30 | 8.04 | 13.93 | 0.00 | 64.1 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 3.72 | 11.17 | 18.95 | 1.00 | 74.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 3.26 | 9.98 | 17.06 | 3.00 | 69.6 | 90.0 |
| XI | Bench | Virgil van Dijk | DEF | 12 | 6.4 | 2.89 | 9.92 | 16.88 | 0.00 | 65.4 | 0.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 2.94 | 9.59 | 15.89 | 1.00 | 84.2 | 90.0 |
| Bench 2 | Autosub In | Noussair Mazraoui | DEF | 14 | 4.7 | 2.65 | 7.80 | 12.73 | 1.00 | 69.7 | 24.0 |
| XI | XI | Jørgen Strand Larsen | FWD | 20 | 5.6 | 4.24 | 11.53 | 18.64 | 2.00 | 78.5 | 61.0 |
| Bench 3 | Autosub In | Danny Welbeck | FWD | 5 | 5.9 | 2.43 | 7.43 | 12.99 | 1.00 | 39.4 | 20.0 |
| Bench 4 | Bench | Iliman Ndiaye | FWD | 8 | 5.4 | 1.99 | 6.82 | 11.74 | 0.00 | 52.0 | 0.0 |
| Captain | Bench | Mohamed Salah | MID | 12 | 13.2 | 7.65 | 23.84 | 39.64 | 0.00 | 93.3 | 0.0 |
| Vice Captain | Captain | Cole Palmer | MID | 6 | 11.0 | 6.50 | 18.35 | 29.91 | 18.00 | 89.6 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.06 | 13.66 | 23.02 | 9.00 | 78.1 | 75.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.4 | 4.56 | 12.13 | 19.47 | 2.00 | 63.2 | 62.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.8 | 3.73 | 11.90 | 20.75 | 13.00 | 76.1 | 90.0 |