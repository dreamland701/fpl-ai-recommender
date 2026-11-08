# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 247.67
- Total actual points: 216.00
- Average predicted points: 61.92
- Average actual points: 54.00
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW11 are included before the first simulated week.
- League-average scores were not available for this run.

## GW12

- Train rows: 111791
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Kieran Trippier
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 57.02
- Actual score: 66.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub outfielders: Pedro Porro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.70 | 10.41 | 16.82 | 2.00 | 85.9 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | 15 | 5.5 | 3.49 | 9.90 | 16.13 | 4.00 | 84.0 | 90.0 |
| Vice Captain | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.51 | 16.26 | 26.90 | 1.00 | 88.7 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.0 | 3.70 | 11.03 | 17.91 | 1.00 | 84.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.2 | 3.70 | 10.35 | 16.74 | 9.00 | 81.1 | 90.0 |
| XI | XI | Matty Cash | DEF | 2 | 5.2 | 3.78 | 10.33 | 16.23 | 2.00 | 68.6 | 90.0 |
| Bench 2 | Autosub In | Pedro Porro | DEF | 18 | 5.2 | 3.21 | 9.63 | 16.01 | 5.00 | 80.1 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 7.2 | 4.04 | 12.63 | 20.58 | 5.00 | 71.9 | 78.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 4.5 | 2.89 | 8.46 | 13.93 | 2.00 | 72.6 | 90.0 |
| Bench 4 | Bench | Chiedozie Ogbene | FWD | 12 | 4.9 | 2.32 | 7.52 | 12.89 | 2.00 | 71.0 | 85.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.9 | 6.65 | 19.76 | 32.51 | 16.00 | 94.7 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 5.30 | 16.14 | 27.25 | 2.00 | 83.1 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.6 | 5.42 | 14.90 | 24.53 | 5.00 | 78.3 | 80.0 |
| XI | Bench | James Maddison | MID | 18 | 8.1 | 4.57 | 14.10 | 23.29 | 0.00 | 67.6 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.7 | 4.02 | 12.61 | 21.30 | 2.00 | 89.2 | 90.0 |

## GW13

- Train rows: 112534
- Bank: 0.10 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Jarrod Bowen
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.29
- Actual score: 40.00
- Transfer: James Maddison -> Jarrod Bowen (projected gain 5.26, hit 0)
- Autosub outfielders: Pedro Porro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.62 | 10.28 | 16.59 | 3.00 | 85.8 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | 15 | 5.5 | 3.38 | 9.84 | 16.27 | 3.00 | 87.7 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.16 | 15.60 | 25.50 | 1.00 | 90.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.10 | 11.76 | 18.52 | 6.00 | 85.3 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.67 | 10.77 | 17.44 | 1.00 | 85.6 | 90.0 |
| XI | XI | Matty Cash | DEF | 2 | 5.2 | 3.44 | 10.20 | 15.95 | 0.00 | 71.9 | 45.0 |
| Bench 2 | Autosub In | Pedro Porro | DEF | 18 | 5.2 | 3.23 | 9.71 | 16.58 | 5.00 | 85.7 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 7.2 | 3.92 | 11.53 | 19.37 | 2.00 | 71.8 | 90.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.92 | 8.11 | 13.28 | 2.00 | 70.2 | 90.0 |
| Bench 4 | Bench | Chiedozie Ogbene | FWD | 12 | 4.9 | 2.82 | 8.10 | 13.92 | 5.00 | 70.9 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.9 | 6.19 | 20.45 | 34.19 | 5.00 | 98.8 | 90.0 |
| Vice Captain | Bench | Jarrod Bowen | MID | 19 | 7.6 | 5.17 | 14.87 | 22.94 | 0.00 | 81.7 | 0.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 4.87 | 14.80 | 24.68 | 2.00 | 84.2 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.6 | 4.99 | 14.57 | 23.42 | 8.00 | 74.3 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 3.96 | 12.44 | 20.88 | 2.00 | 80.5 | 90.0 |

