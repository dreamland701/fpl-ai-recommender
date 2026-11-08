# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 233.84
- Total actual points: 254.00
- Average predicted points: 58.46
- Average actual points: 63.50
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
- Predicted score: 58.13
- Actual score: 82.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Gabriel dos Santos Magalhães replaced Kieran Trippier.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.46 | 9.72 | 16.09 | 11.00 | 75.4 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 4.4 | 3.04 | 9.16 | 15.23 | 2.00 | 86.2 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.3 | 5.10 | 14.99 | 24.28 | 0.00 | 88.3 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.32 | 12.46 | 20.49 | 2.00 | 88.9 | 90.0 |
| XI | Bench | Kieran Trippier | DEF | 15 | 6.9 | 3.78 | 12.02 | 20.47 | 0.00 | 79.2 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 3.76 | 11.05 | 18.14 | 0.00 | 86.0 | 90.0 |
| Bench 2 | Autosub In | Gabriel dos Santos Magalhães | DEF | 1 | 4.9 | 3.19 | 9.68 | 15.66 | 1.00 | 82.0 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 4.9 | 3.96 | 10.49 | 16.40 | 2.00 | 82.7 | 90.0 |
| Bench 3 | Bench | Jean-Philippe Mateta | FWD | 8 | 4.9 | 3.12 | 8.55 | 13.87 | 2.00 | 62.0 | 85.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.60 | 8.24 | 13.32 | 1.00 | 74.5 | 23.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.3 | 6.82 | 19.61 | 32.21 | 16.00 | 93.6 | 90.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.9 | 5.69 | 16.81 | 28.18 | 9.00 | 91.6 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.56 | 16.41 | 26.38 | 7.00 | 82.7 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.8 | 4.62 | 13.87 | 22.99 | 3.00 | 83.0 | 90.0 |
| XI | XI | Michael Olise | MID | 8 | 5.8 | 4.25 | 12.04 | 19.50 | 15.00 | 81.6 | 90.0 |

## GW21

- Train rows: 118627
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 59.26
- Actual score: 57.00
- Transfer: Kieran Trippier -> Virgil van Dijk (projected gain 0.63, hit 0)
- Autosub: Gabriel dos Santos Magalhães replaced Trent Alexander-Arnold.
- Autosub: Cameron Archer replaced Mohamed Salah.
- Autosub: Jean-Philippe Mateta replaced Son Heung-min.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 4.20 | 11.71 | 19.31 | 3.00 | 87.0 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 4.4 | 2.92 | 8.72 | 14.46 | 9.00 | 87.8 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 11 | 8.3 | 4.64 | 14.19 | 23.06 | 0.00 | 83.6 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 3.82 | 12.03 | 20.01 | 6.00 | 86.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 3.80 | 10.61 | 17.30 | 6.00 | 83.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.2 | 3.37 | 10.01 | 16.34 | 6.00 | 79.7 | 90.0 |
| Bench 2 | Autosub In | Gabriel dos Santos Magalhães | DEF | 1 | 4.9 | 3.30 | 9.47 | 15.49 | 17.00 | 85.1 | 80.0 |
| XI | XI | Chris Wood | FWD | 16 | 4.9 | 4.01 | 11.46 | 18.04 | 8.00 | 75.8 | 90.0 |
| Bench 4 | Autosub In | Jean-Philippe Mateta | FWD | 8 | 4.9 | 2.10 | 7.34 | 12.42 | 2.00 | 57.1 | 90.0 |
| Bench 3 | Autosub In | Cameron Archer | FWD | 17 | 4.5 | 2.40 | 6.88 | 11.56 | 1.00 | 53.6 | 23.0 |
| Captain | Bench | Mohamed Salah | MID | 11 | 13.3 | 7.45 | 21.92 | 35.29 | 0.00 | 102.4 | 0.0 |
| XI | Bench | Son Heung-min | MID | 18 | 9.9 | 5.76 | 17.83 | 29.84 | 0.00 | 94.2 | 0.0 |
| Vice Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 5.97 | 16.04 | 25.76 | 3.00 | 86.2 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.8 | 4.93 | 14.64 | 23.47 | 2.00 | 79.8 | 90.0 |
| XI | Bench | Michael Olise | MID | 8 | 5.8 | 3.84 | 12.45 | 20.79 | 0.00 | 87.8 | 0.0 |

