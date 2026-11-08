# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 232.55
- Total actual points: 282.00
- Average predicted points: 58.14
- Average actual points: 70.50
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
- Predicted score: 61.42
- Actual score: 72.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.51 | 9.39 | 15.26 | 11.00 | 78.0 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 4.4 | 3.08 | 9.00 | 14.65 | 2.00 | 87.3 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 5.75 | 16.06 | 25.74 | 0.00 | 94.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.54 | 12.97 | 20.74 | 2.00 | 92.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.95 | 11.23 | 18.19 | 0.00 | 91.6 | 90.0 |
| Bench 2 | Bench | Kieran Trippier | DEF | 15 | 6.8 | 3.27 | 11.05 | 18.90 | 0.00 | 72.7 | 0.0 |
| Bench 3 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.15 | 9.42 | 15.12 | 1.00 | 84.1 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 4.24 | 10.84 | 16.81 | 2.00 | 80.5 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 4.9 | 3.69 | 9.87 | 15.59 | 2.00 | 76.2 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.5 | 2.43 | 7.82 | 12.52 | 1.00 | 71.2 | 23.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.3 | 7.57 | 21.08 | 34.44 | 16.00 | 103.5 | 90.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.9 | 5.92 | 17.59 | 28.90 | 9.00 | 96.8 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.50 | 16.37 | 26.65 | 7.00 | 89.2 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.34 | 15.25 | 24.61 | 3.00 | 96.0 | 90.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 3.84 | 9.73 | 15.73 | 4.00 | 76.0 | 90.0 |

## GW21

- Train rows: 118627
- Bank: 0.20 -> 2.10
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Phil Foden
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 59.11
- Actual score: 55.00
- Transfer: Son Heung-min -> Phil Foden (projected gain 12.09, hit 0)
- Autosub: Kieran Trippier replaced Trent Alexander-Arnold.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 4.12 | 11.06 | 18.07 | 3.00 | 95.5 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 4.4 | 2.81 | 8.15 | 13.55 | 9.00 | 86.3 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.86 | 13.78 | 22.23 | 6.00 | 102.8 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 3.55 | 12.09 | 20.26 | 0.00 | 66.1 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.20 | 11.30 | 18.15 | 6.00 | 91.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.44 | 9.60 | 15.58 | 17.00 | 87.5 | 80.0 |
| Bench 2 | Autosub In | Kieran Trippier | DEF | 15 | 6.7 | 2.68 | 8.61 | 15.39 | 1.00 | 49.2 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 4.97 | 12.57 | 19.17 | 2.00 | 90.7 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 4.9 | 3.27 | 9.33 | 15.25 | 8.00 | 69.6 | 90.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 4.5 | 2.31 | 6.48 | 10.65 | 1.00 | 49.8 | 23.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 7.89 | 20.01 | 31.40 | 3.00 | 119.4 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 7.9 | 6.95 | 17.87 | 27.22 | 2.00 | 116.1 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 5.08 | 14.29 | 23.06 | 2.00 | 89.4 | 90.0 |
| Bench 4 | Bench | Mohamed Salah | MID | 11 | 13.2 | 1.92 | 11.15 | 21.38 | 0.00 | 13.5 | 0.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 2.89 | 8.67 | 13.78 | 2.00 | 70.6 | 90.0 |

## GW22

- Train rows: 119414
- Bank: 2.10 -> 5.10
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Pedro Porro
- Effective captain: Bukayo Saka
- Chip used: triple_captain
- Predicted score: 54.71
- Actual score: 56.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.21) beats the best remaining Triple Captain opportunity (7.04).
- Transfer: Trent Alexander-Arnold -> Kyle Walker (projected gain 3.41, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (6.21) beats the best remaining Triple Captain opportunity (7.04).
- Autosub: Phil Foden replaced Kyle Walker.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.45 | 9.66 | 16.04 | 3.00 | 79.9 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 4.4 | 2.88 | 8.48 | 14.38 | 10.00 | 87.8 | 90.0 |
| Vice Captain | XI | Pedro Porro | DEF | 18 | 5.8 | 4.61 | 12.90 | 21.15 | 1.00 | 86.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.99 | 10.88 | 17.56 | 2.00 | 84.1 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.7 | 3.30 | 10.41 | 17.66 | 7.00 | 70.8 | 90.0 |
| XI | Bench | Kyle Walker | DEF | 13 | 5.4 | 3.68 | 10.20 | 16.23 | 0.00 | 75.5 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.76 | 10.11 | 16.31 | 2.00 | 79.7 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 3.92 | 10.78 | 16.92 | 2.00 | 72.7 | 70.0 |
| XI | XI | Chris Wood | FWD | 16 | 4.9 | 2.87 | 9.01 | 14.63 | 1.00 | 73.3 | 45.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 4.4 | 1.94 | 5.88 | 10.13 | 1.00 | 41.2 | 3.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 6.21 | 17.07 | 27.21 | 10.00 | 83.6 | 90.0 |
| Bench 4 | Bench | Mohamed Salah | MID | 11 | 13.1 | 3.06 | 11.72 | 22.02 | 0.00 | 14.6 | 0.0 |
| Bench 2 | Autosub In | Phil Foden | MID | 13 | 7.9 | 3.66 | 11.65 | 18.57 | 6.00 | 43.0 | 76.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 3.76 | 11.63 | 19.95 | 1.00 | 58.9 | 90.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 2.74 | 8.22 | 13.62 | 1.00 | 69.9 | 90.0 |

## GW23

- Train rows: 120213
- Bank: 5.10 -> 1.70
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Bukayo Saka
- Effective captain: Ollie Watkins
- Chip used: bench_boost
- Predicted score: 57.31
- Actual score: 99.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.77) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: João Pedro Junqueira de Jesus -> Ollie Watkins (projected gain 10.59, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.77) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.08 | 9.61 | 15.66 | 1.00 | 81.6 | 45.0 |
| Bench 1 | Bench Boost | Jordan Pickford | GK | 9 | 4.4 | 2.79 | 8.39 | 14.20 | 2.00 | 85.3 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.7 | 4.47 | 12.57 | 20.31 | 9.00 | 83.6 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.19 | 12.16 | 19.95 | 1.00 | 84.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.40 | 10.32 | 16.71 | 1.00 | 83.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 2.99 | 9.65 | 15.55 | -1.00 | 81.7 | 90.0 |
| Bench 3 | Bench Boost | Kyle Walker | DEF | 13 | 5.4 | 1.86 | 5.78 | 9.91 | 2.00 | 32.1 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.8 | 5.78 | 16.25 | 26.22 | 18.00 | 93.3 | 90.0 |
| Bench 2 | Bench Boost | Chris Wood | FWD | 16 | 4.9 | 1.97 | 6.99 | 12.40 | 0.00 | 39.4 | 0.0 |
| Bench 4 | Bench Boost | Cameron Archer | FWD | 17 | 4.3 | 1.15 | 4.39 | 8.19 | 1.00 | 24.6 | 25.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 5.55 | 16.75 | 26.86 | 9.00 | 87.6 | 78.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 4.22 | 12.67 | 20.98 | 20.00 | 62.1 | 90.0 |
| XI | XI | Mohamed Salah | MID | 11 | 13.0 | 3.58 | 12.65 | 21.80 | 0.00 | 36.5 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 3.69 | 11.57 | 20.04 | 2.00 | 67.9 | 90.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 2.80 | 8.86 | 14.11 | 16.00 | 67.3 | 90.0 |