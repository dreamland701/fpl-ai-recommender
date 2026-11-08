# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 253.34
- Total actual points: 236.00
- Average predicted points: 63.34
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
- Bank: 100.00 -> 0.30
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 57.67
- Actual score: 69.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Ederson Santana de Moraes | GK | 13 | 5.5 | 3.68 | 10.23 | 16.11 | 2.00 | 88.9 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 4.8 | 3.31 | 9.24 | 15.74 | 1.00 | 90.8 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.07 | 14.90 | 24.44 | -1.00 | 75.6 | 85.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.74 | 14.18 | 23.53 | 4.00 | 91.1 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 3.76 | 11.00 | 18.00 | 5.00 | 80.8 | 90.0 |
| Bench 3 | Bench | William Saliba | DEF | 1 | 5.5 | 3.43 | 10.78 | 17.38 | 2.00 | 83.7 | 90.0 |
| Bench 2 | Bench | Vitalii Mykolenko | DEF | 9 | 4.5 | 3.60 | 9.69 | 15.66 | 7.00 | 81.9 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.80 | 10.36 | 16.82 | 9.00 | 82.1 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 3.86 | 10.30 | 16.77 | 2.00 | 69.1 | 90.0 |
| Bench 4 | Bench | Neal Maupay | FWD | 4 | 4.9 | 3.14 | 9.12 | 14.29 | 2.00 | 58.5 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.70 | 20.26 | 33.38 | 13.00 | 97.9 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 5.84 | 17.50 | 28.27 | 2.00 | 98.5 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 4.77 | 14.79 | 24.73 | 17.00 | 85.7 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.68 | 13.35 | 21.38 | 2.00 | 88.2 | 73.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 4.09 | 12.19 | 20.50 | 1.00 | 86.0 | 90.0 |

## GW17

- Train rows: 115549
- Bank: 0.30 -> 0.30
- Free transfers: 2 -> 2
- Captain: Son Heung-min
- Vice captain: Mohamed Salah
- Effective captain: Son Heung-min
- Chip used: none
- Predicted score: 61.84
- Actual score: 56.00
- Transfer: none
- No transfer was applied this week.
- Autosub: Neal Maupay replaced Kieran Trippier.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Ederson Santana de Moraes | GK | 13 | 5.5 | 3.47 | 9.72 | 15.36 | 0.00 | 84.8 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 4.8 | 2.45 | 8.71 | 14.41 | 10.00 | 84.5 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.69 | 14.56 | 23.97 | 9.00 | 94.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 5.23 | 13.51 | 21.52 | 8.00 | 100.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.18 | 11.85 | 18.73 | 7.00 | 87.3 | 90.0 |
| XI | Bench | Kieran Trippier | DEF | 15 | 6.9 | 3.41 | 11.01 | 19.40 | 0.00 | 48.0 | 0.0 |
| Bench 2 | Bench | Vitalii Mykolenko | DEF | 9 | 4.5 | 3.31 | 9.90 | 16.09 | 0.00 | 85.1 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.56 | 10.70 | 17.32 | 2.00 | 82.1 | 90.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 2.83 | 10.11 | 16.04 | 1.00 | 61.8 | 30.0 |
| Bench 3 | Autosub In | Neal Maupay | FWD | 4 | 4.9 | 3.03 | 8.74 | 13.41 | 0.00 | 69.6 | 22.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.1 | 7.21 | 22.08 | 35.86 | 3.00 | 110.7 | 90.0 |
| Captain | Captain | Son Heung-min | MID | 18 | 9.6 | 7.66 | 20.31 | 32.94 | 2.00 | 103.8 | 87.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 6.42 | 18.46 | 29.40 | 3.00 | 101.2 | 88.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.40 | 12.09 | 19.46 | 6.00 | 78.2 | 83.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.97 | 11.37 | 18.89 | 14.00 | 75.3 | 90.0 |

## GW18

- Train rows: 116314
- Bank: 0.30 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Son Heung-min
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 65.49
- Actual score: 46.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.68) beats the best remaining Triple Captain opportunity (8.09).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (5.68) beats the best remaining Triple Captain opportunity (8.09).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.30 | 10.10 | 16.74 | 2.00 | 90.9 | 90.0 |
| Bench 1 | Bench | Ederson Santana de Moraes | GK | 13 | 5.5 | 1.64 | 5.73 | 9.75 | 0.00 | 49.3 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.41 | 14.37 | 24.02 | 5.00 | 85.5 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 4.73 | 13.65 | 23.16 | 2.00 | 74.7 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 4.91 | 13.07 | 20.17 | 2.00 | 89.0 | 90.0 |
| Bench 2 | Bench | William Saliba | DEF | 1 | 5.5 | 3.53 | 10.95 | 17.46 | 2.00 | 89.5 | 90.0 |
| Bench 3 | Bench | Vitalii Mykolenko | DEF | 9 | 4.5 | 1.60 | 6.70 | 11.83 | 1.00 | 56.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.89 | 11.01 | 17.81 | 1.00 | 81.1 | 85.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 3.60 | 10.56 | 17.62 | 2.00 | 56.7 | 90.0 |
| Bench 4 | Bench | Neal Maupay | FWD | 4 | 4.9 | 0.66 | 3.30 | 6.09 | 0.00 | 14.3 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.37 | 20.40 | 33.56 | 7.00 | 76.9 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 5.91 | 18.18 | 28.80 | 1.00 | 98.3 | 90.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.7 | 6.08 | 17.38 | 27.43 | 7.00 | 71.7 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 5.16 | 13.62 | 21.50 | 1.00 | 79.3 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.38 | 12.63 | 20.57 | 2.00 | 75.4 | 90.0 |

## GW19

- Train rows: 117083
- Bank: 0.30 -> 1.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 68.35
- Actual score: 65.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.31) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Kieran Trippier -> Virgil van Dijk (projected gain 1.06, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.31) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.09 | 9.37 | 15.52 | 1.00 | 91.4 | 90.0 |
| Bench 1 | Bench Boost | Ederson Santana de Moraes | GK | 13 | 5.5 | 2.48 | 7.55 | 12.91 | 2.00 | 34.4 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.2 | 5.26 | 15.71 | 25.42 | 8.00 | 100.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 4.18 | 12.16 | 19.32 | 5.00 | 84.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.31 | 11.58 | 18.33 | 1.00 | 93.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.2 | 3.62 | 10.82 | 17.65 | 7.00 | 87.3 | 90.0 |
| Bench 3 | Bench Boost | Vitalii Mykolenko | DEF | 9 | 4.5 | 2.62 | 8.51 | 14.07 | 1.00 | 59.5 | 90.0 |
| Bench 2 | Bench Boost | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.7 | 3.45 | 10.30 | 16.79 | 5.00 | 72.9 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 3.47 | 9.63 | 15.35 | 16.00 | 70.2 | 90.0 |
| Bench 4 | Bench Boost | Neal Maupay | FWD | 4 | 4.9 | 0.76 | 2.34 | 4.01 | 5.00 | 13.2 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.2 | 6.95 | 20.91 | 34.64 | 3.00 | 103.2 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 6.11 | 17.92 | 29.31 | 5.00 | 99.5 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.28 | 17.64 | 28.27 | 2.00 | 98.2 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 5.12 | 13.72 | 22.39 | 1.00 | 88.6 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 3.69 | 11.44 | 18.47 | 0.00 | 68.2 | 0.0 |