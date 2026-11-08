# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 226.36
- Total actual points: 316.00
- Average predicted points: 56.59
- Average actual points: 79.00
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
- Bank: 100.00 -> 0.20
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Bruno Borges Fernandes
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.59
- Actual score: 53.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Sánchez | GK | 6 | 4.7 | 3.92 | 10.64 | 18.16 | 1.00 | 87.8 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 5.1 | 3.63 | 10.40 | 18.99 | 3.00 | 86.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 3.59 | 10.81 | 16.44 | 7.00 | 79.1 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.3 | 4.25 | 10.67 | 16.90 | 0.00 | 86.4 | 90.0 |
| Bench 2 | Bench | Ashley Young | DEF | 8 | 4.5 | 3.37 | 10.29 | 15.70 | 9.00 | 86.9 | 90.0 |
| XI | XI | Andrew Robertson | DEF | 12 | 5.9 | 3.61 | 10.05 | 16.36 | 1.00 | 74.0 | 90.0 |
| Bench 3 | Bench | Antonee Robinson | DEF | 9 | 4.7 | 3.19 | 9.39 | 16.90 | 0.00 | 89.3 | 90.0 |
| XI | XI | Raúl Jiménez | FWD | 9 | 5.8 | 4.20 | 12.04 | 22.29 | 2.00 | 69.2 | 70.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 6.0 | 3.72 | 11.93 | 20.00 | 2.00 | 83.8 | 85.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 5.0 | 2.66 | 7.89 | 12.32 | 1.00 | 60.8 | 13.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 6.57 | 19.60 | 28.20 | 13.00 | 86.3 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.9 | 5.60 | 18.25 | 33.13 | 2.00 | 86.5 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 5.85 | 14.80 | 24.66 | 2.00 | 87.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 3.92 | 14.58 | 23.10 | 3.00 | 78.4 | 90.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.6 | 3.79 | 13.84 | 21.32 | 7.00 | 83.6 | 90.0 |

## GW13

- Train rows: 141592
- Bank: 0.20 -> 0.30
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: bench_boost
- Predicted score: 61.76
- Actual score: 87.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.26) beats the best remaining Bench Boost opportunity (10.37).
- Transfer: Ashley Young -> Lewis Hall (projected gain 2.86, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.26) beats the best remaining Bench Boost opportunity (10.37).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench Boost | André Onana | GK | 14 | 5.1 | 2.72 | 10.82 | 18.11 | 6.00 | 88.0 | 90.0 |
| XI | XI | Robert Sánchez | GK | 6 | 4.7 | 3.28 | 10.30 | 17.41 | 7.00 | 87.4 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 3.06 | 11.01 | 16.24 | 2.00 | 83.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 4.11 | 10.80 | 16.84 | 1.00 | 81.4 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.3 | 3.43 | 9.71 | 17.08 | 0.00 | 85.2 | 0.0 |
| XI | XI | Andrew Robertson | DEF | 12 | 5.9 | 2.98 | 9.58 | 16.89 | 6.00 | 71.3 | 90.0 |
| Bench 2 | Bench Boost | Antonee Robinson | DEF | 9 | 4.7 | 2.90 | 7.75 | 12.79 | 2.00 | 82.9 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 6.0 | 3.74 | 10.12 | 16.83 | 2.00 | 77.2 | 78.0 |
| Bench 3 | Bench Boost | Raúl Jiménez | FWD | 9 | 5.7 | 2.17 | 8.08 | 10.95 | 2.00 | 34.3 | 77.0 |
| Bench 4 | Bench Boost | Cameron Archer | FWD | 17 | 5.0 | 1.48 | 6.47 | 10.51 | 2.00 | 46.2 | 87.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.0 | 6.25 | 19.65 | 32.16 | 13.00 | 91.4 | 83.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 10.9 | 7.16 | 18.86 | 33.57 | 14.00 | 89.3 | 85.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.30 | 14.68 | 20.44 | 9.00 | 83.9 | 65.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 4.90 | 12.18 | 21.34 | 2.00 | 81.8 | 90.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.6 | 3.14 | 11.65 | 18.20 | 5.00 | 85.1 | 85.0 |

