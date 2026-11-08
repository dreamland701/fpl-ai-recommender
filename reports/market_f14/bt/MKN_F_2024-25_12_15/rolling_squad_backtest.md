# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 235.63
- Total actual points: 295.00
- Average predicted points: 58.91
- Average actual points: 73.75
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
- Predicted score: 66.41
- Actual score: 44.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.51 | 11.39 | 18.03 | 6.00 | 98.6 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.13 | 0.47 | 0.68 | 0.00 | 5.6 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 5.19 | 13.34 | 21.29 | 1.00 | 109.9 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.3 | 4.83 | 13.05 | 21.32 | 0.00 | 99.2 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 4.35 | 11.06 | 17.82 | 0.00 | 95.2 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 4.07 | 10.56 | 16.81 | 1.00 | 97.1 | 90.0 |
| Bench 3 | Bench | Cameron Burgess | DEF | 10 | 3.9 | 1.88 | 4.99 | 7.75 | 2.00 | 66.7 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 5.82 | 14.85 | 23.33 | 2.00 | 92.1 | 90.0 |
| Bench 2 | Bench | Danny Welbeck | FWD | 5 | 6.0 | 3.60 | 11.68 | 18.69 | 2.00 | 77.8 | 85.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.5 | 0.21 | 1.04 | 2.17 | 0.00 | 12.7 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 8.12 | 21.85 | 35.64 | 13.00 | 114.5 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.89 | 19.27 | 31.56 | 2.00 | 104.1 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 5.84 | 15.97 | 25.69 | 2.00 | 98.3 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 3.95 | 14.33 | 23.62 | 3.00 | 84.7 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 4.71 | 12.50 | 20.31 | 1.00 | 85.7 | 58.0 |

## GW13

- Train rows: 141592
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 60.52
- Actual score: 73.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (4.91) beats the best remaining Bench Boost opportunity (5.65).
- Transfer: Emile Smith Rowe -> Alex Iwobi (projected gain 1.52, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (4.91) beats the best remaining Bench Boost opportunity (5.65).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.42 | 11.50 | 18.33 | 2.00 | 98.4 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.14 | 0.23 | 0.35 | 0.00 | 0.0 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.3 | 3.47 | 11.72 | 19.73 | 0.00 | 83.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.56 | 11.15 | 18.03 | 6.00 | 85.0 | 90.0 |
| Bench 2 | Bench Boost | Antonee Robinson | DEF | 9 | 4.7 | 2.71 | 9.02 | 15.03 | 2.00 | 78.2 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 2.84 | 8.70 | 13.97 | 2.00 | 73.1 | 90.0 |
| Bench 3 | Bench Boost | Cameron Burgess | DEF | 10 | 3.9 | 1.77 | 5.56 | 8.60 | 2.00 | 66.7 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 3.83 | 12.77 | 20.59 | 1.00 | 56.6 | 21.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 6.0 | 4.26 | 10.91 | 17.61 | 2.00 | 81.6 | 78.0 |
| Bench 4 | Bench Boost | Ross Stewart | FWD | 17 | 4.5 | 0.30 | 0.94 | 1.89 | 0.00 | 10.9 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 7.19 | 23.18 | 37.18 | 13.00 | 95.5 | 83.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.06 | 17.97 | 29.29 | 14.00 | 91.6 | 85.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.15 | 14.48 | 24.25 | 2.00 | 92.8 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.48 | 13.29 | 21.17 | 9.00 | 75.9 | 65.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.6 | 3.17 | 10.49 | 17.34 | 5.00 | 80.9 | 85.0 |

## GW14

- Train rows: 142282
- Bank: 0.20 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.40
- Actual score: 82.00
- Transfer: Alexander Isak -> Nicolas Jackson (projected gain 8.35, hit 0)
- Autosub: Lewis Hall replaced Nicolas Jackson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.05 | 10.64 | 17.14 | 6.00 | 94.3 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.06 | 0.26 | 0.48 | 0.00 | 3.9 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.25 | 12.73 | 20.67 | 1.00 | 96.5 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 3.31 | 9.20 | 15.61 | 6.00 | 53.5 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.03 | 9.15 | 15.06 | 6.00 | 80.6 | 90.0 |
| Bench 2 | Autosub In | Lewis Hall | DEF | 15 | 4.4 | 2.35 | 8.12 | 13.58 | 1.00 | 75.2 | 90.0 |
| Bench 3 | Bench | Cameron Burgess | DEF | 10 | 3.9 | 2.34 | 6.22 | 9.64 | 0.00 | 71.6 | 0.0 |
| XI | Bench | Nicolas Jackson | FWD | 6 | 8.1 | 6.18 | 16.44 | 25.37 | 0.00 | 98.8 | 0.0 |
| XI | Bench | Danny Welbeck | FWD | 5 | 5.9 | 2.96 | 9.51 | 15.86 | 0.00 | 67.7 | 0.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.33 | 0.87 | 1.56 | 0.00 | 9.9 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 7.76 | 23.95 | 38.56 | 18.00 | 109.9 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 7.58 | 20.68 | 33.08 | 7.00 | 112.7 | 78.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 2.59 | 12.12 | 21.54 | 2.00 | 60.2 | 90.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.6 | 3.47 | 10.64 | 17.57 | 15.00 | 77.9 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.8 | 2.47 | 10.25 | 19.03 | 2.00 | 59.3 | 90.0 |

## GW15

- Train rows: 142975
- Bank: 0.60 -> 0.20
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 53.31
- Actual score: 96.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.64) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Nicolas Jackson -> Alexander Isak (projected gain 5.52, hit 0)
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (5.64) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Cameron Burgess replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.97 | 11.23 | 18.02 | 2.00 | 92.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.13 | 0.17 | 0.31 | 0.00 | 0.0 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.33 | 11.78 | 19.65 | 1.00 | 82.3 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 2.35 | 8.72 | 14.54 | 1.00 | 75.5 | 90.0 |
| Bench 2 | Bench | Virgil van Dijk | DEF | 12 | 6.3 | 1.34 | 8.13 | 14.50 | 0.00 | 42.0 | 0.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 2.84 | 7.96 | 13.07 | 1.00 | 81.0 | 82.0 |
| Bench 3 | Autosub In | Cameron Burgess | DEF | 10 | 3.9 | 1.01 | 3.10 | 5.54 | 4.00 | 38.6 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 4.15 | 12.89 | 21.76 | 8.00 | 71.4 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.9 | 2.05 | 5.87 | 10.72 | 1.00 | 34.6 | 20.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.14 | 0.63 | 1.15 | 0.00 | 8.4 | 0.0 |
| Vice Captain | Bench | Mohamed Salah | MID | 12 | 13.1 | 4.66 | 22.41 | 39.04 | 0.00 | 65.8 | 0.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 10.9 | 6.27 | 18.77 | 30.76 | 18.00 | 92.4 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.47 | 14.03 | 23.53 | 9.00 | 81.7 | 75.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.6 | 2.85 | 10.71 | 17.85 | 2.00 | 77.1 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 2.85 | 10.02 | 18.33 | 13.00 | 66.3 | 90.0 |