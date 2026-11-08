# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 296.85
- Total actual points: 368.00
- Average predicted points: 74.21
- Average actual points: 92.00
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW23 are included before the first simulated week.
- League-average scores were not available for this run.

## GW24

- Train rows: 149404
- Bank: 100.00 -> 0.20
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 80.15
- Actual score: 121.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (16.64) beats the best remaining Bench Boost opportunity (17.42).
- Chip advisory: bench_boost (0.58): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.66): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (16.64) beats the best remaining Bench Boost opportunity (17.42).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.0 | 3.90 | 10.40 | 16.48 | 10.00 | 112.9 | 180.0 |
| Bench 1 | Bench Boost | David Raya Martin | GK | 1 | 5.6 | 3.38 | 10.35 | 17.28 | 3.00 | 86.2 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.3 | 6.19 | 16.33 | 25.95 | 7.00 | 116.5 | 98.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 4.99 | 12.51 | 19.91 | 6.00 | 108.0 | 180.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.70 | 11.70 | 19.54 | 4.00 | 85.7 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 5.1 | 3.80 | 10.87 | 17.28 | 1.00 | 77.7 | 86.0 |
| Bench 2 | Bench Boost | Daniel Muñoz | DEF | 7 | 4.8 | 3.45 | 10.20 | 16.69 | 11.00 | 79.3 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.5 | 3.71 | 10.03 | 16.25 | 1.00 | 68.0 | 59.0 |
| Bench 3 | Bench Boost | João Pedro Junqueira de Jesus | FWD | 5 | 5.6 | 3.04 | 9.91 | 16.18 | 1.00 | 69.2 | 45.0 |
| Bench 4 | Bench Boost | Paul Onuachu | FWD | 17 | 4.9 | 2.55 | 6.98 | 11.32 | 7.00 | 58.8 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 9.33 | 26.17 | 42.97 | 29.00 | 125.1 | 177.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.3 | 7.38 | 20.72 | 34.42 | 6.00 | 96.3 | 89.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.8 | 5.77 | 16.78 | 27.51 | 2.00 | 87.8 | 90.0 |
| XI | XI | Amad Diallo | MID | 14 | 5.6 | 4.83 | 13.78 | 22.47 | 2.00 | 87.8 | 90.0 |
| XI | XI | Noni Madueke | MID | 6 | 6.1 | 4.81 | 12.91 | 20.24 | 2.00 | 73.2 | 60.0 |

## GW25

- Train rows: 150166
- Bank: 0.20 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 84.97
- Actual score: 92.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (14.64) beats the best remaining Triple Captain opportunity (9.41).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Jamie Vardy -> Iliman Ndiaye (projected gain 4.16, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (14.64) beats the best remaining Triple Captain opportunity (9.41).
- Autosub outfielders: Lewis Hall, Paul Onuachu.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 4.59 | 13.14 | 20.50 | 3.00 | 119.1 | 90.0 |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.5 | 3.49 | 10.12 | 17.03 | 7.00 | 80.3 | 90.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 6.82 | 17.58 | 28.11 | 13.00 | 125.0 | 128.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 6.22 | 15.60 | 24.30 | 2.00 | 146.3 | 180.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.79 | 11.71 | 19.42 | 2.00 | 86.5 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.8 | 3.89 | 11.26 | 18.25 | 1.00 | 84.0 | 90.0 |
| Bench 2 | Autosub In | Lewis Hall | DEF | 15 | 5.1 | 3.11 | 9.72 | 15.99 | 0.00 | 75.4 | 90.0 |
| XI | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 4.19 | 12.08 | 18.88 | 0.00 | 88.8 | 0.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 2.63 | 8.27 | 14.09 | 1.00 | 55.4 | 17.0 |
| Bench 3 | Autosub In | Paul Onuachu | FWD | 17 | 4.9 | 2.91 | 7.95 | 12.83 | 5.00 | 69.9 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 11.62 | 30.97 | 50.17 | 20.00 | 177.3 | 180.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 6.65 | 20.12 | 33.16 | 2.00 | 94.5 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.37 | 18.16 | 29.25 | 3.00 | 85.9 | 90.0 |
| XI | Bench | Amad Diallo | MID | 14 | 5.6 | 4.19 | 13.04 | 21.42 | 0.00 | 77.7 | 0.0 |
| XI | XI | Noni Madueke | MID | 6 | 6.1 | 3.40 | 10.29 | 16.48 | 1.00 | 57.7 | 20.0 |

## GW26

- Train rows: 150945
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 66.04
- Actual score: 87.00
- Transfer: Amad Diallo -> Morgan Rogers (projected gain 5.55, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.30 | 11.50 | 18.73 | 2.00 | 85.4 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 5.1 | 3.73 | 10.44 | 17.22 | 1.00 | 96.8 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.94 | 17.96 | 29.59 | 6.00 | 110.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 4.80 | 14.30 | 22.99 | 6.00 | 129.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.74 | 11.36 | 18.55 | 1.00 | 84.2 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.8 | 3.23 | 10.25 | 16.92 | 13.00 | 83.7 | 90.0 |
| Bench 2 | Bench | Lewis Hall | DEF | 15 | 5.1 | 2.79 | 8.63 | 14.36 | 9.00 | 72.4 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 2.99 | 8.62 | 13.74 | 1.00 | 72.8 | 18.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 2.87 | 8.15 | 13.80 | 12.00 | 44.3 | 90.0 |
| Bench 4 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 2.34 | 6.74 | 12.04 | 0.00 | 44.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.48 | 30.86 | 50.58 | 14.00 | 163.8 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 6.34 | 19.00 | 31.63 | 2.00 | 94.5 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.80 | 16.39 | 26.30 | 14.00 | 85.1 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 5.05 | 14.17 | 21.62 | 2.00 | 100.4 | 77.0 |
| Bench 3 | Bench | Noni Madueke | MID | 6 | 6.1 | 2.71 | 8.24 | 14.00 | 0.00 | 42.0 | 0.0 |

## GW27

- Train rows: 151728
- Bank: 0.10 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 65.68
- Actual score: 68.00
- Transfer: Noni Madueke -> Justin Kluivert (projected gain 4.08, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.31 | 10.14 | 16.76 | 6.00 | 84.7 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 5.1 | 3.26 | 9.96 | 16.37 | 2.00 | 94.6 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.66 | 16.69 | 27.64 | 6.00 | 98.9 | 76.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 4.24 | 12.62 | 20.62 | 7.00 | 108.2 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.8 | 3.91 | 10.88 | 17.89 | 4.00 | 85.3 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.52 | 10.59 | 17.37 | 0.00 | 83.2 | 18.0 |
| Bench 2 | Bench | Lewis Hall | DEF | 15 | 5.0 | 2.94 | 9.44 | 15.68 | 1.00 | 81.9 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 3.56 | 10.36 | 17.14 | 8.00 | 68.3 | 71.0 |
| Bench 3 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 1.88 | 6.36 | 10.70 | 0.00 | 47.3 | 58.0 |
| Bench 4 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 1.37 | 5.48 | 10.07 | 0.00 | 31.2 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.33 | 30.15 | 49.49 | 6.00 | 142.1 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 6.52 | 18.44 | 30.41 | 3.00 | 91.5 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.08 | 17.53 | 28.37 | 5.00 | 90.6 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.0 | 4.34 | 13.43 | 21.58 | 10.00 | 70.2 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.7 | 3.86 | 10.48 | 17.40 | 7.00 | 79.2 | 90.0 |