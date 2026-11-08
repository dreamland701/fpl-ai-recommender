# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 250.94
- Total actual points: 214.00
- Average predicted points: 62.74
- Average actual points: 53.50
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
- Predicted score: 56.04
- Actual score: 68.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.26 | 9.12 | 15.54 | 1.00 | 88.8 | 90.0 |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.7 | 3.17 | 9.02 | 14.62 | 9.00 | 85.4 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.07 | 14.90 | 24.44 | -1.00 | 95.6 | 85.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.69 | 14.03 | 23.28 | 4.00 | 89.1 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 3.63 | 10.64 | 17.39 | 5.00 | 77.8 | 90.0 |
| Bench 2 | Bench | William Saliba | DEF | 1 | 5.5 | 3.36 | 10.55 | 17.00 | 2.00 | 81.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.1 | 3.66 | 10.45 | 16.93 | 2.00 | 83.7 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.63 | 9.90 | 16.08 | 9.00 | 78.1 | 90.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.84 | 7.40 | 11.73 | 2.00 | 68.2 | 90.0 |
| Bench 4 | Bench | Raúl Jiménez | FWD | 10 | 5.2 | 2.69 | 7.22 | 11.74 | 9.00 | 57.9 | 71.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.70 | 20.26 | 33.38 | 13.00 | 93.9 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 5.84 | 17.50 | 28.27 | 2.00 | 97.5 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 4.72 | 14.63 | 24.47 | 17.00 | 84.7 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.30 | 12.26 | 19.64 | 2.00 | 81.2 | 73.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.83 | 11.43 | 19.22 | 1.00 | 81.0 | 90.0 |

## GW17

- Train rows: 115549
- Bank: 0.00 -> 0.80
- Free transfers: 2 -> 2
- Captain: Son Heung-min
- Vice captain: Mohamed Salah
- Effective captain: Son Heung-min
- Chip used: none
- Predicted score: 60.52
- Actual score: 60.00
- Transfer: Virgil van Dijk -> Kyle Walker (projected gain 0.56, hit 0)
- Autosub: Kyle Walker replaced Kieran Trippier.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.14 | 9.73 | 15.75 | 3.00 | 86.7 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 4.8 | 2.40 | 8.53 | 14.10 | 10.00 | 82.5 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.69 | 14.56 | 23.97 | 9.00 | 91.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 5.23 | 13.51 | 21.52 | 8.00 | 98.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.05 | 11.49 | 18.15 | 7.00 | 85.3 | 90.0 |
| XI | Bench | Kieran Trippier | DEF | 15 | 6.9 | 3.41 | 11.01 | 19.40 | 0.00 | 68.0 | 0.0 |
| Bench 2 | Autosub In | Kyle Walker | DEF | 13 | 5.3 | 3.38 | 9.23 | 14.59 | 1.00 | 78.7 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.48 | 10.46 | 16.94 | 2.00 | 80.1 | 90.0 |
| Bench 4 | Bench | Raúl Jiménez | FWD | 10 | 5.2 | 2.52 | 8.02 | 13.16 | -2.00 | 57.6 | 21.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.70 | 7.69 | 12.22 | 2.00 | 68.4 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.1 | 7.21 | 22.08 | 35.86 | 3.00 | 110.7 | 90.0 |
| Captain | Captain | Son Heung-min | MID | 18 | 9.6 | 7.66 | 20.31 | 32.94 | 2.00 | 123.8 | 87.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 6.42 | 18.46 | 29.40 | 3.00 | 100.2 | 88.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.94 | 10.84 | 17.45 | 6.00 | 70.2 | 83.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.64 | 10.41 | 17.30 | 14.00 | 68.3 | 90.0 |

## GW18

- Train rows: 116314
- Bank: 0.80 -> 0.80
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Son Heung-min
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 64.07
- Actual score: 45.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.68) beats the best remaining Triple Captain opportunity (8.09).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (5.68) beats the best remaining Triple Captain opportunity (8.09).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.65 | 10.19 | 16.53 | 1.00 | 93.2 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 4.8 | 3.30 | 10.10 | 16.74 | 2.00 | 90.9 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.27 | 13.92 | 23.26 | 5.00 | 83.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 4.82 | 12.80 | 19.76 | 2.00 | 87.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 3.81 | 11.00 | 18.66 | 2.00 | 59.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 3.53 | 10.95 | 17.46 | 2.00 | 89.5 | 90.0 |
| Bench 3 | Bench | Kyle Walker | DEF | 13 | 5.3 | 2.34 | 7.86 | 13.27 | 0.00 | 62.4 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.72 | 10.52 | 17.01 | 1.00 | 77.1 | 85.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.59 | 7.65 | 12.03 | 8.00 | 75.8 | 89.0 |
| Bench 4 | Bench | Raúl Jiménez | FWD | 10 | 5.2 | 1.89 | 5.87 | 10.45 | 0.00 | 38.1 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.37 | 20.40 | 33.56 | 7.00 | 96.9 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 5.91 | 18.18 | 28.80 | 1.00 | 97.3 | 90.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.7 | 6.08 | 17.38 | 27.43 | 7.00 | 91.7 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 5.16 | 13.62 | 21.50 | 1.00 | 99.3 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.02 | 11.58 | 18.86 | 2.00 | 69.4 | 90.0 |

## GW19

- Train rows: 117083
- Bank: 0.80 -> 0.90
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 70.31
- Actual score: 41.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.75) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Kyle Walker -> Oleksandr Zinchenko (projected gain 0.12, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.75) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.09 | 9.37 | 15.52 | 1.00 | 91.4 | 90.0 |
| Bench 1 | Bench Boost | Bernd Leno | GK | 10 | 4.7 | 2.95 | 8.79 | 14.69 | 0.00 | 84.2 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.2 | 5.26 | 15.71 | 25.42 | 8.00 | 98.4 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 4.84 | 13.43 | 22.13 | 1.00 | 82.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 4.14 | 12.03 | 19.11 | 5.00 | 83.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.31 | 11.58 | 18.33 | 1.00 | 93.8 | 90.0 |
| Bench 2 | Bench Boost | Oleksandr Zinchenko | DEF | 1 | 5.2 | 3.59 | 9.71 | 15.44 | 1.00 | 78.3 | 63.0 |
| Bench 3 | Bench Boost | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.7 | 3.19 | 9.55 | 15.55 | 5.00 | 67.9 | 90.0 |
| XI | XI | Cameron Archer | FWD | 17 | 4.6 | 3.24 | 8.60 | 13.87 | 5.00 | 78.1 | 85.0 |
| Bench 4 | Bench Boost | Raúl Jiménez | FWD | 10 | 5.2 | 1.02 | 4.09 | 8.53 | 0.00 | 21.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.2 | 6.95 | 20.91 | 34.64 | 3.00 | 104.2 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 6.11 | 17.92 | 29.31 | 5.00 | 101.5 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.28 | 17.64 | 28.27 | 2.00 | 96.2 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.81 | 12.88 | 21.02 | 1.00 | 82.6 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 3.60 | 11.13 | 17.98 | 0.00 | 66.2 | 0.0 |