## GW22

- Train rows: 119414
- Bank: 0.60 -> 2.50
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Phil Foden
- Effective captain: Bukayo Saka
- Chip used: triple_captain
- Predicted score: 57.03
- Actual score: 66.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.03) beats the best remaining Triple Captain opportunity (6.84).
- Transfer: Son Heung-min -> Phil Foden (projected gain 7.16, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (6.03) beats the best remaining Triple Captain opportunity (6.84).
- Autosub: Jean-Philippe Mateta replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.58 | 10.59 | 17.68 | 3.00 | 80.3 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 4.4 | 3.12 | 9.12 | 15.25 | 10.00 | 91.2 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.50 | 13.38 | 21.85 | 1.00 | 82.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 4.9 | 4.05 | 11.23 | 17.91 | 2.00 | 86.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 3.86 | 10.98 | 17.82 | 2.00 | 82.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.2 | 3.68 | 10.47 | 16.81 | 2.00 | 81.0 | 90.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 2.73 | 9.28 | 16.73 | 1.00 | 35.2 | 22.0 |
| XI | XI | Chris Wood | FWD | 16 | 4.9 | 3.27 | 9.99 | 16.03 | 1.00 | 80.5 | 45.0 |
| Bench 2 | Autosub In | Jean-Philippe Mateta | FWD | 8 | 4.9 | 2.91 | 7.72 | 12.83 | 2.00 | 65.6 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.5 | 2.07 | 6.54 | 11.04 | 1.00 | 44.0 | 3.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 6.03 | 16.80 | 26.29 | 10.00 | 80.3 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 7.9 | 4.99 | 14.85 | 23.18 | 6.00 | 63.8 | 76.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.2 | 3.77 | 12.94 | 23.93 | 0.00 | 26.8 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.17 | 12.74 | 21.59 | 1.00 | 64.2 | 90.0 |
| XI | XI | Michael Olise | MID | 8 | 5.8 | 3.06 | 9.34 | 16.01 | 16.00 | 42.5 | 69.0 |

## GW23

- Train rows: 120213
- Bank: 2.50 -> 0.40
- Free transfers: 2 -> 2
- Captain: Julián Álvarez
- Vice captain: Bukayo Saka
- Effective captain: Julián Álvarez
- Chip used: bench_boost
- Predicted score: 59.42
- Actual score: 49.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.83) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Chris Wood -> Julián Álvarez (projected gain 8.36, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.83) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.16 | 10.29 | 17.06 | 1.00 | 82.3 | 45.0 |
| Bench 1 | Bench Boost | Jordan Pickford | GK | 9 | 4.4 | 3.10 | 9.32 | 15.58 | 2.00 | 91.2 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.30 | 12.62 | 20.76 | 1.00 | 86.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 3.51 | 10.72 | 17.55 | 1.00 | 84.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 4.9 | 3.14 | 10.04 | 16.57 | -1.00 | 83.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.2 | 3.09 | 9.99 | 16.47 | 1.00 | 83.1 | 90.0 |
| Bench 3 | Bench Boost | Trent Alexander-Arnold | DEF | 11 | 8.4 | 2.64 | 9.53 | 16.47 | 1.00 | 47.2 | 57.0 |
| Captain | Captain | Julián Álvarez | FWD | 13 | 7.0 | 5.71 | 15.72 | 24.95 | 2.00 | 79.0 | 90.0 |
| Bench 2 | Bench Boost | Jean-Philippe Mateta | FWD | 8 | 4.9 | 2.64 | 7.64 | 12.42 | 6.00 | 69.9 | 79.0 |
| Bench 4 | Bench Boost | Cameron Archer | FWD | 17 | 4.4 | 1.45 | 5.31 | 9.60 | 1.00 | 31.5 | 25.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 5.45 | 15.95 | 25.92 | 9.00 | 84.9 | 78.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 4.80 | 14.36 | 23.21 | 20.00 | 71.9 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 3.99 | 12.53 | 21.45 | 2.00 | 72.6 | 90.0 |
| XI | XI | Mohamed Salah | MID | 11 | 13.1 | 3.22 | 11.66 | 20.42 | 0.00 | 37.0 | 0.0 |
| XI | XI | Michael Olise | MID | 8 | 5.8 | 3.49 | 11.19 | 18.85 | 1.00 | 70.3 | 10.0 |