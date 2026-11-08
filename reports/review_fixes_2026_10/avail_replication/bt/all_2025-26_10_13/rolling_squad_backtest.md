# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW9
- Simulated weeks: GW10-GW13
- Total predicted points: 217.83
- Total actual points: 206.00
- Average predicted points: 54.46
- Average actual points: 51.50
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW9 are included before the first simulated week.
- League-average scores were not available for this run.

## GW10

- Train rows: 167841
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Bryan Mbeumo
- Vice captain: Mohamed Salah
- Effective captain: Bryan Mbeumo
- Chip used: none
- Predicted score: 53.22
- Actual score: 69.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.93 | 11.06 | 17.13 | 6.00 | 93.9 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 2.50 | 7.57 | 12.63 | 2.00 | 92.3 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 4.18 | 11.56 | 18.45 | 12.00 | 93.1 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 4.09 | 10.95 | 17.45 | 6.00 | 89.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 3.61 | 10.92 | 18.09 | 10.00 | 94.9 | 90.0 |
| Bench 4 | Bench | Virgil van Dijk | DEF | 12 | 6.0 | 3.10 | 10.78 | 17.39 | 5.00 | 83.7 | 90.0 |
| Bench 3 | Bench | Daniel Muñoz Mejía | DEF | 8 | 5.7 | 3.32 | 10.10 | 17.79 | 6.00 | 93.3 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 6 | 6.4 | 3.87 | 10.90 | 17.16 | 6.00 | 86.1 | 81.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.2 | 3.75 | 10.45 | 16.13 | 2.00 | 82.0 | 90.0 |
| Bench 2 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 3.32 | 10.15 | 16.50 | 2.00 | 70.3 | 61.0 |
| Captain | Captain | Bryan Mbeumo | MID | 14 | 8.3 | 6.70 | 17.86 | 29.74 | 2.00 | 127.9 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.2 | 4.93 | 14.87 | 26.18 | 10.00 | 79.5 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.1 | 3.97 | 13.65 | 23.08 | 2.00 | 99.9 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.08 | 13.30 | 21.14 | 9.00 | 88.0 | 61.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.5 | 3.41 | 11.05 | 17.52 | 2.00 | 83.6 | 90.0 |

## GW11

- Train rows: 168588
- Bank: 0.10 -> 0.60
- Free transfers: 2 -> 2
- Captain: Moisés Caicedo Corozo
- Vice captain: Mohamed Salah
- Effective captain: Moisés Caicedo Corozo
- Chip used: none
- Predicted score: 47.79
- Actual score: 37.00
- Transfer: Iliman Ndiaye -> Moisés Caicedo Corozo (projected gain 3.48, hit 0)
- Autosub: Igor Thiago Nascimento Rodrigues replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.28 | 10.04 | 15.65 | 1.00 | 92.4 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 2.67 | 7.81 | 13.27 | 2.00 | 93.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 4.32 | 14.61 | 23.05 | 1.00 | 95.5 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.0 | 4.06 | 12.78 | 19.44 | 0.00 | 91.6 | 0.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.7 | 3.65 | 11.20 | 17.81 | 6.00 | 82.7 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 3.48 | 11.08 | 17.45 | 1.00 | 81.5 | 90.0 |
| Bench 4 | Bench | Virgil van Dijk | DEF | 12 | 5.9 | 2.71 | 9.08 | 16.90 | 1.00 | 87.6 | 90.0 |
| XI | XI | Junior Kroupi | FWD | 4 | 4.6 | 3.32 | 10.20 | 16.28 | 1.00 | 85.2 | 27.0 |
| Bench 3 | Bench | Danny Welbeck | FWD | 6 | 6.4 | 3.11 | 9.75 | 15.17 | 2.00 | 66.2 | 84.0 |
| Bench 2 | Autosub In | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.2 | 3.11 | 9.67 | 14.66 | 13.00 | 69.3 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.2 | 4.53 | 16.20 | 27.45 | 2.00 | 91.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.1 | 4.44 | 13.44 | 22.14 | 0.00 | 102.4 | 90.0 |
| Captain | Captain | Moisés Caicedo Corozo | MID | 7 | 6.0 | 5.01 | 12.67 | 19.28 | 2.00 | 97.7 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 3.43 | 11.85 | 17.95 | 7.00 | 70.6 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.5 | 3.26 | 10.34 | 17.25 | 1.00 | 84.8 | 90.0 |

## GW12

