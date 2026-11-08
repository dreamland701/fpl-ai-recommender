# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 366.00
- Total actual points: 339.00
- Average predicted points: 91.50
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
- Predicted score: 111.89
- Actual score: 117.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.10) beats the best remaining Bench Boost opportunity (13.80).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.10) beats the best remaining Bench Boost opportunity (13.80).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 7.42 | 12.06 | 18.49 | 10.00 | 180.0 | 180.0 |
| Bench 1 | Bench Boost | John Ruddy | GK | 15 | 3.9 | 0.18 | 0.54 | 0.91 | 0.00 | 4.8 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 10.28 | 17.22 | 26.94 | 7.00 | 180.0 | 98.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.40 | 10.41 | 17.17 | 4.00 | 82.7 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 6.33 | 10.37 | 15.77 | 7.00 | 175.5 | 177.0 |
| Bench 2 | Bench Boost | Jan Bednarek | DEF | 17 | 4.0 | 2.99 | 8.20 | 13.06 | 1.00 | 89.0 | 90.0 |
| Bench 3 | Bench Boost | Dean Huijsen | DEF | 3 | 4.4 | 2.53 | 8.08 | 13.33 | 0.00 | 80.7 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 6.79 | 19.97 | 33.23 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cody Gakpo | FWD | 12 | 7.6 | 11.27 | 17.99 | 27.02 | 7.00 | 170.4 | 137.0 |
| XI | XI | Iliman Ndiaye | FWD | 8 | 5.5 | 7.43 | 11.99 | 18.27 | 9.00 | 171.0 | 114.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 16.71 | 26.07 | 42.40 | 29.00 | 180.0 | 177.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 7.42 | 20.10 | 33.86 | 6.00 | 90.0 | 89.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.10 | 16.93 | 27.63 | 2.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 4.04 | 13.31 | 20.93 | 2.00 | 88.8 | 90.0 |
| Bench 4 | Bench Boost | Boubakary Soumaré | MID | 11 | 4.4 | 2.29 | 6.55 | 10.54 | 2.00 | 74.3 | 90.0 |

## GW25

- Train rows: 150166
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 118.04
- Actual score: 95.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (23.34) beats the best remaining Triple Captain opportunity (11.52).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (23.34) beats the best remaining Triple Captain opportunity (11.52).
- Autosub: Jan Bednarek replaced Cody Gakpo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.78 | 11.49 | 18.03 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | John Ruddy | GK | 15 | 3.9 | 0.00 | 0.25 | 0.53 | 0.00 | 5.9 | 0.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 10.32 | 16.53 | 26.94 | 13.00 | 179.1 | 128.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.70 | 10.90 | 17.80 | 2.00 | 86.1 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.48 | 10.62 | 16.49 | 2.00 | 90.0 | 90.0 |
| XI | XI | Dean Huijsen | DEF | 3 | 4.4 | 3.13 | 8.42 | 13.65 | 2.00 | 80.3 | 90.0 |
| Bench 2 | Autosub In | Jan Bednarek | DEF | 17 | 4.0 | 2.34 | 7.05 | 11.58 | 1.00 | 84.6 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.87 | 17.97 | 30.42 | 2.00 | 89.5 | 89.0 |
| XI | Bench | Cody Gakpo | FWD | 12 | 7.6 | 8.79 | 14.39 | 22.12 | 0.00 | 134.1 | 0.0 |
| Bench 4 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 2.11 | 7.69 | 12.57 | 0.00 | 54.8 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 20.32 | 29.36 | 48.09 | 20.00 | 180.0 | 180.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.2 | 6.80 | 19.91 | 32.92 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.54 | 15.65 | 25.73 | 3.00 | 82.7 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 5.67 | 15.24 | 23.53 | 5.00 | 82.9 | 76.0 |
| Bench 3 | Bench | Boubakary Soumaré | MID | 11 | 4.4 | 2.12 | 6.52 | 10.79 | 2.00 | 76.9 | 90.0 |

## GW26

- Train rows: 150945
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 67.52
- Actual score: 75.00
- Transfer: Cody Gakpo -> Chris Wood (projected gain 8.70, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.72 | 10.58 | 17.20 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | John Ruddy | GK | 15 | 3.9 | 0.03 | 0.33 | 0.57 | 0.00 | 6.8 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.69 | 17.49 | 28.51 | 6.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.67 | 10.97 | 17.53 | 1.00 | 86.2 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.20 | 9.23 | 15.00 | 1.00 | 87.5 | 90.0 |
| XI | XI | Dean Huijsen | DEF | 3 | 4.4 | 2.63 | 7.72 | 12.55 | 2.00 | 79.4 | 90.0 |
| Bench 3 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 2.46 | 7.34 | 11.94 | 1.00 | 84.3 | 11.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 6.19 | 18.38 | 30.39 | 13.00 | 90.0 | 86.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 5.29 | 15.57 | 25.15 | 5.00 | 85.7 | 90.0 |
| Bench 4 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 1.40 | 4.85 | 9.29 | 0.00 | 26.1 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.29 | 29.95 | 48.81 | 14.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 6.22 | 18.95 | 31.44 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.16 | 17.22 | 26.98 | 14.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 4.18 | 13.03 | 20.23 | 2.00 | 64.8 | 72.0 |
| Bench 2 | Bench | Boubakary Soumaré | MID | 11 | 4.4 | 2.47 | 6.94 | 11.24 | 2.00 | 76.5 | 90.0 |

## GW27

- Train rows: 151728
- Bank: 0.50 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 68.55
- Actual score: 52.00
- Transfer: Dean Huijsen -> Daniel Muñoz (projected gain 4.18, hit 0)
- Autosub: Boubakary Soumaré replaced Alexander Isak.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.26 | 9.97 | 16.24 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | John Ruddy | GK | 15 | 3.9 | 0.00 | 0.06 | 0.23 | 0.00 | 6.3 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.93 | 16.86 | 27.86 | 6.00 | 90.0 | 76.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.9 | 3.89 | 11.08 | 17.89 | 4.00 | 89.2 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.40 | 10.01 | 16.23 | 0.00 | 83.2 | 18.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 2.84 | 8.76 | 14.28 | 6.00 | 85.4 | 90.0 |
| Bench 3 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.88 | 3.98 | 7.13 | 0.00 | 40.9 | 0.0 |
| XI | Bench | Alexander Isak | FWD | 15 | 9.5 | 5.58 | 17.87 | 29.36 | 0.00 | 90.0 | 0.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 4.80 | 15.23 | 25.78 | 2.00 | 90.0 | 84.0 |
| Bench 4 | Bench | Iliman Ndiaye | FWD | 8 | 5.4 | 0.63 | 4.02 | 7.76 | 0.00 | 16.2 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.87 | 29.86 | 48.90 | 6.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 7.27 | 19.90 | 32.62 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.03 | 18.18 | 28.82 | 5.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 3.81 | 11.82 | 18.71 | 10.00 | 63.0 | 90.0 |
| Bench 2 | Autosub In | Boubakary Soumaré | MID | 11 | 4.4 | 2.50 | 6.92 | 11.21 | 2.00 | 76.5 | 60.0 |