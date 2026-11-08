# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 379.52
- Total actual points: 354.00
- Average predicted points: 94.88
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
- Predicted score: 116.52
- Actual score: 129.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.36) beats the best remaining Bench Boost opportunity (14.21).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.36) beats the best remaining Bench Boost opportunity (14.21).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 8.23 | 12.81 | 19.12 | 10.00 | 180.0 | 180.0 |
| Bench 1 | Bench Boost | Daniel Bentley | GK | 20 | 3.9 | 0.15 | 0.28 | 0.55 | 0.00 | 3.7 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 11.45 | 18.85 | 28.22 | 7.00 | 164.2 | 98.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 7.23 | 11.32 | 16.67 | 7.00 | 170.6 | 177.0 |
| XI | XI | James Tarkowski | DEF | 8 | 4.8 | 6.77 | 10.74 | 16.05 | 17.00 | 163.3 | 180.0 |
| Bench 2 | Bench Boost | Jan Bednarek | DEF | 17 | 4.0 | 3.04 | 8.32 | 13.29 | 1.00 | 88.8 | 90.0 |
| Bench 3 | Bench Boost | Taylor Harwood-Bellis | DEF | 17 | 4.0 | 2.61 | 7.21 | 11.51 | 1.00 | 79.9 | 45.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 6.72 | 19.45 | 32.32 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cody Gakpo | FWD | 12 | 7.6 | 12.31 | 19.34 | 27.84 | 7.00 | 158.8 | 137.0 |
| Bench 4 | Bench Boost | Paul Onuachu | FWD | 17 | 4.9 | 2.45 | 6.54 | 10.59 | 7.00 | 58.3 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 17.25 | 26.66 | 41.25 | 29.00 | 180.0 | 177.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 7.10 | 19.36 | 32.58 | 6.00 | 90.0 | 89.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.61 | 16.01 | 26.32 | 2.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 3.95 | 12.96 | 20.81 | 2.00 | 90.0 | 90.0 |
| XI | XI | Amad Diallo | MID | 14 | 5.6 | 4.40 | 12.80 | 20.50 | 2.00 | 82.0 | 90.0 |

## GW25

- Train rows: 150166
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 129.83
- Actual score: 101.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (24.93) beats the best remaining Triple Captain opportunity (12.22).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Amad Diallo -> Morgan Rogers (projected gain 4.28, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (24.93) beats the best remaining Triple Captain opportunity (12.22).
- Autosub: Paul Onuachu replaced Cody Gakpo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.82 | 10.83 | 17.04 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.00 | 0.26 | 0.51 | 0.00 | 2.7 | 0.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 11.69 | 18.51 | 28.55 | 13.00 | 162.3 | 128.0 |
| XI | XI | James Tarkowski | DEF | 8 | 4.8 | 4.09 | 11.70 | 18.75 | 2.00 | 90.0 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.61 | 10.29 | 16.05 | 2.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 2.30 | 7.15 | 11.81 | 1.00 | 84.1 | 90.0 |
| Bench 4 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.0 | 1.89 | 5.80 | 9.63 | 0.00 | 64.0 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.48 | 17.11 | 29.47 | 2.00 | 90.0 | 89.0 |
| XI | Bench | Cody Gakpo | FWD | 12 | 7.6 | 10.33 | 16.76 | 24.30 | 0.00 | 117.8 | 0.0 |
| Bench 2 | Autosub In | Paul Onuachu | FWD | 17 | 4.9 | 2.49 | 6.94 | 11.50 | 5.00 | 65.9 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 21.56 | 31.40 | 48.88 | 20.00 | 180.0 | 180.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.2 | 6.38 | 18.66 | 31.32 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.15 | 14.83 | 24.92 | 3.00 | 86.5 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 5.45 | 14.80 | 23.14 | 5.00 | 87.1 | 76.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 9.16 | 14.72 | 21.81 | 4.00 | 168.8 | 180.0 |

## GW26

- Train rows: 150945
- Bank: 0.10 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 66.92
- Actual score: 75.00
- Transfer: Cody Gakpo -> Chris Wood (projected gain 7.49, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.57 | 9.86 | 16.08 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.00 | 0.28 | 0.62 | 0.00 | 3.0 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.58 | 17.09 | 28.02 | 6.00 | 90.0 | 90.0 |
| XI | XI | James Tarkowski | DEF | 8 | 4.8 | 3.31 | 9.55 | 15.76 | 1.00 | 90.0 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.15 | 8.86 | 14.42 | 1.00 | 87.9 | 90.0 |
| Bench 3 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 2.32 | 7.12 | 11.75 | 1.00 | 84.6 | 11.0 |
| Bench 4 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.0 | 0.98 | 3.46 | 6.03 | 0.00 | 37.2 | 0.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 6.07 | 17.61 | 29.27 | 13.00 | 90.0 | 86.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 5.09 | 14.73 | 24.58 | 5.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 2.53 | 7.32 | 11.89 | 1.00 | 71.6 | 18.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.04 | 29.58 | 48.68 | 14.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.1 | 5.95 | 17.74 | 29.81 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.79 | 16.45 | 25.97 | 14.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 4.33 | 13.08 | 20.30 | 2.00 | 66.6 | 72.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 4.01 | 11.32 | 17.58 | 2.00 | 86.1 | 77.0 |

## GW27

- Train rows: 151728
- Bank: 0.60 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 66.25
- Actual score: 49.00
- Transfer: Morgan Rogers -> Marco Asensio (projected gain 5.66, hit 0)
- Autosub: Paul Onuachu replaced Alexander Isak.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 2.89 | 9.07 | 15.10 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.12 | 0.27 | 0.53 | 0.00 | 2.6 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.90 | 16.54 | 27.20 | 6.00 | 90.0 | 76.0 |
| XI | XI | James Tarkowski | DEF | 8 | 4.8 | 2.56 | 8.60 | 14.52 | 2.00 | 90.0 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 2.54 | 8.10 | 13.51 | 6.00 | 86.6 | 90.0 |
| Bench 3 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 1.33 | 4.85 | 8.56 | 0.00 | 52.3 | 0.0 |
| Bench 4 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.0 | 0.65 | 2.61 | 4.67 | 1.00 | 25.3 | 45.0 |
| XI | Bench | Alexander Isak | FWD | 15 | 9.5 | 5.33 | 16.83 | 28.34 | 0.00 | 90.0 | 0.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 5.09 | 15.09 | 26.01 | 2.00 | 90.0 | 84.0 |
| Bench 2 | Autosub In | Paul Onuachu | FWD | 17 | 4.9 | 1.65 | 5.30 | 9.23 | 0.00 | 47.2 | 58.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.62 | 29.38 | 48.10 | 6.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 7.03 | 19.59 | 31.66 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.94 | 17.64 | 28.00 | 5.00 | 90.0 | 90.0 |
| XI | XI | Marco Asensio | MID | 2 | 6.0 | 4.15 | 13.48 | 22.25 | 1.00 | 86.9 | 22.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 3.58 | 11.24 | 18.26 | 10.00 | 66.7 | 90.0 |