- Train rows: 169340
- Bank: 0.60 -> 1.00
- Free transfers: 2 -> 2
- Captain: Bryan Mbeumo
- Vice captain: Mohamed Salah
- Effective captain: Bryan Mbeumo
- Chip used: triple_captain
- Predicted score: 59.10
- Actual score: 51.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.04) beats the best remaining Triple Captain opportunity (7.12).
- Transfer: Gabriel dos Santos Magalhães -> Marc Cucurella Saseta (projected gain 2.64, hit 0)
- Chip used: Triple Captain on Bryan Mbeumo. Optimizer chose Triple Captain here because the current estimated captain upside (6.04) beats the best remaining Triple Captain opportunity (7.12).
- Autosub: Danny Welbeck replaced Moisés Caicedo Corozo.
- Autosub: Junior Kroupi replaced Antoine Semenyo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.28 | 9.99 | 16.24 | 2.00 | 85.4 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 2.56 | 7.24 | 12.40 | 2.00 | 91.9 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 4.35 | 12.30 | 18.45 | 5.00 | 97.1 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.7 | 4.75 | 11.89 | 20.36 | 14.00 | 93.6 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.1 | 3.86 | 11.64 | 19.23 | 6.00 | 86.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.36 | 11.40 | 17.72 | 3.00 | 104.9 | 90.0 |
| Bench 4 | Bench | Marc Guéhi | DEF | 8 | 5.0 | 2.39 | 6.25 | 10.65 | 5.00 | 28.1 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.3 | 4.39 | 12.73 | 19.38 | 4.00 | 92.0 | 90.0 |
| Bench 2 | Autosub In | Danny Welbeck | FWD | 6 | 6.4 | 2.75 | 9.10 | 14.94 | 8.00 | 68.6 | 90.0 |
| Bench 3 | Autosub In | Junior Kroupi | FWD | 4 | 4.6 | 2.61 | 7.98 | 13.35 | 2.00 | 58.7 | 85.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.2 | 5.51 | 17.33 | 29.61 | 2.00 | 97.0 | 90.0 |
| Captain | Captain | Bryan Mbeumo | MID | 14 | 8.4 | 6.04 | 16.82 | 28.18 | 1.00 | 110.9 | 90.0 |
| XI | Bench | Moisés Caicedo Corozo | MID | 7 | 6.0 | 3.61 | 11.13 | 16.17 | 0.00 | 82.0 | 0.0 |
| XI | Bench | Antoine Semenyo | MID | 4 | 8.0 | 3.17 | 10.90 | 18.30 | 0.00 | 60.6 | 0.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.5 | 3.69 | 10.33 | 16.54 | 2.00 | 86.9 | 90.0 |

## GW13

- Train rows: 170095
- Bank: 1.00 -> 1.90
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Igor Thiago Nascimento Rodrigues
- Chip used: bench_boost
- Predicted score: 57.71
- Actual score: 49.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.30) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Antoine Semenyo -> Declan Rice (projected gain 7.65, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.30) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 2.68 | 8.25 | 13.88 | 3.00 | 82.2 | 90.0 |
| Bench 1 | Bench Boost | Martin Dúbravka | GK | 3 | 4.0 | 2.26 | 6.45 | 10.49 | 1.00 | 89.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.2 | 3.22 | 11.08 | 16.87 | 2.00 | 84.1 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.1 | 3.21 | 10.70 | 17.61 | 1.00 | 83.7 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 3.46 | 10.08 | 16.28 | 0.00 | 78.4 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 3.82 | 9.89 | 16.72 | 1.00 | 93.9 | 90.0 |
| Bench 2 | Bench Boost | Virgil van Dijk | DEF | 12 | 6.0 | 2.25 | 6.83 | 12.28 | 6.00 | 71.8 | 90.0 |
| Vice Captain | Captain | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.4 | 5.76 | 14.78 | 21.28 | 13.00 | 102.8 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 6 | 6.5 | 3.40 | 10.23 | 16.20 | 2.00 | 82.0 | 64.0 |
| Bench 3 | Bench Boost | Junior Kroupi | FWD | 4 | 4.6 | 2.14 | 8.16 | 13.94 | 1.00 | 61.6 | 10.0 |
| Captain | XI | Mohamed Salah | MID | 12 | 14.2 | 5.91 | 17.59 | 28.60 | 0.00 | 97.6 | 0.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.52 | 14.42 | 21.24 | 4.00 | 89.5 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.4 | 4.14 | 13.72 | 21.41 | 1.00 | 75.1 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.5 | 3.38 | 10.01 | 17.96 | 3.00 | 79.6 | 90.0 |
| Bench 4 | Bench Boost | Moisés Caicedo Corozo | MID | 7 | 6.0 | 1.66 | 6.06 | 9.04 | -2.00 | 50.7 | 37.0 |