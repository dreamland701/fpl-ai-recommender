# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 336.99
- Total actual points: 313.00
- Average predicted points: 84.25
- Average actual points: 78.25
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
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Cody Gakpo
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 103.79
- Actual score: 112.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (12.46) beats the best remaining Bench Boost opportunity (12.81).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (12.46) beats the best remaining Bench Boost opportunity (12.81).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 6.56 | 10.74 | 16.66 | 10.00 | 166.5 | 180.0 |
| Bench 1 | Bench Boost | Daniel Bentley | GK | 20 | 3.9 | 0.35 | 0.81 | 1.38 | 0.00 | 10.0 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 9.28 | 15.50 | 24.35 | 7.00 | 166.5 | 98.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.35 | 10.48 | 17.40 | 4.00 | 81.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 5.1 | 3.62 | 10.45 | 16.83 | 1.00 | 77.5 | 86.0 |
| Bench 3 | Bench Boost | Jan Bednarek | DEF | 17 | 4.0 | 2.57 | 6.92 | 11.30 | 1.00 | 82.3 | 90.0 |
| Bench 2 | Bench Boost | Jacob Greaves | DEF | 10 | 3.9 | 2.58 | 6.43 | 10.03 | 1.00 | 70.9 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 6.34 | 18.53 | 31.10 | 2.00 | 83.2 | 90.0 |
| Vice Captain | XI | Cody Gakpo | FWD | 12 | 7.6 | 11.24 | 18.22 | 27.52 | 7.00 | 166.8 | 137.0 |
| XI | XI | Iliman Ndiaye | FWD | 8 | 5.5 | 7.30 | 11.96 | 18.29 | 9.00 | 166.6 | 114.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 15.92 | 24.93 | 40.83 | 29.00 | 166.5 | 177.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 6.92 | 18.37 | 31.32 | 6.00 | 83.2 | 89.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.63 | 15.40 | 25.36 | 2.00 | 83.2 | 90.0 |
| XI | XI | Amad Diallo | MID | 14 | 5.6 | 3.92 | 12.01 | 19.65 | 2.00 | 81.7 | 90.0 |
| Bench 4 | Bench Boost | Harry Winks | MID | 11 | 4.4 | 2.29 | 6.60 | 10.73 | 2.00 | 68.7 | 90.0 |

## GW25

- Train rows: 150166
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 109.45
- Actual score: 87.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (22.53) beats the best remaining Triple Captain opportunity (11.06).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (22.53) beats the best remaining Triple Captain opportunity (11.06).
- Autosub: Jacob Greaves replaced Amad Diallo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.34 | 10.13 | 16.14 | 3.00 | 83.2 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.00 | 0.44 | 1.00 | 0.00 | 9.5 | 0.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 9.31 | 14.76 | 24.26 | 13.00 | 162.4 | 128.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.30 | 9.75 | 16.32 | 2.00 | 79.9 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 5.1 | 2.82 | 8.78 | 14.90 | 0.00 | 73.7 | 90.0 |
| XI | XI | Jan Bednarek | DEF | 17 | 4.0 | 2.27 | 6.93 | 11.40 | 1.00 | 82.4 | 90.0 |
| Bench 4 | Autosub In | Jacob Greaves | DEF | 10 | 3.9 | 1.93 | 5.91 | 9.63 | 1.00 | 71.2 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.40 | 16.44 | 28.15 | 2.00 | 82.7 | 89.0 |
| XI | Bench | Cody Gakpo | FWD | 12 | 7.6 | 9.18 | 15.12 | 23.49 | 0.00 | 143.6 | 0.0 |
| Bench 2 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 2.16 | 7.93 | 13.01 | 0.00 | 55.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 19.51 | 28.19 | 46.50 | 20.00 | 166.4 | 180.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.2 | 6.29 | 18.10 | 30.26 | 2.00 | 83.2 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.42 | 15.35 | 25.18 | 3.00 | 80.7 | 90.0 |
| XI | Bench | Amad Diallo | MID | 14 | 5.6 | 3.60 | 10.99 | 18.57 | 0.00 | 74.4 | 0.0 |
| Bench 3 | Bench | Harry Winks | MID | 11 | 4.4 | 2.08 | 6.52 | 10.84 | 0.00 | 73.5 | 0.0 |

