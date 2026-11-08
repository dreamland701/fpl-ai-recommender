# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 264.97
- Total actual points: 234.00
- Average predicted points: 66.24
- Average actual points: 58.50
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW30 are included before the first simulated week.
- League-average scores were not available for this run.

## GW31

- Train rows: 184363
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 59.49
- Actual score: 46.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Marcos Senesi Barón replaced Gabriel dos Santos Magalhães.
- Autosub: Adrien Truffert replaced Antoine Semenyo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martín | GK | 1 | 6.0 | 3.28 | 11.16 | 19.02 | 0.00 | 73.5 | 0.0 |
| XI | XI | Martin Dúbravka | GK | 3 | 4.0 | 3.29 | 9.64 | 15.69 | 2.00 | 88.9 | 90.0 |
| XI | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.60 | 14.84 | 25.21 | 0.00 | 79.5 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 4.81 | 14.65 | 24.10 | 3.00 | 91.7 | 90.0 |
| Bench 2 | Autosub In | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.13 | 12.04 | 19.40 | 1.00 | 87.7 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 4.24 | 11.98 | 19.46 | -1.00 | 88.8 | 90.0 |
| Bench 3 | Autosub In | Adrien Truffert | DEF | 4 | 4.6 | 3.83 | 11.15 | 18.37 | 4.00 | 84.6 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.03 | 18.05 | 29.58 | 2.00 | 89.6 | 77.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 4.79 | 14.17 | 23.62 | 2.00 | 89.2 | 90.0 |
| Bench 4 | Bench | Danny Welbeck | FWD | 6 | 6.1 | 3.31 | 9.81 | 15.78 | 12.00 | 70.0 | 82.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.1 | 6.42 | 19.45 | 32.16 | 13.00 | 107.3 | 90.0 |
| XI | Bench | Antoine Semenyo | MID | 13 | 8.3 | 5.16 | 16.51 | 27.94 | 0.00 | 70.3 | 0.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.87 | 15.37 | 25.63 | 2.00 | 77.2 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.9 | 4.62 | 14.29 | 23.00 | 3.00 | 92.1 | 90.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 4.23 | 12.55 | 19.83 | 2.00 | 91.0 | 90.0 |

## GW32

- Train rows: 185188
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 58.63
- Actual score: 60.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martín | GK | 1 | 6.0 | 2.91 | 9.27 | 16.07 | 1.00 | 57.7 | 90.0 |
| XI | XI | Martin Dúbravka | GK | 3 | 4.0 | 3.19 | 9.18 | 15.14 | 2.00 | 88.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 5.05 | 14.73 | 23.33 | 9.00 | 91.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 3.86 | 11.97 | 20.87 | 4.00 | 59.6 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.40 | 10.95 | 17.95 | 4.00 | 82.7 | 90.0 |
| Bench 3 | Bench | James Hill | DEF | 4 | 4.2 | 3.37 | 10.64 | 17.37 | 3.00 | 87.8 | 90.0 |
| Bench 4 | Bench | Adrien Truffert | DEF | 4 | 4.6 | 3.11 | 10.14 | 16.85 | 4.00 | 83.2 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.57 | 16.94 | 28.06 | 2.00 | 87.1 | 81.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 4.82 | 13.41 | 22.00 | 14.00 | 84.4 | 90.0 |
| Bench 2 | Bench | Danny Welbeck | FWD | 6 | 6.1 | 3.80 | 10.61 | 17.11 | 2.00 | 69.7 | 74.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.1 | 7.34 | 21.83 | 35.10 | 4.00 | 111.2 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.10 | 15.49 | 25.34 | 4.00 | 86.5 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.9 | 4.70 | 13.96 | 22.22 | 5.00 | 86.2 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.3 | 4.37 | 13.89 | 23.98 | 2.00 | 54.1 | 90.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 3.87 | 11.17 | 18.05 | 6.00 | 83.3 | 90.0 |

## GW33

