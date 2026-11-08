# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 286.83
- Total actual points: 269.00
- Average predicted points: 71.71
- Average actual points: 67.25
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
- Predicted score: 58.69
- Actual score: 49.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.37 | 9.88 | 16.41 | 6.00 | 77.7 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.06 | 0.33 | 0.69 | 0.00 | 0.5 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.11 | 14.37 | 22.56 | 6.00 | 90.0 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 3.95 | 11.31 | 17.70 | 1.00 | 60.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 3.61 | 10.86 | 18.52 | 1.00 | 79.8 | 90.0 |
| Bench 2 | Bench | Jaydee Canvot | DEF | 8 | 4.5 | 3.48 | 10.13 | 15.72 | 0.00 | 80.8 | 90.0 |
| Bench 3 | Bench | James Justin | DEF | 11 | 3.9 | 3.13 | 8.21 | 13.46 | 2.00 | 57.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 6.63 | 18.91 | 30.92 | 7.00 | 77.6 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.64 | 13.42 | 22.55 | 6.00 | 82.2 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.3 | 2.63 | 6.90 | 10.57 | 2.00 | 62.4 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.43 | 19.17 | 32.27 | 5.00 | 90.0 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 5.00 | 14.14 | 23.00 | 4.00 | 79.8 | 20.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.56 | 12.94 | 20.15 | 4.00 | 90.0 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.46 | 12.36 | 19.56 | 1.00 | 82.6 | 45.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.28 | 12.30 | 20.20 | 1.00 | 76.5 | 90.0 |

## GW36

- Train rows: 188505
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Nico O'Reilly
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 97.82
- Actual score: 85.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (18.32) beats the best remaining Triple Captain opportunity (9.12).
- Chip advisory: bench_boost (0.56): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Morgan Gibbs-White -> Dominik Szoboszlai (projected gain 3.96, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (18.32) beats the best remaining Triple Captain opportunity (9.12).
- Autosub: Elliot Anderson replaced Carlos Henrique Casimiro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.72 | 10.80 | 17.62 | 9.00 | 79.8 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.34 | 1.67 | 2.12 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.23 | 14.79 | 23.36 | 11.00 | 90.0 | 90.0 |
| Vice Captain | XI | Nico O'Reilly | DEF | 13 | 5.2 | 7.93 | 12.80 | 19.25 | 5.00 | 146.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.60 | 12.33 | 19.91 | 2.00 | 86.5 | 90.0 |
| XI | XI | Jaydee Canvot | DEF | 8 | 4.5 | 6.42 | 10.54 | 15.90 | 4.00 | 157.1 | 180.0 |
| Bench 3 | Bench | James Justin | DEF | 11 | 3.9 | 2.80 | 8.32 | 13.96 | 4.00 | 72.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 14.87 | 22.49 | 35.69 | 11.00 | 180.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.78 | 11.89 | 20.16 | 2.00 | 76.2 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.60 | 7.57 | 11.14 | 2.00 | 68.7 | 66.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 7.18 | 20.82 | 33.97 | 3.00 | 90.0 | 90.0 |
| XI | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.93 | 13.75 | 21.15 | 0.00 | 90.0 | 0.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.95 | 13.49 | 22.05 | 2.00 | 84.8 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.48 | 12.60 | 20.49 | 2.00 | 77.6 | 90.0 |
| Bench 2 | Autosub In | Elliot Anderson | MID | 16 | 5.6 | 3.37 | 9.54 | 15.82 | 12.00 | 63.1 | 90.0 |

## GW37

- Train rows: 189343
- Bank: 0.60 -> 0.70
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Erling Haaland
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 59.51
- Actual score: 93.00
- Transfer: Nico O'Reilly -> Marc Guéhi (projected gain 5.08, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.70 | 12.15 | 19.35 | 6.00 | 82.8 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.14 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 6.27 | 15.96 | 25.29 | 6.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.51 | 13.13 | 21.78 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jaydee Canvot | DEF | 8 | 4.5 | 4.22 | 11.59 | 18.15 | 3.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.91 | 11.28 | 18.74 | 14.00 | 86.0 | 90.0 |
| Bench 3 | Bench | James Justin | DEF | 11 | 3.9 | 2.67 | 7.55 | 13.09 | 6.00 | 61.3 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 6.37 | 19.61 | 33.26 | 9.00 | 81.2 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.63 | 13.07 | 21.60 | 2.00 | 83.7 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.38 | 6.62 | 10.16 | 11.00 | 54.3 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.90 | 20.18 | 32.80 | 9.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.13 | 11.99 | 20.17 | 9.00 | 79.9 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 3.59 | 10.51 | 17.96 | 12.00 | 71.3 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.40 | 10.20 | 17.29 | 12.00 | 76.8 | 90.0 |
| Bench 2 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.69 | 8.19 | 14.26 | 1.00 | 47.8 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 0.70 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 70.81
- Actual score: 42.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.92) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Jaydee Canvot -> Marcos Senesi Barón (projected gain 2.95, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.92) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.1 | 4.33 | 11.96 | 18.98 | 0.00 | 81.3 | 0.0 |
| Bench 1 | Bench Boost | Marcus Bettinelli | GK | 13 | 3.8 | 0.01 | 0.11 | 0.20 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.31 | 14.65 | 23.59 | 1.00 | 89.5 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 5.03 | 14.01 | 22.35 | 2.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.57 | 12.60 | 20.09 | 0.00 | 90.0 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.2 | 4.30 | 12.54 | 20.33 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | James Justin | DEF | 11 | 3.9 | 3.46 | 9.61 | 15.29 | 1.00 | 78.2 | 90.0 |
| Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 7.40 | 21.33 | 35.42 | 0.00 | 90.0 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 3.96 | 11.69 | 19.25 | 2.00 | 79.6 | 90.0 |
| Bench 3 | Bench Boost | Mateus Mané | FWD | 20 | 4.2 | 3.04 | 8.00 | 12.58 | 2.00 | 65.1 | 90.0 |
| Vice Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.80 | 20.17 | 33.24 | 14.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.89 | 13.75 | 22.73 | 2.00 | 89.9 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.90 | 12.28 | 20.16 | 0.00 | 85.9 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.00 | 11.64 | 19.26 | 2.00 | 90.0 | 64.0 |
| Bench 4 | Bench Boost | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.41 | 7.31 | 13.47 | 0.00 | 51.7 | 0.0 |