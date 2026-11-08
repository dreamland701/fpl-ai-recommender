# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 267.33
- Total actual points: 281.00
- Average predicted points: 66.83
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
- Predicted score: 63.42
- Actual score: 59.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.74 | 10.66 | 17.05 | 6.00 | 87.5 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.27 | 0.65 | 1.16 | 0.00 | 6.3 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.23 | 12.70 | 19.61 | 6.00 | 85.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.23 | 11.55 | 19.09 | 6.00 | 88.7 | 62.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.7 | 3.04 | 9.32 | 15.04 | 1.00 | 80.8 | 90.0 |
| Bench 2 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.41 | 6.38 | 10.55 | 0.00 | 72.0 | 90.0 |
| Bench 4 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 2.21 | 6.35 | 10.35 | 2.00 | 71.4 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.6 | 6.08 | 16.81 | 26.81 | 11.00 | 90.0 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.28 | 12.55 | 20.40 | 9.00 | 81.3 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.76 | 11.20 | 18.03 | 1.00 | 83.0 | 58.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 8.22 | 23.77 | 38.23 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.41 | 22.30 | 37.63 | 5.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.22 | 18.75 | 29.79 | 3.00 | 87.2 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.99 | 12.36 | 19.64 | 5.00 | 84.5 | 90.0 |
| Bench 3 | Bench | Tyler Dibling | MID | 17 | 4.5 | 2.22 | 5.74 | 9.16 | 2.00 | 59.6 | 90.0 |

## GW17

- Train rows: 144369
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 59.58
- Actual score: 70.00
- Transfer: Daniel Muñoz -> Lewis Hall (projected gain 4.80, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.70 | 10.67 | 17.15 | 3.00 | 86.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.24 | 0.60 | 1.07 | 0.00 | 6.3 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 3.87 | 11.68 | 18.59 | 2.00 | 80.2 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.81 | 10.94 | 17.32 | 7.00 | 87.2 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 3.05 | 9.71 | 16.39 | -1.00 | 73.8 | 90.0 |
| Bench 2 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 2.08 | 6.18 | 10.30 | 0.00 | 71.8 | 90.0 |
| Bench 3 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.07 | 6.01 | 10.04 | 8.00 | 72.5 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.7 | 5.79 | 17.68 | 27.81 | 17.00 | 85.5 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.64 | 12.51 | 20.86 | 9.00 | 79.4 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.55 | 9.76 | 16.15 | 2.00 | 71.0 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 7.33 | 23.19 | 37.02 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.13 | 22.73 | 37.71 | 21.00 | 90.0 | 86.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.21 | 18.74 | 30.46 | 1.00 | 86.2 | 23.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.17 | 11.27 | 17.79 | 3.00 | 71.6 | 90.0 |
| Bench 4 | Bench | Tyler Dibling | MID | 17 | 4.5 | 1.97 | 5.59 | 9.12 | 1.00 | 61.6 | 45.0 |

## GW18

- Train rows: 145070
- Bank: 0.10 -> 2.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 71.76
- Actual score: 71.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.63) beats the best remaining Bench Boost opportunity (7.89).
- Transfer: Bukayo Saka -> Bruno Borges Fernandes (projected gain 7.71, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.63) beats the best remaining Bench Boost opportunity (7.89).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 4.11 | 11.17 | 17.90 | 6.00 | 88.1 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.19 | 0.56 | 1.00 | 0.00 | 6.7 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.62 | 12.91 | 20.68 | 7.00 | 88.3 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 3.05 | 9.38 | 15.71 | 1.00 | 79.3 | 9.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.12 | 9.36 | 15.05 | 6.00 | 72.1 | 90.0 |
| Bench 2 | Bench Boost | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.56 | 6.73 | 11.00 | 2.00 | 78.3 | 90.0 |
| Bench 4 | Bench Boost | Cameron Burgess | DEF | 10 | 4.0 | 1.80 | 6.08 | 10.08 | 0.00 | 77.5 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 7.27 | 21.20 | 33.13 | 8.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.58 | 12.80 | 21.52 | 12.00 | 81.9 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 2.75 | 9.02 | 14.97 | 0.00 | 66.3 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.4 | 9.73 | 25.80 | 42.51 | 9.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.58 | 23.22 | 37.56 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 5.17 | 14.35 | 24.14 | -2.00 | 89.4 | 46.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.42 | 10.54 | 17.18 | 2.00 | 75.1 | 90.0 |
| Bench 3 | Bench Boost | Tyler Dibling | MID | 17 | 4.5 | 2.08 | 5.49 | 8.97 | 1.00 | 55.6 | 17.0 |

## GW19

- Train rows: 145775
- Bank: 2.10 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 72.57
- Actual score: 81.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.70) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Tyler Dibling -> Ismaïla Sarr (projected gain 4.72, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.70) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.89 | 11.06 | 17.85 | 2.00 | 88.9 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.07 | 0.65 | 1.12 | 0.00 | 9.2 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.33 | 12.62 | 20.85 | 2.00 | 89.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 4.05 | 11.65 | 18.99 | 12.00 | 83.8 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 2.56 | 7.79 | 13.55 | 4.00 | 53.0 | 90.0 |
| XI | XI | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.47 | 7.17 | 11.55 | 0.00 | 79.7 | 90.0 |
| Bench 3 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 1.22 | 3.86 | 6.55 | 0.00 | 46.4 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 7.09 | 20.46 | 31.98 | 7.00 | 77.6 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 5.43 | 15.33 | 25.26 | 1.00 | 90.0 | 45.0 |
| Bench 4 | Bench | Jamie Vardy | FWD | 11 | 5.6 | 1.13 | 5.03 | 8.87 | 2.00 | 22.3 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.5 | 8.70 | 25.39 | 41.24 | 16.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.83 | 22.83 | 37.63 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ismaïla Sarr | MID | 7 | 5.9 | 4.87 | 12.61 | 20.10 | 2.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.97 | 11.18 | 18.07 | 1.00 | 79.3 | 90.0 |
| Bench 2 | Bench | Bruno Borges Fernandes | MID | 14 | 8.4 | 2.34 | 8.35 | 15.66 | 0.00 | 36.9 | 0.0 |