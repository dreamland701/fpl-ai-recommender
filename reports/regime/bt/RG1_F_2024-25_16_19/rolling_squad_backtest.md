# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 267.56
- Total actual points: 281.00
- Average predicted points: 66.89
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
- Predicted score: 63.43
- Actual score: 59.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.74 | 10.70 | 17.11 | 6.00 | 84.7 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.34 | 0.79 | 1.33 | 0.00 | 4.3 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.25 | 12.79 | 19.78 | 6.00 | 87.6 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.19 | 11.51 | 19.10 | 6.00 | 89.3 | 62.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.7 | 3.06 | 9.49 | 15.39 | 1.00 | 82.7 | 90.0 |
| Bench 2 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.39 | 6.39 | 10.62 | 0.00 | 73.3 | 90.0 |
| Bench 3 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 2.21 | 6.37 | 10.44 | 2.00 | 72.5 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.6 | 6.10 | 16.83 | 26.86 | 11.00 | 90.0 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.20 | 12.32 | 20.02 | 9.00 | 79.7 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.70 | 10.94 | 17.52 | 1.00 | 81.8 | 58.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 8.25 | 23.90 | 38.45 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.45 | 22.50 | 38.04 | 5.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.27 | 18.90 | 30.05 | 3.00 | 88.2 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.96 | 12.22 | 19.35 | 5.00 | 83.8 | 90.0 |
| Bench 4 | Bench | Tyler Dibling | MID | 17 | 4.5 | 2.18 | 5.64 | 9.00 | 2.00 | 58.6 | 90.0 |

## GW17

- Train rows: 144369
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 59.59
- Actual score: 70.00
- Transfer: Daniel Muñoz -> Lewis Hall (projected gain 4.88, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.70 | 10.72 | 17.23 | 3.00 | 83.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.31 | 0.74 | 1.25 | 0.00 | 4.3 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 3.88 | 11.75 | 18.75 | 2.00 | 82.3 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.85 | 11.03 | 17.48 | 7.00 | 88.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 3.02 | 9.68 | 16.39 | -1.00 | 74.5 | 90.0 |
| Bench 2 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 2.06 | 6.17 | 10.34 | 0.00 | 72.8 | 90.0 |
| Bench 3 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.04 | 5.99 | 10.06 | 8.00 | 73.7 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.7 | 5.82 | 17.75 | 27.91 | 17.00 | 85.7 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.57 | 12.31 | 20.57 | 9.00 | 78.0 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.48 | 9.53 | 15.75 | 2.00 | 69.5 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 7.37 | 23.33 | 37.29 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.16 | 22.91 | 38.11 | 21.00 | 90.0 | 86.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.24 | 18.90 | 30.79 | 1.00 | 86.5 | 23.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.14 | 11.17 | 17.60 | 3.00 | 70.8 | 90.0 |
| Bench 4 | Bench | Tyler Dibling | MID | 17 | 4.5 | 1.93 | 5.50 | 8.98 | 1.00 | 60.5 | 45.0 |

## GW18

- Train rows: 145070
- Bank: 0.10 -> 2.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 71.68
- Actual score: 71.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.66) beats the best remaining Bench Boost opportunity (7.92).
- Transfer: Bukayo Saka -> Bruno Borges Fernandes (projected gain 7.76, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.66) beats the best remaining Bench Boost opportunity (7.92).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 4.10 | 11.16 | 17.91 | 6.00 | 85.2 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.26 | 0.70 | 1.18 | 0.00 | 4.8 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.60 | 12.93 | 20.80 | 7.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.13 | 9.46 | 15.26 | 6.00 | 73.1 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 3.01 | 9.36 | 15.75 | 1.00 | 79.7 | 9.0 |
| Bench 2 | Bench Boost | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.54 | 6.73 | 11.04 | 2.00 | 79.7 | 90.0 |
| Bench 4 | Bench Boost | Cameron Burgess | DEF | 10 | 4.0 | 1.80 | 6.11 | 10.16 | 0.00 | 78.8 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 7.30 | 21.17 | 32.99 | 8.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.50 | 12.61 | 21.23 | 12.00 | 80.3 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 2.69 | 8.84 | 14.68 | 0.00 | 65.1 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.4 | 9.77 | 25.92 | 42.74 | 9.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.62 | 23.35 | 37.79 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 5.17 | 14.41 | 24.28 | -2.00 | 89.4 | 46.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.36 | 10.35 | 16.83 | 2.00 | 73.6 | 90.0 |
| Bench 3 | Bench Boost | Tyler Dibling | MID | 17 | 4.5 | 2.05 | 5.45 | 8.92 | 1.00 | 54.9 | 17.0 |

## GW19

- Train rows: 145775
- Bank: 2.10 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 72.86
- Actual score: 81.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.75) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Tyler Dibling -> Ismaïla Sarr (projected gain 5.45, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.75) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Taylor Harwood-Bellis replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.87 | 11.07 | 17.89 | 2.00 | 85.9 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.14 | 0.80 | 1.30 | 0.00 | 7.3 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.32 | 12.68 | 21.04 | 2.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 4.04 | 11.67 | 19.07 | 12.00 | 84.2 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 2.54 | 7.86 | 13.76 | 4.00 | 53.6 | 90.0 |
| Bench 2 | Autosub In | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.46 | 7.18 | 11.62 | 0.00 | 80.8 | 90.0 |
| Bench 3 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 1.20 | 3.91 | 6.72 | 0.00 | 47.5 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 7.12 | 20.55 | 32.11 | 7.00 | 77.3 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 5.33 | 15.08 | 24.85 | 1.00 | 90.0 | 45.0 |
| Bench 4 | Bench | Jamie Vardy | FWD | 11 | 5.6 | 1.01 | 4.31 | 7.43 | 2.00 | 19.4 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.5 | 8.75 | 25.57 | 41.57 | 16.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.87 | 23.00 | 37.96 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ismaïla Sarr | MID | 7 | 5.9 | 4.84 | 12.53 | 19.96 | 2.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.91 | 10.95 | 17.65 | 1.00 | 77.7 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.4 | 2.78 | 9.05 | 16.17 | 0.00 | 45.8 | 0.0 |