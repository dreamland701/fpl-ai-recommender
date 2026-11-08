# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 319.45
- Total actual points: 350.00
- Average predicted points: 79.86
- Average actual points: 87.50
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
- Vice captain: Cody Gakpo
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 93.43
- Actual score: 129.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.24) beats the best remaining Bench Boost opportunity (12.72).
- Chip advisory: triple_captain (0.69): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.24) beats the best remaining Bench Boost opportunity (12.72).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 5.33 | 12.62 | 19.11 | 10.00 | 135.2 | 180.0 |
| Bench 1 | Bench Boost | Daniel Iversen | GK | 11 | 3.9 | 0.07 | 0.20 | 0.43 | 0.00 | 5.0 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 8.84 | 18.94 | 28.26 | 7.00 | 147.0 | 98.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 4.91 | 11.13 | 16.66 | 7.00 | 127.1 | 177.0 |
| XI | XI | James Tarkowski | DEF | 8 | 4.8 | 4.69 | 10.55 | 16.03 | 17.00 | 124.0 | 180.0 |
| Bench 2 | Bench Boost | Jan Bednarek | DEF | 17 | 4.0 | 2.98 | 8.32 | 13.29 | 1.00 | 87.3 | 90.0 |
| Bench 3 | Bench Boost | Taylor Harwood-Bellis | DEF | 17 | 4.0 | 2.74 | 7.20 | 11.51 | 1.00 | 83.0 | 45.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 6.41 | 19.45 | 32.32 | 2.00 | 88.8 | 90.0 |
| Vice Captain | XI | Cody Gakpo | FWD | 12 | 7.6 | 9.59 | 19.42 | 27.88 | 7.00 | 138.8 | 137.0 |
| Bench 4 | Bench Boost | Paul Onuachu | FWD | 17 | 4.9 | 2.34 | 6.53 | 10.57 | 7.00 | 55.3 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 12.08 | 26.74 | 41.28 | 29.00 | 148.7 | 177.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 7.21 | 19.36 | 32.58 | 6.00 | 101.1 | 89.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.55 | 16.00 | 26.29 | 2.00 | 89.4 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 3.89 | 12.98 | 20.86 | 2.00 | 91.1 | 90.0 |
| XI | XI | Amad Diallo | MID | 14 | 5.6 | 4.73 | 12.81 | 20.53 | 2.00 | 89.0 | 90.0 |

## GW25

