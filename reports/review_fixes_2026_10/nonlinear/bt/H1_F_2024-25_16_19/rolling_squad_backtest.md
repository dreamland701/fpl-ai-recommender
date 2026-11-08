# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 253.69
- Total actual points: 254.00
- Average predicted points: 63.42
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
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 62.01
- Actual score: 47.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.93 | 10.66 | 17.07 | 6.00 | 88.5 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.4 | 3.37 | 8.13 | 13.59 | 2.00 | 88.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.09 | 12.76 | 19.68 | 6.00 | 86.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 3.90 | 11.65 | 19.31 | 6.00 | 84.7 | 62.0 |
| Bench 2 | Bench | Joško Gvardiol | DEF | 13 | 6.1 | 3.21 | 9.62 | 16.15 | 7.00 | 71.4 | 90.0 |
| Bench 3 | Bench | Daniel Muñoz | DEF | 7 | 4.7 | 3.09 | 9.21 | 14.90 | 1.00 | 84.6 | 90.0 |
| XI | XI | Milos Kerkez | DEF | 3 | 4.6 | 3.75 | 9.01 | 14.43 | 2.00 | 82.1 | 90.0 |
| Bench 4 | Bench | Jamie Vardy | FWD | 11 | 5.6 | 3.01 | 11.10 | 17.86 | 1.00 | 79.2 | 58.0 |
| XI | XI | Jørgen Strand Larsen | FWD | 20 | 5.7 | 3.65 | 8.46 | 13.98 | 2.00 | 69.6 | 90.0 |
| XI | XI | Adam Armstrong | FWD | 17 | 5.1 | 3.60 | 7.06 | 11.78 | 2.00 | 74.6 | 81.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.1 | 7.20 | 23.99 | 38.56 | 3.00 | 84.2 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.4 | 8.25 | 21.85 | 36.96 | 5.00 | 92.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 10.6 | 7.91 | 18.69 | 29.69 | 3.00 | 83.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.73 | 12.51 | 19.86 | 5.00 | 80.9 | 90.0 |
| XI | XI | Bernardo Veiga de Carvalho e Silva | MID | 13 | 6.3 | 3.73 | 10.77 | 17.43 | 2.00 | 80.6 | 90.0 |

## GW17

