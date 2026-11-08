# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 268.55
- Total actual points: 288.00
- Average predicted points: 67.14
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
- Predicted score: 63.84
- Actual score: 59.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.83 | 10.87 | 17.41 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.27 | 0.61 | 1.07 | 0.00 | 6.8 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.39 | 13.16 | 20.39 | 6.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.32 | 11.83 | 19.62 | 6.00 | 90.0 | 62.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.7 | 3.13 | 9.64 | 15.63 | 1.00 | 83.9 | 90.0 |
| Bench 3 | Bench | Dara O'Shea | DEF | 10 | 4.0 | 2.24 | 6.69 | 11.03 | 2.00 | 82.5 | 90.0 |
| Bench 2 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.28 | 5.99 | 9.90 | 0.00 | 68.7 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.6 | 6.10 | 16.72 | 26.62 | 11.00 | 90.0 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.31 | 12.57 | 20.44 | 9.00 | 82.5 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.61 | 10.61 | 16.98 | 1.00 | 78.8 | 58.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 8.24 | 23.74 | 38.17 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.32 | 21.86 | 36.83 | 5.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.28 | 18.80 | 29.83 | 3.00 | 89.1 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 4.06 | 12.46 | 19.76 | 5.00 | 86.8 | 90.0 |
| Bench 4 | Bench | Tyler Dibling | MID | 17 | 4.5 | 2.13 | 5.49 | 8.77 | 2.00 | 57.6 | 90.0 |

## GW17

- Train rows: 144369
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 59.87
- Actual score: 70.00
- Transfer: Daniel Muñoz -> Lewis Hall (projected gain 3.89, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.75 | 10.75 | 17.29 | 3.00 | 88.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.23 | 0.55 | 0.95 | 0.00 | 6.8 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.01 | 12.04 | 19.21 | 2.00 | 84.8 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.74 | 10.51 | 16.47 | 7.00 | 84.3 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 3.18 | 10.05 | 17.01 | -1.00 | 78.0 | 90.0 |
| Bench 2 | Bench | Dara O'Shea | DEF | 10 | 4.0 | 2.21 | 6.66 | 11.00 | 0.00 | 82.8 | 90.0 |
| Bench 3 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 1.94 | 5.63 | 9.40 | 8.00 | 69.2 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.7 | 5.86 | 17.75 | 27.87 | 17.00 | 87.4 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.69 | 12.61 | 21.08 | 9.00 | 81.1 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.38 | 9.26 | 15.30 | 2.00 | 66.6 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 7.37 | 23.25 | 37.15 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.02 | 22.20 | 36.79 | 21.00 | 90.0 | 86.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.23 | 18.73 | 30.46 | 1.00 | 87.0 | 23.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.26 | 11.44 | 18.05 | 3.00 | 74.3 | 90.0 |
| Bench 4 | Bench | Tyler Dibling | MID | 17 | 4.5 | 1.87 | 5.33 | 8.69 | 1.00 | 59.3 | 45.0 |

## GW18

- Train rows: 145070
- Bank: 0.10 -> 2.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 71.78
- Actual score: 73.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.56) beats the best remaining Bench Boost opportunity (7.81).
- Transfer: Bukayo Saka -> Bruno Borges Fernandes (projected gain 8.07, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.56) beats the best remaining Bench Boost opportunity (7.81).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 4.17 | 11.23 | 18.01 | 6.00 | 89.9 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.19 | 0.51 | 0.89 | 0.00 | 7.2 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.71 | 13.13 | 21.07 | 7.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 3.18 | 9.73 | 16.34 | 1.00 | 83.6 | 9.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.04 | 8.97 | 14.31 | 6.00 | 69.4 | 90.0 |
| Bench 4 | Bench Boost | Dara O'Shea | DEF | 10 | 4.0 | 1.95 | 6.36 | 10.70 | 2.00 | 84.0 | 90.0 |
| Bench 2 | Bench Boost | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.43 | 6.33 | 10.33 | 2.00 | 75.2 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 7.36 | 21.34 | 33.28 | 8.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.63 | 12.84 | 21.61 | 12.00 | 83.2 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 2.59 | 8.60 | 14.29 | 0.00 | 62.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.4 | 9.63 | 25.19 | 41.37 | 9.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.62 | 23.27 | 37.65 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 5.20 | 14.33 | 24.09 | -2.00 | 90.0 | 46.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.46 | 10.55 | 17.15 | 2.00 | 76.3 | 90.0 |
| Bench 3 | Bench Boost | Tyler Dibling | MID | 17 | 4.5 | 1.98 | 5.24 | 8.57 | 1.00 | 53.3 | 17.0 |

## GW19

- Train rows: 145775
- Bank: 2.10 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 73.06
- Actual score: 86.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.66) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Tyler Dibling -> Ismaïla Sarr (projected gain 5.11, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.66) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Dara O'Shea replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.93 | 11.10 | 17.89 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.06 | 0.61 | 1.02 | 0.00 | 9.7 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.43 | 12.86 | 21.26 | 2.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.91 | 11.10 | 18.00 | 12.00 | 79.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 2.72 | 8.28 | 14.41 | 4.00 | 57.8 | 90.0 |
| Bench 2 | Autosub In | Dara O'Shea | DEF | 10 | 4.0 | 2.42 | 6.98 | 11.27 | 5.00 | 84.6 | 90.0 |
| Bench 3 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.35 | 6.79 | 10.93 | 0.00 | 76.6 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 7.21 | 20.84 | 32.63 | 7.00 | 80.8 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 5.44 | 15.33 | 25.24 | 1.00 | 90.0 | 45.0 |
| Bench 4 | Bench | Jamie Vardy | FWD | 11 | 5.6 | 0.93 | 4.14 | 7.20 | 2.00 | 17.9 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.5 | 8.66 | 25.04 | 40.54 | 16.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.88 | 22.96 | 37.86 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ismaïla Sarr | MID | 7 | 5.9 | 4.70 | 12.03 | 19.10 | 2.00 | 86.2 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 4.01 | 11.20 | 18.06 | 1.00 | 80.6 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.4 | 2.83 | 9.06 | 16.11 | 0.00 | 48.3 | 0.0 |