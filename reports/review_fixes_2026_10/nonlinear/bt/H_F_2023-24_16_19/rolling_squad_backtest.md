# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 235.95
- Total actual points: 229.00
- Average predicted points: 58.99
- Average actual points: 57.25
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
- Vice captain: Bruno Borges Fernandes
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.49
- Actual score: 62.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.62 | 11.48 | 20.62 | 9.00 | 87.8 | 90.0 |
| Bench 1 | Bench | Emiliano Martínez Romero | GK | 2 | 5.0 | 2.87 | 11.04 | 19.82 | 10.00 | 89.5 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.35 | 14.19 | 21.55 | -1.00 | 86.6 | 85.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.68 | 12.12 | 22.54 | 4.00 | 85.1 | 90.0 |
| Bench 3 | Bench | Ethan Pinnock | DEF | 4 | 4.6 | 3.56 | 11.63 | 16.40 | 2.00 | 85.2 | 90.0 |
| XI | XI | Diogo Dalot Teixeira | DEF | 14 | 5.0 | 3.80 | 10.36 | 17.43 | 1.00 | 84.4 | 90.0 |
| Bench 2 | Bench | Pedro Porro | DEF | 18 | 5.3 | 3.56 | 10.33 | 18.47 | 5.00 | 86.6 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 6.5 | 3.74 | 12.98 | 19.58 | 7.00 | 82.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.89 | 11.55 | 17.76 | 9.00 | 81.6 | 90.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 3.45 | 11.10 | 18.76 | 2.00 | 68.1 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.73 | 22.14 | 40.24 | 13.00 | 74.1 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 4.10 | 16.15 | 23.88 | 2.00 | 86.3 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.7 | 4.11 | 14.56 | 22.67 | 2.00 | 86.5 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 5.20 | 13.68 | 25.42 | 1.00 | 84.5 | 90.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 4.56 | 12.97 | 23.02 | 2.00 | 78.0 | 78.0 |

## GW17

- Train rows: 115549
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Mohamed Salah
- Effective captain: Bukayo Saka
- Chip used: bench_boost
- Predicted score: 62.19
- Actual score: 48.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.83) beats the best remaining Bench Boost opportunity (8.83).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.83) beats the best remaining Bench Boost opportunity (8.83).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench Boost | Bernd Leno | GK | 10 | 4.7 | 3.24 | 10.85 | 18.76 | 3.00 | 88.4 | 90.0 |
| XI | XI | Emiliano Martínez Romero | GK | 2 | 5.0 | 3.40 | 9.65 | 17.80 | 1.00 | 86.8 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 4.90 | 14.43 | 18.80 | 8.00 | 84.7 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.33 | 14.14 | 22.86 | 9.00 | 88.4 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 4.08 | 12.57 | 20.82 | 0.00 | 68.6 | 0.0 |
| XI | XI | Ethan Pinnock | DEF | 4 | 4.6 | 3.15 | 7.95 | 13.75 | 1.00 | 81.5 | 90.0 |
| Bench 2 | Bench Boost | Diogo Dalot Teixeira | DEF | 14 | 5.0 | 2.20 | 7.62 | 11.21 | 3.00 | 76.9 | 90.0 |
| Bench 4 | Bench Boost | Dominic Solanke | FWD | 3 | 6.5 | 0.08 | 10.47 | 16.70 | 0.00 | 0.5 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.44 | 10.11 | 19.43 | 2.00 | 83.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 2.63 | 7.76 | 15.74 | 1.00 | 69.3 | 30.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.1 | 6.97 | 20.66 | 39.73 | 3.00 | 86.8 | 90.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 8.9 | 7.29 | 17.85 | 28.77 | 3.00 | 86.8 | 88.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.7 | 4.24 | 13.29 | 24.68 | 8.00 | 83.5 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 3.06 | 10.54 | 17.70 | 0.00 | 75.2 | 0.0 |
| Bench 3 | Bench Boost | Alejandro Garnacho | MID | 14 | 4.8 | 1.89 | 10.38 | 15.30 | 3.00 | 61.5 | 70.0 |

