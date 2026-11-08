# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 254.11
- Total actual points: 301.00
- Average predicted points: 63.53
- Average actual points: 75.25
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
- Predicted score: 62.44
- Actual score: 52.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.46 | 10.09 | 16.40 | 6.00 | 92.2 | 90.0 |
| Bench 1 | Bench | Robert Sánchez | GK | 6 | 4.7 | 3.34 | 9.19 | 15.05 | 1.00 | 90.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.77 | 12.66 | 20.25 | 1.00 | 101.8 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.3 | 4.28 | 12.27 | 20.12 | 0.00 | 88.3 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 3.94 | 11.41 | 18.24 | 6.00 | 71.0 | 90.0 |
| Bench 2 | Bench | Antonee Robinson | DEF | 9 | 4.7 | 3.91 | 10.44 | 16.97 | 0.00 | 91.2 | 90.0 |
| XI | XI | Noussair Mazraoui | DEF | 14 | 4.6 | 3.92 | 10.42 | 16.31 | 2.00 | 92.9 | 90.0 |
| XI | XI | Raúl Jiménez | FWD | 9 | 5.8 | 4.21 | 11.18 | 19.11 | 2.00 | 73.1 | 70.0 |
| Bench 3 | Bench | Michail Antonio | FWD | 19 | 5.4 | 2.79 | 9.62 | 15.93 | 2.00 | 44.7 | 74.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 5.0 | 2.19 | 7.67 | 12.24 | 1.00 | 58.9 | 13.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 8.11 | 22.21 | 36.23 | 13.00 | 115.2 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.94 | 19.51 | 31.98 | 2.00 | 105.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 6.36 | 16.55 | 26.43 | 2.00 | 108.3 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 4.22 | 14.58 | 23.92 | 3.00 | 84.9 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.4 | 4.11 | 11.75 | 18.91 | 2.00 | 77.0 | 81.0 |

## GW13

- Train rows: 141592
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 67.65
- Actual score: 88.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.18) beats the best remaining Triple Captain opportunity (8.97).
- Transfer: Raúl Jiménez -> João Pedro Junqueira de Jesus (projected gain 4.96, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.18) beats the best remaining Triple Captain opportunity (8.97).
- Autosub: Antonee Robinson replaced Joško Gvardiol.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.88 | 10.72 | 17.27 | 2.00 | 93.1 | 90.0 |
| Bench 1 | Bench | Robert Sánchez | GK | 6 | 4.7 | 2.92 | 8.39 | 13.62 | 7.00 | 84.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.85 | 11.58 | 18.59 | 6.00 | 87.9 | 90.0 |
| XI | Bench | Joško Gvardiol | DEF | 13 | 6.3 | 3.38 | 11.35 | 19.03 | 0.00 | 83.1 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 4.04 | 11.24 | 17.92 | 9.00 | 94.0 | 45.0 |
| Bench 2 | Autosub In | Antonee Robinson | DEF | 9 | 4.7 | 3.11 | 9.41 | 15.40 | 2.00 | 82.3 | 90.0 |
| XI | XI | Noussair Mazraoui | DEF | 14 | 4.6 | 3.22 | 9.41 | 14.90 | 1.00 | 81.7 | 55.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.7 | 5.49 | 13.67 | 20.51 | 2.00 | 49.2 | 71.0 |
| Bench 3 | Bench | Michail Antonio | FWD | 19 | 5.4 | 2.83 | 8.71 | 14.90 | 2.00 | 46.7 | 64.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 5.0 | 2.16 | 7.35 | 12.47 | 2.00 | 27.7 | 87.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 8.18 | 24.26 | 38.49 | 13.00 | 105.5 | 83.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.59 | 18.64 | 30.18 | 14.00 | 98.0 | 85.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.30 | 14.72 | 24.60 | 2.00 | 93.1 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.08 | 13.76 | 22.36 | 9.00 | 76.1 | 65.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.4 | 3.27 | 10.24 | 17.03 | 2.00 | 73.1 | 65.0 |

## GW14

