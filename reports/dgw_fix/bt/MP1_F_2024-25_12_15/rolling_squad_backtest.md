# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 232.44
- Total actual points: 283.00
- Average predicted points: 58.11
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
- Predicted score: 63.05
- Actual score: 55.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Sánchez | GK | 6 | 4.7 | 3.28 | 9.07 | 14.86 | 1.00 | 88.3 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.05 | 0.41 | 0.60 | 0.00 | 4.3 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.62 | 12.66 | 20.25 | 1.00 | 90.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.3 | 4.27 | 12.14 | 19.92 | 0.00 | 87.3 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 3.57 | 10.08 | 16.11 | 1.00 | 88.6 | 90.0 |
| Bench 2 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.49 | 7.91 | 12.80 | 1.00 | 82.3 | 90.0 |
| Bench 3 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 2.23 | 7.12 | 11.77 | 0.00 | 83.5 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 5.40 | 14.88 | 23.43 | 2.00 | 85.4 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.8 | 4.14 | 12.41 | 20.74 | 16.00 | 82.5 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 5.0 | 1.88 | 6.58 | 10.50 | 1.00 | 60.1 | 13.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 7.89 | 22.21 | 36.23 | 13.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.95 | 19.51 | 31.98 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 6.04 | 16.55 | 26.43 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 4.34 | 14.58 | 23.92 | 3.00 | 88.4 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 4.67 | 12.57 | 20.37 | 1.00 | 85.2 | 58.0 |

## GW13

- Train rows: 141592
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 65.62
- Actual score: 85.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.13) beats the best remaining Triple Captain opportunity (8.92).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.13) beats the best remaining Triple Captain opportunity (8.92).
- Autosub: Taylor Harwood-Bellis replaced Joško Gvardiol.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Sánchez | GK | 6 | 4.7 | 2.79 | 8.03 | 13.04 | 7.00 | 80.7 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.35 | 0.49 | 0.68 | 0.00 | 2.9 | 0.0 |
| XI | Bench | Joško Gvardiol | DEF | 13 | 6.3 | 3.57 | 11.35 | 19.03 | 0.00 | 86.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.74 | 11.22 | 18.02 | 6.00 | 84.7 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 2.68 | 8.45 | 13.61 | 2.00 | 72.7 | 90.0 |
| Bench 2 | Autosub In | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.61 | 8.05 | 13.06 | 1.00 | 84.3 | 90.0 |
| Bench 4 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 1.17 | 4.10 | 7.27 | 0.00 | 43.9 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 6.09 | 17.71 | 27.44 | 2.00 | 90.0 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 3.93 | 12.70 | 20.40 | 1.00 | 59.5 | 21.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 5.0 | 1.56 | 5.25 | 8.91 | 2.00 | 39.2 | 87.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 8.13 | 24.26 | 38.49 | 13.00 | 90.0 | 83.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.56 | 18.64 | 30.18 | 14.00 | 90.0 | 85.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.35 | 14.72 | 24.60 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.67 | 12.79 | 20.78 | 9.00 | 69.1 | 65.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 2.86 | 9.07 | 15.25 | 2.00 | 57.6 | 85.0 |

## GW14

- Train rows: 142282
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 59.79
- Actual score: 67.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.24) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Joško Gvardiol -> Pedro Porro (projected gain 3.93, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.24) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Sánchez | GK | 6 | 4.7 | 3.49 | 9.46 | 15.06 | 0.00 | 88.0 | 0.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.00 | 0.20 | 0.39 | 0.00 | 3.4 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.22 | 12.68 | 20.52 | 1.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.03 | 11.75 | 18.85 | 1.00 | 87.4 | 28.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 2.48 | 8.09 | 13.35 | 1.00 | 77.0 | 90.0 |
| Bench 2 | Bench Boost | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.39 | 7.20 | 11.89 | 0.00 | 81.0 | 0.0 |
| Bench 4 | Bench Boost | Jan Bednarek | DEF | 17 | 4.0 | 0.77 | 2.75 | 5.07 | 0.00 | 31.8 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.19 | 13.70 | 21.26 | 2.00 | 75.0 | 90.0 |
| Bench 3 | Bench Boost | Alexander Isak | FWD | 15 | 8.5 | 2.09 | 8.26 | 14.87 | 11.00 | 31.3 | 90.0 |
| XI | XI | Cameron Archer | FWD | 17 | 5.0 | 2.46 | 6.90 | 11.14 | 2.00 | 62.4 | 71.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 7.90 | 24.30 | 39.01 | 18.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 7.46 | 20.97 | 33.57 | 7.00 | 90.0 | 78.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.51 | 12.73 | 22.05 | 2.00 | 70.3 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.8 | 3.74 | 11.09 | 19.90 | 2.00 | 74.0 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.7 | 3.16 | 9.48 | 16.03 | 2.00 | 66.4 | 70.0 |

## GW15

- Train rows: 142975
- Bank: 0.60 -> 0.00
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Matheus Santos Carneiro Da Cunha
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 43.97
- Actual score: 76.00
- Transfer: Cameron Archer -> Jørgen Strand Larsen (projected gain 3.41, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Sánchez | GK | 6 | 4.7 | 1.30 | 4.65 | 8.27 | 0.00 | 40.6 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.20 | 0.26 | 0.42 | 0.00 | 1.9 | 0.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 12 | 6.3 | 0.00 | 9.88 | 16.74 | 0.00 | 0.0 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 3.00 | 9.34 | 15.99 | 3.00 | 69.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 2.63 | 7.62 | 12.49 | 1.00 | 77.2 | 82.0 |
| XI | XI | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 0.99 | 3.70 | 6.91 | 2.00 | 44.7 | 90.0 |
| Bench 2 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.20 | 1.47 | 3.16 | 0.00 | 19.3 | 0.0 |
| Vice Captain | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.61 | 13.21 | 21.32 | 1.00 | 81.4 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 4.32 | 13.16 | 22.00 | 8.00 | 72.8 | 90.0 |
| XI | XI | Jørgen Strand Larsen | FWD | 20 | 5.6 | 3.52 | 9.98 | 16.11 | 2.00 | 75.6 | 61.0 |
| Bench 4 | Bench | Mohamed Salah | MID | 12 | 13.1 | 0.00 | 23.33 | 38.89 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 10.9 | 6.70 | 19.64 | 31.84 | 18.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.38 | 13.94 | 23.54 | 9.00 | 84.1 | 75.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 3.37 | 10.38 | 18.72 | 13.00 | 71.2 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.6 | 2.43 | 8.30 | 13.84 | 1.00 | 57.3 | 59.0 |