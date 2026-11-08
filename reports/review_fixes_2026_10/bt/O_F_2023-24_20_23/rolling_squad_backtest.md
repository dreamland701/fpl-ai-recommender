# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 233.42
- Total actual points: 234.00
- Average predicted points: 58.35
- Average actual points: 58.50
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW19 are included before the first simulated week.
- League-average scores were not available for this run.

## GW20

- Train rows: 117854
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Son Heung-min
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 58.06
- Actual score: 82.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub outfielders: Gabriel dos Santos Magalhães.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.44 | 9.60 | 15.82 | 11.00 | 75.4 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 4.4 | 3.08 | 9.21 | 15.20 | 2.00 | 86.1 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.3 | 5.12 | 14.93 | 24.13 | 0.00 | 88.3 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.30 | 12.36 | 20.40 | 2.00 | 88.9 | 90.0 |
| XI | Bench | Kieran Trippier | DEF | 15 | 6.9 | 3.79 | 12.03 | 20.33 | 0.00 | 79.2 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 3.75 | 11.05 | 17.98 | 0.00 | 86.0 | 90.0 |
| Bench 2 | Autosub In | Gabriel dos Santos Magalhães | DEF | 1 | 4.9 | 3.19 | 9.71 | 15.66 | 1.00 | 82.0 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 4.9 | 3.98 | 10.40 | 16.34 | 2.00 | 82.7 | 90.0 |
| Bench 3 | Bench | Jean-Philippe Mateta | FWD | 8 | 4.9 | 3.08 | 8.48 | 13.59 | 2.00 | 62.0 | 85.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.61 | 8.27 | 13.36 | 1.00 | 74.5 | 23.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.3 | 6.83 | 19.60 | 31.94 | 16.00 | 93.5 | 90.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.9 | 5.66 | 16.72 | 27.95 | 9.00 | 91.6 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.55 | 16.49 | 26.27 | 7.00 | 82.7 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.8 | 4.60 | 13.88 | 22.86 | 3.00 | 83.0 | 90.0 |
| XI | XI | Michael Olise | MID | 8 | 5.8 | 4.21 | 11.98 | 19.33 | 15.00 | 81.7 | 90.0 |

## GW21

