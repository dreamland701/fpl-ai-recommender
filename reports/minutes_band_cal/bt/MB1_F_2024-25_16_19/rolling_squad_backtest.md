# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 253.53
- Total actual points: 284.00
- Average predicted points: 63.38
- Average actual points: 71.00
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
- Predicted score: 60.25
- Actual score: 61.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Dean Henderson | GK | 7 | 4.4 | 2.80 | 8.26 | 13.71 | 2.00 | 81.5 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 6 | 3.9 | 0.09 | 0.34 | 0.69 | 0.00 | 2.8 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.30 | 12.74 | 19.58 | 6.00 | 84.5 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.1 | 3.50 | 10.03 | 16.85 | 7.00 | 72.6 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 3.70 | 9.99 | 17.01 | 6.00 | 80.9 | 62.0 |
| Bench 2 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 2.29 | 6.56 | 10.76 | 2.00 | 75.2 | 90.0 |
| Bench 3 | Bench | Dara O'Shea | DEF | 10 | 4.0 | 2.08 | 6.13 | 9.90 | 2.00 | 79.1 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.6 | 5.59 | 15.27 | 24.71 | 11.00 | 82.7 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.32 | 12.58 | 20.43 | 9.00 | 79.7 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.84 | 11.23 | 18.01 | 1.00 | 82.1 | 58.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 7.74 | 22.27 | 36.18 | 3.00 | 82.7 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 6.91 | 20.77 | 35.56 | 5.00 | 82.7 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 5.74 | 17.23 | 27.70 | 3.00 | 80.2 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 4.07 | 12.39 | 19.59 | 5.00 | 83.7 | 90.0 |
| Bench 4 | Bench | Yehor Yarmoliuk | MID | 4 | 4.4 | 2.01 | 5.99 | 9.54 | 2.00 | 53.9 | 74.0 |

## GW17

- Train rows: 144369
- Bank: 0.00 -> 0.80
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 57.94
- Actual score: 67.00
- Transfer: Pedro Porro -> Antonee Robinson (projected gain 1.80, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Dean Henderson | GK | 7 | 4.4 | 2.45 | 7.74 | 12.96 | 0.00 | 82.4 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 6 | 3.9 | 0.10 | 0.41 | 0.76 | 0.00 | 2.8 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 3.94 | 11.75 | 18.66 | 2.00 | 79.2 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.8 | 4.46 | 11.50 | 18.55 | 6.00 | 82.7 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.1 | 3.75 | 11.09 | 18.46 | 0.00 | 84.5 | 90.0 |
| Bench 2 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 2.15 | 6.38 | 10.73 | 0.00 | 75.5 | 90.0 |
| Bench 4 | Bench | Dara O'Shea | DEF | 10 | 4.0 | 2.04 | 6.17 | 9.97 | 0.00 | 79.5 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.7 | 5.88 | 17.74 | 27.83 | 17.00 | 84.8 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.63 | 12.53 | 20.81 | 9.00 | 80.7 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.63 | 10.01 | 16.66 | 2.00 | 74.9 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 6.82 | 21.66 | 34.96 | 3.00 | 82.7 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 6.60 | 21.18 | 35.67 | 21.00 | 82.7 | 86.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 5.69 | 17.22 | 28.46 | 1.00 | 78.8 | 23.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.26 | 11.51 | 18.25 | 3.00 | 75.8 | 90.0 |
| Bench 3 | Bench | Yehor Yarmoliuk | MID | 4 | 4.4 | 2.10 | 6.07 | 9.55 | 0.00 | 54.5 | 0.0 |

## GW18

- Train rows: 145070
- Bank: 0.80 -> 1.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 65.16
- Actual score: 71.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (4.85) beats the best remaining Bench Boost opportunity (5.77).
- Transfer: Bukayo Saka -> Son Heung-min (projected gain 7.87, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (4.85) beats the best remaining Bench Boost opportunity (5.77).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Dean Henderson | GK | 7 | 4.4 | 2.40 | 6.97 | 11.28 | 7.00 | 81.7 | 90.0 |
| Bench 1 | Bench Boost | Marcus Bettinelli | GK | 6 | 3.9 | 0.22 | 0.49 | 0.85 | 0.00 | 4.3 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.08 | 11.37 | 18.67 | 7.00 | 80.8 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.8 | 2.96 | 9.65 | 15.24 | 1.00 | 79.1 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.24 | 9.50 | 15.45 | 2.00 | 81.3 | 90.0 |
| Bench 2 | Bench Boost | Cameron Burgess | DEF | 10 | 4.0 | 1.81 | 6.05 | 9.87 | 0.00 | 79.1 | 0.0 |
| Bench 3 | Bench Boost | Dara O'Shea | DEF | 10 | 4.0 | 1.77 | 5.77 | 9.54 | 2.00 | 80.2 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 6.78 | 19.67 | 31.01 | 8.00 | 82.8 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.63 | 12.88 | 21.66 | 12.00 | 80.3 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 2.82 | 9.26 | 15.49 | 0.00 | 70.1 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.4 | 9.23 | 24.25 | 40.42 | 9.00 | 82.8 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.08 | 21.70 | 35.53 | 10.00 | 82.8 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.8 | 4.44 | 13.89 | 22.85 | 2.00 | 81.3 | 80.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.42 | 10.52 | 17.00 | 2.00 | 76.7 | 90.0 |
| Bench 4 | Bench Boost | Yehor Yarmoliuk | MID | 4 | 4.4 | 1.06 | 3.35 | 5.80 | 0.00 | 26.9 | 18.0 |

## GW19

- Train rows: 145775
- Bank: 1.40 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 70.18
- Actual score: 85.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.18) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Cameron Burgess -> Lewis Hall (projected gain 5.41, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.18) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Dean Henderson | GK | 7 | 4.4 | 2.91 | 7.32 | 12.04 | 2.00 | 81.0 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 6 | 3.9 | 0.31 | 0.73 | 1.14 | 0.00 | 7.0 | 0.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.7 | 4.12 | 11.74 | 19.09 | 12.00 | 82.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 3.78 | 11.06 | 18.88 | 2.00 | 81.5 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.74 | 10.22 | 16.38 | 6.00 | 79.6 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.8 | 3.33 | 9.89 | 16.40 | 4.00 | 82.7 | 90.0 |
| Bench 2 | Bench | Dara O'Shea | DEF | 10 | 4.0 | 2.25 | 6.43 | 10.24 | 5.00 | 81.4 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 7.12 | 20.50 | 31.92 | 7.00 | 79.7 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.87 | 13.75 | 23.27 | 1.00 | 82.7 | 45.0 |
| Bench 3 | Bench | Jamie Vardy | FWD | 11 | 5.6 | 0.99 | 4.36 | 7.61 | 2.00 | 19.5 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.5 | 8.18 | 23.82 | 39.16 | 16.00 | 82.7 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.31 | 21.30 | 35.65 | 2.00 | 82.7 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.8 | 4.47 | 13.49 | 22.41 | 0.00 | 76.8 | 63.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.98 | 11.14 | 17.89 | 1.00 | 81.0 | 90.0 |
| Bench 4 | Bench | Yehor Yarmoliuk | MID | 4 | 4.4 | 0.90 | 3.64 | 6.35 | 2.00 | 31.3 | 90.0 |