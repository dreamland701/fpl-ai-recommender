# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 252.69
- Total actual points: 304.00
- Average predicted points: 63.17
- Average actual points: 76.00
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW23 are included before the first simulated week.
- League-average scores were not available for this run.

## GW24

- Train rows: 149404
- Bank: 100.00 -> 0.20
- Free transfers: 1 -> 2
- Captain: Trent Alexander-Arnold
- Vice captain: Cole Palmer
- Effective captain: Trent Alexander-Arnold
- Chip used: bench_boost
- Predicted score: 75.85
- Actual score: 94.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (18.29) beats the best remaining Bench Boost opportunity (18.24).
- Chip advisory: bench_boost (0.58): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (18.29) beats the best remaining Bench Boost opportunity (18.24).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alisson Ramses Becker | GK | 12 | 5.5 | 4.58 | 11.00 | 17.21 | 10.00 | 104.8 | 180.0 |
| Bench 1 | Bench Boost | Emiliano Martínez Romero | GK | 2 | 5.0 | 2.80 | 8.03 | 13.18 | 2.00 | 83.3 | 90.0 |
| Captain | Captain | Trent Alexander-Arnold | DEF | 12 | 7.4 | 6.99 | 18.28 | 28.40 | 7.00 | 119.8 | 98.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 5.52 | 13.62 | 21.35 | 6.00 | 106.3 | 180.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 4.63 | 11.60 | 17.70 | 7.00 | 117.7 | 177.0 |
| XI | XI | James Tarkowski | DEF | 8 | 4.8 | 4.24 | 10.76 | 16.71 | 17.00 | 113.0 | 180.0 |
| Bench 3 | Bench Boost | Lewis Hall | DEF | 15 | 5.1 | 3.36 | 9.94 | 16.06 | 1.00 | 75.2 | 86.0 |
| XI | XI | Iliman Ndiaye | FWD | 8 | 5.5 | 5.51 | 13.64 | 20.82 | 9.00 | 118.8 | 114.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.3 | 4.11 | 11.17 | 18.06 | 2.00 | 75.9 | 90.0 |
| Bench 4 | Bench Boost | Jean-Philippe Mateta | FWD | 7 | 7.4 | 3.32 | 10.20 | 17.15 | 13.00 | 66.5 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.3 | 6.61 | 17.88 | 30.25 | 6.00 | 101.1 | 89.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.58 | 15.20 | 24.80 | 2.00 | 93.9 | 90.0 |
| Bench 2 | Bench Boost | Phil Foden | MID | 13 | 9.3 | 3.70 | 13.15 | 22.76 | 2.00 | 82.5 | 71.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 4.08 | 12.36 | 19.51 | 2.00 | 95.1 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.7 | 3.84 | 11.80 | 19.98 | 1.00 | 71.4 | 90.0 |

## GW25

- Train rows: 150166
- Bank: 0.20 -> 2.20
- Free transfers: 2 -> 2
- Captain: Trent Alexander-Arnold
- Vice captain: Morgan Rogers
- Effective captain: Trent Alexander-Arnold
- Chip used: triple_captain
- Predicted score: 68.35
- Actual score: 73.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (10.29) beats the best remaining Triple Captain opportunity (8.39).
- Transfer: Anthony Gordon -> Morgan Rogers (projected gain 5.64, hit 0)
- Chip used: Triple Captain on Trent Alexander-Arnold. Optimizer chose Triple Captain here because the current estimated captain upside (10.29) beats the best remaining Triple Captain opportunity (8.39).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alisson Ramses Becker | GK | 12 | 5.5 | 4.97 | 12.41 | 19.50 | 4.00 | 139.7 | 180.0 |
| Bench 1 | Bench | Emiliano Martínez Romero | GK | 2 | 5.0 | 4.51 | 11.02 | 17.01 | 4.00 | 113.2 | 180.0 |
| Captain | Captain | Trent Alexander-Arnold | DEF | 12 | 7.4 | 6.57 | 17.01 | 27.51 | 13.00 | 116.0 | 128.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 6.06 | 15.07 | 23.51 | 2.00 | 146.8 | 180.0 |
| XI | XI | James Tarkowski | DEF | 8 | 4.8 | 3.51 | 10.81 | 17.47 | 2.00 | 119.6 | 90.0 |
| Bench 2 | Bench | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.17 | 9.64 | 15.04 | 2.00 | 105.7 | 90.0 |
| Bench 3 | Bench | Lewis Hall | DEF | 15 | 5.1 | 2.45 | 8.25 | 14.08 | 0.00 | 68.8 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.3 | 4.23 | 13.07 | 21.47 | 7.00 | 86.9 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.3 | 4.00 | 11.29 | 18.62 | 2.00 | 72.7 | 90.0 |
| Bench 4 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 2.31 | 8.05 | 13.18 | 0.00 | 66.7 | 0.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.2 | 5.93 | 17.62 | 29.21 | 2.00 | 93.3 | 90.0 |
| Vice Captain | XI | Morgan Rogers | MID | 2 | 5.6 | 6.33 | 15.18 | 22.89 | 4.00 | 119.5 | 180.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 5.98 | 14.96 | 23.17 | 5.00 | 89.9 | 76.0 |
| XI | XI | Phil Foden | MID | 13 | 9.3 | 4.01 | 13.64 | 23.16 | 3.00 | 66.0 | 75.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 3.64 | 11.54 | 19.50 | 3.00 | 82.6 | 90.0 |

