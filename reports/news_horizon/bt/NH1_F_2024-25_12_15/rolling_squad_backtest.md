# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 234.09
- Total actual points: 292.00
- Average predicted points: 58.52
- Average actual points: 73.00
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
- Predicted score: 62.52
- Actual score: 59.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 4.9 | 3.30 | 9.28 | 15.14 | 6.00 | 89.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.22 | 0.89 | 1.39 | 0.00 | 8.3 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.64 | 12.68 | 20.26 | 1.00 | 90.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.3 | 4.26 | 12.04 | 19.70 | 0.00 | 87.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.80 | 10.32 | 16.77 | 0.00 | 87.6 | 90.0 |
| Bench 2 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.44 | 7.76 | 12.53 | 1.00 | 81.2 | 90.0 |
| Bench 3 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 2.21 | 7.05 | 11.62 | 0.00 | 83.1 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 5.38 | 14.86 | 23.42 | 2.00 | 84.9 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.8 | 4.17 | 12.47 | 20.80 | 16.00 | 83.3 | 90.0 |
| Bench 4 | Bench | Ethan Wheatley | FWD | 14 | 4.5 | 0.55 | 1.64 | 2.81 | 0.00 | 10.6 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 7.95 | 22.29 | 36.33 | 13.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.50 | 18.84 | 31.21 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 6.01 | 16.49 | 26.34 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 3.93 | 14.02 | 23.36 | 3.00 | 79.2 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 4.64 | 12.47 | 20.21 | 1.00 | 84.5 | 58.0 |

## GW13

- Train rows: 141592
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 67.36
- Actual score: 81.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.17) beats the best remaining Triple Captain opportunity (8.94).
- Transfer: Emile Smith Rowe -> Alex Iwobi (projected gain 1.72, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.17) beats the best remaining Triple Captain opportunity (8.94).
- Autosub: Taylor Harwood-Bellis replaced Joško Gvardiol.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 4.9 | 2.93 | 8.91 | 14.79 | 0.00 | 88.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.56 | 1.05 | 1.61 | 0.00 | 7.6 | 0.0 |
| XI | Bench | Joško Gvardiol | DEF | 13 | 6.3 | 3.63 | 11.41 | 19.06 | 0.00 | 87.3 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.78 | 11.25 | 18.00 | 6.00 | 85.6 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.07 | 9.18 | 14.97 | 2.00 | 80.3 | 90.0 |
| Bench 2 | Autosub In | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.58 | 7.95 | 12.85 | 1.00 | 83.6 | 90.0 |
| Bench 4 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.42 | 2.75 | 5.85 | 0.00 | 27.1 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 6.01 | 17.57 | 27.29 | 2.00 | 90.0 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 4.01 | 12.87 | 20.63 | 1.00 | 61.4 | 21.0 |
| Bench 3 | Bench | Ethan Wheatley | FWD | 14 | 4.5 | 0.59 | 1.57 | 2.70 | 0.00 | 10.7 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 8.17 | 24.30 | 38.52 | 13.00 | 90.0 | 83.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.58 | 18.62 | 30.09 | 14.00 | 90.0 | 85.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.46 | 14.88 | 24.75 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.80 | 13.03 | 21.06 | 9.00 | 72.1 | 65.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.6 | 3.59 | 10.85 | 17.61 | 5.00 | 84.7 | 85.0 |

## GW14

- Train rows: 142282
- Bank: 0.20 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 59.78
- Actual score: 83.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (1.93) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Alexander Isak -> Nicolas Jackson (projected gain 8.74, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (1.93) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 4.9 | 3.04 | 8.72 | 14.47 | 6.00 | 86.3 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.21 | 0.77 | 1.34 | 0.00 | 8.1 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.24 | 12.68 | 20.51 | 1.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.32 | 9.37 | 15.21 | 6.00 | 82.7 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 2.66 | 8.38 | 14.51 | 6.00 | 52.9 | 90.0 |
| Bench 2 | Bench Boost | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 1.49 | 5.50 | 9.76 | 0.00 | 61.2 | 0.0 |
| Bench 4 | Bench Boost | Jan Bednarek | DEF | 17 | 4.0 | 0.10 | 1.54 | 3.64 | 0.00 | 17.3 | 0.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 8.1 | 5.67 | 16.27 | 25.14 | 0.00 | 87.1 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.22 | 13.73 | 21.27 | 2.00 | 75.6 | 90.0 |
| Bench 3 | Bench Boost | Ethan Wheatley | FWD | 14 | 4.5 | 0.13 | 1.23 | 2.35 | 0.00 | 9.9 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 7.93 | 24.33 | 39.03 | 18.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 7.45 | 20.91 | 33.46 | 7.00 | 90.0 | 78.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.66 | 12.99 | 22.34 | 2.00 | 73.8 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.8 | 3.93 | 11.37 | 20.18 | 2.00 | 78.0 | 90.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.6 | 3.81 | 10.99 | 17.91 | 15.00 | 82.1 | 90.0 |

## GW15

- Train rows: 142975
- Bank: 0.60 -> 0.00
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Matheus Santos Carneiro Da Cunha
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 44.43
- Actual score: 69.00
- Transfer: Jordan Pickford -> David Raya Martin (projected gain 11.05, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.73 | 10.85 | 17.46 | 2.00 | 89.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.42 | 0.86 | 1.40 | 0.00 | 7.0 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.03 | 11.47 | 19.24 | 1.00 | 81.4 | 90.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 12 | 6.3 | 0.00 | 9.77 | 16.52 | 0.00 | 0.0 | 0.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 2.87 | 9.14 | 14.94 | 1.00 | 82.9 | 90.0 |
| XI | XI | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 1.19 | 4.03 | 7.32 | 2.00 | 49.0 | 90.0 |
| Bench 2 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.02 | 1.46 | 3.43 | 0.00 | 15.3 | 0.0 |
| Vice Captain | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.69 | 13.34 | 21.45 | 1.00 | 83.2 | 90.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 8.1 | 2.75 | 9.00 | 14.66 | 2.00 | 32.4 | 75.0 |
| XI | Bench | Ethan Wheatley | FWD | 14 | 4.5 | 0.36 | 1.31 | 2.37 | 0.00 | 8.9 | 0.0 |
| Bench 4 | Bench | Mohamed Salah | MID | 12 | 13.1 | 0.00 | 23.27 | 38.75 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 10.9 | 6.63 | 19.40 | 31.44 | 18.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.54 | 14.24 | 23.90 | 9.00 | 87.6 | 75.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.6 | 3.34 | 11.09 | 18.18 | 2.00 | 84.1 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 3.67 | 10.95 | 19.39 | 13.00 | 78.0 | 90.0 |