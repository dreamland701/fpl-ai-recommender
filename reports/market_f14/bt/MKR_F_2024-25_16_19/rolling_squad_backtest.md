# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 263.35
- Total actual points: 281.00
- Average predicted points: 65.84
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
- Predicted score: 63.07
- Actual score: 59.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 4.20 | 11.73 | 18.42 | 6.00 | 85.1 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 6 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.77 | 13.78 | 20.70 | 6.00 | 83.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.02 | 11.80 | 19.66 | 6.00 | 89.3 | 62.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.7 | 2.94 | 9.16 | 15.00 | 1.00 | 80.5 | 90.0 |
| Bench 3 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.18 | 6.38 | 10.72 | 0.00 | 71.1 | 90.0 |
| Bench 2 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 2.24 | 6.36 | 10.39 | 2.00 | 70.4 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.6 | 5.80 | 16.29 | 26.02 | 11.00 | 90.0 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.20 | 12.44 | 20.20 | 9.00 | 79.5 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.51 | 10.35 | 17.11 | 1.00 | 85.5 | 58.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 7.99 | 23.13 | 36.84 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.08 | 21.23 | 35.52 | 5.00 | 86.1 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.48 | 18.92 | 29.56 | 3.00 | 84.6 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 4.10 | 13.00 | 20.37 | 5.00 | 83.3 | 90.0 |
| Bench 4 | Bench | Tyler Dibling | MID | 17 | 4.5 | 1.88 | 5.45 | 8.94 | 2.00 | 59.3 | 90.0 |

## GW17

- Train rows: 144369
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 59.51
- Actual score: 70.00
- Transfer: Daniel Muñoz -> Lewis Hall (projected gain 3.69, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.97 | 11.27 | 17.90 | 3.00 | 84.5 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 6 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.18 | 12.23 | 19.11 | 2.00 | 76.8 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.87 | 11.32 | 17.83 | 7.00 | 86.8 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 3.01 | 9.62 | 16.41 | -1.00 | 75.1 | 90.0 |
| Bench 2 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.14 | 6.10 | 10.16 | 8.00 | 70.8 | 90.0 |
| Bench 3 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 2.09 | 6.05 | 10.18 | 0.00 | 70.9 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.7 | 5.61 | 17.16 | 27.01 | 17.00 | 86.3 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.15 | 11.70 | 19.96 | 9.00 | 77.9 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.43 | 9.28 | 15.68 | 2.00 | 71.7 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 7.36 | 22.92 | 36.31 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 6.80 | 22.05 | 36.47 | 21.00 | 90.0 | 86.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.36 | 18.76 | 30.22 | 1.00 | 84.5 | 23.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.40 | 11.76 | 18.21 | 3.00 | 70.0 | 90.0 |
| Bench 4 | Bench | Tyler Dibling | MID | 17 | 4.5 | 1.94 | 5.43 | 8.94 | 1.00 | 60.3 | 45.0 |

## GW18

- Train rows: 145070
- Bank: 0.10 -> 2.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 69.80
- Actual score: 71.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.21) beats the best remaining Bench Boost opportunity (7.42).
- Transfer: Bukayo Saka -> Bruno Borges Fernandes (projected gain 7.41, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.21) beats the best remaining Bench Boost opportunity (7.42).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 4.50 | 12.68 | 20.01 | 6.00 | 85.4 | 90.0 |
| Bench 1 | Bench Boost | Marcus Bettinelli | GK | 6 | 3.9 | 0.06 | 0.00 | 0.00 | 0.00 | 0.4 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.96 | 14.09 | 22.03 | 7.00 | 83.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 3.12 | 9.77 | 16.40 | 1.00 | 80.0 | 9.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 2.98 | 9.14 | 14.77 | 6.00 | 70.5 | 90.0 |
| Bench 2 | Bench Boost | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.47 | 6.70 | 11.01 | 2.00 | 77.6 | 90.0 |
| Bench 4 | Bench Boost | Cameron Burgess | DEF | 10 | 4.0 | 1.78 | 5.64 | 9.48 | 0.00 | 78.5 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 7.08 | 20.24 | 31.85 | 8.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 3.94 | 11.48 | 19.95 | 12.00 | 81.5 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 2.58 | 8.44 | 14.51 | 0.00 | 68.1 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.4 | 9.05 | 23.75 | 39.02 | 9.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.60 | 23.02 | 36.86 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 5.13 | 14.04 | 23.70 | -2.00 | 87.8 | 46.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.59 | 11.15 | 17.82 | 2.00 | 72.6 | 90.0 |
| Bench 3 | Bench Boost | Tyler Dibling | MID | 17 | 4.5 | 1.91 | 5.24 | 8.71 | 1.00 | 54.7 | 17.0 |

## GW19

- Train rows: 145775
- Bank: 2.10 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 70.96
- Actual score: 81.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.41) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Tyler Dibling -> Ismaïla Sarr (projected gain 5.82, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.41) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Taylor Harwood-Bellis replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.93 | 11.32 | 18.26 | 2.00 | 88.1 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 6 | 3.9 | 0.15 | 0.17 | 0.28 | 0.00 | 3.2 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.39 | 12.83 | 21.09 | 2.00 | 87.2 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.69 | 10.74 | 17.96 | 12.00 | 86.3 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 2.68 | 8.41 | 14.47 | 4.00 | 51.3 | 90.0 |
| Bench 2 | Autosub In | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.36 | 6.80 | 11.12 | 0.00 | 80.6 | 90.0 |
| Bench 4 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 0.88 | 3.33 | 5.88 | 0.00 | 42.6 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 6.65 | 18.87 | 30.37 | 7.00 | 86.8 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.70 | 13.83 | 23.70 | 1.00 | 90.0 | 45.0 |
| Bench 3 | Bench | Jamie Vardy | FWD | 11 | 5.6 | 1.25 | 4.94 | 8.66 | 2.00 | 28.3 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.5 | 8.41 | 24.83 | 40.07 | 16.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.70 | 22.38 | 36.68 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ismaïla Sarr | MID | 7 | 5.9 | 4.82 | 12.51 | 19.86 | 2.00 | 89.5 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 4.04 | 11.56 | 18.43 | 1.00 | 77.6 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.13 | 9.71 | 17.16 | 0.00 | 51.5 | 0.0 |