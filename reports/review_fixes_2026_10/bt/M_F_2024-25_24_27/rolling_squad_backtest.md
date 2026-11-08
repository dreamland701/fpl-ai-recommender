# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 296.63
- Total actual points: 368.00
- Average predicted points: 74.16
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
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (16.59) beats the best remaining Bench Boost opportunity (17.40).
- Chip advisory: bench_boost (0.58): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.66): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (16.59) beats the best remaining Bench Boost opportunity (17.40).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.0 | 3.90 | 10.34 | 16.34 | 10.00 | 112.9 | 180.0 |
| Bench 1 | Bench Boost | David Raya Martin | GK | 1 | 5.6 | 3.37 | 10.27 | 17.16 | 3.00 | 86.2 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.3 | 6.22 | 16.45 | 25.99 | 7.00 | 116.4 | 98.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 5.02 | 12.50 | 19.83 | 6.00 | 108.0 | 180.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.68 | 11.63 | 19.38 | 4.00 | 85.7 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 5.1 | 3.80 | 10.84 | 17.20 | 1.00 | 77.7 | 86.0 |
| Bench 2 | Bench Boost | Daniel Muñoz | DEF | 7 | 4.8 | 3.44 | 10.15 | 16.60 | 11.00 | 79.4 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.5 | 3.73 | 9.83 | 15.89 | 1.00 | 68.0 | 59.0 |
| Bench 3 | Bench Boost | João Pedro Junqueira de Jesus | FWD | 5 | 5.6 | 3.02 | 9.82 | 16.02 | 1.00 | 69.2 | 45.0 |
| Bench 4 | Bench Boost | Paul Onuachu | FWD | 17 | 4.9 | 2.55 | 6.98 | 11.38 | 7.00 | 58.8 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 9.35 | 25.96 | 42.61 | 29.00 | 125.1 | 177.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.3 | 7.36 | 20.53 | 34.12 | 6.00 | 96.4 | 89.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.8 | 5.74 | 16.62 | 27.27 | 2.00 | 87.8 | 90.0 |
| XI | XI | Amad Diallo | MID | 14 | 5.6 | 4.84 | 13.77 | 22.33 | 2.00 | 87.8 | 90.0 |
| XI | XI | Noni Madueke | MID | 6 | 6.1 | 4.78 | 12.77 | 20.04 | 2.00 | 73.3 | 60.0 |

## GW25

- Train rows: 150166
- Bank: 0.20 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 84.81
- Actual score: 92.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (14.61) beats the best remaining Triple Captain opportunity (9.44).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Jamie Vardy -> Iliman Ndiaye (projected gain 4.15, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (14.61) beats the best remaining Triple Captain opportunity (9.44).
- Autosub: Lewis Hall replaced Amad Diallo.
- Autosub: Paul Onuachu replaced Iliman Ndiaye.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.0 | 4.60 | 13.06 | 20.26 | 3.00 | 119.1 | 90.0 |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.5 | 3.49 | 10.10 | 16.95 | 7.00 | 80.3 | 90.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 12 | 7.3 | 6.78 | 17.51 | 28.00 | 13.00 | 125.0 | 128.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 6.19 | 15.51 | 24.14 | 2.00 | 146.3 | 180.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.77 | 11.60 | 19.23 | 2.00 | 86.5 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.8 | 3.90 | 11.30 | 18.33 | 1.00 | 84.0 | 90.0 |
| Bench 2 | Autosub In | Lewis Hall | DEF | 15 | 5.1 | 3.10 | 9.65 | 15.85 | 0.00 | 75.4 | 90.0 |
| XI | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 4.21 | 12.11 | 18.82 | 0.00 | 88.8 | 0.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 2.65 | 8.23 | 13.99 | 1.00 | 55.3 | 17.0 |
| Bench 3 | Autosub In | Paul Onuachu | FWD | 17 | 4.9 | 2.94 | 7.99 | 12.94 | 5.00 | 69.9 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 11.58 | 30.71 | 49.77 | 20.00 | 177.3 | 180.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 6.67 | 20.01 | 33.00 | 2.00 | 94.5 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.8 | 6.35 | 18.07 | 29.16 | 3.00 | 86.0 | 90.0 |
| XI | Bench | Amad Diallo | MID | 14 | 5.6 | 4.17 | 12.90 | 21.16 | 0.00 | 77.7 | 0.0 |
| XI | XI | Noni Madueke | MID | 6 | 6.1 | 3.42 | 10.32 | 16.52 | 1.00 | 57.6 | 20.0 |

## GW26

- Train rows: 150945
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 66.03
- Actual score: 87.00
- Transfer: Amad Diallo -> Morgan Rogers (projected gain 5.58, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.27 | 11.42 | 18.63 | 2.00 | 85.4 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 5.0 | 3.72 | 10.41 | 17.14 | 1.00 | 96.9 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.3 | 5.93 | 17.96 | 29.41 | 6.00 | 110.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 4.79 | 14.30 | 22.92 | 6.00 | 129.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.75 | 11.36 | 18.47 | 1.00 | 84.2 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.8 | 3.23 | 10.21 | 17.00 | 13.00 | 83.7 | 90.0 |
| Bench 2 | Bench | Lewis Hall | DEF | 15 | 5.1 | 2.77 | 8.64 | 14.31 | 9.00 | 72.5 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 3.01 | 8.64 | 13.80 | 1.00 | 72.8 | 18.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 2.85 | 8.15 | 13.75 | 12.00 | 44.3 | 90.0 |
| Bench 4 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 2.33 | 6.73 | 12.00 | 0.00 | 44.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.47 | 30.80 | 50.49 | 14.00 | 163.8 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 6.38 | 19.02 | 31.61 | 2.00 | 94.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.8 | 5.80 | 16.49 | 26.32 | 14.00 | 85.1 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 5.07 | 14.20 | 21.70 | 2.00 | 100.4 | 77.0 |
| Bench 3 | Bench | Noni Madueke | MID | 6 | 6.1 | 2.74 | 8.28 | 13.86 | 0.00 | 42.0 | 0.0 |

## GW27

- Train rows: 151728
- Bank: 0.10 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 65.65
- Actual score: 68.00
- Transfer: Noni Madueke -> Justin Kluivert (projected gain 4.23, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.29 | 10.14 | 16.72 | 6.00 | 84.7 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 5.0 | 3.28 | 9.99 | 16.34 | 2.00 | 94.5 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.3 | 5.65 | 16.76 | 27.69 | 6.00 | 98.9 | 76.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 4.23 | 12.63 | 20.63 | 7.00 | 108.2 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.8 | 3.94 | 10.87 | 17.90 | 4.00 | 85.2 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.48 | 10.59 | 17.34 | 0.00 | 83.2 | 18.0 |
| Bench 2 | Bench | Lewis Hall | DEF | 15 | 5.0 | 2.93 | 9.40 | 15.69 | 1.00 | 81.9 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 3.59 | 10.38 | 17.16 | 8.00 | 68.2 | 71.0 |
| Bench 3 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 1.90 | 6.36 | 10.74 | 0.00 | 47.3 | 58.0 |
| Bench 4 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 1.39 | 5.60 | 10.16 | 0.00 | 31.2 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.32 | 30.19 | 49.82 | 6.00 | 142.1 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 6.50 | 18.41 | 30.53 | 3.00 | 91.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.8 | 6.09 | 17.48 | 28.32 | 5.00 | 90.6 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.0 | 4.36 | 13.53 | 21.70 | 10.00 | 70.2 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 3.87 | 10.45 | 17.40 | 7.00 | 79.2 | 90.0 |