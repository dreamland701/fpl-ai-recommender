# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW9
- Simulated weeks: GW10-GW13
- Total predicted points: 267.88
- Total actual points: 180.00
- Average predicted points: 66.97
- Average actual points: 45.00
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
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Bryan Mbeumo
- Vice captain: Jean-Philippe Mateta
- Effective captain: Bryan Mbeumo
- Chip used: none
- Predicted score: 67.27
- Actual score: 72.00
- Chip advisory: bench_boost (0.62): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.54 | 12.36 | 19.96 | 6.00 | 96.2 | 90.0 |
| Bench 1 | Bench | Robin Roefs | GK | 17 | 4.7 | 3.34 | 9.67 | 15.89 | 2.00 | 90.2 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.59 | 15.81 | 24.86 | 12.00 | 95.2 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 5.15 | 15.09 | 24.37 | 10.00 | 96.4 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 5.09 | 13.97 | 22.11 | 6.00 | 89.0 | 90.0 |
| Bench 4 | Bench | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.79 | 13.15 | 21.61 | 3.00 | 86.6 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.67 | 12.50 | 19.79 | 2.00 | 94.8 | 90.0 |
| Vice Captain | XI | Jean-Philippe Mateta | FWD | 8 | 7.8 | 6.35 | 16.59 | 25.67 | 9.00 | 97.7 | 89.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 4.12 | 12.00 | 18.75 | 2.00 | 87.9 | 61.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.2 | 4.34 | 11.88 | 18.65 | 2.00 | 77.6 | 90.0 |
| Captain | Captain | Bryan Mbeumo | MID | 14 | 8.3 | 7.73 | 20.18 | 31.06 | 2.00 | 129.8 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.84 | 18.22 | 29.84 | 2.00 | 103.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.2 | 5.46 | 16.52 | 28.42 | 10.00 | 73.7 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.79 | 14.53 | 22.99 | 9.00 | 89.5 | 61.0 |
| Bench 2 | Bench | Dominik Szoboszlai | MID | 12 | 6.5 | 4.22 | 12.17 | 19.24 | 2.00 | 82.4 | 90.0 |

## GW11

- Train rows: 168588
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Jean-Philippe Mateta
- Effective captain: Antoine Semenyo
- Chip used: none
- Predicted score: 62.42
- Actual score: 22.00
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Dominik Szoboszlai -> Moisés Caicedo Corozo (projected gain 1.70, hit 0)
- Autosub: Marcos Senesi Barón replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.39 | 12.42 | 19.91 | 1.00 | 94.3 | 90.0 |
| Bench 1 | Bench | Robin Roefs | GK | 17 | 4.7 | 2.90 | 9.04 | 14.95 | 2.00 | 84.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.83 | 17.82 | 27.99 | 1.00 | 97.3 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.0 | 5.37 | 15.16 | 23.85 | 0.00 | 93.7 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 4.29 | 12.63 | 20.18 | 1.00 | 81.9 | 90.0 |
| Bench 2 | Autosub In | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.25 | 12.08 | 19.56 | 2.00 | 93.6 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.33 | 11.59 | 18.73 | 1.00 | 90.4 | 90.0 |
| Vice Captain | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.85 | 16.14 | 24.73 | 2.00 | 83.5 | 90.0 |
| Bench 3 | Bench | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.2 | 3.69 | 10.95 | 17.17 | 13.00 | 64.0 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 3.67 | 10.79 | 16.79 | 1.00 | 72.2 | 27.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.2 | 5.82 | 18.01 | 30.49 | 2.00 | 88.8 | 90.0 |
| Captain | Captain | Antoine Semenyo | MID | 4 | 8.1 | 5.97 | 17.56 | 28.28 | 0.00 | 106.2 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 4.66 | 14.79 | 22.81 | 7.00 | 67.0 | 90.0 |
| XI | XI | Moisés Caicedo Corozo | MID | 7 | 6.0 | 5.44 | 13.74 | 21.36 | 2.00 | 96.7 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.49 | 12.83 | 20.56 | 3.00 | 78.5 | 90.0 |

## GW12

