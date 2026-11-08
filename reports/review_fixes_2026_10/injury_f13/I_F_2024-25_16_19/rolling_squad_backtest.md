# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 256.60
- Total actual points: 254.00
- Average predicted points: 64.15
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
- Predicted score: 61.07
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.75 | 10.70 | 17.16 | 6.00 | 88.3 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.4 | 2.70 | 8.14 | 13.61 | 2.00 | 82.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.50 | 12.76 | 19.72 | 6.00 | 90.8 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.18 | 11.70 | 19.40 | 6.00 | 87.0 | 62.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.1 | 3.17 | 9.60 | 16.10 | 7.00 | 64.8 | 90.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 4.7 | 3.03 | 9.17 | 14.81 | 1.00 | 79.9 | 90.0 |
| XI | XI | Milos Kerkez | DEF | 3 | 4.6 | 3.23 | 9.04 | 14.48 | 2.00 | 73.5 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.74 | 11.10 | 17.90 | 1.00 | 82.7 | 58.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 5.0 | 2.66 | 7.01 | 11.28 | 1.00 | 63.0 | 8.0 |
| Bench 4 | Bench | Will Lankshear | FWD | 18 | 4.5 | 0.50 | 1.11 | 1.89 | 1.00 | 3.3 | 8.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 8.47 | 24.03 | 38.58 | 3.00 | 115.7 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.26 | 21.91 | 37.07 | 5.00 | 91.2 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.24 | 18.62 | 29.67 | 3.00 | 90.7 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 4.28 | 12.55 | 19.94 | 5.00 | 88.1 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 3.79 | 12.29 | 21.33 | 9.00 | 81.5 | 90.0 |

## GW17

- Train rows: 144369
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 57.88
- Actual score: 46.00
- Transfer: Daniel Muñoz -> Lewis Hall (projected gain 2.89, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.70 | 10.72 | 17.29 | 3.00 | 86.3 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.4 | 2.34 | 7.62 | 12.84 | 0.00 | 83.3 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 3.91 | 11.51 | 18.39 | 2.00 | 81.1 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 4.00 | 10.96 | 17.35 | 7.00 | 91.2 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.1 | 3.62 | 10.87 | 18.13 | 0.00 | 85.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 2.90 | 9.85 | 16.68 | -1.00 | 70.2 | 90.0 |
| Bench 2 | Bench | Milos Kerkez | DEF | 3 | 4.6 | 2.75 | 8.16 | 13.61 | 6.00 | 73.8 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.57 | 9.66 | 16.09 | 2.00 | 70.8 | 90.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 5.0 | 1.60 | 5.07 | 8.74 | 1.00 | 40.4 | 45.0 |
| Bench 4 | Bench | Will Lankshear | FWD | 18 | 4.5 | 0.28 | 1.57 | 2.72 | 0.00 | 7.5 | 0.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 7.57 | 23.46 | 37.35 | 3.00 | 106.2 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 6.87 | 22.59 | 37.54 | 21.00 | 93.2 | 86.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.12 | 18.62 | 30.40 | 1.00 | 86.6 | 23.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 4.74 | 14.05 | 23.51 | 2.00 | 93.2 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.30 | 11.32 | 17.87 | 3.00 | 71.9 | 90.0 |

## GW18

- Train rows: 145070
- Bank: 0.10 -> 2.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 68.52
- Actual score: 66.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.40) beats the best remaining Bench Boost opportunity (9.41).
- Transfer: Bukayo Saka -> Bruno Borges Fernandes (projected gain 4.73, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.40) beats the best remaining Bench Boost opportunity (9.41).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 4.09 | 11.23 | 18.07 | 6.00 | 88.1 | 90.0 |
| Bench 1 | Bench Boost | Dean Henderson | GK | 7 | 4.4 | 2.31 | 6.92 | 11.38 | 7.00 | 78.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.56 | 12.84 | 20.67 | 7.00 | 87.4 | 90.0 |
| Bench 2 | Bench Boost | Pedro Porro | DEF | 18 | 5.5 | 2.97 | 9.59 | 16.11 | 1.00 | 78.0 | 9.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.15 | 9.49 | 15.57 | 2.00 | 78.6 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.11 | 9.20 | 14.84 | 6.00 | 72.0 | 90.0 |
| XI | XI | Milos Kerkez | DEF | 3 | 4.6 | 3.19 | 9.04 | 14.62 | 6.00 | 80.3 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 2.59 | 8.82 | 14.75 | 0.00 | 62.7 | 0.0 |
| Bench 3 | Bench Boost | Cameron Archer | FWD | 17 | 5.0 | 2.11 | 5.84 | 9.84 | 0.00 | 47.3 | 0.0 |
| Bench 4 | Bench Boost | Will Lankshear | FWD | 18 | 4.5 | 0.01 | 0.84 | 1.50 | 0.00 | 1.6 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.4 | 9.57 | 25.66 | 42.30 | 9.00 | 109.4 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.81 | 23.53 | 37.95 | 10.00 | 113.8 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 4.85 | 14.25 | 23.66 | 3.00 | 90.1 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 5.13 | 14.10 | 23.82 | -2.00 | 88.9 | 46.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.48 | 10.57 | 17.25 | 2.00 | 74.6 | 90.0 |

## GW19

- Train rows: 145775
- Bank: 2.10 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 69.13
- Actual score: 86.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.74) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Cameron Archer -> Matheus Santos Carneiro Da Cunha (projected gain 10.78, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.74) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Pedro Porro replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.80 | 11.09 | 17.96 | 2.00 | 87.5 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.4 | 3.40 | 8.81 | 13.98 | 2.00 | 87.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.16 | 12.52 | 20.78 | 2.00 | 86.1 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 4.10 | 11.68 | 19.07 | 12.00 | 84.7 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.66 | 10.07 | 16.27 | 6.00 | 75.6 | 90.0 |
| XI | XI | Milos Kerkez | DEF | 3 | 4.6 | 3.00 | 8.96 | 14.39 | 1.00 | 80.9 | 90.0 |
| Bench 2 | Autosub In | Pedro Porro | DEF | 18 | 5.5 | 2.43 | 7.87 | 13.80 | 4.00 | 50.1 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 5.38 | 15.19 | 25.14 | 1.00 | 95.7 | 45.0 |
| Bench 3 | Bench | Jamie Vardy | FWD | 11 | 5.6 | 1.29 | 5.05 | 8.65 | 2.00 | 25.8 | 90.0 |
| Bench 4 | Bench | Will Lankshear | FWD | 18 | 4.5 | 0.36 | 1.19 | 1.95 | 0.00 | 4.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.5 | 8.74 | 25.42 | 41.29 | 16.00 | 113.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.92 | 23.09 | 37.98 | 2.00 | 105.1 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 4.00 | 13.37 | 21.94 | 7.00 | 86.7 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 4.04 | 11.19 | 18.12 | 1.00 | 79.1 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.4 | 2.84 | 9.45 | 16.75 | 0.00 | 49.9 | 0.0 |