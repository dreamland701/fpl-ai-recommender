# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 366.17
- Total actual points: 339.00
- Average predicted points: 91.54
- Average actual points: 84.75
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
- Predicted score: 113.69
- Actual score: 114.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.03) beats the best remaining Bench Boost opportunity (13.77).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.03) beats the best remaining Bench Boost opportunity (13.77).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 7.31 | 11.93 | 18.72 | 10.00 | 180.0 | 180.0 |
| Bench 1 | Bench Boost | John Ruddy | GK | 15 | 3.9 | 0.11 | 0.41 | 0.76 | 0.00 | 4.2 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 10.51 | 16.85 | 25.99 | 7.00 | 180.0 | 98.0 |
| XI | XI | Lewis Hall | DEF | 15 | 5.1 | 3.73 | 11.07 | 17.78 | 1.00 | 80.2 | 86.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 6.49 | 10.68 | 16.65 | 7.00 | 179.5 | 177.0 |
| Bench 3 | Bench Boost | Dean Huijsen | DEF | 3 | 4.4 | 2.72 | 8.53 | 13.87 | 0.00 | 83.4 | 90.0 |
| Bench 2 | Bench Boost | Jan Bednarek | DEF | 17 | 4.0 | 2.95 | 7.92 | 12.72 | 1.00 | 88.9 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 6.79 | 20.10 | 33.40 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cody Gakpo | FWD | 12 | 7.6 | 11.95 | 18.42 | 27.72 | 7.00 | 180.0 | 137.0 |
| XI | XI | Iliman Ndiaye | FWD | 8 | 5.5 | 7.65 | 12.43 | 19.31 | 9.00 | 174.7 | 114.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 16.90 | 26.60 | 43.10 | 29.00 | 180.0 | 177.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 7.19 | 19.25 | 32.35 | 6.00 | 90.0 | 89.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.04 | 16.26 | 26.69 | 2.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 4.31 | 13.49 | 21.08 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench Boost | Harry Winks | MID | 11 | 4.4 | 2.14 | 6.16 | 9.90 | 2.00 | 65.1 | 90.0 |

## GW25

- Train rows: 150166
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 119.67
- Actual score: 93.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (23.50) beats the best remaining Triple Captain opportunity (11.61).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (23.50) beats the best remaining Triple Captain opportunity (11.61).
- Autosub: Jan Bednarek replaced Cody Gakpo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.94 | 11.30 | 17.60 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | John Ruddy | GK | 15 | 3.9 | 0.00 | 0.22 | 0.42 | 0.00 | 5.6 | 0.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 10.42 | 16.19 | 26.21 | 13.00 | 178.4 | 128.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.72 | 10.79 | 16.66 | 2.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 5.1 | 2.96 | 9.43 | 15.67 | 0.00 | 75.7 | 90.0 |
| XI | XI | Dean Huijsen | DEF | 3 | 4.4 | 3.21 | 8.70 | 13.84 | 2.00 | 81.9 | 90.0 |
| Bench 2 | Autosub In | Jan Bednarek | DEF | 17 | 4.0 | 2.38 | 7.09 | 11.43 | 1.00 | 85.5 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.93 | 18.25 | 30.60 | 2.00 | 89.2 | 89.0 |
| XI | Bench | Cody Gakpo | FWD | 12 | 7.6 | 9.94 | 14.92 | 22.89 | 0.00 | 149.5 | 0.0 |
| Bench 3 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 2.36 | 7.85 | 12.99 | 0.00 | 60.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 20.48 | 29.84 | 48.60 | 20.00 | 180.0 | 180.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.2 | 6.73 | 19.37 | 32.02 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.57 | 15.23 | 24.98 | 3.00 | 83.7 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 5.83 | 15.16 | 23.03 | 5.00 | 85.4 | 76.0 |
| Bench 4 | Bench | Harry Winks | MID | 11 | 4.4 | 1.97 | 6.27 | 10.31 | 0.00 | 70.3 | 0.0 |

## GW26

- Train rows: 150945
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 66.76
- Actual score: 83.00
- Transfer: Cody Gakpo -> Chris Wood (projected gain 8.66, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.61 | 10.30 | 16.91 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | John Ruddy | GK | 15 | 3.9 | 0.01 | 0.26 | 0.48 | 0.00 | 6.5 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.87 | 17.33 | 28.01 | 6.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 5.0 | 3.07 | 9.43 | 15.64 | 9.00 | 80.3 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.21 | 9.20 | 15.21 | 1.00 | 88.6 | 90.0 |
| XI | XI | Dean Huijsen | DEF | 3 | 4.4 | 2.56 | 7.66 | 12.41 | 2.00 | 80.2 | 90.0 |
| Bench 2 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 2.45 | 7.17 | 11.69 | 1.00 | 84.9 | 11.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 6.06 | 17.99 | 29.55 | 13.00 | 90.0 | 86.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 5.35 | 15.72 | 25.95 | 5.00 | 87.5 | 90.0 |
| Bench 3 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 1.47 | 5.02 | 10.09 | 0.00 | 27.3 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.24 | 30.41 | 49.62 | 14.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.1 | 6.06 | 18.55 | 30.40 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.11 | 17.39 | 27.00 | 14.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 4.36 | 12.62 | 20.02 | 2.00 | 68.9 | 72.0 |
| Bench 4 | Bench | Harry Winks | MID | 11 | 4.4 | 1.41 | 4.36 | 7.74 | 0.00 | 40.7 | 0.0 |

## GW27

- Train rows: 151728
- Bank: 0.50 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 66.05
- Actual score: 49.00
- Transfer: none
- No transfer was applied this week.
- Autosub: Harry Winks replaced Alexander Isak.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.25 | 9.73 | 15.92 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | John Ruddy | GK | 15 | 3.9 | 0.00 | 0.10 | 0.31 | 0.00 | 6.1 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.63 | 16.09 | 26.74 | 6.00 | 90.0 | 76.0 |
| XI | XI | Lewis Hall | DEF | 15 | 5.0 | 3.15 | 9.87 | 16.62 | 1.00 | 86.0 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 2.95 | 8.74 | 14.40 | 6.00 | 86.8 | 90.0 |
| XI | XI | Dean Huijsen | DEF | 3 | 4.4 | 2.39 | 7.26 | 11.74 | 1.00 | 80.2 | 90.0 |
| Bench 3 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.91 | 3.68 | 7.04 | 0.00 | 40.8 | 0.0 |
| XI | Bench | Alexander Isak | FWD | 15 | 9.5 | 5.55 | 18.22 | 29.37 | 0.00 | 90.0 | 0.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 4.78 | 15.14 | 26.28 | 2.00 | 90.0 | 84.0 |
| Bench 4 | Bench | Iliman Ndiaye | FWD | 8 | 5.4 | 0.77 | 4.40 | 8.79 | 0.00 | 18.6 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.62 | 29.89 | 49.29 | 6.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 7.09 | 19.34 | 30.91 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.10 | 18.43 | 28.80 | 5.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 3.93 | 11.75 | 18.93 | 10.00 | 67.0 | 90.0 |
| Bench 2 | Autosub In | Harry Winks | MID | 11 | 4.4 | 1.26 | 3.70 | 6.60 | 1.00 | 33.3 | 29.0 |