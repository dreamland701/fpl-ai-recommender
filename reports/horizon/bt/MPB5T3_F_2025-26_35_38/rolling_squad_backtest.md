# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 286.47
- Total actual points: 246.00
- Average predicted points: 71.62
- Average actual points: 61.50
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
- Predicted score: 58.21
- Actual score: 48.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Dean Henderson | GK | 8 | 5.1 | 2.73 | 10.86 | 16.55 | 2.00 | 73.8 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.06 | 0.05 | 0.10 | 0.00 | 3.2 | 0.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 3.88 | 15.02 | 21.26 | 0.00 | 80.2 | 45.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.15 | 15.01 | 23.54 | 6.00 | 90.0 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 3.91 | 14.97 | 21.96 | 1.00 | 59.4 | 90.0 |
| Bench 3 | Bench | Jaydee Canvot | DEF | 8 | 4.5 | 3.46 | 13.63 | 19.74 | 0.00 | 80.4 | 90.0 |
| Bench 4 | Bench | Konstantinos Mavropanos | DEF | 19 | 4.5 | 3.02 | 9.13 | 15.80 | -1.00 | 68.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 6.57 | 25.81 | 39.67 | 7.00 | 76.7 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.71 | 13.83 | 23.09 | 6.00 | 83.1 | 90.0 |
| Bench 2 | Bench | Igor Jesus Maciel da Cruz | FWD | 16 | 5.9 | 3.64 | 10.36 | 16.76 | 5.00 | 64.4 | 45.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.42 | 19.39 | 32.62 | 5.00 | 90.0 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.5 | 4.08 | 15.30 | 22.91 | 5.00 | 56.9 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 5.05 | 14.52 | 23.58 | 4.00 | 79.3 | 20.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.63 | 13.64 | 21.13 | 4.00 | 90.0 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.51 | 12.68 | 20.30 | 1.00 | 84.1 | 45.0 |

## GW36

- Train rows: 188505
- Bank: 0.10 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Rayan Cherki
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 104.50
- Actual score: 83.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (18.88) beats the best remaining Triple Captain opportunity (9.04).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Daniel Muñoz Mejía -> Maxence Lacroix (projected gain 4.80, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (18.88) beats the best remaining Triple Captain opportunity (9.04).
- Autosub: Igor Jesus Maciel da Cruz replaced Carlos Henrique Casimiro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Dean Henderson | GK | 8 | 5.1 | 5.04 | 9.93 | 15.87 | 3.00 | 143.6 | 180.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 1.3 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.25 | 15.16 | 24.10 | 11.00 | 90.0 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 7.81 | 14.82 | 22.70 | 5.00 | 143.7 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.2 | 7.30 | 13.61 | 20.95 | 4.00 | 150.7 | 180.0 |
| XI | XI | Jaydee Canvot | DEF | 8 | 4.5 | 6.38 | 12.73 | 19.57 | 4.00 | 155.7 | 180.0 |
| Bench 4 | Bench | Konstantinos Mavropanos | DEF | 19 | 4.5 | 2.95 | 8.90 | 14.69 | 4.00 | 75.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 14.73 | 28.10 | 45.58 | 11.00 | 180.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.87 | 12.44 | 21.03 | 2.00 | 77.1 | 90.0 |
| Bench 3 | Autosub In | Igor Jesus Maciel da Cruz | FWD | 16 | 5.9 | 3.07 | 9.10 | 15.04 | 1.00 | 55.0 | 82.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 7.16 | 20.84 | 34.28 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Rayan Cherki | MID | 13 | 6.5 | 9.09 | 16.76 | 26.18 | 5.00 | 142.8 | 70.0 |
| XI | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.98 | 14.34 | 22.24 | 0.00 | 90.0 | 0.0 |
| Bench 2 | Bench | Morgan Gibbs-White | MID | 16 | 7.6 | 3.31 | 11.05 | 19.00 | 0.00 | 50.3 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.44 | 9.94 | 16.47 | 12.00 | 64.4 | 90.0 |

## GW37

- Train rows: 189343
- Bank: 0.70 -> 0.80
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 57.31
- Actual score: 58.00
- Transfer: Nico O'Reilly -> Marc Guéhi (projected gain 13.68, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Dean Henderson | GK | 8 | 5.1 | 3.25 | 9.01 | 13.85 | 0.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.02 | 0.00 | 0.00 | 0.00 | 1.4 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 6.28 | 16.27 | 25.95 | 6.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.58 | 13.23 | 21.92 | 2.00 | 90.0 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.2 | 4.43 | 12.06 | 18.13 | 2.00 | 90.0 | 60.0 |
| XI | XI | Jaydee Canvot | DEF | 8 | 4.5 | 4.18 | 11.38 | 17.50 | 3.00 | 90.0 | 90.0 |
| XI | XI | Konstantinos Mavropanos | DEF | 19 | 4.5 | 3.21 | 9.28 | 15.21 | 3.00 | 78.1 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.6 | 6.28 | 19.47 | 32.98 | 9.00 | 80.1 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.71 | 13.20 | 21.87 | 2.00 | 84.3 | 90.0 |
| Bench 2 | Bench | Igor Jesus Maciel da Cruz | FWD | 16 | 5.9 | 2.95 | 9.24 | 15.25 | 2.00 | 61.7 | 83.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.89 | 20.36 | 33.30 | 9.00 | 90.0 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.48 | 10.59 | 17.83 | 12.00 | 77.8 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.5 | 3.13 | 10.29 | 17.11 | 1.00 | 49.5 | 34.0 |
| Bench 4 | Bench | Morgan Gibbs-White | MID | 16 | 7.5 | 2.17 | 8.62 | 15.49 | 7.00 | 36.7 | 90.0 |
| Bench 3 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.73 | 8.61 | 14.95 | 1.00 | 48.4 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 0.80 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 66.45
- Actual score: 57.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.84) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Jaydee Canvot -> Marcos Senesi Barón (projected gain 9.89, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.84) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Dean Henderson | GK | 8 | 5.1 | 2.36 | 6.99 | 11.10 | 2.00 | 79.4 | 90.0 |
| Bench 1 | Bench Boost | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.8 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.33 | 14.88 | 24.21 | 1.00 | 88.1 | 45.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.65 | 12.99 | 20.76 | 0.00 | 90.0 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.2 | 4.34 | 12.82 | 20.79 | 2.00 | 90.0 | 90.0 |
| XI | XI | Konstantinos Mavropanos | DEF | 19 | 4.5 | 3.77 | 10.43 | 16.63 | 8.00 | 84.1 | 90.0 |
| Bench 2 | Bench Boost | Maxence Lacroix | DEF | 8 | 5.2 | 3.33 | 10.12 | 15.86 | 0.00 | 76.4 | 0.0 |
| Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 7.35 | 21.64 | 35.84 | 0.00 | 90.0 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 4.04 | 12.17 | 20.17 | 2.00 | 80.5 | 90.0 |
| Bench 3 | Bench Boost | Igor Jesus Maciel da Cruz | FWD | 16 | 5.9 | 3.06 | 8.90 | 14.53 | 2.00 | 64.7 | 90.0 |
| Vice Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.78 | 20.21 | 33.48 | 14.00 | 90.0 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 4.21 | 12.55 | 20.84 | 9.00 | 76.8 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.08 | 12.15 | 19.77 | 2.00 | 90.0 | 64.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.5 | 3.35 | 9.97 | 16.41 | 1.00 | 49.5 | 32.0 |
| Bench 4 | Bench Boost | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.46 | 7.61 | 13.74 | 0.00 | 52.5 | 0.0 |