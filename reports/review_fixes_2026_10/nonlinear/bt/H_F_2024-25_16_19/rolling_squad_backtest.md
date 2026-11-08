# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 256.92
- Total actual points: 238.00
- Average predicted points: 64.23
- Average actual points: 59.50
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
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 65.40
- Actual score: 41.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.93 | 10.84 | 18.64 | 6.00 | 88.5 | 90.0 |
| Bench 1 | Bench | Emiliano Martínez Romero | GK | 2 | 5.0 | 3.00 | 10.22 | 17.81 | 2.00 | 84.3 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.09 | 12.89 | 22.63 | 6.00 | 86.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 4.72 | 12.81 | 21.54 | 1.00 | 83.1 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.0 | 5.24 | 12.07 | 20.54 | 1.00 | 79.7 | 78.0 |
| Bench 3 | Bench | Marc Cucurella Saseta | DEF | 6 | 5.1 | 2.63 | 9.88 | 19.02 | 5.00 | 76.0 | 90.0 |
| Bench 2 | Bench | Marc Guéhi | DEF | 7 | 4.5 | 3.00 | 9.16 | 15.49 | -1.00 | 85.4 | 90.0 |
| XI | XI | Adam Armstrong | FWD | 17 | 5.1 | 3.60 | 9.63 | 15.09 | 2.00 | 74.6 | 81.0 |
| XI | XI | Cameron Archer | FWD | 17 | 5.0 | 3.65 | 9.62 | 16.64 | 1.00 | 62.3 | 8.0 |
| Bench 4 | Bench | Will Lankshear | FWD | 18 | 4.5 | 0.70 | 1.72 | 2.16 | 1.00 | 12.3 | 8.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 10.6 | 7.91 | 23.90 | 34.92 | 3.00 | 83.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.1 | 7.20 | 23.13 | 38.18 | 3.00 | 84.2 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.4 | 8.25 | 21.05 | 33.25 | 5.00 | 92.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.5 | 4.82 | 12.96 | 19.88 | 3.00 | 70.0 | 79.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.73 | 11.06 | 17.20 | 5.00 | 80.9 | 90.0 |

## GW17

- Train rows: 144369
- Bank: 0.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Bukayo Saka
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 57.76
- Actual score: 46.00
- Transfer: Justin Kluivert -> John McGinn (projected gain 2.60, hit 0)
- Autosub: Marc Guéhi replaced Marc Cucurella Saseta.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.89 | 11.85 | 17.67 | 3.00 | 90.1 | 90.0 |
| Bench 1 | Bench | Emiliano Martínez Romero | GK | 2 | 5.0 | 3.47 | 10.24 | 16.91 | 2.00 | 86.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.75 | 15.68 | 21.71 | 2.00 | 87.1 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.0 | 3.34 | 11.20 | 16.87 | 4.00 | 71.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 3.39 | 11.13 | 17.65 | 1.00 | 84.2 | 90.0 |
| Bench 2 | Autosub In | Marc Guéhi | DEF | 7 | 4.5 | 2.31 | 8.11 | 13.45 | -1.00 | 82.9 | 90.0 |
| XI | Bench | Marc Cucurella Saseta | DEF | 6 | 5.1 | 3.07 | 6.08 | 11.72 | 0.00 | 66.3 | 0.0 |
| XI | XI | Adam Armstrong | FWD | 17 | 5.1 | 2.98 | 8.69 | 14.77 | 2.00 | 71.8 | 90.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 5.0 | 1.79 | 5.66 | 10.39 | 1.00 | 38.3 | 45.0 |
| Bench 4 | Bench | Will Lankshear | FWD | 18 | 4.5 | 0.64 | 1.89 | 3.89 | 0.00 | 18.0 | 0.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 7.56 | 22.63 | 36.29 | 3.00 | 80.9 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.4 | 6.34 | 19.68 | 30.91 | 21.00 | 83.8 | 86.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 10.6 | 7.11 | 18.90 | 32.54 | 1.00 | 86.7 | 23.0 |
| XI | XI | John McGinn | MID | 2 | 5.2 | 4.06 | 11.81 | 16.67 | 4.00 | 79.1 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.71 | 9.65 | 14.68 | 3.00 | 75.5 | 90.0 |

