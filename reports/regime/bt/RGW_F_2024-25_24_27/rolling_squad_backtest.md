# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 366.47
- Total actual points: 339.00
- Average predicted points: 91.62
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
- Predicted score: 112.55
- Actual score: 117.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (12.95) beats the best remaining Bench Boost opportunity (13.67).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (12.95) beats the best remaining Bench Boost opportunity (13.67).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 7.41 | 12.09 | 18.77 | 10.00 | 180.0 | 180.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.08 | 0.59 | 1.09 | 0.00 | 4.4 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 10.32 | 16.82 | 26.10 | 7.00 | 180.0 | 98.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.42 | 10.62 | 17.67 | 4.00 | 85.0 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 6.42 | 10.61 | 16.39 | 7.00 | 179.8 | 177.0 |
| Bench 3 | Bench Boost | Dean Huijsen | DEF | 3 | 4.4 | 2.63 | 8.33 | 13.63 | 0.00 | 83.5 | 90.0 |
| Bench 2 | Bench Boost | Jan Bednarek | DEF | 17 | 4.0 | 2.93 | 7.98 | 12.76 | 1.00 | 90.0 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 6.73 | 19.89 | 32.99 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cody Gakpo | FWD | 12 | 7.6 | 11.71 | 18.38 | 27.79 | 7.00 | 175.1 | 137.0 |
| XI | XI | Iliman Ndiaye | FWD | 8 | 5.5 | 7.58 | 12.26 | 18.84 | 9.00 | 171.2 | 114.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 16.85 | 26.61 | 43.30 | 29.00 | 180.0 | 177.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 7.24 | 19.40 | 32.59 | 6.00 | 90.0 | 89.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.05 | 16.47 | 26.96 | 2.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 4.14 | 13.25 | 20.75 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench Boost | Boubakary Soumaré | MID | 11 | 4.4 | 2.19 | 6.16 | 9.93 | 2.00 | 73.3 | 90.0 |

## GW25

- Train rows: 150166
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 118.79
- Actual score: 95.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (23.38) beats the best remaining Triple Captain opportunity (11.54).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (23.38) beats the best remaining Triple Captain opportunity (11.54).
- Autosub: Jan Bednarek replaced Cody Gakpo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.85 | 11.35 | 17.71 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.30 | 0.72 | 1.19 | 0.00 | 4.2 | 0.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 10.29 | 16.17 | 26.24 | 13.00 | 179.1 | 128.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.67 | 11.02 | 18.15 | 2.00 | 88.2 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.58 | 10.65 | 16.49 | 2.00 | 90.0 | 90.0 |
| XI | XI | Dean Huijsen | DEF | 3 | 4.4 | 3.16 | 8.54 | 13.72 | 2.00 | 82.7 | 90.0 |
| Bench 2 | Autosub In | Jan Bednarek | DEF | 17 | 4.0 | 2.33 | 7.02 | 11.40 | 1.00 | 86.7 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.82 | 17.90 | 30.06 | 2.00 | 89.3 | 89.0 |
| XI | Bench | Cody Gakpo | FWD | 12 | 7.6 | 9.42 | 14.76 | 22.78 | 0.00 | 140.9 | 0.0 |
| Bench 3 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 2.23 | 7.75 | 12.76 | 0.00 | 56.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 20.35 | 29.75 | 48.68 | 20.00 | 180.0 | 180.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.2 | 6.69 | 19.36 | 31.97 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.53 | 15.35 | 25.23 | 3.00 | 83.1 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 5.73 | 15.02 | 23.05 | 5.00 | 85.2 | 76.0 |
| Bench 4 | Bench | Boubakary Soumaré | MID | 11 | 4.4 | 2.06 | 6.27 | 10.43 | 2.00 | 76.3 | 90.0 |

## GW26

- Train rows: 150945
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 67.23
- Actual score: 75.00
- Transfer: Cody Gakpo -> Chris Wood (projected gain 8.32, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.69 | 10.47 | 17.03 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.47 | 0.97 | 1.46 | 0.00 | 4.5 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.77 | 17.27 | 27.97 | 6.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.70 | 11.19 | 18.03 | 1.00 | 88.5 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.19 | 9.19 | 15.04 | 1.00 | 89.1 | 90.0 |
| XI | XI | Dean Huijsen | DEF | 3 | 4.4 | 2.57 | 7.63 | 12.40 | 2.00 | 81.2 | 90.0 |
| Bench 2 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 2.42 | 7.17 | 11.69 | 1.00 | 86.3 | 11.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 6.03 | 17.82 | 29.27 | 13.00 | 90.0 | 86.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 5.26 | 15.43 | 25.20 | 5.00 | 86.8 | 90.0 |
| Bench 4 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 1.45 | 4.95 | 9.71 | 0.00 | 26.6 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.28 | 30.40 | 49.53 | 14.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.1 | 6.07 | 18.48 | 30.39 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.14 | 17.26 | 26.81 | 14.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 4.25 | 12.64 | 19.92 | 2.00 | 67.7 | 72.0 |
| Bench 3 | Bench | Boubakary Soumaré | MID | 11 | 4.4 | 2.40 | 6.68 | 10.87 | 2.00 | 76.0 | 90.0 |

## GW27

- Train rows: 151728
- Bank: 0.50 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 67.89
- Actual score: 52.00
- Transfer: Dean Huijsen -> Daniel Muñoz (projected gain 4.34, hit 0)
- Autosub: Boubakary Soumaré replaced Alexander Isak.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.28 | 9.88 | 16.05 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.32 | 0.74 | 1.12 | 0.00 | 2.9 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.76 | 16.33 | 26.99 | 6.00 | 90.0 | 76.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.9 | 3.89 | 11.11 | 18.01 | 4.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.44 | 10.28 | 16.74 | 0.00 | 85.0 | 18.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 2.87 | 8.66 | 14.21 | 6.00 | 87.2 | 90.0 |
| Bench 3 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.91 | 3.84 | 7.17 | 0.00 | 42.5 | 0.0 |
| XI | Bench | Alexander Isak | FWD | 15 | 9.5 | 5.45 | 17.69 | 28.75 | 0.00 | 90.0 | 0.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 4.73 | 15.02 | 25.79 | 2.00 | 90.0 | 84.0 |
| Bench 4 | Bench | Iliman Ndiaye | FWD | 8 | 5.4 | 0.70 | 4.17 | 8.23 | 0.00 | 17.1 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.75 | 30.00 | 49.25 | 6.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 7.12 | 19.33 | 31.18 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.03 | 18.16 | 28.52 | 5.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 3.82 | 11.53 | 18.53 | 10.00 | 65.6 | 90.0 |
| Bench 2 | Autosub In | Boubakary Soumaré | MID | 11 | 4.4 | 2.45 | 6.78 | 11.07 | 2.00 | 76.4 | 60.0 |