## GW26

- Train rows: 150945
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 61.12
- Actual score: 80.00
- Transfer: Cody Gakpo -> Chris Wood (projected gain 9.85, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.27 | 9.17 | 15.22 | 1.00 | 83.2 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.22 | 0.68 | 1.28 | 0.00 | 9.5 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.18 | 15.75 | 25.90 | 6.00 | 83.2 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.25 | 9.78 | 15.97 | 1.00 | 79.9 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 5.0 | 2.96 | 9.06 | 15.16 | 9.00 | 78.1 | 90.0 |
| XI | XI | Jan Bednarek | DEF | 17 | 4.0 | 2.39 | 7.19 | 11.67 | 1.00 | 82.2 | 11.0 |
| XI | XI | Jacob Greaves | DEF | 10 | 3.9 | 2.42 | 6.47 | 10.59 | 0.00 | 77.9 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 5.70 | 16.79 | 28.02 | 13.00 | 83.2 | 86.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 4.87 | 14.25 | 23.38 | 5.00 | 79.5 | 90.0 |
| Bench 2 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 1.43 | 5.03 | 9.63 | 0.00 | 26.3 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 9.87 | 28.74 | 47.17 | 14.00 | 83.2 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.1 | 5.70 | 17.07 | 28.61 | 2.00 | 83.2 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.66 | 15.62 | 24.59 | 14.00 | 83.2 | 90.0 |
| Bench 3 | Bench | Harry Winks | MID | 11 | 4.4 | 1.41 | 4.31 | 7.52 | 0.00 | 41.9 | 0.0 |
| Bench 4 | Bench | Amad Diallo | MID | 14 | 5.5 | 0.56 | 3.99 | 8.76 | 0.00 | 14.1 | 0.0 |

## GW27

- Train rows: 151728
- Bank: 0.50 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 62.62
- Actual score: 34.00
- Transfer: Amad Diallo -> Antoine Semenyo (projected gain 7.72, hit 0)
- Autosub: Harry Winks replaced Alexander Isak.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 2.77 | 8.53 | 14.21 | 2.00 | 83.1 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.36 | 0.89 | 1.46 | 0.00 | 8.6 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.37 | 15.06 | 25.13 | 6.00 | 83.1 | 76.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.34 | 9.96 | 16.17 | 0.00 | 81.5 | 18.0 |
| XI | XI | Lewis Hall | DEF | 15 | 5.0 | 2.92 | 9.24 | 15.62 | 1.00 | 82.8 | 90.0 |
| XI | XI | Jacob Greaves | DEF | 10 | 3.9 | 2.19 | 6.27 | 10.12 | 1.00 | 75.8 | 90.0 |
| Bench 3 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.89 | 4.02 | 7.21 | 0.00 | 40.9 | 0.0 |
| XI | Bench | Alexander Isak | FWD | 15 | 9.5 | 5.05 | 16.24 | 26.92 | 0.00 | 83.1 | 0.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 4.35 | 13.95 | 24.08 | 2.00 | 83.1 | 84.0 |
| Bench 4 | Bench | Iliman Ndiaye | FWD | 8 | 5.4 | 0.66 | 4.19 | 8.10 | 0.00 | 16.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.39 | 28.56 | 47.10 | 6.00 | 83.1 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 6.72 | 18.00 | 29.71 | 3.00 | 83.1 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.49 | 16.53 | 26.36 | 5.00 | 83.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 3 | 5.7 | 3.64 | 10.85 | 17.38 | 1.00 | 77.0 | 90.0 |
| Bench 2 | Autosub In | Harry Winks | MID | 11 | 4.4 | 1.25 | 3.58 | 6.29 | 1.00 | 34.5 | 29.0 |