# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 282.82
- Total actual points: 238.00
- Average predicted points: 70.71
- Average actual points: 59.50
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
- Bank: 100.00 -> 0.30
- Free transfers: 1 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 60.31
- Actual score: 50.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Caoimhín Kelleher | GK | 5 | 4.8 | 4.39 | 14.50 | 22.47 | 8.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.49 | 15.80 | 24.72 | 6.00 | 90.0 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 4.52 | 12.95 | 19.62 | 1.00 | 70.0 | 90.0 |
| XI | XI | Nikola Milenković | DEF | 16 | 5.1 | 4.18 | 11.73 | 18.40 | 1.00 | 84.1 | 45.0 |
| Bench 3 | Bench | Chris Richards | DEF | 8 | 4.4 | 3.53 | 10.76 | 15.98 | 1.00 | 81.7 | 14.0 |
| Bench 4 | Bench | Marc Guéhi | DEF | 13 | 5.1 | 3.53 | 10.13 | 16.17 | 4.00 | 65.0 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.6 | 5.34 | 15.72 | 25.79 | 7.00 | 68.7 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.8 | 4.29 | 14.87 | 25.75 | 2.00 | 80.1 | 87.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 5.15 | 14.30 | 21.04 | 6.00 | 83.7 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.45 | 18.86 | 31.86 | 5.00 | 90.0 | 90.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.56 | 13.27 | 20.90 | 4.00 | 90.0 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 4.94 | 13.11 | 21.58 | 4.00 | 80.0 | 20.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.53 | 12.32 | 19.30 | 1.00 | 83.3 | 45.0 |
| Bench 2 | Bench | Mathias Jensen | MID | 5 | 4.9 | 3.96 | 10.56 | 17.21 | 3.00 | 87.2 | 90.0 |

## GW36

- Train rows: 188505
- Bank: 0.30 -> 0.90
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Marc Guéhi
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 94.95
- Actual score: 84.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (16.15) beats the best remaining Triple Captain opportunity (8.88).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Morgan Gibbs-White -> Dominik Szoboszlai (projected gain 2.70, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (16.15) beats the best remaining Triple Captain opportunity (8.88).
- Autosub: Mathias Jensen replaced Carlos Henrique Casimiro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Caoimhín Kelleher | GK | 5 | 4.8 | 2.77 | 8.47 | 13.98 | 3.00 | 79.6 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.78 | 16.87 | 26.49 | 11.00 | 90.0 | 90.0 |
| Vice Captain | XI | Marc Guéhi | DEF | 13 | 5.1 | 8.94 | 13.97 | 20.93 | 15.00 | 180.0 | 180.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 8.75 | 13.96 | 20.54 | 5.00 | 150.4 | 90.0 |
| Bench 4 | Bench | Nikola Milenković | DEF | 16 | 5.1 | 3.29 | 9.58 | 15.63 | 2.00 | 67.3 | 90.0 |
| XI | XI | Chris Richards | DEF | 8 | 4.4 | 4.30 | 8.43 | 13.05 | 4.00 | 106.4 | 180.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 12.70 | 20.29 | 32.60 | 11.00 | 180.0 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 4.93 | 13.02 | 18.82 | 2.00 | 82.6 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.24 | 11.93 | 17.92 | 2.00 | 75.6 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 7.23 | 21.13 | 34.17 | 3.00 | 90.0 | 90.0 |
| XI | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 5.03 | 13.71 | 21.65 | 0.00 | 90.0 | 0.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.88 | 13.45 | 21.43 | 2.00 | 87.2 | 90.0 |
| Bench 2 | Autosub In | Mathias Jensen | MID | 5 | 4.9 | 3.56 | 10.79 | 17.38 | 4.00 | 85.4 | 90.0 |
| Bench 3 | Bench | Elliot Anderson | MID | 16 | 5.6 | 3.36 | 9.32 | 15.02 | 12.00 | 68.2 | 90.0 |

## GW37

- Train rows: 189343
- Bank: 0.90 -> 0.90
- Free transfers: 2 -> 2
- Captain: Gabriel dos Santos Magalhães
- Vice captain: Bruno Borges Fernandes
- Effective captain: Gabriel dos Santos Magalhães
- Chip used: none
- Predicted score: 60.45
- Actual score: 51.00
- Transfer: Nico O'Reilly -> Maxence Lacroix (projected gain 2.46, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Caoimhín Kelleher | GK | 5 | 4.8 | 3.30 | 9.56 | 15.98 | 2.00 | 87.2 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 7.05 | 18.20 | 28.60 | 6.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.59 | 13.45 | 21.87 | 2.00 | 90.0 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.2 | 4.33 | 12.82 | 19.45 | 2.00 | 90.0 | 60.0 |
| XI | XI | Chris Richards | DEF | 8 | 4.4 | 4.15 | 11.83 | 18.43 | 0.00 | 90.0 | 29.0 |
| Bench 2 | Bench | Nikola Milenković | DEF | 16 | 5.1 | 3.35 | 10.40 | 16.90 | 1.00 | 84.4 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.6 | 5.68 | 17.33 | 30.43 | 9.00 | 81.0 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 5.00 | 13.69 | 21.28 | 2.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.26 | 11.81 | 20.52 | 2.00 | 87.4 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.80 | 20.03 | 32.58 | 9.00 | 90.0 | 90.0 |
| XI | XI | Mathias Jensen | MID | 5 | 4.9 | 4.14 | 11.92 | 19.12 | 2.00 | 86.5 | 62.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.11 | 11.81 | 19.64 | 9.00 | 82.6 | 90.0 |
| Bench 3 | Bench | Elliot Anderson | MID | 16 | 5.6 | 3.35 | 10.19 | 17.07 | 12.00 | 75.7 | 90.0 |
| Bench 4 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.69 | 8.41 | 14.53 | 1.00 | 50.1 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 0.90 -> 0.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Erling Haaland
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 67.11
- Actual score: 53.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.66) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Caoimhín Kelleher -> Gianluigi Donnarumma (projected gain 5.83, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.66) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Gianluigi Donnarumma | GK | 13 | 5.6 | 4.36 | 14.49 | 24.53 | 0.00 | 90.0 | 0.0 |
| Bench 1 | Bench Boost | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.94 | 17.07 | 26.85 | 1.00 | 90.0 | 45.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.78 | 13.17 | 20.81 | 0.00 | 90.0 | 0.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.2 | 3.59 | 10.86 | 17.05 | 0.00 | 79.5 | 0.0 |
| Bench 2 | Bench Boost | Nikola Milenković | DEF | 16 | 5.1 | 2.99 | 8.66 | 14.99 | 4.00 | 74.7 | 90.0 |
| Bench 4 | Bench Boost | Chris Richards | DEF | 8 | 4.4 | 2.25 | 7.11 | 11.91 | 0.00 | 59.0 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 6.59 | 19.17 | 32.59 | 0.00 | 90.0 | 0.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.8 | 5.19 | 14.01 | 23.24 | 12.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 3.44 | 10.14 | 17.29 | 2.00 | 80.1 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.89 | 20.60 | 33.66 | 14.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.79 | 13.54 | 22.32 | 2.00 | 89.6 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.85 | 11.69 | 19.21 | 2.00 | 90.0 | 64.0 |
| XI | XI | Mathias Jensen | MID | 5 | 4.9 | 3.13 | 9.54 | 15.34 | 2.00 | 75.2 | 82.0 |
| Bench 3 | Bench Boost | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.42 | 7.29 | 13.47 | 0.00 | 52.6 | 0.0 |