## GW18

- Train rows: 145070
- Bank: 0.30 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 67.48
- Actual score: 61.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.72) beats the best remaining Bench Boost opportunity (9.75).
- Transfer: John McGinn -> Amad Diallo (projected gain 5.64, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.72) beats the best remaining Bench Boost opportunity (9.75).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 4.22 | 10.84 | 16.06 | 6.00 | 87.2 | 90.0 |
| Bench 1 | Bench Boost | Emiliano Martínez Romero | GK | 2 | 5.0 | 2.87 | 9.87 | 16.41 | 2.00 | 86.6 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.0 | 5.71 | 12.63 | 22.87 | 2.00 | 73.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.23 | 11.96 | 18.60 | 7.00 | 83.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 4.26 | 11.48 | 17.46 | 2.00 | 74.0 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 6 | 5.1 | 2.46 | 8.52 | 12.53 | 1.00 | 68.4 | 90.0 |
| Bench 3 | Bench Boost | Marc Guéhi | DEF | 7 | 4.5 | 2.23 | 8.15 | 12.97 | 7.00 | 80.0 | 90.0 |
| XI | XI | Adam Armstrong | FWD | 17 | 5.1 | 4.17 | 9.69 | 14.15 | 2.00 | 79.2 | 72.0 |
| Bench 2 | Bench Boost | Cameron Archer | FWD | 17 | 5.0 | 2.27 | 7.81 | 10.92 | 0.00 | 40.5 | 0.0 |
| Bench 4 | Bench Boost | Will Lankshear | FWD | 18 | 4.5 | 0.34 | 1.45 | 2.80 | 0.00 | 7.8 | 0.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.54 | 20.33 | 30.32 | 10.00 | 85.6 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.4 | 7.63 | 19.21 | 27.69 | 9.00 | 74.0 | 90.0 |
| XI | XI | Amad Diallo | MID | 14 | 5.4 | 4.49 | 15.28 | 22.68 | 2.00 | 83.5 | 78.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.4 | 4.31 | 14.84 | 23.38 | 0.00 | 27.8 | 0.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.11 | 9.18 | 10.80 | 2.00 | 81.5 | 90.0 |

## GW19

- Train rows: 145775
- Bank: 0.10 -> 3.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 66.28
- Actual score: 90.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.13) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Bukayo Saka -> Anthony Gordon (projected gain 9.30, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.13) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Emiliano Martínez Romero | GK | 2 | 5.0 | 3.40 | 10.82 | 17.17 | 2.00 | 86.4 | 90.0 |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.81 | 10.40 | 16.57 | 2.00 | 87.1 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.0 | 4.88 | 13.05 | 19.39 | 15.00 | 76.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 4.01 | 12.89 | 17.11 | 6.00 | 80.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.19 | 10.84 | 17.26 | 2.00 | 84.7 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 6 | 5.1 | 3.55 | 9.80 | 17.17 | 1.00 | 79.5 | 90.0 |
| Bench 2 | Bench | Marc Guéhi | DEF | 7 | 4.5 | 3.17 | 6.48 | 11.84 | 0.00 | 71.2 | 0.0 |
| XI | XI | Adam Armstrong | FWD | 17 | 5.1 | 2.57 | 7.10 | 13.02 | 5.00 | 63.1 | 64.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 5.0 | 1.15 | 4.66 | 10.31 | 1.00 | 25.7 | 25.0 |
| Bench 4 | Bench | Will Lankshear | FWD | 18 | 4.5 | 0.32 | 1.40 | 2.37 | 0.00 | 7.0 | 0.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 6.56 | 20.88 | 36.55 | 2.00 | 83.8 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.5 | 8.13 | 18.05 | 31.69 | 16.00 | 81.9 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 5.08 | 15.57 | 25.43 | 6.00 | 75.4 | 84.0 |
| XI | XI | Amad Diallo | MID | 14 | 5.4 | 3.40 | 10.13 | 15.03 | 2.00 | 72.6 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.84 | 9.41 | 17.14 | 1.00 | 84.3 | 90.0 |