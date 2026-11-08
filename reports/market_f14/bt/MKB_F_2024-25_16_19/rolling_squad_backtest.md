# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 266.69
- Total actual points: 281.00
- Average predicted points: 66.67
- Average actual points: 70.25
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
- Predicted score: 63.48
- Actual score: 59.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.83 | 10.90 | 17.39 | 6.00 | 86.4 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 6 | 3.9 | 0.00 | 0.08 | 0.28 | 0.00 | 0.0 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.40 | 13.06 | 20.07 | 6.00 | 85.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.19 | 11.58 | 19.25 | 6.00 | 90.0 | 62.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.7 | 2.98 | 9.23 | 14.96 | 1.00 | 79.3 | 90.0 |
| Bench 3 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 2.19 | 6.31 | 10.33 | 2.00 | 70.4 | 90.0 |
| Bench 2 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.32 | 6.22 | 10.40 | 0.00 | 71.7 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.6 | 6.06 | 16.80 | 26.83 | 11.00 | 90.0 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.16 | 12.31 | 20.07 | 9.00 | 79.5 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.70 | 11.01 | 17.70 | 1.00 | 82.3 | 58.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 8.28 | 23.99 | 38.60 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.20 | 21.95 | 37.12 | 5.00 | 88.2 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.27 | 18.82 | 29.84 | 3.00 | 86.1 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 4.13 | 12.74 | 20.24 | 5.00 | 86.1 | 90.0 |
| Bench 4 | Bench | Tyler Dibling | MID | 17 | 4.5 | 2.10 | 5.50 | 8.89 | 2.00 | 59.3 | 90.0 |

## GW17

- Train rows: 144369
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 59.44
- Actual score: 70.00
- Transfer: Daniel Muñoz -> Lewis Hall (projected gain 3.36, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.77 | 10.90 | 17.48 | 3.00 | 84.7 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 6 | 3.9 | 0.00 | 0.00 | 0.05 | 0.00 | 0.0 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 3.93 | 11.82 | 18.74 | 2.00 | 77.7 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.87 | 11.07 | 17.49 | 7.00 | 87.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 3.03 | 9.69 | 16.45 | -1.00 | 74.7 | 90.0 |
| Bench 3 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 2.03 | 6.09 | 10.22 | 0.00 | 70.7 | 90.0 |
| Bench 2 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.07 | 6.07 | 10.16 | 8.00 | 71.1 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.7 | 5.77 | 17.64 | 27.71 | 17.00 | 85.6 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.42 | 12.05 | 20.26 | 9.00 | 76.4 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.46 | 9.61 | 15.98 | 2.00 | 69.8 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 7.37 | 23.31 | 37.19 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.01 | 22.57 | 37.53 | 21.00 | 90.0 | 86.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.23 | 18.79 | 30.51 | 1.00 | 84.6 | 23.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.22 | 11.39 | 17.95 | 3.00 | 71.6 | 90.0 |
| Bench 4 | Bench | Tyler Dibling | MID | 17 | 4.5 | 1.94 | 5.55 | 9.09 | 1.00 | 59.9 | 45.0 |

## GW18

- Train rows: 145070
- Bank: 0.10 -> 2.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 71.23
- Actual score: 71.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.47) beats the best remaining Bench Boost opportunity (7.73).
- Transfer: Bukayo Saka -> Bruno Borges Fernandes (projected gain 7.61, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.47) beats the best remaining Bench Boost opportunity (7.73).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 4.19 | 11.42 | 18.34 | 6.00 | 87.7 | 90.0 |
| Bench 1 | Bench Boost | Marcus Bettinelli | GK | 6 | 3.9 | 0.07 | 0.13 | 0.23 | 0.00 | 0.0 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.69 | 13.14 | 21.08 | 7.00 | 87.1 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 3.10 | 9.62 | 16.17 | 1.00 | 80.4 | 9.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.00 | 9.14 | 14.75 | 6.00 | 70.3 | 90.0 |
| Bench 2 | Bench Boost | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.52 | 6.70 | 11.00 | 2.00 | 77.8 | 90.0 |
| Bench 4 | Bench Boost | Cameron Burgess | DEF | 10 | 4.0 | 1.89 | 6.23 | 10.23 | 0.00 | 76.9 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 7.33 | 21.27 | 33.18 | 8.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.26 | 12.09 | 20.57 | 12.00 | 79.1 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 2.76 | 8.92 | 14.73 | 0.00 | 64.1 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.4 | 9.61 | 25.54 | 42.18 | 9.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.65 | 23.43 | 37.87 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 5.10 | 14.23 | 23.95 | -2.00 | 86.6 | 46.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.45 | 10.62 | 17.31 | 2.00 | 74.9 | 90.0 |
| Bench 3 | Bench Boost | Tyler Dibling | MID | 17 | 4.5 | 1.99 | 5.36 | 8.84 | 1.00 | 54.4 | 17.0 |

## GW19

- Train rows: 145775
- Bank: 2.10 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 72.54
- Actual score: 81.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.61) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Tyler Dibling -> Ismaïla Sarr (projected gain 5.29, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.61) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Taylor Harwood-Bellis replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.88 | 11.14 | 18.02 | 2.00 | 87.9 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 6 | 3.9 | 0.20 | 0.44 | 0.63 | 0.00 | 2.6 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.32 | 12.70 | 21.00 | 2.00 | 87.3 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.93 | 11.41 | 18.69 | 12.00 | 83.8 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 2.57 | 7.98 | 13.94 | 4.00 | 52.5 | 90.0 |
| Bench 2 | Autosub In | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.49 | 7.28 | 11.75 | 0.00 | 79.4 | 90.0 |
| Bench 4 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 1.00 | 3.42 | 5.96 | 0.00 | 42.6 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 7.05 | 20.33 | 31.83 | 7.00 | 80.3 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 5.24 | 14.95 | 24.80 | 1.00 | 90.0 | 45.0 |
| Bench 3 | Bench | Jamie Vardy | FWD | 11 | 5.6 | 1.29 | 4.93 | 8.42 | 2.00 | 26.9 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.5 | 8.61 | 25.23 | 40.99 | 16.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.87 | 22.96 | 37.84 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ismaïla Sarr | MID | 7 | 5.9 | 4.82 | 12.46 | 19.85 | 2.00 | 89.6 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.99 | 11.24 | 18.15 | 1.00 | 79.2 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.05 | 9.67 | 17.06 | 0.00 | 50.9 | 0.0 |