# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 333.22
- Total actual points: 319.00
- Average predicted points: 83.30
- Average actual points: 79.75
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
- Predicted score: 102.90
- Actual score: 112.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (12.11) beats the best remaining Bench Boost opportunity (12.44).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (12.11) beats the best remaining Bench Boost opportunity (12.44).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 6.28 | 10.41 | 16.43 | 10.00 | 165.4 | 180.0 |
| Bench 1 | Bench Boost | Daniel Iversen | GK | 11 | 3.9 | 0.18 | 0.55 | 1.00 | 0.00 | 7.8 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 9.00 | 15.18 | 24.12 | 7.00 | 165.4 | 98.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.52 | 10.73 | 17.69 | 4.00 | 82.4 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 5.1 | 3.63 | 10.42 | 16.70 | 1.00 | 78.4 | 86.0 |
| Bench 3 | Bench Boost | Jan Bednarek | DEF | 17 | 4.0 | 2.43 | 6.60 | 11.07 | 1.00 | 81.8 | 90.0 |
| Bench 2 | Bench Boost | Jacob Greaves | DEF | 10 | 3.9 | 2.56 | 6.39 | 9.97 | 1.00 | 70.6 | 90.0 |
| Vice Captain | XI | Cody Gakpo | FWD | 12 | 7.6 | 11.57 | 18.47 | 27.81 | 7.00 | 169.5 | 137.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 6.20 | 18.20 | 30.87 | 2.00 | 82.7 | 90.0 |
| XI | XI | Iliman Ndiaye | FWD | 8 | 5.5 | 7.63 | 12.21 | 18.57 | 9.00 | 169.3 | 114.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 15.64 | 24.60 | 40.60 | 29.00 | 165.4 | 177.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 6.78 | 18.04 | 31.09 | 6.00 | 82.7 | 89.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.48 | 15.07 | 25.13 | 2.00 | 82.7 | 90.0 |
| XI | XI | Amad Diallo | MID | 14 | 5.6 | 4.08 | 12.26 | 19.94 | 2.00 | 83.1 | 90.0 |
| Bench 4 | Bench Boost | Harry Winks | MID | 11 | 4.4 | 2.27 | 6.56 | 10.67 | 2.00 | 68.4 | 90.0 |

## GW25

- Train rows: 150166
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cody Gakpo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 108.06
- Actual score: 87.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (22.26) beats the best remaining Triple Captain opportunity (10.90).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (22.26) beats the best remaining Triple Captain opportunity (10.90).
- Autosub: Jacob Greaves replaced Amad Diallo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.20 | 9.79 | 15.88 | 3.00 | 82.7 | 90.0 |
| Bench 1 | Bench | Daniel Iversen | GK | 11 | 3.9 | 0.00 | 0.20 | 0.53 | 0.00 | 7.1 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 9.03 | 14.42 | 24.00 | 13.00 | 161.4 | 128.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.16 | 9.41 | 16.06 | 2.00 | 79.4 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 5.1 | 2.83 | 8.77 | 14.78 | 0.00 | 74.8 | 90.0 |
| XI | XI | Jan Bednarek | DEF | 17 | 4.0 | 2.42 | 7.15 | 11.67 | 1.00 | 83.6 | 90.0 |
| Bench 4 | Autosub In | Jacob Greaves | DEF | 10 | 3.9 | 1.91 | 5.87 | 9.58 | 1.00 | 70.8 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.26 | 16.10 | 27.89 | 2.00 | 82.2 | 89.0 |
| Vice Captain | Bench | Cody Gakpo | FWD | 12 | 7.6 | 9.14 | 15.08 | 23.44 | 0.00 | 142.9 | 0.0 |
| Bench 2 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 2.33 | 8.38 | 13.72 | 0.00 | 59.3 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 19.23 | 27.85 | 46.24 | 20.00 | 165.4 | 180.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.2 | 6.15 | 17.76 | 30.00 | 2.00 | 82.7 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.58 | 15.57 | 25.46 | 3.00 | 81.8 | 90.0 |
| XI | Bench | Amad Diallo | MID | 14 | 5.6 | 3.58 | 10.96 | 18.52 | 0.00 | 74.0 | 0.0 |
| Bench 3 | Bench | Harry Winks | MID | 11 | 4.4 | 2.06 | 6.49 | 10.79 | 0.00 | 73.2 | 0.0 |