- Train rows: 186014
- Bank: 0.10 -> 0.30
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Cole Palmer
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 83.25
- Actual score: 80.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (24.26) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Adrien Truffert -> Konstantinos Mavropanos (projected gain 1.66, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (24.26) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench Boost | David Raya Martín | GK | 1 | 6.0 | 3.21 | 10.51 | 17.81 | 1.00 | 78.2 | 90.0 |
| XI | XI | Martin Dúbravka | GK | 3 | 4.0 | 4.07 | 9.99 | 15.82 | 4.00 | 113.7 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 4.76 | 14.32 | 24.01 | 8.00 | 93.9 | 90.0 |
| Bench 4 | Bench Boost | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.36 | 13.45 | 23.05 | 0.00 | 77.8 | 90.0 |
| Bench 3 | Bench Boost | Konstantinos Mavropanos | DEF | 19 | 4.4 | 4.52 | 13.35 | 20.89 | 6.00 | 101.5 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 5.38 | 13.10 | 20.62 | 6.00 | 111.5 | 180.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 5.03 | 12.19 | 19.13 | 5.00 | 110.4 | 180.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.90 | 16.64 | 27.44 | 0.00 | 103.9 | 0.0 |
| Bench 2 | Bench Boost | Jarrod Bowen | FWD | 19 | 7.5 | 4.58 | 13.68 | 22.55 | 2.00 | 89.9 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 6 | 6.1 | 5.44 | 12.63 | 19.32 | 8.00 | 91.9 | 81.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.98 | 20.80 | 34.81 | 6.00 | 102.3 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.6 | 6.33 | 16.41 | 26.64 | 2.00 | 110.8 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.2 | 5.88 | 16.08 | 27.16 | 5.00 | 98.6 | 154.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.59 | 13.54 | 22.04 | 5.00 | 85.7 | 90.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 5.25 | 12.73 | 19.85 | 16.00 | 110.6 | 180.0 |

## GW34

- Train rows: 186843
- Bank: 0.30 -> 0.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Antoine Semenyo
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 63.60
- Actual score: 48.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (4.70) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Konstantinos Mavropanos -> Jan Paul van Hecke (projected gain 2.79, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (4.70) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.30 | 10.72 | 17.95 | 0.00 | 106.3 | 0.0 |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.39 | 10.15 | 17.15 | 10.00 | 77.4 | 90.0 |
| XI | Bench | Jan Paul van Hecke | DEF | 6 | 4.6 | 4.82 | 14.68 | 23.41 | 0.00 | 104.2 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 4.94 | 14.59 | 24.11 | 4.00 | 96.7 | 90.0 |
| XI | Bench | Marcos Senesi Barón | DEF | 4 | 5.1 | 4.73 | 14.54 | 23.36 | 0.00 | 104.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 4.35 | 12.71 | 21.98 | 8.00 | 77.4 | 90.0 |
| XI | Bench | James Hill | DEF | 4 | 4.2 | 4.07 | 12.55 | 20.76 | 0.00 | 97.3 | 0.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 4.26 | 12.56 | 21.21 | 10.00 | 83.1 | 90.0 |
| Bench 3 | Bench | Danny Welbeck | FWD | 6 | 6.2 | 3.92 | 12.12 | 19.95 | 0.00 | 60.8 | 0.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 2.59 | 10.87 | 19.88 | 0.00 | 23.1 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.20 | 18.27 | 31.68 | 5.00 | 98.9 | 90.0 |
| Vice Captain | Bench | Antoine Semenyo | MID | 13 | 8.2 | 5.34 | 16.96 | 28.15 | 0.00 | 86.6 | 0.0 |
| XI | Bench | Pascal Groß | MID | 6 | 5.5 | 4.68 | 14.33 | 23.44 | 0.00 | 103.7 | 0.0 |
| Bench 2 | Bench | Cole Palmer | MID | 7 | 10.5 | 3.93 | 13.23 | 22.45 | 0.00 | 59.0 | 0.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.45 | 12.70 | 20.98 | 1.00 | 81.4 | 90.0 |