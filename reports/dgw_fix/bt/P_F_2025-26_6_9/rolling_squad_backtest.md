# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW5
- Simulated weeks: GW6-GW9
- Total predicted points: 271.01
- Total actual points: 266.00
- Average predicted points: 67.75
- Average actual points: 66.50
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
- Bank: 100.00 -> 0.30
- Free transfers: 1 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 64.41
- Actual score: 28.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.85 | 11.46 | 19.54 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.18 | 9.92 | 17.07 | 1.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.30 | 14.20 | 20.21 | 7.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Trevoh Chalobah | DEF | 7 | 5.2 | 3.49 | 13.74 | 20.54 | -3.00 | 90.0 | 52.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.86 | 12.50 | 19.92 | 2.00 | 71.8 | 90.0 |
| Bench 2 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 3.84 | 12.27 | 19.93 | 13.00 | 90.0 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.34 | 11.47 | 18.79 | 2.00 | 80.4 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.10 | 16.86 | 28.18 | 2.00 | 90.0 | 90.0 |
| XI | XI | Richarlison de Andrade | FWD | 18 | 6.8 | 4.57 | 12.37 | 20.42 | 2.00 | 71.2 | 90.0 |
| Bench 4 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.82 | 8.13 | 14.19 | 2.00 | 78.5 | 79.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.5 | 5.99 | 19.92 | 34.54 | 2.00 | 84.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 6.01 | 17.56 | 27.46 | 7.00 | 90.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.0 | 6.31 | 16.76 | 27.22 | -1.00 | 88.8 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 5.38 | 14.67 | 23.37 | 2.00 | 90.0 | 82.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.38 | 14.16 | 23.61 | 2.00 | 86.1 | 90.0 |

## GW7

- Train rows: 165607
- Bank: 0.30 -> 0.70
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Mohamed Salah
- Effective captain: Antoine Semenyo
- Chip used: none
- Predicted score: 58.36
- Actual score: 79.00
- Transfer: Trevoh Chalobah -> Marc Guéhi (projected gain 3.83, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.98 | 11.20 | 18.24 | 6.00 | 83.6 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.11 | 9.49 | 15.81 | 2.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 5.48 | 15.26 | 22.15 | 9.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.06 | 14.63 | 19.50 | 2.00 | 85.6 | 77.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.64 | 14.41 | 21.07 | 3.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.04 | 12.79 | 18.86 | 1.00 | 84.1 | 90.0 |
| Bench 2 | Bench | Micky van de Ven | DEF | 18 | 4.7 | 3.57 | 10.67 | 16.88 | 2.00 | 79.7 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.05 | 13.65 | 22.23 | 2.00 | 71.6 | 73.0 |
| Bench 3 | Bench | Richarlison de Andrade | FWD | 18 | 6.8 | 2.95 | 9.18 | 14.83 | 1.00 | 52.7 | 16.0 |
| Bench 4 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.45 | 7.36 | 11.54 | 1.00 | 65.5 | 68.0 |
| Captain | Captain | Antoine Semenyo | MID | 4 | 7.7 | 6.30 | 18.42 | 27.75 | 18.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 5.86 | 17.90 | 30.34 | 2.00 | 78.5 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.81 | 13.29 | 20.69 | 3.00 | 64.6 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.20 | 11.98 | 18.80 | 12.00 | 72.9 | 89.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 3.62 | 10.81 | 16.24 | 3.00 | 65.5 | 75.0 |

## GW8

- Train rows: 166350
- Bank: 0.70 -> 0.90
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Mohamed Salah
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 68.54
- Actual score: 57.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.26) beats the best remaining Triple Captain opportunity (8.91).
- Transfer: Virgil van Dijk -> Jurriën Timber (projected gain 2.99, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (7.26) beats the best remaining Triple Captain opportunity (8.91).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.84 | 11.11 | 18.30 | 6.00 | 85.5 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.60 | 9.89 | 16.21 | 9.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.2 | 5.33 | 15.82 | 22.55 | 12.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.31 | 14.05 | 19.73 | 2.00 | 77.5 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 5.9 | 4.76 | 13.01 | 19.32 | 6.00 | 81.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.70 | 11.48 | 21.25 | 4.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Micky van de Ven | DEF | 18 | 4.7 | 3.65 | 9.93 | 16.75 | 0.00 | 83.8 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.59 | 12.54 | 22.38 | 2.00 | 76.7 | 90.0 |
| Bench 4 | Bench | Richarlison de Andrade | FWD | 18 | 6.7 | 2.46 | 8.01 | 12.61 | 1.00 | 38.6 | 30.0 |
| Bench 3 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.49 | 5.86 | 11.80 | 0.00 | 56.5 | 0.0 |
| Captain | Captain | Antoine Semenyo | MID | 4 | 7.8 | 7.24 | 20.38 | 33.02 | 4.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.4 | 5.74 | 17.42 | 29.33 | 2.00 | 76.6 | 84.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.57 | 15.88 | 23.81 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.04 | 14.22 | 20.98 | 8.00 | 69.0 | 84.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 3.94 | 10.49 | 18.21 | 1.00 | 71.5 | 58.0 |

## GW9

- Train rows: 167095
- Bank: 0.90 -> 1.40
- Free transfers: 2 -> 2
- Captain: Junior Kroupi
- Vice captain: Antoine Semenyo
- Effective captain: Junior Kroupi
- Chip used: bench_boost
- Predicted score: 79.70
- Actual score: 102.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (12.69) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Lyle Foster -> Junior Kroupi (projected gain 8.16, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (12.69) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 4.00 | 11.42 | 18.73 | 6.00 | 86.6 | 90.0 |
| Bench 1 | Bench Boost | Martin Dúbravka | GK | 3 | 4.0 | 3.51 | 9.96 | 16.45 | 2.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.2 | 5.70 | 16.53 | 25.06 | 9.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 5.10 | 14.90 | 21.39 | 5.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.27 | 13.51 | 21.70 | 4.00 | 90.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 5.9 | 4.34 | 12.02 | 18.63 | 6.00 | 71.8 | 90.0 |
| Bench 2 | Bench Boost | Micky van de Ven | DEF | 18 | 4.7 | 3.38 | 9.86 | 15.66 | 23.00 | 80.6 | 90.0 |
| Captain | Captain | Junior Kroupi | FWD | 4 | 4.5 | 9.21 | 15.53 | 20.35 | 12.00 | 167.6 | 136.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.64 | 13.20 | 21.83 | 2.00 | 79.2 | 84.0 |
| Bench 4 | Bench Boost | Richarlison de Andrade | FWD | 18 | 6.6 | 2.26 | 7.47 | 12.28 | 4.00 | 38.2 | 28.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.9 | 6.86 | 19.43 | 30.24 | 3.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.3 | 5.08 | 15.48 | 27.33 | 6.00 | 66.7 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.65 | 13.44 | 21.17 | 4.00 | 80.5 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.42 | 13.09 | 20.03 | 3.00 | 75.9 | 77.0 |
| Bench 3 | Bench Boost | Tijjani Reijnders | MID | 13 | 5.7 | 3.06 | 9.42 | 15.64 | 1.00 | 55.2 | 75.0 |