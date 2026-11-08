# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 247.38
- Total actual points: 216.00
- Average predicted points: 61.85
- Average actual points: 54.00
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
- Predicted score: 55.54
- Actual score: 65.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.27 | 9.12 | 15.54 | 1.00 | 89.2 | 90.0 |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.7 | 3.15 | 9.02 | 14.62 | 9.00 | 83.8 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.07 | 14.90 | 24.44 | -1.00 | 90.0 | 85.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.57 | 14.03 | 23.28 | 4.00 | 86.9 | 90.0 |
| Bench 2 | Bench | Pedro Porro | DEF | 18 | 5.3 | 3.46 | 10.64 | 17.39 | 5.00 | 75.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 3.47 | 10.55 | 17.00 | 2.00 | 81.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.1 | 3.64 | 10.45 | 16.93 | 2.00 | 82.8 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.58 | 9.90 | 16.08 | 9.00 | 77.9 | 90.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.79 | 7.40 | 11.73 | 2.00 | 66.8 | 90.0 |
| Bench 4 | Bench | Raúl Jiménez | FWD | 10 | 5.2 | 2.49 | 7.22 | 11.74 | 9.00 | 55.8 | 71.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.74 | 20.26 | 33.38 | 13.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 5.76 | 17.50 | 28.27 | 2.00 | 90.0 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 4.88 | 14.63 | 24.47 | 17.00 | 84.6 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.06 | 12.26 | 19.64 | 2.00 | 78.2 | 73.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.76 | 11.43 | 19.22 | 1.00 | 81.6 | 90.0 |

## GW17

- Train rows: 115549
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Son Heung-min
- Vice captain: Mohamed Salah
- Effective captain: Son Heung-min
- Chip used: none
- Predicted score: 59.07
- Actual score: 65.00
- Transfer: none
- No transfer was applied this week.
- Autosub: Virgil van Dijk replaced Kieran Trippier.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.13 | 9.73 | 15.75 | 3.00 | 85.3 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 4.8 | 2.48 | 8.53 | 14.10 | 10.00 | 83.2 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.52 | 14.56 | 23.97 | 9.00 | 88.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 4.81 | 13.51 | 21.52 | 8.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.05 | 11.49 | 18.15 | 7.00 | 83.9 | 90.0 |
| XI | Bench | Kieran Trippier | DEF | 15 | 6.9 | 3.78 | 11.01 | 19.40 | 0.00 | 72.4 | 0.0 |
| Bench 2 | Autosub In | Virgil van Dijk | DEF | 11 | 6.1 | 3.38 | 10.45 | 16.85 | 6.00 | 82.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.39 | 10.46 | 16.94 | 2.00 | 79.7 | 90.0 |
| Bench 4 | Bench | Raúl Jiménez | FWD | 10 | 5.2 | 2.35 | 8.02 | 13.16 | -2.00 | 56.2 | 21.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.63 | 7.69 | 12.22 | 2.00 | 66.5 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.1 | 7.16 | 22.08 | 35.86 | 3.00 | 90.0 | 90.0 |
| Captain | Captain | Son Heung-min | MID | 18 | 9.6 | 7.24 | 20.31 | 32.94 | 2.00 | 90.0 | 87.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 6.34 | 18.46 | 29.40 | 3.00 | 90.0 | 88.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.81 | 10.84 | 17.45 | 6.00 | 68.6 | 83.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.60 | 10.41 | 17.30 | 14.00 | 68.9 | 90.0 |

## GW18

- Train rows: 116314
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 62.75
- Actual score: 45.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.72) beats the best remaining Triple Captain opportunity (8.14).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (5.72) beats the best remaining Triple Captain opportunity (8.14).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.56 | 10.19 | 16.53 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 4.8 | 3.35 | 10.10 | 16.74 | 2.00 | 90.0 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.23 | 13.92 | 23.26 | 5.00 | 82.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 4.45 | 12.80 | 19.76 | 2.00 | 80.4 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 3.57 | 11.00 | 18.66 | 2.00 | 56.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 3.55 | 10.95 | 17.46 | 2.00 | 87.9 | 90.0 |
| Bench 2 | Bench | Virgil van Dijk | DEF | 11 | 6.1 | 3.19 | 10.36 | 16.93 | 2.00 | 82.4 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.60 | 10.52 | 17.01 | 1.00 | 75.2 | 85.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.53 | 7.65 | 12.03 | 8.00 | 74.2 | 89.0 |
| Bench 4 | Bench | Raúl Jiménez | FWD | 10 | 5.2 | 1.77 | 5.87 | 10.45 | 0.00 | 38.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.41 | 20.40 | 33.56 | 7.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 5.89 | 18.18 | 28.80 | 1.00 | 90.0 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 5.81 | 17.38 | 27.43 | 7.00 | 85.8 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 4.89 | 13.62 | 21.50 | 1.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.98 | 11.58 | 18.86 | 2.00 | 70.7 | 90.0 |

## GW19

- Train rows: 117083
- Bank: 0.00 -> 0.90
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 70.03
- Actual score: 41.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.68) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Virgil van Dijk -> Oleksandr Zinchenko (projected gain 0.00, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.68) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.16 | 9.37 | 15.52 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Bernd Leno | GK | 10 | 4.7 | 2.96 | 8.79 | 14.69 | 0.00 | 84.2 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.2 | 5.06 | 15.71 | 25.42 | 8.00 | 90.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 4.89 | 13.43 | 22.13 | 1.00 | 82.6 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 3.99 | 12.03 | 19.11 | 5.00 | 80.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.30 | 11.58 | 18.33 | 1.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Oleksandr Zinchenko | DEF | 1 | 5.2 | 3.53 | 9.71 | 15.44 | 1.00 | 76.4 | 63.0 |
| Bench 3 | Bench Boost | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.7 | 3.12 | 9.55 | 15.55 | 5.00 | 66.9 | 90.0 |
| XI | XI | Cameron Archer | FWD | 17 | 4.6 | 3.21 | 8.60 | 13.87 | 5.00 | 78.0 | 85.0 |
| Bench 4 | Bench Boost | Raúl Jiménez | FWD | 10 | 5.2 | 1.07 | 4.09 | 8.53 | 0.00 | 24.2 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.2 | 7.05 | 20.91 | 34.64 | 3.00 | 90.0 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 6.03 | 17.92 | 29.31 | 5.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.29 | 17.64 | 28.27 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.73 | 12.88 | 21.02 | 1.00 | 81.3 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 3.60 | 11.13 | 17.98 | 0.00 | 66.2 | 0.0 |