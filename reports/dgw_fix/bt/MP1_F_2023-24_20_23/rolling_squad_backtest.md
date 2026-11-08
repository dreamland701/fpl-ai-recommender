# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 234.15
- Total actual points: 289.00
- Average predicted points: 58.54
- Average actual points: 72.25
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
- Predicted score: 63.23
- Actual score: 84.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.59 | 9.39 | 15.26 | 11.00 | 78.4 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.8 | 0.23 | 0.39 | 0.60 | 0.00 | 2.6 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 5.52 | 16.06 | 25.74 | 0.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.39 | 12.97 | 20.74 | 2.00 | 89.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.14 | 9.42 | 15.12 | 1.00 | 83.0 | 90.0 |
| Bench 4 | Bench | Auston Trusty | DEF | 17 | 3.9 | 1.90 | 6.23 | 9.93 | 1.00 | 76.6 | 90.0 |
| Bench 3 | Bench | Amari'i Bell | DEF | 12 | 3.9 | 1.95 | 5.45 | 8.95 | 1.00 | 61.2 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.91 | 16.17 | 25.75 | 8.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 5.12 | 14.20 | 22.12 | 7.00 | 85.7 | 90.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.5 | 2.37 | 7.82 | 12.52 | 1.00 | 70.8 | 23.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.3 | 7.61 | 21.08 | 34.44 | 16.00 | 90.0 | 90.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.9 | 5.95 | 17.59 | 28.90 | 9.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.52 | 16.37 | 26.65 | 7.00 | 87.5 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.17 | 15.25 | 24.61 | 3.00 | 90.0 | 90.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 3.70 | 9.73 | 15.73 | 4.00 | 75.5 | 90.0 |

## GW21

- Train rows: 118627
- Bank: 0.00 -> 1.90
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Phil Foden
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 58.18
- Actual score: 44.00
- Transfer: Son Heung-min -> Phil Foden (projected gain 11.48, hit 0)
- Autosub: Auston Trusty replaced Trent Alexander-Arnold.
- Autosub: Amari'i Bell replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 4.12 | 11.06 | 18.07 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.8 | 0.00 | 0.00 | 0.23 | 2.00 | 2.2 | 82.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.63 | 13.78 | 22.23 | 6.00 | 90.0 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 3.62 | 12.09 | 20.26 | 0.00 | 66.6 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.43 | 9.60 | 15.58 | 17.00 | 86.7 | 80.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.37 | 6.41 | 10.36 | 1.00 | 74.1 | 79.0 |
| Bench 3 | Autosub In | Amari'i Bell | DEF | 12 | 3.9 | 2.31 | 6.22 | 10.32 | 2.00 | 70.1 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.07 | 17.13 | 27.02 | 1.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.20 | 12.81 | 20.18 | 2.00 | 66.2 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.5 | 2.22 | 6.48 | 10.65 | 1.00 | 48.4 | 23.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 7.57 | 20.01 | 31.40 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 7.9 | 6.29 | 17.87 | 27.22 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 4.96 | 14.29 | 23.06 | 2.00 | 87.4 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.2 | 2.93 | 11.15 | 21.38 | 0.00 | 31.3 | 0.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 2.80 | 8.67 | 13.78 | 2.00 | 70.0 | 90.0 |

## GW22

- Train rows: 119414
- Bank: 1.90 -> 0.20
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: triple_captain
- Predicted score: 56.25
- Actual score: 72.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.08) beats the best remaining Triple Captain opportunity (6.89).
- Transfer: Auston Trusty -> William Saliba (projected gain 4.59, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (6.08) beats the best remaining Triple Captain opportunity (6.89).
- Autosub: Amari'i Bell replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.52 | 9.66 | 16.04 | 3.00 | 81.4 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.8 | 1.31 | 2.99 | 4.78 | 0.00 | 34.7 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.44 | 12.90 | 21.15 | 1.00 | 84.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.98 | 10.88 | 17.56 | 2.00 | 82.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.72 | 10.11 | 16.31 | 2.00 | 80.3 | 90.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 2.27 | 8.81 | 15.88 | 1.00 | 28.7 | 22.0 |
| Bench 2 | Autosub In | Amari'i Bell | DEF | 12 | 3.9 | 2.37 | 6.31 | 10.39 | 6.00 | 71.7 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.09 | 14.80 | 23.95 | 7.00 | 79.2 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.42 | 12.93 | 20.45 | 13.00 | 62.7 | 86.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.4 | 1.92 | 5.88 | 10.13 | 1.00 | 42.7 | 3.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 6.08 | 17.07 | 27.21 | 10.00 | 80.6 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.1 | 2.93 | 11.72 | 22.02 | 0.00 | 14.1 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 3.47 | 11.65 | 18.57 | 6.00 | 41.3 | 76.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 3.75 | 11.63 | 19.95 | 1.00 | 61.0 | 90.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 2.68 | 8.22 | 13.62 | 1.00 | 69.1 | 90.0 |

## GW23

- Train rows: 120213
- Bank: 0.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Bukayo Saka
- Effective captain: Ollie Watkins
- Chip used: bench_boost
- Predicted score: 56.49
- Actual score: 89.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.51) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.51) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.19 | 9.61 | 15.66 | 1.00 | 83.1 | 45.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.8 | 0.31 | 0.86 | 1.63 | 0.00 | 10.8 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.12 | 12.16 | 19.95 | 1.00 | 82.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.47 | 10.32 | 16.71 | 1.00 | 81.9 | 90.0 |
| Bench 2 | Bench Boost | Trent Alexander-Arnold | DEF | 11 | 8.4 | 2.74 | 9.82 | 16.75 | 1.00 | 46.6 | 57.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 2.94 | 9.65 | 15.55 | -1.00 | 80.1 | 90.0 |
| Bench 3 | Bench Boost | Amari'i Bell | DEF | 12 | 3.9 | 2.14 | 6.65 | 10.66 | 0.00 | 70.2 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.8 | 5.79 | 16.25 | 26.22 | 18.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.86 | 13.24 | 21.88 | 2.00 | 67.2 | 90.0 |
| Bench 4 | Bench Boost | Cameron Archer | FWD | 17 | 4.3 | 1.31 | 4.39 | 8.19 | 1.00 | 29.3 | 25.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 5.59 | 16.75 | 26.86 | 9.00 | 85.8 | 78.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 4.21 | 12.67 | 20.98 | 20.00 | 62.3 | 90.0 |
| XI | XI | Mohamed Salah | MID | 11 | 13.0 | 3.44 | 12.65 | 21.80 | 0.00 | 33.9 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 3.78 | 11.57 | 20.04 | 2.00 | 70.0 | 90.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 2.81 | 8.86 | 14.11 | 16.00 | 67.3 | 90.0 |