- Train rows: 118627
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 59.15
- Actual score: 37.00
- Transfer: Kieran Trippier -> Virgil van Dijk (projected gain 0.57, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 4.23 | 11.76 | 19.19 | 3.00 | 87.0 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 4.4 | 2.89 | 8.67 | 14.36 | 9.00 | 87.8 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 4.62 | 14.08 | 22.87 | 0.00 | 83.6 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 3.84 | 12.03 | 19.98 | 6.00 | 86.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.79 | 10.58 | 17.25 | 6.00 | 83.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.2 | 3.34 | 9.92 | 16.22 | 6.00 | 79.7 | 90.0 |
| Bench 2 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.29 | 9.44 | 15.44 | 17.00 | 85.1 | 80.0 |
| XI | XI | Chris Wood | FWD | 16 | 4.9 | 3.98 | 11.67 | 18.26 | 8.00 | 75.8 | 90.0 |
| Bench 4 | Bench | Jean-Philippe Mateta | FWD | 8 | 4.9 | 2.06 | 7.32 | 12.29 | 2.00 | 57.1 | 90.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 4.5 | 2.44 | 6.80 | 11.49 | 1.00 | 53.5 | 23.0 |
| Captain | Bench | Mohamed Salah | MID | 11 | 13.3 | 7.43 | 22.03 | 35.41 | 0.00 | 102.4 | 0.0 |
| XI | Bench | Son Heung-min | MID | 18 | 9.9 | 5.77 | 17.86 | 29.84 | 0.00 | 94.2 | 0.0 |
| Vice Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 5.96 | 15.96 | 25.59 | 3.00 | 86.2 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.96 | 14.92 | 23.96 | 2.00 | 79.8 | 90.0 |
| XI | Bench | Michael Olise | MID | 8 | 5.8 | 3.81 | 12.48 | 20.73 | 0.00 | 87.9 | 0.0 |

## GW22

- Train rows: 119414
- Bank: 0.60 -> 2.50
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Phil Foden
- Effective captain: Bukayo Saka
- Chip used: triple_captain
- Predicted score: 56.99
- Actual score: 66.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.05) beats the best remaining Triple Captain opportunity (6.86).
- Transfer: Son Heung-min -> Phil Foden (projected gain 7.27, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (6.05) beats the best remaining Triple Captain opportunity (6.86).
- Autosub outfielders: Jean-Philippe Mateta.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.55 | 10.52 | 17.40 | 3.00 | 80.3 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 4.5 | 3.12 | 9.13 | 15.17 | 10.00 | 91.2 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.47 | 13.50 | 22.14 | 1.00 | 82.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 4.07 | 11.32 | 18.01 | 2.00 | 86.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.88 | 11.04 | 17.89 | 2.00 | 82.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.3 | 3.67 | 10.45 | 16.77 | 2.00 | 81.1 | 90.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | 11 | 8.5 | 2.72 | 9.20 | 16.62 | 1.00 | 35.2 | 22.0 |
| XI | XI | Chris Wood | FWD | 16 | 4.9 | 3.24 | 9.94 | 15.82 | 1.00 | 80.5 | 45.0 |
| Bench 2 | Autosub In | Jean-Philippe Mateta | FWD | 8 | 4.9 | 2.94 | 7.77 | 12.82 | 2.00 | 65.6 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.5 | 2.06 | 6.57 | 11.22 | 1.00 | 44.0 | 3.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.1 | 6.05 | 16.88 | 26.63 | 10.00 | 80.2 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 7.9 | 4.97 | 15.00 | 23.57 | 6.00 | 63.8 | 76.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.2 | 3.76 | 12.94 | 23.87 | 0.00 | 26.8 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.1 | 4.14 | 12.82 | 21.67 | 1.00 | 64.2 | 90.0 |
| XI | XI | Michael Olise | MID | 8 | 5.9 | 3.08 | 9.45 | 16.15 | 16.00 | 42.4 | 69.0 |

## GW23

- Train rows: 120213
- Bank: 2.50 -> 0.50
- Free transfers: 2 -> 2
- Captain: Julián Álvarez
- Vice captain: Bukayo Saka
- Effective captain: Julián Álvarez
- Chip used: bench_boost
- Predicted score: 59.21
- Actual score: 49.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.77) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Chris Wood -> Julián Álvarez (projected gain 8.27, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.77) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.17 | 10.23 | 16.91 | 1.00 | 82.3 | 45.0 |
| Bench 1 | Bench Boost | Jordan Pickford | GK | 9 | 4.5 | 3.13 | 9.35 | 15.55 | 2.00 | 91.1 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.9 | 4.29 | 12.73 | 20.97 | 1.00 | 86.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.52 | 10.72 | 17.64 | 1.00 | 84.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.15 | 10.04 | 16.52 | -1.00 | 83.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.3 | 3.05 | 9.92 | 16.43 | 1.00 | 83.1 | 90.0 |
| Bench 3 | Bench Boost | Trent Alexander-Arnold | DEF | 11 | 8.5 | 2.60 | 9.50 | 16.46 | 1.00 | 47.3 | 57.0 |
| Captain | Captain | Julián Álvarez | FWD | 13 | 7.0 | 5.68 | 15.65 | 24.97 | 2.00 | 79.1 | 90.0 |
| Bench 2 | Bench Boost | Jean-Philippe Mateta | FWD | 8 | 4.9 | 2.62 | 7.61 | 12.39 | 6.00 | 70.0 | 79.0 |
| Bench 4 | Bench Boost | Cameron Archer | FWD | 17 | 4.4 | 1.42 | 5.20 | 9.54 | 1.00 | 31.6 | 25.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.1 | 5.46 | 16.08 | 26.23 | 9.00 | 84.9 | 78.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 4.77 | 14.32 | 23.66 | 20.00 | 72.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.1 | 4.00 | 12.53 | 21.44 | 2.00 | 72.5 | 90.0 |
| XI | XI | Mohamed Salah | MID | 11 | 13.1 | 3.19 | 11.51 | 20.39 | 0.00 | 37.1 | 0.0 |
| XI | XI | Michael Olise | MID | 8 | 5.9 | 3.47 | 11.24 | 19.01 | 1.00 | 70.3 | 10.0 |