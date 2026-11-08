# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 299.09
- Total actual points: 338.00
- Average predicted points: 74.77
- Average actual points: 84.50
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
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 79.94
- Actual score: 116.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (17.09) beats the best remaining Bench Boost opportunity (17.35).
- Chip advisory: bench_boost (0.58): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.66): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (17.09) beats the best remaining Bench Boost opportunity (17.35).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench Boost | David Raya Martin | GK | 1 | 5.6 | 3.52 | 10.60 | 17.66 | 3.00 | 87.7 | 90.0 |
| XI | XI | Jordan Pickford | GK | 8 | 5.0 | 3.91 | 10.34 | 16.34 | 10.00 | 112.7 | 180.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.3 | 6.30 | 16.54 | 26.06 | 7.00 | 114.6 | 98.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.98 | 12.36 | 20.54 | 4.00 | 90.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 4.98 | 12.30 | 19.49 | 6.00 | 106.1 | 180.0 |
| XI | XI | Lewis Hall | DEF | 15 | 5.1 | 4.08 | 11.55 | 18.32 | 1.00 | 81.6 | 86.0 |
| Bench 2 | Bench Boost | Ola Aina | DEF | 16 | 5.4 | 3.74 | 11.19 | 18.26 | 6.00 | 83.6 | 90.0 |
| Bench 3 | Bench Boost | João Pedro Junqueira de Jesus | FWD | 5 | 5.6 | 3.17 | 10.05 | 16.40 | 1.00 | 71.4 | 45.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.5 | 3.37 | 9.32 | 15.15 | 1.00 | 68.3 | 59.0 |
| Bench 4 | Bench Boost | Paul Onuachu | FWD | 17 | 4.9 | 2.45 | 6.78 | 11.08 | 7.00 | 58.7 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 9.47 | 25.73 | 42.21 | 29.00 | 123.4 | 177.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.3 | 6.48 | 18.91 | 31.66 | 6.00 | 90.8 | 89.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.8 | 5.84 | 16.91 | 27.76 | 2.00 | 90.5 | 90.0 |
| XI | XI | Amad Diallo | MID | 14 | 5.6 | 4.82 | 13.78 | 22.42 | 2.00 | 90.3 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.6 | 4.36 | 13.37 | 21.73 | 2.00 | 86.1 | 90.0 |

## GW25

