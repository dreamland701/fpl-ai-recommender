# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 267.68
- Total actual points: 297.00
- Average predicted points: 66.92
- Average actual points: 74.25
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
- Predicted score: 63.21
- Actual score: 59.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.71 | 10.80 | 17.33 | 6.00 | 86.9 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 6 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.25 | 12.38 | 19.13 | 6.00 | 86.1 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.25 | 11.78 | 19.36 | 6.00 | 89.3 | 62.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.7 | 2.97 | 9.10 | 14.91 | 1.00 | 79.4 | 90.0 |
| Bench 2 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.36 | 6.46 | 10.71 | 0.00 | 70.9 | 90.0 |
| Bench 3 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 2.17 | 6.36 | 10.22 | 2.00 | 70.5 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.6 | 6.06 | 16.35 | 26.10 | 11.00 | 90.0 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.19 | 12.40 | 19.98 | 9.00 | 79.4 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.72 | 10.74 | 17.42 | 1.00 | 82.0 | 58.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 8.30 | 23.78 | 38.47 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.18 | 22.42 | 38.01 | 5.00 | 88.3 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.19 | 18.51 | 29.34 | 3.00 | 86.5 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 4.06 | 12.01 | 18.98 | 5.00 | 86.1 | 90.0 |
| Bench 4 | Bench | Tyler Dibling | MID | 17 | 4.5 | 2.17 | 5.62 | 8.97 | 2.00 | 58.4 | 90.0 |

## GW17

- Train rows: 144369
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 59.34
- Actual score: 70.00
- Transfer: Daniel Muñoz -> Lewis Hall (projected gain 2.95, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.67 | 10.77 | 17.40 | 3.00 | 85.4 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 6 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 3.79 | 11.30 | 17.84 | 2.00 | 78.5 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.83 | 10.62 | 16.89 | 7.00 | 87.6 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 3.08 | 10.07 | 16.88 | -1.00 | 74.3 | 90.0 |
| Bench 2 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 2.03 | 6.13 | 10.15 | 0.00 | 70.6 | 90.0 |
| Bench 3 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.02 | 6.02 | 10.10 | 8.00 | 71.4 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.7 | 5.79 | 16.82 | 26.43 | 17.00 | 85.5 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.50 | 12.17 | 20.33 | 9.00 | 76.1 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.50 | 9.20 | 15.22 | 2.00 | 69.8 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 7.41 | 23.19 | 37.10 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.03 | 23.04 | 38.39 | 21.00 | 90.0 | 86.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.17 | 18.79 | 30.66 | 1.00 | 85.1 | 23.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.18 | 10.57 | 16.44 | 3.00 | 71.8 | 90.0 |
| Bench 4 | Bench | Tyler Dibling | MID | 17 | 4.5 | 1.91 | 5.24 | 8.63 | 1.00 | 60.1 | 45.0 |

## GW18

- Train rows: 145070
- Bank: 0.10 -> 2.90
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 70.93
- Actual score: 76.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.35) beats the best remaining Bench Boost opportunity (7.58).
- Transfer: Bukayo Saka -> Bryan Mbeumo (projected gain 7.54, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.35) beats the best remaining Bench Boost opportunity (7.58).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 4.10 | 11.38 | 18.38 | 6.00 | 87.7 | 90.0 |
| Bench 1 | Bench Boost | Marcus Bettinelli | GK | 6 | 3.9 | 0.03 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.57 | 12.97 | 20.90 | 7.00 | 87.2 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 3.09 | 9.59 | 16.14 | 1.00 | 80.4 | 9.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.03 | 8.79 | 14.16 | 6.00 | 70.3 | 90.0 |
| Bench 2 | Bench Boost | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.53 | 6.82 | 11.12 | 2.00 | 77.6 | 90.0 |
| Bench 4 | Bench Boost | Cameron Burgess | DEF | 10 | 4.0 | 1.78 | 6.07 | 10.04 | 0.00 | 77.1 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 7.43 | 20.41 | 31.99 | 8.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.43 | 12.34 | 20.87 | 12.00 | 78.5 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 2.65 | 8.44 | 14.06 | 0.00 | 64.2 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.4 | 9.64 | 25.95 | 43.10 | 9.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.69 | 23.68 | 38.29 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 4.89 | 14.26 | 23.56 | 3.00 | 89.4 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.41 | 10.12 | 16.41 | 2.00 | 75.0 | 90.0 |
| Bench 3 | Bench Boost | Tyler Dibling | MID | 17 | 4.5 | 2.02 | 5.28 | 8.62 | 1.00 | 54.2 | 17.0 |

## GW19

- Train rows: 145775
- Bank: 2.90 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 74.19
- Actual score: 92.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.67) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Tyler Dibling -> Anthony Gordon (projected gain 7.09, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.67) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.85 | 11.21 | 18.30 | 2.00 | 88.0 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 6 | 3.9 | 0.13 | 0.20 | 0.30 | 0.00 | 2.7 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.26 | 12.70 | 21.10 | 2.00 | 87.6 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 4.04 | 11.41 | 18.85 | 12.00 | 83.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 2.53 | 7.87 | 13.98 | 4.00 | 52.5 | 90.0 |
| Bench 2 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.46 | 7.18 | 11.79 | 0.00 | 79.4 | 90.0 |
| Bench 4 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 1.03 | 3.64 | 6.52 | 0.00 | 42.2 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 7.20 | 19.57 | 30.92 | 7.00 | 80.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 5.35 | 14.74 | 24.65 | 1.00 | 90.0 | 45.0 |
| Bench 3 | Bench | Jamie Vardy | FWD | 11 | 5.6 | 1.31 | 4.77 | 8.16 | 2.00 | 26.4 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.5 | 8.67 | 25.47 | 41.67 | 16.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.91 | 23.15 | 38.42 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 5.03 | 14.16 | 22.92 | 6.00 | 80.8 | 84.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 4.03 | 13.23 | 21.81 | 7.00 | 85.9 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.96 | 10.65 | 17.45 | 1.00 | 79.2 | 90.0 |