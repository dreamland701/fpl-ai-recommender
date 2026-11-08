# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 253.87
- Total actual points: 232.00
- Average predicted points: 63.47
- Average actual points: 58.00
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
- Predicted score: 56.06
- Actual score: 68.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.26 | 9.12 | 15.54 | 1.00 | 89.2 | 90.0 |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.7 | 3.17 | 8.98 | 14.53 | 9.00 | 85.5 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.08 | 14.89 | 24.41 | -1.00 | 95.7 | 85.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.68 | 14.06 | 23.34 | 4.00 | 88.6 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 3.62 | 10.68 | 17.50 | 5.00 | 77.3 | 90.0 |
| Bench 2 | Bench | William Saliba | DEF | 1 | 5.5 | 3.35 | 10.54 | 17.01 | 2.00 | 82.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.1 | 3.67 | 10.43 | 16.87 | 2.00 | 83.8 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.63 | 9.89 | 16.06 | 9.00 | 78.5 | 90.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.84 | 7.41 | 11.75 | 2.00 | 67.6 | 90.0 |
| Bench 4 | Bench | Raúl Jiménez | FWD | 10 | 5.2 | 2.69 | 7.28 | 11.85 | 9.00 | 57.4 | 71.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.71 | 20.28 | 33.41 | 13.00 | 93.8 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 5.85 | 17.52 | 28.28 | 2.00 | 97.4 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 4.73 | 14.61 | 24.44 | 17.00 | 84.8 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.29 | 12.26 | 19.64 | 2.00 | 81.6 | 73.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.83 | 11.43 | 19.25 | 1.00 | 81.3 | 90.0 |

## GW17

- Train rows: 115549
- Bank: 0.00 -> 1.50
- Free transfers: 2 -> 2
- Captain: Son Heung-min
- Vice captain: Mohamed Salah
- Effective captain: Son Heung-min
- Chip used: none
- Predicted score: 60.54
- Actual score: 61.00
- Transfer: Virgil van Dijk -> Vitalii Mykolenko (projected gain 0.54, hit 0)
- Autosub: Cameron Archer replaced Kieran Trippier.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.15 | 9.69 | 15.66 | 3.00 | 86.8 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 4.8 | 2.39 | 8.52 | 14.11 | 10.00 | 82.8 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.69 | 14.59 | 24.03 | 9.00 | 91.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 5.22 | 13.56 | 21.63 | 8.00 | 98.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.04 | 11.48 | 18.16 | 7.00 | 85.6 | 90.0 |
| XI | Bench | Kieran Trippier | DEF | 15 | 6.9 | 3.42 | 11.00 | 19.37 | 0.00 | 68.1 | 0.0 |
| Bench 2 | Bench | Vitalii Mykolenko | DEF | 9 | 4.6 | 3.14 | 9.38 | 15.25 | 0.00 | 81.4 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.47 | 10.45 | 16.93 | 2.00 | 80.4 | 90.0 |
| Bench 4 | Bench | Raúl Jiménez | FWD | 10 | 5.2 | 2.51 | 8.08 | 13.28 | -2.00 | 57.1 | 21.0 |
| Bench 3 | Autosub In | Cameron Archer | FWD | 17 | 4.6 | 2.71 | 7.71 | 12.24 | 2.00 | 67.8 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.1 | 7.22 | 22.12 | 35.90 | 3.00 | 110.6 | 90.0 |
| Captain | Captain | Son Heung-min | MID | 18 | 9.6 | 7.66 | 20.30 | 32.91 | 2.00 | 123.9 | 87.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 6.43 | 18.48 | 29.41 | 3.00 | 100.1 | 88.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.93 | 10.82 | 17.43 | 6.00 | 70.6 | 83.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.63 | 10.41 | 17.32 | 14.00 | 68.7 | 90.0 |

## GW18

- Train rows: 116314
- Bank: 1.50 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Son Heung-min
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 66.30
- Actual score: 61.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.70) beats the best remaining Triple Captain opportunity (8.11).
- Transfer: Matheus Santos Carneiro Da Cunha -> Dominic Solanke (projected gain 3.65, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (5.70) beats the best remaining Triple Captain opportunity (8.11).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.66 | 10.15 | 16.44 | 1.00 | 93.2 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 4.8 | 3.30 | 10.09 | 16.75 | 2.00 | 91.2 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.27 | 13.96 | 23.34 | 5.00 | 83.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 4.81 | 12.86 | 19.87 | 2.00 | 86.5 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 3.82 | 10.99 | 18.62 | 2.00 | 59.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 3.52 | 10.93 | 17.45 | 2.00 | 89.9 | 90.0 |
| Bench 4 | Bench | Vitalii Mykolenko | DEF | 9 | 4.6 | 1.14 | 4.79 | 8.46 | 1.00 | 40.4 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 6.8 | 5.87 | 14.16 | 21.74 | 17.00 | 93.5 | 90.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.59 | 7.68 | 12.06 | 8.00 | 75.2 | 89.0 |
| Bench 3 | Bench | Raúl Jiménez | FWD | 10 | 5.2 | 1.88 | 5.93 | 10.57 | 0.00 | 37.7 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.39 | 20.44 | 33.60 | 7.00 | 96.8 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 5.93 | 18.20 | 28.82 | 1.00 | 97.2 | 90.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.7 | 6.09 | 17.38 | 27.41 | 7.00 | 91.8 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 5.16 | 13.61 | 21.51 | 1.00 | 99.7 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.01 | 11.56 | 18.85 | 2.00 | 69.8 | 90.0 |

## GW19

- Train rows: 117083
- Bank: 0.30 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 70.97
- Actual score: 42.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.53) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.53) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.09 | 9.36 | 15.51 | 1.00 | 91.7 | 90.0 |
| Bench 1 | Bench Boost | Bernd Leno | GK | 10 | 4.7 | 2.95 | 8.75 | 14.59 | 0.00 | 84.3 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.2 | 5.26 | 15.76 | 25.51 | 8.00 | 97.9 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 4.85 | 13.43 | 22.10 | 1.00 | 82.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 4.13 | 12.09 | 19.23 | 5.00 | 83.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.31 | 11.56 | 18.32 | 1.00 | 94.1 | 90.0 |
| Bench 3 | Bench Boost | Vitalii Mykolenko | DEF | 9 | 4.6 | 2.32 | 7.55 | 12.50 | 1.00 | 70.8 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 6.9 | 5.06 | 13.41 | 21.28 | 6.00 | 79.5 | 90.0 |
| Bench 2 | Bench Boost | Cameron Archer | FWD | 17 | 4.6 | 3.24 | 8.63 | 13.91 | 5.00 | 77.4 | 85.0 |
| Bench 4 | Bench Boost | Raúl Jiménez | FWD | 10 | 5.2 | 1.02 | 4.15 | 8.65 | 0.00 | 20.9 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.2 | 6.97 | 20.97 | 34.70 | 3.00 | 104.0 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 6.11 | 17.91 | 29.30 | 5.00 | 101.6 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.29 | 17.67 | 28.29 | 2.00 | 96.1 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.80 | 12.86 | 21.00 | 1.00 | 83.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 3.59 | 11.12 | 17.98 | 0.00 | 66.6 | 0.0 |