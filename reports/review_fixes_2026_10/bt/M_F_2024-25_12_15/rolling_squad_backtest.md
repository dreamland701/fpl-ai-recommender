# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 238.19
- Total actual points: 273.00
- Average predicted points: 59.55
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
- Predicted score: 57.08
- Actual score: 42.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 4.9 | 3.10 | 9.27 | 15.27 | 6.00 | 86.5 | 90.0 |
| XI | XI | André Onana | GK | 14 | 5.1 | 3.49 | 9.15 | 15.09 | 3.00 | 83.8 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.3 | 4.21 | 12.36 | 20.42 | 0.00 | 86.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 3.94 | 11.20 | 18.43 | 1.00 | 87.0 | 90.0 |
| Bench 3 | Bench | Pedro Porro | DEF | 18 | 5.5 | 3.47 | 10.62 | 17.59 | 14.00 | 83.2 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.62 | 10.17 | 16.71 | 0.00 | 85.4 | 90.0 |
| XI | XI | Noussair Mazraoui | DEF | 14 | 4.5 | 3.59 | 9.97 | 15.84 | 2.00 | 79.9 | 90.0 |
| Bench 2 | Bench | Danny Welbeck | FWD | 5 | 5.9 | 3.49 | 11.32 | 18.36 | 2.00 | 73.2 | 85.0 |
| XI | XI | Raúl Jiménez | FWD | 9 | 5.8 | 3.72 | 10.39 | 17.37 | 2.00 | 65.7 | 70.0 |
| Bench 4 | Bench | Iliman Ndiaye | FWD | 8 | 5.4 | 2.79 | 7.89 | 12.81 | 2.00 | 70.8 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 12.8 | 6.66 | 19.17 | 31.81 | 13.00 | 93.8 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.0 | 6.01 | 17.69 | 29.63 | 2.00 | 87.9 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 5.91 | 16.42 | 25.87 | 2.00 | 86.9 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.07 | 15.42 | 25.59 | 3.00 | 93.6 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.7 | 4.20 | 11.64 | 19.23 | 1.00 | 78.9 | 58.0 |

## GW13

- Train rows: 141592
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 63.04
- Actual score: 85.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.44) beats the best remaining Triple Captain opportunity (8.58).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.44) beats the best remaining Triple Captain opportunity (8.58).
- Autosub: Noussair Mazraoui replaced Joško Gvardiol.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 4.9 | 2.91 | 9.02 | 15.09 | 0.00 | 85.1 | 90.0 |
| XI | XI | André Onana | GK | 14 | 5.1 | 3.02 | 8.85 | 14.65 | 6.00 | 82.6 | 90.0 |
| XI | Bench | Joško Gvardiol | DEF | 13 | 6.3 | 3.83 | 12.46 | 20.82 | 0.00 | 88.0 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 3.97 | 11.62 | 19.38 | 2.00 | 87.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 3.62 | 11.11 | 18.03 | 6.00 | 82.9 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.20 | 9.69 | 16.02 | 2.00 | 81.8 | 90.0 |
| Bench 2 | Autosub In | Noussair Mazraoui | DEF | 14 | 4.5 | 3.12 | 8.92 | 14.30 | 1.00 | 75.4 | 55.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.9 | 3.89 | 10.93 | 17.73 | 2.00 | 73.2 | 78.0 |
| Bench 4 | Bench | Raúl Jiménez | FWD | 9 | 5.8 | 2.94 | 9.29 | 15.31 | 2.00 | 60.6 | 77.0 |
| Bench 3 | Bench | Iliman Ndiaye | FWD | 8 | 5.4 | 2.99 | 8.41 | 13.83 | 2.00 | 71.2 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 12.9 | 7.44 | 23.01 | 36.91 | 13.00 | 99.6 | 83.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.31 | 18.13 | 29.79 | 14.00 | 89.1 | 85.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 4.93 | 14.43 | 24.23 | 2.00 | 85.8 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 4.57 | 13.69 | 22.17 | 9.00 | 75.6 | 65.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.7 | 3.39 | 10.43 | 17.37 | 2.00 | 65.7 | 85.0 |

## GW14

