# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 284.87
- Total actual points: 282.00
- Average predicted points: 71.22
- Average actual points: 70.50
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
- Predicted score: 59.48
- Actual score: 49.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.48 | 10.22 | 16.99 | 6.00 | 85.2 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.18 | 14.46 | 22.63 | 6.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 3.79 | 11.36 | 19.26 | 1.00 | 83.7 | 90.0 |
| XI | XI | Nikola Milenković | DEF | 16 | 5.1 | 4.04 | 11.09 | 17.40 | 1.00 | 87.9 | 45.0 |
| Bench 3 | Bench | Konstantinos Mavropanos | DEF | 19 | 4.5 | 3.11 | 9.06 | 15.75 | -1.00 | 70.9 | 90.0 |
| Bench 2 | Bench | James Justin | DEF | 11 | 3.9 | 3.18 | 8.39 | 13.85 | 2.00 | 59.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 6.58 | 18.68 | 30.48 | 7.00 | 77.1 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.64 | 13.23 | 22.07 | 6.00 | 78.4 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.3 | 2.66 | 6.86 | 10.37 | 2.00 | 61.1 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.43 | 19.10 | 32.10 | 5.00 | 90.0 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 5.12 | 14.37 | 23.26 | 4.00 | 81.3 | 20.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.65 | 13.11 | 20.35 | 4.00 | 90.0 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.58 | 12.71 | 20.12 | 1.00 | 86.4 | 45.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.40 | 12.67 | 20.79 | 1.00 | 81.4 | 90.0 |

## GW36

- Train rows: 188505
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Marc Guéhi
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 93.86
- Actual score: 97.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (17.49) beats the best remaining Triple Captain opportunity (9.04).
- Chip advisory: triple_captain (0.70): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Nikola Milenković -> Marc Guéhi (projected gain 4.14, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (17.49) beats the best remaining Triple Captain opportunity (9.04).
- Autosub: Konstantinos Mavropanos replaced Carlos Henrique Casimiro.
- Autosub: James Justin replaced Morgan Gibbs-White.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.81 | 11.08 | 18.12 | 9.00 | 86.8 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.29 | 14.86 | 23.39 | 11.00 | 90.0 | 90.0 |
| Vice Captain | XI | Marc Guéhi | DEF | 13 | 5.1 | 8.44 | 13.46 | 20.79 | 15.00 | 180.0 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.77 | 12.81 | 20.67 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Autosub In | Konstantinos Mavropanos | DEF | 19 | 4.5 | 3.03 | 9.02 | 15.00 | 4.00 | 77.6 | 90.0 |
| Bench 3 | Autosub In | James Justin | DEF | 11 | 3.9 | 2.91 | 8.66 | 14.49 | 4.00 | 76.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 14.74 | 22.22 | 35.20 | 11.00 | 180.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.80 | 11.74 | 19.73 | 2.00 | 72.2 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.60 | 7.46 | 10.86 | 2.00 | 66.8 | 66.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 7.16 | 20.71 | 33.73 | 3.00 | 90.0 | 90.0 |
| XI | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 5.01 | 13.91 | 21.33 | 0.00 | 90.0 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.61 | 12.97 | 21.08 | 2.00 | 82.2 | 90.0 |
| XI | Bench | Morgan Gibbs-White | MID | 16 | 7.6 | 3.20 | 10.95 | 19.39 | 0.00 | 47.4 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.57 | 10.06 | 16.61 | 12.00 | 68.6 | 90.0 |

## GW37

- Train rows: 189343
- Bank: 0.10 -> 0.40
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Erling Haaland
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 59.56
- Actual score: 89.00
- Transfer: Morgan Gibbs-White -> Declan Rice (projected gain 4.54, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.80 | 12.45 | 19.88 | 6.00 | 89.1 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.02 | 0.00 | 0.00 | 0.00 | 1.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 6.32 | 16.03 | 25.33 | 6.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.65 | 13.61 | 22.61 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.97 | 11.60 | 19.38 | 14.00 | 87.4 | 90.0 |
| XI | XI | Konstantinos Mavropanos | DEF | 19 | 4.5 | 3.28 | 9.45 | 15.56 | 3.00 | 80.0 | 90.0 |
| Bench 2 | Bench | James Justin | DEF | 11 | 3.9 | 2.82 | 7.97 | 13.72 | 6.00 | 66.7 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 6.34 | 19.43 | 32.88 | 9.00 | 81.8 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.64 | 12.92 | 21.20 | 2.00 | 79.7 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.35 | 6.50 | 9.89 | 11.00 | 52.5 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.80 | 19.92 | 32.46 | 9.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 4.72 | 12.46 | 20.18 | 5.00 | 80.3 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 3.67 | 10.81 | 18.56 | 12.00 | 74.0 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.58 | 10.69 | 18.04 | 12.00 | 81.4 | 90.0 |
| Bench 3 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.75 | 8.34 | 14.52 | 1.00 | 48.8 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 0.40 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 71.96
- Actual score: 47.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.38) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Carlos Henrique Casimiro -> Bernardo Mota Veiga de Carvalho e Silva (projected gain 0.82, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.38) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.1 | 4.41 | 12.23 | 19.46 | 0.00 | 87.6 | 0.0 |
| Bench 1 | Bench Boost | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.37 | 14.73 | 23.64 | 1.00 | 89.3 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 5.18 | 14.44 | 23.02 | 2.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.71 | 13.10 | 20.93 | 0.00 | 90.0 | 0.0 |
| Bench 2 | Bench Boost | Konstantinos Mavropanos | DEF | 19 | 4.5 | 3.82 | 10.48 | 16.67 | 8.00 | 85.3 | 90.0 |
| Bench 3 | Bench Boost | James Justin | DEF | 11 | 3.9 | 3.56 | 9.93 | 15.75 | 1.00 | 82.0 | 90.0 |
| Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 7.35 | 21.09 | 34.96 | 0.00 | 90.0 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 3.97 | 11.53 | 18.82 | 2.00 | 75.6 | 90.0 |
| Bench 4 | Bench Boost | Mateus Mané | FWD | 20 | 4.2 | 3.00 | 7.83 | 12.23 | 2.00 | 62.9 | 90.0 |
| Vice Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.76 | 20.00 | 32.92 | 14.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 4.37 | 12.78 | 20.50 | 0.00 | 76.8 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 4.07 | 12.75 | 20.87 | 0.00 | 90.0 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.15 | 12.12 | 20.04 | 2.00 | 90.0 | 64.0 |
| XI | XI | Bernardo Mota Veiga de Carvalho e Silva | MID | 13 | 6.2 | 3.89 | 11.22 | 17.73 | 1.00 | 72.2 | 58.0 |