- Train rows: 142282
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 68.87
- Actual score: 83.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.83) beats the best remaining Bench Boost opportunity (5.74).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.83) beats the best remaining Bench Boost opportunity (5.74).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.66 | 10.19 | 16.59 | 6.00 | 88.9 | 90.0 |
| Bench 1 | Bench Boost | Robert Sánchez | GK | 6 | 4.7 | 3.57 | 9.46 | 15.06 | 0.00 | 93.1 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.29 | 12.68 | 20.52 | 1.00 | 98.4 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 4.11 | 11.80 | 19.02 | 0.00 | 84.5 | 0.0 |
| Bench 2 | Bench Boost | Joško Gvardiol | DEF | 13 | 6.2 | 2.96 | 10.33 | 18.21 | 6.00 | 58.4 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.36 | 9.57 | 15.59 | 6.00 | 84.6 | 90.0 |
| Bench 4 | Bench Boost | Noussair Mazraoui | DEF | 14 | 4.6 | 2.46 | 8.24 | 13.95 | 1.00 | 64.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.7 | 3.88 | 11.89 | 18.10 | 5.00 | 24.9 | 79.0 |
| XI | XI | Michail Antonio | FWD | 19 | 5.4 | 3.60 | 9.32 | 15.63 | 1.00 | 70.4 | 28.0 |
| Bench 3 | Bench Boost | Cameron Archer | FWD | 17 | 5.0 | 2.84 | 7.99 | 12.90 | 2.00 | 72.4 | 71.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 8.06 | 24.30 | 39.01 | 18.00 | 94.6 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 7.58 | 20.97 | 33.57 | 7.00 | 109.7 | 78.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.75 | 13.90 | 24.06 | 2.00 | 75.1 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.8 | 3.40 | 11.24 | 20.17 | 2.00 | 67.9 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.3 | 3.26 | 9.62 | 16.09 | 8.00 | 69.6 | 86.0 |

## GW15

- Train rows: 142975
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 55.16
- Actual score: 78.00
- Transfer: Virgil van Dijk -> William Saliba (projected gain 3.34, hit 0)
- Autosub: Antonee Robinson replaced Gabriel dos Santos Magalhães.
- Autosub: Cameron Archer replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.77 | 10.92 | 17.63 | 2.00 | 92.7 | 90.0 |
| Bench 1 | Bench | Robert Sánchez | GK | 6 | 4.7 | 0.83 | 2.91 | 5.19 | 0.00 | 25.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.24 | 12.08 | 20.33 | 1.00 | 85.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.1 | 4.14 | 11.84 | 18.76 | 9.00 | 93.7 | 90.0 |
| XI | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 3.05 | 10.22 | 17.45 | 0.00 | 30.6 | 0.0 |
| Bench 3 | Autosub In | Antonee Robinson | DEF | 9 | 4.7 | 2.85 | 9.33 | 15.32 | 1.00 | 82.7 | 90.0 |
| XI | XI | Noussair Mazraoui | DEF | 14 | 4.6 | 3.05 | 8.84 | 14.21 | 1.00 | 73.3 | 24.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.8 | 5.10 | 13.06 | 20.50 | 2.00 | 74.2 | 70.0 |
| Bench 2 | Bench | Michail Antonio | FWD | 19 | 5.4 | 2.90 | 8.54 | 14.33 | 0.00 | 34.4 | 0.0 |
| Bench 4 | Autosub In | Cameron Archer | FWD | 17 | 5.0 | 2.61 | 7.74 | 12.96 | 2.00 | 70.5 | 72.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 10.9 | 6.90 | 19.64 | 31.84 | 18.00 | 96.7 | 90.0 |
| Vice Captain | Bench | Mohamed Salah | MID | 12 | 13.1 | 5.54 | 17.49 | 29.17 | 0.00 | 71.5 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.54 | 14.70 | 24.82 | 9.00 | 87.5 | 75.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.3 | 4.56 | 12.14 | 19.56 | 2.00 | 83.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 3.36 | 11.07 | 19.97 | 13.00 | 72.6 | 90.0 |