- Train rows: 150166
- Bank: 0.10 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 86.00
- Actual score: 96.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (14.72) beats the best remaining Triple Captain opportunity (9.14).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Jamie Vardy -> Iliman Ndiaye (projected gain 2.93, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (14.72) beats the best remaining Triple Captain opportunity (9.14).
- Autosub: Lewis Hall replaced Amad Diallo.
- Autosub: Paul Onuachu replaced Iliman Ndiaye.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.0 | 4.51 | 12.81 | 19.88 | 3.00 | 117.7 | 90.0 |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.5 | 3.60 | 10.46 | 17.54 | 7.00 | 83.0 | 90.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 12 | 7.3 | 6.91 | 18.03 | 28.76 | 13.00 | 125.8 | 128.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 6.16 | 15.48 | 24.06 | 2.00 | 145.1 | 180.0 |
| XI | XI | Ola Aina | DEF | 16 | 5.4 | 4.09 | 12.12 | 20.07 | 1.00 | 89.6 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.96 | 12.06 | 19.99 | 2.00 | 90.2 | 90.0 |
| Bench 2 | Autosub In | Lewis Hall | DEF | 15 | 5.1 | 3.27 | 10.10 | 16.58 | 0.00 | 78.4 | 90.0 |
| XI | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 4.00 | 11.46 | 17.81 | 0.00 | 85.7 | 0.0 |
| Bench 3 | Autosub In | Paul Onuachu | FWD | 17 | 4.9 | 3.16 | 8.57 | 13.84 | 5.00 | 72.2 | 90.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 2.76 | 8.53 | 14.48 | 1.00 | 57.2 | 17.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 11.69 | 31.30 | 50.58 | 20.00 | 176.8 | 180.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 6.47 | 19.19 | 31.76 | 2.00 | 91.7 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.8 | 5.59 | 16.42 | 26.62 | 3.00 | 84.4 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.7 | 4.90 | 14.22 | 22.82 | 5.00 | 78.2 | 76.0 |
| XI | Bench | Amad Diallo | MID | 14 | 5.6 | 4.35 | 13.35 | 21.90 | 0.00 | 80.6 | 0.0 |

## GW26

- Train rows: 150945
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 67.67
- Actual score: 64.00
- Transfer: Amad Diallo -> Morgan Rogers (projected gain 6.00, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.84 | 10.80 | 17.72 | 2.00 | 85.9 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 5.0 | 3.79 | 10.57 | 17.37 | 1.00 | 97.0 | 90.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 12 | 7.3 | 6.06 | 18.15 | 29.74 | 6.00 | 112.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 4.68 | 13.97 | 22.38 | 6.00 | 127.1 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.89 | 11.76 | 19.14 | 1.00 | 87.2 | 90.0 |
| XI | XI | Ola Aina | DEF | 16 | 5.4 | 3.52 | 10.92 | 18.14 | 0.00 | 86.6 | 90.0 |
| Bench 3 | Bench | Lewis Hall | DEF | 15 | 5.1 | 2.93 | 9.06 | 15.00 | 9.00 | 75.2 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 3.13 | 8.88 | 14.24 | 1.00 | 75.6 | 18.0 |
| Bench 2 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 3.01 | 8.60 | 14.50 | 12.00 | 47.3 | 90.0 |
| Bench 4 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 2.31 | 6.90 | 12.19 | 0.00 | 43.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.45 | 30.41 | 49.86 | 14.00 | 162.8 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.2 | 5.84 | 17.94 | 29.95 | 2.00 | 89.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.8 | 5.99 | 16.91 | 27.04 | 14.00 | 89.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 5.19 | 14.43 | 22.11 | 2.00 | 102.2 | 77.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.7 | 4.63 | 14.38 | 22.81 | 2.00 | 69.6 | 72.0 |

## GW27

- Train rows: 151728
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 65.48
- Actual score: 62.00
- Transfer: Iliman Ndiaye -> Norberto Bercique Gomes Betuncal (projected gain 1.20, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.5 | 3.33 | 10.30 | 16.98 | 6.00 | 85.6 | 90.0 |
| XI | XI | Jordan Pickford | GK | 8 | 5.0 | 3.40 | 10.20 | 16.67 | 2.00 | 94.9 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.3 | 5.57 | 16.87 | 27.90 | 6.00 | 101.6 | 76.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 4.07 | 12.36 | 20.20 | 7.00 | 107.2 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.73 | 11.22 | 18.37 | 0.00 | 87.0 | 18.0 |
| Bench 2 | Bench | Ola Aina | DEF | 16 | 5.4 | 3.33 | 10.37 | 17.46 | 6.00 | 87.3 | 90.0 |
| Bench 3 | Bench | Lewis Hall | DEF | 15 | 5.0 | 3.09 | 9.78 | 16.33 | 1.00 | 84.4 | 90.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.9 | 4.23 | 11.46 | 18.34 | 2.00 | 83.8 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 3.86 | 11.07 | 18.27 | 8.00 | 71.7 | 71.0 |
| Bench 4 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 2.07 | 6.85 | 11.54 | 0.00 | 50.5 | 58.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 9.74 | 28.73 | 47.69 | 6.00 | 141.8 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.8 | 6.23 | 18.35 | 29.61 | 5.00 | 93.5 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 6.28 | 17.80 | 29.54 | 3.00 | 88.9 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 4.60 | 13.98 | 22.49 | 10.00 | 74.1 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 4.03 | 11.16 | 18.47 | 7.00 | 81.8 | 90.0 |