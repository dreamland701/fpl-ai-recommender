# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 264.96
- Total actual points: 307.00
- Average predicted points: 66.24
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
- Predicted score: 62.54
- Actual score: 60.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.66 | 10.60 | 17.11 | 6.00 | 85.6 | 90.0 |
| Bench 1 | Bench | João Neves Virgínia | GK | 8 | 3.9 | 0.00 | 0.42 | 0.88 | 0.00 | 8.5 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.12 | 12.52 | 19.43 | 6.00 | 83.1 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.17 | 11.51 | 19.18 | 6.00 | 87.8 | 62.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.7 | 2.97 | 9.27 | 15.10 | 1.00 | 79.3 | 90.0 |
| Bench 2 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 2.16 | 6.28 | 10.38 | 2.00 | 70.3 | 90.0 |
| Bench 3 | Bench | Dara O'Shea | DEF | 10 | 4.0 | 2.00 | 6.08 | 10.12 | 2.00 | 75.8 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.6 | 5.96 | 16.61 | 26.63 | 11.00 | 88.5 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.19 | 12.50 | 20.47 | 9.00 | 79.4 | 90.0 |
| Bench 4 | Bench | Will Lankshear | FWD | 18 | 4.5 | 0.70 | 1.59 | 2.71 | 1.00 | 9.3 | 8.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 8.10 | 23.60 | 38.01 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.32 | 22.17 | 37.50 | 5.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.12 | 18.62 | 29.69 | 3.00 | 84.5 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.89 | 12.18 | 19.48 | 5.00 | 82.5 | 90.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.7 | 3.94 | 12.14 | 21.18 | 2.00 | 90.0 | 90.0 |

## GW17

- Train rows: 144369
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 60.93
- Actual score: 71.00
- Transfer: Daniel Muñoz -> Lewis Hall (projected gain 4.69, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.75 | 10.82 | 17.32 | 3.00 | 87.2 | 90.0 |
| Bench 1 | Bench | João Neves Virgínia | GK | 8 | 3.9 | 0.05 | 0.31 | 0.58 | 0.00 | 1.7 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 3.92 | 11.78 | 18.64 | 2.00 | 81.2 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.83 | 10.93 | 17.23 | 7.00 | 87.7 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 3.16 | 9.91 | 16.60 | -1.00 | 76.9 | 90.0 |
| Bench 2 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 2.13 | 6.27 | 10.39 | 0.00 | 73.4 | 90.0 |
| Bench 3 | Bench | Dara O'Shea | DEF | 10 | 4.0 | 2.08 | 6.25 | 10.22 | 0.00 | 79.0 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.7 | 5.78 | 17.62 | 27.60 | 17.00 | 85.4 | 72.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.71 | 12.71 | 21.14 | 9.00 | 81.0 | 90.0 |
| Bench 4 | Bench | Will Lankshear | FWD | 18 | 4.5 | 0.25 | 1.61 | 2.84 | 0.00 | 6.1 | 0.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 7.31 | 23.15 | 36.86 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.17 | 22.84 | 37.79 | 21.00 | 90.0 | 86.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.26 | 18.87 | 30.59 | 1.00 | 87.2 | 23.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.7 | 4.52 | 11.57 | 18.94 | 3.00 | 88.5 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.21 | 11.33 | 17.83 | 3.00 | 72.8 | 90.0 |

## GW18

- Train rows: 145070
- Bank: 0.10 -> 2.90
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 67.83
- Actual score: 77.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (3.68) beats the best remaining Bench Boost opportunity (4.52).
- Transfer: Bukayo Saka -> Bryan Mbeumo (projected gain 8.34, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (3.68) beats the best remaining Bench Boost opportunity (4.52).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 4.04 | 11.10 | 18.00 | 6.00 | 86.4 | 90.0 |
| Bench 1 | Bench Boost | João Neves Virgínia | GK | 8 | 3.9 | 0.02 | 0.45 | 1.00 | 0.00 | 8.6 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.54 | 12.84 | 20.74 | 7.00 | 86.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 3.00 | 9.34 | 15.84 | 1.00 | 78.6 | 9.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.07 | 9.33 | 15.18 | 6.00 | 71.0 | 90.0 |
| Bench 2 | Bench Boost | Cameron Burgess | DEF | 10 | 4.0 | 1.72 | 5.97 | 10.09 | 0.00 | 75.7 | 0.0 |
| Bench 3 | Bench Boost | Dara O'Shea | DEF | 10 | 4.0 | 1.69 | 5.69 | 9.77 | 2.00 | 76.9 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 7.12 | 20.82 | 32.60 | 8.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.54 | 12.83 | 21.77 | 12.00 | 80.8 | 90.0 |
| Bench 4 | Bench Boost | Will Lankshear | FWD | 18 | 4.5 | 0.25 | 1.31 | 2.33 | 0.00 | 8.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.4 | 9.66 | 25.66 | 42.33 | 9.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.47 | 23.02 | 37.40 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 4.85 | 14.24 | 23.72 | 3.00 | 88.3 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.37 | 10.48 | 17.24 | 2.00 | 74.1 | 90.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.7 | 2.81 | 9.32 | 15.23 | 2.00 | 71.5 | 90.0 |

## GW19

- Train rows: 145775
- Bank: 2.90 -> 1.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 73.65
- Actual score: 99.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.61) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Pedro Porro -> Trent Alexander-Arnold (projected gain 4.00, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.61) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.83 | 11.06 | 18.00 | 2.00 | 87.4 | 90.0 |
| Bench 1 | Bench | João Neves Virgínia | GK | 8 | 3.9 | 0.24 | 0.77 | 1.35 | 0.00 | 11.1 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.29 | 12.64 | 21.03 | 2.00 | 87.8 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.1 | 4.08 | 11.94 | 19.02 | 15.00 | 69.4 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.99 | 11.62 | 19.10 | 12.00 | 82.3 | 90.0 |
| Bench 2 | Bench | Dara O'Shea | DEF | 10 | 4.0 | 2.20 | 6.42 | 10.48 | 5.00 | 78.7 | 90.0 |
| Bench 3 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 1.21 | 3.91 | 6.77 | 0.00 | 46.5 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 7.02 | 20.34 | 31.78 | 7.00 | 75.8 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 5.35 | 15.28 | 25.34 | 1.00 | 90.0 | 45.0 |
| Bench 4 | Bench | Will Lankshear | FWD | 18 | 4.5 | 0.59 | 1.67 | 2.75 | 0.00 | 10.8 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.5 | 8.61 | 25.23 | 41.04 | 16.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.78 | 22.79 | 37.63 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 4.05 | 13.49 | 22.20 | 7.00 | 86.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.94 | 11.15 | 18.11 | 1.00 | 78.6 | 90.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.7 | 3.50 | 10.48 | 16.76 | 2.00 | 79.6 | 90.0 |