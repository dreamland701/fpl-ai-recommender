# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW9
- Simulated weeks: GW10-GW13
- Total predicted points: 265.09
- Total actual points: 164.00
- Average predicted points: 66.27
- Average actual points: 41.00
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
- Vice captain: Mohamed Salah
- Effective captain: Antoine Semenyo
- Chip used: none
- Predicted score: 62.08
- Actual score: 71.00
- Chip advisory: bench_boost (0.67): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.7 | 4.16 | 11.64 | 19.01 | 6.00 | 84.7 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.17 | 9.75 | 16.27 | 2.00 | 94.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.4 | 5.43 | 15.61 | 25.21 | 12.00 | 87.1 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 4.9 | 4.86 | 14.98 | 24.73 | 10.00 | 89.7 | 90.0 |
| Bench 4 | Bench | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.35 | 14.72 | 24.39 | 3.00 | 92.0 | 90.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 12 | 6.0 | 4.40 | 13.48 | 22.13 | 5.00 | 88.4 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.74 | 13.22 | 21.24 | 2.00 | 95.7 | 90.0 |
| XI | XI | Nick Woltemade | FWD | 15 | 7.4 | 4.97 | 14.53 | 22.40 | 1.00 | 73.0 | 45.0 |
| XI | XI | Junior Kroupi | FWD | 4 | 4.5 | 5.09 | 14.27 | 21.97 | 2.00 | 95.0 | 61.0 |
| Bench 2 | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.61 | 14.00 | 23.64 | 9.00 | 78.9 | 90.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.31 | 19.46 | 32.17 | 2.00 | 101.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.3 | 5.57 | 16.68 | 28.37 | 10.00 | 75.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.0 | 5.28 | 15.54 | 25.04 | 2.00 | 90.4 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.74 | 14.61 | 23.37 | 9.00 | 90.1 | 61.0 |
| XI | XI | Declan Rice | MID | 1 | 6.6 | 4.61 | 13.72 | 22.36 | 13.00 | 73.9 | 90.0 |

## GW11

- Train rows: 168588
- Bank: 0.40 -> 0.00
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Mohamed Salah
- Effective captain: Antoine Semenyo
- Chip used: none
- Predicted score: 61.81
- Actual score: 28.00
- Chip advisory: bench_boost (0.67): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Nick Woltemade -> Jean-Philippe Mateta (projected gain 3.08, hit 0)
- Autosub: Micky van de Ven replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.7 | 3.89 | 11.74 | 19.05 | 1.00 | 84.6 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.30 | 9.57 | 15.92 | 2.00 | 93.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.4 | 5.35 | 17.67 | 28.57 | 1.00 | 92.2 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 13 | 4.9 | 5.54 | 15.89 | 25.41 | 0.00 | 91.2 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.55 | 13.08 | 21.59 | 2.00 | 95.6 | 90.0 |
| Bench 3 | Autosub In | Micky van de Ven | DEF | 18 | 4.7 | 4.39 | 12.37 | 20.39 | 1.00 | 89.3 | 90.0 |
| Bench 4 | Bench | Virgil van Dijk | DEF | 12 | 6.0 | 4.08 | 12.27 | 20.24 | 1.00 | 91.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.8 | 5.58 | 16.12 | 24.90 | 2.00 | 77.8 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 4.76 | 13.80 | 23.25 | 7.00 | 72.7 | 82.0 |
| Bench 2 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 4.54 | 13.09 | 20.06 | 1.00 | 79.7 | 27.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 5.83 | 17.62 | 28.94 | 0.00 | 97.5 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.2 | 5.67 | 17.40 | 29.46 | 2.00 | 83.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.1 | 5.29 | 16.33 | 25.28 | 7.00 | 81.7 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 6.6 | 4.93 | 15.56 | 24.53 | 2.00 | 89.2 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.59 | 13.00 | 21.14 | 3.00 | 80.1 | 90.0 |

## GW12

