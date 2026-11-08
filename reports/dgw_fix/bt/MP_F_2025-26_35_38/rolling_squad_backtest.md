# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 289.74
- Total actual points: 250.00
- Average predicted points: 72.44
- Average actual points: 62.50
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
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 57.63
- Actual score: 48.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Dean Henderson | GK | 8 | 5.1 | 2.82 | 11.18 | 17.07 | 2.00 | 75.8 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 1.4 | 0.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 3.93 | 15.20 | 21.54 | 0.00 | 81.2 | 45.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.12 | 14.96 | 23.49 | 6.00 | 90.0 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 3.84 | 14.74 | 21.64 | 1.00 | 57.8 | 90.0 |
| Bench 3 | Bench | Jaydee Canvot | DEF | 8 | 4.5 | 3.48 | 13.70 | 19.87 | 0.00 | 80.8 | 90.0 |
| Bench 4 | Bench | Konstantinos Mavropanos | DEF | 19 | 4.5 | 2.94 | 8.93 | 15.49 | -1.00 | 67.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 6.44 | 25.40 | 39.12 | 7.00 | 74.1 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.71 | 13.85 | 23.12 | 6.00 | 83.1 | 90.0 |
| Bench 2 | Bench | Igor Jesus Maciel da Cruz | FWD | 16 | 5.9 | 3.58 | 10.21 | 16.52 | 5.00 | 63.1 | 45.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.41 | 19.37 | 32.60 | 5.00 | 90.0 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.5 | 4.11 | 15.42 | 23.13 | 5.00 | 57.5 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 4.91 | 14.16 | 23.02 | 4.00 | 76.5 | 20.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.43 | 13.14 | 20.35 | 4.00 | 90.0 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.46 | 12.55 | 20.10 | 1.00 | 83.0 | 45.0 |

## GW36

- Train rows: 188505
- Bank: 0.10 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Rayan Cherki
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 105.66
- Actual score: 83.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (19.01) beats the best remaining Triple Captain opportunity (9.12).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Morgan Gibbs-White -> Dominik Szoboszlai (projected gain 3.79, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (19.01) beats the best remaining Triple Captain opportunity (9.12).
- Autosub: Elliot Anderson replaced Carlos Henrique Casimiro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Dean Henderson | GK | 8 | 5.1 | 5.23 | 10.25 | 16.33 | 3.00 | 147.5 | 180.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.26 | 15.20 | 24.20 | 11.00 | 90.0 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 7.87 | 14.93 | 22.87 | 5.00 | 145.0 | 90.0 |
| XI | XI | Jaydee Canvot | DEF | 8 | 4.5 | 6.38 | 12.72 | 19.56 | 4.00 | 155.7 | 180.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 6.24 | 12.08 | 18.41 | 3.00 | 118.8 | 171.0 |
| Bench 4 | Bench | Konstantinos Mavropanos | DEF | 19 | 4.5 | 2.94 | 8.87 | 14.64 | 4.00 | 75.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 14.86 | 28.32 | 45.92 | 11.00 | 180.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.85 | 12.37 | 20.94 | 2.00 | 76.6 | 90.0 |
| Bench 3 | Bench | Igor Jesus Maciel da Cruz | FWD | 16 | 5.9 | 3.04 | 9.01 | 14.90 | 1.00 | 54.3 | 82.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 7.17 | 20.87 | 34.34 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Rayan Cherki | MID | 13 | 6.5 | 9.33 | 17.16 | 26.78 | 5.00 | 147.7 | 70.0 |
| XI | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.82 | 13.94 | 21.66 | 0.00 | 90.0 | 0.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.94 | 13.52 | 22.16 | 2.00 | 85.1 | 90.0 |
| Bench 2 | Autosub In | Elliot Anderson | MID | 16 | 5.6 | 3.37 | 9.76 | 16.19 | 12.00 | 63.0 | 90.0 |

## GW37

- Train rows: 189343
- Bank: 0.70 -> 0.80
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Erling Haaland
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 58.66
- Actual score: 68.00
- Transfer: Nico O'Reilly -> Marc Guéhi (projected gain 4.46, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Dean Henderson | GK | 8 | 5.1 | 3.45 | 9.51 | 14.59 | 0.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 6.27 | 16.25 | 25.93 | 6.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.74 | 13.65 | 22.56 | 2.00 | 90.0 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 4.31 | 11.68 | 17.56 | 6.00 | 90.0 | 90.0 |
| XI | XI | Jaydee Canvot | DEF | 8 | 4.5 | 4.30 | 11.68 | 17.95 | 3.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Konstantinos Mavropanos | DEF | 19 | 4.5 | 3.19 | 9.24 | 15.14 | 3.00 | 77.7 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 6.31 | 19.54 | 33.09 | 9.00 | 80.8 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.68 | 13.13 | 21.76 | 2.00 | 83.9 | 90.0 |
| Bench 3 | Bench | Igor Jesus Maciel da Cruz | FWD | 16 | 5.9 | 2.94 | 9.22 | 15.22 | 2.00 | 61.6 | 83.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.89 | 20.34 | 33.29 | 9.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.10 | 12.02 | 20.03 | 9.00 | 79.8 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.5 | 3.25 | 10.57 | 17.52 | 1.00 | 52.0 | 34.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.46 | 10.55 | 17.78 | 12.00 | 77.5 | 90.0 |
| Bench 4 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.47 | 7.94 | 13.92 | 1.00 | 43.1 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 0.80 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 67.79
- Actual score: 51.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.94) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Jaydee Canvot -> Marcos Senesi Barón (projected gain 2.93, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.94) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Dean Henderson | GK | 8 | 5.1 | 2.46 | 7.25 | 11.47 | 2.00 | 81.4 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.35 | 14.95 | 24.31 | 1.00 | 88.5 | 45.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.70 | 13.15 | 21.01 | 0.00 | 90.0 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.2 | 4.41 | 13.01 | 21.09 | 2.00 | 90.0 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 3.63 | 10.53 | 16.63 | 1.00 | 84.0 | 45.0 |
| XI | XI | Konstantinos Mavropanos | DEF | 19 | 4.5 | 3.76 | 10.39 | 16.57 | 8.00 | 83.8 | 90.0 |
| Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 7.37 | 21.68 | 35.89 | 0.00 | 90.0 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 4.04 | 12.17 | 20.18 | 2.00 | 80.5 | 90.0 |
| Bench 3 | Bench Boost | Igor Jesus Maciel da Cruz | FWD | 16 | 5.9 | 3.09 | 8.99 | 14.66 | 2.00 | 65.4 | 90.0 |
| Vice Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.83 | 20.33 | 33.68 | 14.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.87 | 13.67 | 22.55 | 2.00 | 90.0 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.05 | 12.10 | 19.70 | 2.00 | 90.0 | 64.0 |
| Bench 2 | Bench Boost | Rayan Cherki | MID | 13 | 6.5 | 3.43 | 10.17 | 16.70 | 1.00 | 51.1 | 32.0 |
| Bench 4 | Bench Boost | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.42 | 7.52 | 13.61 | 0.00 | 51.8 | 0.0 |