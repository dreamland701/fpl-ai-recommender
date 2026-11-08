# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 238.54
- Total actual points: 287.00
- Average predicted points: 59.64
- Average actual points: 71.75
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
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 60.82
- Actual score: 50.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.50 | 10.15 | 16.67 | 6.00 | 89.1 | 90.0 |
| Bench 1 | Bench | Robert Sánchez | GK | 6 | 4.7 | 3.28 | 9.07 | 14.92 | 1.00 | 88.3 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.3 | 4.27 | 12.29 | 20.14 | 0.00 | 87.3 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 3.87 | 11.15 | 18.07 | 6.00 | 88.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.83 | 10.32 | 16.91 | 0.00 | 88.4 | 90.0 |
| XI | XI | Noussair Mazraoui | DEF | 14 | 4.6 | 3.77 | 10.12 | 15.94 | 2.00 | 86.7 | 90.0 |
| Bench 3 | Bench | Rayan Aït-Nouri | DEF | 20 | 4.8 | 3.38 | 9.98 | 16.35 | 2.00 | 88.7 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 6.0 | 3.80 | 11.49 | 18.39 | 2.00 | 78.9 | 85.0 |
| Bench 2 | Bench | Raúl Jiménez | FWD | 9 | 5.8 | 3.70 | 9.66 | 16.52 | 2.00 | 65.0 | 70.0 |
| Bench 4 | Bench | Michail Antonio | FWD | 19 | 5.4 | 2.27 | 7.47 | 12.22 | 2.00 | 56.6 | 74.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 7.89 | 22.15 | 28.86 | 13.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.95 | 19.33 | 31.97 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 6.04 | 15.89 | 25.33 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 4.34 | 14.69 | 24.25 | 3.00 | 88.4 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 4.67 | 12.31 | 20.08 | 1.00 | 85.2 | 58.0 |

## GW13

- Train rows: 141592
- Bank: 0.10 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 65.10
- Actual score: 85.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.13) beats the best remaining Triple Captain opportunity (8.92).
- Transfer: Emile Smith Rowe -> Alex Iwobi (projected gain 1.89, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.13) beats the best remaining Triple Captain opportunity (8.92).
- Autosub: Noussair Mazraoui replaced Joško Gvardiol.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.85 | 10.77 | 17.57 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Robert Sánchez | GK | 6 | 4.7 | 2.79 | 8.00 | 13.08 | 7.00 | 80.7 | 90.0 |
| XI | Bench | Joško Gvardiol | DEF | 13 | 6.3 | 3.57 | 11.54 | 19.10 | 0.00 | 86.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 3.92 | 11.00 | 17.61 | 9.00 | 86.3 | 45.0 |
| XI | XI | Rayan Aït-Nouri | DEF | 20 | 4.8 | 3.48 | 9.91 | 15.83 | 0.00 | 86.3 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.05 | 9.14 | 14.92 | 2.00 | 79.9 | 90.0 |
| Bench 2 | Autosub In | Noussair Mazraoui | DEF | 14 | 4.6 | 2.93 | 8.62 | 13.77 | 1.00 | 75.4 | 55.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 6.0 | 3.74 | 10.19 | 16.52 | 2.00 | 71.5 | 78.0 |
| Bench 3 | Bench | Raúl Jiménez | FWD | 9 | 5.7 | 2.38 | 7.68 | 12.95 | 2.00 | 51.9 | 77.0 |
| Bench 4 | Bench | Michail Antonio | FWD | 19 | 5.4 | 2.33 | 6.84 | 11.80 | 2.00 | 58.4 | 64.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.56 | 18.21 | 29.84 | 14.00 | 90.0 | 85.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 8.13 | 15.99 | 30.79 | 13.00 | 90.0 | 83.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.35 | 14.80 | 24.72 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.67 | 12.25 | 19.77 | 9.00 | 69.1 | 65.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.6 | 3.53 | 10.51 | 17.01 | 5.00 | 83.4 | 85.0 |

## GW14

