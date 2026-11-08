# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 233.43
- Total actual points: 237.00
- Average predicted points: 58.36
- Average actual points: 59.25
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
- Bank: 100.00 -> 0.20
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Son Heung-min
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 62.24
- Actual score: 65.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.4 | 3.74 | 10.77 | 18.17 | 2.00 | 88.6 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 4.8 | 3.62 | 9.68 | 19.79 | 1.00 | 83.3 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 4.91 | 14.20 | 24.47 | 0.00 | 89.0 | 90.0 |
| Bench 3 | Bench | Kieran Trippier | DEF | 15 | 6.8 | 2.04 | 12.78 | 20.27 | 0.00 | 60.8 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.2 | 3.82 | 11.40 | 18.50 | 1.00 | 85.7 | 90.0 |
| XI | XI | Destiny Udogie | DEF | 18 | 4.8 | 3.76 | 10.45 | 16.26 | 2.00 | 74.9 | 90.0 |
| Bench 2 | Bench | Pedro Porro | DEF | 18 | 5.7 | 3.27 | 9.87 | 16.96 | 2.00 | 83.1 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 6.22 | 17.29 | 25.97 | 7.00 | 86.0 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 4.9 | 3.48 | 10.13 | 16.85 | 2.00 | 70.2 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.5 | 1.77 | 7.09 | 10.47 | 1.00 | 70.6 | 23.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.9 | 6.51 | 19.72 | 36.34 | 9.00 | 86.8 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.3 | 7.39 | 19.50 | 34.96 | 16.00 | 88.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.27 | 16.91 | 30.57 | 3.00 | 90.4 | 90.0 |
| XI | XI | Bernardo Veiga de Carvalho e Silva | MID | 13 | 6.5 | 5.10 | 16.21 | 23.20 | 3.00 | 84.3 | 90.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 4.64 | 13.97 | 18.59 | 4.00 | 84.7 | 90.0 |

## GW21

- Train rows: 118627
- Bank: 0.20 -> 1.90
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Julián Álvarez
- Effective captain: Julián Álvarez
- Chip used: none
- Predicted score: 50.31
- Actual score: 55.00
- Transfer: Kieran Trippier -> Pervis Estupiñán (projected gain 2.91, hit 0)
- Autosub: Destiny Udogie replaced Trent Alexander-Arnold.
- Autosub: Chris Wood replaced Mohamed Salah.
- Autosub: Cameron Archer replaced Son Heung-min.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.4 | 3.70 | 10.58 | 18.52 | 9.00 | 88.6 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 4.8 | 1.85 | 6.58 | 12.80 | 2.00 | 67.9 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 3.50 | 13.13 | 23.65 | 0.00 | 71.5 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 3.50 | 12.99 | 17.24 | 6.00 | 87.2 | 90.0 |
| XI | XI | Pervis Estupiñán | DEF | 5 | 5.0 | 4.30 | 11.65 | 12.60 | 8.00 | 85.5 | 71.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.2 | 4.22 | 11.47 | 17.41 | 6.00 | 85.9 | 90.0 |
| Bench 2 | Autosub In | Destiny Udogie | DEF | 18 | 4.8 | 3.01 | 8.78 | 14.92 | 1.00 | 77.1 | 90.0 |
| Vice Captain | Captain | Julián Álvarez | FWD | 13 | 6.9 | 4.79 | 13.90 | 24.64 | 2.00 | 83.3 | 90.0 |
| Bench 3 | Autosub In | Chris Wood | FWD | 16 | 4.9 | 2.98 | 9.00 | 17.02 | 8.00 | 65.8 | 90.0 |
| Bench 4 | Autosub In | Cameron Archer | FWD | 17 | 4.5 | 1.97 | 3.69 | 6.21 | 1.00 | 34.4 | 23.0 |
| XI | Bench | Son Heung-min | MID | 18 | 9.8 | 4.50 | 17.56 | 30.69 | 0.00 | 59.6 | 0.0 |
| Captain | Bench | Mohamed Salah | MID | 11 | 13.2 | 4.91 | 17.51 | 33.09 | 0.00 | 62.9 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 4.18 | 14.73 | 24.80 | 2.00 | 84.7 | 90.0 |
| XI | XI | Bernardo Veiga de Carvalho e Silva | MID | 13 | 6.5 | 4.05 | 13.78 | 21.98 | 8.00 | 83.0 | 68.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 3.75 | 11.11 | 15.94 | 2.00 | 83.7 | 90.0 |

## GW22

