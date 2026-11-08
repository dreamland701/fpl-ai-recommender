# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 299.36
- Total actual points: 271.00
- Average predicted points: 74.84
- Average actual points: 67.75
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW34 are included before the first simulated week.
- League-average scores were not available for this run.

## GW35

- Train rows: 187673
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 63.96
- Actual score: 54.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.61 | 10.59 | 17.60 | 6.00 | 81.4 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.27 | 0.37 | 0.84 | 0.00 | 6.2 | 0.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 5.31 | 15.12 | 23.57 | 1.00 | 63.4 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.95 | 13.89 | 21.81 | 6.00 | 86.7 | 90.0 |
| XI | XI | Neco Williams | DEF | 16 | 4.8 | 4.03 | 11.25 | 18.10 | 1.00 | 77.7 | 45.0 |
| Bench 4 | Bench | Konstantinos Mavropanos | DEF | 19 | 4.5 | 3.75 | 11.08 | 19.48 | -1.00 | 73.7 | 90.0 |
| Bench 3 | Bench | James Justin | DEF | 11 | 3.9 | 4.03 | 10.53 | 17.25 | 2.00 | 59.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 7.45 | 21.21 | 34.64 | 7.00 | 79.3 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.91 | 14.24 | 23.96 | 6.00 | 83.2 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.8 | 4.60 | 14.18 | 24.05 | 2.00 | 77.5 | 87.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.20 | 18.47 | 31.11 | 5.00 | 84.4 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.5 | 5.70 | 15.99 | 25.48 | 5.00 | 61.2 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 5.50 | 15.57 | 25.33 | 4.00 | 81.0 | 20.0 |
| Bench 2 | Bench | Pascal Groß | MID | 6 | 5.5 | 4.12 | 12.30 | 21.59 | 2.00 | 61.1 | 90.0 |
| XI | XI | Enzo Le Fée | MID | 17 | 4.8 | 4.25 | 11.54 | 17.85 | 4.00 | 80.3 | 90.0 |

## GW36

