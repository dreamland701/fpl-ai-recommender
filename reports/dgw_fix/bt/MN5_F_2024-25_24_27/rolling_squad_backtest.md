# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 303.96
- Total actual points: 336.00
- Average predicted points: 75.99
- Average actual points: 84.00
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
- Predicted score: 83.45
- Actual score: 120.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.69) beats the best remaining Bench Boost opportunity (12.88).
- Chip advisory: triple_captain (0.66): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.69) beats the best remaining Bench Boost opportunity (12.88).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 4.82 | 12.18 | 18.69 | 10.00 | 128.1 | 180.0 |
| Bench 1 | Bench Boost | Cieran Slicker | GK | 10 | 3.9 | 0.19 | 0.10 | 0.07 | 0.00 | 1.9 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 6.43 | 16.84 | 26.21 | 7.00 | 119.8 | 98.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.34 | 10.61 | 17.59 | 4.00 | 82.0 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 4.20 | 10.51 | 16.04 | 7.00 | 117.7 | 177.0 |
| Bench 2 | Bench Boost | Jan Bednarek | DEF | 17 | 4.0 | 2.95 | 8.26 | 13.18 | 1.00 | 87.7 | 90.0 |
| Bench 4 | Bench Boost | Taylor Harwood-Bellis | DEF | 17 | 4.0 | 2.57 | 7.03 | 11.29 | 1.00 | 81.0 | 45.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 6.76 | 20.04 | 33.23 | 2.00 | 95.2 | 90.0 |
| Vice Captain | XI | Cody Gakpo | FWD | 12 | 7.6 | 7.60 | 18.66 | 28.17 | 7.00 | 123.8 | 137.0 |
| XI | XI | Iliman Ndiaye | FWD | 8 | 5.5 | 4.96 | 12.27 | 18.74 | 9.00 | 118.8 | 114.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 9.48 | 26.31 | 42.77 | 29.00 | 130.3 | 177.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 7.24 | 19.69 | 33.17 | 6.00 | 101.1 | 89.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.14 | 16.76 | 27.28 | 2.00 | 93.9 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 4.41 | 13.33 | 21.06 | 2.00 | 95.1 | 90.0 |
| Bench 3 | Bench Boost | Enzo Fernández | MID | 6 | 4.8 | 2.86 | 7.40 | 12.56 | 4.00 | 63.4 | 90.0 |

## GW25

- Train rows: 150166
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 83.72
- Actual score: 94.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (14.34) beats the best remaining Triple Captain opportunity (9.31).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (14.34) beats the best remaining Triple Captain opportunity (9.31).
- Autosub: Jan Bednarek replaced Cody Gakpo.
- Autosub: Enzo Fernández replaced Iliman Ndiaye.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.84 | 11.65 | 18.28 | 3.00 | 109.3 | 90.0 |
| Bench 1 | Bench | Cieran Slicker | GK | 10 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 1.0 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 6.30 | 16.32 | 26.46 | 13.00 | 116.0 | 128.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.69 | 11.09 | 18.18 | 2.00 | 86.4 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.60 | 10.88 | 16.92 | 2.00 | 105.7 | 90.0 |
| Bench 2 | Autosub In | Jan Bednarek | DEF | 17 | 4.0 | 2.36 | 7.07 | 11.65 | 1.00 | 84.3 | 90.0 |
| Bench 4 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.0 | 1.99 | 5.86 | 9.70 | 0.00 | 65.1 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.61 | 17.79 | 30.04 | 2.00 | 86.0 | 89.0 |
| XI | Bench | Cody Gakpo | FWD | 12 | 7.6 | 5.78 | 14.96 | 23.14 | 0.00 | 95.9 | 0.0 |
| XI | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 2.68 | 9.11 | 14.82 | 0.00 | 66.7 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 11.31 | 29.85 | 48.87 | 20.00 | 172.9 | 180.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 6.58 | 19.52 | 32.25 | 2.00 | 93.3 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.54 | 15.54 | 25.50 | 3.00 | 82.6 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 6.17 | 15.48 | 23.99 | 5.00 | 89.9 | 76.0 |
| Bench 3 | Autosub In | Enzo Fernández | MID | 6 | 4.8 | 2.30 | 7.03 | 11.45 | 1.00 | 62.6 | 90.0 |

