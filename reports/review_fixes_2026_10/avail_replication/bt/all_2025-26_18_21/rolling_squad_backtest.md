# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW17
- Simulated weeks: GW18-GW21
- Total predicted points: 204.68
- Total actual points: 216.00
- Average predicted points: 51.17
- Average actual points: 54.00
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW17 are included before the first simulated week.
- League-average scores were not available for this run.

## GW18

- Train rows: 173897
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Hugo Ekitiké
- Vice captain: Morgan Rogers
- Effective captain: Hugo Ekitiké
- Chip used: none
- Predicted score: 54.82
- Actual score: 67.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Dominic Calvert-Lewin replaced Jurriën Timber.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.11 | 9.83 | 15.81 | 2.00 | 89.5 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 5.5 | 2.98 | 8.12 | 13.27 | 6.00 | 88.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.60 | 12.56 | 19.19 | 2.00 | 96.2 | 90.0 |
| XI | Bench | Jurriën Timber | DEF | 1 | 6.5 | 3.70 | 11.44 | 17.69 | 0.00 | 90.9 | 0.0 |
| Bench 3 | Bench | Joško Gvardiol | DEF | 13 | 6.0 | 3.04 | 9.89 | 16.43 | 8.00 | 82.4 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.5 | 3.35 | 9.88 | 15.74 | 8.00 | 86.5 | 90.0 |
| XI | XI | Michael Keane | DEF | 9 | 4.7 | 3.55 | 9.77 | 15.10 | 10.00 | 90.4 | 90.0 |
| Captain | Captain | Hugo Ekitiké | FWD | 12 | 9.0 | 6.56 | 17.20 | 25.79 | 5.00 | 96.9 | 85.0 |
| Bench 2 | Autosub In | Dominic Calvert-Lewin | FWD | 11 | 5.8 | 3.26 | 9.83 | 16.38 | 8.00 | 73.2 | 84.0 |
| Bench 4 | Bench | Igor Jesus Maciel da Cruz | FWD | 16 | 5.8 | 2.50 | 7.13 | 11.99 | 5.00 | 69.7 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 4.71 | 15.82 | 23.99 | 2.00 | 83.4 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 4.83 | 15.34 | 23.92 | 5.00 | 99.3 | 90.0 |
| Vice Captain | XI | Morgan Rogers | MID | 2 | 7.3 | 5.02 | 14.09 | 24.50 | 1.00 | 106.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 4.25 | 13.31 | 22.78 | 9.00 | 85.8 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.1 | 4.57 | 12.86 | 21.39 | 10.00 | 86.1 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Florian Wirtz
- Effective captain: Phil Foden
- Chip used: none
- Predicted score: 43.09
- Actual score: 38.00
- Transfer: Jurriën Timber -> Reece James (projected gain 2.77, hit 0)
- Autosub: Igor Jesus Maciel da Cruz replaced Declan Rice.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.07 | 9.59 | 16.16 | 2.00 | 87.3 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 5.5 | 2.56 | 8.03 | 13.10 | 10.00 | 86.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.31 | 10.95 | 17.66 | 6.00 | 84.3 | 90.0 |
| XI | XI | Reece James | DEF | 7 | 5.7 | 3.67 | 10.51 | 16.56 | 1.00 | 90.3 | 45.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.28 | 10.50 | 17.10 | 1.00 | 89.2 | 33.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.5 | 3.10 | 9.88 | 16.59 | 9.00 | 86.1 | 90.0 |
| Bench 2 | Bench | Michael Keane | DEF | 9 | 4.7 | 2.92 | 7.84 | 12.07 | 0.00 | 68.6 | 0.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 3.89 | 12.46 | 18.49 | 2.00 | 63.6 | 90.0 |
| Bench 4 | Bench | Dominic Calvert-Lewin | FWD | 11 | 5.8 | 2.43 | 8.80 | 14.87 | 1.00 | 61.7 | 20.0 |
| Bench 3 | Autosub In | Igor Jesus Maciel da Cruz | FWD | 16 | 5.8 | 2.83 | 8.29 | 12.97 | 2.00 | 76.5 | 61.0 |
| Captain | Captain | Phil Foden | MID | 13 | 9.0 | 4.24 | 14.31 | 23.14 | 3.00 | 80.7 | 90.0 |
| Vice Captain | XI | Florian Wirtz | MID | 12 | 8.1 | 4.01 | 12.50 | 19.43 | 3.00 | 81.8 | 65.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 3.75 | 11.94 | 18.90 | 5.00 | 80.2 | 90.0 |
| XI | Bench | Declan Rice | MID | 1 | 7.2 | 3.56 | 11.51 | 20.00 | 0.00 | 72.2 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 2.97 | 11.45 | 18.83 | 1.00 | 76.9 | 81.0 |

## GW20

