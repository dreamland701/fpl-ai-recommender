# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 240.73
- Total actual points: 283.00
- Average predicted points: 60.18
- Average actual points: 70.75
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW11 are included before the first simulated week.
- League-average scores were not available for this run.

## GW12

- Train rows: 140908
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 64.60
- Actual score: 55.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Sánchez | GK | 6 | 4.7 | 3.29 | 9.07 | 14.86 | 1.00 | 88.8 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.09 | 0.41 | 0.60 | 0.00 | 4.9 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.77 | 12.66 | 20.25 | 1.00 | 100.8 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.3 | 4.24 | 12.14 | 19.92 | 0.00 | 87.3 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 3.74 | 10.08 | 16.11 | 1.00 | 91.5 | 90.0 |
| Bench 2 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.50 | 7.91 | 12.80 | 1.00 | 83.3 | 90.0 |
| Bench 3 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 2.27 | 7.12 | 11.77 | 0.00 | 84.4 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 5.72 | 14.88 | 23.43 | 2.00 | 91.3 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.8 | 4.28 | 12.41 | 20.74 | 16.00 | 84.7 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 5.0 | 1.88 | 6.58 | 10.50 | 1.00 | 59.9 | 13.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 8.11 | 22.21 | 36.23 | 13.00 | 114.2 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.94 | 19.51 | 31.98 | 2.00 | 104.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 6.36 | 16.55 | 26.43 | 2.00 | 106.3 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 4.22 | 14.58 | 23.92 | 3.00 | 86.9 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 4.81 | 12.57 | 20.37 | 1.00 | 88.6 | 58.0 |

## GW13

- Train rows: 141592
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 66.04
- Actual score: 85.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.18) beats the best remaining Triple Captain opportunity (8.97).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.18) beats the best remaining Triple Captain opportunity (8.97).
- Autosub: Taylor Harwood-Bellis replaced Joško Gvardiol.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Sánchez | GK | 6 | 4.7 | 2.79 | 8.03 | 13.04 | 7.00 | 81.2 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.39 | 0.49 | 0.68 | 0.00 | 3.3 | 0.0 |
| XI | Bench | Joško Gvardiol | DEF | 13 | 6.3 | 3.38 | 11.35 | 19.03 | 0.00 | 83.1 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.73 | 11.22 | 18.02 | 6.00 | 84.9 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 2.74 | 8.45 | 13.61 | 2.00 | 73.2 | 90.0 |
| Bench 2 | Autosub In | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.63 | 8.05 | 13.06 | 1.00 | 85.0 | 90.0 |
| Bench 4 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 1.25 | 4.10 | 7.27 | 0.00 | 45.1 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 6.47 | 17.71 | 27.44 | 2.00 | 115.4 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 3.93 | 12.70 | 20.40 | 1.00 | 58.9 | 21.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 5.0 | 1.54 | 5.25 | 8.91 | 2.00 | 38.7 | 87.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 8.18 | 24.26 | 38.49 | 13.00 | 107.5 | 83.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.59 | 18.64 | 30.18 | 14.00 | 97.0 | 85.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.30 | 14.72 | 24.60 | 2.00 | 92.1 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.79 | 12.79 | 20.78 | 9.00 | 71.1 | 65.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 2.78 | 9.07 | 15.25 | 2.00 | 56.8 | 85.0 |

## GW14

- Train rows: 142282
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 59.84
- Actual score: 67.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.07) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Joško Gvardiol -> Pedro Porro (projected gain 10.29, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.07) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Sánchez | GK | 6 | 4.7 | 3.57 | 9.46 | 15.06 | 0.00 | 90.1 | 0.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.03 | 0.20 | 0.39 | 0.00 | 3.9 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.29 | 12.68 | 20.52 | 1.00 | 97.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.06 | 11.75 | 18.85 | 1.00 | 87.9 | 28.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 2.50 | 8.09 | 13.35 | 1.00 | 77.1 | 90.0 |
| Bench 2 | Bench Boost | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.34 | 7.20 | 11.89 | 0.00 | 80.1 | 0.0 |
| Bench 4 | Bench Boost | Jan Bednarek | DEF | 17 | 4.0 | 0.76 | 2.75 | 5.07 | 0.00 | 31.6 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.35 | 13.70 | 21.26 | 2.00 | 77.1 | 90.0 |
| Bench 3 | Bench Boost | Alexander Isak | FWD | 15 | 8.5 | 1.94 | 8.26 | 14.87 | 11.00 | 28.8 | 90.0 |
| XI | XI | Cameron Archer | FWD | 17 | 5.0 | 2.45 | 6.90 | 11.14 | 2.00 | 62.4 | 71.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 8.06 | 24.30 | 39.01 | 18.00 | 114.6 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 7.58 | 20.97 | 33.57 | 7.00 | 110.7 | 78.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.44 | 12.73 | 22.05 | 2.00 | 69.1 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.8 | 3.36 | 11.09 | 19.90 | 2.00 | 66.9 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.7 | 3.04 | 9.48 | 16.03 | 2.00 | 64.8 | 70.0 |

## GW15

- Train rows: 142975
- Bank: 0.60 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 50.25
- Actual score: 76.00
- Transfer: none
- No transfer was applied this week.
- Autosub: Taylor Harwood-Bellis replaced Virgil van Dijk.
- Autosub: Cameron Archer replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Sánchez | GK | 6 | 4.7 | 1.33 | 4.65 | 8.27 | 0.00 | 41.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.23 | 0.26 | 0.42 | 0.00 | 2.4 | 0.0 |
| XI | Bench | Virgil van Dijk | DEF | 12 | 6.3 | 2.86 | 9.88 | 16.74 | 0.00 | 66.2 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 2.94 | 9.34 | 15.99 | 3.00 | 67.9 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 2.67 | 7.62 | 12.49 | 1.00 | 77.5 | 82.0 |
| Bench 3 | Autosub In | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 0.97 | 3.70 | 6.91 | 2.00 | 44.2 | 90.0 |
| Bench 4 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.14 | 1.47 | 3.16 | 0.00 | 18.1 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.58 | 13.21 | 21.32 | 1.00 | 80.1 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 4.46 | 13.16 | 22.00 | 8.00 | 74.9 | 90.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 5.0 | 2.21 | 6.56 | 11.00 | 2.00 | 60.5 | 72.0 |
| Captain | Bench | Mohamed Salah | MID | 12 | 13.1 | 7.38 | 23.33 | 38.89 | 0.00 | 91.5 | 0.0 |
| Vice Captain | Captain | Cole Palmer | MID | 6 | 10.9 | 6.90 | 19.64 | 31.84 | 18.00 | 97.7 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.31 | 13.94 | 23.54 | 9.00 | 82.5 | 75.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 3.15 | 10.38 | 18.72 | 13.00 | 67.6 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.6 | 2.28 | 8.30 | 13.84 | 1.00 | 55.9 | 59.0 |