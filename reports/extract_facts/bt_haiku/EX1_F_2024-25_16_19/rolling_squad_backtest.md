# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 268.93
- Total actual points: 292.00
- Average predicted points: 67.23
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
- Predicted score: 64.05
- Actual score: 60.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.73 | 10.68 | 17.08 | 6.00 | 87.1 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.29 | 0.61 | 1.03 | 0.00 | 6.6 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.19 | 12.63 | 19.46 | 6.00 | 84.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.20 | 11.54 | 19.11 | 6.00 | 88.2 | 62.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.7 | 3.03 | 9.34 | 15.08 | 1.00 | 80.5 | 90.0 |
| Bench 2 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 2.20 | 6.33 | 10.34 | 2.00 | 71.1 | 90.0 |
| Bench 3 | Bench | Dara O'Shea | DEF | 10 | 4.0 | 2.07 | 6.16 | 10.10 | 2.00 | 77.3 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.6 | 6.04 | 16.72 | 26.66 | 11.00 | 90.0 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.26 | 12.59 | 20.46 | 9.00 | 81.0 | 90.0 |
| Bench 4 | Bench | Will Lankshear | FWD | 18 | 4.5 | 0.68 | 1.56 | 2.58 | 1.00 | 8.0 | 8.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 8.20 | 23.74 | 38.11 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.38 | 22.27 | 37.51 | 5.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.20 | 18.73 | 29.69 | 3.00 | 86.9 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 4.48 | 13.74 | 21.92 | 5.00 | 90.0 | 90.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.7 | 4.13 | 13.28 | 22.11 | 2.00 | 90.0 | 90.0 |

## GW17

- Train rows: 144369
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 60.82
- Actual score: 71.00
- Transfer: Daniel Muñoz -> Lewis Hall (projected gain 4.71, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.69 | 10.71 | 17.24 | 3.00 | 85.7 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.25 | 0.55 | 0.94 | 0.00 | 6.5 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 3.88 | 11.73 | 18.65 | 2.00 | 80.2 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.78 | 10.85 | 17.16 | 7.00 | 86.7 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 3.04 | 9.74 | 16.45 | -1.00 | 73.5 | 90.0 |
| Bench 3 | Bench | Dara O'Shea | DEF | 10 | 4.0 | 2.04 | 6.18 | 10.17 | 0.00 | 77.7 | 90.0 |
| Bench 2 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 2.07 | 6.17 | 10.31 | 0.00 | 71.5 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.7 | 5.75 | 17.59 | 27.63 | 17.00 | 85.0 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.66 | 12.64 | 21.10 | 9.00 | 79.5 | 90.0 |
| Bench 4 | Bench | Will Lankshear | FWD | 18 | 4.5 | 0.37 | 1.79 | 3.05 | 0.00 | 10.4 | 0.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 7.30 | 23.15 | 36.91 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.12 | 22.78 | 37.73 | 21.00 | 90.0 | 86.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.21 | 18.83 | 30.56 | 1.00 | 86.3 | 23.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.7 | 4.94 | 12.69 | 20.82 | 3.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.15 | 11.26 | 17.76 | 3.00 | 71.5 | 90.0 |

## GW18

- Train rows: 145070
- Bank: 0.10 -> 3.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 70.25
- Actual score: 74.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (3.97) beats the best remaining Bench Boost opportunity (4.85).
- Transfer: Bukayo Saka -> Luis Díaz (projected gain 9.14, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (3.97) beats the best remaining Bench Boost opportunity (4.85).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 4.10 | 11.18 | 17.95 | 6.00 | 87.7 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.20 | 0.51 | 0.86 | 0.00 | 7.0 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.61 | 12.95 | 20.75 | 7.00 | 87.9 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.12 | 9.42 | 15.15 | 6.00 | 72.3 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 3.02 | 9.37 | 15.73 | 1.00 | 78.7 | 9.0 |
| Bench 2 | Bench Boost | Cameron Burgess | DEF | 10 | 4.0 | 1.79 | 6.08 | 10.08 | 0.00 | 77.3 | 0.0 |
| Bench 3 | Bench Boost | Dara O'Shea | DEF | 10 | 4.0 | 1.76 | 5.81 | 9.76 | 2.00 | 78.5 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 7.21 | 20.99 | 32.72 | 8.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.59 | 12.92 | 21.74 | 12.00 | 82.0 | 90.0 |
| Bench 4 | Bench Boost | Will Lankshear | FWD | 18 | 4.5 | 0.22 | 1.27 | 2.17 | 0.00 | 6.7 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.4 | 9.74 | 25.79 | 42.39 | 9.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.56 | 23.18 | 37.41 | 10.00 | 90.0 | 90.0 |
| XI | XI | Luis Díaz | MID | 12 | 7.5 | 6.30 | 15.15 | 23.40 | 0.00 | 81.0 | 0.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.41 | 10.57 | 17.21 | 2.00 | 75.2 | 90.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.7 | 2.88 | 9.43 | 15.23 | 2.00 | 73.0 | 90.0 |

## GW19

- Train rows: 145775
- Bank: 3.00 -> 3.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 73.81
- Actual score: 87.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.70) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Luis Díaz -> Anthony Gordon (projected gain 6.74, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.70) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.88 | 11.12 | 17.97 | 2.00 | 88.6 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.08 | 0.61 | 0.99 | 0.00 | 9.5 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.34 | 12.72 | 21.01 | 2.00 | 89.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 4.03 | 11.66 | 19.04 | 12.00 | 83.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 2.55 | 7.87 | 13.72 | 4.00 | 52.8 | 90.0 |
| Bench 2 | Bench | Dara O'Shea | DEF | 10 | 4.0 | 2.24 | 6.49 | 10.46 | 5.00 | 79.8 | 90.0 |
| Bench 3 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 1.21 | 3.92 | 6.70 | 0.00 | 46.2 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 7.09 | 20.51 | 32.00 | 7.00 | 77.5 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 5.40 | 15.35 | 25.34 | 1.00 | 90.0 | 45.0 |
| Bench 4 | Bench | Will Lankshear | FWD | 18 | 4.5 | 0.55 | 1.61 | 2.60 | 0.00 | 9.1 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.5 | 8.70 | 25.38 | 41.12 | 16.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.85 | 22.92 | 37.67 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 5.01 | 14.42 | 23.07 | 6.00 | 80.6 | 84.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.98 | 11.22 | 18.12 | 1.00 | 79.6 | 90.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.7 | 3.55 | 10.56 | 16.76 | 2.00 | 81.0 | 90.0 |