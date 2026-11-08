# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 235.59
- Total actual points: 279.00
- Average predicted points: 58.90
- Average actual points: 69.75
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
- Predicted score: 63.11
- Actual score: 84.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.54 | 9.17 | 14.82 | 11.00 | 78.7 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.8 | 0.42 | 0.86 | 1.37 | 0.00 | 7.1 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 5.59 | 16.22 | 25.99 | 0.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.33 | 12.82 | 20.51 | 2.00 | 88.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.19 | 9.54 | 15.31 | 1.00 | 84.3 | 90.0 |
| Bench 4 | Bench | Auston Trusty | DEF | 17 | 3.9 | 1.94 | 6.24 | 9.83 | 1.00 | 78.8 | 90.0 |
| Bench 3 | Bench | Amari'i Bell | DEF | 12 | 3.9 | 2.07 | 5.77 | 9.53 | 1.00 | 65.5 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.85 | 16.03 | 25.51 | 8.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 5.04 | 14.01 | 21.83 | 7.00 | 83.8 | 90.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.5 | 2.45 | 8.06 | 12.98 | 1.00 | 74.4 | 23.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.3 | 7.63 | 21.09 | 34.44 | 16.00 | 90.0 | 90.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.9 | 5.92 | 17.52 | 28.79 | 9.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.45 | 16.18 | 26.36 | 7.00 | 85.9 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.19 | 15.29 | 24.67 | 3.00 | 90.0 | 90.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 3.74 | 9.75 | 15.65 | 4.00 | 77.8 | 90.0 |

## GW21

- Train rows: 118627
- Bank: 0.00 -> 1.90
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Phil Foden
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 58.01
- Actual score: 43.00
- Transfer: Son Heung-min -> Phil Foden (projected gain 10.43, hit 0)
- Autosub: Auston Trusty replaced Trent Alexander-Arnold.
- Autosub: Cameron Archer replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.99 | 10.74 | 17.59 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.8 | 0.00 | 0.44 | 1.01 | 2.00 | 6.7 | 82.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.50 | 13.49 | 21.78 | 6.00 | 90.0 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 3.93 | 12.83 | 21.50 | 0.00 | 75.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.43 | 9.61 | 15.60 | 17.00 | 86.9 | 80.0 |
| Bench 4 | Bench | Amari'i Bell | DEF | 12 | 3.9 | 2.40 | 6.46 | 10.79 | 2.00 | 73.8 | 90.0 |
| Bench 3 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.42 | 6.44 | 10.28 | 1.00 | 76.6 | 79.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.03 | 17.01 | 26.84 | 1.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.31 | 13.12 | 20.75 | 2.00 | 70.3 | 90.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 4.5 | 2.50 | 7.17 | 11.74 | 1.00 | 55.2 | 23.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 7.41 | 19.66 | 30.86 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 7.9 | 6.16 | 17.57 | 26.78 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 5.01 | 14.42 | 23.24 | 2.00 | 88.6 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.2 | 2.90 | 11.08 | 21.33 | 0.00 | 30.9 | 0.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 2.93 | 9.01 | 14.40 | 2.00 | 74.5 | 90.0 |

## GW22

- Train rows: 119414
- Bank: 1.90 -> 4.70
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: triple_captain
- Predicted score: 56.54
- Actual score: 72.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.04) beats the best remaining Triple Captain opportunity (6.85).
- Transfer: Trent Alexander-Arnold -> William Saliba (projected gain 4.58, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (6.04) beats the best remaining Triple Captain opportunity (6.85).
- Autosub: Amari'i Bell replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.46 | 9.47 | 15.60 | 3.00 | 81.6 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.8 | 1.33 | 3.09 | 4.98 | 0.00 | 35.3 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.39 | 12.78 | 20.96 | 1.00 | 82.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.96 | 10.84 | 17.50 | 2.00 | 82.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.31 | 9.21 | 15.01 | 2.00 | 73.0 | 90.0 |
| Bench 3 | Bench | Auston Trusty | DEF | 17 | 3.9 | 2.25 | 6.47 | 10.50 | 0.00 | 72.3 | 90.0 |
| Bench 2 | Autosub In | Amari'i Bell | DEF | 12 | 3.9 | 2.40 | 6.29 | 10.22 | 6.00 | 73.8 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.13 | 14.79 | 23.79 | 7.00 | 81.5 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.53 | 13.24 | 21.04 | 13.00 | 67.1 | 86.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.4 | 1.89 | 5.84 | 10.12 | 1.00 | 42.2 | 3.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 6.04 | 16.93 | 26.86 | 10.00 | 81.3 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.1 | 3.20 | 12.51 | 23.28 | 0.00 | 20.3 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 4.03 | 12.37 | 21.16 | 1.00 | 69.0 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 3.58 | 11.96 | 19.09 | 6.00 | 43.9 | 76.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 2.84 | 8.63 | 14.35 | 1.00 | 74.5 | 90.0 |

## GW23

- Train rows: 120213
- Bank: 4.70 -> 3.70
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Bukayo Saka
- Effective captain: Ollie Watkins
- Chip used: bench_boost
- Predicted score: 57.94
- Actual score: 80.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.32) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Alejandro Garnacho -> Cole Palmer (projected gain 3.51, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.32) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.14 | 9.52 | 15.54 | 1.00 | 82.1 | 45.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.8 | 0.46 | 1.24 | 2.26 | 0.00 | 14.4 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.06 | 12.04 | 19.76 | 1.00 | 80.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.47 | 10.30 | 16.68 | 1.00 | 81.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 2.99 | 9.75 | 15.71 | -1.00 | 81.2 | 90.0 |
| Bench 3 | Bench Boost | Amari'i Bell | DEF | 12 | 3.9 | 2.27 | 7.00 | 11.30 | 0.00 | 75.0 | 90.0 |
| Bench 2 | Bench Boost | Auston Trusty | DEF | 17 | 3.9 | 2.30 | 6.14 | 9.72 | 0.00 | 74.1 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.8 | 5.76 | 16.19 | 26.12 | 18.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.97 | 13.56 | 22.50 | 2.00 | 71.7 | 90.0 |
| Bench 4 | Bench Boost | Cameron Archer | FWD | 17 | 4.3 | 1.29 | 4.36 | 8.19 | 1.00 | 29.0 | 25.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 5.56 | 16.67 | 26.74 | 9.00 | 85.0 | 78.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 4.40 | 13.16 | 21.83 | 20.00 | 68.5 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.8 | 4.28 | 12.74 | 20.45 | 8.00 | 82.7 | 90.0 |
| XI | XI | Mohamed Salah | MID | 11 | 13.0 | 3.33 | 12.48 | 21.57 | 0.00 | 31.8 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 3.89 | 11.77 | 20.21 | 2.00 | 74.0 | 90.0 |