## GW26

- Train rows: 150945
- Bank: 2.20 -> 0.60
- Free transfers: 2 -> 2
- Captain: Bryan Mbeumo
- Vice captain: Cole Palmer
- Effective captain: Bryan Mbeumo
- Chip used: none
- Predicted score: 54.13
- Actual score: 73.00
- Transfer: Iliman Ndiaye -> Chris Wood (projected gain 4.19, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alisson Ramses Becker | GK | 12 | 5.5 | 3.52 | 10.76 | 17.38 | 8.00 | 122.7 | 90.0 |
| Bench 1 | Bench | Emiliano Martínez Romero | GK | 2 | 5.0 | 3.36 | 9.71 | 15.38 | 3.00 | 112.2 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.11 | 15.62 | 25.43 | 6.00 | 109.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 4.20 | 12.73 | 20.42 | 6.00 | 127.1 | 90.0 |
| XI | XI | James Tarkowski | DEF | 8 | 4.8 | 3.03 | 8.91 | 14.78 | 1.00 | 95.7 | 90.0 |
| Bench 4 | Bench | Lewis Hall | DEF | 15 | 5.0 | 2.77 | 8.65 | 14.50 | 9.00 | 75.8 | 90.0 |
| Bench 3 | Bench | Vitalii Mykolenko | DEF | 8 | 4.4 | 2.91 | 8.24 | 13.45 | 1.00 | 89.0 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 4.73 | 14.06 | 22.84 | 5.00 | 85.5 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.3 | 4.06 | 13.11 | 21.49 | 5.00 | 81.2 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.3 | 4.26 | 11.85 | 18.58 | 8.00 | 76.3 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 5.37 | 16.63 | 27.59 | 2.00 | 93.4 | 90.0 |
| Captain | Captain | Bryan Mbeumo | MID | 4 | 7.9 | 5.80 | 15.61 | 24.36 | 14.00 | 95.6 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 9.3 | 3.80 | 13.38 | 22.38 | 2.00 | 66.8 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 4.47 | 13.07 | 20.38 | 2.00 | 68.4 | 72.0 |
| Bench 2 | Bench | Morgan Rogers | MID | 2 | 5.6 | 3.45 | 9.97 | 15.37 | 2.00 | 82.8 | 77.0 |

## GW27

- Train rows: 151728
- Bank: 0.60 -> 0.10
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Bryan Mbeumo
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 54.35
- Actual score: 64.00
- Transfer: Vitalii Mykolenko -> Daniel Muñoz (projected gain 1.36, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alisson Ramses Becker | GK | 12 | 5.5 | 3.37 | 9.95 | 16.26 | 6.00 | 101.3 | 90.0 |
| Bench 1 | Bench | Emiliano Martínez Romero | GK | 2 | 5.0 | 2.71 | 8.10 | 13.31 | 1.00 | 96.5 | 45.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.40 | 15.12 | 24.94 | 6.00 | 100.3 | 76.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 3.99 | 11.66 | 19.04 | 7.00 | 108.0 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.9 | 3.59 | 10.11 | 16.39 | 4.00 | 88.3 | 90.0 |
| Bench 2 | Bench | Lewis Hall | DEF | 15 | 5.0 | 2.70 | 8.76 | 14.88 | 1.00 | 83.4 | 90.0 |
| Bench 3 | Bench | James Tarkowski | DEF | 8 | 4.8 | 2.63 | 8.44 | 14.00 | 2.00 | 90.4 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 4.28 | 13.78 | 23.55 | 2.00 | 94.0 | 84.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.3 | 3.68 | 10.62 | 16.69 | 9.00 | 72.8 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.4 | 3.31 | 10.46 | 17.42 | 8.00 | 82.7 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 6.65 | 17.81 | 29.13 | 3.00 | 104.2 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.56 | 16.35 | 25.84 | 5.00 | 95.4 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 9.3 | 4.07 | 13.14 | 22.03 | 1.00 | 69.3 | 16.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 3.79 | 11.72 | 18.59 | 10.00 | 62.1 | 90.0 |
| Bench 4 | Bench | Morgan Rogers | MID | 2 | 5.6 | 2.25 | 7.07 | 12.61 | 7.00 | 57.7 | 90.0 |