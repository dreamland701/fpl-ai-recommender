# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 224.51
- Total actual points: 294.00
- Average predicted points: 56.13
- Average actual points: 73.50
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
- Predicted score: 56.91
- Actual score: 50.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.18 | 9.27 | 15.09 | 6.00 | 90.2 | 90.0 |
| Bench 1 | Bench | Robert Sánchez | GK | 6 | 4.7 | 3.02 | 8.32 | 13.65 | 1.00 | 88.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.38 | 11.61 | 18.59 | 1.00 | 100.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 3.82 | 11.06 | 17.70 | 6.00 | 91.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.3 | 3.82 | 10.97 | 18.05 | 0.00 | 87.3 | 90.0 |
| XI | XI | Ibrahima Konaté | DEF | 12 | 5.4 | 3.90 | 10.03 | 16.01 | 0.00 | 88.4 | 90.0 |
| Bench 2 | Bench | Lewis Hall | DEF | 15 | 4.4 | 3.60 | 9.68 | 15.50 | 1.00 | 91.5 | 90.0 |
| XI | XI | Liam Delap | FWD | 10 | 5.6 | 3.04 | 9.30 | 15.17 | 2.00 | 61.5 | 80.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 5.0 | 1.97 | 6.87 | 10.94 | 1.00 | 59.9 | 13.0 |
| Bench 3 | Bench | Adam Armstrong | FWD | 17 | 5.1 | 2.32 | 6.80 | 10.61 | 7.00 | 62.7 | 76.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 7.51 | 20.47 | 33.47 | 13.00 | 114.2 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.39 | 17.96 | 29.45 | 2.00 | 104.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 5.97 | 15.49 | 24.77 | 2.00 | 106.3 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 3.69 | 13.00 | 21.39 | 3.00 | 86.9 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.4 | 3.70 | 10.58 | 17.03 | 2.00 | 78.0 | 81.0 |

## GW13

- Train rows: 141592
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 59.81
- Actual score: 92.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.50) beats the best remaining Triple Captain opportunity (8.35).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.50) beats the best remaining Triple Captain opportunity (8.35).
- Autosub: Lewis Hall replaced Joško Gvardiol.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.59 | 9.90 | 15.98 | 2.00 | 92.1 | 90.0 |
| Bench 1 | Bench | Robert Sánchez | GK | 6 | 4.7 | 2.64 | 7.58 | 12.32 | 7.00 | 81.2 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 3.84 | 10.69 | 17.06 | 9.00 | 89.0 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.48 | 10.49 | 16.83 | 6.00 | 84.9 | 90.0 |
| XI | Bench | Joško Gvardiol | DEF | 13 | 6.3 | 2.98 | 10.10 | 17.01 | 0.00 | 83.1 | 0.0 |
| Bench 2 | Autosub In | Lewis Hall | DEF | 15 | 4.4 | 2.69 | 8.31 | 13.39 | 2.00 | 73.2 | 90.0 |
| Bench 4 | Bench | Ibrahima Konaté | DEF | 12 | 5.4 | 1.40 | 4.65 | 7.68 | 0.00 | 65.1 | 0.0 |
| XI | XI | Liam Delap | FWD | 10 | 5.6 | 3.04 | 9.49 | 15.15 | 2.00 | 62.5 | 90.0 |
| XI | XI | Adam Armstrong | FWD | 17 | 5.1 | 2.79 | 7.82 | 12.12 | 5.00 | 64.3 | 90.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 5.0 | 1.99 | 6.64 | 11.23 | 2.00 | 38.7 | 87.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 7.50 | 22.29 | 35.42 | 13.00 | 107.5 | 83.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.14 | 17.34 | 28.11 | 14.00 | 97.0 | 85.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 4.86 | 13.46 | 22.54 | 2.00 | 92.1 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.65 | 12.38 | 20.13 | 9.00 | 71.1 | 65.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.4 | 2.92 | 9.15 | 15.24 | 2.00 | 67.1 | 65.0 |

## GW14

