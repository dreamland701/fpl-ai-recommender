# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 234.18
- Total actual points: 289.00
- Average predicted points: 58.55
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
- Predicted score: 63.09
- Actual score: 84.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.53 | 9.22 | 15.01 | 11.00 | 77.1 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.8 | 0.48 | 0.96 | 1.46 | 0.00 | 8.1 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 5.59 | 16.22 | 25.99 | 0.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.33 | 12.82 | 20.51 | 2.00 | 88.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.19 | 9.54 | 15.31 | 1.00 | 84.3 | 90.0 |
| Bench 4 | Bench | Auston Trusty | DEF | 17 | 3.9 | 1.93 | 6.29 | 10.02 | 1.00 | 77.1 | 90.0 |
| Bench 3 | Bench | Amari'i Bell | DEF | 12 | 3.9 | 1.98 | 5.53 | 9.05 | 1.00 | 61.7 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.85 | 16.03 | 25.51 | 8.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 5.04 | 14.01 | 21.83 | 7.00 | 83.8 | 90.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.5 | 2.36 | 7.81 | 12.51 | 1.00 | 70.7 | 23.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.3 | 7.63 | 21.09 | 34.44 | 16.00 | 90.0 | 90.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.9 | 5.92 | 17.52 | 28.79 | 9.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.45 | 16.18 | 26.36 | 7.00 | 85.9 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.19 | 15.29 | 24.67 | 3.00 | 90.0 | 90.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 3.73 | 9.80 | 15.84 | 4.00 | 76.1 | 90.0 |

## GW21

- Train rows: 118627
- Bank: 0.00 -> 1.90
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Phil Foden
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 57.79
- Actual score: 44.00
- Transfer: Son Heung-min -> Phil Foden (projected gain 30.68, hit 0)
- Autosub: Auston Trusty replaced Trent Alexander-Arnold.
- Autosub: Amari'i Bell replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.99 | 10.74 | 17.59 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.8 | 0.01 | 0.54 | 1.10 | 2.00 | 7.7 | 82.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.50 | 13.49 | 21.78 | 6.00 | 90.0 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 3.84 | 12.59 | 21.03 | 0.00 | 71.5 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.43 | 9.61 | 15.60 | 17.00 | 86.9 | 80.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.40 | 6.48 | 10.47 | 1.00 | 74.8 | 79.0 |
| Bench 3 | Autosub In | Amari'i Bell | DEF | 12 | 3.9 | 2.31 | 6.22 | 10.32 | 2.00 | 70.1 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.03 | 17.01 | 26.84 | 1.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.22 | 12.88 | 20.29 | 2.00 | 66.6 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.5 | 2.31 | 6.69 | 10.97 | 1.00 | 50.4 | 23.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 7.41 | 19.66 | 30.86 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 7.9 | 6.16 | 17.57 | 26.78 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 5.01 | 14.42 | 23.24 | 2.00 | 88.6 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.2 | 2.95 | 11.18 | 21.42 | 0.00 | 31.8 | 0.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 2.84 | 8.77 | 13.93 | 2.00 | 70.8 | 90.0 |

## GW22

- Train rows: 119414
- Bank: 1.90 -> 0.20
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: triple_captain
- Predicted score: 56.24
- Actual score: 72.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.03) beats the best remaining Triple Captain opportunity (6.84).
- Transfer: Auston Trusty -> William Saliba (projected gain 13.00, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (6.03) beats the best remaining Triple Captain opportunity (6.84).
- Autosub: Amari'i Bell replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.45 | 9.51 | 15.81 | 3.00 | 79.9 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.8 | 1.38 | 3.18 | 5.08 | 0.00 | 36.3 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.39 | 12.78 | 20.96 | 1.00 | 82.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.96 | 10.84 | 17.50 | 2.00 | 82.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.22 | 8.96 | 14.53 | 2.00 | 69.1 | 90.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 2.17 | 8.61 | 15.57 | 1.00 | 26.4 | 22.0 |
| Bench 2 | Autosub In | Amari'i Bell | DEF | 12 | 3.9 | 2.39 | 6.33 | 10.44 | 6.00 | 72.0 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.12 | 14.83 | 24.01 | 7.00 | 79.7 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.44 | 13.00 | 20.57 | 13.00 | 63.2 | 86.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.4 | 1.95 | 5.94 | 10.22 | 1.00 | 43.2 | 3.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 6.03 | 16.98 | 27.08 | 10.00 | 79.5 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.1 | 3.25 | 12.61 | 23.38 | 0.00 | 21.2 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 3.94 | 12.12 | 20.68 | 1.00 | 65.2 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 3.63 | 12.06 | 19.19 | 6.00 | 44.9 | 76.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 2.75 | 8.39 | 13.87 | 1.00 | 70.6 | 90.0 |

## GW23

- Train rows: 120213
- Bank: 0.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Bukayo Saka
- Effective captain: Ollie Watkins
- Chip used: bench_boost
- Predicted score: 57.07
- Actual score: 89.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.92) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.92) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.14 | 9.52 | 15.54 | 1.00 | 82.1 | 45.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.8 | 0.52 | 1.34 | 2.36 | 0.00 | 15.3 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.06 | 12.04 | 19.76 | 1.00 | 80.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.47 | 10.30 | 16.68 | 1.00 | 81.9 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 2.94 | 10.28 | 17.45 | 1.00 | 51.0 | 57.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 2.99 | 9.75 | 15.71 | -1.00 | 81.2 | 90.0 |
| Bench 3 | Bench Boost | Amari'i Bell | DEF | 12 | 3.9 | 2.19 | 6.76 | 10.83 | 0.00 | 71.2 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.8 | 5.76 | 16.19 | 26.12 | 18.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.88 | 13.32 | 22.03 | 2.00 | 67.8 | 90.0 |
| Bench 4 | Bench Boost | Cameron Archer | FWD | 17 | 4.3 | 1.34 | 4.46 | 8.29 | 1.00 | 30.0 | 25.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 5.56 | 16.67 | 26.74 | 9.00 | 85.0 | 78.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 4.31 | 12.92 | 21.36 | 20.00 | 64.7 | 90.0 |
| XI | XI | Mohamed Salah | MID | 11 | 13.0 | 3.38 | 12.58 | 21.67 | 0.00 | 32.8 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 3.88 | 11.82 | 20.43 | 2.00 | 72.2 | 90.0 |
| Bench 2 | Bench Boost | Alejandro Garnacho | MID | 14 | 4.8 | 2.87 | 9.00 | 14.30 | 16.00 | 68.7 | 90.0 |