- Train rows: 142282
- Bank: 0.30 -> 0.90
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 66.55
- Actual score: 78.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.45) beats the best remaining Bench Boost opportunity (8.32).
- Transfer: Joško Gvardiol -> Pedro Porro (projected gain 3.69, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.45) beats the best remaining Bench Boost opportunity (8.32).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.59 | 10.17 | 16.61 | 6.00 | 85.9 | 90.0 |
| Bench 1 | Bench Boost | Robert Sánchez | GK | 6 | 4.7 | 3.49 | 9.35 | 15.06 | 0.00 | 88.0 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.03 | 11.68 | 18.75 | 1.00 | 87.4 | 28.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 3.62 | 10.60 | 17.11 | 0.00 | 73.7 | 0.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.29 | 9.34 | 15.22 | 6.00 | 82.1 | 90.0 |
| XI | XI | Rayan Aït-Nouri | DEF | 20 | 4.8 | 3.23 | 9.30 | 15.17 | 0.00 | 83.6 | 90.0 |
| Bench 4 | Bench Boost | Noussair Mazraoui | DEF | 14 | 4.6 | 2.12 | 7.13 | 12.06 | 1.00 | 63.3 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.9 | 3.09 | 9.39 | 15.56 | 0.00 | 68.3 | 0.0 |
| Bench 2 | Bench Boost | Raúl Jiménez | FWD | 9 | 5.6 | 2.94 | 8.02 | 13.28 | 1.00 | 57.8 | 10.0 |
| Bench 3 | Bench Boost | Michail Antonio | FWD | 19 | 5.4 | 2.90 | 7.37 | 12.45 | 1.00 | 57.1 | 28.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 7.46 | 20.72 | 33.72 | 7.00 | 90.0 | 78.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 7.90 | 16.10 | 31.18 | 18.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.51 | 12.57 | 21.89 | 2.00 | 70.3 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.8 | 3.74 | 11.63 | 20.45 | 2.00 | 74.0 | 90.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.6 | 3.75 | 10.74 | 17.39 | 15.00 | 80.8 | 90.0 |

## GW15

- Train rows: 142975
- Bank: 0.90 -> 0.50
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Bruno Borges Fernandes
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 46.07
- Actual score: 74.00
- Transfer: Raúl Jiménez -> João Pedro Junqueira de Jesus (projected gain 4.73, hit 0)
- Autosub: Danny Welbeck replaced Gabriel dos Santos Magalhães.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.73 | 11.04 | 17.98 | 2.00 | 89.0 | 90.0 |
| Bench 1 | Bench | Robert Sánchez | GK | 6 | 4.7 | 1.30 | 4.77 | 8.47 | 0.00 | 40.6 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 3.00 | 9.53 | 16.22 | 3.00 | 69.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 2.85 | 9.16 | 14.98 | 1.00 | 82.3 | 90.0 |
| XI | XI | Rayan Aït-Nouri | DEF | 20 | 4.8 | 2.94 | 8.08 | 13.26 | 4.00 | 77.8 | 85.0 |
| XI | XI | Noussair Mazraoui | DEF | 14 | 4.6 | 2.76 | 7.99 | 12.72 | 1.00 | 73.0 | 24.0 |
| XI | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 2.19 | 7.50 | 13.01 | 0.00 | 40.4 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.9 | 4.18 | 10.64 | 16.69 | 2.00 | 60.4 | 70.0 |
| Bench 2 | Bench | Michail Antonio | FWD | 19 | 5.4 | 2.14 | 6.13 | 10.27 | 0.00 | 45.8 | 0.0 |
| Bench 3 | Autosub In | Danny Welbeck | FWD | 5 | 5.9 | 1.97 | 5.75 | 10.57 | 1.00 | 32.8 | 20.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 10.9 | 6.70 | 19.47 | 31.70 | 18.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Mohamed Salah | MID | 12 | 13.1 | 0.00 | 16.80 | 33.52 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.38 | 13.90 | 23.33 | 9.00 | 84.1 | 75.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.6 | 3.28 | 10.72 | 17.80 | 2.00 | 82.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 3.37 | 10.18 | 18.13 | 13.00 | 71.2 | 90.0 |