# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 254.01
- Total actual points: 238.00
- Average predicted points: 63.50
- Average actual points: 59.50
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
- Bank: 100.00 -> 0.20
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 57.54
- Actual score: 68.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.43 | 9.55 | 16.22 | 1.00 | 92.4 | 90.0 |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.7 | 3.17 | 9.03 | 14.63 | 9.00 | 84.9 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.00 | 15.00 | 24.53 | -1.00 | 98.3 | 85.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.80 | 14.26 | 23.66 | 4.00 | 91.5 | 90.0 |
| Bench 2 | Bench | William Saliba | DEF | 1 | 5.5 | 3.57 | 10.90 | 17.59 | 2.00 | 84.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 3.78 | 10.87 | 17.86 | 5.00 | 80.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.1 | 3.75 | 10.65 | 17.25 | 2.00 | 85.9 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.52 | 9.71 | 15.80 | 9.00 | 79.5 | 90.0 |
| Bench 3 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 3.28 | 9.03 | 14.65 | 2.00 | 59.7 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.81 | 7.41 | 11.73 | 2.00 | 68.4 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.90 | 20.67 | 34.07 | 13.00 | 98.5 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.04 | 17.96 | 29.02 | 2.00 | 100.8 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 4.89 | 14.94 | 25.01 | 17.00 | 87.6 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 4.11 | 11.75 | 19.80 | 1.00 | 82.4 | 90.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.7 | 4.40 | 11.48 | 18.26 | 2.00 | 93.0 | 90.0 |

## GW17

- Train rows: 115549
- Bank: 0.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Son Heung-min
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 60.74
- Actual score: 62.00
- Transfer: none
- No transfer was applied this week.
- Autosub: Hwang Hee-chan replaced Kieran Trippier.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.00 | 9.37 | 15.32 | 3.00 | 85.4 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 4.8 | 2.54 | 8.64 | 14.39 | 10.00 | 84.4 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 5.06 | 14.77 | 24.40 | 9.00 | 94.6 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 4.96 | 13.19 | 21.01 | 8.00 | 96.3 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.12 | 11.52 | 18.37 | 7.00 | 86.5 | 90.0 |
| XI | Bench | Kieran Trippier | DEF | 15 | 6.9 | 3.25 | 10.74 | 19.12 | 0.00 | 66.3 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.1 | 3.66 | 10.63 | 17.29 | 6.00 | 86.8 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.54 | 10.50 | 17.04 | 2.00 | 82.8 | 90.0 |
| Bench 3 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 2.72 | 8.91 | 14.34 | 1.00 | 56.4 | 30.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.57 | 7.51 | 11.93 | 2.00 | 66.7 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 7.85 | 22.73 | 37.07 | 3.00 | 118.0 | 90.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.6 | 7.35 | 19.92 | 32.31 | 2.00 | 123.4 | 87.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 6.57 | 18.64 | 29.83 | 3.00 | 103.3 | 88.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.52 | 10.24 | 17.07 | 14.00 | 67.5 | 90.0 |
| Bench 2 | Autosub In | Hwang Hee-chan | MID | 20 | 5.7 | 2.83 | 9.00 | 14.92 | 2.00 | 67.6 | 90.0 |

## GW18

- Train rows: 116314
- Bank: 0.20 -> 1.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Son Heung-min
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 64.29
- Actual score: 45.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.05) beats the best remaining Triple Captain opportunity (8.56).
- Transfer: Hwang Hee-chan -> Scott McTominay (projected gain 0.05, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (6.05) beats the best remaining Triple Captain opportunity (8.56).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | André Onana | GK | 14 | 4.8 | 3.28 | 9.98 | 16.74 | 2.00 | 91.8 | 90.0 |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.59 | 9.98 | 16.24 | 1.00 | 90.9 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.52 | 14.04 | 23.49 | 5.00 | 84.3 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 4.81 | 12.78 | 20.10 | 2.00 | 84.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 3.59 | 11.05 | 17.74 | 2.00 | 90.1 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 3.73 | 10.84 | 18.49 | 2.00 | 57.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.1 | 3.34 | 10.45 | 17.15 | 2.00 | 84.8 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.48 | 10.30 | 16.75 | 1.00 | 75.4 | 85.0 |
| Bench 3 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 2.69 | 7.85 | 13.11 | 2.00 | 41.9 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.55 | 7.62 | 12.15 | 8.00 | 75.8 | 89.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.74 | 20.81 | 34.28 | 7.00 | 101.2 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 5.89 | 18.16 | 29.10 | 1.00 | 97.7 | 90.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.7 | 6.09 | 17.37 | 27.86 | 7.00 | 89.2 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 5.03 | 13.50 | 21.36 | 1.00 | 98.3 | 90.0 |
| Bench 2 | Bench | Scott McTominay | MID | 14 | 4.9 | 3.26 | 9.46 | 15.12 | 2.00 | 80.0 | 90.0 |

## GW19

- Train rows: 117083
- Bank: 1.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 71.44
- Actual score: 63.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (12.34) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Scott McTominay -> Bruno Guimarães Rodriguez Moura (projected gain 0.05, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (12.34) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.22 | 9.56 | 15.91 | 1.00 | 93.2 | 90.0 |
| Bench 1 | Bench Boost | Bernd Leno | GK | 10 | 4.7 | 2.85 | 8.48 | 14.25 | 0.00 | 80.2 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.2 | 5.49 | 15.77 | 25.64 | 8.00 | 98.3 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 4.63 | 13.23 | 21.83 | 1.00 | 80.8 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 3.99 | 11.77 | 18.74 | 5.00 | 81.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.28 | 11.42 | 18.16 | 1.00 | 92.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.1 | 3.61 | 10.49 | 17.20 | 7.00 | 84.2 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.7 | 3.28 | 9.58 | 15.70 | 5.00 | 68.9 | 90.0 |
| Bench 3 | Bench Boost | Cameron Archer | FWD | 17 | 4.6 | 3.10 | 8.32 | 13.43 | 5.00 | 75.9 | 85.0 |
| Bench 4 | Bench Boost | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 2.91 | 8.25 | 13.29 | 16.00 | 59.9 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.2 | 7.31 | 21.27 | 35.39 | 3.00 | 107.6 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.39 | 17.77 | 28.50 | 2.00 | 97.6 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 5.98 | 17.77 | 29.11 | 5.00 | 100.7 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 3.60 | 11.08 | 17.92 | 0.00 | 66.4 | 0.0 |
| Bench 2 | Bench Boost | Bruno Guimarães Rodriguez Moura | MID | 15 | 5.8 | 3.49 | 9.90 | 16.02 | 1.00 | 81.1 | 90.0 |