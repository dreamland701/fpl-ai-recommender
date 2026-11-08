# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 267.56
- Total actual points: 281.00
- Average predicted points: 66.89
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
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.74 | 10.69 | 17.10 | 6.00 | 87.2 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.28 | 0.56 | 0.94 | 0.00 | 6.4 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.25 | 12.76 | 19.67 | 6.00 | 85.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.19 | 11.49 | 19.03 | 6.00 | 87.9 | 62.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.7 | 3.03 | 9.31 | 15.02 | 1.00 | 80.4 | 90.0 |
| Bench 2 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.41 | 6.46 | 10.77 | 0.00 | 72.5 | 90.0 |
| Bench 3 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 2.20 | 6.33 | 10.35 | 2.00 | 71.2 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.6 | 6.06 | 16.75 | 26.73 | 11.00 | 90.0 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.24 | 12.53 | 20.42 | 9.00 | 80.6 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.79 | 11.24 | 18.06 | 1.00 | 83.0 | 58.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 8.27 | 23.93 | 38.49 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.36 | 22.19 | 37.47 | 5.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.27 | 18.90 | 30.03 | 3.00 | 87.7 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.99 | 12.33 | 19.57 | 5.00 | 85.0 | 90.0 |
| Bench 4 | Bench | Tyler Dibling | MID | 17 | 4.5 | 2.20 | 5.70 | 9.11 | 2.00 | 59.1 | 90.0 |

## GW17

- Train rows: 144369
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 59.67
- Actual score: 70.00
- Transfer: Daniel Muñoz -> Lewis Hall (projected gain 4.82, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.70 | 10.72 | 17.24 | 3.00 | 85.5 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.24 | 0.51 | 0.84 | 0.00 | 6.4 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 3.90 | 11.79 | 18.76 | 2.00 | 80.2 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.83 | 10.95 | 17.32 | 7.00 | 87.2 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 3.03 | 9.69 | 16.36 | -1.00 | 73.2 | 90.0 |
| Bench 2 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 2.06 | 6.16 | 10.30 | 0.00 | 71.5 | 90.0 |
| Bench 3 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.06 | 6.07 | 10.22 | 8.00 | 72.9 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.7 | 5.79 | 17.65 | 27.75 | 17.00 | 86.1 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.61 | 12.50 | 20.94 | 9.00 | 78.8 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.56 | 9.83 | 16.27 | 2.00 | 70.7 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 7.38 | 23.34 | 37.30 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.09 | 22.64 | 37.60 | 21.00 | 90.0 | 86.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.24 | 18.87 | 30.74 | 1.00 | 86.3 | 23.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.17 | 11.28 | 17.82 | 3.00 | 72.0 | 90.0 |
| Bench 4 | Bench | Tyler Dibling | MID | 17 | 4.5 | 1.95 | 5.56 | 9.08 | 1.00 | 61.2 | 45.0 |

## GW18

- Train rows: 145070
- Bank: 0.10 -> 2.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 71.69
- Actual score: 71.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.62) beats the best remaining Bench Boost opportunity (7.88).
- Transfer: Bukayo Saka -> Bruno Borges Fernandes (projected gain 7.75, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.62) beats the best remaining Bench Boost opportunity (7.88).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 4.10 | 11.17 | 17.93 | 6.00 | 87.5 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.19 | 0.47 | 0.76 | 0.00 | 6.8 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.62 | 12.94 | 20.76 | 7.00 | 87.8 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.13 | 9.45 | 15.22 | 6.00 | 72.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 3.01 | 9.32 | 15.64 | 1.00 | 78.4 | 9.0 |
| Bench 2 | Bench Boost | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.57 | 6.82 | 11.22 | 2.00 | 78.9 | 90.0 |
| Bench 4 | Bench Boost | Cameron Burgess | DEF | 10 | 4.0 | 1.79 | 6.07 | 10.07 | 0.00 | 77.4 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 7.27 | 21.13 | 32.95 | 8.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.55 | 12.80 | 21.61 | 12.00 | 81.2 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 2.75 | 9.05 | 15.05 | 0.00 | 65.9 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.4 | 9.70 | 25.69 | 42.31 | 9.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.63 | 23.36 | 37.80 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 5.20 | 14.48 | 24.37 | -2.00 | 89.1 | 46.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.41 | 10.53 | 17.17 | 2.00 | 75.1 | 90.0 |
| Bench 3 | Bench Boost | Tyler Dibling | MID | 17 | 4.5 | 2.07 | 5.50 | 9.02 | 1.00 | 55.4 | 17.0 |

## GW19

- Train rows: 145775
- Bank: 2.10 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 72.72
- Actual score: 81.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.67) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Tyler Dibling -> Ismaïla Sarr (projected gain 5.34, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.67) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Taylor Harwood-Bellis replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.88 | 11.09 | 17.93 | 2.00 | 88.3 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.07 | 0.56 | 0.88 | 0.00 | 9.3 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.33 | 12.68 | 20.99 | 2.00 | 88.6 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 4.04 | 11.69 | 19.09 | 12.00 | 83.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 2.52 | 7.78 | 13.60 | 4.00 | 52.3 | 90.0 |
| Bench 2 | Autosub In | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.48 | 7.25 | 11.76 | 0.00 | 80.2 | 90.0 |
| Bench 3 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 1.20 | 3.90 | 6.69 | 0.00 | 46.1 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 7.09 | 20.50 | 32.06 | 7.00 | 78.3 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 5.39 | 15.33 | 25.33 | 1.00 | 90.0 | 45.0 |
| Bench 4 | Bench | Jamie Vardy | FWD | 11 | 5.6 | 1.05 | 4.45 | 7.69 | 2.00 | 20.3 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.5 | 8.67 | 25.28 | 41.05 | 16.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.89 | 23.02 | 37.98 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ismaïla Sarr | MID | 7 | 5.9 | 4.82 | 12.48 | 19.91 | 2.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.95 | 11.15 | 18.05 | 1.00 | 79.4 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.4 | 2.79 | 9.06 | 16.15 | 0.00 | 45.5 | 0.0 |