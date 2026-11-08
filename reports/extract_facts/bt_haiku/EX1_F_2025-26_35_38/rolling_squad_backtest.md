# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 295.09
- Total actual points: 262.00
- Average predicted points: 73.77
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
- Predicted score: 60.85
- Actual score: 49.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.38 | 9.92 | 16.45 | 6.00 | 80.2 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.06 | 0.00 | 0.16 | 0.00 | 3.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.16 | 14.49 | 22.72 | 6.00 | 90.0 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 4.34 | 12.25 | 19.22 | 1.00 | 67.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 3.75 | 11.24 | 19.06 | 1.00 | 80.3 | 90.0 |
| Bench 2 | Bench | Jaydee Canvot | DEF | 8 | 4.5 | 3.46 | 10.03 | 15.54 | 0.00 | 80.3 | 90.0 |
| Bench 3 | Bench | James Justin | DEF | 11 | 3.9 | 3.13 | 8.20 | 13.39 | 2.00 | 56.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 7.23 | 20.69 | 33.66 | 7.00 | 89.7 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.73 | 13.72 | 23.04 | 6.00 | 83.2 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.3 | 2.70 | 7.18 | 11.09 | 2.00 | 64.0 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.45 | 19.21 | 32.30 | 5.00 | 90.0 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 5.10 | 14.42 | 23.39 | 4.00 | 79.9 | 20.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.64 | 13.18 | 20.55 | 4.00 | 90.0 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.53 | 12.60 | 19.99 | 1.00 | 84.3 | 45.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.31 | 12.37 | 20.26 | 1.00 | 76.8 | 90.0 |

## GW36

- Train rows: 188505
- Bank: 0.00 -> 1.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Rayan Cherki
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 102.33
- Actual score: 88.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (18.10) beats the best remaining Triple Captain opportunity (9.30).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Morgan Gibbs-White -> Rayan Cherki (projected gain 4.32, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (18.10) beats the best remaining Triple Captain opportunity (9.30).
- Autosub: Elliot Anderson replaced Carlos Henrique Casimiro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.70 | 10.73 | 17.51 | 9.00 | 81.8 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 1.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.24 | 14.81 | 23.35 | 11.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.68 | 12.55 | 20.24 | 2.00 | 86.3 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 7.74 | 12.51 | 18.72 | 5.00 | 142.4 | 90.0 |
| XI | XI | Jaydee Canvot | DEF | 8 | 4.5 | 7.05 | 11.07 | 16.65 | 4.00 | 178.7 | 180.0 |
| Bench 3 | Bench | James Justin | DEF | 11 | 3.9 | 2.80 | 8.29 | 13.88 | 4.00 | 72.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 14.65 | 22.18 | 35.12 | 11.00 | 180.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.93 | 12.37 | 20.93 | 2.00 | 77.9 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.64 | 7.78 | 11.57 | 2.00 | 70.0 | 66.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 7.58 | 21.97 | 35.75 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Rayan Cherki | MID | 13 | 6.6 | 8.96 | 14.16 | 21.69 | 5.00 | 140.3 | 70.0 |
| XI | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.98 | 13.94 | 21.46 | 0.00 | 90.0 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.53 | 12.71 | 20.62 | 2.00 | 78.0 | 90.0 |
| Bench 2 | Autosub In | Elliot Anderson | MID | 16 | 5.6 | 3.47 | 9.88 | 16.39 | 12.00 | 64.8 | 90.0 |

## GW37

- Train rows: 189343
- Bank: 1.00 -> 1.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 59.83
- Actual score: 85.00
- Transfer: Nico O'Reilly -> Marc Guéhi (projected gain 5.09, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.69 | 12.14 | 19.34 | 6.00 | 84.5 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.02 | 0.00 | 0.01 | 0.00 | 1.4 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 6.28 | 15.97 | 25.26 | 6.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.57 | 13.36 | 22.15 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jaydee Canvot | DEF | 8 | 4.5 | 4.18 | 11.47 | 17.92 | 3.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.96 | 11.43 | 18.94 | 14.00 | 85.3 | 90.0 |
| Bench 3 | Bench | James Justin | DEF | 11 | 3.9 | 2.67 | 7.55 | 13.07 | 6.00 | 61.3 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 6.95 | 21.28 | 35.87 | 9.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.74 | 13.44 | 22.20 | 2.00 | 84.7 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.41 | 6.80 | 10.52 | 11.00 | 55.8 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.88 | 20.19 | 32.81 | 9.00 | 90.0 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.79 | 11.10 | 18.67 | 12.00 | 89.3 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.6 | 3.16 | 10.87 | 18.13 | 1.00 | 50.1 | 34.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 3.67 | 10.72 | 18.25 | 12.00 | 72.0 | 90.0 |
| Bench 2 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.76 | 8.40 | 14.59 | 1.00 | 48.8 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 1.10 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 72.09
- Actual score: 40.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.80) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Carlos Henrique Casimiro -> Bruno Guimarães Rodriguez Moura (projected gain 3.45, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.80) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.1 | 4.31 | 11.95 | 18.96 | 0.00 | 83.3 | 0.0 |
| Bench 1 | Bench Boost | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.8 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.33 | 14.71 | 23.62 | 1.00 | 88.0 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 5.07 | 14.15 | 22.58 | 2.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.64 | 12.87 | 20.53 | 0.00 | 90.0 | 0.0 |
| Bench 2 | Bench Boost | James Justin | DEF | 11 | 3.9 | 3.47 | 9.63 | 15.31 | 1.00 | 78.1 | 90.0 |
| Bench 3 | Bench Boost | Jaydee Canvot | DEF | 8 | 4.5 | 3.25 | 9.35 | 14.83 | 0.00 | 84.7 | 0.0 |
| Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 7.81 | 21.95 | 36.19 | 0.00 | 90.0 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 4.07 | 12.08 | 19.90 | 2.00 | 80.8 | 90.0 |
| Bench 4 | Bench Boost | Mateus Mané | FWD | 20 | 4.2 | 3.08 | 8.22 | 13.02 | 2.00 | 67.2 | 90.0 |
| Vice Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.75 | 20.09 | 33.12 | 14.00 | 90.0 | 90.0 |
| XI | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 6.9 | 4.46 | 13.01 | 20.10 | 1.00 | 81.6 | 65.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 4.00 | 12.56 | 20.57 | 0.00 | 86.4 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.05 | 11.86 | 19.68 | 2.00 | 90.0 | 64.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.5 | 3.98 | 11.50 | 18.65 | 1.00 | 58.6 | 32.0 |