## GW26

- Train rows: 150945
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 67.72
- Actual score: 74.00
- Transfer: Cody Gakpo -> Chris Wood (projected gain 19.43, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.79 | 10.52 | 17.11 | 1.00 | 97.2 | 90.0 |
| Bench 1 | Bench | Cieran Slicker | GK | 10 | 3.9 | 0.09 | 0.00 | 0.00 | 0.00 | 1.8 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.75 | 17.45 | 28.32 | 6.00 | 109.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.70 | 11.17 | 17.91 | 1.00 | 87.3 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.28 | 9.24 | 15.04 | 1.00 | 89.0 | 90.0 |
| XI | XI | Jan Bednarek | DEF | 17 | 4.0 | 2.41 | 7.32 | 11.93 | 1.00 | 82.7 | 11.0 |
| Bench 4 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.0 | 1.05 | 3.55 | 6.15 | 0.00 | 37.7 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 6.08 | 18.11 | 29.86 | 13.00 | 96.2 | 86.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 5.29 | 15.71 | 25.43 | 5.00 | 85.5 | 90.0 |
| Bench 3 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 1.70 | 5.65 | 10.57 | 0.00 | 32.1 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.29 | 30.47 | 49.65 | 14.00 | 162.3 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.1 | 5.98 | 18.45 | 30.54 | 2.00 | 93.4 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.35 | 17.12 | 26.71 | 14.00 | 95.6 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 4.51 | 13.20 | 20.58 | 2.00 | 68.4 | 72.0 |
| Bench 2 | Bench | Enzo Fernández | MID | 6 | 4.7 | 2.40 | 7.51 | 12.05 | 7.00 | 72.2 | 90.0 |

## GW27

- Train rows: 151728
- Bank: 0.50 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 69.08
- Actual score: 48.00
- Transfer: Vitalii Mykolenko -> Daniel Muñoz (projected gain 5.35, hit 0)
- Autosub: Taylor Harwood-Bellis replaced Alexander Isak.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.31 | 9.92 | 16.16 | 2.00 | 94.4 | 90.0 |
| Bench 1 | Bench | Cieran Slicker | GK | 10 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 1.4 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.92 | 16.61 | 27.32 | 6.00 | 100.3 | 76.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.9 | 3.91 | 11.02 | 17.85 | 4.00 | 88.3 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.39 | 10.13 | 16.47 | 0.00 | 83.8 | 18.0 |
| Bench 2 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 1.37 | 5.10 | 8.84 | 0.00 | 50.9 | 0.0 |
| Bench 4 | Autosub In | Taylor Harwood-Bellis | DEF | 17 | 4.0 | 0.49 | 2.37 | 4.43 | 1.00 | 25.9 | 45.0 |
| XI | Bench | Alexander Isak | FWD | 15 | 9.5 | 5.43 | 17.65 | 28.91 | 0.00 | 95.3 | 0.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 4.81 | 15.34 | 26.03 | 2.00 | 94.0 | 84.0 |
| Bench 3 | Bench | Iliman Ndiaye | FWD | 8 | 5.4 | 0.94 | 4.85 | 9.09 | 0.00 | 21.8 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.70 | 30.06 | 49.22 | 6.00 | 142.2 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 7.23 | 19.41 | 31.69 | 3.00 | 104.2 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.13 | 17.98 | 28.39 | 5.00 | 95.4 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 3.84 | 11.88 | 18.84 | 10.00 | 62.1 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.7 | 3.69 | 9.11 | 14.38 | 3.00 | 76.6 | 89.0 |