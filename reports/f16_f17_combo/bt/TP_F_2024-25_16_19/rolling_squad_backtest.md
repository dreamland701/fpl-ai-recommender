# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 265.79
- Total actual points: 288.00
- Average predicted points: 66.45
- Average actual points: 72.00
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW15 are included before the first simulated week.
- League-average scores were not available for this run.

## GW16

- Train rows: 143668
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 62.91
- Actual score: 59.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.77 | 10.78 | 17.41 | 6.00 | 88.9 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.28 | 0.63 | 1.17 | 0.00 | 7.7 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.32 | 13.06 | 20.37 | 6.00 | 89.2 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.31 | 11.82 | 19.70 | 6.00 | 90.0 | 62.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.7 | 3.08 | 9.56 | 15.63 | 1.00 | 82.7 | 90.0 |
| Bench 3 | Bench | Dara O'Shea | DEF | 10 | 4.0 | 2.19 | 6.61 | 11.04 | 2.00 | 81.3 | 90.0 |
| Bench 2 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.23 | 5.91 | 9.90 | 0.00 | 67.8 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.6 | 6.01 | 16.57 | 26.55 | 11.00 | 89.5 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.25 | 12.49 | 20.45 | 9.00 | 81.0 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.50 | 10.42 | 16.85 | 1.00 | 76.2 | 58.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 8.13 | 23.55 | 38.04 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.25 | 21.74 | 36.80 | 5.00 | 89.6 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.18 | 18.64 | 29.75 | 3.00 | 86.6 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.98 | 12.33 | 19.72 | 5.00 | 85.1 | 90.0 |
| Bench 4 | Bench | Tyler Dibling | MID | 17 | 4.5 | 2.09 | 5.43 | 8.78 | 2.00 | 57.1 | 90.0 |

## GW17

- Train rows: 144369
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 60.50
- Actual score: 70.00
- Transfer: Daniel Muñoz -> Lewis Hall (projected gain 3.81, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.83 | 10.88 | 17.40 | 3.00 | 89.8 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.36 | 0.76 | 1.15 | 0.00 | 10.6 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.07 | 12.13 | 19.26 | 2.00 | 86.3 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.76 | 10.54 | 16.48 | 7.00 | 85.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 3.32 | 10.29 | 17.25 | -1.00 | 82.1 | 90.0 |
| Bench 2 | Bench | Dara O'Shea | DEF | 10 | 4.0 | 2.27 | 6.77 | 11.11 | 0.00 | 84.5 | 90.0 |
| Bench 3 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.01 | 5.75 | 9.50 | 8.00 | 71.3 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.7 | 5.88 | 17.77 | 27.85 | 17.00 | 88.0 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.77 | 12.73 | 21.16 | 9.00 | 83.0 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.44 | 9.33 | 15.32 | 2.00 | 68.4 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 7.38 | 23.24 | 37.10 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.08 | 22.30 | 36.87 | 21.00 | 90.0 | 86.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.29 | 18.81 | 30.51 | 1.00 | 88.3 | 23.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.31 | 11.52 | 18.11 | 3.00 | 75.8 | 90.0 |
| Bench 4 | Bench | Tyler Dibling | MID | 17 | 4.5 | 1.96 | 5.47 | 8.81 | 1.00 | 61.8 | 45.0 |

## GW18

- Train rows: 145070
- Bank: 0.10 -> 2.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 70.80
- Actual score: 73.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.36) beats the best remaining Bench Boost opportunity (7.58).
- Transfer: Bukayo Saka -> Bruno Borges Fernandes (projected gain 8.09, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.36) beats the best remaining Bench Boost opportunity (7.58).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 4.11 | 11.15 | 18.03 | 6.00 | 88.7 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.20 | 0.52 | 1.00 | 0.00 | 8.2 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.66 | 13.04 | 21.08 | 7.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 3.17 | 9.72 | 16.44 | 1.00 | 83.7 | 9.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 2.96 | 8.82 | 14.24 | 6.00 | 67.7 | 90.0 |
| Bench 4 | Bench Boost | Dara O'Shea | DEF | 10 | 4.0 | 1.89 | 6.25 | 10.70 | 2.00 | 82.6 | 90.0 |
| Bench 2 | Bench Boost | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.35 | 6.19 | 10.27 | 2.00 | 73.3 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 7.26 | 21.14 | 33.14 | 8.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.57 | 12.75 | 21.61 | 12.00 | 82.0 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 2.53 | 8.48 | 14.25 | 0.00 | 61.2 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.4 | 9.56 | 25.05 | 41.31 | 9.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.52 | 23.08 | 37.55 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 5.14 | 14.21 | 24.05 | -2.00 | 89.0 | 46.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.41 | 10.46 | 17.15 | 2.00 | 75.3 | 90.0 |
| Bench 3 | Bench Boost | Tyler Dibling | MID | 17 | 4.5 | 1.92 | 5.13 | 8.54 | 1.00 | 52.2 | 17.0 |

## GW19

- Train rows: 145775
- Bank: 2.10 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 71.57
- Actual score: 86.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.56) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Jamie Vardy -> Dominic Solanke-Mitchell (projected gain 5.04, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.56) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Dara O'Shea replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.89 | 11.04 | 17.91 | 2.00 | 89.1 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.07 | 0.64 | 1.13 | 0.00 | 10.6 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.39 | 12.81 | 21.29 | 2.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.84 | 10.98 | 17.94 | 12.00 | 77.6 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 2.78 | 8.38 | 14.59 | 4.00 | 60.0 | 90.0 |
| Bench 2 | Autosub In | Dara O'Shea | DEF | 10 | 4.0 | 2.38 | 6.92 | 11.29 | 5.00 | 83.8 | 90.0 |
| Bench 3 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.27 | 6.67 | 10.87 | 0.00 | 74.8 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 7.15 | 20.70 | 32.50 | 7.00 | 79.4 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 5.39 | 15.24 | 25.22 | 1.00 | 90.0 | 45.0 |
| XI | XI | Dominic Solanke-Mitchell | FWD | 18 | 7.5 | 3.87 | 11.88 | 19.52 | 2.00 | 84.2 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.5 | 8.56 | 24.86 | 40.40 | 16.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.81 | 22.84 | 37.80 | 2.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.97 | 11.13 | 18.05 | 1.00 | 79.7 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.4 | 2.81 | 9.04 | 16.14 | 0.00 | 47.7 | 0.0 |
| Bench 4 | Bench | Tyler Dibling | MID | 17 | 4.5 | 1.49 | 4.79 | 7.97 | 8.00 | 43.0 | 85.0 |