- Train rows: 169340
- Bank: 0.50 -> 1.20
- Free transfers: 2 -> 2
- Captain: Bryan Mbeumo
- Vice captain: Mohamed Salah
- Effective captain: Bryan Mbeumo
- Chip used: triple_captain
- Predicted score: 69.81
- Actual score: 42.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.12) beats the best remaining Triple Captain opportunity (8.40).
- Transfer: Gabriel dos Santos Magalhães -> Daniel Muñoz Mejía (projected gain 1.89, hit 0)
- Chip used: Triple Captain on Bryan Mbeumo. Optimizer chose Triple Captain here because the current estimated captain upside (7.12) beats the best remaining Triple Captain opportunity (8.40).
- Autosub: Micky van de Ven replaced Antoine Semenyo.
- Autosub: Marc Guéhi replaced Moisés Caicedo Corozo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.95 | 11.38 | 18.42 | 2.00 | 85.2 | 90.0 |
| Bench 1 | Bench | Robin Roefs | GK | 17 | 4.7 | 3.00 | 8.89 | 14.66 | 3.00 | 87.2 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 5.01 | 13.82 | 21.68 | 5.00 | 96.2 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 5.07 | 13.56 | 22.76 | 14.00 | 92.2 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.82 | 12.50 | 19.74 | 3.00 | 94.3 | 90.0 |
| Bench 2 | Autosub In | Micky van de Ven | DEF | 18 | 4.7 | 3.91 | 11.81 | 18.84 | 0.00 | 94.7 | 90.0 |
| Bench 3 | Autosub In | Marc Guéhi | DEF | 8 | 5.0 | 3.28 | 9.19 | 15.20 | 5.00 | 48.2 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 4.82 | 14.99 | 23.87 | 1.00 | 69.7 | 59.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.3 | 5.02 | 14.08 | 21.98 | 4.00 | 91.0 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 2.52 | 8.15 | 13.69 | 2.00 | 39.6 | 85.0 |
| Captain | Captain | Bryan Mbeumo | MID | 14 | 8.4 | 7.12 | 19.24 | 29.98 | 1.00 | 112.8 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.2 | 6.30 | 18.73 | 31.20 | 2.00 | 94.0 | 90.0 |
| XI | Bench | Antoine Semenyo | MID | 4 | 8.0 | 5.07 | 14.96 | 24.38 | 0.00 | 80.9 | 0.0 |
| XI | Bench | Moisés Caicedo Corozo | MID | 7 | 6.0 | 4.45 | 12.54 | 18.85 | 0.00 | 79.4 | 0.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 3.93 | 12.07 | 20.39 | 3.00 | 74.0 | 80.0 |

## GW13

- Train rows: 170095
- Bank: 1.20 -> 0.00
- Free transfers: 2 -> 2
- Captain: Igor Thiago Nascimento Rodrigues
- Vice captain: Mohamed Salah
- Effective captain: Igor Thiago Nascimento Rodrigues
- Chip used: bench_boost
- Predicted score: 68.38
- Actual score: 44.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.61) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Iliman Ndiaye -> Eberechi Eze (projected gain 5.45, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.61) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.47 | 10.35 | 17.03 | 3.00 | 80.5 | 90.0 |
| Bench 1 | Bench Boost | Robin Roefs | GK | 17 | 4.7 | 2.75 | 8.21 | 13.50 | 1.00 | 82.5 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 5.23 | 13.96 | 22.84 | 1.00 | 94.2 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.2 | 4.26 | 12.43 | 19.72 | 2.00 | 80.8 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.06 | 11.48 | 19.10 | 0.00 | 87.7 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.77 | 11.37 | 18.19 | 2.00 | 83.4 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 3.98 | 11.21 | 18.68 | 0.00 | 75.8 | 90.0 |
| Captain | Captain | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.4 | 6.78 | 17.27 | 25.76 | 13.00 | 100.1 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 3.53 | 12.29 | 20.64 | 6.00 | 52.0 | 90.0 |
| Bench 2 | Bench Boost | Junior Kroupi | FWD | 4 | 4.6 | 2.49 | 9.12 | 15.33 | 1.00 | 49.4 | 10.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.2 | 6.23 | 18.62 | 30.71 | 0.00 | 91.8 | 0.0 |
| XI | XI | Eberechi Eze | MID | 1 | 7.7 | 5.86 | 16.14 | 25.51 | 2.00 | 101.1 | 71.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.4 | 4.82 | 14.96 | 23.75 | 1.00 | 72.1 | 90.0 |
| Bench 3 | Bench Boost | Antoine Semenyo | MID | 4 | 7.9 | 2.26 | 8.15 | 14.98 | 1.00 | 30.6 | 90.0 |
| Bench 4 | Bench Boost | Moisés Caicedo Corozo | MID | 7 | 6.0 | 2.10 | 7.38 | 11.99 | -2.00 | 37.8 | 37.0 |