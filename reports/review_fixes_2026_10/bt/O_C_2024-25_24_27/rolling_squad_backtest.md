# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 299.32
- Total actual points: 338.00
- Average predicted points: 74.83
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
- Predicted score: 79.90
- Actual score: 116.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (17.10) beats the best remaining Bench Boost opportunity (17.31).
- Chip advisory: bench_boost (0.58): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.66): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (17.10) beats the best remaining Bench Boost opportunity (17.31).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench Boost | David Raya Martin | GK | 1 | 5.6 | 3.53 | 10.66 | 17.75 | 3.00 | 87.7 | 90.0 |
| XI | XI | Jordan Pickford | GK | 8 | 5.0 | 3.91 | 10.41 | 16.47 | 10.00 | 112.7 | 180.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.3 | 6.27 | 16.45 | 26.02 | 7.00 | 114.6 | 98.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 4.00 | 12.42 | 20.68 | 4.00 | 90.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 4.95 | 12.31 | 19.57 | 6.00 | 106.1 | 180.0 |
| XI | XI | Lewis Hall | DEF | 15 | 5.1 | 4.07 | 11.57 | 18.37 | 1.00 | 81.6 | 86.0 |
| Bench 2 | Bench Boost | Ola Aina | DEF | 16 | 5.4 | 3.72 | 11.20 | 18.33 | 6.00 | 83.6 | 90.0 |
| Bench 3 | Bench Boost | João Pedro Junqueira de Jesus | FWD | 5 | 5.6 | 3.19 | 10.14 | 16.57 | 1.00 | 71.4 | 45.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.5 | 3.36 | 9.44 | 15.42 | 1.00 | 68.3 | 59.0 |
| Bench 4 | Bench Boost | Paul Onuachu | FWD | 17 | 4.9 | 2.44 | 6.77 | 11.02 | 7.00 | 58.7 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 9.44 | 26.01 | 42.69 | 29.00 | 123.4 | 177.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.3 | 6.52 | 19.01 | 31.87 | 6.00 | 90.8 | 89.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.8 | 5.87 | 17.05 | 27.98 | 2.00 | 90.5 | 90.0 |
| XI | XI | Amad Diallo | MID | 14 | 5.6 | 4.81 | 13.78 | 22.55 | 2.00 | 90.3 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.6 | 4.37 | 13.30 | 21.68 | 2.00 | 86.1 | 90.0 |

## GW25

- Train rows: 150166
- Bank: 0.10 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 86.23
- Actual score: 96.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (14.75) beats the best remaining Triple Captain opportunity (9.11).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Jamie Vardy -> Iliman Ndiaye (projected gain 2.96, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (14.75) beats the best remaining Triple Captain opportunity (9.11).
- Autosub outfielders: Lewis Hall, Paul Onuachu.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 4.50 | 12.89 | 20.11 | 3.00 | 117.7 | 90.0 |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.5 | 3.60 | 10.47 | 17.61 | 7.00 | 83.0 | 90.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 6.94 | 18.10 | 28.85 | 13.00 | 125.7 | 128.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 6.20 | 15.58 | 24.22 | 2.00 | 145.1 | 180.0 |
| XI | XI | Ola Aina | DEF | 16 | 5.4 | 4.08 | 12.17 | 20.21 | 1.00 | 89.6 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.99 | 12.15 | 20.16 | 2.00 | 90.1 | 90.0 |
| Bench 2 | Autosub In | Lewis Hall | DEF | 15 | 5.1 | 3.28 | 10.16 | 16.70 | 0.00 | 78.4 | 90.0 |
| XI | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 3.99 | 11.44 | 17.89 | 0.00 | 85.7 | 0.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 2.74 | 8.56 | 14.56 | 1.00 | 57.2 | 17.0 |
| Bench 3 | Autosub In | Paul Onuachu | FWD | 17 | 4.9 | 3.13 | 8.52 | 13.70 | 5.00 | 72.2 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 11.73 | 31.57 | 50.99 | 20.00 | 176.8 | 180.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 6.44 | 19.30 | 31.95 | 2.00 | 91.8 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.62 | 16.59 | 26.96 | 3.00 | 84.4 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 4.92 | 14.25 | 22.92 | 5.00 | 78.1 | 76.0 |
| XI | Bench | Amad Diallo | MID | 14 | 5.6 | 4.37 | 13.49 | 22.14 | 0.00 | 80.6 | 0.0 |

## GW26

- Train rows: 150945
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 67.71
- Actual score: 64.00
- Transfer: Amad Diallo -> Morgan Rogers (projected gain 5.96, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.87 | 10.87 | 17.84 | 2.00 | 85.9 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 5.1 | 3.80 | 10.60 | 17.46 | 1.00 | 97.0 | 90.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 6.07 | 18.15 | 29.91 | 6.00 | 112.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 4.69 | 13.97 | 22.45 | 6.00 | 127.1 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.88 | 11.76 | 19.21 | 1.00 | 87.2 | 90.0 |
| XI | XI | Ola Aina | DEF | 16 | 5.4 | 3.53 | 10.94 | 18.20 | 0.00 | 86.6 | 90.0 |
| Bench 3 | Bench | Lewis Hall | DEF | 15 | 5.1 | 2.95 | 9.05 | 15.03 | 9.00 | 75.2 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 3.11 | 8.87 | 14.17 | 1.00 | 75.7 | 18.0 |
| Bench 2 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 3.03 | 8.60 | 14.52 | 12.00 | 47.3 | 90.0 |
| Bench 4 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 2.32 | 6.90 | 12.24 | 0.00 | 43.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.46 | 30.48 | 49.99 | 14.00 | 162.8 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.2 | 5.81 | 17.96 | 30.03 | 2.00 | 89.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.99 | 16.83 | 27.03 | 14.00 | 89.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 5.17 | 14.39 | 21.99 | 2.00 | 102.2 | 77.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 4.66 | 14.38 | 22.69 | 2.00 | 69.6 | 72.0 |

## GW27

- Train rows: 151728
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 65.49
- Actual score: 62.00
- Transfer: Iliman Ndiaye -> Norberto Bercique Gomes Betuncal (projected gain 1.14, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.5 | 3.35 | 10.29 | 17.02 | 6.00 | 85.5 | 90.0 |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.38 | 10.17 | 16.68 | 2.00 | 95.0 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.59 | 16.80 | 27.88 | 6.00 | 101.5 | 76.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 4.09 | 12.34 | 20.20 | 7.00 | 107.2 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.76 | 11.23 | 18.38 | 0.00 | 86.9 | 18.0 |
| Bench 2 | Bench | Ola Aina | DEF | 16 | 5.4 | 3.30 | 10.33 | 17.39 | 6.00 | 87.4 | 90.0 |
| Bench 3 | Bench | Lewis Hall | DEF | 15 | 5.0 | 3.10 | 9.82 | 16.30 | 1.00 | 84.4 | 90.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.9 | 4.20 | 11.36 | 18.11 | 2.00 | 83.9 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 3.84 | 11.05 | 18.23 | 8.00 | 71.8 | 71.0 |
| Bench 4 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 2.06 | 6.84 | 11.47 | 0.00 | 50.5 | 58.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 9.76 | 28.75 | 47.49 | 6.00 | 141.7 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.22 | 18.34 | 29.61 | 5.00 | 93.5 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 6.30 | 17.83 | 29.46 | 3.00 | 88.9 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.0 | 4.58 | 13.89 | 22.35 | 10.00 | 74.1 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.7 | 4.02 | 11.14 | 18.41 | 7.00 | 81.8 | 90.0 |