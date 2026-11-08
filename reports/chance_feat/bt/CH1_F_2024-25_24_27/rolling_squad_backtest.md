# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 366.32
- Total actual points: 340.00
- Average predicted points: 91.58
- Average actual points: 85.00
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
- Predicted score: 112.45
- Actual score: 118.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.41) beats the best remaining Bench Boost opportunity (14.22).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.41) beats the best remaining Bench Boost opportunity (14.22).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 7.44 | 12.11 | 18.58 | 10.00 | 180.0 | 180.0 |
| Bench 1 | Bench Boost | Hákon Valdimarsson | GK | 4 | 3.9 | 0.47 | 1.06 | 1.85 | 1.00 | 9.3 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 10.15 | 16.83 | 26.18 | 7.00 | 180.0 | 98.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.45 | 10.64 | 17.61 | 4.00 | 83.2 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 6.38 | 10.51 | 16.04 | 7.00 | 176.1 | 177.0 |
| Bench 2 | Bench Boost | Jan Bednarek | DEF | 17 | 4.0 | 3.01 | 8.28 | 13.20 | 1.00 | 89.0 | 90.0 |
| Bench 3 | Bench Boost | Dean Huijsen | DEF | 3 | 4.4 | 2.53 | 8.09 | 13.32 | 0.00 | 80.7 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 6.77 | 19.81 | 32.84 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cody Gakpo | FWD | 12 | 7.6 | 11.45 | 18.46 | 27.88 | 7.00 | 171.6 | 137.0 |
| XI | XI | Iliman Ndiaye | FWD | 8 | 5.5 | 7.51 | 12.19 | 18.63 | 9.00 | 171.4 | 114.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 16.78 | 26.23 | 42.62 | 29.00 | 180.0 | 177.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 7.35 | 19.66 | 33.09 | 6.00 | 90.0 | 89.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.06 | 16.74 | 27.22 | 2.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 4.04 | 13.33 | 21.07 | 2.00 | 89.4 | 90.0 |
| Bench 4 | Bench Boost | Boubakary Soumaré | MID | 11 | 4.4 | 2.29 | 6.53 | 10.51 | 2.00 | 74.3 | 90.0 |

## GW25

- Train rows: 150166
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 118.15
- Actual score: 95.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (23.41) beats the best remaining Triple Captain opportunity (11.55).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (23.41) beats the best remaining Triple Captain opportunity (11.55).
- Autosub: Jan Bednarek replaced Cody Gakpo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.78 | 11.46 | 17.97 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 1.42 | 3.62 | 5.60 | 0.00 | 40.7 | 0.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 10.18 | 16.08 | 26.06 | 13.00 | 175.6 | 128.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.74 | 11.10 | 18.17 | 2.00 | 86.6 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.49 | 10.67 | 16.59 | 2.00 | 90.0 | 90.0 |
| XI | XI | Dean Huijsen | DEF | 3 | 4.4 | 3.13 | 8.41 | 13.61 | 2.00 | 80.2 | 90.0 |
| Bench 2 | Autosub In | Jan Bednarek | DEF | 17 | 4.0 | 2.36 | 7.11 | 11.70 | 1.00 | 84.6 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.83 | 17.76 | 29.96 | 2.00 | 89.3 | 89.0 |
| XI | Bench | Cody Gakpo | FWD | 12 | 7.6 | 8.94 | 14.77 | 22.80 | 0.00 | 134.7 | 0.0 |
| Bench 3 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 2.24 | 8.68 | 14.53 | 0.00 | 57.2 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 20.38 | 29.53 | 48.33 | 20.00 | 180.0 | 180.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.2 | 6.73 | 19.42 | 32.06 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.51 | 15.48 | 25.38 | 3.00 | 82.7 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 5.69 | 15.31 | 23.74 | 5.00 | 83.6 | 76.0 |
| Bench 4 | Bench | Boubakary Soumaré | MID | 11 | 4.4 | 2.13 | 6.55 | 10.85 | 2.00 | 76.9 | 90.0 |

## GW26

- Train rows: 150945
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 67.37
- Actual score: 75.00
- Transfer: Cody Gakpo -> Chris Wood (projected gain 8.71, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.71 | 10.49 | 17.03 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 0.77 | 1.84 | 2.93 | 0.00 | 18.7 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.62 | 17.12 | 27.80 | 6.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.70 | 11.13 | 17.84 | 1.00 | 86.6 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.19 | 9.21 | 14.96 | 1.00 | 87.4 | 90.0 |
| XI | XI | Dean Huijsen | DEF | 3 | 4.4 | 2.62 | 7.66 | 12.44 | 2.00 | 79.3 | 90.0 |
| Bench 3 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 2.46 | 7.36 | 11.97 | 1.00 | 84.3 | 11.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 6.15 | 18.14 | 29.89 | 13.00 | 90.0 | 86.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 5.31 | 15.59 | 25.22 | 5.00 | 86.1 | 90.0 |
| Bench 4 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 1.39 | 4.73 | 9.03 | 0.00 | 25.5 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.31 | 30.06 | 48.99 | 14.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.1 | 6.14 | 18.39 | 30.42 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.11 | 16.99 | 26.50 | 14.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 4.20 | 13.11 | 20.42 | 2.00 | 65.5 | 72.0 |
| Bench 2 | Bench | Boubakary Soumaré | MID | 11 | 4.4 | 2.48 | 6.95 | 11.25 | 2.00 | 76.5 | 90.0 |

## GW27

- Train rows: 151728
- Bank: 0.50 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 68.35
- Actual score: 52.00
- Transfer: Dean Huijsen -> Daniel Muñoz (projected gain 4.25, hit 0)
- Autosub: Boubakary Soumaré replaced Alexander Isak.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.24 | 9.87 | 16.04 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 0.53 | 1.50 | 2.33 | 0.00 | 16.1 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.86 | 16.41 | 27.00 | 6.00 | 90.0 | 76.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.9 | 3.91 | 11.18 | 18.08 | 4.00 | 89.4 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.41 | 10.10 | 16.41 | 0.00 | 83.4 | 18.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 2.83 | 8.70 | 14.17 | 6.00 | 85.3 | 90.0 |
| Bench 3 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.99 | 4.84 | 8.83 | 0.00 | 43.2 | 0.0 |
| XI | Bench | Alexander Isak | FWD | 15 | 9.5 | 5.53 | 17.60 | 28.80 | 0.00 | 90.0 | 0.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 4.84 | 15.34 | 26.00 | 2.00 | 90.0 | 84.0 |
| Bench 4 | Bench | Iliman Ndiaye | FWD | 8 | 5.4 | 0.63 | 3.93 | 7.57 | 0.00 | 15.7 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.87 | 29.87 | 48.88 | 6.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 7.20 | 19.37 | 31.61 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.98 | 17.91 | 28.26 | 5.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 3.82 | 11.84 | 18.77 | 10.00 | 63.7 | 90.0 |
| Bench 2 | Autosub In | Boubakary Soumaré | MID | 11 | 4.4 | 2.50 | 6.94 | 11.26 | 2.00 | 76.6 | 60.0 |