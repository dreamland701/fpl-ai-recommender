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
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.71 | 10.66 | 17.07 | 6.00 | 86.9 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 6 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.25 | 12.76 | 19.68 | 6.00 | 86.1 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.25 | 11.65 | 19.31 | 6.00 | 89.3 | 62.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.7 | 2.97 | 9.21 | 14.90 | 1.00 | 79.4 | 90.0 |
| Bench 2 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.36 | 6.29 | 10.45 | 0.00 | 70.9 | 90.0 |
| Bench 3 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 2.17 | 6.26 | 10.23 | 2.00 | 70.5 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.6 | 6.06 | 16.77 | 26.76 | 11.00 | 90.0 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.19 | 12.40 | 20.22 | 9.00 | 79.4 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.72 | 11.10 | 17.86 | 1.00 | 82.0 | 58.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 8.30 | 23.99 | 38.56 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.18 | 21.85 | 36.96 | 5.00 | 88.3 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.19 | 18.69 | 29.69 | 3.00 | 86.5 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 4.06 | 12.51 | 19.86 | 5.00 | 86.1 | 90.0 |
| Bench 4 | Bench | Tyler Dibling | MID | 17 | 4.5 | 2.17 | 5.64 | 9.04 | 2.00 | 58.4 | 90.0 |

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
- Transfer: Daniel Muñoz -> Lewis Hall (projected gain 3.25, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.67 | 10.68 | 17.22 | 3.00 | 85.4 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 6 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 3.79 | 11.52 | 18.37 | 2.00 | 78.5 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.83 | 10.96 | 17.33 | 7.00 | 87.6 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 3.08 | 9.80 | 16.57 | -1.00 | 74.3 | 90.0 |
| Bench 2 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 2.03 | 6.07 | 10.16 | 0.00 | 70.6 | 90.0 |
| Bench 3 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.02 | 5.91 | 9.92 | 8.00 | 71.4 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.7 | 5.79 | 17.66 | 27.75 | 17.00 | 85.5 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.50 | 12.24 | 20.54 | 9.00 | 76.1 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.50 | 9.67 | 16.06 | 2.00 | 69.8 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 7.41 | 23.40 | 37.35 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.03 | 22.53 | 37.45 | 21.00 | 90.0 | 86.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.17 | 18.69 | 30.43 | 1.00 | 85.1 | 23.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.18 | 11.27 | 17.80 | 3.00 | 71.8 | 90.0 |
| Bench 4 | Bench | Tyler Dibling | MID | 17 | 4.5 | 1.91 | 5.46 | 8.94 | 1.00 | 60.1 | 45.0 |

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
- Transfer: Bukayo Saka -> Bryan Mbeumo (projected gain 7.68, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.35) beats the best remaining Bench Boost opportunity (7.58).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 4.10 | 11.19 | 17.99 | 6.00 | 87.7 | 90.0 |
| Bench 1 | Bench Boost | Marcus Bettinelli | GK | 6 | 3.9 | 0.03 | 0.00 | 0.03 | 0.00 | 0.0 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.57 | 12.86 | 20.66 | 7.00 | 87.2 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 3.09 | 9.54 | 16.01 | 1.00 | 80.4 | 9.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.03 | 9.20 | 14.84 | 6.00 | 70.3 | 90.0 |
| Bench 2 | Bench Boost | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.53 | 6.69 | 10.96 | 2.00 | 77.6 | 90.0 |
| Bench 4 | Bench Boost | Cameron Burgess | DEF | 10 | 4.0 | 1.78 | 6.05 | 10.04 | 0.00 | 77.1 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 7.43 | 21.52 | 33.55 | 8.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.43 | 12.51 | 21.16 | 12.00 | 78.5 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 2.65 | 8.82 | 14.72 | 0.00 | 64.2 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.4 | 9.64 | 25.60 | 42.19 | 9.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.69 | 23.48 | 37.95 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 4.89 | 14.28 | 23.66 | 3.00 | 89.4 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.41 | 10.54 | 17.19 | 2.00 | 75.0 | 90.0 |
| Bench 3 | Bench Boost | Tyler Dibling | MID | 17 | 4.5 | 2.02 | 5.41 | 8.89 | 1.00 | 54.2 | 17.0 |

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
- Transfer: Tyler Dibling -> Anthony Gordon (projected gain 7.38, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.67) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.85 | 11.05 | 17.89 | 2.00 | 88.0 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 6 | 3.9 | 0.13 | 0.26 | 0.37 | 0.00 | 2.7 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.26 | 12.54 | 20.79 | 2.00 | 87.6 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 4.04 | 11.68 | 19.07 | 12.00 | 83.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 2.53 | 7.82 | 13.68 | 4.00 | 52.5 | 90.0 |
| Bench 2 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.46 | 7.19 | 11.60 | 0.00 | 79.4 | 90.0 |
| Bench 4 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 1.03 | 3.52 | 6.10 | 0.00 | 42.2 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 7.20 | 20.73 | 32.41 | 7.00 | 80.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 5.35 | 15.22 | 25.17 | 1.00 | 90.0 | 45.0 |
| Bench 3 | Bench | Jamie Vardy | FWD | 11 | 5.6 | 1.31 | 5.05 | 8.62 | 2.00 | 26.4 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.5 | 8.67 | 25.37 | 41.18 | 16.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.91 | 23.04 | 37.97 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 5.03 | 14.46 | 23.14 | 6.00 | 80.8 | 84.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 4.03 | 13.40 | 21.97 | 7.00 | 85.9 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.96 | 11.16 | 18.06 | 1.00 | 79.2 | 90.0 |