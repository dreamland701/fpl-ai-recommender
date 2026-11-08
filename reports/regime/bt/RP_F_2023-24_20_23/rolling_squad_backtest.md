# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 234.37
- Total actual points: 289.00
- Average predicted points: 58.59
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
- Predicted score: 63.30
- Actual score: 84.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.50 | 9.11 | 14.78 | 11.00 | 74.3 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.8 | 0.53 | 1.11 | 1.71 | 0.00 | 5.6 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 5.71 | 16.61 | 26.68 | 0.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.36 | 12.93 | 20.71 | 2.00 | 88.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.19 | 9.53 | 15.32 | 1.00 | 85.7 | 90.0 |
| Bench 4 | Bench | Auston Trusty | DEF | 17 | 3.9 | 1.94 | 6.33 | 10.11 | 1.00 | 78.4 | 90.0 |
| Bench 3 | Bench | Amari'i Bell | DEF | 12 | 3.9 | 1.98 | 5.55 | 9.10 | 1.00 | 62.8 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.79 | 15.80 | 25.10 | 8.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.99 | 13.82 | 21.47 | 7.00 | 82.6 | 90.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.5 | 2.29 | 7.53 | 11.96 | 1.00 | 68.9 | 23.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.3 | 7.73 | 21.47 | 35.14 | 16.00 | 90.0 | 90.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.9 | 5.93 | 17.55 | 28.85 | 9.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.45 | 16.19 | 26.39 | 7.00 | 86.3 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.18 | 15.27 | 24.64 | 3.00 | 90.0 | 90.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 3.74 | 9.86 | 15.96 | 4.00 | 76.6 | 90.0 |

## GW21

- Train rows: 118627
- Bank: 0.00 -> 1.90
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Phil Foden
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 57.92
- Actual score: 44.00
- Transfer: Son Heung-min -> Phil Foden (projected gain 11.21, hit 0)
- Autosub: Auston Trusty replaced Trent Alexander-Arnold.
- Autosub: Amari'i Bell replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.95 | 10.61 | 17.32 | 3.00 | 89.2 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.8 | 0.06 | 0.70 | 1.36 | 2.00 | 5.2 | 82.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.51 | 13.53 | 21.86 | 6.00 | 90.0 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 3.94 | 12.95 | 21.69 | 0.00 | 72.8 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.42 | 9.57 | 15.55 | 17.00 | 88.3 | 80.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.41 | 6.51 | 10.54 | 1.00 | 76.0 | 79.0 |
| Bench 3 | Autosub In | Amari'i Bell | DEF | 12 | 3.9 | 2.32 | 6.24 | 10.37 | 2.00 | 71.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.96 | 16.75 | 26.36 | 1.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.18 | 12.72 | 19.98 | 2.00 | 65.4 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.5 | 2.24 | 6.39 | 10.39 | 1.00 | 48.6 | 23.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 7.43 | 19.74 | 31.01 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 7.9 | 6.19 | 17.70 | 27.00 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 5.02 | 14.46 | 23.33 | 2.00 | 89.3 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.2 | 3.05 | 11.56 | 22.15 | 0.00 | 34.1 | 0.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 2.84 | 8.78 | 13.97 | 2.00 | 71.3 | 90.0 |

## GW22

- Train rows: 119414
- Bank: 1.90 -> 0.20
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: triple_captain
- Predicted score: 56.26
- Actual score: 72.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.05) beats the best remaining Triple Captain opportunity (6.86).
- Transfer: Auston Trusty -> William Saliba (projected gain 4.40, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (6.05) beats the best remaining Triple Captain opportunity (6.86).
- Autosub: Amari'i Bell replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.41 | 9.36 | 15.52 | 3.00 | 77.6 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.8 | 1.43 | 3.32 | 5.30 | 0.00 | 33.7 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.41 | 12.85 | 21.10 | 1.00 | 83.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.93 | 10.72 | 17.31 | 2.00 | 83.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.22 | 8.97 | 14.58 | 2.00 | 70.4 | 90.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 2.27 | 8.97 | 16.23 | 1.00 | 27.7 | 22.0 |
| Bench 2 | Autosub In | Amari'i Bell | DEF | 12 | 3.9 | 2.39 | 6.34 | 10.45 | 6.00 | 72.9 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.05 | 14.60 | 23.58 | 7.00 | 79.1 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.40 | 12.84 | 20.26 | 13.00 | 61.9 | 86.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.4 | 1.87 | 5.63 | 9.62 | 1.00 | 41.3 | 3.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 6.05 | 17.05 | 27.20 | 10.00 | 79.6 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.1 | 3.35 | 13.00 | 24.13 | 0.00 | 23.2 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 3.67 | 12.20 | 19.45 | 6.00 | 44.7 | 76.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 3.94 | 12.15 | 20.76 | 1.00 | 66.2 | 90.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 2.73 | 8.35 | 13.82 | 1.00 | 71.0 | 90.0 |

## GW23

- Train rows: 120213
- Bank: 0.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Bukayo Saka
- Effective captain: Ollie Watkins
- Chip used: bench_boost
- Predicted score: 56.88
- Actual score: 89.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.85) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.85) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.09 | 9.32 | 15.15 | 1.00 | 80.0 | 45.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.8 | 0.56 | 1.47 | 2.57 | 0.00 | 12.9 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.06 | 12.04 | 19.76 | 1.00 | 81.8 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 3.03 | 10.60 | 18.05 | 1.00 | 52.8 | 57.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.44 | 10.17 | 16.46 | 1.00 | 83.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 2.98 | 9.72 | 15.68 | -1.00 | 82.9 | 90.0 |
| Bench 3 | Bench Boost | Amari'i Bell | DEF | 12 | 3.9 | 2.17 | 6.71 | 10.74 | 0.00 | 72.0 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.8 | 5.69 | 15.92 | 25.62 | 18.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.82 | 13.08 | 21.57 | 2.00 | 66.6 | 90.0 |
| Bench 4 | Bench Boost | Cameron Archer | FWD | 17 | 4.3 | 1.27 | 4.18 | 7.74 | 1.00 | 28.1 | 25.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 5.56 | 16.67 | 26.76 | 9.00 | 85.4 | 78.0 |
| XI | XI | Mohamed Salah | MID | 11 | 13.0 | 3.50 | 13.02 | 22.50 | 0.00 | 34.8 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 4.30 | 12.89 | 21.29 | 20.00 | 64.4 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 3.87 | 11.84 | 20.47 | 2.00 | 73.2 | 90.0 |
| Bench 2 | Bench Boost | Alejandro Garnacho | MID | 14 | 4.8 | 2.85 | 8.92 | 14.16 | 16.00 | 68.4 | 90.0 |