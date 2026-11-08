# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 231.49
- Total actual points: 269.00
- Average predicted points: 57.87
- Average actual points: 67.25
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
- Predicted score: 62.93
- Actual score: 72.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.4 | 3.46 | 10.09 | 16.40 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.8 | 0.40 | 0.75 | 1.12 | 0.00 | 6.1 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 5.76 | 16.67 | 26.66 | 0.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.45 | 13.11 | 20.97 | 2.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi | DEF | 3 | 4.5 | 2.68 | 8.44 | 13.90 | 0.00 | 71.6 | 90.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 5 | 4.0 | 2.52 | 6.99 | 11.10 | 8.00 | 81.6 | 90.0 |
| Bench 4 | Bench | Jordan Beyer | DEF | 6 | 4.0 | 2.08 | 6.84 | 11.01 | 1.00 | 76.6 | 16.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.06 | 16.66 | 26.53 | 8.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 5.61 | 15.68 | 24.52 | 7.00 | 88.9 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 4.9 | 3.90 | 10.90 | 17.31 | 2.00 | 79.0 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.3 | 7.36 | 20.40 | 33.36 | 16.00 | 90.0 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.9 | 5.87 | 17.16 | 28.10 | 9.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.42 | 16.20 | 26.46 | 7.00 | 85.6 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.99 | 14.68 | 23.66 | 3.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Lewis Miley | MID | 15 | 4.5 | 2.52 | 8.45 | 13.74 | 0.00 | 73.7 | 53.0 |

## GW21

- Train rows: 118627
- Bank: 0.00 -> 1.90
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 57.44
- Actual score: 44.00
- Transfer: Son Heung-min -> Phil Foden (projected gain 10.76, hit 0)
- Autosub: Lewis Miley replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.4 | 3.27 | 9.30 | 15.38 | 9.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.8 | 0.00 | 0.33 | 0.75 | 2.00 | 5.7 | 82.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.51 | 13.54 | 21.90 | 6.00 | 90.0 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 3.92 | 12.85 | 21.44 | 0.00 | 72.1 | 0.0 |
| XI | XI | Jan Paul van Hecke | DEF | 5 | 4.0 | 2.60 | 7.05 | 11.48 | 6.00 | 77.6 | 90.0 |
| Bench 3 | Bench | Marcos Senesi | DEF | 3 | 4.5 | 1.77 | 6.32 | 10.81 | 0.00 | 60.2 | 0.0 |
| Bench 4 | Bench | Jordan Beyer | DEF | 6 | 4.0 | 1.03 | 3.60 | 6.36 | 0.00 | 35.5 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.32 | 17.87 | 28.24 | 1.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.76 | 14.46 | 22.83 | 2.00 | 71.6 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 4.9 | 3.49 | 10.35 | 16.94 | 8.00 | 74.0 | 90.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 7.32 | 19.52 | 30.71 | 3.00 | 90.0 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 6.22 | 17.84 | 27.25 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 4.87 | 13.90 | 22.36 | 2.00 | 87.8 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.2 | 2.83 | 10.63 | 20.45 | 0.00 | 33.3 | 0.0 |
| Bench 2 | Autosub In | Lewis Miley | MID | 15 | 4.5 | 2.20 | 7.13 | 11.99 | 2.00 | 63.8 | 90.0 |

## GW22

- Train rows: 119414
- Bank: 1.90 -> 0.30
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: triple_captain
- Predicted score: 56.16
- Actual score: 74.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.09) beats the best remaining Triple Captain opportunity (6.90).
- Transfer: Jan Paul van Hecke -> William Saliba (projected gain 2.94, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (6.09) beats the best remaining Triple Captain opportunity (6.90).
- Autosub: Lewis Miley replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.4 | 3.33 | 9.58 | 16.14 | 10.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.8 | 1.51 | 3.48 | 5.50 | 0.00 | 37.4 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.44 | 12.84 | 21.06 | 1.00 | 84.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.84 | 10.36 | 16.66 | 2.00 | 82.5 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 2.19 | 8.67 | 15.70 | 1.00 | 26.6 | 22.0 |
| Bench 3 | Bench | Marcos Senesi | DEF | 3 | 4.5 | 1.57 | 5.02 | 8.78 | 2.00 | 47.1 | 90.0 |
| Bench 4 | Bench | Jordan Beyer | DEF | 6 | 4.0 | 0.07 | 1.68 | 3.32 | 0.00 | 23.0 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.39 | 15.63 | 25.28 | 7.00 | 82.4 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.94 | 14.45 | 22.89 | 13.00 | 68.0 | 86.0 |
| XI | XI | Chris Wood | FWD | 16 | 4.9 | 3.23 | 10.49 | 17.02 | 1.00 | 78.3 | 45.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 6.09 | 17.09 | 27.25 | 10.00 | 81.6 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 3.64 | 12.15 | 19.37 | 6.00 | 44.4 | 76.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.1 | 3.15 | 12.12 | 22.52 | 0.00 | 23.2 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 3.74 | 11.42 | 19.54 | 1.00 | 64.7 | 90.0 |
| Bench 2 | Autosub In | Lewis Miley | MID | 15 | 4.5 | 2.43 | 7.37 | 12.31 | 2.00 | 74.2 | 74.0 |

## GW23

- Train rows: 120213
- Bank: 0.30 -> 0.50
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Bukayo Saka
- Effective captain: Ollie Watkins
- Chip used: bench_boost
- Predicted score: 54.96
- Actual score: 79.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.01) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Jordan Pickford -> Alphonse Areola (projected gain 0.86, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.01) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.38 | 10.26 | 16.72 | 1.00 | 84.0 | 45.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.8 | 0.61 | 1.59 | 2.76 | 0.00 | 15.4 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.01 | 11.90 | 19.58 | 1.00 | 80.8 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 2.90 | 10.22 | 17.38 | 1.00 | 50.8 | 57.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.26 | 9.73 | 15.77 | 1.00 | 79.6 | 90.0 |
| XI | XI | Marcos Senesi | DEF | 3 | 4.5 | 2.55 | 6.89 | 11.06 | 1.00 | 67.1 | 90.0 |
| Bench 4 | Bench Boost | Jordan Beyer | DEF | 6 | 4.0 | 0.26 | 1.17 | 2.23 | 0.00 | 9.0 | 0.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.8 | 6.03 | 16.97 | 27.37 | 18.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 5.21 | 14.31 | 23.65 | 2.00 | 70.7 | 90.0 |
| Bench 3 | Bench Boost | Chris Wood | FWD | 16 | 4.9 | 1.92 | 7.17 | 12.78 | 0.00 | 35.5 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 5.51 | 16.62 | 26.74 | 9.00 | 85.2 | 78.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 4.28 | 12.93 | 21.39 | 20.00 | 63.8 | 90.0 |
| XI | XI | Mohamed Salah | MID | 11 | 13.0 | 3.19 | 12.07 | 20.89 | 0.00 | 31.7 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 3.58 | 11.01 | 19.17 | 2.00 | 69.8 | 90.0 |
| Bench 2 | Bench Boost | Lewis Miley | MID | 15 | 4.5 | 2.21 | 6.29 | 10.43 | 5.00 | 61.9 | 90.0 |