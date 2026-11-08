# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 366.97
- Total actual points: 339.00
- Average predicted points: 91.74
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
- Predicted score: 112.53
- Actual score: 117.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (12.98) beats the best remaining Bench Boost opportunity (13.70).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (12.98) beats the best remaining Bench Boost opportunity (13.70).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 7.37 | 12.04 | 18.72 | 10.00 | 180.0 | 180.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.02 | 0.40 | 0.77 | 0.00 | 6.6 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 10.29 | 16.75 | 25.96 | 7.00 | 180.0 | 98.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.44 | 10.69 | 17.79 | 4.00 | 84.1 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 6.43 | 10.62 | 16.40 | 7.00 | 177.9 | 177.0 |
| Bench 3 | Bench Boost | Dean Huijsen | DEF | 3 | 4.4 | 2.65 | 8.39 | 13.73 | 0.00 | 82.4 | 90.0 |
| Bench 2 | Bench Boost | Jan Bednarek | DEF | 17 | 4.0 | 2.96 | 8.07 | 12.89 | 1.00 | 89.2 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 6.78 | 20.06 | 33.32 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cody Gakpo | FWD | 12 | 7.6 | 11.71 | 18.41 | 27.86 | 7.00 | 176.8 | 137.0 |
| XI | XI | Iliman Ndiaye | FWD | 8 | 5.5 | 7.63 | 12.38 | 19.09 | 9.00 | 173.4 | 114.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 16.76 | 26.44 | 42.96 | 29.00 | 180.0 | 177.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 7.25 | 19.41 | 32.60 | 6.00 | 90.0 | 89.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.06 | 16.50 | 27.02 | 2.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 4.18 | 13.36 | 20.98 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench Boost | Boubakary Soumaré | MID | 11 | 4.4 | 2.24 | 6.31 | 10.22 | 2.00 | 74.1 | 90.0 |

## GW25

- Train rows: 150166
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 118.77
- Actual score: 95.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (23.34) beats the best remaining Triple Captain opportunity (11.51).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (23.34) beats the best remaining Triple Captain opportunity (11.51).
- Autosub: Jan Bednarek replaced Cody Gakpo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.82 | 11.32 | 17.70 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.22 | 0.53 | 0.85 | 0.00 | 6.4 | 0.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 10.26 | 16.11 | 26.11 | 13.00 | 176.6 | 128.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.70 | 11.09 | 18.27 | 2.00 | 87.3 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.59 | 10.69 | 16.56 | 2.00 | 90.0 | 90.0 |
| XI | XI | Dean Huijsen | DEF | 3 | 4.4 | 3.19 | 8.62 | 13.86 | 2.00 | 81.5 | 90.0 |
| Bench 2 | Autosub In | Jan Bednarek | DEF | 17 | 4.0 | 2.36 | 7.09 | 11.51 | 1.00 | 85.3 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.88 | 18.09 | 30.41 | 2.00 | 89.2 | 89.0 |
| XI | Bench | Cody Gakpo | FWD | 12 | 7.6 | 9.41 | 14.77 | 22.83 | 0.00 | 142.9 | 0.0 |
| Bench 3 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 2.25 | 7.83 | 12.95 | 0.00 | 57.7 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 20.31 | 29.66 | 48.49 | 20.00 | 180.0 | 180.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.2 | 6.69 | 19.35 | 31.95 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.53 | 15.34 | 25.21 | 3.00 | 83.1 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 5.76 | 15.11 | 23.22 | 5.00 | 85.2 | 76.0 |
| Bench 4 | Bench | Boubakary Soumaré | MID | 11 | 4.4 | 2.10 | 6.41 | 10.69 | 2.00 | 77.1 | 90.0 |

## GW26

- Train rows: 150945
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 67.46
- Actual score: 75.00
- Transfer: Cody Gakpo -> Chris Wood (projected gain 8.49, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.67 | 10.45 | 17.04 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.39 | 0.75 | 1.13 | 0.00 | 6.8 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.76 | 17.22 | 27.88 | 6.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.73 | 11.26 | 18.14 | 1.00 | 87.6 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.22 | 9.26 | 15.14 | 1.00 | 88.2 | 90.0 |
| XI | XI | Dean Huijsen | DEF | 3 | 4.4 | 2.60 | 7.73 | 12.53 | 2.00 | 80.1 | 90.0 |
| Bench 2 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 2.46 | 7.27 | 11.84 | 1.00 | 84.8 | 11.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 6.12 | 18.08 | 29.69 | 13.00 | 90.0 | 86.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 5.35 | 15.70 | 25.64 | 5.00 | 87.1 | 90.0 |
| Bench 4 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 1.49 | 5.12 | 9.99 | 0.00 | 27.5 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.25 | 30.31 | 49.36 | 14.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.1 | 6.08 | 18.49 | 30.39 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.14 | 17.26 | 26.81 | 14.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 4.29 | 12.77 | 20.13 | 2.00 | 67.9 | 72.0 |
| Bench 3 | Bench | Boubakary Soumaré | MID | 11 | 4.4 | 2.44 | 6.83 | 11.13 | 2.00 | 76.9 | 90.0 |

## GW27

- Train rows: 151728
- Bank: 0.50 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 68.22
- Actual score: 52.00
- Transfer: Dean Huijsen -> Daniel Muñoz (projected gain 4.22, hit 0)
- Autosub: Boubakary Soumaré replaced Alexander Isak.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.25 | 9.84 | 16.03 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.23 | 0.48 | 0.79 | 0.00 | 5.3 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.76 | 16.30 | 26.93 | 6.00 | 90.0 | 76.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.9 | 3.90 | 11.14 | 18.05 | 4.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.48 | 10.37 | 16.85 | 0.00 | 84.0 | 18.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 2.91 | 8.76 | 14.34 | 6.00 | 86.2 | 90.0 |
| Bench 3 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.92 | 3.85 | 7.16 | 0.00 | 41.2 | 0.0 |
| XI | Bench | Alexander Isak | FWD | 15 | 9.5 | 5.53 | 17.94 | 29.11 | 0.00 | 90.0 | 0.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 4.83 | 15.36 | 26.30 | 2.00 | 90.0 | 84.0 |
| Bench 4 | Bench | Iliman Ndiaye | FWD | 8 | 5.4 | 0.74 | 4.35 | 8.51 | 0.00 | 18.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.75 | 29.97 | 49.18 | 6.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 7.13 | 19.34 | 31.18 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.04 | 18.20 | 28.59 | 5.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 3.88 | 11.74 | 18.84 | 10.00 | 65.8 | 90.0 |
| Bench 2 | Autosub In | Boubakary Soumaré | MID | 11 | 4.4 | 2.50 | 6.94 | 11.32 | 2.00 | 77.2 | 60.0 |