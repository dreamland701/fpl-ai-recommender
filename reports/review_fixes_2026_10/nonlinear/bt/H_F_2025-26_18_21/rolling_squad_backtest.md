# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW17
- Simulated weeks: GW18-GW21
- Total predicted points: 239.47
- Total actual points: 205.00
- Average predicted points: 59.87
- Average actual points: 51.25
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
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Bukayo Saka
- Vice captain: Florian Wirtz
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 61.84
- Actual score: 77.00
- Chip advisory: bench_boost (0.62): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Nico O'Reilly replaced Jurriën Timber.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.8 | 4.15 | 11.04 | 18.33 | 3.00 | 88.5 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | 8 | 5.1 | 3.43 | 11.02 | 18.40 | 3.00 | 81.9 | 90.0 |
| XI | XI | Michael Keane | DEF | 9 | 4.7 | 4.57 | 13.62 | 22.90 | 10.00 | 87.5 | 90.0 |
| XI | Bench | Jurriën Timber | DEF | 1 | 6.5 | 4.76 | 13.59 | 20.40 | 0.00 | 83.4 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.34 | 13.53 | 20.23 | 8.00 | 82.3 | 90.0 |
| Bench 2 | Autosub In | Nico O'Reilly | DEF | 13 | 5.3 | 3.96 | 13.19 | 19.56 | 1.00 | 86.0 | 90.0 |
| Bench 4 | Bench | Marcos Senesi Barón | DEF | 4 | 4.9 | 3.87 | 11.93 | 20.36 | 2.00 | 81.4 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 5.59 | 13.98 | 21.55 | 5.00 | 81.5 | 85.0 |
| Bench 3 | Bench | Jarrod Bowen | FWD | 19 | 7.6 | 3.96 | 12.51 | 20.75 | 2.00 | 82.8 | 90.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 11 | 5.8 | 4.46 | 9.19 | 16.70 | 8.00 | 75.3 | 84.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 10.3 | 6.09 | 16.45 | 25.99 | 7.00 | 79.7 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.63 | 15.85 | 25.18 | 2.00 | 84.8 | 90.0 |
| Vice Captain | XI | Florian Wirtz | MID | 12 | 8.1 | 5.71 | 14.44 | 21.93 | 10.00 | 80.2 | 90.0 |
| XI | XI | Ryan Gravenberch | MID | 12 | 5.6 | 5.62 | 13.71 | 20.56 | 11.00 | 84.3 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 4.84 | 13.44 | 21.98 | 5.00 | 86.1 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 0.10 -> 1.30
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Florian Wirtz
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 60.14
- Actual score: 42.00
- Transfer: Jurriën Timber -> Maxence Lacroix (projected gain 3.25, hit 0)
- Autosub: Marcos Senesi Barón replaced Declan Rice.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Dean Henderson | GK | 8 | 5.1 | 3.70 | 11.96 | 18.32 | 3.00 | 88.8 | 90.0 |
| Bench 1 | Bench | Robin Roefs | GK | 17 | 4.8 | 2.31 | 8.02 | 13.35 | 7.00 | 84.7 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.2 | 4.36 | 13.73 | 19.50 | 2.00 | 86.9 | 90.0 |
| Bench 3 | Autosub In | Marcos Senesi Barón | DEF | 4 | 4.9 | 3.33 | 12.30 | 19.24 | 3.00 | 73.0 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.3 | 4.57 | 11.93 | 18.28 | 1.00 | 81.3 | 56.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.07 | 11.20 | 20.35 | 1.00 | 84.2 | 33.0 |
| Bench 2 | Bench | Michael Keane | DEF | 9 | 4.7 | 3.48 | 10.57 | 20.68 | 0.00 | 85.8 | 0.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 5.69 | 14.01 | 21.53 | 2.00 | 79.6 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.6 | 4.66 | 9.64 | 16.32 | 7.00 | 80.9 | 90.0 |
| Bench 4 | Bench | Dominic Calvert-Lewin | FWD | 11 | 5.8 | 2.72 | 9.13 | 14.98 | 1.00 | 73.9 | 20.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 10.3 | 7.19 | 16.62 | 28.96 | 6.00 | 79.6 | 82.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 3.76 | 15.89 | 24.59 | 3.00 | 82.3 | 90.0 |
| Vice Captain | XI | Florian Wirtz | MID | 12 | 8.1 | 6.14 | 15.84 | 24.49 | 3.00 | 80.2 | 65.0 |
| XI | Bench | Declan Rice | MID | 1 | 7.2 | 4.29 | 11.99 | 18.89 | 0.00 | 81.5 | 0.0 |
| XI | XI | Ryan Gravenberch | MID | 12 | 5.6 | 4.50 | 10.77 | 18.24 | 5.00 | 82.6 | 90.0 |

## GW20