- Train rows: 175452
- Bank: 0.70 -> 0.80
- Free transfers: 2 -> 2
- Captain: Morgan Rogers
- Vice captain: Phil Foden
- Effective captain: Morgan Rogers
- Chip used: triple_captain
- Predicted score: 50.99
- Actual score: 47.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (4.73) beats the best remaining Triple Captain opportunity (6.06).
- Transfer: Declan Rice -> Bruno Guimarães Rodriguez Moura (projected gain 5.23, hit 0)
- Chip used: Triple Captain on Morgan Rogers. Optimizer chose Triple Captain here because the current estimated captain upside (4.73) beats the best remaining Triple Captain opportunity (6.06).
- Autosub: Igor Jesus Maciel da Cruz replaced Hugo Ekitiké.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.29 | 9.72 | 15.84 | 1.00 | 95.2 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 5.5 | 2.52 | 7.31 | 12.03 | 1.00 | 92.3 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.5 | 4.28 | 11.97 | 18.66 | 2.00 | 98.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.60 | 10.74 | 17.24 | 1.00 | 87.8 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 2.97 | 9.53 | 15.85 | 1.00 | 71.6 | 50.0 |
| Bench 3 | Bench | Reece James | DEF | 7 | 5.7 | 1.97 | 7.36 | 12.83 | 1.00 | 72.6 | 90.0 |
| Bench 4 | Bench | Michael Keane | DEF | 9 | 4.7 | 0.93 | 3.53 | 6.43 | 0.00 | 21.4 | 90.0 |
| XI | Bench | Hugo Ekitiké | FWD | 12 | 9.0 | 3.57 | 11.44 | 21.96 | 0.00 | 73.5 | 0.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 11 | 5.8 | 2.62 | 8.46 | 15.64 | 2.00 | 39.3 | 90.0 |
| Bench 2 | Autosub In | Igor Jesus Maciel da Cruz | FWD | 16 | 5.8 | 2.48 | 7.42 | 12.14 | 2.00 | 67.2 | 82.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.9 | 4.72 | 15.23 | 24.56 | 2.00 | 88.7 | 90.0 |
| Captain | Captain | Morgan Rogers | MID | 2 | 7.4 | 4.73 | 12.97 | 20.43 | 5.00 | 82.6 | 90.0 |
| XI | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.0 | 4.59 | 12.58 | 20.13 | 10.00 | 91.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 4.02 | 11.33 | 18.54 | 1.00 | 91.6 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.1 | 3.12 | 10.67 | 18.27 | 10.00 | 68.1 | 75.0 |

## GW21

- Train rows: 176242
- Bank: 0.80 -> 1.10
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Bruno Guimarães Rodriguez Moura
- Effective captain: Ollie Watkins
- Chip used: bench_boost
- Predicted score: 55.78
- Actual score: 64.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.92) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Hugo Ekitiké -> Ollie Watkins (projected gain 5.62, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.92) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench Boost | David Raya Martín | GK | 1 | 6.0 | 2.87 | 9.01 | 14.29 | 6.00 | 87.4 | 90.0 |
| XI | XI | Jordan Pickford | GK | 9 | 5.5 | 3.17 | 8.79 | 14.36 | 3.00 | 91.4 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.6 | 4.06 | 10.54 | 15.39 | 4.00 | 92.9 | 90.0 |
| XI | XI | Reece James | DEF | 7 | 5.7 | 3.03 | 8.99 | 14.44 | 1.00 | 85.3 | 25.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 2.77 | 8.88 | 14.95 | 6.00 | 85.9 | 90.0 |
| Bench 2 | Bench Boost | Joško Gvardiol | DEF | 13 | 6.0 | 2.40 | 7.92 | 13.70 | 0.00 | 64.7 | 0.0 |
| XI | XI | Michael Keane | DEF | 9 | 4.7 | 2.92 | 6.98 | 11.41 | 5.00 | 76.4 | 82.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.7 | 4.86 | 13.52 | 21.06 | 2.00 | 87.9 | 90.0 |
| Bench 3 | Bench Boost | Dominic Calvert-Lewin | FWD | 11 | 5.8 | 2.34 | 8.33 | 13.92 | 8.00 | 60.2 | 86.0 |
| Bench 4 | Bench Boost | Igor Jesus Maciel da Cruz | FWD | 16 | 5.8 | 2.32 | 7.22 | 12.17 | 2.00 | 50.9 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.8 | 4.46 | 13.80 | 22.32 | 2.00 | 85.0 | 72.0 |
| Vice Captain | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.0 | 4.50 | 12.73 | 20.67 | 11.00 | 91.1 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 3.93 | 12.41 | 19.63 | 3.00 | 79.9 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.1 | 3.39 | 12.06 | 20.04 | 3.00 | 74.3 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 3.91 | 11.63 | 18.92 | 6.00 | 90.0 | 90.0 |