# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 366.96
- Total actual points: 342.00
- Average predicted points: 91.74
- Average actual points: 85.50
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
- Predicted score: 113.11
- Actual score: 120.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.49) beats the best remaining Bench Boost opportunity (14.26).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.49) beats the best remaining Bench Boost opportunity (14.26).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 7.65 | 12.29 | 18.81 | 10.00 | 180.0 | 180.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.01 | 0.51 | 0.86 | 0.00 | 7.9 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 10.13 | 16.88 | 26.23 | 7.00 | 180.0 | 98.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.47 | 10.73 | 17.75 | 4.00 | 83.8 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 6.58 | 10.70 | 16.28 | 7.00 | 176.8 | 177.0 |
| Bench 2 | Bench Boost | Jan Bednarek | DEF | 17 | 4.0 | 3.02 | 8.20 | 13.00 | 1.00 | 88.9 | 90.0 |
| Bench 4 | Bench Boost | Taylor Harwood-Bellis | DEF | 17 | 4.0 | 2.50 | 6.80 | 10.84 | 1.00 | 78.6 | 45.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 6.78 | 19.95 | 33.10 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cody Gakpo | FWD | 12 | 7.6 | 11.43 | 18.45 | 27.84 | 7.00 | 172.2 | 137.0 |
| XI | XI | Iliman Ndiaye | FWD | 8 | 5.5 | 7.72 | 12.38 | 18.85 | 9.00 | 172.1 | 114.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 16.77 | 26.25 | 42.67 | 29.00 | 180.0 | 177.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 7.30 | 19.65 | 33.10 | 6.00 | 90.0 | 89.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.07 | 16.85 | 27.35 | 2.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 4.07 | 13.31 | 20.95 | 2.00 | 89.9 | 90.0 |
| Bench 3 | Bench Boost | Enzo Fernández | MID | 6 | 4.8 | 2.85 | 7.42 | 12.62 | 4.00 | 64.9 | 90.0 |

## GW25

- Train rows: 150166
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 117.10
- Actual score: 94.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (23.29) beats the best remaining Triple Captain opportunity (11.49).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (23.29) beats the best remaining Triple Captain opportunity (11.49).
- Autosub: Jan Bednarek replaced Cody Gakpo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.82 | 11.61 | 18.24 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.28 | 0.69 | 1.05 | 0.00 | 7.5 | 0.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 10.10 | 16.00 | 26.04 | 13.00 | 176.7 | 128.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.73 | 11.21 | 18.28 | 2.00 | 87.5 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.53 | 10.78 | 16.82 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Autosub In | Jan Bednarek | DEF | 17 | 4.0 | 2.26 | 6.98 | 11.42 | 1.00 | 84.8 | 90.0 |
| Bench 4 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.0 | 1.35 | 4.52 | 7.56 | 0.00 | 52.8 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.90 | 17.85 | 30.21 | 2.00 | 89.2 | 89.0 |
| XI | Bench | Cody Gakpo | FWD | 12 | 7.6 | 8.88 | 14.74 | 22.86 | 0.00 | 136.0 | 0.0 |
| Bench 3 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 2.21 | 8.00 | 13.18 | 0.00 | 55.7 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 20.27 | 29.42 | 48.24 | 20.00 | 180.0 | 180.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.2 | 6.71 | 19.45 | 32.13 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.49 | 15.54 | 25.53 | 3.00 | 83.3 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 5.73 | 15.28 | 23.61 | 5.00 | 84.0 | 76.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.8 | 2.41 | 7.18 | 11.69 | 1.00 | 65.9 | 90.0 |

## GW26

- Train rows: 150945
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 67.37
- Actual score: 80.00
- Transfer: Cody Gakpo -> Chris Wood (projected gain 8.49, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.75 | 10.62 | 17.29 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.52 | 0.85 | 1.28 | 0.00 | 7.5 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.64 | 17.01 | 27.74 | 6.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.71 | 11.13 | 17.88 | 1.00 | 87.5 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.23 | 9.33 | 15.21 | 1.00 | 88.3 | 90.0 |
| Bench 2 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 2.38 | 7.21 | 11.70 | 1.00 | 84.6 | 11.0 |
| Bench 4 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.0 | 0.58 | 2.49 | 4.49 | 0.00 | 29.1 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 6.14 | 18.35 | 30.13 | 13.00 | 90.0 | 86.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 5.31 | 15.58 | 25.19 | 5.00 | 87.1 | 90.0 |
| Bench 3 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 1.46 | 5.08 | 9.75 | 0.00 | 27.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.34 | 30.00 | 49.02 | 14.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.1 | 6.16 | 18.42 | 30.55 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.20 | 17.16 | 26.67 | 14.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 4.16 | 12.96 | 20.27 | 2.00 | 66.4 | 72.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.7 | 2.39 | 7.47 | 12.04 | 7.00 | 72.1 | 90.0 |

## GW27

- Train rows: 151728
- Bank: 0.50 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 69.38
- Actual score: 48.00
- Transfer: Vitalii Mykolenko -> Daniel Muñoz (projected gain 2.34, hit 0)
- Autosub: Taylor Harwood-Bellis replaced Alexander Isak.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.28 | 10.09 | 16.35 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.22 | 0.57 | 0.82 | 0.00 | 6.4 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.82 | 16.39 | 26.98 | 6.00 | 90.0 | 76.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.9 | 3.94 | 11.25 | 18.25 | 4.00 | 89.9 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.41 | 10.09 | 16.45 | 0.00 | 84.3 | 18.0 |
| Bench 2 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.81 | 3.89 | 6.94 | 0.00 | 41.0 | 0.0 |
| Bench 4 | Autosub In | Taylor Harwood-Bellis | DEF | 17 | 4.0 | 0.12 | 1.50 | 3.03 | 1.00 | 18.9 | 45.0 |
| XI | Bench | Alexander Isak | FWD | 15 | 9.5 | 5.60 | 17.79 | 29.13 | 0.00 | 90.0 | 0.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 4.90 | 15.28 | 26.01 | 2.00 | 90.0 | 84.0 |
| Bench 3 | Bench | Iliman Ndiaye | FWD | 8 | 5.4 | 0.70 | 4.34 | 8.28 | 0.00 | 17.2 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.83 | 29.92 | 48.97 | 6.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 7.29 | 19.48 | 31.74 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.97 | 17.92 | 28.32 | 5.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 3.79 | 11.80 | 18.66 | 10.00 | 64.5 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.7 | 3.69 | 9.20 | 14.49 | 3.00 | 76.0 | 89.0 |