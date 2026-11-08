# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 267.60
- Total actual points: 281.00
- Average predicted points: 66.90
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
- Predicted score: 63.39
- Actual score: 59.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.71 | 10.55 | 16.68 | 6.00 | 87.0 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 6 | 3.9 | 0.15 | 0.40 | 0.71 | 0.00 | 3.8 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.22 | 12.52 | 19.04 | 6.00 | 85.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.17 | 11.39 | 18.91 | 6.00 | 87.9 | 62.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.7 | 3.05 | 9.54 | 15.35 | 1.00 | 81.6 | 90.0 |
| Bench 2 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.36 | 6.34 | 10.53 | 0.00 | 71.7 | 90.0 |
| Bench 4 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 2.17 | 6.28 | 10.23 | 2.00 | 71.2 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.6 | 6.10 | 16.89 | 26.79 | 11.00 | 90.0 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.29 | 12.56 | 20.41 | 9.00 | 81.8 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.79 | 11.24 | 18.01 | 1.00 | 83.9 | 58.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 8.18 | 23.68 | 37.93 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.45 | 22.56 | 37.83 | 5.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.24 | 18.64 | 29.40 | 3.00 | 88.1 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 4.03 | 12.33 | 19.58 | 5.00 | 86.8 | 90.0 |
| Bench 3 | Bench | Tyler Dibling | MID | 17 | 4.5 | 2.19 | 5.76 | 9.15 | 2.00 | 59.5 | 90.0 |

## GW17

- Train rows: 144369
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 59.43
- Actual score: 70.00
- Transfer: Daniel Muñoz -> Lewis Hall (projected gain 4.89, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.60 | 10.48 | 16.76 | 3.00 | 85.5 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 6 | 3.9 | 0.15 | 0.44 | 0.80 | 0.00 | 3.7 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 3.85 | 11.43 | 18.03 | 2.00 | 81.1 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.83 | 11.00 | 17.47 | 7.00 | 88.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 3.07 | 9.62 | 16.19 | -1.00 | 73.6 | 90.0 |
| Bench 2 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 2.07 | 6.12 | 10.13 | 0.00 | 71.8 | 90.0 |
| Bench 3 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.02 | 5.95 | 9.97 | 8.00 | 72.2 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.7 | 5.87 | 17.79 | 27.99 | 17.00 | 87.7 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.67 | 12.71 | 21.25 | 9.00 | 79.8 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.47 | 9.39 | 15.55 | 2.00 | 70.2 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 7.33 | 23.20 | 36.99 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.03 | 22.77 | 37.48 | 21.00 | 90.0 | 86.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.17 | 18.52 | 30.09 | 1.00 | 85.4 | 23.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.20 | 11.07 | 17.58 | 3.00 | 74.8 | 90.0 |
| Bench 4 | Bench | Tyler Dibling | MID | 17 | 4.5 | 1.97 | 5.67 | 9.18 | 1.00 | 61.8 | 45.0 |

## GW18

- Train rows: 145070
- Bank: 0.10 -> 2.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 72.02
- Actual score: 71.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.77) beats the best remaining Bench Boost opportunity (8.10).
- Transfer: Bukayo Saka -> Bruno Borges Fernandes (projected gain 7.63, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.77) beats the best remaining Bench Boost opportunity (8.10).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 4.03 | 10.99 | 17.65 | 6.00 | 87.8 | 90.0 |
| Bench 1 | Bench Boost | Marcus Bettinelli | GK | 6 | 3.9 | 0.26 | 0.55 | 0.86 | 0.00 | 5.1 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.61 | 12.86 | 20.57 | 7.00 | 88.7 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 3.08 | 9.54 | 15.89 | 1.00 | 79.7 | 9.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.16 | 9.36 | 15.15 | 6.00 | 74.4 | 90.0 |
| Bench 2 | Bench Boost | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.56 | 6.91 | 11.12 | 2.00 | 77.9 | 90.0 |
| Bench 4 | Bench Boost | Cameron Burgess | DEF | 10 | 4.0 | 1.91 | 6.26 | 10.16 | 0.00 | 77.9 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 7.34 | 20.83 | 32.88 | 8.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.59 | 12.97 | 21.99 | 12.00 | 82.7 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 2.75 | 8.84 | 14.78 | 0.00 | 66.6 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.4 | 9.71 | 25.63 | 42.27 | 9.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.54 | 23.26 | 37.46 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 5.27 | 14.46 | 24.48 | -2.00 | 90.0 | 46.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.45 | 10.49 | 17.18 | 2.00 | 76.9 | 90.0 |
| Bench 3 | Bench Boost | Tyler Dibling | MID | 17 | 4.5 | 2.04 | 5.64 | 9.16 | 1.00 | 55.3 | 17.0 |

## GW19

- Train rows: 145775
- Bank: 2.10 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 72.76
- Actual score: 81.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.68) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Tyler Dibling -> Ismaïla Sarr (projected gain 5.61, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.68) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Taylor Harwood-Bellis replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.83 | 11.00 | 17.83 | 2.00 | 88.3 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 6 | 3.9 | 0.33 | 0.76 | 1.15 | 0.00 | 7.8 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.34 | 12.59 | 20.90 | 2.00 | 89.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.97 | 11.42 | 19.09 | 12.00 | 84.8 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 2.53 | 7.88 | 13.79 | 4.00 | 52.7 | 90.0 |
| Bench 2 | Autosub In | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.42 | 7.05 | 11.49 | 0.00 | 79.4 | 90.0 |
| Bench 3 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 1.23 | 3.94 | 6.81 | 0.00 | 45.7 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 7.17 | 20.00 | 31.61 | 7.00 | 80.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 5.45 | 15.35 | 25.58 | 1.00 | 90.0 | 45.0 |
| Bench 4 | Bench | Jamie Vardy | FWD | 11 | 5.6 | 1.08 | 4.37 | 7.60 | 2.00 | 20.7 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.5 | 8.68 | 25.39 | 41.35 | 16.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.77 | 22.65 | 37.24 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ismaïla Sarr | MID | 7 | 5.9 | 4.90 | 12.57 | 20.23 | 2.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.98 | 11.09 | 18.00 | 1.00 | 80.8 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.4 | 2.78 | 8.81 | 15.74 | 0.00 | 46.2 | 0.0 |