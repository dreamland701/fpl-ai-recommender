# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 257.90
- Total actual points: 254.00
- Average predicted points: 64.48
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
- Predicted score: 61.83
- Actual score: 55.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.91 | 10.99 | 17.55 | 6.00 | 91.2 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.4 | 2.76 | 8.33 | 13.82 | 2.00 | 84.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.80 | 13.17 | 20.32 | 6.00 | 92.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.13 | 11.85 | 19.50 | 6.00 | 89.2 | 62.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.1 | 3.25 | 9.72 | 16.34 | 7.00 | 66.6 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.7 | 3.06 | 9.28 | 14.99 | 1.00 | 81.7 | 90.0 |
| Bench 2 | Bench | Leif Davis | DEF | 10 | 4.5 | 2.96 | 8.42 | 13.92 | 2.00 | 81.8 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.58 | 10.69 | 17.30 | 1.00 | 82.0 | 58.0 |
| Bench 3 | Bench | Adam Armstrong | FWD | 17 | 5.1 | 2.52 | 7.13 | 11.83 | 2.00 | 65.9 | 81.0 |
| Bench 4 | Bench | Will Lankshear | FWD | 18 | 4.5 | 0.54 | 1.19 | 1.95 | 1.00 | 4.2 | 8.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 8.44 | 23.68 | 38.25 | 3.00 | 116.2 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.54 | 22.61 | 37.93 | 5.00 | 94.1 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.62 | 19.10 | 30.38 | 3.00 | 93.3 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 3.83 | 12.26 | 21.26 | 9.00 | 79.4 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 4.22 | 12.25 | 19.51 | 5.00 | 87.0 | 90.0 |

## GW17

- Train rows: 144369
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 60.57
- Actual score: 46.00
- Transfer: Daniel Muñoz -> Lewis Hall (projected gain 3.14, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.87 | 11.09 | 17.76 | 3.00 | 89.0 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.4 | 2.54 | 8.04 | 13.36 | 0.00 | 85.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.18 | 12.19 | 19.23 | 2.00 | 82.5 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.1 | 3.71 | 11.28 | 18.69 | 0.00 | 86.9 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 4.15 | 11.16 | 17.65 | 7.00 | 92.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 2.96 | 9.87 | 16.65 | -1.00 | 71.0 | 90.0 |
| Bench 2 | Bench | Leif Davis | DEF | 10 | 4.5 | 2.81 | 8.06 | 13.41 | 0.00 | 79.4 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.29 | 9.40 | 15.51 | 2.00 | 69.2 | 90.0 |
| Bench 3 | Bench | Adam Armstrong | FWD | 17 | 5.1 | 2.16 | 6.97 | 11.78 | 2.00 | 64.0 | 90.0 |
| Bench 4 | Bench | Will Lankshear | FWD | 18 | 4.5 | 0.27 | 1.56 | 2.68 | 0.00 | 8.0 | 0.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 8.18 | 23.63 | 38.07 | 3.00 | 111.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.21 | 22.53 | 37.66 | 21.00 | 95.9 | 86.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.40 | 18.96 | 30.83 | 1.00 | 88.2 | 23.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 4.75 | 14.11 | 23.57 | 2.00 | 94.3 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.68 | 11.37 | 18.12 | 3.00 | 73.8 | 90.0 |

## GW18

- Train rows: 145070
- Bank: 0.10 -> 2.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 67.58
- Actual score: 63.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.00) beats the best remaining Bench Boost opportunity (8.80).
- Transfer: Bukayo Saka -> Bruno Borges Fernandes (projected gain 6.28, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.00) beats the best remaining Bench Boost opportunity (8.80).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 4.15 | 11.33 | 18.22 | 6.00 | 90.7 | 90.0 |
| Bench 1 | Bench Boost | Dean Henderson | GK | 7 | 4.4 | 2.35 | 6.95 | 11.43 | 7.00 | 78.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.60 | 12.88 | 20.73 | 7.00 | 89.6 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.39 | 10.00 | 16.43 | 2.00 | 82.7 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 3.01 | 9.55 | 16.11 | 1.00 | 78.5 | 9.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.22 | 9.44 | 15.19 | 6.00 | 71.4 | 90.0 |
| Bench 3 | Bench Boost | Leif Davis | DEF | 10 | 4.5 | 2.24 | 7.38 | 12.36 | 1.00 | 79.5 | 90.0 |
| Bench 2 | Bench Boost | Jamie Vardy | FWD | 11 | 5.6 | 2.41 | 8.32 | 13.98 | 0.00 | 60.0 | 0.0 |
| XI | XI | Adam Armstrong | FWD | 17 | 5.1 | 2.84 | 7.76 | 12.47 | 2.00 | 73.7 | 72.0 |
| Bench 4 | Bench Boost | Will Lankshear | FWD | 18 | 4.5 | 0.00 | 0.68 | 1.34 | 0.00 | 1.7 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.4 | 8.84 | 25.17 | 41.24 | 9.00 | 109.1 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 8.28 | 23.91 | 38.84 | 10.00 | 117.8 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.89 | 14.46 | 24.07 | -2.00 | 87.8 | 46.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 4.78 | 14.20 | 23.51 | 3.00 | 90.1 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.74 | 10.80 | 17.67 | 2.00 | 76.9 | 90.0 |

## GW19

- Train rows: 145775
- Bank: 2.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 67.92
- Actual score: 90.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.89) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Adam Armstrong -> Matheus Santos Carneiro Da Cunha (projected gain 7.13, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.89) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Leif Davis replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.86 | 11.17 | 18.17 | 2.00 | 89.8 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.4 | 3.38 | 8.75 | 14.01 | 2.00 | 88.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.18 | 12.66 | 21.04 | 2.00 | 87.3 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.80 | 11.14 | 18.29 | 12.00 | 82.1 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.47 | 9.70 | 15.77 | 6.00 | 74.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 2.38 | 7.63 | 13.48 | 4.00 | 48.6 | 90.0 |
| Bench 2 | Autosub In | Leif Davis | DEF | 10 | 4.5 | 2.37 | 7.07 | 11.50 | 5.00 | 77.3 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.93 | 14.38 | 23.95 | 1.00 | 92.0 | 45.0 |
| Bench 3 | Bench | Jamie Vardy | FWD | 11 | 5.6 | 1.30 | 4.87 | 8.46 | 2.00 | 24.5 | 90.0 |
| Bench 4 | Bench | Will Lankshear | FWD | 18 | 4.5 | 0.25 | 0.82 | 1.49 | 0.00 | 2.2 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.5 | 8.89 | 25.60 | 41.66 | 16.00 | 112.1 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.76 | 22.92 | 37.81 | 2.00 | 105.5 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 4.33 | 13.57 | 22.42 | 7.00 | 87.4 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.94 | 10.99 | 17.85 | 1.00 | 79.0 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.4 | 2.62 | 9.34 | 16.56 | 0.00 | 44.8 | 0.0 |