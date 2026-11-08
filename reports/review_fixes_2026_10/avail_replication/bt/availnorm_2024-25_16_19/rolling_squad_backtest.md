# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 232.55
- Total actual points: 257.00
- Average predicted points: 58.14
- Average actual points: 64.25
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
- Predicted score: 56.08
- Actual score: 39.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.45 | 9.78 | 15.68 | 6.00 | 88.6 | 90.0 |
| Bench 1 | Bench | Emiliano Martínez Romero | GK | 2 | 5.0 | 2.48 | 7.76 | 12.86 | 2.00 | 75.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.31 | 12.22 | 18.88 | 6.00 | 90.4 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.0 | 3.55 | 10.22 | 17.25 | 1.00 | 48.5 | 78.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 3.23 | 9.34 | 15.79 | 1.00 | 57.7 | 90.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 4.7 | 2.78 | 8.50 | 13.78 | 1.00 | 80.0 | 90.0 |
| XI | XI | Milos Kerkez | DEF | 3 | 4.6 | 3.01 | 8.42 | 13.49 | 2.00 | 74.0 | 90.0 |
| Bench 3 | Bench | Adam Armstrong | FWD | 17 | 5.1 | 2.59 | 7.31 | 12.16 | 2.00 | 65.3 | 81.0 |
| XI | XI | Cameron Archer | FWD | 17 | 5.0 | 2.72 | 7.20 | 11.62 | 1.00 | 63.0 | 8.0 |
| Bench 4 | Bench | Patson Daka | FWD | 11 | 4.8 | 0.92 | 3.47 | 5.87 | 1.00 | 21.7 | 31.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.30 | 21.98 | 37.17 | 5.00 | 91.6 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 7.53 | 21.50 | 34.69 | 3.00 | 116.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 5.76 | 17.20 | 27.38 | 3.00 | 90.1 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.94 | 11.55 | 18.38 | 5.00 | 88.5 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.5 | 3.73 | 10.97 | 17.12 | 3.00 | 52.1 | 79.0 |

## GW17

