# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW5
- Simulated weeks: GW6-GW9
- Total predicted points: 269.10
- Total actual points: 244.00
- Average predicted points: 67.27
- Average actual points: 61.00
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
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 62.13
- Actual score: 30.00
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 3.83 | 11.95 | 21.92 | 2.00 | 88.9 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.33 | 10.83 | 20.15 | 1.00 | 98.9 | 90.0 |
| Bench 3 | Bench | Trevoh Chalobah | DEF | 7 | 5.1 | 3.50 | 14.53 | 23.81 | -3.00 | 100.9 | 52.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.6 | 4.54 | 13.95 | 24.26 | 1.00 | 90.5 | 27.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 4.7 | 4.31 | 13.71 | 23.67 | 7.00 | 93.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 5.21 | 13.41 | 23.00 | 2.00 | 74.8 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.61 | 13.15 | 23.32 | 2.00 | 85.0 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.22 | 17.86 | 31.43 | 2.00 | 95.1 | 90.0 |
| Bench 2 | Bench | Chris Wood | FWD | 16 | 7.6 | 4.01 | 12.27 | 22.28 | 2.00 | 62.7 | 89.0 |
| Bench 4 | Bench | Wilson Isidor | FWD | 17 | 5.5 | 3.40 | 9.72 | 18.03 | 2.00 | 65.9 | 84.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 6.26 | 19.90 | 35.46 | 2.00 | 86.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.68 | 17.81 | 29.96 | 7.00 | 86.1 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.35 | 15.10 | 26.68 | -1.00 | 77.9 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 4.85 | 14.24 | 25.07 | 2.00 | 92.1 | 82.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.6 | 5.00 | 14.09 | 25.12 | 2.00 | 80.8 | 90.0 |

## GW7

- Train rows: 165607
- Bank: 0.00 -> 0.80
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Mohamed Salah
- Effective captain: Antoine Semenyo
- Chip used: none
- Predicted score: 59.76
- Actual score: 72.00
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Pedro Porro Sauceda -> Marcos Senesi Barón (projected gain 3.10, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 3.97 | 11.77 | 20.08 | 6.00 | 84.1 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.40 | 10.80 | 18.73 | 2.00 | 96.1 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.05 | 15.51 | 22.32 | 2.00 | 84.8 | 77.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 4.7 | 4.56 | 14.89 | 23.03 | 3.00 | 93.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.23 | 13.52 | 20.88 | 1.00 | 88.3 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.16 | 12.97 | 21.20 | 2.00 | 87.7 | 90.0 |
| Bench 2 | Bench | Trevoh Chalobah | DEF | 7 | 5.1 | 3.99 | 12.44 | 19.14 | 0.00 | 73.0 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 5.44 | 17.31 | 28.31 | 2.00 | 89.9 | 73.0 |
| Bench 3 | Bench | Chris Wood | FWD | 16 | 7.5 | 3.81 | 11.34 | 19.69 | 2.00 | 64.3 | 63.0 |
| Bench 4 | Bench | Wilson Isidor | FWD | 17 | 5.5 | 3.17 | 9.22 | 15.12 | 1.00 | 65.6 | 58.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 7.6 | 6.28 | 19.14 | 29.83 | 18.00 | 93.1 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 5.68 | 17.24 | 29.87 | 2.00 | 78.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.20 | 14.39 | 22.55 | 3.00 | 69.5 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 4.38 | 13.37 | 20.78 | 3.00 | 76.4 | 75.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.6 | 4.53 | 13.15 | 20.72 | 12.00 | 76.9 | 89.0 |

## GW8

- Train rows: 166350
- Bank: 0.80 -> 0.70
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Mohamed Salah
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 68.60
- Actual score: 51.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.99) beats the best remaining Triple Captain opportunity (8.57).
- Transfer: Virgil van Dijk -> Gabriel dos Santos Magalhães (projected gain 4.89, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.99) beats the best remaining Triple Captain opportunity (8.57).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 3.96 | 12.07 | 20.38 | 6.00 | 87.4 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.83 | 11.07 | 18.55 | 9.00 | 97.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.2 | 5.12 | 15.96 | 23.54 | 12.00 | 90.5 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 4.75 | 15.44 | 22.81 | 2.00 | 81.5 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 4.7 | 5.29 | 13.26 | 24.92 | 4.00 | 97.3 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.32 | 11.94 | 20.41 | 0.00 | 91.8 | 90.0 |
| Bench 4 | Bench | Trevoh Chalobah | DEF | 7 | 5.1 | 2.22 | 7.36 | 13.79 | 6.00 | 35.7 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.70 | 13.98 | 25.60 | 2.00 | 78.4 | 90.0 |
| Bench 3 | Bench | Chris Wood | FWD | 16 | 7.4 | 3.23 | 10.21 | 16.74 | 1.00 | 53.7 | 16.0 |
| Bench 2 | Bench | Wilson Isidor | FWD | 17 | 5.5 | 3.29 | 8.66 | 14.42 | 2.00 | 59.8 | 75.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 7.7 | 6.96 | 19.79 | 32.94 | 4.00 | 105.7 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 5.49 | 17.03 | 28.97 | 2.00 | 74.3 | 84.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.6 | 5.13 | 15.12 | 22.98 | 2.00 | 88.7 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.49 | 15.11 | 22.26 | 8.00 | 75.9 | 84.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 4.46 | 12.16 | 21.19 | 1.00 | 77.7 | 58.0 |

## GW9

- Train rows: 167095
- Bank: 0.70 -> 3.50
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Junior Kroupi
- Effective captain: Antoine Semenyo
- Chip used: bench_boost
- Predicted score: 78.60
- Actual score: 91.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (14.96) beats the best remaining Bench Boost opportunity (0.00).
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Chris Wood -> Junior Kroupi (projected gain 3.31, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (14.96) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 4.04 | 11.86 | 19.90 | 6.00 | 86.5 | 90.0 |
| Bench 1 | Bench Boost | Martin Dúbravka | GK | 3 | 4.0 | 3.97 | 11.57 | 19.39 | 2.00 | 100.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.2 | 5.45 | 16.22 | 25.35 | 9.00 | 93.9 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 5.34 | 16.10 | 24.14 | 5.00 | 99.2 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 4.8 | 4.99 | 15.60 | 25.59 | 4.00 | 96.6 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.10 | 12.17 | 19.68 | 23.00 | 90.0 | 90.0 |
| Bench 3 | Bench Boost | Trevoh Chalobah | DEF | 7 | 5.1 | 3.83 | 10.89 | 17.91 | 1.00 | 65.8 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 5.58 | 16.30 | 27.05 | 2.00 | 89.5 | 84.0 |
| Vice Captain | XI | Junior Kroupi | FWD | 4 | 4.5 | 6.59 | 15.24 | 21.98 | 12.00 | 123.4 | 136.0 |
| Bench 4 | Bench Boost | Wilson Isidor | FWD | 17 | 5.5 | 2.73 | 8.12 | 13.85 | 7.00 | 58.4 | 74.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 7.8 | 6.85 | 20.33 | 32.45 | 3.00 | 98.8 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.4 | 5.09 | 15.71 | 27.65 | 6.00 | 67.6 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.91 | 14.38 | 21.98 | 3.00 | 81.3 | 77.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.33 | 12.82 | 20.47 | 4.00 | 76.0 | 90.0 |
| Bench 2 | Bench Boost | Tijjani Reijnders | MID | 13 | 5.7 | 3.95 | 12.03 | 19.91 | 1.00 | 65.7 | 75.0 |