- Train rows: 188505
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Rayan Cherki
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 101.46
- Actual score: 82.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (17.75) beats the best remaining Triple Captain opportunity (8.99).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Morgan Gibbs-White -> Dominik Szoboszlai (projected gain 3.64, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (17.75) beats the best remaining Triple Captain opportunity (8.99).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.94 | 11.44 | 18.69 | 9.00 | 84.2 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.00 | 0.07 | 0.53 | 0.00 | 6.2 | 0.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 9.24 | 14.89 | 22.29 | 5.00 | 147.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.15 | 14.56 | 22.96 | 11.00 | 87.7 | 90.0 |
| XI | XI | Konstantinos Mavropanos | DEF | 19 | 4.5 | 3.19 | 9.57 | 16.01 | 4.00 | 77.3 | 90.0 |
| Bench 3 | Bench | Neco Williams | DEF | 16 | 4.8 | 2.88 | 8.30 | 13.86 | 2.00 | 62.8 | 90.0 |
| Bench 4 | Bench | James Justin | DEF | 11 | 3.9 | 2.78 | 8.24 | 13.83 | 4.00 | 71.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 14.65 | 22.13 | 35.08 | 11.00 | 179.5 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 4.36 | 13.77 | 23.39 | 2.00 | 79.6 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.10 | 12.93 | 21.97 | 2.00 | 77.1 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 7.05 | 20.46 | 33.40 | 3.00 | 86.9 | 90.0 |
| Vice Captain | XI | Rayan Cherki | MID | 13 | 6.5 | 10.95 | 17.23 | 26.39 | 5.00 | 144.7 | 70.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.06 | 13.84 | 22.64 | 2.00 | 83.4 | 90.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 4.47 | 11.75 | 19.48 | 6.00 | 81.2 | 90.0 |
| Bench 2 | Bench | Enzo Le Fée | MID | 17 | 4.8 | 3.72 | 10.31 | 16.64 | 3.00 | 76.1 | 90.0 |

## GW37

- Train rows: 189343
- Bank: 0.60 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 61.52
- Actual score: 71.00
- Transfer: Nico O'Reilly -> Marc Guéhi (projected gain 3.12, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.83 | 12.50 | 19.93 | 6.00 | 85.6 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 1.3 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 6.16 | 15.66 | 24.79 | 6.00 | 88.6 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.47 | 13.05 | 21.66 | 2.00 | 87.4 | 90.0 |
| XI | XI | Konstantinos Mavropanos | DEF | 19 | 4.5 | 3.50 | 10.15 | 16.80 | 3.00 | 80.9 | 90.0 |
| Bench 3 | Bench | Neco Williams | DEF | 16 | 4.8 | 3.32 | 9.97 | 16.25 | 1.00 | 81.6 | 90.0 |
| Bench 4 | Bench | James Justin | DEF | 11 | 3.9 | 2.66 | 7.51 | 13.03 | 6.00 | 61.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 6.80 | 20.93 | 35.47 | 9.00 | 80.7 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.88 | 13.84 | 22.92 | 2.00 | 84.3 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 4.56 | 13.47 | 22.91 | 2.00 | 84.3 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.75 | 19.77 | 32.16 | 9.00 | 85.9 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.5 | 4.38 | 15.09 | 25.23 | 1.00 | 52.5 | 34.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.44 | 12.93 | 21.76 | 9.00 | 82.3 | 90.0 |
| Bench 2 | Bench | Pascal Groß | MID | 6 | 5.5 | 3.48 | 11.16 | 19.60 | 3.00 | 71.1 | 90.0 |
| XI | XI | Enzo Le Fée | MID | 17 | 4.8 | 3.95 | 10.67 | 16.88 | 13.00 | 74.5 | 90.0 |

## GW38

- Train rows: 190183
- Bank: 0.70 -> 1.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 72.42
- Actual score: 64.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.45) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Igor Thiago Nascimento Rodrigues -> Richarlison de Andrade (projected gain 1.39, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.45) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.1 | 4.26 | 11.80 | 18.74 | 0.00 | 81.5 | 0.0 |
| Bench 1 | Bench Boost | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 1.4 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.14 | 14.17 | 22.79 | 1.00 | 83.4 | 45.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.49 | 12.43 | 19.85 | 0.00 | 86.6 | 0.0 |
| XI | XI | Konstantinos Mavropanos | DEF | 19 | 4.5 | 3.80 | 10.48 | 16.76 | 8.00 | 83.5 | 90.0 |
| Bench 3 | Bench Boost | James Justin | DEF | 11 | 3.9 | 3.46 | 9.62 | 15.30 | 1.00 | 77.6 | 90.0 |
| Bench 4 | Bench Boost | Neco Williams | DEF | 16 | 4.8 | 3.25 | 9.10 | 14.86 | 2.00 | 81.9 | 90.0 |
| Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 7.28 | 20.94 | 34.75 | 0.00 | 88.4 | 0.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.8 | 5.03 | 13.79 | 22.34 | 12.00 | 85.1 | 90.0 |
| XI | XI | Richarlison de Andrade | FWD | 18 | 6.5 | 4.72 | 12.60 | 19.33 | 2.00 | 80.6 | 72.0 |
| Vice Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.54 | 19.42 | 32.02 | 14.00 | 84.8 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.5 | 4.69 | 14.12 | 23.40 | 1.00 | 51.9 | 32.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.79 | 13.50 | 22.33 | 2.00 | 86.2 | 90.0 |
| Bench 2 | Bench Boost | Pascal Groß | MID | 6 | 5.5 | 3.74 | 11.24 | 18.58 | 2.00 | 79.6 | 90.0 |
| XI | XI | Enzo Le Fée | MID | 17 | 4.8 | 3.93 | 10.21 | 16.21 | 5.00 | 74.4 | 90.0 |