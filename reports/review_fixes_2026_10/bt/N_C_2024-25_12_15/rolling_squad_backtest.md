# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 246.37
- Total actual points: 284.00
- Average predicted points: 61.59
- Average actual points: 71.00
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
- Predicted score: 61.51
- Actual score: 50.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.47 | 10.07 | 16.42 | 6.00 | 90.2 | 90.0 |
| Bench 1 | Bench | Robert Sánchez | GK | 6 | 4.7 | 3.27 | 9.01 | 14.80 | 1.00 | 88.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.81 | 12.86 | 20.54 | 1.00 | 101.9 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.3 | 4.16 | 12.04 | 19.71 | 0.00 | 86.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 3.97 | 11.38 | 18.28 | 6.00 | 91.2 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.75 | 10.29 | 16.60 | 0.00 | 87.6 | 90.0 |
| Bench 2 | Bench | Lewis Hall | DEF | 15 | 4.4 | 3.71 | 10.13 | 16.14 | 1.00 | 91.7 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 6.0 | 3.93 | 11.60 | 18.61 | 2.00 | 79.1 | 85.0 |
| Bench 3 | Bench | Iliman Ndiaye | FWD | 8 | 5.4 | 2.69 | 7.76 | 12.66 | 2.00 | 68.8 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 5.0 | 2.00 | 6.55 | 10.58 | 1.00 | 60.1 | 13.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 8.06 | 22.68 | 36.62 | 13.00 | 114.9 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.81 | 19.26 | 31.63 | 2.00 | 103.9 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 5.98 | 16.25 | 25.81 | 2.00 | 105.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 4.59 | 14.68 | 24.40 | 3.00 | 87.2 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.4 | 3.95 | 11.05 | 17.92 | 2.00 | 79.3 | 81.0 |

## GW13

- Train rows: 141592
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 64.22
- Actual score: 89.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.88) beats the best remaining Triple Captain opportunity (8.89).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.88) beats the best remaining Triple Captain opportunity (8.89).
- Autosub: Antonee Robinson replaced Joško Gvardiol.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.95 | 10.86 | 17.49 | 2.00 | 93.1 | 90.0 |
| Bench 1 | Bench | Robert Sánchez | GK | 6 | 4.7 | 2.74 | 7.89 | 12.86 | 7.00 | 80.3 | 90.0 |
| XI | Bench | Joško Gvardiol | DEF | 13 | 6.3 | 3.38 | 11.28 | 18.95 | 0.00 | 82.3 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 4.04 | 11.24 | 17.88 | 9.00 | 89.5 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.60 | 10.96 | 17.67 | 6.00 | 84.1 | 90.0 |
| Bench 2 | Autosub In | Antonee Robinson | DEF | 9 | 4.7 | 3.01 | 9.02 | 14.82 | 2.00 | 78.0 | 90.0 |
| Bench 3 | Bench | Lewis Hall | DEF | 15 | 4.4 | 2.73 | 8.35 | 13.55 | 2.00 | 73.6 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 6.0 | 3.60 | 10.22 | 16.62 | 2.00 | 69.4 | 78.0 |
| XI | XI | Iliman Ndiaye | FWD | 8 | 5.4 | 3.05 | 8.67 | 14.20 | 2.00 | 73.0 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 5.0 | 1.54 | 5.12 | 8.80 | 2.00 | 37.8 | 87.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 7.88 | 23.34 | 37.51 | 13.00 | 109.3 | 83.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.53 | 18.51 | 30.06 | 14.00 | 97.6 | 85.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.06 | 14.59 | 24.21 | 2.00 | 90.3 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.33 | 13.43 | 21.92 | 9.00 | 73.7 | 65.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.4 | 3.05 | 9.44 | 15.77 | 2.00 | 66.4 | 65.0 |

## GW14

