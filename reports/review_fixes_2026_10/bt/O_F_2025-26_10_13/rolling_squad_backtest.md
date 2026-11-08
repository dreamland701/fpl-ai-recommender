# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW9
- Simulated weeks: GW10-GW13
- Total predicted points: 260.03
- Total actual points: 150.00
- Average predicted points: 65.01
- Average actual points: 37.50
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
- Bank: 100.00 -> 0.80
- Free transfers: 1 -> 2
- Captain: Antoine Semenyo
- Vice captain: Mohamed Salah
- Effective captain: Antoine Semenyo
- Chip used: none
- Predicted score: 61.97
- Actual score: 66.00
- Chip advisory: bench_boost (0.67): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.7 | 4.13 | 11.55 | 18.67 | 6.00 | 84.8 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.13 | 9.66 | 16.02 | 2.00 | 94.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.4 | 5.40 | 15.52 | 25.26 | 12.00 | 87.2 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 4.9 | 4.84 | 14.35 | 23.50 | 10.00 | 89.7 | 90.0 |
| Bench 4 | Bench | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.36 | 14.09 | 23.20 | 3.00 | 92.0 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.73 | 13.38 | 21.72 | 2.00 | 95.7 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.0 | 4.81 | 13.25 | 21.30 | 6.00 | 79.1 | 90.0 |
| XI | XI | Junior Kroupi | FWD | 4 | 4.5 | 5.11 | 14.32 | 22.05 | 2.00 | 95.0 | 61.0 |
| Bench 2 | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.64 | 14.11 | 23.84 | 9.00 | 78.8 | 90.0 |
| Bench 3 | Bench | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.1 | 4.51 | 12.72 | 20.32 | 2.00 | 73.3 | 90.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.32 | 19.22 | 31.78 | 2.00 | 101.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.3 | 5.53 | 16.70 | 28.39 | 10.00 | 75.1 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.0 | 5.30 | 15.56 | 25.07 | 2.00 | 90.4 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.77 | 14.43 | 23.21 | 9.00 | 90.0 | 61.0 |
| XI | XI | Cody Gakpo | MID | 12 | 7.5 | 4.72 | 14.03 | 22.43 | 3.00 | 70.6 | 90.0 |

## GW11

- Train rows: 168588
- Bank: 0.80 -> 2.50
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Mohamed Salah
- Effective captain: Antoine Semenyo
- Chip used: none
- Predicted score: 60.63
- Actual score: 27.00
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Cody Gakpo -> Moisés Caicedo Corozo (projected gain 0.74, hit 0)
- Autosub outfielders: Micky van de Ven.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.91 | 11.67 | 18.83 | 1.00 | 84.6 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.34 | 9.53 | 15.73 | 2.00 | 93.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.38 | 16.93 | 27.86 | 1.00 | 92.1 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 13 | 5.0 | 5.52 | 15.29 | 24.66 | 0.00 | 91.2 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.52 | 13.18 | 21.89 | 2.00 | 95.7 | 90.0 |
| Bench 2 | Autosub In | Micky van de Ven | DEF | 18 | 4.7 | 4.41 | 12.76 | 20.95 | 1.00 | 89.3 | 90.0 |
| Bench 4 | Bench | Jurriën Timber | DEF | 1 | 6.1 | 4.01 | 12.26 | 19.64 | 1.00 | 76.8 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 4.79 | 13.78 | 23.26 | 7.00 | 72.7 | 82.0 |
| XI | XI | Junior Kroupi | FWD | 4 | 4.6 | 4.51 | 12.95 | 20.08 | 1.00 | 79.7 | 27.0 |
| Bench 3 | Bench | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.2 | 4.09 | 12.18 | 19.30 | 13.00 | 71.8 | 90.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 5.80 | 17.70 | 29.18 | 0.00 | 97.5 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.2 | 5.68 | 17.41 | 29.41 | 2.00 | 83.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 5.32 | 16.25 | 25.14 | 7.00 | 81.6 | 90.0 |
| XI | XI | Moisés Caicedo Corozo | MID | 7 | 5.9 | 4.82 | 13.48 | 21.85 | 2.00 | 86.1 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.59 | 13.43 | 21.83 | 3.00 | 80.1 | 90.0 |

## GW12