- Train rows: 144369
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Bukayo Saka
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 59.45
- Actual score: 49.00
- Transfer: Daniel Muñoz -> Lewis Hall (projected gain 2.90, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.89 | 10.68 | 17.22 | 3.00 | 90.1 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.4 | 2.74 | 7.62 | 12.82 | 0.00 | 88.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.75 | 11.52 | 18.37 | 2.00 | 87.1 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.74 | 10.96 | 17.33 | 7.00 | 86.4 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.1 | 3.79 | 10.89 | 18.19 | 0.00 | 84.0 | 90.0 |
| Bench 4 | Bench | Pedro Porro | DEF | 18 | 5.6 | 2.17 | 9.80 | 16.57 | -1.00 | 65.4 | 90.0 |
| Bench 2 | Bench | Milos Kerkez | DEF | 3 | 4.6 | 3.11 | 8.12 | 13.56 | 6.00 | 84.8 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 4.00 | 9.67 | 16.06 | 2.00 | 70.0 | 90.0 |
| XI | XI | Jørgen Strand Larsen | FWD | 20 | 5.7 | 3.79 | 8.60 | 13.78 | 2.00 | 73.1 | 83.0 |
| Bench 3 | Bench | Adam Armstrong | FWD | 17 | 5.1 | 2.98 | 6.93 | 11.80 | 2.00 | 71.8 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 7.56 | 23.40 | 37.35 | 3.00 | 80.9 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.4 | 6.34 | 22.53 | 37.45 | 21.00 | 83.8 | 86.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 10.6 | 7.11 | 18.69 | 30.43 | 1.00 | 86.7 | 23.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.71 | 11.27 | 17.80 | 3.00 | 75.5 | 90.0 |
| XI | XI | Bernardo Veiga de Carvalho e Silva | MID | 13 | 6.3 | 3.22 | 10.00 | 16.57 | 2.00 | 84.0 | 90.0 |

## GW18

- Train rows: 145070
- Bank: 0.10 -> 2.90
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 64.28
- Actual score: 76.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.63) beats the best remaining Triple Captain opportunity (9.69).
- Transfer: Bukayo Saka -> Bryan Mbeumo (projected gain 9.32, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.63) beats the best remaining Triple Captain opportunity (9.69).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 4.22 | 11.19 | 17.99 | 6.00 | 87.2 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.4 | 3.02 | 6.92 | 11.37 | 7.00 | 87.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.23 | 12.86 | 20.66 | 7.00 | 83.6 | 90.0 |
| Bench 3 | Bench | Pedro Porro | DEF | 18 | 5.5 | 2.75 | 9.54 | 16.01 | 1.00 | 74.2 | 9.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.41 | 9.51 | 15.63 | 2.00 | 78.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.53 | 9.20 | 14.84 | 6.00 | 84.8 | 90.0 |
| Bench 2 | Bench | Milos Kerkez | DEF | 3 | 4.6 | 2.95 | 9.01 | 14.57 | 6.00 | 84.4 | 90.0 |
| Bench 4 | Bench | Jamie Vardy | FWD | 11 | 5.6 | 2.22 | 8.82 | 14.72 | 0.00 | 68.4 | 0.0 |
| XI | XI | Jørgen Strand Larsen | FWD | 20 | 5.6 | 3.46 | 7.90 | 12.86 | 2.00 | 55.8 | 90.0 |
| XI | XI | Adam Armstrong | FWD | 17 | 5.1 | 4.17 | 7.57 | 12.31 | 2.00 | 79.2 | 72.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.4 | 7.63 | 25.60 | 42.19 | 9.00 | 74.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.54 | 23.48 | 37.95 | 10.00 | 85.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 4.20 | 14.28 | 23.66 | 3.00 | 85.5 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.11 | 10.54 | 17.19 | 2.00 | 81.5 | 90.0 |
| XI | XI | Bernardo Veiga de Carvalho e Silva | MID | 13 | 6.3 | 3.50 | 9.46 | 15.46 | 9.00 | 80.0 | 90.0 |

## GW19

- Train rows: 145775
- Bank: 2.90 -> 1.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 67.96
- Actual score: 82.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.26) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Jørgen Strand Larsen -> Matheus Santos Carneiro Da Cunha (projected gain 7.19, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.26) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench Boost | David Raya Martin | GK | 1 | 5.6 | 3.81 | 11.05 | 17.89 | 2.00 | 87.1 | 90.0 |
| XI | XI | Dean Henderson | GK | 7 | 4.4 | 3.93 | 8.82 | 13.98 | 2.00 | 84.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.19 | 12.54 | 20.79 | 2.00 | 84.7 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.56 | 11.68 | 19.07 | 12.00 | 83.4 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.23 | 10.09 | 16.33 | 6.00 | 80.7 | 90.0 |
| XI | XI | Milos Kerkez | DEF | 3 | 4.6 | 2.91 | 8.93 | 14.35 | 1.00 | 85.1 | 90.0 |
| Bench 4 | Bench Boost | Pedro Porro | DEF | 18 | 5.5 | 1.91 | 7.82 | 13.68 | 4.00 | 50.3 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 5.21 | 15.22 | 25.17 | 1.00 | 86.8 | 45.0 |
| Bench 2 | Bench Boost | Adam Armstrong | FWD | 17 | 5.1 | 2.57 | 7.37 | 11.78 | 5.00 | 63.1 | 64.0 |
| Bench 3 | Bench Boost | Jamie Vardy | FWD | 11 | 5.6 | 1.97 | 5.05 | 8.62 | 2.00 | 27.1 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.5 | 8.13 | 25.37 | 41.18 | 16.00 | 81.9 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 6.56 | 23.04 | 37.97 | 2.00 | 83.8 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 3.97 | 13.40 | 21.97 | 7.00 | 85.9 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.84 | 11.16 | 18.06 | 1.00 | 84.3 | 90.0 |
| XI | XI | Bernardo Veiga de Carvalho e Silva | MID | 13 | 6.3 | 4.03 | 10.52 | 17.19 | 3.00 | 82.1 | 90.0 |