# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 238.05
- Total actual points: 236.00
- Average predicted points: 59.51
- Average actual points: 59.00
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW15 are included before the first simulated week.
- League-average scores were not available for this run.

## GW16

- Train rows: 114791
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 53.74
- Actual score: 62.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Ederson Santana de Moraes | GK | 13 | 5.5 | 3.41 | 9.50 | 14.96 | 2.00 | 83.9 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 4.8 | 3.06 | 8.56 | 14.62 | 1.00 | 88.8 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.68 | 13.73 | 22.60 | -1.00 | 95.6 | 85.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.41 | 13.25 | 22.02 | 4.00 | 89.1 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 3.43 | 10.10 | 16.54 | 5.00 | 77.8 | 90.0 |
| Bench 2 | Bench | William Saliba | DEF | 1 | 5.5 | 3.13 | 9.86 | 15.91 | 2.00 | 81.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.1 | 3.39 | 9.70 | 15.76 | 2.00 | 83.7 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 3.52 | 9.42 | 15.28 | 2.00 | 60.1 | 90.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.84 | 7.40 | 11.73 | 2.00 | 68.2 | 90.0 |
| Bench 4 | Bench | Antoine Semenyo | FWD | 3 | 4.6 | 2.15 | 6.96 | 10.62 | 1.00 | 46.2 | 57.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.46 | 19.56 | 32.27 | 13.00 | 93.9 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 5.50 | 16.53 | 26.75 | 2.00 | 97.5 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 4.36 | 13.59 | 22.83 | 17.00 | 84.7 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.34 | 12.40 | 19.85 | 2.00 | 81.2 | 73.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.78 | 11.27 | 18.96 | 1.00 | 81.0 | 90.0 |

## GW17

- Train rows: 115549
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Son Heung-min
- Vice captain: Mohamed Salah
- Effective captain: Son Heung-min
- Chip used: none
- Predicted score: 58.06
- Actual score: 62.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Ederson Santana de Moraes | GK | 13 | 5.5 | 3.25 | 9.11 | 14.39 | 0.00 | 78.8 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 4.8 | 2.28 | 8.13 | 13.46 | 10.00 | 82.5 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.54 | 14.14 | 23.28 | 9.00 | 91.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 5.04 | 12.99 | 20.70 | 8.00 | 98.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 3.91 | 11.09 | 17.53 | 7.00 | 85.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.1 | 3.30 | 10.10 | 16.30 | 6.00 | 83.8 | 90.0 |
| Bench 2 | Bench | Kieran Trippier | DEF | 15 | 6.9 | 3.08 | 10.08 | 17.91 | 0.00 | 68.0 | 0.0 |
| Bench 3 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 2.61 | 9.22 | 14.61 | 1.00 | 52.8 | 30.0 |
| XI | XI | Cameron Archer | FWD | 17 | 4.6 | 2.75 | 7.82 | 12.42 | 2.00 | 68.4 | 90.0 |
| Bench 4 | Bench | Antoine Semenyo | FWD | 3 | 4.6 | 0.90 | 2.78 | 4.65 | 0.00 | 30.4 | 0.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.1 | 6.78 | 20.87 | 33.95 | 3.00 | 110.7 | 90.0 |
| Captain | Captain | Son Heung-min | MID | 18 | 9.6 | 7.28 | 19.25 | 31.24 | 2.00 | 123.8 | 87.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 6.09 | 17.53 | 27.96 | 3.00 | 100.2 | 88.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.12 | 11.33 | 18.21 | 6.00 | 70.2 | 83.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.70 | 10.60 | 17.61 | 14.00 | 68.3 | 90.0 |

## GW18

- Train rows: 116314
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Son Heung-min
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 61.44
- Actual score: 47.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.41) beats the best remaining Triple Captain opportunity (7.75).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (5.41) beats the best remaining Triple Captain opportunity (7.75).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.07 | 9.43 | 15.66 | 2.00 | 90.9 | 90.0 |
| Bench 1 | Bench | Ederson Santana de Moraes | GK | 13 | 5.5 | 1.70 | 5.33 | 8.96 | 0.00 | 64.3 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.11 | 13.44 | 22.49 | 5.00 | 83.5 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 4.45 | 13.18 | 22.60 | 2.00 | 59.7 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 4.60 | 12.21 | 18.82 | 2.00 | 87.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 3.28 | 10.19 | 16.26 | 2.00 | 89.5 | 90.0 |
| Bench 2 | Bench | Virgil van Dijk | DEF | 11 | 6.1 | 3.01 | 9.78 | 16.01 | 2.00 | 83.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 3.30 | 9.64 | 15.93 | 2.00 | 41.7 | 90.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.56 | 7.55 | 11.88 | 8.00 | 75.8 | 89.0 |
| Bench 4 | Bench | Antoine Semenyo | FWD | 3 | 4.6 | 2.12 | 6.17 | 10.09 | 1.00 | 26.8 | 69.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.10 | 19.57 | 32.22 | 7.00 | 96.9 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 5.60 | 17.23 | 27.35 | 1.00 | 97.3 | 90.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.7 | 5.81 | 16.61 | 26.20 | 7.00 | 91.7 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 4.84 | 12.71 | 20.08 | 1.00 | 99.3 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.08 | 11.76 | 19.15 | 2.00 | 69.4 | 90.0 |

## GW19

- Train rows: 117083
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 64.80
- Actual score: 65.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.99) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.99) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 2.79 | 8.48 | 14.07 | 1.00 | 91.4 | 90.0 |
| Bench 1 | Bench Boost | Ederson Santana de Moraes | GK | 13 | 5.5 | 2.22 | 6.76 | 11.49 | 2.00 | 45.4 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.2 | 4.91 | 14.69 | 23.79 | 8.00 | 98.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 3.78 | 10.98 | 17.47 | 5.00 | 83.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 3.93 | 10.52 | 16.66 | 1.00 | 93.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.1 | 3.28 | 9.84 | 16.07 | 7.00 | 84.3 | 90.0 |
| Bench 2 | Bench Boost | Kieran Trippier | DEF | 15 | 6.9 | 3.23 | 9.43 | 16.13 | 1.00 | 82.5 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 3.12 | 8.65 | 13.79 | 16.00 | 63.2 | 90.0 |
| Bench 3 | Bench Boost | Cameron Archer | FWD | 17 | 4.6 | 3.01 | 8.00 | 12.94 | 5.00 | 78.1 | 85.0 |
| Bench 4 | Bench Boost | Antoine Semenyo | FWD | 3 | 4.6 | 2.52 | 6.77 | 10.75 | 5.00 | 41.6 | 71.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.2 | 6.34 | 19.14 | 31.79 | 3.00 | 104.2 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 5.84 | 16.43 | 26.40 | 2.00 | 96.2 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 5.57 | 16.36 | 26.85 | 5.00 | 101.5 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.69 | 12.56 | 20.51 | 1.00 | 82.6 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 3.23 | 10.10 | 16.37 | 0.00 | 66.2 | 0.0 |