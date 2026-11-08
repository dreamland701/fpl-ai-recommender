# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 366.30
- Total actual points: 339.00
- Average predicted points: 91.58
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
- Predicted score: 112.27
- Actual score: 117.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.31) beats the best remaining Bench Boost opportunity (14.00).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.31) beats the best remaining Bench Boost opportunity (14.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 7.44 | 12.11 | 18.59 | 10.00 | 180.0 | 180.0 |
| Bench 1 | Bench Boost | Daniel Bentley | GK | 20 | 3.9 | 0.34 | 0.83 | 1.46 | 0.00 | 9.6 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 10.15 | 16.84 | 26.19 | 7.00 | 180.0 | 98.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.47 | 10.66 | 17.61 | 4.00 | 83.6 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 6.38 | 10.51 | 16.05 | 7.00 | 176.0 | 177.0 |
| Bench 2 | Bench Boost | Jan Bednarek | DEF | 17 | 4.0 | 3.02 | 8.29 | 13.19 | 1.00 | 89.3 | 90.0 |
| Bench 3 | Bench Boost | Dean Huijsen | DEF | 3 | 4.4 | 2.54 | 8.10 | 13.33 | 0.00 | 80.9 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 6.77 | 19.82 | 32.86 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cody Gakpo | FWD | 12 | 7.6 | 11.41 | 18.45 | 27.91 | 7.00 | 170.8 | 137.0 |
| XI | XI | Iliman Ndiaye | FWD | 8 | 5.5 | 7.50 | 12.19 | 18.63 | 9.00 | 171.2 | 114.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 16.76 | 26.23 | 42.63 | 29.00 | 180.0 | 177.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 7.38 | 19.69 | 33.06 | 6.00 | 90.0 | 89.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.06 | 16.74 | 27.24 | 2.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 4.01 | 13.31 | 21.11 | 2.00 | 88.7 | 90.0 |
| Bench 4 | Bench Boost | Boubakary Soumaré | MID | 11 | 4.4 | 2.29 | 6.54 | 10.51 | 2.00 | 74.5 | 90.0 |

## GW25

- Train rows: 150166
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 118.09
- Actual score: 95.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (23.36) beats the best remaining Triple Captain opportunity (11.52).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (23.36) beats the best remaining Triple Captain opportunity (11.52).
- Autosub: Jan Bednarek replaced Cody Gakpo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.78 | 11.48 | 18.00 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.00 | 0.46 | 1.09 | 0.00 | 9.1 | 0.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 10.18 | 16.11 | 26.09 | 13.00 | 175.8 | 128.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.75 | 11.12 | 18.17 | 2.00 | 87.0 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.49 | 10.69 | 16.62 | 2.00 | 90.0 | 90.0 |
| XI | XI | Dean Huijsen | DEF | 3 | 4.4 | 3.14 | 8.42 | 13.61 | 2.00 | 80.5 | 90.0 |
| Bench 2 | Autosub In | Jan Bednarek | DEF | 17 | 4.0 | 2.37 | 7.12 | 11.70 | 1.00 | 84.9 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.85 | 17.78 | 29.97 | 2.00 | 89.6 | 89.0 |
| XI | Bench | Cody Gakpo | FWD | 12 | 7.6 | 8.96 | 14.80 | 22.84 | 0.00 | 135.2 | 0.0 |
| Bench 3 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 2.21 | 8.44 | 14.10 | 0.00 | 56.1 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 20.33 | 29.52 | 48.38 | 20.00 | 180.0 | 180.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.2 | 6.76 | 19.44 | 32.03 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.52 | 15.50 | 25.40 | 3.00 | 82.9 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 5.66 | 15.30 | 23.78 | 5.00 | 83.0 | 76.0 |
| Bench 4 | Bench | Boubakary Soumaré | MID | 11 | 4.4 | 2.14 | 6.56 | 10.84 | 2.00 | 77.3 | 90.0 |

## GW26

- Train rows: 150945
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 67.48
- Actual score: 75.00
- Transfer: Cody Gakpo -> Chris Wood (projected gain 8.71, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.73 | 10.52 | 17.03 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.21 | 0.71 | 1.37 | 0.00 | 9.1 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.63 | 17.13 | 27.82 | 6.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.72 | 11.15 | 17.84 | 1.00 | 87.0 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.22 | 9.24 | 14.97 | 1.00 | 87.9 | 90.0 |
| XI | XI | Dean Huijsen | DEF | 3 | 4.4 | 2.62 | 7.67 | 12.45 | 2.00 | 79.4 | 90.0 |
| Bench 3 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 2.48 | 7.38 | 11.97 | 1.00 | 84.6 | 11.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 6.18 | 18.17 | 29.86 | 13.00 | 90.0 | 86.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 5.32 | 15.61 | 25.23 | 5.00 | 86.3 | 90.0 |
| Bench 4 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 1.39 | 4.89 | 9.37 | 0.00 | 25.3 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.30 | 30.07 | 49.03 | 14.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.1 | 6.17 | 18.42 | 30.39 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.11 | 16.99 | 26.50 | 14.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 4.18 | 13.11 | 20.48 | 2.00 | 65.1 | 72.0 |
| Bench 2 | Bench | Boubakary Soumaré | MID | 11 | 4.4 | 2.49 | 6.96 | 11.24 | 2.00 | 76.9 | 90.0 |

## GW27

- Train rows: 151728
- Bank: 0.50 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 68.47
- Actual score: 52.00
- Transfer: Dean Huijsen -> Daniel Muñoz (projected gain 4.24, hit 0)
- Autosub: Boubakary Soumaré replaced Alexander Isak.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.27 | 9.90 | 16.05 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.35 | 0.92 | 1.54 | 0.00 | 8.2 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.87 | 16.44 | 27.02 | 6.00 | 90.0 | 76.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.9 | 3.91 | 11.19 | 18.10 | 4.00 | 89.4 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.43 | 10.12 | 16.41 | 0.00 | 83.8 | 18.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 2.85 | 8.73 | 14.18 | 6.00 | 85.7 | 90.0 |
| Bench 3 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.95 | 4.58 | 8.37 | 0.00 | 42.3 | 0.0 |
| XI | Bench | Alexander Isak | FWD | 15 | 9.5 | 5.54 | 17.61 | 28.80 | 0.00 | 90.0 | 0.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 4.83 | 15.34 | 26.01 | 2.00 | 90.0 | 84.0 |
| Bench 4 | Bench | Iliman Ndiaye | FWD | 8 | 5.4 | 0.63 | 4.08 | 7.89 | 0.00 | 15.7 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.88 | 29.89 | 48.90 | 6.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 7.23 | 19.39 | 31.58 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.96 | 17.90 | 28.29 | 5.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 3.82 | 11.86 | 18.81 | 10.00 | 63.6 | 90.0 |
| Bench 2 | Autosub In | Boubakary Soumaré | MID | 11 | 4.4 | 2.52 | 6.96 | 11.25 | 2.00 | 77.0 | 60.0 |