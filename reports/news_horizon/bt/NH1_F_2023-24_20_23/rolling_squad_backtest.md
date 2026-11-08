# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 234.24
- Total actual points: 288.00
- Average predicted points: 58.56
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
- Predicted score: 63.04
- Actual score: 84.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.52 | 9.21 | 15.02 | 11.00 | 76.8 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.8 | 0.46 | 1.00 | 1.59 | 0.00 | 7.8 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 5.59 | 16.21 | 25.97 | 0.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.31 | 12.81 | 20.51 | 2.00 | 87.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.19 | 9.52 | 15.25 | 1.00 | 84.4 | 90.0 |
| Bench 4 | Bench | Auston Trusty | DEF | 17 | 3.9 | 1.94 | 6.26 | 9.93 | 1.00 | 77.4 | 90.0 |
| Bench 3 | Bench | Amari'i Bell | DEF | 12 | 3.9 | 1.98 | 5.53 | 9.06 | 1.00 | 61.8 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.86 | 15.99 | 25.42 | 8.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 5.03 | 14.04 | 21.93 | 7.00 | 83.6 | 90.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.5 | 2.38 | 7.77 | 12.37 | 1.00 | 71.0 | 23.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.3 | 7.64 | 21.06 | 34.37 | 16.00 | 90.0 | 90.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.9 | 5.92 | 17.50 | 28.74 | 9.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.45 | 16.16 | 26.33 | 7.00 | 85.8 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.17 | 15.29 | 24.71 | 3.00 | 90.0 | 90.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 3.72 | 9.79 | 15.84 | 4.00 | 75.8 | 90.0 |

## GW21

- Train rows: 118627
- Bank: 0.00 -> 1.90
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Phil Foden
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 57.64
- Actual score: 43.00
- Transfer: Son Heung-min -> Phil Foden (projected gain 11.21, hit 0)
- Autosub: Auston Trusty replaced Trent Alexander-Arnold.
- Autosub: Cameron Archer replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.96 | 10.74 | 17.63 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.8 | 0.00 | 0.58 | 1.24 | 2.00 | 7.4 | 82.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.49 | 13.50 | 21.85 | 6.00 | 90.0 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 3.85 | 12.55 | 20.90 | 0.00 | 71.7 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.45 | 9.58 | 15.50 | 17.00 | 87.2 | 80.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.42 | 6.45 | 10.37 | 1.00 | 75.1 | 79.0 |
| Bench 4 | Bench | Amari'i Bell | DEF | 12 | 3.9 | 2.32 | 6.20 | 10.27 | 2.00 | 70.2 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.02 | 16.99 | 26.82 | 1.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.20 | 12.82 | 20.19 | 2.00 | 66.3 | 90.0 |
| Bench 3 | Autosub In | Cameron Archer | FWD | 17 | 4.5 | 2.33 | 6.63 | 10.77 | 1.00 | 50.8 | 23.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 7.39 | 19.67 | 30.94 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 7.9 | 6.13 | 17.64 | 27.03 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 4.99 | 14.41 | 23.29 | 2.00 | 88.1 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.2 | 2.93 | 10.91 | 20.77 | 0.00 | 31.1 | 0.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 2.84 | 8.75 | 13.88 | 2.00 | 70.8 | 90.0 |

## GW22

- Train rows: 119414
- Bank: 1.90 -> 0.20
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: triple_captain
- Predicted score: 56.57
- Actual score: 72.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.03) beats the best remaining Triple Captain opportunity (6.84).
- Transfer: Auston Trusty -> William Saliba (projected gain 4.48, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (6.03) beats the best remaining Triple Captain opportunity (6.84).
- Autosub: Amari'i Bell replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.44 | 9.51 | 15.82 | 3.00 | 79.6 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.8 | 1.35 | 3.25 | 5.31 | 0.00 | 35.7 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.39 | 12.76 | 20.92 | 1.00 | 82.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.98 | 10.78 | 17.32 | 2.00 | 82.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.28 | 9.53 | 15.76 | 2.00 | 70.5 | 90.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 2.32 | 9.23 | 16.68 | 1.00 | 29.7 | 22.0 |
| Bench 2 | Autosub In | Amari'i Bell | DEF | 12 | 3.9 | 2.39 | 6.31 | 10.37 | 6.00 | 72.1 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.13 | 14.79 | 23.87 | 7.00 | 80.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.44 | 12.93 | 20.40 | 13.00 | 63.3 | 86.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.4 | 1.98 | 5.91 | 10.06 | 1.00 | 43.9 | 3.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 6.03 | 16.92 | 26.93 | 10.00 | 79.6 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.1 | 3.41 | 12.58 | 22.86 | 0.00 | 24.6 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 4.01 | 12.11 | 20.49 | 1.00 | 66.7 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 3.64 | 11.98 | 18.98 | 6.00 | 45.0 | 76.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 2.76 | 8.36 | 13.78 | 1.00 | 70.9 | 90.0 |

## GW23

- Train rows: 120213
- Bank: 0.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Bukayo Saka
- Effective captain: Ollie Watkins
- Chip used: bench_boost
- Predicted score: 56.98
- Actual score: 89.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.95) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.95) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.13 | 9.54 | 15.59 | 1.00 | 81.9 | 45.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.8 | 0.50 | 1.37 | 2.48 | 0.00 | 15.0 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.07 | 12.02 | 19.70 | 1.00 | 80.8 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 2.97 | 10.28 | 17.34 | 1.00 | 51.8 | 57.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.48 | 10.25 | 16.53 | 1.00 | 82.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.00 | 9.72 | 15.62 | -1.00 | 81.4 | 90.0 |
| Bench 3 | Bench Boost | Amari'i Bell | DEF | 12 | 3.9 | 2.19 | 6.74 | 10.78 | 0.00 | 71.2 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.8 | 5.79 | 16.17 | 26.00 | 18.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.89 | 13.24 | 21.80 | 2.00 | 68.0 | 90.0 |
| Bench 4 | Bench Boost | Cameron Archer | FWD | 17 | 4.3 | 1.38 | 4.44 | 8.14 | 1.00 | 30.7 | 25.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 5.57 | 16.60 | 26.56 | 9.00 | 85.2 | 78.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 4.35 | 12.91 | 21.22 | 20.00 | 65.4 | 90.0 |
| XI | XI | Mohamed Salah | MID | 11 | 13.0 | 3.07 | 12.17 | 21.61 | 0.00 | 25.7 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 3.92 | 11.81 | 20.29 | 2.00 | 73.1 | 90.0 |
| Bench 2 | Bench Boost | Alejandro Garnacho | MID | 14 | 4.8 | 2.88 | 9.00 | 14.28 | 16.00 | 68.9 | 90.0 |