# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 362.51
- Total actual points: 339.00
- Average predicted points: 90.63
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
- Predicted score: 112.39
- Actual score: 117.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.30) beats the best remaining Bench Boost opportunity (13.99).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.30) beats the best remaining Bench Boost opportunity (13.99).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 7.44 | 12.10 | 18.57 | 10.00 | 180.0 | 180.0 |
| Bench 1 | Bench Boost | Daniel Bentley | GK | 20 | 3.9 | 0.36 | 0.79 | 1.33 | 0.00 | 9.9 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 10.16 | 16.87 | 26.26 | 7.00 | 180.0 | 98.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.45 | 10.70 | 17.72 | 4.00 | 83.3 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 6.38 | 10.52 | 16.06 | 7.00 | 176.2 | 177.0 |
| Bench 2 | Bench Boost | Jan Bednarek | DEF | 17 | 4.0 | 3.01 | 8.29 | 13.22 | 1.00 | 89.1 | 90.0 |
| Bench 3 | Bench Boost | Dean Huijsen | DEF | 3 | 4.4 | 2.53 | 8.12 | 13.38 | 0.00 | 80.8 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 6.78 | 19.89 | 33.01 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cody Gakpo | FWD | 12 | 7.6 | 11.44 | 18.44 | 27.85 | 7.00 | 171.5 | 137.0 |
| XI | XI | Iliman Ndiaye | FWD | 8 | 5.5 | 7.50 | 12.18 | 18.61 | 9.00 | 171.3 | 114.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 16.79 | 26.29 | 42.74 | 29.00 | 180.0 | 177.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 7.36 | 19.73 | 33.24 | 6.00 | 90.0 | 89.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.06 | 16.76 | 27.28 | 2.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 4.04 | 13.30 | 21.01 | 2.00 | 89.3 | 90.0 |
| Bench 4 | Bench Boost | Boubakary Soumaré | MID | 11 | 4.4 | 2.29 | 6.56 | 10.56 | 2.00 | 74.4 | 90.0 |

## GW25

- Train rows: 150166
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 114.23
- Actual score: 95.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (23.42) beats the best remaining Triple Captain opportunity (11.56).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (23.42) beats the best remaining Triple Captain opportunity (11.56).
- Autosub: Jan Bednarek replaced Cody Gakpo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.78 | 11.53 | 18.09 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.00 | 0.37 | 0.88 | 0.00 | 6.1 | 0.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 10.19 | 16.16 | 26.21 | 13.00 | 176.0 | 128.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.74 | 11.15 | 18.27 | 2.00 | 86.7 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.49 | 10.71 | 16.68 | 2.00 | 90.0 | 90.0 |
| XI | XI | Dean Huijsen | DEF | 3 | 4.4 | 3.13 | 8.43 | 13.66 | 2.00 | 80.3 | 90.0 |
| Bench 2 | Autosub In | Jan Bednarek | DEF | 17 | 4.0 | 2.36 | 7.13 | 11.73 | 1.00 | 84.6 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.84 | 17.83 | 30.10 | 2.00 | 89.5 | 89.0 |
| XI | Bench | Cody Gakpo | FWD | 12 | 7.6 | 4.93 | 12.64 | 20.94 | 0.00 | 74.4 | 0.0 |
| Bench 4 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 0.06 | 5.36 | 10.49 | 0.00 | 1.7 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 20.39 | 29.58 | 48.45 | 20.00 | 180.0 | 180.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.2 | 6.73 | 19.49 | 32.21 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.51 | 15.55 | 25.51 | 3.00 | 82.9 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 5.69 | 15.29 | 23.71 | 5.00 | 83.6 | 76.0 |
| Bench 3 | Bench | Boubakary Soumaré | MID | 11 | 4.4 | 2.13 | 6.58 | 10.91 | 2.00 | 77.0 | 90.0 |

## GW26

- Train rows: 150945
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 67.45
- Actual score: 75.00
- Transfer: Cody Gakpo -> Chris Wood (projected gain 8.77, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.72 | 10.57 | 17.18 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.15 | 0.59 | 1.15 | 0.00 | 6.1 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.63 | 17.15 | 27.86 | 6.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.71 | 11.18 | 17.93 | 1.00 | 86.7 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.20 | 9.28 | 15.10 | 1.00 | 87.6 | 90.0 |
| XI | XI | Dean Huijsen | DEF | 3 | 4.4 | 2.62 | 7.70 | 12.51 | 2.00 | 79.4 | 90.0 |
| Bench 3 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 2.47 | 7.38 | 12.02 | 1.00 | 84.3 | 11.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 6.15 | 18.19 | 29.98 | 13.00 | 90.0 | 86.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 5.32 | 15.65 | 25.34 | 5.00 | 86.3 | 90.0 |
| Bench 4 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 0.04 | 3.40 | 7.76 | 0.00 | 0.8 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.32 | 30.14 | 49.13 | 14.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.1 | 6.15 | 18.47 | 30.56 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.11 | 17.02 | 26.55 | 14.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 4.21 | 13.14 | 20.50 | 2.00 | 65.6 | 72.0 |
| Bench 2 | Bench | Boubakary Soumaré | MID | 11 | 4.4 | 2.48 | 6.99 | 11.33 | 2.00 | 76.6 | 90.0 |

## GW27

- Train rows: 151728
- Bank: 0.50 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 68.43
- Actual score: 52.00
- Transfer: Dean Huijsen -> Daniel Muñoz (projected gain 4.24, hit 0)
- Autosub: Boubakary Soumaré replaced Alexander Isak.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.25 | 9.94 | 16.20 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.37 | 0.88 | 1.41 | 0.00 | 8.5 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.86 | 16.47 | 27.12 | 6.00 | 90.0 | 76.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.9 | 3.91 | 11.20 | 18.13 | 4.00 | 89.5 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.42 | 10.14 | 16.49 | 0.00 | 83.5 | 18.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 2.84 | 8.76 | 14.29 | 6.00 | 85.4 | 90.0 |
| Bench 3 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.89 | 4.02 | 7.21 | 0.00 | 40.9 | 0.0 |
| XI | Bench | Alexander Isak | FWD | 15 | 9.5 | 5.53 | 17.66 | 28.91 | 0.00 | 90.0 | 0.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 4.84 | 15.37 | 26.07 | 2.00 | 90.0 | 84.0 |
| Bench 4 | Bench | Iliman Ndiaye | FWD | 8 | 5.4 | 0.66 | 4.19 | 8.10 | 0.00 | 16.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.88 | 29.98 | 49.09 | 6.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 7.20 | 19.42 | 31.70 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.98 | 17.95 | 28.35 | 5.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 3.83 | 11.86 | 18.81 | 10.00 | 63.8 | 90.0 |
| Bench 2 | Autosub In | Boubakary Soumaré | MID | 11 | 4.4 | 2.51 | 6.98 | 11.33 | 2.00 | 76.7 | 60.0 |