- Train rows: 175452
- Bank: 1.30 -> 2.80
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Jarrod Bowen
- Effective captain: Phil Foden
- Chip used: triple_captain
- Predicted score: 55.52
- Actual score: 29.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.33) beats the best remaining Triple Captain opportunity (6.54).
- Transfer: Florian Wirtz -> Dominik Szoboszlai (projected gain 4.95, hit 0)
- Chip used: Triple Captain on Phil Foden. Optimizer chose Triple Captain here because the current estimated captain upside (5.33) beats the best remaining Triple Captain opportunity (6.54).
- Autosub: Nico O'Reilly replaced Hugo Ekitiké.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Dean Henderson | GK | 8 | 5.1 | 3.58 | 12.80 | 19.26 | 2.00 | 87.6 | 90.0 |
| Bench 1 | Bench | Robin Roefs | GK | 17 | 4.8 | 3.43 | 10.58 | 15.33 | 3.00 | 89.2 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.2 | 4.13 | 13.00 | 20.01 | 3.00 | 85.8 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 3.55 | 12.39 | 20.32 | 1.00 | 88.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.15 | 10.35 | 18.63 | 1.00 | 64.9 | 50.0 |
| Bench 2 | Autosub In | Nico O'Reilly | DEF | 13 | 5.3 | 2.76 | 8.12 | 13.76 | 2.00 | 59.9 | 90.0 |
| Bench 3 | Bench | Michael Keane | DEF | 9 | 4.7 | 1.62 | 5.25 | 11.00 | 0.00 | 35.5 | 90.0 |
| XI | Bench | Hugo Ekitiké | FWD | 12 | 9.0 | 4.41 | 15.02 | 24.57 | 0.00 | 76.2 | 0.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.6 | 5.20 | 13.06 | 20.21 | 4.00 | 85.5 | 90.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 11 | 5.8 | 3.42 | 12.47 | 19.12 | 2.00 | 68.7 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.3 | 3.90 | 17.12 | 28.55 | 4.00 | 78.8 | 23.0 |
| Captain | Captain | Phil Foden | MID | 13 | 8.9 | 5.33 | 16.15 | 24.06 | 2.00 | 83.7 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.6 | 4.11 | 14.64 | 26.25 | 2.00 | 79.0 | 90.0 |
| XI | XI | Ryan Gravenberch | MID | 12 | 5.6 | 4.09 | 11.93 | 18.88 | 2.00 | 87.0 | 90.0 |
| Bench 4 | Bench | Declan Rice | MID | 1 | 7.1 | 1.05 | 5.53 | 11.65 | 17.00 | 31.5 | 90.0 |

## GW21

- Train rows: 176242
- Bank: 2.80 -> 2.90
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Jarrod Bowen
- Effective captain: Bukayo Saka
- Chip used: bench_boost
- Predicted score: 61.97
- Actual score: 57.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.44) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Ryan Gravenberch -> Carlos Henrique Casimiro (projected gain 3.47, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.44) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench Boost | Dean Henderson | GK | 8 | 5.1 | 3.34 | 10.17 | 17.55 | 7.00 | 88.8 | 90.0 |
| XI | XI | Robin Roefs | GK | 17 | 4.8 | 3.82 | 10.04 | 17.73 | 2.00 | 87.6 | 90.0 |
| XI | XI | Michael Keane | DEF | 9 | 4.7 | 4.38 | 11.24 | 19.29 | 5.00 | 81.7 | 82.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 3.77 | 10.95 | 19.06 | 6.00 | 83.2 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 4.01 | 10.80 | 19.54 | 8.00 | 90.9 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.3 | 3.70 | 10.75 | 16.06 | 1.00 | 79.2 | 17.0 |
| Bench 4 | Bench Boost | Joško Gvardiol | DEF | 13 | 6.0 | 1.09 | 5.81 | 11.05 | 0.00 | 21.8 | 0.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 11 | 5.8 | 3.41 | 11.62 | 17.74 | 8.00 | 78.6 | 86.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.6 | 5.11 | 11.53 | 19.36 | 2.00 | 85.0 | 90.0 |
| Bench 3 | Bench Boost | Hugo Ekitiké | FWD | 12 | 9.0 | 2.11 | 9.30 | 15.39 | 0.00 | 39.9 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 8.8 | 4.79 | 15.45 | 24.68 | 2.00 | 82.4 | 72.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.5 | 4.11 | 15.11 | 21.60 | 4.00 | 79.6 | 73.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 4.67 | 14.76 | 22.59 | 3.00 | 84.3 | 90.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 10.2 | 5.38 | 12.14 | 22.48 | 3.00 | 66.2 | 77.0 |
| Bench 2 | Bench Boost | Dominik Szoboszlai | MID | 12 | 6.6 | 2.89 | 11.71 | 20.51 | 3.00 | 75.0 | 90.0 |