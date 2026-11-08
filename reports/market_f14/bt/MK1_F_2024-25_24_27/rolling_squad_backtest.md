# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 376.64
- Total actual points: 354.00
- Average predicted points: 94.16
- Average actual points: 88.50
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
- Predicted score: 115.55
- Actual score: 129.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.26) beats the best remaining Bench Boost opportunity (14.11).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.26) beats the best remaining Bench Boost opportunity (14.11).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 8.00 | 12.62 | 19.11 | 10.00 | 180.0 | 180.0 |
| Bench 1 | Bench Boost | Daniel Iversen | GK | 11 | 3.9 | 0.00 | 0.20 | 0.43 | 0.00 | 2.4 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 11.40 | 18.94 | 28.26 | 7.00 | 163.5 | 98.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 7.00 | 11.13 | 16.66 | 7.00 | 171.7 | 177.0 |
| XI | XI | James Tarkowski | DEF | 8 | 4.8 | 6.55 | 10.55 | 16.03 | 17.00 | 164.4 | 180.0 |
| Bench 2 | Bench Boost | Jan Bednarek | DEF | 17 | 4.0 | 3.04 | 8.32 | 13.29 | 1.00 | 88.8 | 90.0 |
| Bench 3 | Bench Boost | Taylor Harwood-Bellis | DEF | 17 | 4.0 | 2.63 | 7.20 | 11.51 | 1.00 | 79.9 | 45.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 6.71 | 19.45 | 32.32 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cody Gakpo | FWD | 12 | 7.6 | 12.25 | 19.42 | 27.88 | 7.00 | 158.1 | 137.0 |
| Bench 4 | Bench Boost | Paul Onuachu | FWD | 17 | 4.9 | 2.48 | 6.53 | 10.57 | 7.00 | 58.4 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 17.26 | 26.74 | 41.28 | 29.00 | 180.0 | 177.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 7.11 | 19.36 | 32.58 | 6.00 | 90.0 | 89.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.67 | 16.00 | 26.29 | 2.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 3.86 | 12.98 | 20.86 | 2.00 | 90.0 | 90.0 |
| XI | XI | Amad Diallo | MID | 14 | 5.6 | 4.35 | 12.81 | 20.53 | 2.00 | 82.0 | 90.0 |

## GW25

- Train rows: 150166
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 128.20
- Actual score: 101.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (24.63) beats the best remaining Triple Captain opportunity (12.05).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Amad Diallo -> Morgan Rogers (projected gain 4.16, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (24.63) beats the best remaining Triple Captain opportunity (12.05).
- Autosub: Paul Onuachu replaced Cody Gakpo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.85 | 10.83 | 17.02 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Daniel Iversen | GK | 11 | 3.9 | 0.00 | 0.00 | 0.05 | 0.00 | 1.2 | 0.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 11.35 | 18.53 | 28.63 | 13.00 | 161.8 | 128.0 |
| XI | XI | James Tarkowski | DEF | 8 | 4.8 | 4.11 | 11.69 | 18.74 | 2.00 | 90.0 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.64 | 10.29 | 16.04 | 2.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 2.33 | 7.15 | 11.79 | 1.00 | 84.1 | 90.0 |
| Bench 4 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.0 | 1.93 | 5.79 | 9.62 | 0.00 | 64.0 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.49 | 17.11 | 29.47 | 2.00 | 90.0 | 89.0 |
| XI | Bench | Cody Gakpo | FWD | 12 | 7.6 | 9.96 | 16.79 | 24.39 | 0.00 | 117.2 | 0.0 |
| Bench 2 | Autosub In | Paul Onuachu | FWD | 17 | 4.9 | 2.54 | 6.94 | 11.48 | 5.00 | 66.0 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 21.25 | 31.42 | 48.95 | 20.00 | 180.0 | 180.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.2 | 6.40 | 18.66 | 31.31 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.24 | 14.82 | 24.88 | 3.00 | 86.7 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 5.52 | 14.79 | 23.10 | 5.00 | 87.3 | 76.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 8.89 | 14.60 | 21.85 | 4.00 | 169.0 | 180.0 |

## GW26

- Train rows: 150945
- Bank: 0.10 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 66.93
- Actual score: 75.00
- Transfer: Cody Gakpo -> Chris Wood (projected gain 7.50, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.66 | 9.85 | 16.03 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Daniel Iversen | GK | 11 | 3.9 | 0.05 | 0.08 | 0.15 | 0.00 | 2.6 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.56 | 17.09 | 28.03 | 6.00 | 90.0 | 90.0 |
| XI | XI | James Tarkowski | DEF | 8 | 4.8 | 3.39 | 9.54 | 15.72 | 1.00 | 90.0 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.23 | 8.86 | 14.38 | 1.00 | 88.0 | 90.0 |
| Bench 3 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 2.33 | 7.13 | 11.75 | 1.00 | 84.6 | 11.0 |
| Bench 4 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.0 | 1.00 | 3.46 | 6.02 | 0.00 | 37.2 | 0.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 5.96 | 17.62 | 29.32 | 13.00 | 90.0 | 86.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 5.02 | 14.74 | 24.62 | 5.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 2.56 | 7.32 | 11.88 | 1.00 | 71.7 | 18.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.04 | 29.58 | 48.68 | 14.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.1 | 5.88 | 17.74 | 29.85 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.92 | 16.44 | 25.91 | 14.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 4.24 | 13.09 | 20.34 | 2.00 | 66.5 | 72.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 3.99 | 11.32 | 17.60 | 2.00 | 86.0 | 77.0 |

## GW27

- Train rows: 151728
- Bank: 0.60 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 65.97
- Actual score: 49.00
- Transfer: Morgan Rogers -> Marco Asensio (projected gain 5.66, hit 0)
- Autosub: Paul Onuachu replaced Alexander Isak.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 2.94 | 9.07 | 15.08 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Daniel Iversen | GK | 11 | 3.9 | 0.09 | 0.12 | 0.15 | 0.00 | 2.0 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.76 | 16.56 | 27.27 | 6.00 | 90.0 | 76.0 |
| XI | XI | James Tarkowski | DEF | 8 | 4.8 | 2.60 | 8.60 | 14.51 | 2.00 | 90.0 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 2.59 | 8.10 | 13.49 | 6.00 | 86.7 | 90.0 |
| Bench 3 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 1.31 | 4.86 | 8.57 | 0.00 | 52.2 | 0.0 |
| Bench 4 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.0 | 0.63 | 2.61 | 4.68 | 1.00 | 25.3 | 45.0 |
| XI | Bench | Alexander Isak | FWD | 15 | 9.5 | 5.28 | 16.84 | 28.36 | 0.00 | 90.0 | 0.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 4.94 | 15.11 | 26.08 | 2.00 | 90.0 | 84.0 |
| Bench 2 | Autosub In | Paul Onuachu | FWD | 17 | 4.9 | 1.63 | 5.31 | 9.23 | 0.00 | 47.2 | 58.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.50 | 29.39 | 48.15 | 6.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 7.12 | 19.58 | 31.62 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.96 | 17.64 | 28.00 | 5.00 | 90.0 | 90.0 |
| XI | XI | Marco Asensio | MID | 2 | 6.0 | 4.15 | 13.48 | 22.25 | 1.00 | 86.9 | 22.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 3.62 | 11.24 | 18.24 | 10.00 | 66.8 | 90.0 |