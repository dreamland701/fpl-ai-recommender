# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 253.62
- Total actual points: 304.00
- Average predicted points: 63.40
- Average actual points: 76.00
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
- Predicted score: 65.10
- Actual score: 71.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 5.1 | 5.52 | 16.27 | 22.61 | 3.00 | 85.9 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.05 | 0.37 | 0.73 | 0.00 | 8.4 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.89 | 12.99 | 20.92 | 1.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 3.80 | 11.56 | 18.69 | 6.00 | 87.2 | 90.0 |
| XI | XI | Ibrahima Konaté | DEF | 12 | 5.4 | 4.25 | 11.01 | 17.78 | 0.00 | 85.9 | 90.0 |
| Bench 3 | Bench | Noussair Mazraoui | DEF | 14 | 4.6 | 3.70 | 10.09 | 15.60 | 2.00 | 85.1 | 90.0 |
| Bench 4 | Bench | Lewis Hall | DEF | 15 | 4.4 | 3.32 | 8.76 | 13.97 | 1.00 | 88.4 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.8 | 4.59 | 14.21 | 23.78 | 16.00 | 83.5 | 90.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 7.9 | 5.07 | 13.96 | 22.29 | 12.00 | 79.7 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 6.0 | 3.84 | 12.69 | 20.25 | 2.00 | 79.0 | 85.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 8.14 | 22.89 | 36.85 | 13.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.26 | 18.37 | 30.02 | 2.00 | 89.4 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 6.12 | 17.24 | 26.97 | 2.00 | 90.0 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 4.47 | 12.25 | 19.69 | 1.00 | 84.6 | 58.0 |
| Bench 2 | Bench | Morgan Rogers | MID | 2 | 5.4 | 3.77 | 10.55 | 16.75 | 2.00 | 77.0 | 81.0 |

## GW13

- Train rows: 141592
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: André Onana
- Vice captain: Mohamed Salah
- Effective captain: André Onana
- Chip used: none
- Predicted score: 68.70
- Actual score: 79.00
- Transfer: Emile Smith Rowe -> Alex Iwobi (projected gain 1.43, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Captain | Captain | André Onana | GK | 14 | 5.1 | 10.45 | 26.32 | 36.22 | 6.00 | 84.8 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.19 | 0.36 | 0.53 | 0.00 | 7.9 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.41 | 11.42 | 18.38 | 6.00 | 85.2 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 3.51 | 10.36 | 16.37 | 9.00 | 75.4 | 45.0 |
| XI | XI | Noussair Mazraoui | DEF | 14 | 4.6 | 2.48 | 7.90 | 12.28 | 1.00 | 73.8 | 55.0 |
| Bench 4 | Bench | Ibrahima Konaté | DEF | 12 | 5.4 | 1.89 | 7.57 | 12.09 | 0.00 | 55.7 | 0.0 |
| Bench 3 | Bench | Lewis Hall | DEF | 15 | 4.4 | 2.11 | 6.70 | 10.51 | 2.00 | 72.9 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 6.18 | 18.15 | 28.50 | 2.00 | 90.0 | 90.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 7.9 | 5.18 | 15.03 | 24.05 | 6.00 | 84.7 | 70.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 6.0 | 3.97 | 11.18 | 18.01 | 2.00 | 72.2 | 78.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.0 | 8.60 | 24.65 | 38.38 | 13.00 | 90.0 | 83.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.9 | 6.76 | 18.95 | 30.26 | 14.00 | 90.0 | 85.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.11 | 13.42 | 21.74 | 9.00 | 71.9 | 65.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.6 | 3.61 | 10.85 | 17.80 | 5.00 | 84.6 | 85.0 |
| Bench 2 | Bench | Morgan Rogers | MID | 2 | 5.4 | 3.26 | 9.44 | 15.66 | 2.00 | 68.4 | 65.0 |

## GW14

- Train rows: 142282
- Bank: 0.20 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 63.37
- Actual score: 76.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (4.86) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Gabriel dos Santos Magalhães -> Pedro Porro (projected gain 1.83, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (4.86) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 5.1 | 3.13 | 10.00 | 16.43 | 2.00 | 86.3 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.06 | 0.28 | 0.56 | 0.00 | 8.4 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.32 | 13.01 | 21.10 | 1.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 3.46 | 11.39 | 17.96 | 1.00 | 87.0 | 28.0 |
| Bench 3 | Bench Boost | Noussair Mazraoui | DEF | 14 | 4.6 | 1.71 | 6.49 | 11.24 | 1.00 | 64.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 2.13 | 6.34 | 10.08 | 1.00 | 77.5 | 90.0 |
| Bench 4 | Bench Boost | Ibrahima Konaté | DEF | 12 | 5.3 | 0.12 | 1.94 | 4.54 | 0.00 | 21.4 | 0.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 8.0 | 5.40 | 16.41 | 25.90 | 0.00 | 87.3 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.40 | 15.12 | 23.82 | 2.00 | 75.7 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.9 | 3.57 | 10.27 | 16.69 | 0.00 | 68.7 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 8.57 | 25.27 | 39.37 | 18.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 7.36 | 20.98 | 33.14 | 7.00 | 90.0 | 78.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.63 | 12.84 | 22.39 | 2.00 | 73.3 | 90.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.6 | 3.98 | 11.35 | 18.70 | 15.00 | 81.9 | 90.0 |
| Bench 2 | Bench Boost | Morgan Rogers | MID | 2 | 5.3 | 2.97 | 8.40 | 14.02 | 8.00 | 61.3 | 86.0 |

## GW15

- Train rows: 142975
- Bank: 0.70 -> 0.70
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Matheus Santos Carneiro Da Cunha
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 56.44
- Actual score: 78.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.79) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Danny Welbeck -> João Pedro Junqueira de Jesus (projected gain 6.49, hit 0)
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (6.79) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 5.1 | 3.42 | 9.84 | 16.34 | 1.00 | 87.8 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.13 | 0.29 | 0.52 | 0.00 | 7.3 | 0.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 12 | 6.3 | 0.00 | 10.00 | 16.99 | 0.00 | 0.0 | 0.0 |
| XI | XI | Noussair Mazraoui | DEF | 14 | 4.6 | 2.66 | 7.78 | 12.56 | 1.00 | 72.3 | 24.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 2.36 | 7.56 | 13.22 | 3.00 | 68.8 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 2.49 | 6.97 | 11.16 | 1.00 | 77.5 | 82.0 |
| Bench 2 | Bench | Ibrahima Konaté | DEF | 12 | 5.3 | 0.00 | 1.80 | 5.13 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.79 | 14.09 | 22.90 | 1.00 | 82.8 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.9 | 4.11 | 11.38 | 17.55 | 2.00 | 59.8 | 70.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 8.0 | 2.49 | 9.10 | 14.87 | 2.00 | 32.2 | 75.0 |
| Bench 4 | Bench | Mohamed Salah | MID | 12 | 13.1 | 0.00 | 24.38 | 39.59 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 10.9 | 7.42 | 20.65 | 32.71 | 18.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.46 | 13.81 | 23.59 | 9.00 | 87.0 | 75.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.6 | 3.28 | 11.48 | 19.04 | 2.00 | 84.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.3 | 4.11 | 11.12 | 17.79 | 2.00 | 75.9 | 90.0 |