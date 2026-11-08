# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 272.19
- Total actual points: 283.00
- Average predicted points: 68.05
- Average actual points: 70.75
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
- Predicted score: 65.62
- Actual score: 59.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 4.16 | 12.47 | 20.07 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.00 | 0.05 | 0.18 | 0.00 | 0.4 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.52 | 13.53 | 20.38 | 6.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.10 | 10.19 | 17.02 | 6.00 | 90.0 | 62.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.7 | 2.80 | 8.64 | 13.80 | 1.00 | 89.9 | 90.0 |
| Bench 4 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 1.79 | 5.80 | 9.29 | 2.00 | 71.3 | 90.0 |
| Bench 3 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 1.93 | 5.03 | 8.48 | 0.00 | 71.4 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.6 | 5.93 | 16.47 | 26.40 | 11.00 | 90.0 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 5.02 | 14.38 | 23.06 | 9.00 | 88.8 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 4.01 | 11.15 | 18.53 | 1.00 | 78.3 | 58.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 8.65 | 24.42 | 38.13 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.57 | 22.42 | 37.44 | 5.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.56 | 19.08 | 30.09 | 3.00 | 84.6 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.65 | 11.90 | 19.09 | 5.00 | 82.1 | 90.0 |
| Bench 2 | Bench | Tyler Dibling | MID | 17 | 4.5 | 2.32 | 6.01 | 9.68 | 2.00 | 59.0 | 90.0 |

## GW17

- Train rows: 144369
- Bank: 0.00 -> 0.80
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 60.32
- Actual score: 78.00
- Transfer: Pedro Porro -> Antonee Robinson (projected gain 3.76, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.89 | 12.08 | 19.66 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.00 | 0.09 | 0.20 | 0.00 | 0.9 | 0.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.8 | 4.94 | 12.44 | 19.79 | 6.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 3.52 | 11.81 | 18.05 | 2.00 | 82.3 | 90.0 |
| Bench 4 | Bench | Daniel Muñoz | DEF | 7 | 4.7 | 1.35 | 5.66 | 9.11 | 0.00 | 62.2 | 0.0 |
| Bench 3 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 1.50 | 4.99 | 8.35 | 0.00 | 70.9 | 90.0 |
| XI | XI | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 1.59 | 4.71 | 7.94 | 8.00 | 72.4 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.7 | 5.30 | 16.51 | 26.83 | 17.00 | 90.0 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 5.15 | 13.55 | 22.12 | 9.00 | 83.7 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 4.05 | 10.86 | 18.28 | 2.00 | 66.8 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 7.67 | 23.44 | 36.56 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.22 | 22.36 | 37.18 | 21.00 | 90.0 | 86.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.31 | 18.86 | 31.12 | 1.00 | 83.0 | 23.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.02 | 10.76 | 17.29 | 3.00 | 72.1 | 90.0 |
| Bench 2 | Bench | Tyler Dibling | MID | 17 | 4.5 | 2.17 | 6.24 | 10.21 | 1.00 | 60.2 | 45.0 |

## GW18

- Train rows: 145070
- Bank: 0.80 -> 2.80
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 70.40
- Actual score: 71.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (4.88) beats the best remaining Bench Boost opportunity (6.16).
- Transfer: Bukayo Saka -> Bruno Borges Fernandes (projected gain 9.41, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (4.88) beats the best remaining Bench Boost opportunity (6.16).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 4.23 | 12.44 | 20.41 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.00 | 0.06 | 0.19 | 0.00 | 1.7 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.81 | 13.66 | 21.30 | 7.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.8 | 2.05 | 8.87 | 13.37 | 1.00 | 67.3 | 90.0 |
| XI | XI | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.30 | 5.35 | 8.85 | 2.00 | 77.5 | 90.0 |
| Bench 3 | Bench Boost | Daniel Muñoz | DEF | 7 | 4.7 | 1.50 | 5.11 | 8.39 | 6.00 | 52.6 | 90.0 |
| Bench 4 | Bench Boost | Cameron Burgess | DEF | 10 | 4.0 | 1.23 | 4.64 | 7.69 | 0.00 | 77.5 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 6.58 | 19.15 | 30.51 | 8.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 5.49 | 14.58 | 24.28 | 12.00 | 86.4 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.18 | 10.35 | 17.18 | 0.00 | 64.9 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.4 | 10.14 | 26.64 | 43.41 | 9.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.66 | 23.12 | 37.28 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 5.58 | 15.34 | 25.42 | -2.00 | 90.0 | 46.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.35 | 10.75 | 17.62 | 2.00 | 76.6 | 90.0 |
| Bench 2 | Bench Boost | Tyler Dibling | MID | 17 | 4.5 | 2.15 | 5.99 | 9.85 | 1.00 | 53.7 | 17.0 |

## GW19

- Train rows: 145775
- Bank: 2.80 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 75.85
- Actual score: 75.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (9.22) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Tyler Dibling -> Anthony Gordon (projected gain 8.79, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (9.22) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Taylor Harwood-Bellis replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 4.23 | 12.09 | 19.78 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.04 | 0.29 | 0.49 | 0.00 | 4.1 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.42 | 11.54 | 19.09 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.8 | 3.53 | 10.44 | 16.25 | 4.00 | 87.7 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.7 | 3.59 | 8.75 | 14.05 | 2.00 | 77.4 | 90.0 |
| Bench 2 | Autosub In | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.15 | 5.96 | 9.58 | 0.00 | 79.4 | 90.0 |
| Bench 4 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 0.94 | 2.63 | 4.72 | 0.00 | 45.1 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 6.02 | 18.46 | 29.41 | 7.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 6.10 | 16.34 | 26.71 | 1.00 | 90.0 | 45.0 |
| Bench 3 | Bench | Jamie Vardy | FWD | 11 | 5.6 | 1.20 | 5.73 | 9.34 | 2.00 | 24.4 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.5 | 9.22 | 26.22 | 42.21 | 16.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.93 | 22.89 | 37.93 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 5.15 | 14.70 | 23.45 | 6.00 | 78.2 | 84.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.94 | 11.53 | 18.62 | 1.00 | 79.5 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.28 | 9.35 | 16.85 | 0.00 | 47.3 | 0.0 |