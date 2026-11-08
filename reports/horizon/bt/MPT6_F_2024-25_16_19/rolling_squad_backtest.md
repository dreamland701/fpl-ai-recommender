# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 268.98
- Total actual points: 297.00
- Average predicted points: 67.24
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
- Predicted score: 63.44
- Actual score: 59.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.74 | 10.85 | 17.39 | 6.00 | 87.4 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 6 | 3.9 | 0.14 | 0.44 | 0.75 | 0.00 | 3.6 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.23 | 12.32 | 19.05 | 6.00 | 85.6 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.20 | 11.66 | 19.17 | 6.00 | 88.2 | 62.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.7 | 3.03 | 9.25 | 15.14 | 1.00 | 80.7 | 90.0 |
| Bench 2 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.40 | 6.56 | 10.85 | 0.00 | 71.7 | 90.0 |
| Bench 4 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 2.20 | 6.45 | 10.36 | 2.00 | 71.2 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.6 | 6.09 | 16.42 | 26.19 | 11.00 | 90.0 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.26 | 12.58 | 20.24 | 9.00 | 80.8 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.77 | 10.88 | 17.62 | 1.00 | 83.2 | 58.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 8.24 | 23.61 | 38.20 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.41 | 22.98 | 38.86 | 5.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.24 | 18.62 | 29.49 | 3.00 | 87.5 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 4.00 | 11.85 | 18.73 | 5.00 | 84.8 | 90.0 |
| Bench 3 | Bench | Tyler Dibling | MID | 17 | 4.5 | 2.21 | 5.73 | 9.15 | 2.00 | 59.3 | 90.0 |

## GW17

- Train rows: 144369
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 59.60
- Actual score: 70.00
- Transfer: Daniel Muñoz -> Lewis Hall (projected gain 12.25, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.69 | 10.82 | 17.45 | 3.00 | 85.8 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 6 | 3.9 | 0.14 | 0.47 | 0.80 | 0.00 | 3.7 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 3.88 | 11.51 | 18.17 | 2.00 | 80.3 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.83 | 10.61 | 16.87 | 7.00 | 87.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 3.04 | 9.98 | 16.73 | -1.00 | 73.4 | 90.0 |
| Bench 2 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 2.07 | 6.24 | 10.32 | 0.00 | 71.5 | 90.0 |
| Bench 3 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.05 | 6.12 | 10.24 | 8.00 | 72.1 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.7 | 5.81 | 16.88 | 26.53 | 17.00 | 86.0 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.62 | 12.50 | 20.84 | 9.00 | 79.0 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.55 | 9.34 | 15.43 | 2.00 | 70.9 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.12 | 23.29 | 38.77 | 21.00 | 90.0 | 86.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 7.34 | 23.01 | 36.83 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.21 | 18.90 | 30.82 | 1.00 | 86.1 | 23.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.17 | 10.58 | 16.47 | 3.00 | 71.8 | 90.0 |
| Bench 4 | Bench | Tyler Dibling | MID | 17 | 4.5 | 1.96 | 5.38 | 8.85 | 1.00 | 61.3 | 45.0 |

## GW18

- Train rows: 145070
- Bank: 0.10 -> 2.90
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 71.56
- Actual score: 76.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.70) beats the best remaining Bench Boost opportunity (8.02).
- Transfer: Bukayo Saka -> Bryan Mbeumo (projected gain 22.45, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.70) beats the best remaining Bench Boost opportunity (8.02).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 4.10 | 11.38 | 18.37 | 6.00 | 87.8 | 90.0 |
| Bench 1 | Bench Boost | Marcus Bettinelli | GK | 6 | 3.9 | 0.27 | 0.63 | 0.94 | 0.00 | 5.2 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.60 | 13.05 | 21.02 | 7.00 | 88.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 3.02 | 9.40 | 15.85 | 1.00 | 78.6 | 9.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.12 | 9.02 | 14.52 | 6.00 | 72.3 | 90.0 |
| Bench 2 | Bench Boost | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.55 | 6.89 | 11.22 | 2.00 | 78.2 | 90.0 |
| Bench 4 | Bench Boost | Cameron Burgess | DEF | 10 | 4.0 | 1.80 | 6.11 | 10.10 | 0.00 | 77.4 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 7.30 | 20.09 | 31.49 | 8.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.56 | 12.69 | 21.42 | 12.00 | 81.5 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 2.74 | 8.66 | 14.40 | 0.00 | 66.1 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.4 | 9.74 | 26.21 | 43.48 | 9.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.60 | 23.45 | 37.94 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 4.91 | 14.33 | 23.66 | 3.00 | 89.9 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.42 | 10.13 | 16.44 | 2.00 | 75.0 | 90.0 |
| Bench 3 | Bench Boost | Tyler Dibling | MID | 17 | 4.5 | 2.08 | 5.43 | 8.85 | 1.00 | 55.5 | 17.0 |

## GW19

- Train rows: 145775
- Bank: 2.90 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 74.38
- Actual score: 92.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.72) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Tyler Dibling -> Anthony Gordon (projected gain 20.57, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.72) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.87 | 11.27 | 18.39 | 2.00 | 88.6 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 6 | 3.9 | 0.36 | 0.81 | 1.24 | 0.00 | 7.9 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.32 | 12.85 | 21.34 | 2.00 | 88.8 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 4.05 | 11.43 | 18.89 | 12.00 | 83.7 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 2.53 | 7.88 | 13.98 | 4.00 | 52.4 | 90.0 |
| Bench 2 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.47 | 7.19 | 11.79 | 0.00 | 79.5 | 90.0 |
| Bench 3 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 1.20 | 4.07 | 7.17 | 0.00 | 46.0 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 7.11 | 19.34 | 30.59 | 7.00 | 78.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 5.40 | 14.89 | 24.88 | 1.00 | 90.0 | 45.0 |
| Bench 4 | Bench | Jamie Vardy | FWD | 11 | 5.6 | 1.04 | 4.08 | 7.11 | 2.00 | 20.4 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.5 | 8.72 | 25.56 | 41.80 | 16.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.85 | 23.01 | 38.20 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 5.05 | 14.21 | 23.00 | 6.00 | 81.2 | 84.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 4.08 | 13.37 | 22.03 | 7.00 | 87.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.97 | 10.68 | 17.48 | 1.00 | 79.3 | 90.0 |