## GW14

- Train rows: 142282
- Bank: 0.30 -> 0.10
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 50.90
- Actual score: 82.00
- Transfer: Raúl Jiménez -> João Pedro Junqueira de Jesus (projected gain 5.63, hit 0)
- Autosub: André Onana replaced Robert Sánchez.
- Autosub: Cameron Archer replaced Danny Welbeck.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Robert Sánchez | GK | 6 | 4.7 | 3.97 | 11.06 | 15.97 | 0.00 | 88.2 | 0.0 |
| Bench 1 | Autosub In | André Onana | GK | 14 | 5.1 | 2.41 | 8.91 | 15.75 | 2.00 | 88.7 | 90.0 |
| XI | XI | Andrew Robertson | DEF | 12 | 5.9 | 3.60 | 10.38 | 17.79 | 1.00 | 80.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 3.26 | 9.22 | 15.71 | 15.00 | 78.7 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.41 | 8.22 | 15.20 | 6.00 | 85.7 | 90.0 |
| Bench 3 | Bench | Lewis Hall | DEF | 15 | 4.4 | 2.40 | 7.85 | 12.92 | 1.00 | 86.1 | 90.0 |
| Bench 4 | Bench | Joško Gvardiol | DEF | 13 | 6.2 | 2.07 | 7.76 | 15.70 | 6.00 | 49.8 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.8 | 3.87 | 13.03 | 19.16 | 5.00 | 76.0 | 79.0 |
| XI | Bench | Danny Welbeck | FWD | 5 | 5.9 | 3.21 | 9.06 | 14.88 | 0.00 | 72.8 | 0.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 5.0 | 2.87 | 7.89 | 12.95 | 2.00 | 61.1 | 71.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 10.9 | 6.57 | 20.93 | 33.00 | 7.00 | 83.6 | 78.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.1 | 5.72 | 17.91 | 31.21 | 18.00 | 84.6 | 90.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.6 | 4.83 | 12.63 | 21.16 | 15.00 | 80.7 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 2.87 | 10.34 | 18.20 | 2.00 | 59.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.8 | 3.02 | 9.82 | 19.20 | 2.00 | 69.8 | 90.0 |

## GW15

- Train rows: 142975
- Bank: 0.10 -> 1.30
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 58.11
- Actual score: 94.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.81) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Andrew Robertson -> Lucas Digne (projected gain 4.15, hit 0)
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (6.81) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 5.1 | 2.85 | 9.81 | 16.27 | 1.00 | 88.3 | 90.0 |
| Bench 1 | Bench | Robert Sánchez | GK | 6 | 4.7 | 1.67 | 5.99 | 11.33 | 0.00 | 60.3 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 3.97 | 13.23 | 22.82 | 1.00 | 88.1 | 90.0 |
| XI | XI | Lucas Digne | DEF | 2 | 4.7 | 4.49 | 12.11 | 16.07 | 1.00 | 81.8 | 31.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 3.83 | 11.22 | 18.58 | 9.00 | 82.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 2.82 | 8.95 | 15.76 | 1.00 | 87.0 | 82.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 2.53 | 8.70 | 13.29 | 1.00 | 85.8 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.8 | 4.61 | 13.48 | 19.50 | 2.00 | 80.7 | 70.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 5.0 | 2.16 | 8.13 | 13.70 | 2.00 | 58.6 | 72.0 |
| Bench 3 | Bench | Danny Welbeck | FWD | 5 | 5.9 | 1.30 | 4.41 | 8.93 | 1.00 | 24.1 | 20.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 10.9 | 7.44 | 20.29 | 36.45 | 18.00 | 81.2 | 90.0 |
| Bench 4 | Bench | Mohamed Salah | MID | 12 | 13.1 | 0.54 | 17.31 | 25.02 | 0.00 | 2.8 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.08 | 12.60 | 19.78 | 9.00 | 80.8 | 75.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.6 | 3.45 | 10.97 | 16.23 | 2.00 | 81.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 3.14 | 10.19 | 17.35 | 13.00 | 74.4 | 90.0 |