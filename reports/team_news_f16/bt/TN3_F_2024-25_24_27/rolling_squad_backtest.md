# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 366.63
- Total actual points: 336.00
- Average predicted points: 91.66
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
- Predicted score: 113.64
- Actual score: 120.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.89) beats the best remaining Bench Boost opportunity (14.74).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.89) beats the best remaining Bench Boost opportunity (14.74).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 7.51 | 12.16 | 18.60 | 10.00 | 180.0 | 180.0 |
| Bench 1 | Bench Boost | Marcus Bettinelli | GK | 6 | 3.9 | 0.18 | 0.46 | 0.87 | 0.00 | 1.4 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 10.20 | 16.90 | 26.26 | 7.00 | 180.0 | 98.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.52 | 10.79 | 17.78 | 4.00 | 84.9 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 6.46 | 10.57 | 16.08 | 7.00 | 178.0 | 177.0 |
| Bench 2 | Bench Boost | Jan Bednarek | DEF | 17 | 4.0 | 3.06 | 8.37 | 13.27 | 1.00 | 90.0 | 90.0 |
| Bench 4 | Bench Boost | Taylor Harwood-Bellis | DEF | 17 | 4.0 | 2.54 | 6.95 | 11.09 | 1.00 | 80.4 | 45.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 6.82 | 19.94 | 33.01 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cody Gakpo | FWD | 12 | 7.6 | 11.50 | 18.48 | 27.85 | 7.00 | 173.1 | 137.0 |
| XI | XI | Iliman Ndiaye | FWD | 8 | 5.5 | 7.57 | 12.22 | 18.62 | 9.00 | 173.0 | 114.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 16.86 | 26.32 | 42.75 | 29.00 | 180.0 | 177.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 7.40 | 19.79 | 33.24 | 6.00 | 90.0 | 89.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.09 | 16.79 | 27.26 | 2.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 4.08 | 13.35 | 21.04 | 2.00 | 90.0 | 90.0 |
| Bench 3 | Bench Boost | Enzo Fernández | MID | 6 | 4.8 | 2.99 | 7.65 | 12.84 | 4.00 | 66.9 | 90.0 |

## GW25

- Train rows: 150166
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 117.33
- Actual score: 94.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (23.38) beats the best remaining Triple Captain opportunity (11.54).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (23.38) beats the best remaining Triple Captain opportunity (11.54).
- Autosub: Enzo Fernández replaced Cody Gakpo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.80 | 11.55 | 18.08 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 6 | 3.9 | 0.10 | 0.40 | 0.78 | 0.00 | 6.4 | 0.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 10.30 | 16.23 | 26.25 | 13.00 | 178.9 | 128.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.80 | 11.24 | 18.32 | 2.00 | 88.1 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.50 | 10.72 | 16.65 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jan Bednarek | DEF | 17 | 4.0 | 2.42 | 7.21 | 11.78 | 1.00 | 86.2 | 90.0 |
| Bench 4 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.0 | 1.08 | 3.86 | 6.89 | 0.00 | 1.3 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.89 | 17.89 | 30.12 | 2.00 | 90.0 | 89.0 |
| XI | Bench | Cody Gakpo | FWD | 12 | 7.6 | 8.62 | 14.99 | 23.68 | 0.00 | 69.4 | 0.0 |
| Bench 3 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 1.76 | 7.07 | 11.98 | 0.00 | 1.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 20.35 | 29.54 | 48.37 | 20.00 | 180.0 | 180.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.2 | 6.67 | 19.39 | 32.16 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.56 | 15.60 | 25.51 | 3.00 | 84.1 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 5.71 | 15.33 | 23.70 | 5.00 | 84.3 | 76.0 |
| Bench 2 | Autosub In | Enzo Fernández | MID | 6 | 4.8 | 2.39 | 7.17 | 11.77 | 1.00 | 64.6 | 90.0 |

## GW26

- Train rows: 150945
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 67.47
- Actual score: 74.00
- Transfer: Cody Gakpo -> Chris Wood (projected gain 8.27, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.75 | 10.62 | 17.19 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 6 | 3.9 | 0.00 | 0.17 | 0.41 | 0.00 | 1.5 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.64 | 17.18 | 27.86 | 6.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.75 | 11.25 | 17.97 | 1.00 | 87.9 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.23 | 9.32 | 15.11 | 1.00 | 88.2 | 90.0 |
| XI | XI | Jan Bednarek | DEF | 17 | 4.0 | 2.52 | 7.47 | 12.08 | 1.00 | 85.8 | 11.0 |
| Bench 4 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.0 | 0.32 | 1.91 | 3.88 | 0.00 | 0.6 | 0.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 6.20 | 18.27 | 30.01 | 13.00 | 90.0 | 86.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 5.37 | 15.72 | 25.36 | 5.00 | 87.7 | 90.0 |
| Bench 3 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 1.09 | 4.26 | 8.68 | 0.00 | 0.5 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.26 | 30.04 | 48.99 | 14.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.1 | 6.20 | 18.55 | 30.60 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.04 | 16.88 | 26.47 | 14.00 | 88.4 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 4.25 | 13.20 | 20.51 | 2.00 | 66.8 | 72.0 |
| Bench 2 | Bench | Enzo Fernández | MID | 6 | 4.7 | 2.43 | 7.59 | 12.11 | 7.00 | 72.9 | 90.0 |

## GW27

- Train rows: 151728
- Bank: 0.50 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 68.19
- Actual score: 48.00
- Transfer: Vitalii Mykolenko -> Daniel Muñoz (projected gain 2.46, hit 0)
- Autosub: Taylor Harwood-Bellis replaced Alexander Isak.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.18 | 9.80 | 16.14 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 6 | 3.9 | 0.47 | 0.67 | 1.09 | 0.00 | 7.5 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.79 | 16.33 | 27.05 | 6.00 | 90.0 | 76.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.9 | 3.84 | 11.07 | 18.08 | 4.00 | 87.8 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.35 | 10.02 | 16.45 | 0.00 | 82.0 | 18.0 |
| Bench 2 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.88 | 3.99 | 7.25 | 0.00 | 40.8 | 0.0 |
| Bench 4 | Autosub In | Taylor Harwood-Bellis | DEF | 17 | 4.0 | 0.22 | 1.65 | 3.38 | 1.00 | 19.6 | 45.0 |
| XI | Bench | Alexander Isak | FWD | 15 | 9.5 | 5.47 | 17.53 | 28.88 | 0.00 | 90.0 | 0.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 4.76 | 15.21 | 25.99 | 2.00 | 90.0 | 84.0 |
| Bench 3 | Bench | Iliman Ndiaye | FWD | 8 | 5.4 | 0.69 | 4.22 | 8.19 | 0.00 | 17.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.74 | 29.71 | 48.90 | 6.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 7.13 | 19.28 | 31.63 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.90 | 17.78 | 28.26 | 5.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 3.77 | 11.75 | 18.78 | 10.00 | 62.6 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.7 | 3.53 | 8.99 | 14.36 | 3.00 | 74.1 | 89.0 |