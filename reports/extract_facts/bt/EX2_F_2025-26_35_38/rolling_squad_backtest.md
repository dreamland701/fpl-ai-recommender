# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 297.02
- Total actual points: 262.00
- Average predicted points: 74.25
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
- Predicted score: 59.30
- Actual score: 49.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.42 | 10.00 | 16.50 | 6.00 | 81.2 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.08 | 0.00 | 0.22 | 0.00 | 3.6 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.18 | 14.53 | 22.71 | 6.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 3.81 | 11.33 | 19.11 | 1.00 | 81.8 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 3.91 | 11.12 | 17.24 | 1.00 | 59.7 | 90.0 |
| Bench 2 | Bench | Jaydee Canvot | DEF | 8 | 4.5 | 3.48 | 10.09 | 15.58 | 0.00 | 81.0 | 90.0 |
| Bench 3 | Bench | James Justin | DEF | 11 | 3.9 | 3.12 | 8.15 | 13.39 | 2.00 | 56.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 6.59 | 18.75 | 30.48 | 7.00 | 76.8 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.77 | 13.78 | 23.04 | 6.00 | 84.3 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.3 | 2.78 | 7.32 | 11.20 | 2.00 | 66.3 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.38 | 19.09 | 32.22 | 5.00 | 90.0 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 5.13 | 14.49 | 23.40 | 4.00 | 80.9 | 20.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.60 | 13.07 | 20.47 | 4.00 | 90.0 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.57 | 12.67 | 20.02 | 1.00 | 85.3 | 45.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.34 | 12.42 | 20.25 | 1.00 | 77.6 | 90.0 |

## GW36

- Train rows: 188505
- Bank: 0.00 -> 1.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Rayan Cherki
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 105.89
- Actual score: 88.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (18.73) beats the best remaining Triple Captain opportunity (9.82).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Morgan Gibbs-White -> Rayan Cherki (projected gain 4.69, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (18.73) beats the best remaining Triple Captain opportunity (9.82).
- Autosub: Elliot Anderson replaced Carlos Henrique Casimiro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.72 | 10.78 | 17.53 | 9.00 | 82.3 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.26 | 14.85 | 23.35 | 11.00 | 90.0 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 8.44 | 12.96 | 19.52 | 5.00 | 157.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.73 | 12.64 | 20.29 | 2.00 | 87.6 | 90.0 |
| XI | XI | Jaydee Canvot | DEF | 8 | 4.5 | 6.68 | 10.47 | 16.19 | 4.00 | 168.3 | 180.0 |
| Bench 3 | Bench | James Justin | DEF | 11 | 3.9 | 2.84 | 8.36 | 13.92 | 4.00 | 73.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 15.28 | 22.58 | 35.85 | 11.00 | 180.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.98 | 12.45 | 20.98 | 2.00 | 79.3 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.71 | 7.89 | 11.65 | 2.00 | 71.9 | 66.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 8.00 | 21.42 | 35.88 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Rayan Cherki | MID | 13 | 6.6 | 9.65 | 14.61 | 22.48 | 5.00 | 155.1 | 70.0 |
| XI | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 5.02 | 14.00 | 21.49 | 0.00 | 90.0 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.56 | 12.77 | 20.64 | 2.00 | 79.0 | 90.0 |
| Bench 2 | Autosub In | Elliot Anderson | MID | 16 | 5.6 | 3.55 | 10.01 | 16.49 | 12.00 | 67.2 | 90.0 |

## GW37

- Train rows: 189343
- Bank: 1.00 -> 1.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Erling Haaland
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 60.17
- Actual score: 85.00
- Transfer: Nico O'Reilly -> Marc Guéhi (projected gain 5.13, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.72 | 12.20 | 19.38 | 6.00 | 85.4 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.03 | 0.00 | 0.07 | 0.00 | 1.8 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 6.29 | 16.00 | 25.24 | 6.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.60 | 13.41 | 22.20 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jaydee Canvot | DEF | 8 | 4.5 | 4.16 | 11.46 | 17.89 | 3.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.93 | 11.37 | 18.91 | 14.00 | 84.3 | 90.0 |
| Bench 3 | Bench | James Justin | DEF | 11 | 3.9 | 2.74 | 7.68 | 13.19 | 6.00 | 63.0 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 6.65 | 19.95 | 33.63 | 9.00 | 86.2 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.08 | 13.97 | 22.99 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.46 | 6.88 | 10.57 | 11.00 | 57.1 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 7.15 | 20.60 | 33.58 | 9.00 | 90.0 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.6 | 3.24 | 11.01 | 18.24 | 1.00 | 52.2 | 34.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 3.66 | 10.67 | 18.23 | 12.00 | 71.3 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.55 | 10.60 | 17.87 | 12.00 | 79.5 | 90.0 |
| Bench 2 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.77 | 8.40 | 14.61 | 1.00 | 49.2 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 1.10 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 71.66
- Actual score: 40.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.94) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Rayan Cherki -> Dominik Szoboszlai (projected gain 3.25, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.94) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.1 | 4.34 | 12.00 | 18.99 | 0.00 | 84.0 | 0.0 |
| Bench 1 | Bench Boost | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.37 | 14.76 | 23.64 | 1.00 | 88.9 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 5.11 | 14.22 | 22.61 | 2.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.66 | 12.90 | 20.53 | 0.00 | 90.0 | 0.0 |
| XI | XI | James Justin | DEF | 11 | 3.9 | 3.49 | 9.69 | 15.35 | 1.00 | 78.8 | 90.0 |
| Bench 2 | Bench Boost | Jaydee Canvot | DEF | 8 | 4.5 | 3.25 | 9.38 | 14.83 | 0.00 | 84.8 | 0.0 |
| Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 7.47 | 20.97 | 34.58 | 0.00 | 90.0 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 4.11 | 12.14 | 19.91 | 2.00 | 81.7 | 90.0 |
| Bench 3 | Bench Boost | Mateus Mané | FWD | 20 | 4.2 | 3.12 | 8.30 | 13.07 | 2.00 | 68.4 | 90.0 |
| Vice Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 7.15 | 20.63 | 33.93 | 14.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.1 | 5.27 | 14.29 | 23.57 | 2.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.81 | 12.54 | 20.28 | 0.00 | 82.1 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.46 | 12.42 | 20.53 | 2.00 | 90.0 | 64.0 |
| Bench 4 | Bench Boost | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.56 | 7.69 | 14.00 | 0.00 | 55.1 | 0.0 |