- Train rows: 142282
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 58.50
- Actual score: 74.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.92) beats the best remaining Bench Boost opportunity (2.53).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.92) beats the best remaining Bench Boost opportunity (2.53).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench Boost | David Raya Martin | GK | 1 | 5.5 | 3.21 | 8.97 | 14.64 | 6.00 | 86.9 | 90.0 |
| XI | XI | Robert Sánchez | GK | 6 | 4.7 | 3.27 | 8.67 | 13.81 | 0.00 | 90.1 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.86 | 11.38 | 18.45 | 1.00 | 97.4 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 3.67 | 10.52 | 16.97 | 0.00 | 76.5 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 2.61 | 9.00 | 15.82 | 6.00 | 45.4 | 90.0 |
| Bench 3 | Bench Boost | Lewis Hall | DEF | 15 | 4.4 | 2.37 | 7.69 | 12.71 | 1.00 | 77.1 | 90.0 |
| Bench 4 | Bench Boost | Ibrahima Konaté | DEF | 12 | 5.3 | 0.83 | 4.53 | 9.16 | 0.00 | 23.3 | 0.0 |
| XI | XI | Liam Delap | FWD | 10 | 5.6 | 3.33 | 9.34 | 14.98 | 2.00 | 70.6 | 78.0 |
| XI | XI | Adam Armstrong | FWD | 17 | 5.1 | 2.73 | 7.85 | 12.10 | 1.00 | 68.6 | 61.0 |
| Bench 2 | Bench Boost | Cameron Archer | FWD | 17 | 5.0 | 2.51 | 7.05 | 11.38 | 2.00 | 62.4 | 71.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 7.17 | 21.71 | 34.98 | 18.00 | 114.6 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.79 | 18.81 | 30.18 | 7.00 | 110.7 | 78.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.27 | 12.20 | 21.18 | 2.00 | 69.1 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.8 | 2.86 | 9.59 | 17.44 | 2.00 | 66.9 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.3 | 2.85 | 8.41 | 14.07 | 8.00 | 60.6 | 86.0 |

## GW15

- Train rows: 142975
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 49.29
- Actual score: 78.00
- Transfer: Virgil van Dijk -> William Saliba (projected gain 4.01, hit 0)
- Autosub: Adam Armstrong replaced Gabriel dos Santos Magalhães.
- Autosub: Cameron Archer replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.52 | 10.23 | 16.53 | 2.00 | 90.7 | 90.0 |
| Bench 1 | Bench | Robert Sánchez | GK | 6 | 4.7 | 0.65 | 2.48 | 4.54 | 0.00 | 41.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.1 | 3.97 | 11.36 | 18.02 | 9.00 | 88.7 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 3.89 | 11.07 | 18.64 | 1.00 | 80.6 | 90.0 |
| XI | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 2.79 | 9.20 | 15.63 | 0.00 | 40.6 | 0.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 2.65 | 7.57 | 12.41 | 1.00 | 77.5 | 82.0 |
| Bench 4 | Bench | Ibrahima Konaté | DEF | 12 | 5.3 | 0.07 | 2.45 | 5.88 | 0.00 | 4.4 | 0.0 |
| XI | XI | Liam Delap | FWD | 10 | 5.6 | 3.05 | 8.64 | 14.05 | 1.00 | 58.5 | 80.0 |
| Bench 2 | Autosub In | Adam Armstrong | FWD | 17 | 5.1 | 2.57 | 7.41 | 12.36 | 2.00 | 58.3 | 90.0 |
| Bench 3 | Autosub In | Cameron Archer | FWD | 17 | 5.0 | 2.38 | 7.06 | 11.79 | 2.00 | 60.5 | 72.0 |
| Vice Captain | Bench | Mohamed Salah | MID | 12 | 13.1 | 5.38 | 19.33 | 32.89 | 0.00 | 91.5 | 0.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 10.9 | 6.32 | 18.03 | 29.34 | 18.00 | 97.7 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.18 | 13.52 | 22.86 | 9.00 | 82.5 | 75.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.3 | 4.18 | 11.12 | 17.93 | 2.00 | 77.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 3.02 | 9.98 | 18.04 | 13.00 | 67.6 | 90.0 |