## GW26

- Train rows: 150945
- Bank: 0.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 59.69
- Actual score: 80.00
- Transfer: Cody Gakpo -> Jean-Philippe Mateta (projected gain 9.93, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.14 | 8.84 | 14.94 | 1.00 | 82.7 | 90.0 |
| Bench 1 | Bench | Daniel Iversen | GK | 11 | 3.9 | 0.23 | 0.53 | 0.90 | 0.00 | 7.5 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.04 | 15.42 | 25.62 | 6.00 | 82.7 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.12 | 9.45 | 15.69 | 1.00 | 79.5 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 5.0 | 2.98 | 9.07 | 15.04 | 9.00 | 79.2 | 90.0 |
| XI | XI | Jan Bednarek | DEF | 17 | 4.0 | 2.53 | 7.40 | 11.95 | 1.00 | 83.3 | 11.0 |
| XI | XI | Jacob Greaves | DEF | 10 | 3.9 | 2.44 | 6.47 | 10.47 | 0.00 | 79.0 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 5.57 | 16.46 | 27.74 | 13.00 | 82.7 | 86.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.3 | 4.31 | 14.22 | 23.16 | 5.00 | 79.8 | 90.0 |
| Bench 2 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 1.37 | 4.94 | 9.55 | 0.00 | 25.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 9.73 | 28.41 | 46.89 | 14.00 | 82.7 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.1 | 5.57 | 16.74 | 28.33 | 2.00 | 82.7 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.53 | 15.29 | 24.31 | 14.00 | 82.7 | 90.0 |
| Bench 3 | Bench | Harry Winks | MID | 11 | 4.4 | 1.36 | 4.21 | 7.39 | 0.00 | 40.9 | 0.0 |
| Bench 4 | Bench | Amad Diallo | MID | 14 | 5.5 | 0.51 | 3.90 | 8.67 | 0.00 | 13.2 | 0.0 |

## GW27

- Train rows: 151728
- Bank: 0.30 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 62.57
- Actual score: 40.00
- Transfer: Amad Diallo -> Antoine Semenyo (projected gain 7.83, hit 0)
- Autosub: Harry Winks replaced Alexander Isak.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 2.63 | 8.21 | 13.92 | 2.00 | 82.6 | 90.0 |
| Bench 1 | Bench | Daniel Iversen | GK | 11 | 3.9 | 0.32 | 0.59 | 0.92 | 0.00 | 7.4 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.24 | 14.74 | 24.84 | 6.00 | 82.6 | 76.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.47 | 10.14 | 16.39 | 0.00 | 82.4 | 18.0 |
| XI | XI | Lewis Hall | DEF | 15 | 5.0 | 3.05 | 9.41 | 15.84 | 1.00 | 83.7 | 90.0 |
| XI | XI | Jacob Greaves | DEF | 10 | 3.9 | 2.20 | 6.26 | 10.00 | 1.00 | 76.9 | 90.0 |
| Bench 3 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.83 | 3.93 | 7.13 | 0.00 | 40.0 | 0.0 |
| XI | Bench | Alexander Isak | FWD | 15 | 9.5 | 4.92 | 15.92 | 26.64 | 0.00 | 82.6 | 0.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.3 | 4.95 | 14.78 | 23.81 | 8.00 | 83.8 | 90.0 |
| Bench 4 | Bench | Iliman Ndiaye | FWD | 8 | 5.4 | 0.61 | 4.10 | 8.02 | 0.00 | 15.5 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.26 | 28.24 | 46.82 | 6.00 | 82.6 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 6.58 | 17.68 | 29.43 | 3.00 | 82.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.36 | 16.22 | 26.08 | 5.00 | 82.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 3 | 5.7 | 3.64 | 10.83 | 17.26 | 1.00 | 78.1 | 90.0 |
| Bench 2 | Autosub In | Harry Winks | MID | 11 | 4.4 | 1.20 | 3.47 | 6.16 | 1.00 | 33.5 | 29.0 |