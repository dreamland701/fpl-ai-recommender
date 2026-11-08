# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 267.38
- Total actual points: 281.00
- Average predicted points: 66.84
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
- Predicted score: 63.41
- Actual score: 59.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.73 | 10.65 | 17.05 | 6.00 | 87.3 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.29 | 0.67 | 1.15 | 0.00 | 6.8 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.23 | 12.70 | 19.59 | 6.00 | 85.6 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.20 | 11.52 | 19.10 | 6.00 | 88.1 | 62.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.7 | 3.03 | 9.31 | 15.04 | 1.00 | 80.6 | 90.0 |
| Bench 2 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.40 | 6.37 | 10.57 | 0.00 | 71.7 | 90.0 |
| Bench 4 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 2.20 | 6.34 | 10.36 | 2.00 | 71.2 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.6 | 6.09 | 16.81 | 26.82 | 11.00 | 90.0 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.25 | 12.53 | 20.41 | 9.00 | 80.8 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.77 | 11.21 | 18.03 | 1.00 | 83.2 | 58.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 8.23 | 23.78 | 38.22 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.41 | 22.30 | 37.64 | 5.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.23 | 18.75 | 29.77 | 3.00 | 87.4 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 4.00 | 12.37 | 19.63 | 5.00 | 84.8 | 90.0 |
| Bench 3 | Bench | Tyler Dibling | MID | 17 | 4.5 | 2.21 | 5.73 | 9.18 | 2.00 | 59.3 | 90.0 |

## GW17

- Train rows: 144369
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 59.54
- Actual score: 70.00
- Transfer: Daniel Muñoz -> Lewis Hall (projected gain 4.80, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.68 | 10.65 | 17.14 | 3.00 | 85.6 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.26 | 0.62 | 1.06 | 0.00 | 6.7 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 3.87 | 11.66 | 18.55 | 2.00 | 80.2 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.83 | 10.94 | 17.29 | 7.00 | 87.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 3.03 | 9.69 | 16.39 | -1.00 | 73.4 | 90.0 |
| Bench 2 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 2.07 | 6.17 | 10.31 | 0.00 | 71.5 | 90.0 |
| Bench 3 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.05 | 6.00 | 10.06 | 8.00 | 72.2 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.7 | 5.81 | 17.69 | 27.79 | 17.00 | 85.9 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.62 | 12.48 | 20.87 | 9.00 | 78.8 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.54 | 9.74 | 16.14 | 2.00 | 70.8 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 7.34 | 23.19 | 37.00 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.12 | 22.72 | 37.73 | 21.00 | 90.0 | 86.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.20 | 18.72 | 30.45 | 1.00 | 85.9 | 23.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.17 | 11.26 | 17.76 | 3.00 | 71.7 | 90.0 |
| Bench 4 | Bench | Tyler Dibling | MID | 17 | 4.5 | 1.96 | 5.59 | 9.14 | 1.00 | 61.3 | 45.0 |

## GW18

- Train rows: 145070
- Bank: 0.10 -> 2.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 71.69
- Actual score: 71.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.63) beats the best remaining Bench Boost opportunity (7.88).
- Transfer: Bukayo Saka -> Bruno Borges Fernandes (projected gain 7.70, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.63) beats the best remaining Bench Boost opportunity (7.88).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 4.09 | 11.14 | 17.90 | 6.00 | 87.7 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.21 | 0.58 | 0.99 | 0.00 | 7.2 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.60 | 12.89 | 20.68 | 7.00 | 87.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 3.02 | 9.36 | 15.73 | 1.00 | 78.6 | 9.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.11 | 9.35 | 15.02 | 6.00 | 72.0 | 90.0 |
| Bench 2 | Bench Boost | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.55 | 6.71 | 10.99 | 2.00 | 78.1 | 90.0 |
| Bench 4 | Bench Boost | Cameron Burgess | DEF | 10 | 4.0 | 1.80 | 6.08 | 10.08 | 0.00 | 77.3 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 7.30 | 21.22 | 33.09 | 8.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.55 | 12.77 | 21.54 | 12.00 | 81.3 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 2.73 | 9.00 | 14.97 | 0.00 | 66.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.4 | 9.75 | 25.80 | 42.51 | 9.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.60 | 23.22 | 37.54 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 5.15 | 14.34 | 24.14 | -2.00 | 89.1 | 46.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.41 | 10.53 | 17.16 | 2.00 | 74.9 | 90.0 |
| Bench 3 | Bench Boost | Tyler Dibling | MID | 17 | 4.5 | 2.07 | 5.47 | 8.95 | 1.00 | 55.3 | 17.0 |

## GW19

- Train rows: 145775
- Bank: 2.10 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 72.74
- Actual score: 81.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.71) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Tyler Dibling -> Ismaïla Sarr (projected gain 5.55, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.71) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Taylor Harwood-Bellis replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.86 | 11.03 | 17.84 | 2.00 | 88.4 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.09 | 0.67 | 1.11 | 0.00 | 9.7 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.31 | 12.59 | 20.85 | 2.00 | 88.6 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 4.04 | 11.64 | 18.99 | 12.00 | 83.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 2.52 | 7.76 | 13.56 | 4.00 | 52.2 | 90.0 |
| Bench 2 | Autosub In | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.46 | 7.16 | 11.55 | 0.00 | 79.4 | 90.0 |
| Bench 3 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 1.19 | 3.84 | 6.56 | 0.00 | 45.8 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 7.10 | 20.46 | 31.94 | 7.00 | 77.7 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 5.40 | 15.31 | 25.29 | 1.00 | 90.0 | 45.0 |
| Bench 4 | Bench | Jamie Vardy | FWD | 11 | 5.6 | 1.14 | 5.28 | 9.37 | 2.00 | 22.8 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.5 | 8.71 | 25.39 | 41.21 | 16.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.84 | 22.83 | 37.62 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ismaïla Sarr | MID | 7 | 5.9 | 4.87 | 12.60 | 20.09 | 2.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.96 | 11.16 | 18.05 | 1.00 | 79.2 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.4 | 2.69 | 8.58 | 15.25 | 0.00 | 44.6 | 0.0 |