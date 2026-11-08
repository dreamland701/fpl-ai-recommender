# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 256.19
- Total actual points: 285.00
- Average predicted points: 64.05
- Average actual points: 71.25
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
- Predicted score: 60.17
- Actual score: 59.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.33 | 9.37 | 15.18 | 6.00 | 80.6 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 6 | 3.9 | 0.14 | 0.44 | 0.81 | 0.00 | 3.8 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.15 | 12.52 | 19.30 | 6.00 | 83.1 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 3.80 | 10.22 | 17.19 | 6.00 | 81.3 | 62.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.7 | 2.94 | 9.15 | 14.79 | 1.00 | 78.2 | 90.0 |
| Bench 2 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.52 | 6.68 | 11.07 | 0.00 | 76.1 | 90.0 |
| Bench 4 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 2.32 | 6.63 | 10.84 | 2.00 | 75.5 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.6 | 5.68 | 15.50 | 24.89 | 11.00 | 83.1 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.17 | 12.36 | 20.14 | 9.00 | 78.4 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.69 | 11.02 | 17.72 | 1.00 | 80.7 | 58.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 7.83 | 22.50 | 36.36 | 3.00 | 83.1 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.01 | 21.00 | 35.74 | 5.00 | 83.1 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 5.83 | 17.46 | 27.88 | 3.00 | 80.6 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.91 | 12.17 | 19.30 | 5.00 | 82.3 | 90.0 |
| Bench 3 | Bench | Tyler Dibling | MID | 17 | 4.5 | 2.44 | 6.39 | 10.19 | 2.00 | 65.8 | 90.0 |

## GW17

- Train rows: 144369
- Bank: 0.00 -> 0.80
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 57.79
- Actual score: 70.00
- Transfer: Pedro Porro -> Antonee Robinson (projected gain 2.05, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.60 | 10.53 | 16.97 | 3.00 | 83.4 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 6 | 3.9 | 0.14 | 0.51 | 0.89 | 0.00 | 3.8 | 0.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.8 | 4.56 | 11.74 | 18.74 | 6.00 | 83.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 3.79 | 11.54 | 18.38 | 2.00 | 77.9 | 90.0 |
| Bench 4 | Bench | Daniel Muñoz | DEF | 7 | 4.7 | 1.63 | 6.68 | 11.12 | 0.00 | 62.2 | 0.0 |
| XI | XI | Cameron Burgess | DEF | 10 | 4.0 | 2.18 | 6.47 | 10.82 | 0.00 | 75.8 | 90.0 |
| Bench 3 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.05 | 5.98 | 9.98 | 8.00 | 73.0 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.7 | 5.72 | 17.53 | 27.55 | 17.00 | 83.6 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.62 | 12.53 | 20.95 | 9.00 | 79.9 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.66 | 10.10 | 16.75 | 2.00 | 75.3 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 6.93 | 21.90 | 35.15 | 3.00 | 83.1 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 6.71 | 21.42 | 35.86 | 21.00 | 83.1 | 86.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 5.80 | 17.46 | 28.65 | 1.00 | 79.2 | 23.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.29 | 11.59 | 18.34 | 3.00 | 76.2 | 90.0 |
| Bench 2 | Bench | Tyler Dibling | MID | 17 | 4.5 | 2.07 | 5.89 | 9.64 | 1.00 | 65.6 | 45.0 |

## GW18

- Train rows: 145070
- Bank: 0.80 -> 1.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 67.16
- Actual score: 75.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.05) beats the best remaining Bench Boost opportunity (7.64).
- Transfer: Bukayo Saka -> Son Heung-min (projected gain 7.57, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.05) beats the best remaining Bench Boost opportunity (7.64).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.68 | 9.87 | 16.06 | 6.00 | 80.9 | 90.0 |
| Bench 1 | Bench Boost | Marcus Bettinelli | GK | 6 | 3.9 | 0.27 | 0.59 | 0.97 | 0.00 | 5.3 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.18 | 11.61 | 18.84 | 7.00 | 81.1 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.8 | 2.95 | 9.68 | 15.39 | 1.00 | 78.2 | 90.0 |
| XI | XI | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.55 | 6.73 | 10.97 | 2.00 | 79.0 | 90.0 |
| Bench 4 | Bench Boost | Daniel Muñoz | DEF | 7 | 4.7 | 1.68 | 6.08 | 10.44 | 6.00 | 52.0 | 90.0 |
| Bench 3 | Bench Boost | Cameron Burgess | DEF | 10 | 4.0 | 1.79 | 6.07 | 10.01 | 0.00 | 78.2 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 6.88 | 19.91 | 31.18 | 8.00 | 83.1 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.48 | 12.64 | 21.40 | 12.00 | 79.1 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 2.85 | 9.33 | 15.56 | 0.00 | 70.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.4 | 9.33 | 24.49 | 40.59 | 9.00 | 83.1 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.18 | 21.94 | 35.70 | 10.00 | 83.1 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.8 | 4.29 | 13.66 | 22.59 | 2.00 | 80.2 | 80.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.41 | 10.55 | 17.14 | 2.00 | 75.8 | 90.0 |
| Bench 2 | Bench Boost | Tyler Dibling | MID | 17 | 4.5 | 2.31 | 6.17 | 10.04 | 1.00 | 61.8 | 17.0 |

## GW19

- Train rows: 145775
- Bank: 1.40 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 71.07
- Actual score: 81.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.30) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Cameron Burgess -> Lewis Hall (projected gain 4.39, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.30) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.45 | 9.77 | 16.06 | 2.00 | 81.7 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 6 | 3.9 | 0.36 | 0.83 | 1.27 | 0.00 | 8.0 | 0.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.7 | 3.96 | 11.49 | 18.80 | 12.00 | 81.3 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 3.90 | 11.34 | 19.09 | 2.00 | 82.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.8 | 3.45 | 10.16 | 16.61 | 4.00 | 83.2 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.7 | 3.48 | 8.91 | 14.14 | 2.00 | 76.0 | 90.0 |
| Bench 2 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.47 | 7.19 | 11.57 | 0.00 | 80.4 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 7.12 | 20.55 | 32.08 | 7.00 | 78.9 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.98 | 14.03 | 23.48 | 1.00 | 83.2 | 45.0 |
| Bench 4 | Bench | Jamie Vardy | FWD | 11 | 5.6 | 1.04 | 4.44 | 7.69 | 2.00 | 20.4 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.5 | 8.30 | 24.09 | 39.37 | 16.00 | 83.2 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.43 | 21.58 | 35.86 | 2.00 | 83.2 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.8 | 4.46 | 13.54 | 22.57 | 0.00 | 75.9 | 63.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.97 | 11.19 | 18.06 | 1.00 | 80.1 | 90.0 |
| Bench 3 | Bench | Tyler Dibling | MID | 17 | 4.5 | 1.84 | 5.79 | 9.44 | 8.00 | 51.5 | 85.0 |