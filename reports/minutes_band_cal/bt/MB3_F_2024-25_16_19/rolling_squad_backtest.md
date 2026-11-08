# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 268.29
- Total actual points: 281.00
- Average predicted points: 67.07
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
- Predicted score: 63.44
- Actual score: 59.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.74 | 10.69 | 17.13 | 6.00 | 87.4 | 90.0 |
| Bench 1 | Bench | João Neves Virgínia | GK | 8 | 3.9 | 0.00 | 0.32 | 0.70 | 0.00 | 6.6 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.23 | 12.71 | 19.61 | 6.00 | 85.6 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.20 | 11.54 | 19.14 | 6.00 | 88.2 | 62.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.7 | 3.03 | 9.35 | 15.11 | 1.00 | 80.7 | 90.0 |
| Bench 2 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.48 | 6.60 | 10.99 | 0.00 | 75.7 | 90.0 |
| Bench 4 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 2.29 | 6.56 | 10.76 | 2.00 | 75.2 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.6 | 6.09 | 16.82 | 26.84 | 11.00 | 90.0 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.26 | 12.55 | 20.46 | 9.00 | 80.8 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.77 | 11.21 | 18.03 | 1.00 | 83.2 | 58.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 8.24 | 23.82 | 38.31 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.41 | 22.32 | 37.69 | 5.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.24 | 18.78 | 29.83 | 3.00 | 87.5 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 4.00 | 12.36 | 19.62 | 5.00 | 84.8 | 90.0 |
| Bench 3 | Bench | Tyler Dibling | MID | 17 | 4.5 | 2.39 | 6.23 | 9.99 | 2.00 | 64.0 | 90.0 |

## GW17

- Train rows: 144369
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 59.78
- Actual score: 70.00
- Transfer: Daniel Muñoz -> Lewis Hall (projected gain 4.60, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.69 | 10.72 | 17.27 | 3.00 | 85.8 | 90.0 |
| Bench 1 | Bench | João Neves Virgínia | GK | 8 | 3.9 | 0.14 | 0.44 | 0.75 | 0.00 | 5.8 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 3.88 | 11.72 | 18.68 | 2.00 | 80.3 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.83 | 10.95 | 17.31 | 7.00 | 87.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 3.04 | 9.70 | 16.23 | -1.00 | 75.1 | 90.0 |
| Bench 2 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 2.15 | 6.38 | 10.73 | 0.00 | 75.5 | 90.0 |
| Bench 3 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.06 | 5.98 | 9.83 | 8.00 | 73.9 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.7 | 5.81 | 17.71 | 27.84 | 17.00 | 86.0 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.63 | 12.53 | 20.81 | 9.00 | 80.7 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.63 | 10.01 | 16.66 | 2.00 | 74.9 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 7.34 | 23.22 | 37.08 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.12 | 22.75 | 37.79 | 21.00 | 90.0 | 86.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.21 | 18.79 | 30.58 | 1.00 | 86.1 | 23.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.26 | 11.51 | 18.25 | 3.00 | 75.8 | 90.0 |
| Bench 4 | Bench | Tyler Dibling | MID | 17 | 4.5 | 2.04 | 5.80 | 9.55 | 1.00 | 65.3 | 45.0 |

## GW18

- Train rows: 145070
- Bank: 0.10 -> 2.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 71.84
- Actual score: 71.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.63) beats the best remaining Bench Boost opportunity (7.90).
- Transfer: Bukayo Saka -> Bruno Borges Fernandes (projected gain 7.72, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.63) beats the best remaining Bench Boost opportunity (7.90).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 4.10 | 11.19 | 17.98 | 6.00 | 87.8 | 90.0 |
| Bench 1 | Bench Boost | João Neves Virgínia | GK | 8 | 3.9 | 0.00 | 0.37 | 0.81 | 0.00 | 6.7 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.60 | 12.93 | 20.76 | 7.00 | 88.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.13 | 9.38 | 14.95 | 6.00 | 74.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 3.03 | 9.33 | 15.52 | 1.00 | 80.4 | 9.0 |
| Bench 2 | Bench Boost | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.56 | 6.71 | 10.83 | 2.00 | 79.9 | 90.0 |
| Bench 4 | Bench Boost | Cameron Burgess | DEF | 10 | 4.0 | 1.81 | 6.05 | 9.87 | 0.00 | 79.1 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 7.30 | 21.23 | 33.10 | 8.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.56 | 12.84 | 21.67 | 12.00 | 81.5 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 2.82 | 9.26 | 15.49 | 0.00 | 70.1 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.4 | 9.74 | 25.81 | 42.51 | 9.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.60 | 23.26 | 37.62 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 5.16 | 14.35 | 24.17 | -2.00 | 89.1 | 46.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.42 | 10.52 | 17.00 | 2.00 | 76.7 | 90.0 |
| Bench 3 | Bench Boost | Tyler Dibling | MID | 17 | 4.5 | 2.26 | 6.02 | 9.85 | 1.00 | 60.0 | 17.0 |

## GW19

- Train rows: 145775
- Bank: 2.10 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 73.22
- Actual score: 81.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.72) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Tyler Dibling -> Ismaïla Sarr (projected gain 5.55, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.72) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Taylor Harwood-Bellis replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.87 | 11.10 | 17.97 | 2.00 | 88.6 | 90.0 |
| Bench 1 | Bench | João Neves Virgínia | GK | 8 | 3.9 | 0.18 | 0.66 | 1.17 | 0.00 | 9.2 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.32 | 12.67 | 21.00 | 2.00 | 88.8 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 4.05 | 11.70 | 19.11 | 12.00 | 83.7 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 2.71 | 8.30 | 14.44 | 4.00 | 56.9 | 90.0 |
| Bench 2 | Autosub In | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.48 | 7.14 | 11.40 | 0.00 | 81.2 | 90.0 |
| Bench 3 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 1.38 | 4.38 | 7.43 | 0.00 | 50.5 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 7.12 | 20.50 | 31.92 | 7.00 | 79.7 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 5.40 | 15.36 | 25.39 | 1.00 | 90.0 | 45.0 |
| Bench 4 | Bench | Jamie Vardy | FWD | 11 | 5.6 | 0.99 | 4.36 | 7.61 | 2.00 | 19.5 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.5 | 8.72 | 25.42 | 41.28 | 16.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.85 | 22.91 | 37.77 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ismaïla Sarr | MID | 7 | 5.9 | 4.87 | 12.61 | 20.10 | 2.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.98 | 11.14 | 17.89 | 1.00 | 81.0 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.4 | 2.91 | 9.36 | 16.60 | 0.00 | 49.9 | 0.0 |