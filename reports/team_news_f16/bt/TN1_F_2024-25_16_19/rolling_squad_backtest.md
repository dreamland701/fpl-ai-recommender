# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 265.37
- Total actual points: 281.00
- Average predicted points: 66.34
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
- Predicted score: 62.44
- Actual score: 59.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.66 | 10.58 | 17.10 | 6.00 | 85.6 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.30 | 0.64 | 1.15 | 0.00 | 7.6 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.15 | 12.58 | 19.56 | 6.00 | 83.6 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.17 | 11.50 | 19.18 | 6.00 | 87.7 | 62.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.7 | 2.97 | 9.25 | 15.09 | 1.00 | 79.2 | 90.0 |
| Bench 2 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.36 | 6.33 | 10.61 | 0.00 | 71.1 | 90.0 |
| Bench 4 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 2.15 | 6.27 | 10.37 | 2.00 | 70.3 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.6 | 5.99 | 16.68 | 26.77 | 11.00 | 89.1 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.19 | 12.46 | 20.44 | 9.00 | 79.2 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.68 | 11.06 | 17.96 | 1.00 | 81.0 | 58.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 8.13 | 23.63 | 38.18 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.35 | 22.22 | 37.67 | 5.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.13 | 18.62 | 29.74 | 3.00 | 84.8 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.91 | 12.23 | 19.58 | 5.00 | 83.0 | 90.0 |
| Bench 3 | Bench | Tyler Dibling | MID | 17 | 4.5 | 2.17 | 5.69 | 9.23 | 2.00 | 58.9 | 90.0 |

## GW17

- Train rows: 144369
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 60.15
- Actual score: 70.00
- Transfer: Daniel Muñoz -> Lewis Hall (projected gain 4.74, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.75 | 10.81 | 17.32 | 3.00 | 87.3 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.38 | 0.76 | 1.12 | 0.00 | 10.4 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 3.92 | 11.77 | 18.67 | 2.00 | 81.4 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.86 | 10.99 | 17.32 | 7.00 | 88.2 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 3.16 | 9.91 | 16.61 | -1.00 | 77.0 | 90.0 |
| Bench 2 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 2.14 | 6.28 | 10.40 | 0.00 | 73.5 | 90.0 |
| Bench 3 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.13 | 6.12 | 10.15 | 8.00 | 74.4 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.7 | 5.83 | 17.72 | 27.80 | 17.00 | 86.4 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.69 | 12.64 | 21.05 | 9.00 | 80.6 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.62 | 9.89 | 16.29 | 2.00 | 73.0 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 7.34 | 23.20 | 37.01 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.18 | 22.84 | 37.85 | 21.00 | 90.0 | 86.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.26 | 18.84 | 30.59 | 1.00 | 87.2 | 23.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.22 | 11.35 | 17.86 | 3.00 | 73.1 | 90.0 |
| Bench 4 | Bench | Tyler Dibling | MID | 17 | 4.5 | 2.05 | 5.73 | 9.26 | 1.00 | 63.9 | 45.0 |

## GW18

- Train rows: 145070
- Bank: 0.10 -> 2.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 70.73
- Actual score: 71.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.44) beats the best remaining Bench Boost opportunity (7.66).
- Transfer: Bukayo Saka -> Bruno Borges Fernandes (projected gain 7.67, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.44) beats the best remaining Bench Boost opportunity (7.66).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 4.04 | 11.08 | 17.97 | 6.00 | 86.4 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.21 | 0.53 | 0.99 | 0.00 | 8.1 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.53 | 12.81 | 20.74 | 7.00 | 86.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 2.99 | 9.31 | 15.81 | 1.00 | 78.4 | 9.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.05 | 9.29 | 15.14 | 6.00 | 70.8 | 90.0 |
| Bench 2 | Bench Boost | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.48 | 6.62 | 11.03 | 2.00 | 76.6 | 90.0 |
| Bench 4 | Bench Boost | Cameron Burgess | DEF | 10 | 4.0 | 1.72 | 5.95 | 10.07 | 0.00 | 75.6 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 7.20 | 21.03 | 32.97 | 8.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.50 | 12.73 | 21.64 | 12.00 | 80.1 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 2.69 | 8.94 | 15.04 | 0.00 | 65.2 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.4 | 9.68 | 25.68 | 42.47 | 9.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.49 | 23.06 | 37.53 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 5.08 | 14.21 | 24.12 | -2.00 | 87.4 | 46.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.36 | 10.45 | 17.21 | 2.00 | 73.9 | 90.0 |
| Bench 3 | Bench Boost | Tyler Dibling | MID | 17 | 4.5 | 2.03 | 5.44 | 9.08 | 1.00 | 54.6 | 17.0 |

## GW19

- Train rows: 145775
- Bank: 2.10 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 72.06
- Actual score: 81.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.62) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Tyler Dibling -> Ismaïla Sarr (projected gain 5.48, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.62) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Taylor Harwood-Bellis replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.82 | 11.02 | 17.96 | 2.00 | 87.2 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.09 | 0.64 | 1.10 | 0.00 | 10.6 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.27 | 12.59 | 20.99 | 2.00 | 87.5 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.98 | 11.60 | 19.08 | 12.00 | 82.1 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 2.57 | 7.87 | 13.81 | 4.00 | 54.2 | 90.0 |
| Bench 2 | Autosub In | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.40 | 7.09 | 11.58 | 0.00 | 78.0 | 90.0 |
| Bench 3 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 1.19 | 3.88 | 6.73 | 0.00 | 46.2 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 7.04 | 20.39 | 31.99 | 7.00 | 76.4 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 5.34 | 15.26 | 25.34 | 1.00 | 90.0 | 45.0 |
| Bench 4 | Bench | Jamie Vardy | FWD | 11 | 5.6 | 1.06 | 4.47 | 7.78 | 2.00 | 20.8 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.5 | 8.62 | 25.25 | 41.16 | 16.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.78 | 22.77 | 37.71 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ismaïla Sarr | MID | 7 | 5.9 | 4.79 | 12.48 | 20.03 | 2.00 | 88.5 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.92 | 11.11 | 18.08 | 1.00 | 78.3 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.4 | 2.70 | 8.82 | 15.83 | 0.00 | 44.5 | 0.0 |