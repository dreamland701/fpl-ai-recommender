# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 263.40
- Total actual points: 281.00
- Average predicted points: 65.85
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
- Predicted score: 62.97
- Actual score: 59.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 4.14 | 11.76 | 18.47 | 6.00 | 85.0 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 6 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.69 | 13.80 | 20.76 | 6.00 | 82.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.12 | 11.76 | 19.58 | 6.00 | 89.4 | 62.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.7 | 2.94 | 9.17 | 15.01 | 1.00 | 80.5 | 90.0 |
| Bench 3 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 2.22 | 6.37 | 10.41 | 2.00 | 70.4 | 90.0 |
| Bench 2 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.27 | 6.34 | 10.64 | 0.00 | 71.3 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.6 | 5.87 | 16.26 | 25.96 | 11.00 | 90.0 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.23 | 12.43 | 20.18 | 9.00 | 79.6 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.50 | 10.36 | 17.13 | 1.00 | 85.4 | 58.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 7.98 | 23.13 | 36.85 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.03 | 21.24 | 35.56 | 5.00 | 86.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.43 | 18.94 | 29.60 | 3.00 | 84.5 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 4.05 | 13.02 | 20.41 | 5.00 | 83.3 | 90.0 |
| Bench 4 | Bench | Tyler Dibling | MID | 17 | 4.5 | 1.99 | 5.41 | 8.86 | 2.00 | 59.5 | 90.0 |

## GW17

- Train rows: 144369
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 59.45
- Actual score: 70.00
- Transfer: Daniel Muñoz -> Lewis Hall (projected gain 5.20, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.94 | 11.28 | 17.92 | 3.00 | 84.5 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 6 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.14 | 12.24 | 19.14 | 2.00 | 76.8 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.89 | 11.31 | 17.81 | 7.00 | 86.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 2.93 | 9.65 | 16.48 | -1.00 | 75.0 | 90.0 |
| Bench 2 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.10 | 6.12 | 10.19 | 8.00 | 70.7 | 90.0 |
| Bench 3 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 2.01 | 6.08 | 10.25 | 0.00 | 70.8 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.7 | 5.64 | 17.15 | 26.98 | 17.00 | 86.3 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.28 | 11.66 | 19.85 | 9.00 | 78.1 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.39 | 9.29 | 15.72 | 2.00 | 71.6 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 7.35 | 22.92 | 36.31 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 6.82 | 22.04 | 36.46 | 21.00 | 90.0 | 86.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.35 | 18.76 | 30.23 | 1.00 | 84.5 | 23.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.35 | 11.77 | 18.25 | 3.00 | 69.9 | 90.0 |
| Bench 4 | Bench | Tyler Dibling | MID | 17 | 4.5 | 1.91 | 5.43 | 8.96 | 1.00 | 60.3 | 45.0 |

## GW18

- Train rows: 145070
- Bank: 0.10 -> 2.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 69.83
- Actual score: 71.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.17) beats the best remaining Bench Boost opportunity (7.34).
- Transfer: Bukayo Saka -> Bruno Borges Fernandes (projected gain 7.43, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.17) beats the best remaining Bench Boost opportunity (7.34).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 4.51 | 12.67 | 20.01 | 6.00 | 85.4 | 90.0 |
| Bench 1 | Bench Boost | Marcus Bettinelli | GK | 6 | 3.9 | 0.02 | 0.00 | 0.00 | 0.00 | 0.4 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.96 | 14.09 | 22.03 | 7.00 | 83.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 3.04 | 9.80 | 16.47 | 1.00 | 79.8 | 9.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 2.96 | 9.15 | 14.79 | 6.00 | 70.4 | 90.0 |
| Bench 2 | Bench Boost | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.49 | 6.69 | 10.99 | 2.00 | 77.7 | 90.0 |
| Bench 4 | Bench Boost | Cameron Burgess | DEF | 10 | 4.0 | 1.72 | 5.66 | 9.53 | 0.00 | 78.4 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 7.08 | 20.25 | 31.86 | 8.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.07 | 11.45 | 19.85 | 12.00 | 81.7 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 2.57 | 8.45 | 14.52 | 0.00 | 68.1 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.4 | 9.13 | 23.71 | 38.95 | 9.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.58 | 23.03 | 36.88 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 5.08 | 14.05 | 23.74 | -2.00 | 87.7 | 46.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.56 | 11.16 | 17.84 | 2.00 | 72.6 | 90.0 |
| Bench 3 | Bench Boost | Tyler Dibling | MID | 17 | 4.5 | 1.94 | 5.23 | 8.68 | 1.00 | 54.8 | 17.0 |

## GW19

- Train rows: 145775
- Bank: 2.10 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 71.16
- Actual score: 81.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.48) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Tyler Dibling -> Ismaïla Sarr (projected gain 5.79, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.48) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Taylor Harwood-Bellis replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.90 | 11.33 | 18.29 | 2.00 | 88.1 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 6 | 3.9 | 0.15 | 0.17 | 0.27 | 0.00 | 3.3 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.34 | 12.84 | 21.13 | 2.00 | 87.1 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.68 | 10.74 | 17.96 | 12.00 | 86.3 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 2.62 | 8.43 | 14.51 | 4.00 | 51.2 | 90.0 |
| Bench 2 | Autosub In | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.35 | 6.80 | 11.14 | 0.00 | 80.5 | 90.0 |
| Bench 4 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 0.95 | 3.32 | 5.84 | 0.00 | 42.7 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 6.66 | 18.87 | 30.37 | 7.00 | 86.8 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.78 | 13.81 | 23.64 | 1.00 | 90.0 | 45.0 |
| Bench 3 | Bench | Jamie Vardy | FWD | 11 | 5.6 | 1.26 | 4.94 | 8.66 | 2.00 | 28.3 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.5 | 8.48 | 24.81 | 40.02 | 16.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.72 | 22.37 | 36.67 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ismaïla Sarr | MID | 7 | 5.9 | 4.88 | 12.49 | 19.82 | 2.00 | 89.6 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 4.06 | 11.56 | 18.42 | 1.00 | 77.7 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.07 | 9.73 | 17.21 | 0.00 | 51.5 | 0.0 |