# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 214.42
- Total actual points: 260.00
- Average predicted points: 53.60
- Average actual points: 65.00
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
- Bank: 100.00 -> 0.40
- Free transfers: 1 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 49.23
- Actual score: 41.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.47 | 11.33 | 17.56 | 6.00 | 89.0 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 5.6 | 2.45 | 8.28 | 13.35 | 1.00 | 83.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 3.89 | 12.79 | 20.25 | 1.00 | 92.4 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 4.37 | 12.21 | 18.70 | 6.00 | 94.1 | 90.0 |
| XI | XI | Konstantinos Mavropanos | DEF | 19 | 4.5 | 3.42 | 10.79 | 17.40 | -1.00 | 84.8 | 90.0 |
| Bench 2 | Bench | Nico O'Reilly | DEF | 13 | 5.1 | 3.31 | 10.72 | 16.84 | 1.00 | 71.9 | 90.0 |
| Bench 3 | Bench | Marc Guéhi | DEF | 13 | 5.1 | 3.23 | 10.41 | 16.63 | 4.00 | 78.8 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.06 | 12.48 | 20.17 | 6.00 | 85.6 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 3.91 | 12.30 | 19.62 | 2.00 | 88.0 | 87.0 |
| Bench 4 | Bench | Igor Jesus Maciel da Cruz | FWD | 16 | 5.8 | 3.15 | 9.71 | 15.16 | 5.00 | 76.7 | 45.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.3 | 5.30 | 16.21 | 27.06 | 5.00 | 97.7 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.5 | 4.06 | 12.90 | 20.97 | 4.00 | 88.0 | 20.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.2 | 3.75 | 12.47 | 20.75 | 2.00 | 74.2 | 74.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 3.68 | 12.09 | 18.72 | 1.00 | 82.7 | 90.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.7 | 4.03 | 11.66 | 18.06 | 4.00 | 96.9 | 90.0 |

## GW36

