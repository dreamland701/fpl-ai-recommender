# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 268.40
- Total actual points: 291.00
- Average predicted points: 67.10
- Average actual points: 72.75
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
- Predicted score: 64.32
- Actual score: 59.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.75 | 10.66 | 17.07 | 6.00 | 88.6 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 6 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.51 | 12.76 | 19.68 | 6.00 | 90.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.18 | 11.65 | 19.31 | 6.00 | 87.4 | 62.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.7 | 3.02 | 9.21 | 14.90 | 1.00 | 80.0 | 90.0 |
| Bench 2 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.31 | 6.29 | 10.45 | 0.00 | 70.7 | 90.0 |
| Bench 4 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 2.14 | 6.26 | 10.23 | 2.00 | 69.4 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.6 | 6.25 | 16.77 | 26.76 | 11.00 | 94.8 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.16 | 12.40 | 20.22 | 9.00 | 78.6 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.75 | 11.10 | 17.86 | 1.00 | 82.3 | 58.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 8.44 | 23.99 | 38.56 | 3.00 | 116.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.26 | 21.85 | 36.96 | 5.00 | 91.6 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.28 | 18.69 | 29.69 | 3.00 | 90.1 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 4.28 | 12.51 | 19.86 | 5.00 | 88.5 | 90.0 |
| Bench 3 | Bench | Tyler Dibling | MID | 17 | 4.5 | 2.18 | 5.64 | 9.04 | 2.00 | 58.6 | 90.0 |

## GW17

- Train rows: 144369
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 59.99
- Actual score: 70.00
- Transfer: Daniel Muñoz -> Lewis Hall (projected gain 7.26, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.70 | 10.68 | 17.22 | 3.00 | 86.7 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 6 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 3.93 | 11.52 | 18.37 | 2.00 | 80.7 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 4.00 | 10.96 | 17.33 | 7.00 | 90.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 2.91 | 9.80 | 16.57 | -1.00 | 70.6 | 90.0 |
| Bench 2 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 1.97 | 6.07 | 10.16 | 0.00 | 69.4 | 90.0 |
| Bench 3 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 1.96 | 5.91 | 9.92 | 8.00 | 70.9 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.7 | 6.12 | 17.66 | 27.75 | 17.00 | 92.1 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.36 | 12.24 | 20.54 | 9.00 | 73.7 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.58 | 9.67 | 16.06 | 2.00 | 70.4 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 7.54 | 23.40 | 37.35 | 3.00 | 106.5 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 6.87 | 22.53 | 37.45 | 21.00 | 93.7 | 86.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.16 | 18.69 | 30.43 | 1.00 | 86.0 | 23.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.29 | 11.27 | 17.80 | 3.00 | 72.3 | 90.0 |
| Bench 4 | Bench | Tyler Dibling | MID | 17 | 4.5 | 1.89 | 5.46 | 8.94 | 1.00 | 60.0 | 45.0 |

## GW18

- Train rows: 145070
- Bank: 0.10 -> 2.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 71.62
- Actual score: 71.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.36) beats the best remaining Bench Boost opportunity (7.59).
- Transfer: Bukayo Saka -> Bruno Borges Fernandes (projected gain 18.41, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.36) beats the best remaining Bench Boost opportunity (7.59).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 4.09 | 11.19 | 17.99 | 6.00 | 88.5 | 90.0 |
| Bench 1 | Bench Boost | Marcus Bettinelli | GK | 6 | 3.9 | 0.05 | 0.00 | 0.03 | 0.00 | 0.0 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.57 | 12.86 | 20.66 | 7.00 | 87.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 2.97 | 9.54 | 16.01 | 1.00 | 78.3 | 9.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.11 | 9.20 | 14.84 | 6.00 | 71.7 | 90.0 |
| Bench 2 | Bench Boost | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.48 | 6.69 | 10.96 | 2.00 | 77.0 | 90.0 |
| Bench 4 | Bench Boost | Cameron Burgess | DEF | 10 | 4.0 | 1.76 | 6.05 | 10.04 | 0.00 | 77.0 | 0.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 8.8 | 8.05 | 21.52 | 33.55 | 8.00 | 114.5 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.30 | 12.51 | 21.16 | 12.00 | 77.2 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 2.60 | 8.82 | 14.72 | 0.00 | 62.3 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.4 | 9.57 | 25.60 | 42.19 | 9.00 | 109.9 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.2 | 7.78 | 23.48 | 37.95 | 10.00 | 114.1 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 5.14 | 14.14 | 23.85 | -2.00 | 88.5 | 46.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.48 | 10.54 | 17.19 | 2.00 | 75.0 | 90.0 |
| Bench 3 | Bench Boost | Tyler Dibling | MID | 17 | 4.5 | 2.07 | 5.41 | 8.89 | 1.00 | 55.5 | 17.0 |

## GW19

- Train rows: 145775
- Bank: 2.10 -> 1.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 72.47
- Actual score: 91.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.74) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Taylor Harwood-Bellis -> Antonee Robinson (projected gain 10.34, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.74) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Tyler Dibling replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.80 | 11.05 | 17.89 | 2.00 | 87.9 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 6 | 3.9 | 0.16 | 0.26 | 0.37 | 0.00 | 3.1 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.17 | 12.54 | 20.79 | 2.00 | 85.7 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 4.10 | 11.68 | 19.07 | 12.00 | 84.4 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.9 | 4.01 | 11.64 | 18.72 | 4.00 | 93.6 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 2.43 | 7.82 | 13.68 | 4.00 | 50.4 | 90.0 |
| Bench 4 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 1.06 | 3.52 | 6.10 | 0.00 | 43.0 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 7.56 | 20.73 | 32.41 | 7.00 | 84.5 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 5.39 | 15.22 | 25.17 | 1.00 | 95.3 | 45.0 |
| Bench 3 | Bench | Jamie Vardy | FWD | 11 | 5.6 | 1.30 | 5.05 | 8.62 | 2.00 | 25.5 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.5 | 8.74 | 25.37 | 41.18 | 16.00 | 113.4 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.89 | 23.04 | 37.97 | 2.00 | 105.4 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 4.04 | 11.16 | 18.06 | 1.00 | 79.5 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.4 | 2.85 | 9.48 | 16.78 | 0.00 | 49.6 | 0.0 |
| Bench 2 | Autosub In | Tyler Dibling | MID | 17 | 4.5 | 1.59 | 5.03 | 8.31 | 8.00 | 44.7 | 85.0 |