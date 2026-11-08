# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 237.61
- Total actual points: 288.00
- Average predicted points: 59.40
- Average actual points: 72.00
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW19 are included before the first simulated week.
- League-average scores were not available for this run.

## GW20

- Train rows: 117854
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Son Heung-min
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 63.87
- Actual score: 84.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.44 | 9.22 | 15.01 | 11.00 | 76.6 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.8 | 0.47 | 0.96 | 1.46 | 0.00 | 7.6 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 5.82 | 16.22 | 25.99 | 0.00 | 95.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.48 | 12.82 | 20.51 | 2.00 | 91.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.20 | 9.54 | 15.31 | 1.00 | 85.2 | 90.0 |
| Bench 4 | Bench | Auston Trusty | DEF | 17 | 3.9 | 1.93 | 6.29 | 10.02 | 1.00 | 77.6 | 90.0 |
| Bench 3 | Bench | Amari'i Bell | DEF | 12 | 3.9 | 1.97 | 5.53 | 9.05 | 1.00 | 62.1 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.86 | 16.03 | 25.51 | 8.00 | 97.1 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 5.39 | 14.01 | 21.83 | 7.00 | 89.7 | 90.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.5 | 2.43 | 7.81 | 12.51 | 1.00 | 71.1 | 23.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.3 | 7.57 | 21.09 | 34.44 | 16.00 | 103.6 | 90.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.9 | 5.89 | 17.52 | 28.79 | 9.00 | 96.1 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.42 | 16.18 | 26.36 | 7.00 | 87.5 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.36 | 15.29 | 24.67 | 3.00 | 96.4 | 90.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 3.86 | 9.80 | 15.84 | 4.00 | 76.5 | 90.0 |

## GW21

- Train rows: 118627
- Bank: 0.00 -> 1.90
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Phil Foden
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 59.29
- Actual score: 43.00
- Transfer: Son Heung-min -> Phil Foden (projected gain 11.01, hit 0)
- Autosub: Cameron Archer replaced Trent Alexander-Arnold.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.99 | 10.74 | 17.59 | 3.00 | 92.6 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.8 | 0.00 | 0.54 | 1.10 | 2.00 | 7.3 | 82.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.74 | 13.49 | 21.78 | 6.00 | 100.1 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 3.75 | 12.59 | 21.03 | 0.00 | 70.5 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.44 | 9.61 | 15.60 | 17.00 | 87.6 | 80.0 |
| XI | XI | Auston Trusty | DEF | 17 | 3.9 | 2.43 | 6.48 | 10.47 | 1.00 | 75.6 | 79.0 |
| Bench 3 | Bench | Amari'i Bell | DEF | 12 | 3.9 | 2.32 | 6.22 | 10.32 | 2.00 | 70.7 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.11 | 17.01 | 26.84 | 1.00 | 100.7 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.46 | 12.88 | 20.29 | 2.00 | 69.3 | 90.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 4.5 | 2.39 | 6.69 | 10.97 | 1.00 | 51.7 | 23.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 7.74 | 19.66 | 30.86 | 3.00 | 116.1 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 7.9 | 6.83 | 17.57 | 26.78 | 2.00 | 113.4 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 5.13 | 14.42 | 23.24 | 2.00 | 90.5 | 90.0 |
| Bench 4 | Bench | Mohamed Salah | MID | 11 | 13.2 | 1.94 | 11.18 | 21.42 | 0.00 | 13.9 | 0.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 2.93 | 8.77 | 13.93 | 2.00 | 71.4 | 90.0 |

## GW22

- Train rows: 119414
- Bank: 1.90 -> 0.20
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: triple_captain
- Predicted score: 57.43
- Actual score: 72.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.17) beats the best remaining Triple Captain opportunity (7.00).
- Transfer: Auston Trusty -> William Saliba (projected gain 4.52, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (6.17) beats the best remaining Triple Captain opportunity (7.00).
- Autosub: Amari'i Bell replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.39 | 9.51 | 15.81 | 3.00 | 78.6 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.8 | 1.36 | 3.18 | 5.08 | 0.00 | 35.3 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.56 | 12.78 | 20.96 | 1.00 | 85.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.97 | 10.84 | 17.50 | 2.00 | 83.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.30 | 8.96 | 14.53 | 2.00 | 69.4 | 90.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 2.29 | 8.61 | 15.57 | 1.00 | 27.8 | 22.0 |
| Bench 2 | Autosub In | Amari'i Bell | DEF | 12 | 3.9 | 2.40 | 6.33 | 10.44 | 6.00 | 72.3 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 4.99 | 14.83 | 24.01 | 7.00 | 79.1 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.68 | 13.00 | 20.57 | 13.00 | 66.9 | 86.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.4 | 1.97 | 5.94 | 10.22 | 1.00 | 41.7 | 3.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 6.17 | 16.98 | 27.08 | 10.00 | 82.8 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.1 | 3.42 | 12.61 | 23.38 | 0.00 | 22.6 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 3.96 | 12.12 | 20.68 | 1.00 | 63.3 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 3.82 | 12.06 | 19.19 | 6.00 | 46.7 | 76.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 2.81 | 8.39 | 13.87 | 1.00 | 71.4 | 90.0 |

## GW23

- Train rows: 120213
- Bank: 0.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Bukayo Saka
- Effective captain: Ollie Watkins
- Chip used: bench_boost
- Predicted score: 57.02
- Actual score: 89.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.78) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.78) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.05 | 9.52 | 15.54 | 1.00 | 80.9 | 45.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.8 | 0.53 | 1.34 | 2.36 | 0.00 | 14.6 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.14 | 12.04 | 19.76 | 1.00 | 83.3 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.39 | 10.30 | 16.68 | 1.00 | 83.0 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 2.92 | 10.28 | 17.45 | 1.00 | 50.8 | 57.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.03 | 9.75 | 15.71 | -1.00 | 82.7 | 90.0 |
| Bench 3 | Bench Boost | Amari'i Bell | DEF | 12 | 3.9 | 2.21 | 6.76 | 10.83 | 0.00 | 71.7 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.8 | 5.75 | 16.19 | 26.12 | 18.00 | 92.7 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 5.02 | 13.32 | 22.03 | 2.00 | 68.4 | 90.0 |
| Bench 4 | Bench Boost | Cameron Archer | FWD | 17 | 4.3 | 1.18 | 4.46 | 8.29 | 1.00 | 25.3 | 25.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 5.51 | 16.67 | 26.74 | 9.00 | 87.0 | 78.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 4.32 | 12.92 | 21.36 | 20.00 | 64.3 | 90.0 |
| XI | XI | Mohamed Salah | MID | 11 | 13.0 | 3.55 | 12.58 | 21.67 | 0.00 | 35.8 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 3.79 | 11.82 | 20.43 | 2.00 | 70.1 | 90.0 |
| Bench 2 | Bench Boost | Alejandro Garnacho | MID | 14 | 4.8 | 2.86 | 9.00 | 14.30 | 16.00 | 68.6 | 90.0 |