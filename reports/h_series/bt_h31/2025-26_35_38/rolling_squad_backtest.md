# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 276.94
- Total actual points: 270.00
- Average predicted points: 69.24
- Average actual points: 67.50
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
- Predicted score: 56.73
- Actual score: 49.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.22 | 9.75 | 16.49 | 6.00 | 81.9 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.06 | 0.00 | 0.15 | 0.00 | 3.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.96 | 14.38 | 22.54 | 6.00 | 91.6 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 3.69 | 10.95 | 17.52 | 1.00 | 61.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 3.46 | 10.85 | 18.42 | 1.00 | 80.6 | 90.0 |
| Bench 3 | Bench | Konstantinos Mavropanos | DEF | 19 | 4.5 | 2.91 | 8.99 | 15.91 | -1.00 | 71.4 | 90.0 |
| Bench 2 | Bench | James Justin | DEF | 11 | 3.9 | 2.93 | 7.89 | 13.08 | 2.00 | 58.6 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 6.42 | 18.66 | 30.52 | 7.00 | 78.6 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.53 | 13.32 | 22.51 | 6.00 | 85.1 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.3 | 2.69 | 7.16 | 11.07 | 2.00 | 63.9 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.25 | 19.16 | 32.25 | 5.00 | 92.0 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 4.90 | 14.28 | 23.19 | 4.00 | 81.7 | 20.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.44 | 12.88 | 20.03 | 4.00 | 92.4 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.33 | 12.49 | 19.91 | 1.00 | 86.0 | 45.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.10 | 12.31 | 20.19 | 1.00 | 78.6 | 90.0 |

## GW36

- Train rows: 188505
- Bank: 0.00 -> 1.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Rayan Cherki
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 96.58
- Actual score: 88.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (17.66) beats the best remaining Triple Captain opportunity (8.94).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Morgan Gibbs-White -> Rayan Cherki (projected gain 5.64, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (17.66) beats the best remaining Triple Captain opportunity (8.94).
- Autosub: Konstantinos Mavropanos replaced Carlos Henrique Casimiro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.53 | 10.77 | 17.77 | 9.00 | 84.4 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 1.3 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.10 | 14.71 | 23.32 | 11.00 | 92.3 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 7.73 | 12.49 | 18.95 | 5.00 | 145.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.46 | 12.12 | 19.86 | 2.00 | 87.5 | 90.0 |
| Bench 2 | Autosub In | Konstantinos Mavropanos | DEF | 19 | 4.5 | 2.78 | 8.72 | 14.68 | 4.00 | 77.7 | 90.0 |
| Bench 3 | Bench | James Justin | DEF | 11 | 3.9 | 2.78 | 8.24 | 13.83 | 4.00 | 71.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 14.56 | 22.15 | 35.13 | 11.00 | 182.9 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.66 | 12.03 | 20.55 | 2.00 | 79.4 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.66 | 7.83 | 11.64 | 2.00 | 70.4 | 66.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 7.05 | 20.73 | 33.99 | 3.00 | 92.5 | 90.0 |
| Vice Captain | XI | Rayan Cherki | MID | 13 | 6.6 | 8.91 | 14.34 | 21.95 | 5.00 | 145.7 | 70.0 |
| XI | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.80 | 13.64 | 20.99 | 0.00 | 92.2 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.34 | 12.53 | 20.41 | 2.00 | 79.9 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.32 | 9.87 | 16.31 | 12.00 | 67.0 | 90.0 |

## GW37

- Train rows: 189343
- Bank: 1.00 -> 1.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 55.52
- Actual score: 85.00
- Transfer: Nico O'Reilly -> Marc Guéhi (projected gain 4.92, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.45 | 11.63 | 18.95 | 6.00 | 86.0 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.02 | 0.00 | 0.01 | 0.00 | 1.4 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 6.13 | 15.91 | 25.44 | 6.00 | 92.2 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.40 | 13.12 | 22.16 | 2.00 | 92.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.77 | 11.19 | 18.39 | 14.00 | 87.3 | 90.0 |
| XI | XI | Konstantinos Mavropanos | DEF | 19 | 4.5 | 3.06 | 9.09 | 15.41 | 3.00 | 80.8 | 90.0 |
| Bench 3 | Bench | James Justin | DEF | 11 | 3.9 | 2.66 | 7.51 | 13.03 | 6.00 | 61.0 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.6 | 6.04 | 19.13 | 32.89 | 9.00 | 81.8 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.51 | 13.21 | 21.99 | 2.00 | 87.1 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.42 | 6.82 | 10.55 | 11.00 | 56.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.72 | 19.96 | 32.50 | 9.00 | 92.2 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.6 | 2.94 | 10.44 | 17.65 | 1.00 | 51.8 | 34.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 3.47 | 10.33 | 17.94 | 12.00 | 72.6 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.31 | 10.25 | 17.50 | 12.00 | 79.9 | 90.0 |
| Bench 2 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.73 | 8.34 | 14.52 | 1.00 | 48.4 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 1.10 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 68.12
- Actual score: 48.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.81) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Rayan Cherki -> Dominik Szoboszlai (projected gain 4.36, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.81) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.1 | 4.12 | 11.84 | 18.95 | 0.00 | 85.4 | 0.0 |
| Bench 1 | Bench Boost | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.8 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.17 | 14.57 | 23.36 | 1.00 | 90.6 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.87 | 13.81 | 22.38 | 2.00 | 92.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.31 | 12.12 | 19.70 | 0.00 | 89.7 | 0.0 |
| XI | XI | Konstantinos Mavropanos | DEF | 19 | 4.5 | 3.59 | 10.30 | 16.32 | 8.00 | 85.8 | 90.0 |
| Bench 2 | Bench Boost | James Justin | DEF | 11 | 3.9 | 3.27 | 9.31 | 14.82 | 1.00 | 79.2 | 90.0 |
| Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 7.17 | 20.83 | 34.78 | 0.00 | 92.1 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 3.80 | 11.28 | 18.82 | 2.00 | 80.8 | 90.0 |
| Bench 3 | Bench Boost | Mateus Mané | FWD | 20 | 4.2 | 3.08 | 8.21 | 13.01 | 2.00 | 67.3 | 90.0 |
| Vice Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.61 | 19.98 | 33.07 | 14.00 | 91.4 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.1 | 4.79 | 13.65 | 22.68 | 2.00 | 91.3 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.84 | 12.27 | 20.45 | 0.00 | 88.1 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.87 | 11.39 | 19.13 | 2.00 | 90.4 | 64.0 |
| Bench 4 | Bench Boost | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.46 | 7.49 | 13.79 | 0.00 | 52.5 | 0.0 |