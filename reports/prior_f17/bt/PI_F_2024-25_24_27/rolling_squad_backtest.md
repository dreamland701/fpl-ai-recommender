# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 366.80
- Total actual points: 339.00
- Average predicted points: 91.70
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
- Predicted score: 112.22
- Actual score: 117.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.36) beats the best remaining Bench Boost opportunity (14.04).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.36) beats the best remaining Bench Boost opportunity (14.04).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 7.46 | 12.10 | 18.53 | 10.00 | 180.0 | 180.0 |
| Bench 1 | Bench Boost | Daniel Bentley | GK | 20 | 3.9 | 0.43 | 1.08 | 1.91 | 0.00 | 11.4 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 10.09 | 16.79 | 26.14 | 7.00 | 180.0 | 98.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.45 | 10.65 | 17.62 | 4.00 | 83.0 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 6.39 | 10.51 | 16.04 | 7.00 | 176.1 | 177.0 |
| Bench 2 | Bench Boost | Jan Bednarek | DEF | 17 | 4.0 | 3.00 | 8.23 | 13.10 | 1.00 | 88.8 | 90.0 |
| Bench 3 | Bench Boost | Dean Huijsen | DEF | 3 | 4.4 | 2.53 | 8.10 | 13.34 | 0.00 | 80.7 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 6.71 | 19.72 | 32.74 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cody Gakpo | FWD | 12 | 7.6 | 11.59 | 18.63 | 28.15 | 7.00 | 171.5 | 137.0 |
| XI | XI | Iliman Ndiaye | FWD | 8 | 5.5 | 7.41 | 12.07 | 18.45 | 9.00 | 172.1 | 114.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 16.67 | 26.13 | 42.50 | 29.00 | 180.0 | 177.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 7.43 | 19.93 | 33.58 | 6.00 | 90.0 | 89.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.04 | 16.70 | 27.19 | 2.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 4.07 | 13.36 | 21.09 | 2.00 | 89.2 | 90.0 |
| Bench 4 | Bench Boost | Boubakary Soumaré | MID | 11 | 4.4 | 2.29 | 6.57 | 10.58 | 2.00 | 74.6 | 90.0 |

## GW25

- Train rows: 150166
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 118.32
- Actual score: 95.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (23.37) beats the best remaining Triple Captain opportunity (11.53).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (23.37) beats the best remaining Triple Captain opportunity (11.53).
- Autosub: Jan Bednarek replaced Cody Gakpo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.81 | 11.55 | 18.09 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.02 | 0.70 | 1.52 | 0.00 | 10.8 | 0.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 10.12 | 16.08 | 26.09 | 13.00 | 175.7 | 128.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.73 | 11.10 | 18.16 | 2.00 | 86.4 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.50 | 10.72 | 16.68 | 2.00 | 90.0 | 90.0 |
| XI | XI | Dean Huijsen | DEF | 3 | 4.4 | 3.13 | 8.41 | 13.62 | 2.00 | 80.2 | 90.0 |
| Bench 2 | Autosub In | Jan Bednarek | DEF | 17 | 4.0 | 2.35 | 7.08 | 11.62 | 1.00 | 84.3 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.80 | 17.74 | 29.95 | 2.00 | 89.6 | 89.0 |
| XI | Bench | Cody Gakpo | FWD | 12 | 7.6 | 9.14 | 15.08 | 23.35 | 0.00 | 135.1 | 0.0 |
| Bench 4 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 2.12 | 7.85 | 12.91 | 0.00 | 55.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 20.35 | 29.53 | 48.37 | 20.00 | 180.0 | 180.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.2 | 6.81 | 19.69 | 32.54 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.50 | 15.53 | 25.49 | 3.00 | 82.7 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 5.71 | 15.34 | 23.77 | 5.00 | 83.4 | 76.0 |
| Bench 3 | Bench | Boubakary Soumaré | MID | 11 | 4.4 | 2.13 | 6.58 | 10.92 | 2.00 | 77.2 | 90.0 |

## GW26

- Train rows: 150945
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 67.56
- Actual score: 75.00
- Transfer: Cody Gakpo -> Chris Wood (projected gain 8.72, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.73 | 10.56 | 17.12 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.31 | 0.96 | 1.80 | 0.00 | 10.8 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.59 | 17.05 | 27.71 | 6.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.70 | 11.14 | 17.84 | 1.00 | 86.4 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.20 | 9.27 | 15.08 | 1.00 | 87.6 | 90.0 |
| XI | XI | Dean Huijsen | DEF | 3 | 4.4 | 2.62 | 7.68 | 12.48 | 2.00 | 79.3 | 90.0 |
| Bench 3 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 2.45 | 7.33 | 11.91 | 1.00 | 84.1 | 11.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 6.15 | 18.18 | 29.97 | 13.00 | 90.0 | 86.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 5.32 | 15.65 | 25.33 | 5.00 | 86.0 | 90.0 |
| Bench 4 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 1.37 | 4.90 | 9.47 | 0.00 | 26.8 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.33 | 30.18 | 49.20 | 14.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 6.23 | 18.68 | 30.89 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.12 | 17.04 | 26.59 | 14.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 4.24 | 13.22 | 20.60 | 2.00 | 65.5 | 72.0 |
| Bench 2 | Bench | Boubakary Soumaré | MID | 11 | 4.4 | 2.48 | 6.99 | 11.35 | 2.00 | 76.8 | 90.0 |

## GW27

- Train rows: 151728
- Bank: 0.50 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 68.70
- Actual score: 52.00
- Transfer: Dean Huijsen -> Daniel Muñoz (projected gain 4.26, hit 0)
- Autosub: Boubakary Soumaré replaced Alexander Isak.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.26 | 9.94 | 16.15 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.45 | 1.18 | 1.96 | 0.00 | 9.8 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.82 | 16.37 | 26.97 | 6.00 | 90.0 | 76.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.9 | 3.92 | 11.22 | 18.12 | 4.00 | 89.2 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.41 | 10.10 | 16.40 | 0.00 | 83.2 | 18.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 2.84 | 8.75 | 14.27 | 6.00 | 85.4 | 90.0 |
| Bench 3 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.87 | 3.97 | 7.11 | 0.00 | 40.8 | 0.0 |
| XI | Bench | Alexander Isak | FWD | 15 | 9.5 | 5.55 | 17.70 | 28.98 | 0.00 | 90.0 | 0.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 4.86 | 15.40 | 26.11 | 2.00 | 90.0 | 84.0 |
| Bench 4 | Bench | Iliman Ndiaye | FWD | 8 | 5.4 | 0.61 | 4.07 | 7.96 | 0.00 | 17.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.94 | 30.14 | 49.33 | 6.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 7.29 | 19.66 | 32.05 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.01 | 18.03 | 28.46 | 5.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 3.85 | 11.89 | 18.83 | 10.00 | 63.6 | 90.0 |
| Bench 2 | Autosub In | Boubakary Soumaré | MID | 11 | 4.4 | 2.51 | 6.98 | 11.33 | 2.00 | 76.8 | 60.0 |