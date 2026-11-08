# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 289.10
- Total actual points: 262.00
- Average predicted points: 72.28
- Average actual points: 65.50
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
- Predicted score: 58.61
- Actual score: 49.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.37 | 9.83 | 16.28 | 6.00 | 79.9 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.16 | 0.24 | 0.52 | 0.00 | 3.1 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.18 | 14.59 | 22.95 | 6.00 | 90.0 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 4.05 | 11.63 | 18.24 | 1.00 | 61.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 3.65 | 10.99 | 18.73 | 1.00 | 79.9 | 90.0 |
| Bench 2 | Bench | Jaydee Canvot | DEF | 8 | 4.5 | 3.48 | 10.13 | 15.73 | 0.00 | 80.5 | 90.0 |
| Bench 3 | Bench | James Justin | DEF | 11 | 3.9 | 3.19 | 8.38 | 13.76 | 2.00 | 57.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 6.62 | 18.86 | 30.83 | 7.00 | 78.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.62 | 13.32 | 22.36 | 6.00 | 82.8 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.3 | 2.61 | 6.83 | 10.44 | 2.00 | 62.6 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.41 | 19.08 | 32.11 | 5.00 | 90.0 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 4.97 | 14.04 | 22.81 | 4.00 | 79.6 | 20.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.51 | 12.74 | 19.80 | 4.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.25 | 12.20 | 20.03 | 1.00 | 76.3 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.37 | 12.08 | 19.09 | 1.00 | 82.6 | 45.0 |

## GW36

- Train rows: 188505
- Bank: 0.00 -> 1.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Rayan Cherki
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 102.16
- Actual score: 88.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (18.32) beats the best remaining Triple Captain opportunity (9.12).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Morgan Gibbs-White -> Rayan Cherki (projected gain 5.07, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (18.32) beats the best remaining Triple Captain opportunity (9.12).
- Autosub: Elliot Anderson replaced Carlos Henrique Casimiro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.72 | 10.74 | 17.47 | 9.00 | 82.0 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.09 | 0.27 | 0.00 | 1.4 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.32 | 15.10 | 23.87 | 11.00 | 90.0 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 8.11 | 13.12 | 19.78 | 5.00 | 146.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.63 | 12.45 | 20.11 | 2.00 | 86.7 | 90.0 |
| XI | XI | Jaydee Canvot | DEF | 8 | 4.5 | 6.45 | 10.61 | 16.01 | 4.00 | 156.7 | 180.0 |
| Bench 3 | Bench | James Justin | DEF | 11 | 3.9 | 2.85 | 8.49 | 14.25 | 4.00 | 72.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 14.87 | 22.47 | 35.64 | 11.00 | 180.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.76 | 11.79 | 19.98 | 2.00 | 76.8 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.59 | 7.52 | 11.04 | 2.00 | 69.2 | 66.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 7.16 | 20.75 | 33.84 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Rayan Cherki | MID | 13 | 6.6 | 9.10 | 14.32 | 21.95 | 5.00 | 140.7 | 70.0 |
| XI | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.86 | 13.49 | 20.70 | 0.00 | 90.0 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.45 | 12.49 | 20.31 | 2.00 | 77.5 | 90.0 |
| Bench 2 | Autosub In | Elliot Anderson | MID | 16 | 5.6 | 3.29 | 9.27 | 15.36 | 12.00 | 62.9 | 90.0 |

## GW37

- Train rows: 189343
- Bank: 1.00 -> 1.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Erling Haaland
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 58.58
- Actual score: 85.00
- Transfer: Nico O'Reilly -> Marc Guéhi (projected gain 5.77, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.70 | 12.08 | 19.22 | 6.00 | 84.9 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.12 | 0.20 | 0.38 | 0.00 | 1.5 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 6.35 | 16.22 | 25.73 | 6.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.59 | 13.39 | 22.21 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jaydee Canvot | DEF | 8 | 4.5 | 4.23 | 11.66 | 18.25 | 3.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.96 | 11.47 | 19.05 | 14.00 | 86.4 | 90.0 |
| Bench 2 | Bench | James Justin | DEF | 11 | 3.9 | 2.69 | 7.63 | 13.23 | 6.00 | 61.4 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 6.36 | 19.60 | 33.24 | 9.00 | 81.6 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.62 | 13.04 | 21.54 | 2.00 | 84.4 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.36 | 6.59 | 10.09 | 11.00 | 54.8 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.87 | 20.11 | 32.66 | 9.00 | 90.0 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.6 | 3.15 | 10.84 | 18.11 | 1.00 | 48.2 | 34.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 3.56 | 10.42 | 17.79 | 12.00 | 71.2 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.32 | 9.93 | 16.81 | 12.00 | 76.5 | 90.0 |
| Bench 3 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.61 | 7.95 | 13.81 | 1.00 | 48.1 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 1.10 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 69.75
- Actual score: 40.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.65) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Rayan Cherki -> Dominik Szoboszlai (projected gain 3.72, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.65) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.1 | 4.32 | 11.91 | 18.86 | 0.00 | 83.5 | 0.0 |
| Bench 1 | Bench Boost | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.07 | 0.19 | 0.00 | 1.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.39 | 14.91 | 24.04 | 1.00 | 90.0 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 5.07 | 14.16 | 22.61 | 2.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.64 | 12.84 | 20.50 | 0.00 | 90.0 | 0.0 |
| XI | XI | James Justin | DEF | 11 | 3.9 | 3.48 | 9.70 | 15.43 | 1.00 | 78.2 | 90.0 |
| Bench 2 | Bench Boost | Jaydee Canvot | DEF | 8 | 4.5 | 3.30 | 9.53 | 15.15 | 0.00 | 85.4 | 0.0 |
| Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 7.41 | 21.34 | 35.44 | 0.00 | 90.0 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 3.95 | 11.66 | 19.17 | 2.00 | 80.3 | 90.0 |
| Bench 3 | Bench Boost | Mateus Mané | FWD | 20 | 4.2 | 3.02 | 7.94 | 12.46 | 2.00 | 65.8 | 90.0 |
| Vice Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.78 | 20.10 | 33.10 | 14.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.1 | 4.86 | 13.66 | 22.56 | 2.00 | 89.8 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.87 | 12.19 | 19.98 | 0.00 | 85.8 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.93 | 11.40 | 18.81 | 2.00 | 89.9 | 64.0 |
| Bench 4 | Bench Boost | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.33 | 7.06 | 13.01 | 0.00 | 51.8 | 0.0 |