- Train rows: 119414
- Bank: 1.90 -> 1.00
- Free transfers: 2 -> 2
- Captain: Kevin De Bruyne
- Vice captain: Jarrod Bowen
- Effective captain: Kevin De Bruyne
- Chip used: bench_boost
- Predicted score: 64.20
- Actual score: 56.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.55) beats the best remaining Bench Boost opportunity (11.94).
- Transfer: Son Heung-min -> Kevin De Bruyne (projected gain 12.14, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.55) beats the best remaining Bench Boost opportunity (11.94).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.4 | 3.25 | 9.21 | 18.02 | 10.00 | 91.3 | 90.0 |
| Bench 1 | Bench Boost | André Onana | GK | 14 | 4.8 | 2.78 | 7.70 | 14.73 | 1.00 | 82.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 3.72 | 12.30 | 17.01 | 1.00 | 84.9 | 90.0 |
| XI | XI | Pervis Estupiñán | DEF | 5 | 5.0 | 3.72 | 10.82 | 14.18 | 0.00 | 77.0 | 45.0 |
| Bench 2 | Bench Boost | Trent Alexander-Arnold | DEF | 11 | 8.4 | 3.14 | 10.20 | 18.48 | 1.00 | 61.0 | 22.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.2 | 4.13 | 10.18 | 16.55 | 2.00 | 86.4 | 90.0 |
| XI | XI | Destiny Udogie | DEF | 18 | 4.8 | 3.87 | 9.29 | 16.20 | 10.00 | 79.6 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 3.71 | 11.96 | 21.86 | 13.00 | 75.0 | 86.0 |
| XI | XI | Chris Wood | FWD | 16 | 4.9 | 3.27 | 9.24 | 16.74 | 1.00 | 77.0 | 45.0 |
| Bench 4 | Bench Boost | Cameron Archer | FWD | 17 | 4.4 | 2.21 | 5.34 | 7.03 | 1.00 | 48.5 | 3.0 |
| Captain | Captain | Kevin De Bruyne | MID | 13 | 10.6 | 7.31 | 20.41 | 28.31 | 7.00 | 71.2 | 70.0 |
| Vice Captain | XI | Jarrod Bowen | MID | 19 | 8.0 | 5.48 | 13.04 | 21.96 | 1.00 | 84.1 | 90.0 |
| XI | XI | Bernardo Veiga de Carvalho e Silva | MID | 13 | 6.5 | 4.34 | 12.55 | 21.47 | 0.00 | 71.2 | 0.0 |
| Bench 3 | Bench Boost | Mohamed Salah | MID | 11 | 13.1 | 2.42 | 11.54 | 23.03 | 0.00 | 20.4 | 0.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 3.56 | 7.55 | 15.21 | 1.00 | 78.4 | 90.0 |

## GW23

- Train rows: 120213
- Bank: 1.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Kevin De Bruyne
- Vice captain: Kieran Trippier
- Effective captain: Kevin De Bruyne
- Chip used: triple_captain
- Predicted score: 56.68
- Actual score: 61.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.38) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Virgil van Dijk -> Kieran Trippier (projected gain 4.81, hit 0)
- Chip used: Triple Captain on Kevin De Bruyne. Optimizer chose Triple Captain here because the current estimated captain upside (6.38) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Bernardo Veiga de Carvalho e Silva replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.93 | 10.73 | 17.72 | 8.00 | 87.3 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 4.4 | 3.52 | 10.24 | 17.86 | 2.00 | 90.1 | 90.0 |
| Vice Captain | XI | Kieran Trippier | DEF | 15 | 6.7 | 4.72 | 14.30 | 19.91 | 9.00 | 88.0 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 4.18 | 13.82 | 20.96 | 1.00 | 60.0 | 57.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.07 | 11.58 | 17.94 | 1.00 | 82.2 | 90.0 |
| XI | XI | Destiny Udogie | DEF | 18 | 4.8 | 4.14 | 10.19 | 18.42 | 4.00 | 85.4 | 90.0 |
| XI | XI | Pervis Estupiñán | DEF | 5 | 5.0 | 3.12 | 8.57 | 14.74 | 1.00 | 48.1 | 10.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 2.61 | 14.35 | 23.79 | 2.00 | 59.3 | 90.0 |
| Bench 2 | Bench | Chris Wood | FWD | 16 | 4.9 | 2.20 | 7.59 | 12.89 | 0.00 | 36.2 | 0.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.3 | 0.88 | 3.08 | 6.87 | 1.00 | 15.8 | 25.0 |
| Captain | Captain | Kevin De Bruyne | MID | 13 | 10.6 | 6.38 | 18.03 | 29.36 | 5.00 | 74.4 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 3.84 | 14.22 | 20.22 | 2.00 | 81.7 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.0 | 2.96 | 12.48 | 20.46 | 0.00 | 29.7 | 0.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 3.99 | 9.82 | 17.32 | 16.00 | 80.0 | 90.0 |
| Bench 3 | Autosub In | Bernardo Veiga de Carvalho e Silva | MID | 13 | 6.5 | 1.87 | 6.90 | 14.31 | 2.00 | 23.7 | 70.0 |