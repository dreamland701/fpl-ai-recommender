# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 268.20
- Total actual points: 281.00
- Average predicted points: 67.05
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
- Predicted score: 63.65
- Actual score: 59.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.73 | 10.69 | 17.12 | 6.00 | 87.4 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.29 | 0.62 | 1.05 | 0.00 | 6.6 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.19 | 12.50 | 19.24 | 6.00 | 85.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.30 | 11.90 | 19.85 | 6.00 | 89.2 | 62.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.7 | 2.99 | 9.15 | 14.76 | 1.00 | 80.6 | 90.0 |
| Bench 2 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.38 | 6.30 | 10.44 | 0.00 | 71.6 | 90.0 |
| Bench 3 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 2.19 | 6.29 | 10.27 | 2.00 | 71.1 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.6 | 6.11 | 16.95 | 27.12 | 11.00 | 90.0 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.31 | 12.88 | 21.05 | 9.00 | 81.6 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.80 | 11.36 | 18.22 | 1.00 | 82.6 | 58.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 8.32 | 24.28 | 39.09 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.36 | 22.10 | 37.36 | 5.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.20 | 18.73 | 29.62 | 3.00 | 87.1 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 4.01 | 12.40 | 19.69 | 5.00 | 84.5 | 90.0 |
| Bench 4 | Bench | Tyler Dibling | MID | 17 | 4.5 | 2.18 | 5.63 | 8.98 | 2.00 | 59.1 | 90.0 |

## GW17

- Train rows: 144369
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 59.73
- Actual score: 70.00
- Transfer: Daniel Muñoz -> Lewis Hall (projected gain 4.58, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.68 | 10.70 | 17.23 | 3.00 | 85.8 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.25 | 0.56 | 0.95 | 0.00 | 6.6 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 3.83 | 11.52 | 18.31 | 2.00 | 80.2 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.77 | 10.69 | 16.82 | 7.00 | 86.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 3.15 | 10.18 | 17.33 | -1.00 | 74.6 | 90.0 |
| Bench 2 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 2.06 | 6.13 | 10.24 | 0.00 | 71.4 | 90.0 |
| Bench 3 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.04 | 5.93 | 9.91 | 8.00 | 72.0 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.7 | 5.82 | 17.78 | 28.01 | 17.00 | 85.8 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.68 | 12.87 | 21.60 | 9.00 | 79.9 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.57 | 9.94 | 16.45 | 2.00 | 70.4 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 7.40 | 23.59 | 37.71 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.08 | 22.54 | 37.46 | 21.00 | 90.0 | 86.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.16 | 18.62 | 30.17 | 1.00 | 85.6 | 23.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.18 | 11.28 | 17.81 | 3.00 | 71.4 | 90.0 |
| Bench 4 | Bench | Tyler Dibling | MID | 17 | 4.5 | 1.93 | 5.44 | 8.86 | 1.00 | 61.0 | 45.0 |

## GW18

- Train rows: 145070
- Bank: 0.10 -> 2.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 71.89
- Actual score: 71.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.59) beats the best remaining Bench Boost opportunity (7.84).
- Transfer: Bukayo Saka -> Bruno Borges Fernandes (projected gain 8.36, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.59) beats the best remaining Bench Boost opportunity (7.84).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 4.09 | 11.16 | 17.93 | 6.00 | 87.7 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.21 | 0.52 | 0.87 | 0.00 | 7.0 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.56 | 12.74 | 20.42 | 7.00 | 87.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 3.11 | 9.75 | 16.49 | 1.00 | 79.7 | 9.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.08 | 9.19 | 14.75 | 6.00 | 71.8 | 90.0 |
| Bench 2 | Bench Boost | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.55 | 6.71 | 10.98 | 2.00 | 78.1 | 90.0 |
| Bench 4 | Bench Boost | Cameron Burgess | DEF | 10 | 4.0 | 1.79 | 6.02 | 9.98 | 0.00 | 77.3 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 7.32 | 21.26 | 33.23 | 8.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.60 | 13.09 | 22.13 | 12.00 | 82.1 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 2.75 | 9.16 | 15.20 | 0.00 | 65.6 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.4 | 9.71 | 25.63 | 42.22 | 9.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.65 | 23.63 | 38.27 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 5.27 | 14.98 | 25.31 | -2.00 | 90.0 | 46.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.43 | 10.60 | 17.30 | 2.00 | 74.6 | 90.0 |
| Bench 3 | Bench Boost | Tyler Dibling | MID | 17 | 4.5 | 2.05 | 5.42 | 8.86 | 1.00 | 55.3 | 17.0 |

## GW19

- Train rows: 145775
- Bank: 2.10 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 72.94
- Actual score: 81.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.69) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Tyler Dibling -> Ismaïla Sarr (projected gain 5.39, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.69) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Taylor Harwood-Bellis replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.87 | 11.08 | 17.93 | 2.00 | 88.5 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.08 | 0.62 | 1.00 | 0.00 | 9.5 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.27 | 12.43 | 20.57 | 2.00 | 88.6 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 4.01 | 11.51 | 18.75 | 12.00 | 83.2 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 2.62 | 8.19 | 14.41 | 4.00 | 53.4 | 90.0 |
| Bench 2 | Autosub In | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.46 | 7.14 | 11.51 | 0.00 | 79.4 | 90.0 |
| Bench 3 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 1.19 | 3.84 | 6.57 | 0.00 | 45.9 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 7.11 | 20.49 | 32.06 | 7.00 | 77.7 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 5.44 | 15.61 | 25.86 | 1.00 | 90.0 | 45.0 |
| Bench 4 | Bench | Jamie Vardy | FWD | 11 | 5.6 | 1.06 | 4.56 | 7.85 | 2.00 | 20.0 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.5 | 8.69 | 25.28 | 41.05 | 16.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.89 | 23.21 | 38.31 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ismaïla Sarr | MID | 7 | 5.9 | 4.83 | 12.43 | 19.76 | 2.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.98 | 11.24 | 18.19 | 1.00 | 78.8 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.4 | 2.82 | 9.43 | 16.86 | 0.00 | 46.7 | 0.0 |