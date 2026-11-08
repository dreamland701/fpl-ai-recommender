# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 266.40
- Total actual points: 292.00
- Average predicted points: 66.60
- Average actual points: 73.00
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
- Actual score: 60.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.65 | 10.57 | 17.06 | 6.00 | 85.4 | 90.0 |
| Bench 1 | Bench | João Neves Virgínia | GK | 8 | 3.9 | 0.00 | 0.42 | 0.88 | 0.00 | 8.5 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.12 | 12.51 | 19.42 | 6.00 | 83.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.17 | 11.50 | 19.16 | 6.00 | 87.7 | 62.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.7 | 2.96 | 9.24 | 15.07 | 1.00 | 79.1 | 90.0 |
| Bench 2 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 2.15 | 6.27 | 10.37 | 2.00 | 70.3 | 90.0 |
| Bench 3 | Bench | Dara O'Shea | DEF | 10 | 4.0 | 2.00 | 6.07 | 10.10 | 2.00 | 75.7 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.6 | 5.95 | 16.59 | 26.61 | 11.00 | 88.3 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.19 | 12.49 | 20.46 | 9.00 | 79.3 | 90.0 |
| Bench 4 | Bench | Will Lankshear | FWD | 18 | 4.5 | 0.69 | 1.59 | 2.70 | 1.00 | 9.2 | 8.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 8.09 | 23.57 | 38.01 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.32 | 22.18 | 37.51 | 5.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.10 | 18.57 | 29.63 | 3.00 | 84.3 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 4.37 | 13.58 | 21.87 | 5.00 | 90.0 | 90.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.7 | 4.05 | 13.17 | 22.11 | 2.00 | 90.0 | 90.0 |

## GW17

- Train rows: 144369
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 61.24
- Actual score: 71.00
- Transfer: Daniel Muñoz -> Lewis Hall (projected gain 4.65, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.74 | 10.79 | 17.28 | 3.00 | 87.0 | 90.0 |
| Bench 1 | Bench | João Neves Virgínia | GK | 8 | 3.9 | 0.05 | 0.32 | 0.59 | 0.00 | 1.8 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 3.91 | 11.77 | 18.64 | 2.00 | 81.1 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.81 | 10.89 | 17.16 | 7.00 | 87.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 3.16 | 9.91 | 16.60 | -1.00 | 77.0 | 90.0 |
| Bench 2 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 2.13 | 6.27 | 10.38 | 0.00 | 73.4 | 90.0 |
| Bench 3 | Bench | Dara O'Shea | DEF | 10 | 4.0 | 2.08 | 6.24 | 10.20 | 0.00 | 78.9 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.7 | 5.77 | 17.60 | 27.59 | 17.00 | 85.4 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.71 | 12.70 | 21.12 | 9.00 | 80.9 | 90.0 |
| Bench 4 | Bench | Will Lankshear | FWD | 18 | 4.5 | 0.25 | 1.61 | 2.85 | 0.00 | 6.1 | 0.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 7.30 | 23.14 | 36.86 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.17 | 22.86 | 37.79 | 21.00 | 90.0 | 86.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.25 | 18.87 | 30.56 | 1.00 | 87.1 | 23.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.7 | 4.94 | 12.67 | 20.77 | 3.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.19 | 11.32 | 17.79 | 3.00 | 72.7 | 90.0 |

## GW18

- Train rows: 145070
- Bank: 0.10 -> 3.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 69.12
- Actual score: 74.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (3.67) beats the best remaining Bench Boost opportunity (4.50).
- Transfer: Bukayo Saka -> Luis Díaz (projected gain 9.12, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (3.67) beats the best remaining Bench Boost opportunity (4.50).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 4.03 | 11.08 | 17.95 | 6.00 | 86.2 | 90.0 |
| Bench 1 | Bench Boost | João Neves Virgínia | GK | 8 | 3.9 | 0.02 | 0.45 | 1.00 | 0.00 | 8.6 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.54 | 12.82 | 20.73 | 7.00 | 86.3 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 2.99 | 9.33 | 15.81 | 1.00 | 78.5 | 9.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.05 | 9.29 | 15.12 | 6.00 | 70.8 | 90.0 |
| Bench 2 | Bench Boost | Cameron Burgess | DEF | 10 | 4.0 | 1.72 | 5.96 | 10.07 | 0.00 | 75.6 | 0.0 |
| Bench 3 | Bench Boost | Dara O'Shea | DEF | 10 | 4.0 | 1.69 | 5.68 | 9.75 | 2.00 | 76.8 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 7.12 | 20.82 | 32.63 | 8.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.53 | 12.80 | 21.71 | 12.00 | 80.5 | 90.0 |
| Bench 4 | Bench Boost | Will Lankshear | FWD | 18 | 4.5 | 0.24 | 1.31 | 2.33 | 0.00 | 8.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.4 | 9.67 | 25.66 | 42.36 | 9.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.45 | 23.00 | 37.36 | 10.00 | 90.0 | 90.0 |
| XI | XI | Luis Díaz | MID | 12 | 7.5 | 6.24 | 15.02 | 23.37 | 0.00 | 79.7 | 0.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.36 | 10.47 | 17.21 | 2.00 | 74.1 | 90.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.7 | 2.81 | 9.31 | 15.22 | 2.00 | 71.4 | 90.0 |

## GW19

- Train rows: 145775
- Bank: 3.00 -> 3.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 72.97
- Actual score: 87.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.60) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Luis Díaz -> Anthony Gordon (projected gain 6.65, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.60) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.82 | 11.04 | 17.96 | 2.00 | 87.2 | 90.0 |
| Bench 1 | Bench | João Neves Virgínia | GK | 8 | 3.9 | 0.24 | 0.77 | 1.36 | 0.00 | 11.1 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.28 | 12.63 | 21.01 | 2.00 | 87.6 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.97 | 11.56 | 19.02 | 12.00 | 81.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 2.59 | 7.92 | 13.85 | 4.00 | 54.5 | 90.0 |
| Bench 2 | Bench | Dara O'Shea | DEF | 10 | 4.0 | 2.19 | 6.40 | 10.45 | 5.00 | 78.6 | 90.0 |
| Bench 3 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 1.20 | 3.90 | 6.75 | 0.00 | 46.4 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 7.03 | 20.37 | 31.89 | 7.00 | 76.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 5.33 | 15.24 | 25.30 | 1.00 | 90.0 | 45.0 |
| Bench 4 | Bench | Will Lankshear | FWD | 18 | 4.5 | 0.59 | 1.66 | 2.74 | 0.00 | 10.8 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.5 | 8.60 | 25.22 | 41.02 | 16.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.77 | 22.80 | 37.63 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 4.94 | 14.30 | 23.03 | 6.00 | 78.8 | 84.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.93 | 11.14 | 18.10 | 1.00 | 78.5 | 90.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.7 | 3.49 | 10.46 | 16.74 | 2.00 | 79.5 | 90.0 |