# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW9
- Simulated weeks: GW10-GW13
- Total predicted points: 268.83
- Total actual points: 152.00
- Average predicted points: 67.21
- Average actual points: 38.00
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
- Bank: 100.00 -> 0.40
- Free transfers: 1 -> 2
- Captain: Antoine Semenyo
- Vice captain: Micky van de Ven
- Effective captain: Antoine Semenyo
- Chip used: none
- Predicted score: 62.51
- Actual score: 67.00
- Chip advisory: bench_boost (0.67): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.7 | 4.30 | 12.38 | 20.54 | 6.00 | 89.4 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.63 | 10.96 | 18.47 | 2.00 | 100.6 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 4.9 | 5.24 | 16.17 | 26.82 | 10.00 | 94.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.4 | 5.37 | 15.92 | 25.80 | 12.00 | 90.1 | 90.0 |
| Bench 3 | Bench | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.43 | 15.08 | 25.07 | 3.00 | 94.8 | 90.0 |
| Vice Captain | XI | Micky van de Ven | DEF | 18 | 4.7 | 5.40 | 15.02 | 24.26 | 2.00 | 103.9 | 90.0 |
| Bench 2 | Bench | Virgil van Dijk | DEF | 12 | 6.0 | 4.50 | 13.82 | 22.86 | 5.00 | 90.1 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 5.02 | 15.16 | 25.64 | 9.00 | 85.4 | 90.0 |
| XI | XI | Junior Kroupi | FWD | 4 | 4.5 | 4.85 | 13.84 | 21.67 | 2.00 | 98.6 | 61.0 |
| XI | XI | Nick Woltemade | FWD | 15 | 7.4 | 4.74 | 13.78 | 21.53 | 1.00 | 73.2 | 45.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.13 | 19.29 | 32.00 | 2.00 | 102.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.0 | 5.23 | 15.48 | 25.18 | 2.00 | 91.6 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.3 | 5.15 | 15.47 | 26.63 | 10.00 | 69.0 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.96 | 15.16 | 24.28 | 9.00 | 90.8 | 61.0 |
| Bench 4 | Bench | Declan Rice | MID | 1 | 6.6 | 4.42 | 13.55 | 22.22 | 13.00 | 74.6 | 90.0 |

## GW11

- Train rows: 168588
- Bank: 0.40 -> 0.00
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Antoine Semenyo
- Chip used: none
- Predicted score: 63.09
- Actual score: 28.00
- Chip advisory: bench_boost (0.67): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Nick Woltemade -> Jean-Philippe Mateta (projected gain 1.41, hit 0)
- Autosub: Iliman Ndiaye replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.7 | 4.30 | 12.72 | 20.81 | 1.00 | 89.4 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.52 | 10.38 | 17.48 | 2.00 | 98.5 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.4 | 5.84 | 18.54 | 29.84 | 1.00 | 94.7 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 13 | 4.9 | 5.61 | 16.32 | 26.32 | 0.00 | 94.8 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.69 | 13.66 | 22.57 | 2.00 | 99.0 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.88 | 13.64 | 22.50 | 1.00 | 96.2 | 90.0 |
| Bench 4 | Bench | Virgil van Dijk | DEF | 12 | 6.0 | 3.98 | 12.07 | 20.05 | 1.00 | 90.4 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.8 | 5.11 | 14.62 | 22.78 | 2.00 | 74.4 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 5.17 | 14.56 | 24.67 | 7.00 | 79.3 | 82.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 4.48 | 12.87 | 20.06 | 1.00 | 84.2 | 27.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 5.95 | 18.17 | 29.83 | 0.00 | 100.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.1 | 5.49 | 16.69 | 25.84 | 7.00 | 80.7 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 6.6 | 5.25 | 16.16 | 25.43 | 2.00 | 89.9 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.2 | 4.86 | 15.39 | 26.45 | 2.00 | 74.6 | 90.0 |
| Bench 2 | Autosub In | Iliman Ndiaye | MID | 9 | 6.5 | 4.61 | 13.26 | 21.50 | 3.00 | 80.1 | 90.0 |

## GW12

