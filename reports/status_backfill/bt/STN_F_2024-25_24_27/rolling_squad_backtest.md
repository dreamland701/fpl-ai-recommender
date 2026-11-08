# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 304.68
- Total actual points: 339.00
- Average predicted points: 76.17
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
- Predicted score: 81.69
- Actual score: 115.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (12.93) beats the best remaining Bench Boost opportunity (12.20).
- Chip advisory: bench_boost (0.56): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.66): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (12.93) beats the best remaining Bench Boost opportunity (12.20).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 4.78 | 12.10 | 18.57 | 10.00 | 127.4 | 180.0 |
| Bench 1 | Bench Boost | João Neves Virgínia | GK | 8 | 3.9 | 0.99 | 1.76 | 2.39 | 0.00 | 34.6 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 6.44 | 16.87 | 26.26 | 7.00 | 120.0 | 98.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.38 | 10.70 | 17.72 | 4.00 | 82.9 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 4.20 | 10.52 | 16.06 | 7.00 | 117.8 | 177.0 |
| Bench 2 | Bench Boost | Jacob Greaves | DEF | 10 | 3.9 | 2.44 | 6.18 | 9.57 | 1.00 | 65.5 | 90.0 |
| Bench 4 | Bench Boost | Jannik Vestergaard | DEF | 11 | 3.9 | 1.98 | 5.71 | 9.28 | 0.00 | 74.5 | 59.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 6.70 | 19.89 | 33.01 | 2.00 | 93.9 | 90.0 |
| Vice Captain | XI | Cody Gakpo | FWD | 12 | 7.6 | 7.51 | 18.44 | 27.85 | 7.00 | 121.8 | 137.0 |
| Bench 3 | Bench Boost | Paul Onuachu | FWD | 17 | 4.9 | 2.41 | 6.63 | 10.70 | 7.00 | 55.9 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 9.48 | 26.29 | 42.74 | 29.00 | 130.2 | 177.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 7.26 | 19.73 | 33.24 | 6.00 | 101.5 | 89.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.14 | 16.76 | 27.28 | 2.00 | 93.9 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 4.40 | 13.30 | 21.01 | 2.00 | 94.8 | 90.0 |
| XI | XI | Amad Diallo | MID | 14 | 5.6 | 4.10 | 12.23 | 19.98 | 2.00 | 85.6 | 90.0 |

## GW25