## GW14

- Train rows: 113281
- Bank: 0.50 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 69.50
- Actual score: 73.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (12.10) beats the best remaining Bench Boost opportunity (13.62).
- Transfer: Jarrod Bowen -> Phil Foden (projected gain 1.92, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (12.10) beats the best remaining Bench Boost opportunity (13.62).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.66 | 10.25 | 16.55 | 2.00 | 86.2 | 90.0 |
| Bench 1 | Bench Boost | Nick Pope | GK | 15 | 5.5 | 3.04 | 9.39 | 15.63 | 6.00 | 85.8 | 85.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.78 | 14.40 | 24.02 | 12.00 | 88.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.29 | 12.07 | 18.97 | 1.00 | 83.4 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.2 | 3.69 | 10.84 | 17.43 | 2.00 | 85.7 | 90.0 |
| Bench 3 | Bench Boost | Pedro Porro | DEF | 18 | 5.3 | 3.09 | 10.00 | 17.09 | 0.00 | 87.9 | 90.0 |
| Bench 4 | Bench Boost | Matty Cash | DEF | 2 | 5.1 | 2.85 | 8.40 | 13.84 | 1.00 | 53.7 | 16.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 7.1 | 4.24 | 12.78 | 20.82 | 5.00 | 71.0 | 86.0 |
| Bench 2 | Bench Boost | Chiedozie Ogbene | FWD | 12 | 4.9 | 3.12 | 9.18 | 15.46 | 1.00 | 81.8 | 59.0 |
| XI | XI | Cameron Archer | FWD | 17 | 4.6 | 3.14 | 8.74 | 14.27 | 1.00 | 73.7 | 45.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.0 | 7.45 | 21.86 | 35.81 | 5.00 | 97.3 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.7 | 5.62 | 15.82 | 25.14 | 8.00 | 83.4 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 4.47 | 14.84 | 25.13 | 10.00 | 85.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 4.67 | 13.66 | 22.53 | 5.00 | 74.6 | 77.0 |
| XI | XI | Phil Foden | MID | 13 | 7.5 | 3.94 | 11.96 | 19.96 | 9.00 | 74.8 | 72.0 |

## GW15

- Train rows: 114034
- Bank: 0.70 -> 1.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 65.85
- Actual score: 37.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.34) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Nick Pope -> André Onana (projected gain 0.64, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.34) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.61 | 10.58 | 17.57 | 2.00 | 88.0 | 90.0 |
| Bench 1 | Bench | Alphonse Areola | GK | 19 | 4.3 | 3.25 | 9.94 | 16.08 | 0.00 | 86.1 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.42 | 15.60 | 25.55 | 1.00 | 95.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.14 | 11.86 | 19.05 | 1.00 | 84.3 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 3.70 | 11.02 | 18.35 | 5.00 | 83.2 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.2 | 3.76 | 10.54 | 17.31 | 1.00 | 84.9 | 90.0 |
| Bench 4 | Bench | Matty Cash | DEF | 2 | 5.0 | 1.81 | 6.55 | 10.95 | 0.00 | 40.3 | 0.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 7.0 | 4.27 | 13.17 | 21.99 | 2.00 | 76.0 | 67.0 |
| Bench 2 | Bench | Chiedozie Ogbene | FWD | 12 | 4.9 | 2.32 | 7.77 | 13.23 | 1.00 | 75.2 | 28.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.32 | 7.25 | 11.82 | 2.00 | 62.3 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 7.34 | 21.83 | 35.66 | 3.00 | 99.6 | 66.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.8 | 5.74 | 16.21 | 26.02 | 5.00 | 84.6 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 5.30 | 15.62 | 26.41 | 2.00 | 85.6 | 87.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.1 | 4.36 | 13.45 | 21.72 | 6.00 | 68.7 | 39.0 |
| XI | XI | Phil Foden | MID | 13 | 7.5 | 3.51 | 11.16 | 18.66 | 3.00 | 71.4 | 72.0 |