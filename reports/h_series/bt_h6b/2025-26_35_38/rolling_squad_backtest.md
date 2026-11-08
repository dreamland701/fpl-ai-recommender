# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 277.23
- Total actual points: 266.00
- Average predicted points: 69.31
- Average actual points: 66.50
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
- Captain: Bruno Borges Fernandes
- Vice captain: Erling Haaland
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 57.61
- Actual score: 46.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.59 | 10.95 | 18.10 | 6.00 | 83.2 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.06 | 0.00 | 0.15 | 0.00 | 3.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.78 | 13.78 | 21.42 | 6.00 | 87.3 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 4.09 | 12.10 | 18.17 | 0.00 | 81.5 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 3.64 | 11.34 | 19.15 | 1.00 | 82.8 | 90.0 |
| Bench 2 | Bench | James Justin | DEF | 11 | 3.9 | 3.33 | 8.37 | 13.80 | 2.00 | 60.2 | 90.0 |
| Bench 4 | Bench | Maxime Estève | DEF | 3 | 3.9 | 2.09 | 6.28 | 10.66 | 3.00 | 57.3 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 6.31 | 18.57 | 30.22 | 7.00 | 77.4 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.36 | 13.08 | 21.95 | 6.00 | 80.2 | 90.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.3 | 2.69 | 7.16 | 11.07 | 2.00 | 63.9 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.31 | 19.13 | 31.98 | 5.00 | 88.6 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 5.01 | 14.67 | 23.58 | 4.00 | 80.4 | 20.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.51 | 13.02 | 19.91 | 4.00 | 87.9 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.21 | 12.78 | 20.66 | 1.00 | 78.2 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.48 | 12.49 | 19.76 | 1.00 | 83.7 | 45.0 |

## GW36

- Train rows: 188505
- Bank: 0.00 -> 1.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Rayan Cherki
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 95.34
- Actual score: 85.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (17.40) beats the best remaining Triple Captain opportunity (8.77).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Morgan Gibbs-White -> Rayan Cherki (projected gain 6.05, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (17.40) beats the best remaining Triple Captain opportunity (8.77).
- Autosub: Maxime Estève replaced Carlos Henrique Casimiro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.94 | 11.45 | 18.79 | 9.00 | 84.0 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 1.3 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.97 | 14.20 | 22.36 | 11.00 | 88.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.47 | 12.19 | 19.58 | 2.00 | 86.5 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 6.66 | 11.46 | 17.05 | 3.00 | 124.3 | 171.0 |
| Bench 2 | Autosub In | Maxime Estève | DEF | 3 | 3.9 | 3.07 | 8.52 | 13.64 | 3.00 | 80.5 | 90.0 |
| Bench 3 | Bench | James Justin | DEF | 11 | 3.9 | 2.78 | 8.24 | 13.83 | 4.00 | 71.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 14.30 | 21.82 | 34.35 | 11.00 | 179.7 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.64 | 11.60 | 19.69 | 2.00 | 74.8 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.66 | 7.83 | 11.64 | 2.00 | 70.4 | 66.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 7.02 | 20.05 | 32.77 | 3.00 | 90.1 | 90.0 |
| Vice Captain | XI | Rayan Cherki | MID | 13 | 6.6 | 9.10 | 14.54 | 21.54 | 5.00 | 144.7 | 70.0 |
| XI | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.83 | 13.25 | 20.15 | 0.00 | 87.5 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.31 | 12.56 | 20.50 | 2.00 | 77.0 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.52 | 9.65 | 16.35 | 12.00 | 66.5 | 90.0 |

## GW37

- Train rows: 189343
- Bank: 1.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Erling Haaland
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 57.16
- Actual score: 90.00
- Transfer: Maxime Estève -> Sven Botman (projected gain 2.92, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.92 | 12.99 | 20.72 | 6.00 | 86.0 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.02 | 0.00 | 0.01 | 0.00 | 1.4 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.94 | 15.37 | 24.37 | 6.00 | 87.9 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 4.22 | 11.64 | 18.03 | 6.00 | 88.5 | 90.0 |
| XI | XI | Sven Botman | DEF | 15 | 4.9 | 4.12 | 11.11 | 17.17 | 4.00 | 84.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.88 | 11.11 | 18.56 | 14.00 | 86.3 | 90.0 |
| Bench 3 | Bench | James Justin | DEF | 11 | 3.9 | 2.66 | 7.51 | 13.03 | 6.00 | 61.0 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 6.04 | 19.02 | 32.37 | 9.00 | 81.2 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.42 | 12.58 | 20.88 | 2.00 | 81.3 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.42 | 6.82 | 10.55 | 11.00 | 56.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.80 | 19.64 | 31.97 | 9.00 | 90.4 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 3.52 | 10.66 | 18.13 | 12.00 | 72.7 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.6 | 3.04 | 10.29 | 16.81 | 1.00 | 51.0 | 34.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.46 | 9.88 | 17.37 | 12.00 | 77.6 | 90.0 |
| Bench 2 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.73 | 8.34 | 14.52 | 1.00 | 48.4 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 67.12
- Actual score: 45.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.87) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Carlos Henrique Casimiro -> Pascal Groß (projected gain 1.99, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.87) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.1 | 4.49 | 12.53 | 20.09 | 0.00 | 84.4 | 0.0 |
| Bench 1 | Bench Boost | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.8 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.25 | 14.20 | 22.90 | 1.00 | 87.7 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.81 | 13.30 | 21.08 | 2.00 | 90.1 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 3.73 | 10.84 | 17.42 | 1.00 | 83.3 | 45.0 |
| XI | XI | Sven Botman | DEF | 15 | 4.9 | 3.86 | 10.82 | 17.14 | 3.00 | 85.3 | 90.0 |
| Bench 2 | Bench Boost | James Justin | DEF | 11 | 3.9 | 3.47 | 9.03 | 14.93 | 1.00 | 77.6 | 90.0 |
| Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 6.87 | 20.32 | 33.55 | 0.00 | 87.6 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 3.83 | 11.26 | 18.69 | 2.00 | 79.0 | 90.0 |
| Bench 4 | Bench Boost | Mateus Mané | FWD | 20 | 4.2 | 3.08 | 8.21 | 13.01 | 2.00 | 67.3 | 90.0 |
| Vice Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.53 | 19.06 | 31.75 | 14.00 | 87.9 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.50 | 11.27 | 18.81 | 0.00 | 81.1 | 0.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.6 | 3.67 | 10.96 | 18.01 | 2.00 | 78.8 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.83 | 10.95 | 18.47 | 2.00 | 86.9 | 64.0 |
| Bench 3 | Bench Boost | Rayan Cherki | MID | 13 | 6.5 | 3.32 | 9.79 | 15.90 | 1.00 | 49.9 | 32.0 |