- Train rows: 144369
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 49.71
- Actual score: 58.00
- Transfer: Milos Kerkez -> Lewis Hall (projected gain 2.60, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.37 | 9.72 | 15.71 | 3.00 | 86.7 | 90.0 |
| Bench 1 | Bench | Emiliano Martínez Romero | GK | 2 | 5.0 | 2.48 | 7.54 | 12.54 | 2.00 | 78.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 3.67 | 10.79 | 17.25 | 2.00 | 80.7 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.69 | 10.14 | 16.06 | 7.00 | 90.9 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.0 | 3.04 | 9.60 | 15.77 | 4.00 | 55.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 2.91 | 8.83 | 14.66 | 1.00 | 69.2 | 90.0 |
| Bench 3 | Bench | Daniel Muñoz | DEF | 7 | 4.7 | 1.89 | 7.13 | 11.77 | 0.00 | 72.0 | 0.0 |
| XI | XI | Adam Armstrong | FWD | 17 | 5.1 | 2.29 | 7.18 | 12.21 | 2.00 | 64.5 | 90.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 5.0 | 1.97 | 6.31 | 10.86 | 1.00 | 40.4 | 45.0 |
| Bench 4 | Bench | Patson Daka | FWD | 11 | 4.8 | 0.71 | 2.26 | 3.96 | 0.00 | 29.6 | 0.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 6.66 | 20.92 | 33.47 | 3.00 | 106.5 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 6.27 | 20.74 | 34.52 | 21.00 | 93.7 | 86.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 5.63 | 17.13 | 27.95 | 1.00 | 86.0 | 23.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.00 | 10.38 | 16.41 | 3.00 | 72.3 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.5 | 2.53 | 9.21 | 15.53 | 8.00 | 47.5 | 77.0 |

## GW18

- Train rows: 145070
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 62.18
- Actual score: 69.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.63) beats the best remaining Bench Boost opportunity (6.87).
- Transfer: Bukayo Saka -> Son Heung-min (projected gain 6.99, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.63) beats the best remaining Bench Boost opportunity (6.87).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.70 | 10.09 | 16.24 | 6.00 | 88.5 | 90.0 |
| Bench 1 | Bench Boost | Emiliano Martínez Romero | GK | 2 | 5.0 | 2.42 | 7.50 | 12.43 | 2.00 | 81.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.23 | 11.96 | 19.26 | 7.00 | 87.0 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.0 | 4.57 | 11.86 | 18.96 | 2.00 | 75.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 3.33 | 9.04 | 14.86 | 2.00 | 68.9 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 2.92 | 8.67 | 14.01 | 6.00 | 71.7 | 90.0 |
| Bench 3 | Bench Boost | Daniel Muñoz | DEF | 7 | 4.7 | 0.49 | 2.46 | 4.34 | 6.00 | 39.3 | 90.0 |
| XI | XI | Adam Armstrong | FWD | 17 | 5.1 | 2.84 | 7.49 | 12.18 | 2.00 | 73.4 | 72.0 |
| Bench 2 | Bench Boost | Cameron Archer | FWD | 17 | 5.0 | 2.48 | 6.89 | 11.57 | 0.00 | 47.3 | 0.0 |
| Bench 4 | Bench Boost | Patson Daka | FWD | 11 | 4.8 | 0.24 | 1.95 | 3.23 | 2.00 | 14.2 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.4 | 8.59 | 22.87 | 37.86 | 9.00 | 109.9 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 6.93 | 21.03 | 34.07 | 10.00 | 114.1 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.8 | 4.32 | 13.41 | 22.16 | 2.00 | 83.7 | 80.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.5 | 3.42 | 10.64 | 17.65 | 2.00 | 61.1 | 71.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.11 | 9.53 | 15.58 | 2.00 | 75.0 | 90.0 |

## GW19

- Train rows: 145775
- Bank: 0.60 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 64.57
- Actual score: 91.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.84) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Justin Kluivert -> Ismaïla Sarr (projected gain 2.27, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.84) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.42 | 9.95 | 16.13 | 2.00 | 87.9 | 90.0 |
| Bench 1 | Bench | Emiliano Martínez Romero | GK | 2 | 5.0 | 2.66 | 7.69 | 12.56 | 2.00 | 83.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 3.92 | 11.78 | 19.58 | 2.00 | 85.7 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.0 | 4.11 | 11.64 | 18.43 | 15.00 | 74.4 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.78 | 10.78 | 17.66 | 12.00 | 84.4 | 90.0 |
| Bench 2 | Bench | Virgil van Dijk | DEF | 12 | 6.4 | 3.27 | 9.25 | 14.94 | 6.00 | 79.8 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.7 | 3.35 | 8.53 | 13.60 | 2.00 | 73.2 | 90.0 |
| XI | XI | Adam Armstrong | FWD | 17 | 5.1 | 2.57 | 7.61 | 12.15 | 5.00 | 68.9 | 64.0 |
| Bench 3 | Bench | Patson Daka | FWD | 11 | 4.8 | 1.86 | 5.74 | 8.70 | 1.00 | 48.5 | 5.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 5.0 | 1.03 | 3.60 | 6.30 | 1.00 | 26.3 | 25.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.5 | 7.84 | 22.84 | 37.22 | 16.00 | 113.4 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.16 | 20.89 | 34.47 | 2.00 | 105.4 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.8 | 4.55 | 13.64 | 22.80 | 0.00 | 73.4 | 63.0 |
| XI | XI | Ismaïla Sarr | MID | 7 | 5.9 | 4.53 | 11.43 | 18.26 | 2.00 | 91.1 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.68 | 10.20 | 16.53 | 1.00 | 79.5 | 90.0 |