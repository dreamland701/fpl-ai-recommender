# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW5
- Simulated weeks: GW6-GW9
- Total predicted points: 264.91
- Total actual points: 243.00
- Average predicted points: 66.23
- Average actual points: 60.75
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW5 are included before the first simulated week.
- League-average scores were not available for this run.

## GW6

- Train rows: 164865
- Bank: 100.00 -> 0.80
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 61.75
- Actual score: 37.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 3.44 | 10.54 | 17.10 | 2.00 | 83.0 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 2.97 | 9.43 | 15.30 | 1.00 | 92.7 | 90.0 |
| Bench 3 | Bench | Trevoh Chalobah | DEF | 7 | 5.1 | 3.43 | 14.25 | 19.55 | -3.00 | 98.0 | 52.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 5.54 | 13.63 | 19.30 | 2.00 | 75.5 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.6 | 4.23 | 13.01 | 19.13 | 1.00 | 85.3 | 27.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 4.7 | 3.79 | 12.48 | 18.04 | 7.00 | 89.2 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.26 | 12.06 | 17.98 | 2.00 | 79.1 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.09 | 17.40 | 27.13 | 2.00 | 90.8 | 90.0 |
| Bench 2 | Bench | Richarlison de Andrade | FWD | 18 | 6.7 | 3.76 | 11.19 | 17.38 | 2.00 | 61.7 | 90.0 |
| Bench 4 | Bench | Wilson Isidor | FWD | 17 | 5.5 | 3.33 | 9.29 | 14.24 | 2.00 | 61.6 | 84.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.04 | 21.51 | 34.52 | 2.00 | 92.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.64 | 17.46 | 25.40 | 7.00 | 84.4 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.66 | 15.73 | 23.62 | -1.00 | 80.9 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 4.33 | 13.62 | 20.42 | 9.00 | 85.9 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 4.68 | 13.40 | 20.12 | 2.00 | 87.2 | 82.0 |

## GW7

