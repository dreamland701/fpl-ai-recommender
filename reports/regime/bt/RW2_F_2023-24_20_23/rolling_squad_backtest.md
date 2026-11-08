# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 232.48
- Total actual points: 288.00
- Average predicted points: 58.12
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
- Predicted score: 62.53
- Actual score: 84.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.42 | 9.02 | 14.56 | 11.00 | 76.4 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.8 | 0.49 | 0.96 | 1.45 | 0.00 | 8.3 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 5.72 | 16.47 | 26.36 | 0.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.38 | 12.87 | 20.49 | 2.00 | 88.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.10 | 9.44 | 15.18 | 1.00 | 85.2 | 90.0 |
| Bench 3 | Bench | Auston Trusty | DEF | 17 | 3.9 | 1.98 | 6.26 | 9.94 | 1.00 | 77.1 | 90.0 |
| Bench 4 | Bench | Amari'i Bell | DEF | 12 | 3.9 | 1.94 | 5.45 | 8.84 | 1.00 | 61.8 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.77 | 15.88 | 25.15 | 8.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 5.02 | 13.65 | 21.23 | 7.00 | 83.8 | 90.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.5 | 2.47 | 7.93 | 12.65 | 1.00 | 71.2 | 23.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.3 | 7.52 | 20.84 | 34.01 | 16.00 | 90.0 | 90.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.9 | 5.80 | 17.24 | 28.34 | 9.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.38 | 16.25 | 26.36 | 7.00 | 84.6 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.09 | 14.97 | 24.13 | 3.00 | 90.0 | 90.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 3.81 | 9.83 | 15.87 | 4.00 | 77.8 | 90.0 |

## GW21

- Train rows: 118627
- Bank: 0.00 -> 1.90
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Phil Foden
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 57.24
- Actual score: 43.00
- Transfer: Son Heung-min -> Phil Foden (projected gain 10.44, hit 0)
- Autosub: Auston Trusty replaced Trent Alexander-Arnold.
- Autosub: Cameron Archer replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.83 | 10.36 | 16.87 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.8 | 0.02 | 0.55 | 1.12 | 2.00 | 7.8 | 82.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.55 | 13.35 | 21.49 | 6.00 | 90.0 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 3.83 | 12.92 | 21.46 | 0.00 | 73.4 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.44 | 9.70 | 15.66 | 17.00 | 87.4 | 80.0 |
| Bench 3 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.41 | 6.40 | 10.30 | 1.00 | 74.9 | 79.0 |
| Bench 4 | Bench | Amari'i Bell | DEF | 12 | 3.9 | 2.29 | 6.17 | 10.20 | 2.00 | 70.6 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.96 | 16.66 | 26.09 | 1.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.16 | 12.33 | 19.50 | 2.00 | 66.9 | 90.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 4.5 | 2.41 | 6.88 | 11.11 | 1.00 | 50.7 | 23.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 7.39 | 19.39 | 30.23 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 7.9 | 6.22 | 17.21 | 26.29 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 4.92 | 13.99 | 22.46 | 2.00 | 88.8 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.2 | 2.69 | 11.04 | 21.22 | 0.00 | 28.9 | 0.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 2.85 | 8.83 | 14.01 | 2.00 | 72.6 | 90.0 |

## GW22

- Train rows: 119414
- Bank: 1.90 -> 0.20
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: triple_captain
- Predicted score: 55.83
- Actual score: 72.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.93) beats the best remaining Triple Captain opportunity (6.72).
- Transfer: Auston Trusty -> William Saliba (projected gain 4.10, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (5.93) beats the best remaining Triple Captain opportunity (6.72).
- Autosub: Amari'i Bell replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.31 | 9.04 | 14.93 | 3.00 | 79.9 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.8 | 1.41 | 3.14 | 4.91 | 0.00 | 36.5 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.39 | 12.38 | 20.24 | 1.00 | 83.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.89 | 10.36 | 16.75 | 2.00 | 81.7 | 90.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 2.35 | 8.67 | 15.52 | 1.00 | 29.1 | 22.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.27 | 8.65 | 14.20 | 2.00 | 69.6 | 90.0 |
| Bench 2 | Autosub In | Amari'i Bell | DEF | 12 | 3.9 | 2.42 | 6.29 | 10.31 | 6.00 | 72.4 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.03 | 14.57 | 23.27 | 7.00 | 78.9 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.38 | 12.69 | 20.16 | 13.00 | 63.7 | 86.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.4 | 2.00 | 5.91 | 10.10 | 1.00 | 43.5 | 3.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 5.93 | 16.42 | 26.05 | 10.00 | 79.2 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.1 | 3.52 | 12.30 | 22.25 | 0.00 | 23.8 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 4.02 | 11.59 | 19.62 | 1.00 | 67.5 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 3.47 | 11.24 | 18.06 | 6.00 | 48.0 | 76.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 2.79 | 8.37 | 13.76 | 1.00 | 71.5 | 90.0 |

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
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.12) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.12) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.02 | 9.04 | 14.70 | 1.00 | 81.0 | 45.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.8 | 0.53 | 1.30 | 2.29 | 0.00 | 15.7 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.02 | 11.86 | 19.39 | 1.00 | 81.5 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 3.02 | 10.39 | 17.48 | 1.00 | 51.5 | 57.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.40 | 10.09 | 16.25 | 1.00 | 81.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 2.97 | 9.65 | 15.52 | -1.00 | 82.2 | 90.0 |
| Bench 3 | Bench Boost | Amari'i Bell | DEF | 12 | 3.9 | 2.16 | 6.52 | 10.54 | 0.00 | 71.3 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.8 | 5.66 | 15.80 | 25.19 | 18.00 | 89.8 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.83 | 12.91 | 21.50 | 2.00 | 67.2 | 90.0 |
| Bench 4 | Bench Boost | Cameron Archer | FWD | 17 | 4.3 | 1.47 | 4.70 | 8.59 | 1.00 | 30.2 | 25.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 5.51 | 16.49 | 26.24 | 9.00 | 83.7 | 78.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 4.33 | 12.84 | 21.10 | 20.00 | 64.8 | 90.0 |
| XI | XI | Mohamed Salah | MID | 11 | 13.0 | 3.49 | 12.55 | 21.29 | 0.00 | 34.0 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 3.86 | 11.53 | 19.85 | 2.00 | 72.2 | 90.0 |
| Bench 2 | Bench Boost | Alejandro Garnacho | MID | 14 | 4.8 | 2.96 | 9.17 | 14.57 | 16.00 | 70.4 | 90.0 |