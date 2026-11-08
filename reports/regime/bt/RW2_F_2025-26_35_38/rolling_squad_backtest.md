# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 283.51
- Total actual points: 261.00
- Average predicted points: 70.88
- Average actual points: 65.25
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
- Predicted score: 56.92
- Actual score: 48.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.25 | 9.83 | 16.18 | 6.00 | 81.1 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.03 | 0.00 | 0.00 | 0.00 | 3.3 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.00 | 14.52 | 22.63 | 6.00 | 90.0 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 3.83 | 11.09 | 17.18 | 1.00 | 57.3 | 90.0 |
| Bench 2 | Bench | Virgil van Dijk | DEF | 12 | 6.2 | 3.49 | 10.80 | 18.27 | 1.00 | 78.6 | 90.0 |
| XI | XI | Jaydee Canvot | DEF | 8 | 4.5 | 3.54 | 10.26 | 15.93 | 0.00 | 81.2 | 90.0 |
| Bench 3 | Bench | James Justin | DEF | 11 | 3.9 | 3.04 | 7.95 | 12.98 | 2.00 | 53.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 6.16 | 17.79 | 28.94 | 7.00 | 69.2 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.69 | 13.56 | 22.63 | 6.00 | 83.6 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.3 | 2.74 | 7.29 | 11.20 | 2.00 | 66.2 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.16 | 18.61 | 31.31 | 5.00 | 90.0 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 4.96 | 14.07 | 22.77 | 4.00 | 79.9 | 20.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.48 | 13.10 | 20.19 | 4.00 | 90.0 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.46 | 12.64 | 19.97 | 1.00 | 83.8 | 45.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.21 | 12.08 | 19.62 | 1.00 | 76.5 | 90.0 |

## GW36

- Train rows: 188505
- Bank: 0.00 -> 1.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Rayan Cherki
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 100.16
- Actual score: 88.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (17.71) beats the best remaining Triple Captain opportunity (8.75).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Morgan Gibbs-White -> Rayan Cherki (projected gain 4.25, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (17.71) beats the best remaining Triple Captain opportunity (8.75).
- Autosub: Elliot Anderson replaced Carlos Henrique Casimiro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.67 | 10.77 | 17.41 | 9.00 | 83.2 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 1.5 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.17 | 14.90 | 23.46 | 11.00 | 90.0 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 7.95 | 12.38 | 18.87 | 5.00 | 145.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.52 | 12.18 | 19.47 | 2.00 | 85.4 | 90.0 |
| XI | XI | Jaydee Canvot | DEF | 8 | 4.5 | 6.62 | 10.81 | 16.40 | 4.00 | 156.1 | 180.0 |
| Bench 3 | Bench | James Justin | DEF | 11 | 3.9 | 2.88 | 8.38 | 13.90 | 4.00 | 72.3 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 14.26 | 21.37 | 33.98 | 11.00 | 180.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.83 | 12.10 | 20.51 | 2.00 | 77.9 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.72 | 7.93 | 11.93 | 2.00 | 71.8 | 66.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.95 | 20.32 | 33.07 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Rayan Cherki | MID | 13 | 6.6 | 9.32 | 14.05 | 22.12 | 5.00 | 148.6 | 70.0 |
| XI | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.92 | 13.89 | 21.30 | 0.00 | 90.0 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.44 | 12.42 | 19.93 | 2.00 | 77.2 | 90.0 |
| Bench 2 | Autosub In | Elliot Anderson | MID | 16 | 5.6 | 3.40 | 9.82 | 16.14 | 12.00 | 63.6 | 90.0 |

## GW37

- Train rows: 189343
- Bank: 1.00 -> 1.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Erling Haaland
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 57.86
- Actual score: 85.00
- Transfer: Nico O'Reilly -> Marc Guéhi (projected gain 5.37, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.55 | 11.93 | 18.74 | 6.00 | 85.8 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.01 | 0.00 | 0.00 | 0.00 | 1.3 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 6.03 | 15.58 | 24.42 | 6.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.57 | 13.01 | 21.53 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jaydee Canvot | DEF | 8 | 4.5 | 4.41 | 11.90 | 18.60 | 3.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.91 | 11.13 | 18.39 | 14.00 | 84.9 | 90.0 |
| Bench 2 | Bench | James Justin | DEF | 11 | 3.9 | 2.74 | 7.66 | 13.31 | 6.00 | 63.2 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 6.05 | 18.50 | 31.24 | 9.00 | 79.3 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.69 | 13.12 | 21.62 | 2.00 | 85.1 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.40 | 6.74 | 10.60 | 11.00 | 56.2 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.72 | 19.83 | 32.20 | 9.00 | 90.0 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.51 | 10.62 | 17.93 | 12.00 | 78.6 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 3.59 | 10.48 | 17.82 | 12.00 | 71.8 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.6 | 3.12 | 10.39 | 17.54 | 1.00 | 52.3 | 34.0 |
| Bench 3 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.63 | 8.07 | 14.10 | 1.00 | 45.2 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 1.10 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 68.56
- Actual score: 40.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.92) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Rayan Cherki -> Dominik Szoboszlai (projected gain 3.97, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.92) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.1 | 4.15 | 11.61 | 18.23 | 0.00 | 83.8 | 0.0 |
| Bench 1 | Bench Boost | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.7 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.09 | 14.18 | 22.73 | 1.00 | 87.3 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 5.09 | 14.16 | 22.53 | 2.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.55 | 12.64 | 19.97 | 0.00 | 90.0 | 0.0 |
| XI | XI | James Justin | DEF | 11 | 3.9 | 3.44 | 9.65 | 15.45 | 1.00 | 79.0 | 90.0 |
| Bench 2 | Bench Boost | Jaydee Canvot | DEF | 8 | 4.5 | 3.38 | 9.63 | 15.29 | 0.00 | 84.5 | 0.0 |
| Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 6.98 | 20.21 | 33.02 | 0.00 | 90.0 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 3.98 | 12.01 | 19.84 | 2.00 | 79.6 | 90.0 |
| Bench 3 | Bench Boost | Mateus Mané | FWD | 20 | 4.2 | 3.01 | 8.11 | 12.82 | 2.00 | 67.7 | 90.0 |
| Vice Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.60 | 19.64 | 32.42 | 14.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.1 | 4.85 | 13.58 | 22.47 | 2.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.90 | 12.23 | 20.02 | 0.00 | 86.4 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.04 | 11.75 | 19.35 | 2.00 | 90.0 | 64.0 |
| Bench 4 | Bench Boost | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.53 | 7.42 | 13.92 | 0.00 | 53.9 | 0.0 |