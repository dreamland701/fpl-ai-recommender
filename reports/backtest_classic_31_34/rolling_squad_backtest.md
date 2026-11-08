# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW31-GW34
- Total predicted points: 264.85
- Total actual points: 234.00
- Average predicted points: 66.21
- Average actual points: 58.50
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW26 are included before the first simulated week.
- League-average scores were not available for this run.

## GW31

- Train rows: 184363
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 59.39
- Actual score: 46.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub outfielders: Marcos Senesi Barón, Adrien Truffert.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martín | GK | 1 | 6.0 | 3.28 | 11.10 | 18.90 | 0.00 | 73.5 | 0.0 |
| XI | XI | Martin Dúbravka | GK | 3 | 4.0 | 3.29 | 9.58 | 15.55 | 2.00 | 88.9 | 90.0 |
| XI | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.60 | 14.79 | 25.30 | 0.00 | 79.5 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 4.80 | 14.59 | 24.01 | 3.00 | 91.8 | 90.0 |
| Bench 2 | Autosub In | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.15 | 12.01 | 19.38 | 1.00 | 87.7 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 4.25 | 11.97 | 19.49 | -1.00 | 88.7 | 90.0 |
| Bench 3 | Autosub In | Adrien Truffert | DEF | 4 | 4.6 | 3.84 | 11.17 | 18.36 | 4.00 | 84.6 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.02 | 17.93 | 29.24 | 2.00 | 89.6 | 77.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 4.76 | 14.05 | 23.35 | 2.00 | 89.2 | 90.0 |
| Bench 4 | Bench | Danny Welbeck | FWD | 6 | 6.1 | 3.31 | 9.75 | 15.66 | 12.00 | 70.0 | 82.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.1 | 6.40 | 19.32 | 31.69 | 13.00 | 107.3 | 90.0 |
| XI | Bench | Antoine Semenyo | MID | 13 | 8.3 | 5.16 | 16.41 | 27.75 | 0.00 | 70.3 | 0.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.86 | 15.20 | 25.35 | 2.00 | 77.3 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.9 | 4.61 | 14.20 | 22.69 | 3.00 | 92.2 | 90.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 4.23 | 12.46 | 19.54 | 2.00 | 91.0 | 90.0 |

## GW32

- Train rows: 185188
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 58.57
- Actual score: 60.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martín | GK | 1 | 6.0 | 2.89 | 9.21 | 15.89 | 1.00 | 57.7 | 90.0 |
| XI | XI | Martin Dúbravka | GK | 3 | 4.0 | 3.17 | 9.12 | 14.99 | 2.00 | 88.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 5.05 | 14.70 | 23.24 | 9.00 | 91.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 3.84 | 11.89 | 20.79 | 4.00 | 59.6 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 3.37 | 10.90 | 17.86 | 4.00 | 82.7 | 90.0 |
| Bench 3 | Bench | James Hill | DEF | 4 | 4.2 | 3.35 | 10.68 | 17.34 | 3.00 | 87.8 | 90.0 |
| Bench 4 | Bench | Adrien Truffert | DEF | 4 | 4.6 | 3.08 | 10.12 | 16.79 | 4.00 | 83.3 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 5.58 | 16.89 | 27.78 | 2.00 | 87.1 | 81.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 4.85 | 13.37 | 21.74 | 14.00 | 84.4 | 90.0 |
| Bench 2 | Bench | Danny Welbeck | FWD | 6 | 6.1 | 3.77 | 10.56 | 17.05 | 2.00 | 69.7 | 74.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.34 | 21.75 | 34.62 | 4.00 | 111.2 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.11 | 15.47 | 25.16 | 4.00 | 86.5 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.70 | 13.97 | 22.13 | 5.00 | 86.2 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.3 | 4.36 | 13.73 | 23.63 | 2.00 | 54.1 | 90.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 3.85 | 11.17 | 17.91 | 6.00 | 83.3 | 90.0 |

## GW33

