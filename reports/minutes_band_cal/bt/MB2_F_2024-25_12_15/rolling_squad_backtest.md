# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 229.06
- Total actual points: 269.00
- Average predicted points: 57.27
- Average actual points: 67.25
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
- Predicted score: 59.80
- Actual score: 58.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 5.1 | 3.24 | 8.97 | 14.70 | 3.00 | 83.3 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.23 | 0.87 | 1.33 | 0.00 | 8.6 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.21 | 11.31 | 18.21 | 1.00 | 83.2 | 90.0 |
| XI | XI | Ibrahima Konaté | DEF | 12 | 5.4 | 3.86 | 10.39 | 16.52 | 0.00 | 83.3 | 90.0 |
| XI | XI | Noussair Mazraoui | DEF | 14 | 4.6 | 3.61 | 10.04 | 15.65 | 2.00 | 82.5 | 90.0 |
| Bench 2 | Bench | Lewis Hall | DEF | 15 | 4.4 | 3.14 | 8.68 | 14.00 | 1.00 | 81.6 | 90.0 |
| Bench 4 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 2.12 | 6.88 | 11.35 | 0.00 | 80.3 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 5.32 | 14.69 | 23.09 | 2.00 | 82.8 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.8 | 4.09 | 12.33 | 20.56 | 16.00 | 80.9 | 90.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 5.0 | 2.12 | 7.21 | 11.45 | 1.00 | 66.3 | 13.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 7.53 | 20.95 | 34.34 | 13.00 | 83.2 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.40 | 18.23 | 29.99 | 2.00 | 89.4 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 5.59 | 15.12 | 24.27 | 2.00 | 83.2 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 3.86 | 13.46 | 22.19 | 3.00 | 77.8 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 4.55 | 12.31 | 19.92 | 1.00 | 82.0 | 58.0 |

## GW13

- Train rows: 141592
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 64.00
- Actual score: 82.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.75) beats the best remaining Triple Captain opportunity (8.45).
- Transfer: Ibrahima Konaté -> Rayan Aït-Nouri (projected gain 1.51, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.75) beats the best remaining Triple Captain opportunity (8.45).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 5.1 | 2.87 | 8.64 | 14.20 | 6.00 | 82.3 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.57 | 1.04 | 1.55 | 0.00 | 8.1 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.68 | 11.08 | 17.78 | 6.00 | 82.7 | 90.0 |
| XI | XI | Rayan Aït-Nouri | DEF | 20 | 4.8 | 3.37 | 9.91 | 15.63 | 0.00 | 83.1 | 90.0 |
| XI | XI | Noussair Mazraoui | DEF | 14 | 4.6 | 2.87 | 8.70 | 13.78 | 1.00 | 74.7 | 55.0 |
| Bench 2 | Bench | Lewis Hall | DEF | 15 | 4.4 | 2.70 | 8.47 | 13.61 | 2.00 | 73.8 | 90.0 |
| Bench 4 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.81 | 3.23 | 5.93 | 0.00 | 35.6 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 5.61 | 16.20 | 25.16 | 2.00 | 83.2 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 4.12 | 13.22 | 21.24 | 1.00 | 66.0 | 21.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 5.0 | 1.59 | 5.33 | 9.07 | 2.00 | 40.0 | 87.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 7.75 | 22.98 | 36.56 | 13.00 | 83.2 | 83.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.14 | 17.29 | 28.13 | 14.00 | 83.2 | 85.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.00 | 13.53 | 22.80 | 2.00 | 83.2 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.90 | 13.39 | 21.74 | 9.00 | 76.4 | 65.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 3.18 | 9.89 | 16.50 | 2.00 | 65.7 | 85.0 |

## GW14

- Train rows: 142282
- Bank: 0.60 -> 1.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 59.70
- Actual score: 58.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.50) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Alexander Isak -> Nicolas Jackson (projected gain 7.83, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.50) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 5.1 | 2.27 | 7.43 | 12.68 | 2.00 | 79.5 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.23 | 0.76 | 1.27 | 0.00 | 8.6 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.82 | 11.35 | 18.54 | 1.00 | 83.2 | 90.0 |
| XI | XI | Rayan Aït-Nouri | DEF | 20 | 4.8 | 3.16 | 9.32 | 15.10 | 0.00 | 81.6 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 2.51 | 8.12 | 13.37 | 1.00 | 78.4 | 90.0 |
| Bench 3 | Bench Boost | Noussair Mazraoui | DEF | 14 | 4.6 | 2.27 | 7.68 | 12.99 | 1.00 | 68.5 | 90.0 |
| Bench 4 | Bench Boost | Jan Bednarek | DEF | 17 | 4.0 | 0.44 | 1.99 | 3.88 | 0.00 | 24.6 | 0.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 8.1 | 5.26 | 14.94 | 23.13 | 0.00 | 80.5 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.24 | 13.78 | 21.35 | 2.00 | 76.6 | 90.0 |
| Bench 2 | Bench Boost | Cameron Archer | FWD | 17 | 5.0 | 2.57 | 7.17 | 11.61 | 2.00 | 66.7 | 71.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 7.51 | 23.01 | 37.09 | 18.00 | 83.2 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 7.03 | 19.59 | 31.51 | 7.00 | 83.2 | 78.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.65 | 13.04 | 22.49 | 2.00 | 74.3 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.8 | 3.90 | 11.41 | 20.36 | 2.00 | 78.1 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.7 | 3.32 | 9.88 | 16.69 | 2.00 | 71.8 | 70.0 |

## GW15

- Train rows: 142975
- Bank: 1.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Matheus Santos Carneiro Da Cunha
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 45.57
- Actual score: 71.00
- Transfer: Cameron Archer -> João Pedro Junqueira de Jesus (projected gain 4.92, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 5.1 | 2.66 | 7.77 | 12.93 | 1.00 | 80.9 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.44 | 0.84 | 1.34 | 0.00 | 7.4 | 0.0 |
| Bench 2 | Bench | Virgil van Dijk | DEF | 12 | 6.3 | 0.00 | 8.48 | 14.66 | 0.00 | 0.0 | 0.0 |
| XI | XI | Rayan Aït-Nouri | DEF | 20 | 4.8 | 2.97 | 8.21 | 13.48 | 4.00 | 79.4 | 85.0 |
| XI | XI | Noussair Mazraoui | DEF | 14 | 4.6 | 2.74 | 8.08 | 12.95 | 1.00 | 73.2 | 24.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 2.66 | 7.64 | 12.49 | 1.00 | 78.4 | 82.0 |
| Bench 3 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.00 | 0.83 | 2.16 | 0.00 | 13.3 | 0.0 |
| Vice Captain | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.59 | 13.15 | 21.21 | 1.00 | 80.2 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.9 | 4.38 | 11.75 | 18.41 | 2.00 | 66.1 | 70.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 8.1 | 2.73 | 9.13 | 15.01 | 2.00 | 32.3 | 75.0 |
| Bench 4 | Bench | Mohamed Salah | MID | 12 | 13.1 | 0.00 | 22.01 | 36.94 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 10.9 | 6.21 | 18.12 | 29.59 | 18.00 | 83.2 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.10 | 12.92 | 22.02 | 9.00 | 80.1 | 75.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 3.60 | 10.96 | 19.58 | 13.00 | 77.1 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.6 | 2.71 | 9.05 | 14.97 | 1.00 | 64.7 | 59.0 |