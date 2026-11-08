# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 282.42
- Total actual points: 281.00
- Average predicted points: 70.61
- Average actual points: 70.25
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
- Predicted score: 58.90
- Actual score: 49.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.42 | 10.09 | 16.87 | 6.00 | 83.5 | 90.0 |
| Bench 1 | Bench | Remi Matthews | GK | 8 | 3.9 | 0.00 | 0.00 | 0.04 | 0.00 | 3.4 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.15 | 14.40 | 22.61 | 6.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 3.71 | 11.21 | 19.14 | 1.00 | 81.5 | 90.0 |
| XI | XI | Nikola Milenković | DEF | 16 | 5.1 | 3.96 | 10.96 | 17.28 | 1.00 | 86.1 | 45.0 |
| Bench 3 | Bench | Konstantinos Mavropanos | DEF | 19 | 4.5 | 3.03 | 8.91 | 15.62 | -1.00 | 68.6 | 90.0 |
| Bench 2 | Bench | James Justin | DEF | 11 | 3.9 | 3.18 | 8.41 | 13.83 | 2.00 | 59.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 6.55 | 18.64 | 30.49 | 7.00 | 76.3 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.60 | 13.19 | 22.07 | 6.00 | 77.5 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.3 | 2.59 | 6.73 | 10.26 | 2.00 | 59.0 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.41 | 19.06 | 32.08 | 5.00 | 90.0 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 5.06 | 14.27 | 23.18 | 4.00 | 79.9 | 20.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.61 | 13.07 | 20.35 | 4.00 | 90.0 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.53 | 12.61 | 20.04 | 1.00 | 85.0 | 45.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.35 | 12.57 | 20.72 | 1.00 | 80.0 | 90.0 |

## GW36

- Train rows: 188505
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Marc Guéhi
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 93.40
- Actual score: 97.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (17.84) beats the best remaining Triple Captain opportunity (9.04).
- Chip advisory: bench_boost (0.56): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.70): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Nikola Milenković -> Marc Guéhi (projected gain 4.25, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (17.84) beats the best remaining Triple Captain opportunity (9.04).
- Autosub: Konstantinos Mavropanos replaced Carlos Henrique Casimiro.
- Autosub: James Justin replaced Morgan Gibbs-White.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.76 | 10.99 | 18.04 | 9.00 | 85.7 | 90.0 |
| Bench 1 | Bench | Remi Matthews | GK | 8 | 3.9 | 0.00 | 0.96 | 1.21 | 0.00 | 4.9 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.25 | 14.80 | 23.36 | 11.00 | 90.0 | 90.0 |
| Vice Captain | XI | Marc Guéhi | DEF | 13 | 5.1 | 8.32 | 13.36 | 20.71 | 15.00 | 180.0 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.69 | 12.66 | 20.52 | 2.00 | 88.2 | 90.0 |
| Bench 2 | Autosub In | Konstantinos Mavropanos | DEF | 19 | 4.5 | 2.97 | 8.91 | 14.89 | 4.00 | 76.0 | 90.0 |
| Bench 3 | Autosub In | James Justin | DEF | 11 | 3.9 | 2.85 | 8.55 | 14.40 | 4.00 | 75.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 14.74 | 22.23 | 35.24 | 11.00 | 180.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.76 | 11.68 | 19.69 | 2.00 | 71.0 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.56 | 7.38 | 10.79 | 2.00 | 65.4 | 66.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 7.14 | 20.66 | 33.70 | 3.00 | 90.0 | 90.0 |
| XI | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.96 | 13.84 | 21.29 | 0.00 | 90.0 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.55 | 12.85 | 20.97 | 2.00 | 80.6 | 90.0 |
| XI | Bench | Morgan Gibbs-White | MID | 16 | 7.6 | 3.31 | 10.71 | 18.67 | 0.00 | 50.3 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.46 | 9.87 | 16.43 | 12.00 | 65.7 | 90.0 |

## GW37

- Train rows: 189343
- Bank: 0.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 59.32
- Actual score: 89.00
- Transfer: Morgan Gibbs-White -> Declan Rice (projected gain 4.19, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.73 | 12.34 | 19.76 | 6.00 | 87.7 | 90.0 |
| Bench 1 | Bench | Remi Matthews | GK | 8 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 1.1 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 6.29 | 15.98 | 25.32 | 6.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.61 | 13.54 | 22.54 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.00 | 11.64 | 19.39 | 14.00 | 88.2 | 90.0 |
| XI | XI | Konstantinos Mavropanos | DEF | 19 | 4.5 | 3.23 | 9.35 | 15.47 | 3.00 | 78.7 | 90.0 |
| Bench 3 | Bench | James Justin | DEF | 11 | 3.9 | 2.72 | 7.78 | 13.52 | 6.00 | 64.3 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.6 | 6.27 | 19.32 | 32.77 | 9.00 | 80.3 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.62 | 12.90 | 21.20 | 2.00 | 79.1 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.33 | 6.48 | 9.89 | 11.00 | 51.8 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.86 | 20.04 | 32.56 | 9.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 4.67 | 12.37 | 20.10 | 5.00 | 79.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 3.67 | 10.80 | 18.51 | 12.00 | 74.0 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.51 | 10.54 | 17.89 | 12.00 | 79.4 | 90.0 |
| Bench 2 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.74 | 8.34 | 14.49 | 1.00 | 48.3 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 0.30 -> 1.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 70.81
- Actual score: 46.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.94) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Igor Thiago Nascimento Rodrigues -> Richarlison de Andrade (projected gain 0.55, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.94) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.1 | 4.35 | 12.13 | 19.37 | 0.00 | 86.4 | 0.0 |
| Bench 1 | Bench Boost | Remi Matthews | GK | 8 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 1.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.32 | 14.65 | 23.58 | 1.00 | 88.1 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 5.12 | 14.33 | 22.93 | 2.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.68 | 13.04 | 20.90 | 0.00 | 90.0 | 0.0 |
| XI | XI | Konstantinos Mavropanos | DEF | 19 | 4.5 | 3.78 | 10.41 | 16.62 | 8.00 | 84.4 | 90.0 |
| Bench 2 | Bench Boost | James Justin | DEF | 11 | 3.9 | 3.51 | 9.82 | 15.66 | 1.00 | 80.7 | 90.0 |
| Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 7.33 | 21.05 | 34.95 | 0.00 | 90.0 | 0.0 |
| XI | XI | Richarlison de Andrade | FWD | 18 | 6.5 | 4.57 | 12.05 | 18.35 | 2.00 | 78.3 | 72.0 |
| Bench 3 | Bench Boost | Mateus Mané | FWD | 20 | 4.2 | 2.99 | 7.81 | 12.25 | 2.00 | 62.4 | 90.0 |
| Vice Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.75 | 19.97 | 32.91 | 14.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 4.53 | 13.03 | 20.80 | 0.00 | 82.4 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.99 | 12.59 | 20.72 | 0.00 | 88.0 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.11 | 12.03 | 19.96 | 2.00 | 90.0 | 64.0 |
| Bench 4 | Bench Boost | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.44 | 7.39 | 13.59 | 0.00 | 51.6 | 0.0 |