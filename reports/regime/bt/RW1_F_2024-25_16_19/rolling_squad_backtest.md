# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 268.01
- Total actual points: 281.00
- Average predicted points: 67.00
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
- Predicted score: 63.25
- Actual score: 59.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.69 | 10.46 | 16.35 | 6.00 | 87.1 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.25 | 0.53 | 0.87 | 0.00 | 5.7 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.19 | 12.38 | 18.58 | 6.00 | 85.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.13 | 11.31 | 18.79 | 6.00 | 88.0 | 62.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.7 | 3.06 | 9.68 | 15.56 | 1.00 | 82.3 | 90.0 |
| Bench 2 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.34 | 6.35 | 10.59 | 0.00 | 71.8 | 90.0 |
| Bench 4 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 2.15 | 6.25 | 10.16 | 2.00 | 71.1 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.6 | 6.11 | 17.04 | 26.83 | 11.00 | 90.0 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.31 | 12.62 | 20.45 | 9.00 | 82.6 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.78 | 11.20 | 17.90 | 1.00 | 83.8 | 58.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 8.14 | 23.51 | 37.53 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.48 | 22.61 | 37.76 | 5.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.29 | 18.58 | 29.15 | 3.00 | 88.6 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.93 | 12.13 | 19.27 | 5.00 | 88.1 | 90.0 |
| Bench 3 | Bench | Tyler Dibling | MID | 17 | 4.5 | 2.18 | 5.79 | 9.10 | 2.00 | 59.9 | 90.0 |

## GW17

- Train rows: 144369
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 59.52
- Actual score: 70.00
- Transfer: Daniel Muñoz -> Lewis Hall (projected gain 4.92, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.57 | 10.35 | 16.40 | 3.00 | 85.8 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.22 | 0.55 | 0.88 | 0.00 | 6.2 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 3.91 | 11.29 | 17.62 | 2.00 | 82.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.80 | 11.02 | 17.58 | 7.00 | 88.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 3.11 | 9.60 | 16.06 | -1.00 | 74.5 | 90.0 |
| Bench 2 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 2.07 | 6.11 | 9.99 | 0.00 | 71.9 | 90.0 |
| Bench 3 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.02 | 5.96 | 9.99 | 8.00 | 72.3 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.7 | 5.94 | 17.90 | 28.17 | 17.00 | 88.8 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.74 | 12.92 | 21.47 | 9.00 | 80.8 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.41 | 9.07 | 15.01 | 2.00 | 68.9 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 7.32 | 23.03 | 36.69 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.03 | 22.93 | 37.36 | 21.00 | 90.0 | 86.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.19 | 18.38 | 29.75 | 1.00 | 85.2 | 23.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.17 | 10.82 | 17.25 | 3.00 | 76.9 | 90.0 |
| Bench 4 | Bench | Tyler Dibling | MID | 17 | 4.5 | 1.96 | 5.77 | 9.28 | 1.00 | 62.6 | 45.0 |

## GW18

- Train rows: 145070
- Bank: 0.10 -> 2.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 72.20
- Actual score: 71.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.74) beats the best remaining Bench Boost opportunity (8.03).
- Transfer: Bukayo Saka -> Bruno Borges Fernandes (projected gain 7.39, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.74) beats the best remaining Bench Boost opportunity (8.03).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.99 | 10.81 | 17.37 | 6.00 | 87.9 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.19 | 0.51 | 0.84 | 0.00 | 6.6 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.62 | 12.78 | 20.36 | 7.00 | 89.2 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 3.13 | 9.69 | 16.10 | 1.00 | 80.8 | 9.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.21 | 9.39 | 15.25 | 6.00 | 76.2 | 90.0 |
| Bench 2 | Bench Boost | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.58 | 7.10 | 11.24 | 2.00 | 77.7 | 90.0 |
| Bench 3 | Bench Boost | Cameron Burgess | DEF | 10 | 4.0 | 1.99 | 6.41 | 10.24 | 0.00 | 78.1 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 7.36 | 20.39 | 32.44 | 8.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.64 | 13.06 | 22.31 | 12.00 | 83.8 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 2.80 | 8.79 | 14.73 | 0.00 | 67.6 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.4 | 9.71 | 25.52 | 42.06 | 9.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.47 | 23.17 | 37.21 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 5.35 | 14.40 | 24.49 | -2.00 | 90.0 | 46.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.46 | 10.34 | 16.96 | 2.00 | 78.2 | 90.0 |
| Bench 4 | Bench Boost | Tyler Dibling | MID | 17 | 4.5 | 1.98 | 5.66 | 9.20 | 1.00 | 54.7 | 17.0 |

## GW19

- Train rows: 145775
- Bank: 2.10 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 73.03
- Actual score: 81.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.72) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Tyler Dibling -> Ismaïla Sarr (projected gain 5.64, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.72) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Taylor Harwood-Bellis replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.80 | 10.94 | 17.77 | 2.00 | 88.4 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.09 | 0.52 | 0.98 | 0.00 | 8.8 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.36 | 12.54 | 20.84 | 2.00 | 89.6 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.88 | 11.06 | 19.02 | 12.00 | 85.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 2.53 | 7.91 | 13.98 | 4.00 | 53.1 | 90.0 |
| Bench 2 | Autosub In | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.40 | 6.93 | 11.48 | 0.00 | 79.5 | 90.0 |
| Bench 3 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 1.22 | 3.92 | 6.87 | 0.00 | 44.9 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 7.26 | 19.62 | 31.28 | 7.00 | 80.8 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 5.48 | 15.29 | 25.80 | 1.00 | 90.0 | 45.0 |
| Bench 4 | Bench | Jamie Vardy | FWD | 11 | 5.6 | 1.11 | 4.41 | 7.64 | 2.00 | 21.0 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.5 | 8.72 | 25.33 | 41.32 | 16.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.77 | 22.52 | 36.91 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ismaïla Sarr | MID | 7 | 5.9 | 4.93 | 12.49 | 20.29 | 2.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.99 | 10.93 | 17.71 | 1.00 | 81.9 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.4 | 2.87 | 8.79 | 15.64 | 0.00 | 46.5 | 0.0 |