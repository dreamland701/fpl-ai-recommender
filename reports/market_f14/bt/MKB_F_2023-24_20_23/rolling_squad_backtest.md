# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 236.10
- Total actual points: 291.00
- Average predicted points: 59.02
- Average actual points: 72.75
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
- Vice captain: Ollie Watkins
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 63.06
- Actual score: 84.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.45 | 9.04 | 14.79 | 11.00 | 78.9 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.8 | 0.50 | 1.02 | 1.55 | 0.00 | 1.8 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 5.48 | 16.08 | 25.80 | 0.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.35 | 12.97 | 20.77 | 2.00 | 89.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.28 | 9.84 | 15.68 | 1.00 | 82.4 | 90.0 |
| Bench 4 | Bench | Auston Trusty | DEF | 17 | 3.9 | 1.94 | 6.30 | 9.94 | 1.00 | 76.7 | 90.0 |
| Bench 3 | Bench | Chris Richards | DEF | 8 | 3.9 | 2.04 | 5.56 | 8.64 | 2.00 | 67.3 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.87 | 16.16 | 25.73 | 8.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 5.35 | 14.72 | 22.94 | 7.00 | 85.1 | 90.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.5 | 2.40 | 7.88 | 12.52 | 1.00 | 71.0 | 23.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.3 | 7.54 | 21.01 | 34.37 | 16.00 | 90.0 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.9 | 5.86 | 17.47 | 28.76 | 9.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.60 | 16.59 | 26.94 | 7.00 | 87.2 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.01 | 14.83 | 24.06 | 3.00 | 90.0 | 90.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 3.73 | 9.84 | 15.88 | 4.00 | 75.4 | 90.0 |

## GW21

- Train rows: 118627
- Bank: 0.00 -> 1.90
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Phil Foden
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 58.47
- Actual score: 43.00
- Transfer: Son Heung-min -> Phil Foden (projected gain 11.68, hit 0)
- Autosub: Auston Trusty replaced Trent Alexander-Arnold.
- Autosub: Cameron Archer replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 4.08 | 10.97 | 17.94 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.8 | 0.00 | 0.35 | 0.75 | 2.00 | 1.7 | 82.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.54 | 13.58 | 21.98 | 6.00 | 90.0 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 3.56 | 12.06 | 20.23 | 0.00 | 66.8 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.64 | 10.10 | 16.27 | 17.00 | 86.1 | 80.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.36 | 6.38 | 10.32 | 1.00 | 74.1 | 79.0 |
| Bench 4 | Bench | Chris Richards | DEF | 8 | 3.9 | 1.69 | 5.46 | 8.76 | 0.00 | 71.8 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.91 | 16.76 | 26.52 | 1.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.28 | 13.07 | 20.54 | 2.00 | 65.7 | 90.0 |
| Bench 3 | Autosub In | Cameron Archer | FWD | 17 | 4.5 | 2.20 | 6.43 | 10.59 | 1.00 | 48.5 | 23.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 7.70 | 20.31 | 31.80 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 7.9 | 6.33 | 18.03 | 27.43 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 4.89 | 14.10 | 22.81 | 2.00 | 87.7 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.2 | 2.94 | 11.27 | 21.57 | 0.00 | 31.3 | 0.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 2.90 | 9.02 | 14.28 | 2.00 | 69.5 | 90.0 |

## GW22

- Train rows: 119414
- Bank: 1.90 -> 0.20
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: triple_captain
- Predicted score: 56.66
- Actual score: 67.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.15) beats the best remaining Triple Captain opportunity (6.97).
- Transfer: Auston Trusty -> William Saliba (projected gain 4.86, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (6.15) beats the best remaining Triple Captain opportunity (6.97).
- Autosub: Chris Richards replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.43 | 9.44 | 15.75 | 3.00 | 81.8 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.8 | 1.51 | 3.45 | 5.48 | 0.00 | 34.2 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.37 | 12.80 | 21.03 | 1.00 | 84.3 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.09 | 11.13 | 17.87 | 2.00 | 82.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.88 | 10.50 | 16.81 | 2.00 | 79.8 | 90.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 2.19 | 8.65 | 15.68 | 1.00 | 29.0 | 22.0 |
| Bench 2 | Autosub In | Chris Richards | DEF | 8 | 3.9 | 2.47 | 6.31 | 10.24 | 1.00 | 74.9 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.02 | 14.69 | 23.83 | 7.00 | 79.4 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.58 | 13.25 | 20.96 | 13.00 | 62.4 | 86.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.4 | 1.85 | 5.64 | 9.82 | 1.00 | 43.0 | 3.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 6.15 | 17.22 | 27.39 | 10.00 | 80.4 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 3.64 | 11.99 | 19.10 | 6.00 | 40.9 | 76.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.1 | 2.84 | 11.53 | 21.76 | 0.00 | 14.4 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 3.63 | 11.31 | 19.51 | 1.00 | 61.5 | 90.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 2.74 | 8.41 | 13.89 | 1.00 | 68.8 | 90.0 |

## GW23

- Train rows: 120213
- Bank: 0.20 -> 1.90
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Bukayo Saka
- Effective captain: Ollie Watkins
- Chip used: bench_boost
- Predicted score: 57.91
- Actual score: 97.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.49) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Trent Alexander-Arnold -> Kieran Trippier (projected gain 3.63, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.49) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.15 | 9.53 | 15.57 | 1.00 | 83.2 | 45.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.8 | 0.37 | 1.06 | 1.91 | 0.00 | 10.5 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.7 | 4.44 | 12.74 | 20.54 | 9.00 | 80.3 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.02 | 11.94 | 19.66 | 1.00 | 82.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.49 | 10.40 | 16.84 | 1.00 | 81.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.02 | 9.89 | 15.91 | -1.00 | 79.7 | 90.0 |
| Bench 3 | Bench Boost | Chris Richards | DEF | 8 | 3.9 | 1.98 | 5.82 | 9.39 | 0.00 | 72.9 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.8 | 5.79 | 16.29 | 26.28 | 18.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.86 | 13.26 | 21.92 | 2.00 | 67.2 | 90.0 |
| Bench 4 | Bench Boost | Cameron Archer | FWD | 17 | 4.3 | 1.24 | 4.20 | 7.94 | 1.00 | 29.6 | 25.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 5.61 | 16.83 | 26.99 | 9.00 | 85.6 | 78.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 4.20 | 12.68 | 20.99 | 20.00 | 62.3 | 90.0 |
| XI | XI | Mohamed Salah | MID | 11 | 13.0 | 3.36 | 12.43 | 21.51 | 0.00 | 34.1 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 3.70 | 11.36 | 19.76 | 2.00 | 70.4 | 90.0 |
| Bench 2 | Bench Boost | Alejandro Garnacho | MID | 14 | 4.8 | 2.90 | 9.14 | 14.49 | 16.00 | 66.9 | 90.0 |