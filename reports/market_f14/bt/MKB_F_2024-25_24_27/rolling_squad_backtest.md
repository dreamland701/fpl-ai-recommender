# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 368.62
- Total actual points: 342.00
- Average predicted points: 92.15
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
- Predicted score: 113.29
- Actual score: 120.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.64) beats the best remaining Bench Boost opportunity (14.42).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.64) beats the best remaining Bench Boost opportunity (14.42).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 7.34 | 11.93 | 18.31 | 10.00 | 180.0 | 180.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.00 | 0.01 | 0.17 | 0.00 | 1.3 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 10.48 | 17.29 | 26.83 | 7.00 | 179.2 | 98.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.40 | 10.59 | 17.59 | 4.00 | 82.4 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 6.26 | 10.30 | 15.73 | 7.00 | 175.6 | 177.0 |
| Bench 2 | Bench Boost | Jan Bednarek | DEF | 17 | 4.0 | 3.02 | 8.32 | 13.29 | 1.00 | 88.8 | 90.0 |
| Bench 4 | Bench Boost | Taylor Harwood-Bellis | DEF | 17 | 4.0 | 2.57 | 7.05 | 11.34 | 1.00 | 80.4 | 45.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 6.78 | 19.91 | 33.03 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cody Gakpo | FWD | 12 | 7.6 | 11.94 | 19.03 | 28.68 | 7.00 | 174.7 | 137.0 |
| XI | XI | Iliman Ndiaye | FWD | 8 | 5.5 | 7.43 | 12.02 | 18.37 | 9.00 | 172.6 | 114.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 16.93 | 26.52 | 43.02 | 29.00 | 180.0 | 177.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 7.29 | 19.64 | 33.12 | 6.00 | 90.0 | 89.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.95 | 16.53 | 26.96 | 2.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 4.03 | 13.26 | 20.99 | 2.00 | 89.8 | 90.0 |
| Bench 3 | Bench Boost | Enzo Fernández | MID | 6 | 4.8 | 2.93 | 7.63 | 12.91 | 4.00 | 63.8 | 90.0 |

## GW25

- Train rows: 150166
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 119.34
- Actual score: 94.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (23.70) beats the best remaining Triple Captain opportunity (11.72).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (23.70) beats the best remaining Triple Captain opportunity (11.72).
- Autosub: Jan Bednarek replaced Cody Gakpo.
- Autosub: Enzo Fernández replaced Iliman Ndiaye.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.80 | 11.47 | 18.04 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 1.1 | 0.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 10.59 | 16.69 | 27.01 | 13.00 | 179.1 | 128.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.78 | 11.24 | 18.38 | 2.00 | 85.4 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.55 | 10.75 | 16.76 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Autosub In | Jan Bednarek | DEF | 17 | 4.0 | 2.37 | 7.13 | 11.74 | 1.00 | 84.2 | 90.0 |
| Bench 4 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.0 | 1.97 | 5.88 | 9.74 | 0.00 | 64.1 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.77 | 17.73 | 29.99 | 2.00 | 89.0 | 89.0 |
| XI | Bench | Cody Gakpo | FWD | 12 | 7.6 | 9.37 | 15.35 | 23.72 | 0.00 | 137.7 | 0.0 |
| XI | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 2.67 | 9.02 | 14.70 | 0.00 | 66.3 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 20.68 | 29.98 | 49.05 | 20.00 | 180.0 | 180.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.2 | 6.63 | 19.28 | 31.92 | 2.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 5.75 | 15.42 | 23.89 | 5.00 | 85.7 | 76.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.40 | 15.27 | 25.11 | 3.00 | 83.4 | 90.0 |
| Bench 3 | Autosub In | Enzo Fernández | MID | 6 | 4.8 | 2.34 | 7.05 | 11.50 | 1.00 | 63.6 | 90.0 |

## GW26

- Train rows: 150945
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 67.08
- Actual score: 80.00
- Transfer: Cody Gakpo -> Chris Wood (projected gain 8.46, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.58 | 10.16 | 16.57 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.17 | 0.26 | 0.37 | 0.00 | 1.3 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.75 | 17.42 | 28.30 | 6.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.70 | 11.15 | 17.89 | 1.00 | 86.3 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.09 | 8.93 | 14.58 | 1.00 | 87.3 | 90.0 |
| Bench 2 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 2.42 | 7.26 | 11.84 | 1.00 | 84.0 | 11.0 |
| Bench 4 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.0 | 0.99 | 3.43 | 5.98 | 0.00 | 37.4 | 0.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 6.13 | 18.17 | 29.97 | 13.00 | 90.0 | 86.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 5.29 | 15.61 | 25.31 | 5.00 | 86.7 | 90.0 |
| Bench 3 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 1.59 | 5.34 | 10.10 | 0.00 | 32.1 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.38 | 30.30 | 49.41 | 14.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.1 | 6.07 | 18.35 | 30.41 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.05 | 16.85 | 26.33 | 14.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 4.25 | 13.20 | 20.56 | 2.00 | 66.1 | 72.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.7 | 2.43 | 7.69 | 12.34 | 7.00 | 71.3 | 90.0 |

## GW27

- Train rows: 151728
- Bank: 0.50 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 68.90
- Actual score: 48.00
- Transfer: Vitalii Mykolenko -> Daniel Muñoz (projected gain 2.43, hit 0)
- Autosub: Taylor Harwood-Bellis replaced Alexander Isak.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.13 | 9.66 | 15.78 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.92 | 16.63 | 27.35 | 6.00 | 90.0 | 76.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.9 | 3.80 | 10.93 | 17.72 | 4.00 | 87.9 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.38 | 10.06 | 16.38 | 0.00 | 83.2 | 18.0 |
| Bench 2 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 1.39 | 5.11 | 8.79 | 0.00 | 51.2 | 0.0 |
| Bench 4 | Autosub In | Taylor Harwood-Bellis | DEF | 17 | 4.0 | 0.52 | 2.34 | 4.32 | 1.00 | 25.9 | 45.0 |
| XI | Bench | Alexander Isak | FWD | 15 | 9.5 | 5.52 | 17.63 | 28.88 | 0.00 | 90.0 | 0.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 4.82 | 15.31 | 25.99 | 2.00 | 90.0 | 84.0 |
| Bench 3 | Bench | Iliman Ndiaye | FWD | 8 | 5.4 | 0.87 | 4.65 | 8.82 | 0.00 | 22.7 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.85 | 29.96 | 49.07 | 6.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 7.17 | 19.40 | 31.69 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.98 | 17.95 | 28.35 | 5.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 3.77 | 11.69 | 18.58 | 10.00 | 64.4 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.7 | 3.71 | 9.46 | 14.91 | 3.00 | 75.6 | 89.0 |