- Train rows: 142282
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 63.99
- Actual score: 76.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.43) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Raúl Jiménez -> Jørgen Strand Larsen (projected gain 2.28, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.43) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench Boost | André Onana | GK | 14 | 5.1 | 2.59 | 8.67 | 14.57 | 2.00 | 84.2 | 90.0 |
| XI | XI | Jordan Pickford | GK | 8 | 4.9 | 2.84 | 8.64 | 14.59 | 6.00 | 82.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 3.79 | 11.84 | 19.61 | 1.00 | 87.7 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 3.89 | 11.83 | 19.32 | 1.00 | 84.5 | 28.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.26 | 9.50 | 15.65 | 6.00 | 81.0 | 90.0 |
| Bench 3 | Bench Boost | Joško Gvardiol | DEF | 13 | 6.3 | 2.64 | 8.96 | 15.77 | 6.00 | 48.9 | 90.0 |
| Bench 4 | Bench Boost | Noussair Mazraoui | DEF | 14 | 4.5 | 2.13 | 7.33 | 12.52 | 1.00 | 62.8 | 90.0 |
| XI | XI | Jørgen Strand Larsen | FWD | 20 | 5.6 | 3.66 | 10.67 | 17.25 | 2.00 | 78.3 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.9 | 3.21 | 10.11 | 16.83 | 0.00 | 68.9 | 0.0 |
| Bench 2 | Bench Boost | Iliman Ndiaye | FWD | 8 | 5.4 | 3.07 | 8.39 | 13.73 | 2.00 | 74.7 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 12.9 | 7.34 | 22.55 | 36.69 | 18.00 | 103.9 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.68 | 19.19 | 31.37 | 7.00 | 94.7 | 78.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 4.61 | 13.66 | 23.22 | 2.00 | 87.6 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.58 | 12.82 | 22.05 | 2.00 | 72.0 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.7 | 3.36 | 10.33 | 17.40 | 2.00 | 69.4 | 70.0 |

## GW15

- Train rows: 142975
- Bank: 0.10 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 54.08
- Actual score: 70.00
- Transfer: Emile Smith Rowe -> Justin Kluivert (projected gain 2.42, hit 0)
- Autosub: Noussair Mazraoui replaced Virgil van Dijk.
- Autosub: Danny Welbeck replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 5.1 | 2.90 | 8.72 | 14.38 | 1.00 | 84.2 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 4.9 | 2.30 | 8.06 | 13.99 | 0.00 | 64.1 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 3.73 | 11.17 | 19.14 | 1.00 | 74.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 3.28 | 10.03 | 17.15 | 3.00 | 69.6 | 90.0 |
| XI | Bench | Virgil van Dijk | DEF | 12 | 6.3 | 2.89 | 9.96 | 16.94 | 0.00 | 65.4 | 0.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 2.98 | 9.66 | 15.93 | 1.00 | 84.1 | 90.0 |
| Bench 2 | Autosub In | Noussair Mazraoui | DEF | 14 | 4.6 | 2.63 | 7.82 | 12.70 | 1.00 | 69.7 | 24.0 |
| XI | XI | Jørgen Strand Larsen | FWD | 20 | 5.6 | 4.21 | 11.42 | 18.37 | 2.00 | 78.5 | 61.0 |
| Bench 3 | Autosub In | Danny Welbeck | FWD | 5 | 5.9 | 2.43 | 7.41 | 13.08 | 1.00 | 39.4 | 20.0 |
| Bench 4 | Bench | Iliman Ndiaye | FWD | 8 | 5.4 | 1.99 | 6.83 | 11.69 | 0.00 | 52.0 | 0.0 |
| Captain | Bench | Mohamed Salah | MID | 12 | 13.0 | 7.65 | 23.74 | 39.37 | 0.00 | 93.3 | 0.0 |
| Vice Captain | Captain | Cole Palmer | MID | 6 | 11.0 | 6.46 | 18.29 | 29.82 | 18.00 | 89.6 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.04 | 13.57 | 22.88 | 9.00 | 78.2 | 75.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.4 | 4.58 | 12.02 | 19.09 | 2.00 | 63.2 | 62.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.8 | 3.71 | 11.89 | 20.93 | 13.00 | 76.1 | 90.0 |