- Train rows: 150166
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 85.92
- Actual score: 101.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (14.57) beats the best remaining Triple Captain opportunity (9.30).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Amad Diallo -> Morgan Rogers (projected gain 2.33, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (14.57) beats the best remaining Triple Captain opportunity (9.30).
- Autosub: Paul Onuachu replaced Cody Gakpo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.78 | 11.53 | 18.09 | 3.00 | 108.1 | 90.0 |
| Bench 1 | Bench | João Neves Virgínia | GK | 8 | 3.9 | 0.14 | 0.48 | 0.88 | 0.00 | 4.7 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 6.23 | 16.16 | 26.21 | 13.00 | 114.5 | 128.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.71 | 11.15 | 18.27 | 2.00 | 86.9 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.54 | 10.71 | 16.68 | 2.00 | 104.2 | 90.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 1.77 | 5.66 | 9.15 | 1.00 | 66.7 | 90.0 |
| Bench 4 | Bench | Jannik Vestergaard | DEF | 11 | 3.9 | 0.92 | 3.54 | 6.20 | 0.00 | 55.3 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.63 | 17.83 | 30.10 | 2.00 | 86.4 | 89.0 |
| XI | Bench | Cody Gakpo | FWD | 12 | 7.6 | 5.74 | 14.87 | 23.01 | 0.00 | 95.1 | 0.0 |
| Bench 2 | Autosub In | Paul Onuachu | FWD | 17 | 4.9 | 2.59 | 7.15 | 11.71 | 5.00 | 64.3 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 11.20 | 29.58 | 48.45 | 20.00 | 170.4 | 180.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 6.57 | 19.49 | 32.21 | 2.00 | 93.1 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.54 | 15.55 | 25.51 | 3.00 | 82.7 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 6.09 | 15.29 | 23.71 | 5.00 | 88.2 | 76.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 5.49 | 13.07 | 19.65 | 4.00 | 116.8 | 180.0 |

## GW26

- Train rows: 150945
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 68.86
- Actual score: 75.00
- Transfer: Cody Gakpo -> Chris Wood (projected gain 7.83, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.80 | 10.57 | 17.18 | 1.00 | 97.6 | 90.0 |
| Bench 1 | Bench | João Neves Virgínia | GK | 8 | 3.9 | 0.38 | 0.67 | 1.09 | 0.00 | 5.0 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.63 | 17.15 | 27.86 | 6.00 | 106.2 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.70 | 11.18 | 17.93 | 1.00 | 87.4 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.29 | 9.28 | 15.10 | 1.00 | 89.3 | 90.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 2.42 | 6.50 | 10.65 | 0.00 | 77.3 | 90.0 |
| Bench 4 | Bench | Jannik Vestergaard | DEF | 11 | 3.9 | 1.12 | 3.38 | 5.68 | 1.00 | 42.7 | 45.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 6.11 | 18.19 | 29.98 | 13.00 | 96.9 | 86.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 5.27 | 15.65 | 25.34 | 5.00 | 85.1 | 90.0 |
| Bench 2 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 2.78 | 7.95 | 12.59 | 1.00 | 69.2 | 18.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.16 | 30.14 | 49.13 | 14.00 | 159.3 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.1 | 5.99 | 18.47 | 30.56 | 2.00 | 93.6 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.31 | 17.02 | 26.55 | 14.00 | 94.8 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 4.49 | 13.14 | 20.50 | 2.00 | 68.0 | 72.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 3.95 | 11.38 | 17.52 | 2.00 | 82.0 | 77.0 |

## GW27

- Train rows: 151728
- Bank: 0.50 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 68.21
- Actual score: 48.00
- Transfer: Morgan Rogers -> Marco Asensio (projected gain 6.35, hit 0)
- Autosub: Jacob Greaves replaced Alexander Isak.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.32 | 9.94 | 16.20 | 2.00 | 94.6 | 90.0 |
| Bench 1 | Bench | João Neves Virgínia | GK | 8 | 3.9 | 0.15 | 0.49 | 0.86 | 0.00 | 4.3 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.86 | 16.47 | 27.12 | 6.00 | 98.9 | 76.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.39 | 10.14 | 16.49 | 0.00 | 83.9 | 18.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 2.92 | 8.76 | 14.29 | 6.00 | 87.0 | 90.0 |
| Bench 2 | Autosub In | Jacob Greaves | DEF | 10 | 3.9 | 2.17 | 6.29 | 10.16 | 1.00 | 75.0 | 90.0 |
| Bench 4 | Bench | Jannik Vestergaard | DEF | 11 | 3.9 | 1.60 | 4.60 | 7.53 | -1.00 | 52.5 | 86.0 |
| XI | Bench | Alexander Isak | FWD | 15 | 9.5 | 5.44 | 17.66 | 28.91 | 0.00 | 95.4 | 0.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 4.83 | 15.37 | 26.07 | 2.00 | 94.3 | 84.0 |
| Bench 3 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 1.80 | 5.87 | 9.93 | 0.00 | 45.6 | 58.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.67 | 29.98 | 49.09 | 6.00 | 141.4 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 7.24 | 19.42 | 31.70 | 3.00 | 104.2 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.12 | 17.95 | 28.35 | 5.00 | 95.2 | 90.0 |
| XI | XI | Marco Asensio | MID | 2 | 6.0 | 3.94 | 12.64 | 21.00 | 1.00 | 85.9 | 22.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 3.83 | 11.86 | 18.81 | 10.00 | 61.9 | 90.0 |