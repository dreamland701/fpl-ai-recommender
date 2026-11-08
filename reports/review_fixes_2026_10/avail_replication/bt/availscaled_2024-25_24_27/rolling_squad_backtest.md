# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 279.57
- Total actual points: 301.00
- Average predicted points: 69.89
- Average actual points: 75.25
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
- Predicted score: 83.56
- Actual score: 100.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (19.58) beats the best remaining Bench Boost opportunity (16.88).
- Chip advisory: bench_boost (0.63): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (19.58) beats the best remaining Bench Boost opportunity (16.88).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alisson Ramses Becker | GK | 12 | 5.5 | 5.06 | 12.20 | 19.20 | 10.00 | 92.8 | 180.0 |
| Bench 1 | Bench Boost | Matz Sels | GK | 16 | 5.0 | 2.88 | 8.91 | 14.58 | 8.00 | 84.4 | 90.0 |
| Captain | Captain | Trent Alexander-Arnold | DEF | 12 | 7.4 | 7.69 | 20.13 | 31.34 | 7.00 | 107.8 | 98.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 6.11 | 15.12 | 23.81 | 6.00 | 96.3 | 180.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 5.10 | 12.76 | 19.48 | 7.00 | 137.7 | 177.0 |
| XI | XI | James Tarkowski | DEF | 8 | 4.8 | 4.69 | 11.98 | 18.69 | 17.00 | 133.0 | 180.0 |
| Bench 3 | Bench Boost | Lewis Hall | DEF | 15 | 5.1 | 3.74 | 11.05 | 17.82 | 1.00 | 74.2 | 86.0 |
| XI | XI | Iliman Ndiaye | FWD | 8 | 5.5 | 6.09 | 15.05 | 23.00 | 9.00 | 138.8 | 114.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.3 | 4.55 | 12.38 | 19.97 | 2.00 | 79.9 | 90.0 |
| Bench 4 | Bench Boost | Jean-Philippe Mateta | FWD | 7 | 7.4 | 3.72 | 11.38 | 19.09 | 13.00 | 71.5 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.3 | 7.24 | 19.69 | 33.17 | 6.00 | 99.1 | 89.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.14 | 16.76 | 27.28 | 2.00 | 93.9 | 90.0 |
| Bench 2 | Bench Boost | Phil Foden | MID | 13 | 9.3 | 4.12 | 14.49 | 25.00 | 2.00 | 84.5 | 71.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 4.41 | 13.33 | 21.06 | 2.00 | 97.1 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.7 | 4.32 | 13.22 | 22.31 | 1.00 | 74.4 | 90.0 |

## GW25

- Train rows: 150166
- Bank: 0.20 -> 2.20
- Free transfers: 2 -> 2
- Captain: Trent Alexander-Arnold
- Vice captain: Morgan Rogers
- Effective captain: Trent Alexander-Arnold
- Chip used: triple_captain
- Predicted score: 75.74
- Actual score: 73.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (10.75) beats the best remaining Triple Captain opportunity (9.31).
- Transfer: Anthony Gordon -> Morgan Rogers (projected gain 5.83, hit 0)
- Chip used: Triple Captain on Trent Alexander-Arnold. Optimizer chose Triple Captain here because the current estimated captain upside (10.75) beats the best remaining Triple Captain opportunity (9.31).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alisson Ramses Becker | GK | 12 | 5.5 | 5.56 | 13.87 | 21.75 | 4.00 | 119.7 | 180.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 5.0 | 3.02 | 9.23 | 15.13 | 3.00 | 85.6 | 90.0 |
| Captain | Captain | Trent Alexander-Arnold | DEF | 12 | 7.4 | 7.37 | 19.11 | 30.98 | 13.00 | 115.0 | 128.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 6.75 | 16.78 | 26.13 | 2.00 | 145.8 | 180.0 |
| XI | XI | James Tarkowski | DEF | 8 | 4.8 | 3.96 | 12.03 | 19.29 | 2.00 | 118.6 | 90.0 |
| Bench 2 | Bench | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.60 | 10.88 | 16.92 | 2.00 | 104.7 | 90.0 |
| Bench 3 | Bench | Lewis Hall | DEF | 15 | 5.1 | 2.77 | 9.31 | 15.84 | 0.00 | 48.8 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.3 | 4.69 | 14.39 | 23.56 | 7.00 | 88.9 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.3 | 4.44 | 12.57 | 20.72 | 2.00 | 78.7 | 90.0 |
| Bench 4 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 2.71 | 9.24 | 15.02 | 0.00 | 67.7 | 0.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.2 | 6.58 | 19.52 | 32.25 | 2.00 | 73.3 | 90.0 |
| Vice Captain | XI | Morgan Rogers | MID | 2 | 5.6 | 6.97 | 16.60 | 24.97 | 4.00 | 118.5 | 180.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 6.18 | 15.50 | 24.02 | 5.00 | 88.9 | 76.0 |
| XI | XI | Phil Foden | MID | 13 | 9.3 | 4.48 | 15.25 | 25.90 | 3.00 | 65.0 | 75.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 4.03 | 11.31 | 18.56 | 3.00 | 62.6 | 90.0 |

