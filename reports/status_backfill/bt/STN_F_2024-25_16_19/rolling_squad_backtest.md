# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 270.13
- Total actual points: 281.00
- Average predicted points: 67.53
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
- Predicted score: 64.48
- Actual score: 59.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.77 | 10.69 | 17.13 | 6.00 | 88.9 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.28 | 0.62 | 1.04 | 0.00 | 6.3 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.49 | 12.71 | 19.61 | 6.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.14 | 11.54 | 19.14 | 6.00 | 86.4 | 62.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.7 | 3.08 | 9.35 | 15.11 | 1.00 | 81.3 | 90.0 |
| Bench 2 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.35 | 6.38 | 10.58 | 0.00 | 71.5 | 90.0 |
| Bench 4 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 2.17 | 6.33 | 10.35 | 2.00 | 70.1 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.6 | 6.27 | 16.82 | 26.84 | 11.00 | 95.2 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.22 | 12.55 | 20.46 | 9.00 | 79.9 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.79 | 11.21 | 18.03 | 1.00 | 83.3 | 58.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 8.37 | 23.82 | 38.31 | 3.00 | 114.4 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.45 | 22.32 | 37.69 | 5.00 | 95.8 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.32 | 18.78 | 29.83 | 3.00 | 90.9 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 4.22 | 12.36 | 19.62 | 5.00 | 87.1 | 90.0 |
| Bench 3 | Bench | Tyler Dibling | MID | 17 | 4.5 | 2.22 | 5.74 | 9.19 | 2.00 | 59.6 | 90.0 |

## GW17

- Train rows: 144369
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 60.22
- Actual score: 70.00
- Transfer: Daniel Muñoz -> Lewis Hall (projected gain 4.80, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.71 | 10.72 | 17.27 | 3.00 | 87.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.24 | 0.56 | 0.95 | 0.00 | 6.4 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.01 | 11.72 | 18.68 | 2.00 | 82.5 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 4.00 | 10.95 | 17.31 | 7.00 | 90.8 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 2.87 | 9.72 | 16.44 | -1.00 | 69.8 | 90.0 |
| Bench 2 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 2.01 | 6.17 | 10.31 | 0.00 | 70.3 | 90.0 |
| Bench 3 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 1.99 | 6.00 | 10.05 | 8.00 | 71.7 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.7 | 6.14 | 17.71 | 27.84 | 17.00 | 92.5 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.48 | 12.55 | 21.02 | 9.00 | 76.5 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.63 | 9.80 | 16.24 | 2.00 | 71.5 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 7.47 | 23.22 | 37.08 | 3.00 | 104.8 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 6.95 | 22.75 | 37.79 | 21.00 | 95.5 | 86.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.20 | 18.79 | 30.58 | 1.00 | 86.8 | 23.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.30 | 11.29 | 17.83 | 3.00 | 72.5 | 90.0 |
| Bench 4 | Bench | Tyler Dibling | MID | 17 | 4.5 | 1.94 | 5.59 | 9.14 | 1.00 | 61.2 | 45.0 |

## GW18

- Train rows: 145070
- Bank: 0.10 -> 2.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 72.14
- Actual score: 71.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.59) beats the best remaining Bench Boost opportunity (7.84).
- Transfer: Bukayo Saka -> Bruno Borges Fernandes (projected gain 7.73, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.59) beats the best remaining Bench Boost opportunity (7.84).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 4.09 | 11.19 | 17.98 | 6.00 | 88.4 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.19 | 0.52 | 0.87 | 0.00 | 6.9 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.60 | 12.93 | 20.76 | 7.00 | 87.6 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.20 | 9.42 | 15.17 | 6.00 | 73.6 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 2.90 | 9.36 | 15.74 | 1.00 | 76.7 | 9.0 |
| Bench 2 | Bench Boost | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.50 | 6.74 | 11.05 | 2.00 | 77.5 | 90.0 |
| Bench 4 | Bench Boost | Cameron Burgess | DEF | 10 | 4.0 | 1.77 | 6.08 | 10.09 | 0.00 | 77.2 | 0.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 8.8 | 7.93 | 21.23 | 33.10 | 8.00 | 111.8 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.43 | 12.84 | 21.67 | 12.00 | 80.1 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 2.69 | 9.04 | 15.04 | 0.00 | 64.3 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.4 | 9.66 | 25.81 | 42.51 | 9.00 | 111.7 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.2 | 7.69 | 23.26 | 37.62 | 10.00 | 112.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 5.23 | 14.35 | 24.17 | -2.00 | 90.4 | 46.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.49 | 10.56 | 17.22 | 2.00 | 75.2 | 90.0 |
| Bench 3 | Bench Boost | Tyler Dibling | MID | 17 | 4.5 | 2.12 | 5.54 | 9.08 | 1.00 | 56.7 | 17.0 |

## GW19

- Train rows: 145775
- Bank: 2.10 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 73.29
- Actual score: 81.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.76) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Tyler Dibling -> Ismaïla Sarr (projected gain 4.96, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.76) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Pedro Porro replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.82 | 11.10 | 17.97 | 2.00 | 88.3 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.07 | 0.62 | 0.99 | 0.00 | 9.6 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.22 | 12.67 | 21.00 | 2.00 | 86.8 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 4.10 | 11.70 | 19.11 | 12.00 | 84.5 | 90.0 |
| Bench 2 | Autosub In | Pedro Porro | DEF | 18 | 5.5 | 2.43 | 7.82 | 13.69 | 4.00 | 50.4 | 90.0 |
| XI | XI | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.45 | 7.19 | 11.61 | 0.00 | 79.8 | 90.0 |
| Bench 3 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 1.21 | 3.90 | 6.68 | 0.00 | 46.4 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 7.49 | 20.55 | 32.13 | 7.00 | 82.8 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 5.45 | 15.36 | 25.39 | 1.00 | 96.6 | 45.0 |
| Bench 4 | Bench | Jamie Vardy | FWD | 11 | 5.6 | 1.05 | 4.44 | 7.69 | 2.00 | 20.0 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.5 | 8.76 | 25.42 | 41.28 | 16.00 | 113.9 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.83 | 22.91 | 37.77 | 2.00 | 104.1 | 90.0 |
| XI | XI | Ismaïla Sarr | MID | 7 | 5.9 | 5.00 | 12.61 | 20.10 | 2.00 | 92.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 4.05 | 11.19 | 18.10 | 1.00 | 79.8 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.4 | 2.61 | 8.88 | 15.85 | 0.00 | 44.0 | 0.0 |