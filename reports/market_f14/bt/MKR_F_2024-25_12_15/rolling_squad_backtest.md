# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 232.00
- Total actual points: 296.00
- Average predicted points: 58.00
- Average actual points: 74.00
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
- Predicted score: 62.71
- Actual score: 45.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.21 | 11.33 | 17.89 | 6.00 | 86.6 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.08 | 0.48 | 0.69 | 0.00 | 4.4 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.56 | 13.38 | 21.38 | 1.00 | 90.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.3 | 4.27 | 13.07 | 21.35 | 0.00 | 85.7 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 4.07 | 11.04 | 17.76 | 0.00 | 87.2 | 90.0 |
| Bench 2 | Bench | Lewis Hall | DEF | 15 | 4.4 | 3.61 | 10.57 | 16.83 | 1.00 | 87.8 | 90.0 |
| Bench 3 | Bench | Cameron Burgess | DEF | 10 | 3.9 | 1.83 | 5.03 | 7.84 | 2.00 | 68.1 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 5.31 | 14.87 | 23.36 | 2.00 | 85.0 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 6.0 | 3.67 | 11.68 | 18.69 | 2.00 | 80.0 | 85.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.5 | 0.24 | 1.00 | 2.10 | 0.00 | 10.5 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 7.56 | 21.90 | 35.74 | 13.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.69 | 19.33 | 31.69 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 5.84 | 15.99 | 25.72 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 4.26 | 14.34 | 23.62 | 3.00 | 89.7 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 4.70 | 12.48 | 20.27 | 1.00 | 85.6 | 58.0 |

## GW13

- Train rows: 141592
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 61.39
- Actual score: 73.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.05) beats the best remaining Bench Boost opportunity (5.71).
- Transfer: Emile Smith Rowe -> Alex Iwobi (projected gain 1.50, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.05) beats the best remaining Bench Boost opportunity (5.71).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.08 | 11.50 | 18.33 | 2.00 | 88.9 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.23 | 0.28 | 0.45 | 0.00 | 4.2 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.3 | 3.79 | 11.65 | 19.59 | 0.00 | 86.2 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.71 | 11.10 | 17.93 | 6.00 | 85.4 | 90.0 |
| Bench 2 | Bench Boost | Antonee Robinson | DEF | 9 | 4.7 | 2.79 | 9.04 | 15.07 | 2.00 | 81.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 2.84 | 8.68 | 13.93 | 2.00 | 72.8 | 90.0 |
| Bench 3 | Bench Boost | Cameron Burgess | DEF | 10 | 3.9 | 1.84 | 5.53 | 8.52 | 2.00 | 67.7 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 4.03 | 12.76 | 20.55 | 1.00 | 60.5 | 21.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 6.0 | 3.60 | 10.96 | 17.70 | 2.00 | 69.8 | 78.0 |
| Bench 4 | Bench Boost | Ross Stewart | FWD | 17 | 4.5 | 0.18 | 0.97 | 1.95 | 0.00 | 8.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 7.83 | 23.14 | 37.10 | 13.00 | 90.0 | 83.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.29 | 17.97 | 29.29 | 14.00 | 90.0 | 85.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.08 | 14.53 | 24.36 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.01 | 13.27 | 21.12 | 9.00 | 67.2 | 65.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.6 | 3.26 | 10.51 | 17.39 | 5.00 | 84.8 | 85.0 |

## GW14

- Train rows: 142282
- Bank: 0.20 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 63.78
- Actual score: 100.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.87) beats the best remaining Triple Captain opportunity (7.72).
- Transfer: Alexander Isak -> Nicolas Jackson (projected gain 8.45, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.87) beats the best remaining Triple Captain opportunity (7.72).
- Autosub: Lewis Hall replaced Nicolas Jackson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.69 | 10.67 | 17.19 | 6.00 | 84.7 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.04 | 0.25 | 0.47 | 0.00 | 3.3 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.30 | 12.69 | 20.57 | 1.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.16 | 9.15 | 15.06 | 6.00 | 83.1 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 2.99 | 9.13 | 15.46 | 6.00 | 44.9 | 90.0 |
| Bench 2 | Autosub In | Lewis Hall | DEF | 15 | 4.4 | 2.57 | 8.07 | 13.46 | 1.00 | 77.8 | 90.0 |
| Bench 3 | Bench | Cameron Burgess | DEF | 10 | 3.9 | 2.32 | 6.20 | 9.61 | 0.00 | 70.6 | 0.0 |
| XI | Bench | Nicolas Jackson | FWD | 6 | 8.1 | 5.50 | 16.48 | 25.47 | 0.00 | 88.8 | 0.0 |
| XI | Bench | Danny Welbeck | FWD | 5 | 5.9 | 3.03 | 9.51 | 15.86 | 0.00 | 68.8 | 0.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.19 | 0.90 | 1.65 | 0.00 | 7.1 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 7.87 | 23.92 | 38.49 | 18.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 7.08 | 20.74 | 33.20 | 7.00 | 90.0 | 78.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.36 | 12.09 | 21.47 | 2.00 | 73.7 | 90.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.6 | 3.64 | 10.64 | 17.56 | 15.00 | 82.2 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.8 | 3.43 | 10.24 | 18.99 | 2.00 | 77.3 | 90.0 |

## GW15

- Train rows: 142975
- Bank: 0.60 -> 0.20
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Bruno Borges Fernandes
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 44.12
- Actual score: 78.00
- Transfer: Nicolas Jackson -> Alexander Isak (projected gain 5.42, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.87 | 11.22 | 18.00 | 2.00 | 88.7 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.11 | 0.21 | 0.39 | 0.00 | 2.3 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.20 | 11.75 | 19.59 | 1.00 | 79.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 2.84 | 8.67 | 14.44 | 1.00 | 83.9 | 90.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 12 | 6.3 | 0.00 | 8.13 | 14.51 | 0.00 | 0.0 | 0.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 2.66 | 7.95 | 13.05 | 1.00 | 76.7 | 82.0 |
| XI | XI | Cameron Burgess | DEF | 10 | 3.9 | 0.96 | 3.11 | 5.55 | 4.00 | 37.9 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 4.19 | 12.89 | 21.76 | 8.00 | 73.9 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.9 | 1.88 | 5.91 | 10.81 | 1.00 | 32.2 | 20.0 |
| Bench 2 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.06 | 0.61 | 1.11 | 0.00 | 3.8 | 0.0 |
| Bench 4 | Bench | Mohamed Salah | MID | 12 | 13.1 | 0.00 | 22.43 | 39.08 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 10.9 | 6.19 | 18.80 | 30.82 | 18.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.62 | 13.97 | 23.42 | 9.00 | 84.0 | 75.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.6 | 3.32 | 10.67 | 17.75 | 2.00 | 84.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 3.19 | 10.00 | 18.29 | 13.00 | 72.3 | 90.0 |