- Train rows: 150166
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 99.24
- Actual score: 97.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (18.13) beats the best remaining Triple Captain opportunity (8.36).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Amad Diallo -> Morgan Rogers (projected gain 4.16, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (18.13) beats the best remaining Triple Captain opportunity (8.36).
- Autosub: Jan Bednarek replaced Cody Gakpo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.39 | 10.83 | 17.02 | 3.00 | 97.9 | 90.0 |
| Bench 1 | Bench | Daniel Iversen | GK | 11 | 3.9 | 0.00 | 0.00 | 0.05 | 0.00 | 5.2 | 0.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 8.84 | 18.53 | 28.63 | 13.00 | 148.0 | 128.0 |
| XI | XI | James Tarkowski | DEF | 8 | 4.8 | 3.80 | 11.69 | 18.74 | 2.00 | 112.4 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.26 | 10.29 | 16.04 | 2.00 | 96.3 | 90.0 |
| Bench 2 | Autosub In | Jan Bednarek | DEF | 17 | 4.0 | 2.40 | 7.15 | 11.79 | 1.00 | 85.2 | 90.0 |
| Bench 4 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.0 | 1.94 | 5.79 | 9.62 | 0.00 | 64.5 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 4.76 | 17.11 | 29.47 | 2.00 | 77.6 | 89.0 |
| XI | Bench | Cody Gakpo | FWD | 12 | 7.6 | 8.49 | 16.79 | 24.39 | 0.00 | 125.7 | 0.0 |
| Bench 3 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 2.37 | 6.94 | 11.48 | 5.00 | 61.9 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 14.75 | 31.42 | 48.95 | 20.00 | 180.0 | 180.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.2 | 5.71 | 18.66 | 31.31 | 2.00 | 84.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 4.63 | 14.82 | 24.88 | 3.00 | 74.9 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 5.61 | 14.79 | 23.10 | 5.00 | 82.4 | 76.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 6.48 | 14.60 | 21.85 | 4.00 | 138.0 | 180.0 |

## GW26

- Train rows: 150945
- Bank: 0.10 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 63.04
- Actual score: 75.00
- Transfer: Cody Gakpo -> Chris Wood (projected gain 7.49, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.47 | 9.85 | 16.03 | 1.00 | 91.0 | 90.0 |
| Bench 1 | Bench | Daniel Iversen | GK | 11 | 3.9 | 0.05 | 0.08 | 0.15 | 0.00 | 3.4 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.33 | 17.09 | 28.03 | 6.00 | 104.9 | 90.0 |
| XI | XI | James Tarkowski | DEF | 8 | 4.8 | 3.29 | 9.54 | 15.72 | 1.00 | 92.7 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.14 | 8.86 | 14.38 | 1.00 | 85.6 | 90.0 |
| Bench 3 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 2.20 | 7.13 | 11.75 | 1.00 | 81.7 | 11.0 |
| Bench 4 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.0 | 1.01 | 3.46 | 6.02 | 0.00 | 38.5 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.61 | 17.62 | 29.32 | 13.00 | 88.4 | 86.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 4.13 | 14.74 | 24.62 | 5.00 | 72.4 | 90.0 |
| Bench 2 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 2.23 | 7.32 | 11.88 | 1.00 | 63.5 | 18.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 9.45 | 29.58 | 48.68 | 14.00 | 153.8 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.1 | 5.24 | 17.74 | 29.85 | 2.00 | 84.8 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.74 | 16.44 | 25.91 | 14.00 | 90.1 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 4.47 | 13.09 | 20.34 | 2.00 | 66.2 | 72.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 3.74 | 11.32 | 17.60 | 2.00 | 81.8 | 77.0 |

## GW27

- Train rows: 151728
- Bank: 0.60 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 63.74
- Actual score: 49.00
- Transfer: Morgan Rogers -> Marco Asensio (projected gain 5.66, hit 0)
- Autosub: Paul Onuachu replaced Alexander Isak.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 2.63 | 9.07 | 15.08 | 2.00 | 86.7 | 90.0 |
| Bench 1 | Bench | Daniel Iversen | GK | 11 | 3.9 | 0.13 | 0.12 | 0.15 | 0.00 | 4.0 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.85 | 16.56 | 27.27 | 6.00 | 100.4 | 76.0 |
| XI | XI | James Tarkowski | DEF | 8 | 4.8 | 2.39 | 8.60 | 14.51 | 2.00 | 85.6 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 2.38 | 8.10 | 13.49 | 6.00 | 81.4 | 90.0 |
| Bench 3 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 1.11 | 4.86 | 8.57 | 0.00 | 47.6 | 0.0 |
| Bench 4 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.0 | 0.71 | 2.61 | 4.68 | 1.00 | 29.5 | 45.0 |
| XI | Bench | Alexander Isak | FWD | 15 | 9.5 | 4.42 | 16.84 | 28.36 | 0.00 | 83.9 | 0.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 4.39 | 15.11 | 26.08 | 2.00 | 87.6 | 84.0 |
| Bench 2 | Autosub In | Paul Onuachu | FWD | 17 | 4.9 | 1.33 | 5.31 | 9.23 | 0.00 | 39.4 | 58.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.32 | 29.39 | 48.15 | 6.00 | 137.1 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 7.56 | 19.58 | 31.62 | 3.00 | 108.9 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.84 | 17.64 | 28.00 | 5.00 | 90.3 | 90.0 |
| XI | XI | Marco Asensio | MID | 2 | 6.0 | 4.45 | 13.48 | 22.25 | 1.00 | 93.9 | 22.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 3.18 | 11.24 | 18.24 | 10.00 | 55.8 | 90.0 |