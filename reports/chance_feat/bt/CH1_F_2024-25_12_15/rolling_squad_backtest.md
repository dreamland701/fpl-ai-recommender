# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 234.13
- Total actual points: 292.00
- Average predicted points: 58.53
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
- Predicted score: 62.53
- Actual score: 59.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 4.9 | 3.28 | 9.25 | 15.15 | 6.00 | 88.4 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.23 | 0.90 | 1.38 | 0.00 | 8.5 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.63 | 12.67 | 20.26 | 1.00 | 90.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.3 | 4.24 | 12.02 | 19.70 | 0.00 | 86.5 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.79 | 10.32 | 16.76 | 0.00 | 87.4 | 90.0 |
| Bench 2 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.43 | 7.75 | 12.54 | 1.00 | 81.0 | 90.0 |
| Bench 3 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 2.20 | 7.03 | 11.62 | 0.00 | 82.8 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 5.40 | 14.87 | 23.39 | 2.00 | 85.3 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.8 | 4.17 | 12.47 | 20.80 | 16.00 | 83.3 | 90.0 |
| Bench 4 | Bench | Ethan Wheatley | FWD | 14 | 4.5 | 0.57 | 1.66 | 2.79 | 0.00 | 11.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 7.95 | 22.28 | 36.32 | 13.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.51 | 19.11 | 31.75 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 6.01 | 16.49 | 26.32 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 3.96 | 14.29 | 23.84 | 3.00 | 80.2 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 4.64 | 12.47 | 20.20 | 1.00 | 84.5 | 58.0 |

## GW13

- Train rows: 141592
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 67.19
- Actual score: 81.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.17) beats the best remaining Triple Captain opportunity (8.92).
- Transfer: Emile Smith Rowe -> Alex Iwobi (projected gain 1.75, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.17) beats the best remaining Triple Captain opportunity (8.92).
- Autosub: Taylor Harwood-Bellis replaced Joško Gvardiol.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 4.9 | 2.90 | 8.89 | 14.79 | 0.00 | 87.5 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.58 | 1.07 | 1.59 | 0.00 | 8.1 | 0.0 |
| XI | Bench | Joško Gvardiol | DEF | 13 | 6.3 | 3.60 | 11.39 | 19.07 | 0.00 | 86.7 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.76 | 11.23 | 18.00 | 6.00 | 85.1 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.05 | 9.16 | 14.97 | 2.00 | 79.9 | 90.0 |
| Bench 2 | Autosub In | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.57 | 7.93 | 12.86 | 1.00 | 83.3 | 90.0 |
| Bench 3 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.78 | 2.99 | 5.45 | 0.00 | 34.9 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 6.03 | 17.60 | 27.28 | 2.00 | 90.0 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 4.00 | 12.86 | 20.62 | 1.00 | 61.2 | 21.0 |
| Bench 4 | Bench | Ethan Wheatley | FWD | 14 | 4.5 | 0.61 | 1.59 | 2.69 | 0.00 | 11.1 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 8.17 | 24.29 | 38.53 | 13.00 | 90.0 | 83.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.56 | 18.61 | 30.11 | 14.00 | 90.0 | 85.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.42 | 14.85 | 24.78 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.78 | 13.00 | 21.05 | 9.00 | 71.6 | 65.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.6 | 3.58 | 10.84 | 17.60 | 5.00 | 84.5 | 85.0 |

## GW14

- Train rows: 142282
- Bank: 0.20 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 60.26
- Actual score: 83.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (2.62) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Alexander Isak -> Nicolas Jackson (projected gain 8.48, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (2.62) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 4.9 | 3.02 | 8.70 | 14.49 | 6.00 | 85.7 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.23 | 0.79 | 1.32 | 0.00 | 8.6 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.23 | 12.67 | 20.50 | 1.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.30 | 9.35 | 15.22 | 6.00 | 82.3 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 2.59 | 8.33 | 14.57 | 6.00 | 51.5 | 90.0 |
| Bench 2 | Bench Boost | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 1.83 | 5.74 | 9.54 | 0.00 | 68.4 | 0.0 |
| Bench 3 | Bench Boost | Jan Bednarek | DEF | 17 | 4.0 | 0.42 | 1.77 | 3.46 | 0.00 | 24.0 | 0.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 8.1 | 5.68 | 16.28 | 25.14 | 0.00 | 87.3 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.21 | 13.72 | 21.26 | 2.00 | 75.4 | 90.0 |
| Bench 4 | Bench Boost | Ethan Wheatley | FWD | 14 | 4.5 | 0.14 | 1.24 | 2.34 | 0.00 | 10.3 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 7.93 | 24.32 | 39.02 | 18.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 7.45 | 20.90 | 33.46 | 7.00 | 90.0 | 78.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.63 | 12.97 | 22.37 | 2.00 | 73.1 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.8 | 3.88 | 11.32 | 20.20 | 2.00 | 76.9 | 90.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.6 | 3.80 | 10.98 | 17.91 | 15.00 | 81.8 | 90.0 |

## GW15

- Train rows: 142975
- Bank: 0.60 -> 0.00
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Matheus Santos Carneiro Da Cunha
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 44.16
- Actual score: 69.00
- Transfer: Jordan Pickford -> David Raya Martin (projected gain 11.01, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.71 | 10.83 | 17.46 | 2.00 | 88.6 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.44 | 0.88 | 1.39 | 0.00 | 7.4 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.01 | 11.45 | 19.26 | 1.00 | 81.0 | 90.0 |
| Bench 2 | Bench | Virgil van Dijk | DEF | 12 | 6.3 | 0.00 | 9.75 | 16.51 | 0.00 | 0.0 | 0.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 2.86 | 9.12 | 14.95 | 1.00 | 82.5 | 90.0 |
| XI | XI | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 1.15 | 4.00 | 7.35 | 2.00 | 48.1 | 90.0 |
| Bench 3 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.00 | 1.37 | 3.24 | 0.00 | 14.9 | 0.0 |
| Vice Captain | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.67 | 13.31 | 21.46 | 1.00 | 82.6 | 90.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 8.1 | 2.72 | 8.96 | 14.66 | 2.00 | 31.7 | 75.0 |
| XI | Bench | Ethan Wheatley | FWD | 14 | 4.5 | 0.38 | 1.33 | 2.35 | 0.00 | 9.4 | 0.0 |
| Bench 4 | Bench | Mohamed Salah | MID | 12 | 13.1 | 0.00 | 23.25 | 38.73 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 10.9 | 6.62 | 19.38 | 31.42 | 18.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.51 | 14.22 | 23.94 | 9.00 | 86.9 | 75.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.6 | 3.34 | 11.07 | 18.17 | 2.00 | 83.9 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 3.59 | 10.89 | 19.47 | 13.00 | 76.0 | 90.0 |