- Train rows: 142282
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 67.63
- Actual score: 74.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.43) beats the best remaining Bench Boost opportunity (2.99).
- Transfer: Joško Gvardiol -> Pedro Porro (projected gain 3.19, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.43) beats the best remaining Bench Boost opportunity (2.99).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.65 | 10.08 | 16.38 | 6.00 | 86.5 | 90.0 |
| Bench 1 | Bench Boost | Robert Sánchez | GK | 6 | 4.7 | 3.60 | 9.50 | 15.13 | 0.00 | 90.8 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.39 | 12.81 | 20.73 | 1.00 | 98.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 3.90 | 11.38 | 18.34 | 1.00 | 86.7 | 28.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 3.87 | 10.92 | 17.54 | 0.00 | 75.9 | 0.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.30 | 9.43 | 15.31 | 6.00 | 82.5 | 90.0 |
| Bench 3 | Bench Boost | Lewis Hall | DEF | 15 | 4.4 | 2.57 | 8.13 | 13.43 | 1.00 | 77.4 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.9 | 3.03 | 9.46 | 15.73 | 0.00 | 67.0 | 0.0 |
| XI | XI | Iliman Ndiaye | FWD | 8 | 5.4 | 3.08 | 8.40 | 13.69 | 2.00 | 75.2 | 90.0 |
| Bench 4 | Bench Boost | Cameron Archer | FWD | 17 | 5.0 | 2.53 | 7.01 | 11.35 | 2.00 | 63.6 | 71.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 8.30 | 24.51 | 39.42 | 18.00 | 116.4 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 7.65 | 20.91 | 33.63 | 7.00 | 112.7 | 78.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.62 | 12.94 | 22.42 | 2.00 | 69.5 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.8 | 3.10 | 11.06 | 19.65 | 2.00 | 66.3 | 90.0 |
| Bench 2 | Bench Boost | Morgan Rogers | MID | 2 | 5.3 | 2.74 | 8.22 | 13.68 | 8.00 | 58.1 | 86.0 |

## GW15

- Train rows: 142975
- Bank: 0.60 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 53.00
- Actual score: 71.00
- Transfer: Danny Welbeck -> João Pedro Junqueira de Jesus (projected gain 4.48, hit 0)
- Autosub: Cameron Archer replaced Virgil van Dijk.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.78 | 10.93 | 17.63 | 2.00 | 91.0 | 90.0 |
| Bench 1 | Bench | Robert Sánchez | GK | 6 | 4.7 | 1.40 | 4.83 | 8.48 | 0.00 | 41.7 | 90.0 |
| XI | Bench | Virgil van Dijk | DEF | 12 | 6.3 | 2.87 | 9.90 | 16.77 | 0.00 | 66.4 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 3.14 | 9.72 | 16.49 | 3.00 | 69.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 2.90 | 9.24 | 15.16 | 1.00 | 82.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 2.66 | 7.67 | 12.49 | 1.00 | 77.4 | 82.0 |
| Bench 2 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 2.19 | 7.29 | 12.48 | 0.00 | 41.3 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.9 | 4.16 | 11.03 | 17.22 | 2.00 | 63.1 | 70.0 |
| Bench 4 | Bench | Iliman Ndiaye | FWD | 8 | 5.4 | 2.00 | 6.83 | 11.68 | 0.00 | 50.8 | 0.0 |
| Bench 3 | Autosub In | Cameron Archer | FWD | 17 | 5.0 | 2.16 | 6.56 | 10.91 | 2.00 | 59.9 | 72.0 |
| Captain | Bench | Mohamed Salah | MID | 12 | 13.1 | 7.40 | 23.43 | 39.04 | 0.00 | 93.0 | 0.0 |
| Vice Captain | Captain | Cole Palmer | MID | 6 | 10.9 | 7.11 | 20.25 | 32.49 | 18.00 | 97.9 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.32 | 14.17 | 23.80 | 9.00 | 85.0 | 75.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.3 | 4.08 | 11.05 | 17.82 | 2.00 | 76.2 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 3.18 | 10.41 | 18.77 | 13.00 | 68.4 | 90.0 |