- Train rows: 186014
- Bank: 0.10 -> 0.40
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Cole Palmer
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 83.33
- Actual score: 80.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (24.27) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Adrien Truffert -> Konstantinos Mavropanos (projected gain 1.65, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (24.27) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench Boost | David Raya Martín | GK | 1 | 6.0 | 3.23 | 10.54 | 17.81 | 1.00 | 78.2 | 90.0 |
| XI | XI | Martin Dúbravka | GK | 3 | 4.0 | 4.10 | 9.96 | 15.74 | 4.00 | 113.7 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.76 | 14.35 | 24.09 | 8.00 | 93.9 | 90.0 |
| Bench 4 | Bench Boost | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.37 | 13.47 | 23.10 | 0.00 | 77.8 | 90.0 |
| Bench 3 | Bench Boost | Konstantinos Mavropanos | DEF | 19 | 4.4 | 4.51 | 13.46 | 20.87 | 6.00 | 101.5 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 5.40 | 13.16 | 20.73 | 6.00 | 111.5 | 180.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 5.05 | 12.23 | 19.24 | 5.00 | 110.4 | 180.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 5.91 | 16.57 | 27.25 | 0.00 | 103.8 | 0.0 |
| Bench 2 | Bench Boost | Jarrod Bowen | FWD | 19 | 7.6 | 4.57 | 13.70 | 22.49 | 2.00 | 89.9 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 6 | 6.2 | 5.47 | 12.74 | 19.40 | 8.00 | 91.8 | 81.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.3 | 6.97 | 20.77 | 34.51 | 6.00 | 102.3 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.6 | 6.35 | 16.41 | 26.73 | 2.00 | 110.8 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.2 | 5.84 | 15.98 | 27.00 | 5.00 | 98.6 | 154.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.1 | 4.59 | 13.58 | 22.16 | 5.00 | 85.7 | 90.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 5.28 | 12.79 | 19.84 | 16.00 | 110.6 | 180.0 |

## GW34

- Train rows: 186843
- Bank: 0.40 -> 0.20
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Antoine Semenyo
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 63.56
- Actual score: 48.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (4.68) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Konstantinos Mavropanos -> Jan Paul van Hecke (projected gain 2.80, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (4.68) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.30 | 10.68 | 17.86 | 0.00 | 106.3 | 0.0 |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.41 | 10.15 | 17.17 | 10.00 | 77.4 | 90.0 |
| XI | Bench | Jan Paul van Hecke | DEF | 6 | 4.6 | 4.82 | 14.75 | 23.39 | 0.00 | 104.2 | 0.0 |
| XI | Bench | Marcos Senesi Barón | DEF | 4 | 5.2 | 4.72 | 14.59 | 23.10 | 0.00 | 104.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.93 | 14.56 | 24.19 | 4.00 | 96.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 4.37 | 12.81 | 21.77 | 8.00 | 77.4 | 90.0 |
| XI | Bench | James Hill | DEF | 4 | 4.2 | 4.07 | 12.66 | 20.88 | 0.00 | 97.3 | 0.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.6 | 4.26 | 12.55 | 21.21 | 10.00 | 83.1 | 90.0 |
| Bench 3 | Bench | Danny Welbeck | FWD | 6 | 6.3 | 3.92 | 12.17 | 20.03 | 0.00 | 60.8 | 0.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 2.59 | 10.79 | 19.58 | 0.00 | 23.1 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.3 | 6.18 | 18.21 | 31.41 | 5.00 | 99.0 | 90.0 |
| Vice Captain | Bench | Antoine Semenyo | MID | 13 | 8.2 | 5.34 | 16.92 | 27.97 | 0.00 | 86.6 | 0.0 |
| XI | Bench | Pascal Groß | MID | 6 | 5.5 | 4.67 | 14.34 | 23.17 | 0.00 | 103.7 | 0.0 |
| Bench 2 | Bench | Cole Palmer | MID | 7 | 10.5 | 3.93 | 13.23 | 22.37 | 0.00 | 59.0 | 0.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.1 | 4.44 | 12.75 | 20.89 | 1.00 | 81.4 | 90.0 |