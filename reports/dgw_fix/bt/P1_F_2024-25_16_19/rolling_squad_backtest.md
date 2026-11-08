# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 255.03
- Total actual points: 261.00
- Average predicted points: 63.76
- Average actual points: 65.25
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
- Predicted score: 60.21
- Actual score: 49.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.71 | 10.66 | 17.07 | 6.00 | 86.9 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 4.7 | 2.88 | 8.14 | 13.62 | 2.00 | 87.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.25 | 12.76 | 19.68 | 6.00 | 86.1 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.25 | 11.65 | 19.31 | 6.00 | 89.3 | 62.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.1 | 3.33 | 9.62 | 16.15 | 7.00 | 66.9 | 90.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 4.7 | 2.97 | 9.21 | 14.90 | 1.00 | 79.4 | 90.0 |
| XI | XI | Milos Kerkez | DEF | 3 | 4.6 | 3.18 | 9.01 | 14.43 | 2.00 | 73.4 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.72 | 11.10 | 17.86 | 1.00 | 82.0 | 58.0 |
| Bench 4 | Bench | Raúl Jiménez | FWD | 9 | 5.5 | 2.16 | 7.46 | 12.81 | 2.00 | 56.4 | 67.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 5.0 | 2.61 | 7.04 | 11.37 | 1.00 | 62.4 | 8.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 8.30 | 23.99 | 38.56 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.18 | 21.85 | 36.96 | 5.00 | 88.3 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.19 | 18.69 | 29.69 | 3.00 | 86.5 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 4.06 | 12.51 | 19.86 | 5.00 | 86.1 | 90.0 |
| XI | XI | Bernardo Veiga de Carvalho e Silva | MID | 13 | 6.3 | 3.71 | 10.77 | 17.43 | 2.00 | 80.0 | 90.0 |

## GW17

- Train rows: 144369
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 56.03
- Actual score: 47.00
- Transfer: Daniel Muñoz -> Lewis Hall (projected gain 1.23, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.67 | 10.68 | 17.22 | 3.00 | 85.4 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 4.7 | 2.53 | 7.52 | 12.45 | 7.00 | 82.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 3.79 | 11.52 | 18.37 | 2.00 | 78.5 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.83 | 10.96 | 17.33 | 7.00 | 87.6 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.1 | 3.61 | 10.89 | 18.19 | 0.00 | 84.1 | 90.0 |
| Bench 2 | Bench | Pedro Porro | DEF | 18 | 5.6 | 3.08 | 9.80 | 16.57 | -1.00 | 74.3 | 90.0 |
| Bench 3 | Bench | Milos Kerkez | DEF | 3 | 4.6 | 2.75 | 8.12 | 13.56 | 6.00 | 74.6 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.50 | 9.67 | 16.06 | 2.00 | 69.8 | 90.0 |
| XI | XI | Raúl Jiménez | FWD | 9 | 5.5 | 3.20 | 8.11 | 13.57 | 0.00 | 56.9 | 28.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 5.0 | 1.58 | 5.10 | 8.82 | 1.00 | 40.5 | 45.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 7.41 | 23.40 | 37.35 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.03 | 22.53 | 37.45 | 21.00 | 90.0 | 86.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.17 | 18.69 | 30.43 | 1.00 | 85.1 | 23.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.18 | 11.27 | 17.80 | 3.00 | 71.8 | 90.0 |
| XI | XI | Bernardo Veiga de Carvalho e Silva | MID | 13 | 6.3 | 3.24 | 10.00 | 16.57 | 2.00 | 79.4 | 90.0 |

## GW18

- Train rows: 145070
- Bank: 0.10 -> 2.90
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 68.80
- Actual score: 80.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.66) beats the best remaining Bench Boost opportunity (11.58).
- Transfer: Bukayo Saka -> Bryan Mbeumo (projected gain 4.96, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.66) beats the best remaining Bench Boost opportunity (11.58).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 4.10 | 11.19 | 17.99 | 6.00 | 87.7 | 90.0 |
| Bench 1 | Bench Boost | Matz Sels | GK | 16 | 4.7 | 3.16 | 8.67 | 13.95 | 8.00 | 83.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.57 | 12.86 | 20.66 | 7.00 | 87.2 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 3.09 | 9.54 | 16.01 | 1.00 | 80.4 | 9.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.22 | 9.51 | 15.63 | 2.00 | 79.3 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.03 | 9.20 | 14.84 | 6.00 | 70.3 | 90.0 |
| XI | XI | Milos Kerkez | DEF | 3 | 4.6 | 3.20 | 9.01 | 14.57 | 6.00 | 81.8 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 2.65 | 8.82 | 14.72 | 0.00 | 64.2 | 0.0 |
| Bench 3 | Bench Boost | Cameron Archer | FWD | 17 | 5.0 | 2.14 | 5.87 | 9.91 | 0.00 | 47.9 | 0.0 |
| Bench 4 | Bench Boost | Raúl Jiménez | FWD | 9 | 5.5 | 1.43 | 5.22 | 9.01 | 2.00 | 36.8 | 73.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.4 | 9.64 | 25.60 | 42.19 | 9.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.69 | 23.48 | 37.95 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 4.89 | 14.28 | 23.66 | 3.00 | 89.4 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.41 | 10.54 | 17.19 | 2.00 | 75.0 | 90.0 |
| Bench 2 | Bench Boost | Bernardo Veiga de Carvalho e Silva | MID | 13 | 6.3 | 2.94 | 9.46 | 15.46 | 9.00 | 75.4 | 90.0 |

## GW19

- Train rows: 145775
- Bank: 2.90 -> 0.80
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 69.98
- Actual score: 85.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.67) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Cameron Archer -> Matheus Santos Carneiro Da Cunha (projected gain 8.03, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.67) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.85 | 11.05 | 17.89 | 2.00 | 88.0 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 4.7 | 2.94 | 8.87 | 14.38 | 6.00 | 88.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.26 | 12.54 | 20.79 | 2.00 | 87.6 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 4.04 | 11.68 | 19.07 | 12.00 | 83.5 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.67 | 10.09 | 16.33 | 6.00 | 76.4 | 90.0 |
| XI | XI | Milos Kerkez | DEF | 3 | 4.6 | 2.98 | 8.93 | 14.35 | 1.00 | 81.5 | 90.0 |
| Bench 2 | Bench | Pedro Porro | DEF | 18 | 5.5 | 2.53 | 7.82 | 13.68 | 4.00 | 52.5 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 5.35 | 15.22 | 25.17 | 1.00 | 90.0 | 45.0 |
| Bench 3 | Bench | Raúl Jiménez | FWD | 9 | 5.5 | 2.47 | 7.26 | 11.40 | 9.00 | 54.3 | 67.0 |
| Bench 4 | Bench | Jamie Vardy | FWD | 11 | 5.6 | 1.31 | 5.05 | 8.62 | 2.00 | 26.4 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.5 | 8.67 | 25.37 | 41.18 | 16.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.91 | 23.04 | 37.97 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 4.03 | 13.40 | 21.97 | 7.00 | 85.9 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.96 | 11.16 | 18.06 | 1.00 | 79.2 | 90.0 |
| XI | XI | Bernardo Veiga de Carvalho e Silva | MID | 13 | 6.3 | 3.91 | 10.52 | 17.19 | 3.00 | 79.4 | 90.0 |