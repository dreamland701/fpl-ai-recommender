# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 267.54
- Total actual points: 307.00
- Average predicted points: 66.88
- Average actual points: 76.75
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
- Predicted score: 63.47
- Actual score: 60.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.74 | 10.70 | 17.12 | 6.00 | 87.4 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 6 | 3.9 | 0.14 | 0.41 | 0.74 | 0.00 | 3.6 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.20 | 12.65 | 19.47 | 6.00 | 85.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.21 | 11.55 | 19.13 | 6.00 | 88.3 | 62.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.7 | 3.04 | 9.36 | 15.11 | 1.00 | 80.8 | 90.0 |
| Bench 2 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 2.20 | 6.34 | 10.34 | 2.00 | 71.1 | 90.0 |
| Bench 3 | Bench | Dara O'Shea | DEF | 10 | 4.0 | 2.07 | 6.18 | 10.12 | 2.00 | 77.3 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.6 | 6.05 | 16.74 | 26.67 | 11.00 | 90.0 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.27 | 12.59 | 20.48 | 9.00 | 81.0 | 90.0 |
| Bench 4 | Bench | Will Lankshear | FWD | 18 | 4.5 | 0.68 | 1.56 | 2.58 | 1.00 | 8.1 | 8.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 8.20 | 23.77 | 38.10 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.38 | 22.27 | 37.50 | 5.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.22 | 18.77 | 29.75 | 3.00 | 87.1 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.96 | 12.28 | 19.49 | 5.00 | 84.1 | 90.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.7 | 4.01 | 12.24 | 21.18 | 2.00 | 90.0 | 90.0 |

## GW17

- Train rows: 144369
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 60.50
- Actual score: 71.00
- Transfer: Daniel Muñoz -> Lewis Hall (projected gain 4.75, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.70 | 10.74 | 17.29 | 3.00 | 85.9 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 6 | 3.9 | 0.14 | 0.48 | 0.82 | 0.00 | 3.6 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 3.88 | 11.74 | 18.65 | 2.00 | 80.3 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.80 | 10.89 | 17.22 | 7.00 | 87.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 3.04 | 9.74 | 16.45 | -1.00 | 73.5 | 90.0 |
| Bench 3 | Bench | Dara O'Shea | DEF | 10 | 4.0 | 2.04 | 6.19 | 10.18 | 0.00 | 77.8 | 90.0 |
| Bench 2 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 2.07 | 6.17 | 10.31 | 0.00 | 71.5 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.7 | 5.76 | 17.61 | 27.63 | 17.00 | 85.0 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.67 | 12.65 | 21.12 | 9.00 | 79.8 | 90.0 |
| Bench 4 | Bench | Will Lankshear | FWD | 18 | 4.5 | 0.38 | 1.78 | 3.05 | 0.00 | 10.4 | 0.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 7.31 | 23.17 | 36.92 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.12 | 22.77 | 37.74 | 21.00 | 90.0 | 86.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.23 | 18.83 | 30.59 | 1.00 | 86.4 | 23.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.7 | 4.49 | 11.53 | 18.94 | 3.00 | 87.7 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.17 | 11.28 | 17.80 | 3.00 | 71.6 | 90.0 |

## GW18

- Train rows: 145070
- Bank: 0.10 -> 2.90
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 69.01
- Actual score: 77.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (4.05) beats the best remaining Bench Boost opportunity (4.98).
- Transfer: Bukayo Saka -> Bryan Mbeumo (projected gain 8.37, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (4.05) beats the best remaining Bench Boost opportunity (4.98).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 4.11 | 11.21 | 17.99 | 6.00 | 87.9 | 90.0 |
| Bench 1 | Bench Boost | Marcus Bettinelli | GK | 6 | 3.9 | 0.27 | 0.57 | 0.91 | 0.00 | 5.2 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.61 | 12.96 | 20.75 | 7.00 | 88.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.14 | 9.45 | 15.20 | 6.00 | 72.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 3.03 | 9.39 | 15.76 | 1.00 | 78.8 | 9.0 |
| Bench 2 | Bench Boost | Cameron Burgess | DEF | 10 | 4.0 | 1.80 | 6.09 | 10.09 | 0.00 | 77.4 | 0.0 |
| Bench 3 | Bench Boost | Dara O'Shea | DEF | 10 | 4.0 | 1.76 | 5.82 | 9.78 | 2.00 | 78.6 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 7.21 | 20.99 | 32.68 | 8.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.61 | 12.95 | 21.79 | 12.00 | 82.3 | 90.0 |
| Bench 4 | Bench Boost | Will Lankshear | FWD | 18 | 4.5 | 0.22 | 1.27 | 2.17 | 0.00 | 6.7 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.4 | 9.73 | 25.78 | 42.35 | 9.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.57 | 23.20 | 37.45 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 4.92 | 14.37 | 23.74 | 3.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.43 | 10.58 | 17.23 | 2.00 | 75.2 | 90.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.7 | 2.88 | 9.43 | 15.24 | 2.00 | 73.1 | 90.0 |

## GW19

- Train rows: 145775
- Bank: 2.90 -> 1.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 74.56
- Actual score: 99.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.71) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Pedro Porro -> Trent Alexander-Arnold (projected gain 4.19, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.71) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.89 | 11.14 | 18.01 | 2.00 | 88.8 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 6 | 3.9 | 0.36 | 0.81 | 1.21 | 0.00 | 7.9 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.34 | 12.72 | 21.03 | 2.00 | 89.2 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.1 | 4.15 | 12.05 | 19.05 | 15.00 | 71.1 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 4.06 | 11.72 | 19.11 | 12.00 | 83.8 | 90.0 |
| Bench 2 | Bench | Dara O'Shea | DEF | 10 | 4.0 | 2.25 | 6.50 | 10.49 | 5.00 | 79.9 | 90.0 |
| Bench 3 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 1.22 | 3.93 | 6.72 | 0.00 | 46.3 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 7.08 | 20.48 | 31.89 | 7.00 | 77.3 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 5.41 | 15.39 | 25.38 | 1.00 | 90.0 | 45.0 |
| Bench 4 | Bench | Will Lankshear | FWD | 18 | 4.5 | 0.55 | 1.61 | 2.60 | 0.00 | 9.2 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.5 | 8.71 | 25.39 | 41.14 | 16.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.86 | 22.92 | 37.67 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 4.11 | 13.58 | 22.22 | 7.00 | 87.5 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.99 | 11.23 | 18.12 | 1.00 | 79.7 | 90.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.7 | 3.56 | 10.57 | 16.78 | 2.00 | 81.1 | 90.0 |