- Train rows: 169340
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: João Pedro Junqueira de Jesus
- Chip used: triple_captain
- Predicted score: 70.90
- Actual score: 28.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.56) beats the best remaining Triple Captain opportunity (7.74).
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Iliman Ndiaye -> Moisés Caicedo Corozo (projected gain 0.77, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.56) beats the best remaining Triple Captain opportunity (7.74).
- Autosub: Marc Guéhi replaced Gabriel dos Santos Magalhães.
- Autosub: Virgil van Dijk replaced Antoine Semenyo.
- Autosub: Junior Kroupi replaced Moisés Caicedo Corozo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.21 | 12.34 | 20.25 | 2.00 | 86.2 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.61 | 10.56 | 17.55 | 2.00 | 96.7 | 90.0 |
| XI | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.79 | 17.26 | 28.40 | 0.00 | 95.1 | 0.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.50 | 13.77 | 22.30 | 0.00 | 100.3 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.75 | 12.99 | 21.19 | 3.00 | 93.2 | 90.0 |
| Bench 3 | Autosub In | Virgil van Dijk | DEF | 12 | 5.9 | 3.95 | 11.59 | 19.52 | 3.00 | 86.0 | 90.0 |
| Bench 2 | Autosub In | Marc Guéhi | DEF | 13 | 5.0 | 3.96 | 11.26 | 18.75 | 5.00 | 55.7 | 90.0 |
| Vice Captain | Captain | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 6.03 | 16.78 | 26.58 | 1.00 | 88.3 | 75.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 4.51 | 14.25 | 22.82 | 1.00 | 65.2 | 59.0 |
| Bench 4 | Autosub In | Junior Kroupi | FWD | 4 | 4.5 | 3.22 | 10.12 | 16.95 | 2.00 | 50.8 | 85.0 |
| Captain | Bench | Antoine Semenyo | MID | 13 | 8.1 | 6.56 | 18.69 | 30.06 | 0.00 | 100.1 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.2 | 5.93 | 17.11 | 27.64 | 1.00 | 94.2 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 6.7 | 5.42 | 16.01 | 24.72 | 6.00 | 87.9 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.2 | 5.31 | 15.96 | 26.83 | 2.00 | 79.5 | 90.0 |
| XI | Bench | Moisés Caicedo Corozo | MID | 7 | 6.0 | 4.77 | 13.61 | 20.84 | 0.00 | 84.8 | 0.0 |

## GW13

- Train rows: 170095
- Bank: 0.50 -> 1.10
- Free transfers: 2 -> 2
- Captain: Declan Rice
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Declan Rice
- Chip used: bench_boost
- Predicted score: 72.33
- Actual score: 29.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.89) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Gabriel dos Santos Magalhães -> Daniel Muñoz Mejía (projected gain 2.01, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.89) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.88 | 11.64 | 19.35 | 3.00 | 84.2 | 90.0 |
| Bench 1 | Bench Boost | Martin Dúbravka | GK | 3 | 4.0 | 3.45 | 10.31 | 17.12 | 1.00 | 94.4 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.67 | 13.88 | 22.33 | 2.00 | 96.2 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 4.91 | 13.61 | 22.63 | 1.00 | 88.7 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.0 | 4.36 | 12.62 | 21.37 | 0.00 | 78.8 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.23 | 12.54 | 21.39 | 0.00 | 88.2 | 90.0 |
| Bench 2 | Bench Boost | Virgil van Dijk | DEF | 12 | 6.0 | 4.04 | 11.72 | 20.27 | 6.00 | 79.1 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 5.82 | 16.29 | 26.16 | 1.00 | 86.9 | 54.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 4.23 | 13.66 | 22.38 | 6.00 | 62.8 | 90.0 |
| Bench 3 | Bench Boost | Junior Kroupi | FWD | 4 | 4.5 | 3.35 | 11.41 | 19.00 | 1.00 | 62.4 | 10.0 |
| Captain | Captain | Declan Rice | MID | 1 | 6.7 | 5.83 | 17.13 | 26.43 | 4.00 | 97.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 5.52 | 16.47 | 25.96 | 1.00 | 81.9 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.2 | 5.11 | 15.57 | 25.91 | 0.00 | 75.3 | 0.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 4.06 | 12.61 | 21.89 | 1.00 | 54.7 | 90.0 |
| Bench 4 | Bench Boost | Moisés Caicedo Corozo | MID | 7 | 6.0 | 3.04 | 9.65 | 15.60 | -2.00 | 51.0 | 37.0 |