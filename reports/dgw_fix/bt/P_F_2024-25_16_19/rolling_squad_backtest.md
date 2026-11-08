# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 255.62
- Total actual points: 254.00
- Average predicted points: 63.90
- Average actual points: 63.50
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
- Predicted score: 60.40
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.71 | 10.80 | 17.33 | 6.00 | 86.9 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.4 | 2.69 | 8.13 | 13.67 | 2.00 | 81.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.25 | 12.38 | 19.13 | 6.00 | 86.1 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.25 | 11.78 | 19.36 | 6.00 | 89.3 | 62.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.1 | 3.33 | 9.69 | 16.60 | 7.00 | 66.9 | 90.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 4.7 | 2.97 | 9.10 | 14.91 | 1.00 | 79.4 | 90.0 |
| XI | XI | Milos Kerkez | DEF | 3 | 4.6 | 3.18 | 8.84 | 14.26 | 2.00 | 73.4 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.72 | 10.74 | 17.42 | 1.00 | 82.0 | 58.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 5.0 | 2.61 | 6.89 | 11.09 | 1.00 | 62.4 | 8.0 |
| Bench 4 | Bench | Will Lankshear | FWD | 18 | 4.5 | 0.48 | 1.11 | 1.77 | 1.00 | 3.6 | 8.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 8.30 | 23.78 | 38.47 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.18 | 22.42 | 38.01 | 5.00 | 88.3 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.19 | 18.51 | 29.34 | 3.00 | 86.5 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 4.06 | 12.01 | 18.98 | 5.00 | 86.1 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 3.90 | 12.00 | 20.70 | 9.00 | 82.6 | 90.0 |

## GW17

- Train rows: 144369
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 57.45
- Actual score: 46.00
- Transfer: Daniel Muñoz -> Lewis Hall (projected gain 2.59, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.67 | 10.77 | 17.40 | 3.00 | 85.4 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.4 | 2.34 | 7.68 | 12.82 | 0.00 | 82.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 3.79 | 11.30 | 17.84 | 2.00 | 78.5 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.1 | 3.61 | 10.66 | 18.17 | 0.00 | 84.1 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.83 | 10.62 | 16.89 | 7.00 | 87.6 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 3.08 | 10.07 | 16.88 | -1.00 | 74.3 | 90.0 |
| Bench 2 | Bench | Milos Kerkez | DEF | 3 | 4.6 | 2.75 | 8.11 | 13.33 | 6.00 | 74.6 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.50 | 9.20 | 15.22 | 2.00 | 69.8 | 90.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 5.0 | 1.58 | 5.03 | 8.69 | 1.00 | 40.5 | 45.0 |
| Bench 4 | Bench | Will Lankshear | FWD | 18 | 4.5 | 0.28 | 1.48 | 2.49 | 0.00 | 8.2 | 0.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 7.41 | 23.19 | 37.10 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.03 | 23.04 | 38.39 | 21.00 | 90.0 | 86.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.17 | 18.79 | 30.66 | 1.00 | 85.1 | 23.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 4.78 | 13.93 | 23.15 | 2.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.18 | 10.57 | 16.44 | 3.00 | 71.8 | 90.0 |

## GW18

- Train rows: 145070
- Bank: 0.10 -> 2.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 68.71
- Actual score: 66.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.54) beats the best remaining Bench Boost opportunity (9.45).
- Transfer: Bukayo Saka -> Bruno Borges Fernandes (projected gain 5.24, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.54) beats the best remaining Bench Boost opportunity (9.45).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 4.10 | 11.38 | 18.38 | 6.00 | 87.7 | 90.0 |
| Bench 1 | Bench Boost | Dean Henderson | GK | 7 | 4.4 | 2.35 | 7.06 | 11.42 | 7.00 | 79.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.57 | 12.97 | 20.90 | 7.00 | 87.2 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.22 | 9.65 | 15.81 | 2.00 | 79.3 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 3.09 | 9.59 | 16.14 | 1.00 | 80.4 | 9.0 |
| XI | XI | Milos Kerkez | DEF | 3 | 4.6 | 3.20 | 8.90 | 14.29 | 6.00 | 81.8 | 90.0 |
| Bench 2 | Bench Boost | Lewis Hall | DEF | 15 | 4.6 | 3.03 | 8.79 | 14.16 | 6.00 | 70.3 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 2.65 | 8.44 | 14.06 | 0.00 | 64.2 | 0.0 |
| Bench 3 | Bench Boost | Cameron Archer | FWD | 17 | 5.0 | 2.14 | 5.76 | 9.64 | 0.00 | 47.9 | 0.0 |
| Bench 4 | Bench Boost | Will Lankshear | FWD | 18 | 4.5 | 0.02 | 0.69 | 1.38 | 0.00 | 2.3 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.4 | 9.64 | 25.95 | 43.10 | 9.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.69 | 23.68 | 38.29 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 4.89 | 14.26 | 23.56 | 3.00 | 89.4 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 5.06 | 13.88 | 23.23 | -2.00 | 87.1 | 46.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.41 | 10.12 | 16.41 | 2.00 | 75.0 | 90.0 |

## GW19

- Train rows: 145775
- Bank: 2.10 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 69.06
- Actual score: 86.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.67) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Cameron Archer -> Matheus Santos Carneiro Da Cunha (projected gain 10.60, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.67) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Pedro Porro replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.85 | 11.21 | 18.30 | 2.00 | 88.0 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.4 | 3.40 | 8.81 | 14.02 | 2.00 | 87.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.26 | 12.70 | 21.10 | 2.00 | 87.6 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 4.04 | 11.41 | 18.85 | 12.00 | 83.5 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.67 | 9.93 | 16.08 | 6.00 | 76.4 | 90.0 |
| XI | XI | Milos Kerkez | DEF | 3 | 4.6 | 2.98 | 8.72 | 14.07 | 1.00 | 81.5 | 90.0 |
| Bench 2 | Autosub In | Pedro Porro | DEF | 18 | 5.5 | 2.53 | 7.87 | 13.98 | 4.00 | 52.5 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 5.35 | 14.74 | 24.65 | 1.00 | 90.0 | 45.0 |
| Bench 3 | Bench | Jamie Vardy | FWD | 11 | 5.6 | 1.31 | 4.77 | 8.16 | 2.00 | 26.4 | 90.0 |
| Bench 4 | Bench | Will Lankshear | FWD | 18 | 4.5 | 0.35 | 1.09 | 1.92 | 0.00 | 4.7 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.5 | 8.67 | 25.47 | 41.67 | 16.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.91 | 23.15 | 38.42 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 4.03 | 13.23 | 21.81 | 7.00 | 85.9 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.96 | 10.65 | 17.45 | 1.00 | 79.2 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.4 | 2.99 | 9.36 | 16.29 | 0.00 | 51.4 | 0.0 |