- Train rows: 169340
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: João Pedro Junqueira de Jesus
- Chip used: triple_captain
- Predicted score: 69.41
- Actual score: 40.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.40) beats the best remaining Triple Captain opportunity (7.56).
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Virgil van Dijk -> Daniel Muñoz Mejía (projected gain 1.06, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.40) beats the best remaining Triple Captain opportunity (7.56).
- Autosub: Micky van de Ven replaced Gabriel dos Santos Magalhães.
- Autosub: Marc Guéhi replaced Antoine Semenyo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.88 | 11.50 | 18.74 | 2.00 | 81.6 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.31 | 9.72 | 16.01 | 2.00 | 91.6 | 90.0 |
| XI | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.41 | 16.46 | 27.15 | 0.00 | 91.6 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.64 | 12.55 | 20.49 | 3.00 | 90.5 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.7 | 4.43 | 12.43 | 21.55 | 14.00 | 79.7 | 90.0 |
| Bench 2 | Autosub In | Micky van de Ven | DEF | 18 | 4.7 | 3.84 | 12.20 | 19.82 | 0.00 | 93.5 | 90.0 |
| Bench 3 | Autosub In | Marc Guéhi | DEF | 13 | 5.0 | 3.77 | 10.55 | 17.49 | 5.00 | 51.2 | 90.0 |
| Vice Captain | Captain | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 6.07 | 17.27 | 27.05 | 1.00 | 85.6 | 75.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 4.74 | 14.67 | 23.48 | 1.00 | 67.9 | 59.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 3.14 | 9.22 | 15.55 | 2.00 | 46.1 | 85.0 |
| Captain | Bench | Antoine Semenyo | MID | 13 | 8.1 | 6.40 | 18.04 | 29.02 | 0.00 | 96.6 | 0.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.2 | 5.87 | 17.38 | 28.95 | 2.00 | 88.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.2 | 5.87 | 16.99 | 27.38 | 1.00 | 93.8 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 6.7 | 5.18 | 15.47 | 23.99 | 6.00 | 87.4 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.10 | 12.94 | 21.91 | 3.00 | 77.6 | 80.0 |

## GW13

- Train rows: 170095
- Bank: 0.20 -> 0.50
- Free transfers: 2 -> 2
- Captain: Bryan Mbeumo
- Vice captain: Mohamed Salah
- Effective captain: Bryan Mbeumo
- Chip used: bench_boost
- Predicted score: 71.78
- Actual score: 25.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.84) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Gabriel dos Santos Magalhães -> Marc Cucurella Saseta (projected gain 1.19, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.84) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.58 | 10.93 | 18.11 | 3.00 | 80.3 | 90.0 |
| Bench 1 | Bench Boost | Martin Dúbravka | GK | 3 | 4.0 | 3.18 | 9.51 | 15.67 | 1.00 | 89.5 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.7 | 4.81 | 13.50 | 22.45 | 1.00 | 88.6 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.38 | 13.17 | 21.18 | 2.00 | 92.4 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.1 | 4.30 | 12.80 | 21.63 | 1.00 | 83.2 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.0 | 4.11 | 11.99 | 20.28 | 0.00 | 75.2 | 90.0 |
| Bench 2 | Bench Boost | Micky van de Ven | DEF | 18 | 4.7 | 3.92 | 11.72 | 19.99 | 0.00 | 83.1 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 5.41 | 15.24 | 24.56 | 1.00 | 83.2 | 54.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 4.25 | 13.96 | 22.85 | 6.00 | 64.7 | 90.0 |
| Bench 4 | Bench Boost | Junior Kroupi | FWD | 4 | 4.5 | 2.94 | 10.83 | 18.13 | 1.00 | 58.0 | 10.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.2 | 5.70 | 16.94 | 28.00 | 0.00 | 84.1 | 0.0 |
| Captain | Captain | Bryan Mbeumo | MID | 14 | 8.3 | 5.97 | 16.79 | 26.32 | 1.00 | 82.8 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 6.7 | 5.37 | 16.18 | 25.10 | 4.00 | 95.3 | 90.0 |
| Bench 3 | Bench Boost | Antoine Semenyo | MID | 13 | 8.0 | 3.79 | 11.90 | 20.74 | 1.00 | 50.6 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.09 | 11.35 | 19.81 | 2.00 | 70.7 | 79.0 |