- Train rows: 169340
- Bank: 2.50 -> 1.50
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: João Pedro Junqueira de Jesus
- Chip used: triple_captain
- Predicted score: 69.12
- Actual score: 31.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.44) beats the best remaining Triple Captain opportunity (7.60).
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Marc Guéhi -> Marc Cucurella Saseta (projected gain 1.15, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.44) beats the best remaining Triple Captain opportunity (7.60).
- Autosub outfielders: Jurriën Timber, Micky van de Ven, Junior Kroupi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.92 | 11.44 | 18.53 | 2.00 | 81.6 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.29 | 9.62 | 15.78 | 2.00 | 91.7 | 90.0 |
| XI | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 6.6 | 5.44 | 16.41 | 26.96 | 0.00 | 91.6 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.1 | 4.53 | 12.60 | 20.57 | 6.00 | 80.8 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.68 | 12.53 | 21.03 | 3.00 | 90.5 | 90.0 |
| Bench 3 | Autosub In | Micky van de Ven | DEF | 18 | 4.8 | 3.81 | 12.07 | 20.08 | 0.00 | 93.5 | 90.0 |
| Bench 2 | Autosub In | Jurriën Timber | DEF | 1 | 6.1 | 3.88 | 11.46 | 18.56 | 5.00 | 76.8 | 90.0 |
| Vice Captain | Captain | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 6.03 | 17.11 | 26.66 | 1.00 | 85.7 | 75.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.2 | 4.56 | 13.49 | 21.45 | 4.00 | 81.8 | 90.0 |
| Bench 4 | Autosub In | Junior Kroupi | FWD | 4 | 4.6 | 3.17 | 9.28 | 15.77 | 2.00 | 46.0 | 85.0 |
| Captain | Bench | Antoine Semenyo | MID | 13 | 8.1 | 6.44 | 17.99 | 28.97 | 0.00 | 96.5 | 0.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.2 | 5.89 | 17.37 | 28.88 | 2.00 | 87.9 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.4 | 5.87 | 16.97 | 27.15 | 1.00 | 93.8 | 90.0 |
| XI | Bench | Moisés Caicedo Corozo | MID | 7 | 6.0 | 4.78 | 13.59 | 21.31 | 0.00 | 84.1 | 0.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.12 | 12.98 | 21.80 | 3.00 | 77.6 | 80.0 |

## GW13

- Train rows: 170095
- Bank: 1.50 -> 1.90
- Free transfers: 2 -> 2
- Captain: Bryan Mbeumo
- Vice captain: Mohamed Salah
- Effective captain: Bryan Mbeumo
- Chip used: bench_boost
- Predicted score: 68.31
- Actual score: 26.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.80) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Jurriën Timber -> Daniel Muñoz Mejía (projected gain 2.45, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.80) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.57 | 10.86 | 17.90 | 3.00 | 80.3 | 90.0 |
| Bench 1 | Bench Boost | Martin Dúbravka | GK | 3 | 4.0 | 3.16 | 9.39 | 15.42 | 1.00 | 89.6 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 4.82 | 13.76 | 21.94 | 1.00 | 88.6 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.41 | 13.00 | 21.44 | 2.00 | 92.4 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.1 | 4.26 | 12.99 | 21.04 | 1.00 | 83.2 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.8 | 3.92 | 11.90 | 19.27 | 0.00 | 83.1 | 90.0 |
| Bench 4 | Bench Boost | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 1.91 | 8.02 | 16.23 | 0.00 | 34.4 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.4 | 5.59 | 15.39 | 23.70 | 13.00 | 78.9 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 5.38 | 15.06 | 24.26 | 1.00 | 83.3 | 54.0 |
| Bench 2 | Bench Boost | Junior Kroupi | FWD | 4 | 4.6 | 2.97 | 10.80 | 18.40 | 1.00 | 57.9 | 10.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.2 | 5.74 | 16.92 | 27.87 | 0.00 | 84.0 | 0.0 |
| Captain | Captain | Bryan Mbeumo | MID | 14 | 8.6 | 5.95 | 16.60 | 25.84 | 1.00 | 82.8 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 3.82 | 11.73 | 20.58 | 1.00 | 50.5 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.6 | 4.11 | 11.57 | 19.65 | 2.00 | 70.7 | 79.0 |
| Bench 3 | Bench Boost | Moisés Caicedo Corozo | MID | 7 | 6.1 | 2.76 | 8.79 | 15.07 | -2.00 | 48.7 | 37.0 |