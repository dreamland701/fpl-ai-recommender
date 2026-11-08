# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 234.64
- Total actual points: 283.00
- Average predicted points: 58.66
- Average actual points: 70.75
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
- Predicted score: 63.17
- Actual score: 84.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.56 | 9.35 | 15.24 | 11.00 | 77.9 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.8 | 0.52 | 1.10 | 1.69 | 0.00 | 9.1 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 5.59 | 16.22 | 25.99 | 0.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.27 | 12.60 | 20.14 | 2.00 | 86.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.23 | 9.67 | 15.53 | 1.00 | 85.1 | 90.0 |
| Bench 4 | Bench | Auston Trusty | DEF | 17 | 3.9 | 1.87 | 6.09 | 9.69 | 1.00 | 76.0 | 90.0 |
| Bench 3 | Bench | Chris Richards | DEF | 8 | 3.9 | 2.05 | 5.75 | 9.00 | 2.00 | 68.7 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.87 | 16.15 | 25.75 | 8.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 5.05 | 14.08 | 21.97 | 7.00 | 84.2 | 90.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.5 | 2.40 | 7.96 | 12.76 | 1.00 | 71.6 | 23.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.3 | 7.62 | 21.10 | 34.49 | 16.00 | 90.0 | 90.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.9 | 5.94 | 17.60 | 28.94 | 9.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.47 | 16.29 | 26.59 | 7.00 | 86.4 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.20 | 15.33 | 24.74 | 3.00 | 90.0 | 90.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 3.75 | 9.85 | 15.91 | 4.00 | 76.5 | 90.0 |

## GW21

- Train rows: 118627
- Bank: 0.00 -> 1.90
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Phil Foden
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 57.91
- Actual score: 43.00
- Transfer: Son Heung-min -> Phil Foden (projected gain 10.85, hit 0)
- Autosub: Auston Trusty replaced Trent Alexander-Arnold.
- Autosub: Cameron Archer replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 4.02 | 10.88 | 17.82 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.8 | 0.05 | 0.68 | 1.34 | 2.00 | 8.7 | 82.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.44 | 13.27 | 21.42 | 6.00 | 90.0 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 3.84 | 12.61 | 21.05 | 0.00 | 71.7 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.46 | 9.72 | 15.80 | 17.00 | 87.5 | 80.0 |
| Bench 3 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.35 | 6.30 | 10.17 | 1.00 | 73.6 | 79.0 |
| Bench 4 | Bench | Chris Richards | DEF | 8 | 3.9 | 1.74 | 5.69 | 9.18 | 0.00 | 72.7 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.05 | 17.12 | 27.05 | 1.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.24 | 12.97 | 20.45 | 2.00 | 67.1 | 90.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 4.5 | 2.35 | 6.84 | 11.21 | 1.00 | 51.5 | 23.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 7.43 | 19.76 | 31.07 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 7.9 | 6.17 | 17.61 | 26.86 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 5.04 | 14.49 | 23.36 | 2.00 | 89.2 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.2 | 2.94 | 11.15 | 21.38 | 0.00 | 31.6 | 0.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 2.86 | 8.80 | 13.97 | 2.00 | 71.2 | 90.0 |

## GW22

- Train rows: 119414
- Bank: 1.90 -> 0.20
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: triple_captain
- Predicted score: 56.41
- Actual score: 67.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.05) beats the best remaining Triple Captain opportunity (6.86).
- Transfer: Auston Trusty -> William Saliba (projected gain 4.84, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (6.05) beats the best remaining Triple Captain opportunity (6.86).
- Autosub: Chris Richards replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.48 | 9.63 | 16.02 | 3.00 | 80.7 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.8 | 1.42 | 3.32 | 5.30 | 0.00 | 37.1 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.33 | 12.57 | 20.59 | 1.00 | 80.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.00 | 10.97 | 17.73 | 2.00 | 83.2 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.23 | 8.99 | 14.57 | 2.00 | 69.4 | 90.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 2.17 | 8.56 | 15.46 | 1.00 | 26.4 | 22.0 |
| Bench 2 | Autosub In | Chris Richards | DEF | 8 | 3.9 | 2.38 | 6.16 | 10.12 | 1.00 | 76.2 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.14 | 14.95 | 24.24 | 7.00 | 80.4 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.47 | 13.10 | 20.76 | 13.00 | 63.9 | 86.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.4 | 1.99 | 6.08 | 10.45 | 1.00 | 44.2 | 3.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 6.05 | 17.07 | 27.24 | 10.00 | 80.1 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.1 | 3.23 | 12.47 | 23.08 | 0.00 | 20.9 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 3.96 | 12.13 | 20.65 | 1.00 | 65.8 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 3.66 | 12.10 | 19.21 | 6.00 | 45.6 | 76.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 2.76 | 8.41 | 13.88 | 1.00 | 71.0 | 90.0 |

## GW23

- Train rows: 120213
- Bank: 0.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Bukayo Saka
- Effective captain: Ollie Watkins
- Chip used: bench_boost
- Predicted score: 57.14
- Actual score: 89.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.90) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.90) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.17 | 9.64 | 15.74 | 1.00 | 82.8 | 45.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.8 | 0.56 | 1.48 | 2.59 | 0.00 | 16.3 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.00 | 11.83 | 19.40 | 1.00 | 78.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.51 | 10.44 | 16.93 | 1.00 | 82.6 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 2.94 | 10.30 | 17.47 | 1.00 | 51.1 | 57.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.01 | 9.82 | 15.82 | -1.00 | 81.8 | 90.0 |
| Bench 3 | Bench Boost | Chris Richards | DEF | 8 | 3.9 | 2.07 | 6.12 | 9.86 | 0.00 | 74.5 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.8 | 5.78 | 16.29 | 26.31 | 18.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.90 | 13.42 | 22.22 | 2.00 | 68.3 | 90.0 |
| Bench 4 | Bench Boost | Cameron Archer | FWD | 17 | 4.3 | 1.38 | 4.61 | 8.53 | 1.00 | 31.0 | 25.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 5.58 | 16.76 | 26.93 | 9.00 | 85.4 | 78.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 4.31 | 12.91 | 21.34 | 20.00 | 64.7 | 90.0 |
| XI | XI | Mohamed Salah | MID | 11 | 13.0 | 3.37 | 12.50 | 21.54 | 0.00 | 32.3 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 3.89 | 11.86 | 20.48 | 2.00 | 72.5 | 90.0 |
| Bench 2 | Bench Boost | Alejandro Garnacho | MID | 14 | 4.8 | 2.89 | 9.04 | 14.34 | 16.00 | 69.2 | 90.0 |