- Train rows: 165607
- Bank: 0.80 -> 0.30
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Mohamed Salah
- Effective captain: Antoine Semenyo
- Chip used: none
- Predicted score: 58.67
- Actual score: 69.00
- Transfer: Pedro Porro Sauceda -> Gabriel dos Santos Magalhães (projected gain 3.13, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 3.78 | 10.86 | 17.50 | 6.00 | 79.9 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.05 | 9.52 | 15.53 | 2.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 5.10 | 14.76 | 22.25 | 9.00 | 91.7 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 4.7 | 4.43 | 14.29 | 21.61 | 3.00 | 89.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.16 | 13.09 | 19.84 | 1.00 | 87.3 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 3.94 | 12.02 | 19.21 | 2.00 | 81.6 | 90.0 |
| Bench 2 | Bench | Trevoh Chalobah | DEF | 7 | 5.1 | 3.74 | 11.65 | 17.42 | 0.00 | 70.0 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 5.15 | 16.47 | 26.54 | 2.00 | 86.4 | 73.0 |
| Bench 3 | Bench | Richarlison de Andrade | FWD | 18 | 6.7 | 3.69 | 11.45 | 18.14 | 1.00 | 62.7 | 16.0 |
| Bench 4 | Bench | Wilson Isidor | FWD | 17 | 5.5 | 2.89 | 8.39 | 13.06 | 1.00 | 60.8 | 58.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 7.6 | 6.13 | 18.52 | 28.82 | 18.00 | 90.7 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 6.08 | 18.07 | 30.51 | 2.00 | 83.8 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.14 | 14.20 | 22.28 | 3.00 | 72.1 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 4.45 | 13.71 | 21.82 | 2.00 | 85.3 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 4.19 | 12.88 | 19.70 | 3.00 | 74.1 | 75.0 |

## GW8

- Train rows: 166350
- Bank: 0.30 -> 1.50
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Mohamed Salah
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 68.96
- Actual score: 50.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.59) beats the best remaining Triple Captain opportunity (9.31).
- Transfer: Virgil van Dijk -> Marcos Senesi Barón (projected gain 5.07, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (7.59) beats the best remaining Triple Captain opportunity (9.31).
- Autosub: Richarlison de Andrade replaced Enzo Fernández.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 3.74 | 11.22 | 18.35 | 6.00 | 82.9 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.54 | 9.99 | 16.16 | 9.00 | 91.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 5.13 | 15.81 | 23.40 | 12.00 | 89.3 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.97 | 15.68 | 22.78 | 2.00 | 79.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 4.7 | 4.90 | 12.35 | 23.15 | 4.00 | 93.8 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.00 | 10.94 | 18.50 | 0.00 | 86.5 | 90.0 |
| Bench 4 | Bench | Trevoh Chalobah | DEF | 7 | 5.1 | 2.04 | 6.65 | 11.86 | 6.00 | 32.2 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.44 | 13.06 | 23.67 | 2.00 | 73.7 | 90.0 |
| Bench 2 | Autosub In | Richarlison de Andrade | FWD | 18 | 6.7 | 3.24 | 9.88 | 15.55 | 1.00 | 48.6 | 30.0 |
| Bench 3 | Bench | Wilson Isidor | FWD | 17 | 5.5 | 3.02 | 7.82 | 12.60 | 2.00 | 55.8 | 75.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 7.7 | 7.56 | 20.47 | 33.82 | 4.00 | 103.8 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 5.75 | 17.56 | 29.55 | 2.00 | 79.5 | 84.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.46 | 15.54 | 23.00 | 8.00 | 78.1 | 84.0 |
| XI | Bench | Enzo Fernández | MID | 7 | 6.7 | 4.49 | 13.88 | 20.72 | 0.00 | 79.7 | 0.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 4.39 | 11.86 | 20.43 | 1.00 | 75.3 | 58.0 |

## GW9

- Train rows: 167095
- Bank: 1.50 -> 2.50
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Junior Kroupi
- Effective captain: Antoine Semenyo
- Chip used: bench_boost
- Predicted score: 75.54
- Actual score: 87.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.41) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Wilson Isidor -> Junior Kroupi (projected gain 4.71, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.41) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 4.11 | 11.48 | 18.81 | 6.00 | 83.5 | 90.0 |
| Bench 1 | Bench Boost | Martin Dúbravka | GK | 3 | 4.0 | 3.55 | 10.29 | 16.95 | 2.00 | 93.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.2 | 6.12 | 17.01 | 26.39 | 9.00 | 92.5 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 5.15 | 15.52 | 23.25 | 5.00 | 96.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 4.8 | 4.52 | 14.37 | 23.47 | 4.00 | 91.9 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 3.78 | 11.20 | 18.00 | 23.00 | 84.6 | 90.0 |
| Bench 2 | Bench Boost | Trevoh Chalobah | DEF | 7 | 5.1 | 3.53 | 10.16 | 16.23 | 1.00 | 61.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 5.14 | 15.12 | 24.93 | 2.00 | 82.9 | 84.0 |
| Vice Captain | XI | Junior Kroupi | FWD | 4 | 4.5 | 6.47 | 14.79 | 21.21 | 12.00 | 119.9 | 136.0 |
| Bench 4 | Bench Boost | Richarlison de Andrade | FWD | 18 | 6.7 | 2.66 | 8.82 | 14.47 | 4.00 | 43.9 | 28.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 7.8 | 6.76 | 20.01 | 31.79 | 3.00 | 96.4 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.4 | 5.34 | 16.19 | 28.16 | 6.00 | 73.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.64 | 13.38 | 21.47 | 4.00 | 79.6 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 3.83 | 11.68 | 19.02 | 1.00 | 63.2 | 75.0 |
| Bench 3 | Bench Boost | Enzo Fernández | MID | 7 | 6.7 | 3.18 | 9.28 | 14.80 | 2.00 | 42.0 | 90.0 |