## GW18

- Train rows: 116314
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Dominic Solanke
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 56.12
- Actual score: 54.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.59 | 9.86 | 18.16 | 1.00 | 87.5 | 90.0 |
| Bench 1 | Bench | Emiliano Martínez Romero | GK | 2 | 5.0 | 3.36 | 8.32 | 15.96 | 2.00 | 84.8 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 4.60 | 14.33 | 23.23 | 2.00 | 77.1 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 3.48 | 12.64 | 17.64 | 2.00 | 85.3 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.90 | 12.24 | 23.69 | 5.00 | 86.9 | 90.0 |
| Bench 3 | Bench | Diogo Dalot Teixeira | DEF | 14 | 5.0 | 2.51 | 6.83 | 12.30 | 0.00 | 67.5 | 0.0 |
| Bench 4 | Bench | Ethan Pinnock | DEF | 4 | 4.6 | 0.00 | 6.69 | 11.06 | 0.00 | 1.4 | 0.0 |
| Vice Captain | XI | Dominic Solanke | FWD | 3 | 6.6 | 5.26 | 18.66 | 26.28 | 17.00 | 84.4 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.88 | 11.38 | 16.97 | 1.00 | 83.0 | 85.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 3.42 | 10.21 | 15.14 | 2.00 | 68.7 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 7.80 | 25.14 | 35.86 | 7.00 | 86.8 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 3.49 | 15.71 | 27.52 | 1.00 | 83.4 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.7 | 4.64 | 14.82 | 20.98 | 8.00 | 86.7 | 87.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.2 | 3.26 | 12.06 | 18.40 | 1.00 | 67.2 | 90.0 |
| Bench 2 | Bench | Alejandro Garnacho | MID | 14 | 4.8 | 2.76 | 10.10 | 15.05 | 2.00 | 56.5 | 84.0 |

## GW19

- Train rows: 117083
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Mohamed Salah
- Effective captain: Bukayo Saka
- Chip used: triple_captain
- Predicted score: 62.14
- Actual score: 65.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.35) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (6.35) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 2.82 | 10.05 | 17.61 | 0.00 | 83.7 | 90.0 |
| Bench 1 | Bench | Emiliano Martínez Romero | GK | 2 | 5.1 | 2.17 | 8.69 | 14.05 | 2.00 | 84.5 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 4.52 | 14.43 | 23.79 | 1.00 | 78.4 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.2 | 3.97 | 13.59 | 25.42 | 8.00 | 88.3 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 3.49 | 10.20 | 16.21 | 5.00 | 86.6 | 90.0 |
| Bench 4 | Bench | Diogo Dalot Teixeira | DEF | 14 | 5.0 | 1.74 | 6.05 | 10.35 | 1.00 | 50.2 | 90.0 |
| Bench 3 | Bench | Ethan Pinnock | DEF | 4 | 4.6 | 2.69 | 5.35 | 8.80 | 0.00 | 74.1 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 6.7 | 5.75 | 14.48 | 25.62 | 6.00 | 83.2 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.7 | 3.56 | 9.76 | 14.66 | 5.00 | 78.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 4.08 | 8.84 | 12.03 | 16.00 | 65.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.2 | 6.20 | 19.17 | 37.88 | 3.00 | 88.0 | 90.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 8.9 | 6.35 | 16.33 | 25.84 | 2.00 | 84.8 | 90.0 |
| Bench 2 | Bench | Jarrod Bowen | MID | 19 | 7.7 | 3.48 | 13.09 | 21.99 | 6.00 | 85.4 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.2 | 4.64 | 11.37 | 16.78 | 1.00 | 79.9 | 90.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.7 | 4.07 | 10.51 | 16.43 | 14.00 | 71.7 | 90.0 |