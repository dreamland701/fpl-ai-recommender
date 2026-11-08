# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 246.26
- Total actual points: 284.00
- Average predicted points: 61.57
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
- Predicted score: 61.71
- Actual score: 50.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.45 | 10.13 | 16.50 | 6.00 | 89.9 | 90.0 |
| Bench 1 | Bench | Robert Sánchez | GK | 6 | 4.7 | 3.29 | 9.08 | 14.91 | 1.00 | 89.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.75 | 12.64 | 20.25 | 1.00 | 101.3 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.3 | 4.24 | 12.12 | 19.87 | 0.00 | 87.4 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 3.92 | 11.39 | 18.25 | 6.00 | 91.5 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.90 | 10.49 | 17.08 | 0.00 | 89.9 | 90.0 |
| Bench 2 | Bench | Lewis Hall | DEF | 15 | 4.4 | 3.74 | 10.11 | 16.19 | 1.00 | 92.0 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 6.0 | 3.87 | 11.89 | 18.87 | 2.00 | 79.5 | 85.0 |
| Bench 3 | Bench | Iliman Ndiaye | FWD | 8 | 5.4 | 2.85 | 7.90 | 12.87 | 2.00 | 70.4 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 5.0 | 1.89 | 6.56 | 10.43 | 1.00 | 59.9 | 13.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 8.11 | 22.25 | 36.31 | 13.00 | 113.7 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.97 | 19.56 | 31.98 | 2.00 | 103.8 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 6.34 | 16.50 | 26.41 | 2.00 | 106.8 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 4.19 | 14.54 | 23.90 | 3.00 | 87.5 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.4 | 3.83 | 11.00 | 17.74 | 2.00 | 78.5 | 81.0 |

## GW13

- Train rows: 141592
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 64.92
- Actual score: 89.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.18) beats the best remaining Triple Captain opportunity (9.01).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.18) beats the best remaining Triple Captain opportunity (9.01).
- Autosub: Iliman Ndiaye replaced Joško Gvardiol.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.88 | 10.76 | 17.36 | 2.00 | 91.8 | 90.0 |
| Bench 1 | Bench | Robert Sánchez | GK | 6 | 4.7 | 2.79 | 8.05 | 13.09 | 7.00 | 81.6 | 90.0 |
| XI | Bench | Joško Gvardiol | DEF | 13 | 6.3 | 3.39 | 11.33 | 18.98 | 0.00 | 83.2 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.71 | 11.20 | 18.02 | 6.00 | 85.3 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 3.98 | 11.10 | 17.72 | 9.00 | 89.4 | 45.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.04 | 9.25 | 15.16 | 2.00 | 80.0 | 90.0 |
| Bench 3 | Bench | Lewis Hall | DEF | 15 | 4.4 | 2.74 | 8.48 | 13.68 | 2.00 | 73.6 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 6.0 | 3.69 | 10.35 | 16.88 | 2.00 | 69.9 | 78.0 |
| Bench 2 | Autosub In | Iliman Ndiaye | FWD | 8 | 5.4 | 2.95 | 8.47 | 13.82 | 2.00 | 71.4 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 5.0 | 1.55 | 5.22 | 8.84 | 2.00 | 38.7 | 87.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 8.18 | 24.31 | 38.60 | 13.00 | 106.9 | 83.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.62 | 18.68 | 30.18 | 14.00 | 96.8 | 85.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.28 | 14.67 | 24.57 | 2.00 | 92.6 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.77 | 12.74 | 20.75 | 9.00 | 71.6 | 65.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.4 | 3.02 | 9.49 | 15.82 | 2.00 | 67.6 | 65.0 |

## GW14

- Train rows: 142282
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 66.90
- Actual score: 74.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.36) beats the best remaining Bench Boost opportunity (2.95).
- Transfer: Joško Gvardiol -> Pedro Porro (projected gain 3.45, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.36) beats the best remaining Bench Boost opportunity (2.95).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.58 | 10.03 | 16.34 | 6.00 | 86.6 | 90.0 |
| Bench 1 | Bench Boost | Robert Sánchez | GK | 6 | 4.7 | 3.57 | 9.48 | 15.10 | 0.00 | 90.4 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.28 | 12.66 | 20.54 | 1.00 | 97.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.05 | 11.79 | 18.93 | 1.00 | 87.5 | 28.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 3.71 | 10.66 | 17.21 | 0.00 | 76.9 | 0.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.29 | 9.41 | 15.35 | 6.00 | 82.2 | 90.0 |
| Bench 3 | Bench Boost | Lewis Hall | DEF | 15 | 4.4 | 2.50 | 8.11 | 13.41 | 1.00 | 77.4 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.9 | 3.01 | 9.52 | 15.83 | 0.00 | 66.5 | 0.0 |
| XI | XI | Iliman Ndiaye | FWD | 8 | 5.4 | 3.12 | 8.40 | 13.65 | 2.00 | 75.5 | 90.0 |
| Bench 4 | Bench Boost | Cameron Archer | FWD | 17 | 5.0 | 2.45 | 6.86 | 11.06 | 2.00 | 62.4 | 71.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 8.06 | 24.36 | 39.11 | 18.00 | 114.1 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 7.61 | 21.00 | 33.56 | 7.00 | 110.5 | 78.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.42 | 12.70 | 22.04 | 2.00 | 69.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.8 | 3.34 | 11.06 | 19.88 | 2.00 | 67.4 | 90.0 |
| Bench 2 | Bench Boost | Morgan Rogers | MID | 2 | 5.3 | 2.83 | 8.39 | 14.06 | 8.00 | 61.1 | 86.0 |

## GW15

- Train rows: 142975
- Bank: 0.60 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 52.74
- Actual score: 71.00
- Transfer: Danny Welbeck -> João Pedro Junqueira de Jesus (projected gain 4.64, hit 0)
- Autosub: Cameron Archer replaced Virgil van Dijk.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.76 | 10.96 | 17.72 | 2.00 | 90.4 | 90.0 |
| Bench 1 | Bench | Robert Sánchez | GK | 6 | 4.7 | 1.33 | 4.66 | 8.32 | 0.00 | 41.3 | 90.0 |
| XI | Bench | Virgil van Dijk | DEF | 12 | 6.3 | 2.85 | 9.87 | 16.77 | 0.00 | 66.6 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 2.93 | 9.38 | 16.08 | 3.00 | 67.6 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 2.79 | 9.17 | 15.08 | 1.00 | 81.4 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 2.66 | 7.64 | 12.54 | 1.00 | 77.8 | 82.0 |
| Bench 3 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 2.16 | 7.29 | 12.49 | 0.00 | 41.1 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.9 | 4.36 | 11.15 | 17.50 | 2.00 | 63.4 | 70.0 |
| Bench 4 | Bench | Iliman Ndiaye | FWD | 8 | 5.4 | 2.03 | 6.87 | 11.70 | 0.00 | 51.4 | 0.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 5.0 | 2.22 | 6.53 | 10.91 | 2.00 | 60.5 | 72.0 |
| Captain | Bench | Mohamed Salah | MID | 12 | 13.1 | 7.38 | 23.39 | 39.01 | 0.00 | 91.0 | 0.0 |
| Vice Captain | Captain | Cole Palmer | MID | 6 | 10.9 | 6.93 | 19.67 | 31.84 | 18.00 | 97.5 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.29 | 13.90 | 23.51 | 9.00 | 82.9 | 75.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.3 | 4.25 | 11.36 | 18.34 | 2.00 | 77.7 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 3.14 | 10.34 | 18.68 | 13.00 | 68.1 | 90.0 |