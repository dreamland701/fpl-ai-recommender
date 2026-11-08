# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 246.47
- Total actual points: 284.00
- Average predicted points: 61.62
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
- Predicted score: 61.78
- Actual score: 50.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.46 | 10.09 | 16.40 | 6.00 | 88.9 | 90.0 |
| Bench 1 | Bench | Robert Sánchez | GK | 6 | 4.7 | 3.29 | 9.07 | 14.86 | 1.00 | 87.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.77 | 12.66 | 20.25 | 1.00 | 86.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.3 | 4.24 | 12.14 | 19.92 | 0.00 | 86.4 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 3.94 | 11.41 | 18.24 | 6.00 | 85.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.91 | 10.44 | 16.97 | 0.00 | 89.3 | 90.0 |
| Bench 2 | Bench | Lewis Hall | DEF | 15 | 4.4 | 3.74 | 10.08 | 16.11 | 1.00 | 86.1 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 6.0 | 3.88 | 11.85 | 18.76 | 2.00 | 83.8 | 85.0 |
| Bench 3 | Bench | Iliman Ndiaye | FWD | 8 | 5.4 | 2.84 | 7.93 | 12.96 | 2.00 | 72.7 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 5.0 | 1.88 | 6.58 | 10.50 | 1.00 | 60.8 | 13.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 8.11 | 22.21 | 36.23 | 13.00 | 86.3 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.94 | 19.51 | 31.98 | 2.00 | 86.5 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 6.36 | 16.55 | 26.43 | 2.00 | 87.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 4.22 | 14.58 | 23.92 | 3.00 | 78.4 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.4 | 3.84 | 10.99 | 17.68 | 2.00 | 81.2 | 81.0 |

## GW13

- Train rows: 141592
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 64.97
- Actual score: 89.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.18) beats the best remaining Triple Captain opportunity (8.97).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.18) beats the best remaining Triple Captain opportunity (8.97).
- Autosub: Iliman Ndiaye replaced Joško Gvardiol.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.88 | 10.72 | 17.27 | 2.00 | 88.2 | 90.0 |
| Bench 1 | Bench | Robert Sánchez | GK | 6 | 4.7 | 2.79 | 8.03 | 13.04 | 7.00 | 87.4 | 90.0 |
| XI | Bench | Joško Gvardiol | DEF | 13 | 6.3 | 3.38 | 11.35 | 19.03 | 0.00 | 85.2 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.73 | 11.22 | 18.02 | 6.00 | 86.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 3.99 | 11.11 | 17.71 | 9.00 | 84.3 | 45.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.04 | 9.20 | 15.06 | 2.00 | 82.9 | 90.0 |
| Bench 3 | Bench | Lewis Hall | DEF | 15 | 4.4 | 2.74 | 8.45 | 13.61 | 2.00 | 83.2 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 6.0 | 3.70 | 10.31 | 16.79 | 2.00 | 77.2 | 78.0 |
| Bench 2 | Autosub In | Iliman Ndiaye | FWD | 8 | 5.4 | 2.94 | 8.50 | 13.91 | 2.00 | 70.8 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 5.0 | 1.54 | 5.25 | 8.91 | 2.00 | 46.2 | 87.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 8.18 | 24.26 | 38.49 | 13.00 | 91.4 | 83.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.59 | 18.64 | 30.18 | 14.00 | 89.3 | 85.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.30 | 14.72 | 24.60 | 2.00 | 81.8 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.79 | 12.79 | 20.78 | 9.00 | 83.9 | 65.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.4 | 3.03 | 9.48 | 15.77 | 2.00 | 72.8 | 65.0 |

## GW14

- Train rows: 142282
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 66.94
- Actual score: 74.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.37) beats the best remaining Bench Boost opportunity (2.96).
- Transfer: Joško Gvardiol -> Pedro Porro (projected gain 3.43, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.37) beats the best remaining Bench Boost opportunity (2.96).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.59 | 9.99 | 16.25 | 6.00 | 85.5 | 90.0 |
| Bench 1 | Bench Boost | Robert Sánchez | GK | 6 | 4.7 | 3.57 | 9.46 | 15.06 | 0.00 | 88.2 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.29 | 12.68 | 20.52 | 1.00 | 86.6 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.06 | 11.75 | 18.85 | 1.00 | 86.8 | 28.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 3.72 | 10.67 | 17.20 | 0.00 | 71.6 | 0.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.29 | 9.37 | 15.26 | 6.00 | 85.7 | 90.0 |
| Bench 3 | Bench Boost | Lewis Hall | DEF | 15 | 4.4 | 2.50 | 8.09 | 13.35 | 1.00 | 86.1 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.9 | 3.01 | 9.48 | 15.74 | 0.00 | 72.8 | 0.0 |
| XI | XI | Iliman Ndiaye | FWD | 8 | 5.4 | 3.11 | 8.43 | 13.76 | 2.00 | 78.3 | 90.0 |
| Bench 4 | Bench Boost | Cameron Archer | FWD | 17 | 5.0 | 2.45 | 6.90 | 11.14 | 2.00 | 61.1 | 71.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 8.06 | 24.30 | 39.01 | 18.00 | 84.6 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 7.58 | 20.97 | 33.57 | 7.00 | 83.6 | 78.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.44 | 12.73 | 22.05 | 2.00 | 59.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.8 | 3.36 | 11.09 | 19.90 | 2.00 | 69.8 | 90.0 |
| Bench 2 | Bench Boost | Morgan Rogers | MID | 2 | 5.3 | 2.84 | 8.38 | 14.01 | 8.00 | 63.0 | 86.0 |

## GW15

- Train rows: 142975
- Bank: 0.60 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 52.77
- Actual score: 71.00
- Transfer: Danny Welbeck -> João Pedro Junqueira de Jesus (projected gain 4.61, hit 0)
- Autosub: Cameron Archer replaced Virgil van Dijk.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.77 | 10.92 | 17.63 | 2.00 | 88.5 | 90.0 |
| Bench 1 | Bench | Robert Sánchez | GK | 6 | 4.7 | 1.33 | 4.65 | 8.27 | 0.00 | 60.3 | 90.0 |
| XI | Bench | Virgil van Dijk | DEF | 12 | 6.3 | 2.86 | 9.88 | 16.74 | 0.00 | 1.5 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 2.94 | 9.34 | 15.99 | 3.00 | 63.8 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 2.79 | 9.13 | 14.99 | 1.00 | 85.8 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 2.67 | 7.62 | 12.49 | 1.00 | 87.0 | 82.0 |
| Bench 3 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 2.18 | 7.30 | 12.47 | 0.00 | 43.4 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.9 | 4.36 | 11.16 | 17.51 | 2.00 | 80.7 | 70.0 |
| Bench 4 | Bench | Iliman Ndiaye | FWD | 8 | 5.4 | 2.03 | 6.90 | 11.79 | 0.00 | 0.7 | 0.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 5.0 | 2.21 | 6.56 | 11.00 | 2.00 | 58.6 | 72.0 |
| Captain | Bench | Mohamed Salah | MID | 12 | 13.1 | 7.38 | 23.33 | 38.89 | 0.00 | 2.8 | 0.0 |
| Vice Captain | Captain | Cole Palmer | MID | 6 | 10.9 | 6.90 | 19.64 | 31.84 | 18.00 | 81.2 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.31 | 13.94 | 23.54 | 9.00 | 80.8 | 75.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.3 | 4.26 | 11.35 | 18.28 | 2.00 | 80.7 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 3.15 | 10.38 | 18.72 | 13.00 | 74.4 | 90.0 |