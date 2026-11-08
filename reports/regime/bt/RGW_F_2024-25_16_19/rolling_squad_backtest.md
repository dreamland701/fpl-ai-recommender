# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 267.46
- Total actual points: 281.00
- Average predicted points: 66.87
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
- Predicted score: 63.36
- Actual score: 59.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.73 | 10.60 | 16.74 | 6.00 | 84.3 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 6 | 3.9 | 0.20 | 0.58 | 1.01 | 0.00 | 1.6 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.21 | 12.53 | 19.09 | 6.00 | 87.1 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.15 | 11.33 | 18.84 | 6.00 | 88.9 | 62.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.7 | 3.06 | 9.60 | 15.49 | 1.00 | 83.4 | 90.0 |
| Bench 2 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.34 | 6.30 | 10.49 | 0.00 | 73.0 | 90.0 |
| Bench 4 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 2.17 | 6.27 | 10.25 | 2.00 | 72.3 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.6 | 6.11 | 16.91 | 26.84 | 11.00 | 90.0 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.25 | 12.39 | 20.12 | 9.00 | 80.9 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.75 | 11.05 | 17.66 | 1.00 | 82.7 | 58.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 8.18 | 23.73 | 38.01 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.46 | 22.66 | 38.02 | 5.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.26 | 18.73 | 29.56 | 3.00 | 88.6 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 4.00 | 12.22 | 19.38 | 5.00 | 85.9 | 90.0 |
| Bench 3 | Bench | Tyler Dibling | MID | 17 | 4.5 | 2.18 | 5.68 | 9.00 | 2.00 | 58.7 | 90.0 |

## GW17

- Train rows: 144369
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 59.41
- Actual score: 70.00
- Transfer: Daniel Muñoz -> Lewis Hall (projected gain 4.95, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.62 | 10.52 | 16.81 | 3.00 | 82.7 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 6 | 3.9 | 0.20 | 0.62 | 1.09 | 0.00 | 1.5 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 3.84 | 11.41 | 18.00 | 2.00 | 82.8 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.84 | 11.03 | 17.56 | 7.00 | 89.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 3.05 | 9.56 | 16.11 | -1.00 | 74.5 | 90.0 |
| Bench 2 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 2.06 | 6.10 | 10.10 | 0.00 | 73.0 | 90.0 |
| Bench 3 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.00 | 5.90 | 9.90 | 8.00 | 73.5 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.7 | 5.88 | 17.82 | 28.07 | 17.00 | 87.6 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.64 | 12.54 | 20.95 | 9.00 | 79.1 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.43 | 9.20 | 15.22 | 2.00 | 69.0 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 7.35 | 23.28 | 37.14 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.03 | 22.87 | 37.66 | 21.00 | 90.0 | 86.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.19 | 18.61 | 30.26 | 1.00 | 85.7 | 23.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.18 | 10.98 | 17.41 | 3.00 | 73.8 | 90.0 |
| Bench 4 | Bench | Tyler Dibling | MID | 17 | 4.5 | 1.95 | 5.60 | 9.05 | 1.00 | 61.0 | 45.0 |

## GW18

- Train rows: 145070
- Bank: 0.10 -> 2.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 71.95
- Actual score: 71.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.78) beats the best remaining Bench Boost opportunity (8.12).
- Transfer: Bukayo Saka -> Bruno Borges Fernandes (projected gain 7.73, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.78) beats the best remaining Bench Boost opportunity (8.12).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 4.04 | 11.00 | 17.64 | 6.00 | 85.1 | 90.0 |
| Bench 1 | Bench Boost | Marcus Bettinelli | GK | 6 | 3.9 | 0.32 | 0.72 | 1.16 | 0.00 | 2.9 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.59 | 12.82 | 20.51 | 7.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 3.07 | 9.51 | 15.85 | 1.00 | 80.6 | 9.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.16 | 9.38 | 15.18 | 6.00 | 75.2 | 90.0 |
| Bench 2 | Bench Boost | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.54 | 6.86 | 11.05 | 2.00 | 79.2 | 90.0 |
| Bench 4 | Bench Boost | Cameron Burgess | DEF | 10 | 4.0 | 1.90 | 6.24 | 10.15 | 0.00 | 79.2 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 7.34 | 20.81 | 32.84 | 8.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.56 | 12.81 | 21.69 | 12.00 | 81.8 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 2.72 | 8.71 | 14.52 | 0.00 | 65.8 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.4 | 9.72 | 25.70 | 42.40 | 9.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.56 | 23.33 | 37.59 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 5.28 | 14.50 | 24.57 | -2.00 | 90.0 | 46.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.42 | 10.34 | 16.89 | 2.00 | 75.6 | 90.0 |
| Bench 3 | Bench Boost | Tyler Dibling | MID | 17 | 4.5 | 2.02 | 5.57 | 9.03 | 1.00 | 54.6 | 17.0 |

## GW19

- Train rows: 145775
- Bank: 2.10 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 72.75
- Actual score: 81.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.70) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Tyler Dibling -> Ismaïla Sarr (projected gain 5.57, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.70) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Taylor Harwood-Bellis replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.84 | 11.02 | 17.83 | 2.00 | 85.5 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 6 | 3.9 | 0.39 | 0.94 | 1.46 | 0.00 | 5.6 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.32 | 12.55 | 20.86 | 2.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.97 | 11.39 | 19.05 | 12.00 | 85.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 2.53 | 7.87 | 13.80 | 4.00 | 53.8 | 90.0 |
| Bench 2 | Autosub In | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.41 | 7.02 | 11.45 | 0.00 | 80.6 | 90.0 |
| Bench 3 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 1.22 | 3.92 | 6.79 | 0.00 | 47.1 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 7.18 | 20.02 | 31.64 | 7.00 | 79.6 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 5.40 | 15.14 | 25.19 | 1.00 | 90.0 | 45.0 |
| Bench 4 | Bench | Jamie Vardy | FWD | 11 | 5.6 | 1.06 | 4.28 | 7.43 | 2.00 | 19.9 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.5 | 8.70 | 25.48 | 41.54 | 16.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.78 | 22.72 | 37.38 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ismaïla Sarr | MID | 7 | 5.9 | 4.88 | 12.50 | 20.10 | 2.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.94 | 10.93 | 17.69 | 1.00 | 79.4 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.4 | 2.82 | 8.96 | 16.02 | 0.00 | 46.6 | 0.0 |