- Train rows: 188505
- Bank: 0.40 -> 2.40
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Marc Guéhi
- Effective captain: Antoine Semenyo
- Chip used: bench_boost
- Predicted score: 63.13
- Actual score: 87.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (15.65) beats the best remaining Bench Boost opportunity (12.01).
- Chip advisory: bench_boost (0.56): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Transfer: Virgil van Dijk -> James Hill (projected gain 0.43, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (15.65) beats the best remaining Bench Boost opportunity (12.01).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.38 | 10.23 | 16.88 | 9.00 | 89.2 | 90.0 |
| Bench 1 | Bench Boost | Jordan Pickford | GK | 9 | 5.6 | 2.58 | 7.57 | 12.72 | 3.00 | 83.5 | 90.0 |
| Vice Captain | XI | Marc Guéhi | DEF | 13 | 5.1 | 5.00 | 12.72 | 19.85 | 15.00 | 142.3 | 180.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.40 | 12.55 | 19.97 | 11.00 | 96.2 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 4.46 | 10.76 | 16.45 | 5.00 | 124.3 | 90.0 |
| Bench 2 | Bench Boost | James Hill | DEF | 4 | 4.2 | 3.13 | 9.14 | 15.41 | 6.00 | 85.1 | 90.0 |
| Bench 3 | Bench Boost | Konstantinos Mavropanos | DEF | 19 | 4.5 | 2.97 | 8.71 | 14.77 | 4.00 | 84.9 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.8 | 4.00 | 12.05 | 20.48 | 2.00 | 86.9 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 3.31 | 10.80 | 17.93 | 2.00 | 66.0 | 90.0 |
| Bench 4 | Bench Boost | Igor Jesus Maciel da Cruz | FWD | 16 | 5.9 | 2.75 | 7.93 | 13.13 | 1.00 | 51.9 | 82.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 4.96 | 16.72 | 28.18 | 3.00 | 83.9 | 90.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.2 | 5.16 | 12.73 | 20.30 | 12.00 | 126.0 | 180.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.16 | 12.39 | 19.53 | 0.00 | 91.9 | 0.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 3.70 | 12.06 | 20.45 | 0.00 | 77.2 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 3.99 | 11.95 | 19.66 | 2.00 | 83.8 | 90.0 |

## GW37

- Train rows: 189343
- Bank: 2.40 -> 3.00
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 49.14
- Actual score: 63.00
- Transfer: Morgan Gibbs-White -> Dominik Szoboszlai (projected gain 1.89, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.1 | 3.27 | 8.85 | 14.35 | 6.00 | 89.5 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 5.6 | 2.83 | 7.85 | 12.76 | 1.00 | 85.6 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.94 | 12.82 | 20.71 | 6.00 | 94.4 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.10 | 12.01 | 20.04 | 2.00 | 109.6 | 90.0 |
| XI | XI | Konstantinos Mavropanos | DEF | 19 | 4.5 | 3.11 | 9.45 | 15.59 | 3.00 | 86.9 | 90.0 |
| Bench 3 | Bench | Nico O'Reilly | DEF | 13 | 5.3 | 2.79 | 8.66 | 14.79 | 2.00 | 71.9 | 90.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.2 | 2.90 | 8.63 | 14.05 | 1.00 | 78.5 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.95 | 11.84 | 19.94 | 2.00 | 84.6 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 3.40 | 10.25 | 17.27 | 2.00 | 83.1 | 90.0 |
| XI | XI | Igor Jesus Maciel da Cruz | FWD | 16 | 5.9 | 3.04 | 9.21 | 15.03 | 2.00 | 77.2 | 83.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 5.85 | 16.62 | 27.08 | 9.00 | 102.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 4.87 | 13.67 | 22.16 | 1.00 | 108.3 | 55.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 3.47 | 10.47 | 17.54 | 9.00 | 85.3 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 3.30 | 9.30 | 15.45 | 12.00 | 80.7 | 90.0 |
| Bench 4 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.65 | 7.66 | 13.16 | 1.00 | 62.0 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 3.00 -> 1.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 52.91
- Actual score: 69.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.46) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: James Hill -> Virgil van Dijk (projected gain 3.11, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (5.46) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Jordan Pickford replaced David Raya Martín.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martín | GK | 1 | 6.1 | 3.04 | 9.17 | 14.95 | 0.00 | 88.9 | 0.0 |
| Bench 1 | Autosub In | Jordan Pickford | GK | 9 | 5.6 | 2.51 | 7.48 | 11.95 | 2.00 | 83.9 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.3 | 4.19 | 12.36 | 20.45 | 1.00 | 92.3 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.95 | 11.23 | 18.44 | 2.00 | 96.9 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 13 | 5.1 | 3.59 | 11.04 | 18.14 | 0.00 | 94.4 | 0.0 |
| XI | Bench | Nico O'Reilly | DEF | 13 | 5.3 | 3.39 | 9.27 | 15.17 | 0.00 | 82.5 | 0.0 |
| Bench 2 | Bench | Konstantinos Mavropanos | DEF | 19 | 4.5 | 2.99 | 8.13 | 12.98 | 8.00 | 89.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.69 | 10.63 | 17.31 | 2.00 | 88.3 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 3.40 | 9.76 | 16.31 | 12.00 | 83.9 | 90.0 |
| Bench 3 | Bench | Igor Jesus Maciel da Cruz | FWD | 16 | 5.9 | 2.93 | 8.27 | 13.62 | 2.00 | 77.6 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 5.46 | 16.52 | 27.87 | 14.00 | 103.3 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 3.99 | 11.65 | 19.00 | 6.00 | 85.2 | 57.0 |
| XI | Bench | Morgan Rogers | MID | 2 | 7.4 | 3.48 | 10.50 | 17.07 | 0.00 | 89.2 | 0.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 3.81 | 10.39 | 17.53 | 2.00 | 88.6 | 90.0 |
| Bench 4 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.9 | 2.22 | 6.86 | 11.93 | 0.00 | 44.3 | 0.0 |