## GW26

- Train rows: 150945
- Bank: 2.20 -> 0.60
- Free transfers: 2 -> 2
- Captain: Bryan Mbeumo
- Vice captain: Cole Palmer
- Effective captain: Bryan Mbeumo
- Chip used: none
- Predicted score: 60.15
- Actual score: 73.00
- Transfer: Iliman Ndiaye -> Chris Wood (projected gain 4.35, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alisson Ramses Becker | GK | 12 | 5.5 | 3.93 | 11.97 | 19.26 | 8.00 | 121.7 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 5.0 | 2.94 | 9.18 | 15.17 | 0.00 | 88.2 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.75 | 17.45 | 28.32 | 6.00 | 108.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 4.68 | 14.14 | 22.62 | 6.00 | 107.1 | 90.0 |
| XI | XI | James Tarkowski | DEF | 8 | 4.8 | 3.37 | 9.82 | 16.21 | 1.00 | 94.7 | 90.0 |
| Bench 4 | Bench | Lewis Hall | DEF | 15 | 5.0 | 3.08 | 9.63 | 16.13 | 9.00 | 81.8 | 90.0 |
| Bench 3 | Bench | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.28 | 9.24 | 15.04 | 1.00 | 89.0 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 5.29 | 15.71 | 25.43 | 5.00 | 83.5 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.3 | 4.52 | 14.54 | 23.79 | 5.00 | 84.2 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.3 | 4.71 | 13.14 | 20.60 | 8.00 | 82.3 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 5.98 | 18.45 | 30.54 | 2.00 | 92.4 | 90.0 |
| Captain | Captain | Bryan Mbeumo | MID | 4 | 7.9 | 6.35 | 17.12 | 26.71 | 14.00 | 96.6 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 9.3 | 4.24 | 14.92 | 24.96 | 2.00 | 65.8 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 4.99 | 14.59 | 22.74 | 2.00 | 76.4 | 72.0 |
| Bench 2 | Bench | Morgan Rogers | MID | 2 | 5.6 | 3.99 | 11.48 | 17.67 | 2.00 | 71.8 | 77.0 |

## GW27

- Train rows: 151728
- Bank: 0.60 -> 1.10
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Bryan Mbeumo
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 60.11
- Actual score: 55.00
- Transfer: Jean-Philippe Mateta -> Matheus Santos Carneiro Da Cunha (projected gain 3.52, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alisson Ramses Becker | GK | 12 | 5.5 | 3.69 | 10.90 | 17.77 | 6.00 | 100.3 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 5.0 | 2.65 | 8.40 | 14.19 | 6.00 | 88.7 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.92 | 16.61 | 27.32 | 6.00 | 80.3 | 76.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 4.36 | 12.76 | 20.79 | 7.00 | 107.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 5.0 | 2.99 | 9.67 | 16.37 | 1.00 | 86.4 | 90.0 |
| Bench 3 | Bench | James Tarkowski | DEF | 8 | 4.8 | 2.86 | 9.12 | 15.08 | 2.00 | 91.4 | 90.0 |
| Bench 2 | Bench | Vitalii Mykolenko | DEF | 8 | 4.4 | 2.94 | 8.81 | 14.37 | 6.00 | 87.6 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 4.81 | 15.34 | 26.03 | 2.00 | 93.0 | 84.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.97 | 14.05 | 21.84 | 2.00 | 90.7 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.3 | 4.08 | 11.74 | 18.46 | 9.00 | 77.8 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 7.23 | 19.41 | 31.69 | 3.00 | 104.2 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.13 | 17.98 | 28.39 | 5.00 | 94.4 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 9.3 | 4.46 | 14.43 | 24.19 | 1.00 | 77.3 | 16.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 4.23 | 13.09 | 20.75 | 10.00 | 69.1 | 90.0 |
| Bench 4 | Bench | Morgan Rogers | MID | 2 | 5.6 | 2.63 | 8.14 | 14.38 | 7.00 | 60.7 | 90.0 |