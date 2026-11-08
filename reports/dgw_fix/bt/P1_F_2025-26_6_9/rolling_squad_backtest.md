# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW5
- Simulated weeks: GW6-GW9
- Total predicted points: 267.57
- Total actual points: 251.00
- Average predicted points: 66.89
- Average actual points: 62.75
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
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 64.60
- Actual score: 28.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martín | GK | 1 | 5.6 | 3.85 | 11.62 | 19.86 | 2.00 | 90.0 | 90.0 |
| XI | XI | Gianluigi Donnarumma | GK | 13 | 5.6 | 4.04 | 11.13 | 18.35 | 2.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.30 | 14.77 | 21.11 | 7.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Trevoh Chalobah | DEF | 7 | 5.2 | 3.49 | 13.86 | 21.01 | -3.00 | 90.0 | 52.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.86 | 12.41 | 20.02 | 2.00 | 71.8 | 90.0 |
| Bench 2 | Bench | Marc Guéhi | DEF | 8 | 4.7 | 3.53 | 11.72 | 19.03 | 7.00 | 86.5 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.34 | 11.60 | 19.22 | 2.00 | 80.4 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.10 | 16.70 | 28.05 | 2.00 | 90.0 | 90.0 |
| XI | XI | Richarlison de Andrade | FWD | 18 | 6.8 | 4.57 | 12.76 | 21.23 | 2.00 | 71.2 | 90.0 |
| Bench 4 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.82 | 8.26 | 14.66 | 2.00 | 78.5 | 79.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.5 | 5.99 | 19.27 | 33.76 | 2.00 | 84.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 6.01 | 18.33 | 28.73 | 7.00 | 90.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.0 | 6.31 | 17.17 | 28.02 | -1.00 | 88.8 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 5.38 | 14.98 | 24.05 | 2.00 | 90.0 | 82.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.38 | 14.36 | 24.10 | 2.00 | 86.1 | 90.0 |

## GW7

- Train rows: 165607
- Bank: 0.10 -> 1.20
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Mohamed Salah
- Effective captain: Antoine Semenyo
- Chip used: none
- Predicted score: 57.18
- Actual score: 70.00
- Transfer: Trevoh Chalobah -> Omar Alderete (projected gain 2.48, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.98 | 11.46 | 18.63 | 6.00 | 83.6 | 90.0 |
| Bench 1 | Bench | Gianluigi Donnarumma | GK | 13 | 5.6 | 2.63 | 8.43 | 13.81 | 6.00 | 69.7 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.06 | 15.21 | 20.45 | 2.00 | 85.6 | 77.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.7 | 4.64 | 14.78 | 21.60 | 3.00 | 90.0 | 90.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.1 | 4.31 | 13.12 | 18.28 | 0.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.04 | 12.45 | 18.53 | 1.00 | 84.1 | 90.0 |
| Bench 2 | Bench | Micky van de Ven | DEF | 18 | 4.7 | 3.57 | 10.72 | 16.99 | 2.00 | 79.7 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.05 | 13.11 | 21.70 | 2.00 | 71.6 | 73.0 |
| Bench 3 | Bench | Richarlison de Andrade | FWD | 18 | 6.8 | 2.95 | 9.58 | 15.58 | 1.00 | 52.7 | 16.0 |
| Bench 4 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.45 | 7.57 | 11.97 | 1.00 | 65.5 | 68.0 |
| Captain | Captain | Antoine Semenyo | MID | 4 | 7.7 | 6.30 | 18.77 | 28.15 | 18.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 5.86 | 17.67 | 30.29 | 2.00 | 78.5 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.81 | 13.50 | 21.21 | 3.00 | 64.6 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.20 | 12.15 | 19.16 | 12.00 | 72.9 | 89.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 3.62 | 11.07 | 16.62 | 3.00 | 65.5 | 75.0 |

## GW8

- Train rows: 166350
- Bank: 1.20 -> 1.00
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Mohamed Salah
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 67.57
- Actual score: 57.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.26) beats the best remaining Triple Captain opportunity (8.91).
- Transfer: Virgil van Dijk -> Gabriel dos Santos Magalhães (projected gain 6.15, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (7.26) beats the best remaining Triple Captain opportunity (8.91).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.84 | 11.23 | 18.42 | 6.00 | 85.5 | 90.0 |
| Bench 1 | Bench | Gianluigi Donnarumma | GK | 13 | 5.6 | 3.25 | 9.54 | 15.67 | 6.00 | 80.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 5.33 | 15.84 | 22.61 | 12.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.31 | 14.27 | 20.21 | 2.00 | 77.5 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.70 | 11.62 | 21.63 | 4.00 | 90.0 | 90.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.1 | 3.79 | 11.32 | 15.24 | 6.00 | 70.8 | 90.0 |
| Bench 2 | Bench | Micky van de Ven | DEF | 18 | 4.7 | 3.65 | 9.76 | 16.58 | 0.00 | 83.8 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.59 | 12.52 | 22.54 | 2.00 | 76.7 | 90.0 |
| Bench 4 | Bench | Richarlison de Andrade | FWD | 18 | 6.7 | 2.46 | 7.93 | 12.65 | 1.00 | 38.6 | 30.0 |
| Bench 3 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.49 | 5.95 | 12.04 | 0.00 | 56.5 | 0.0 |
| Captain | Captain | Antoine Semenyo | MID | 4 | 7.8 | 7.24 | 20.46 | 32.91 | 4.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.4 | 5.74 | 17.13 | 29.34 | 2.00 | 76.6 | 84.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.57 | 15.97 | 23.92 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.04 | 14.20 | 20.99 | 8.00 | 69.0 | 84.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 3.94 | 10.49 | 18.19 | 1.00 | 71.5 | 58.0 |

## GW9

- Train rows: 167095
- Bank: 1.00 -> 1.50
- Free transfers: 2 -> 2
- Captain: Junior Kroupi
- Vice captain: Antoine Semenyo
- Effective captain: Junior Kroupi
- Chip used: bench_boost
- Predicted score: 78.23
- Actual score: 96.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (12.18) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Lyle Foster -> Junior Kroupi (projected gain 5.88, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (12.18) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 4.00 | 11.49 | 18.74 | 6.00 | 86.6 | 90.0 |
| Bench 1 | Bench Boost | Gianluigi Donnarumma | GK | 13 | 5.6 | 2.99 | 9.44 | 15.67 | 2.00 | 80.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 5.70 | 16.31 | 24.78 | 9.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 5.10 | 14.78 | 21.38 | 5.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.27 | 13.51 | 21.88 | 4.00 | 90.0 | 90.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.1 | 3.39 | 10.05 | 15.10 | 0.00 | 75.2 | 0.0 |
| Bench 2 | Bench Boost | Micky van de Ven | DEF | 18 | 4.7 | 3.38 | 9.69 | 15.50 | 23.00 | 80.6 | 90.0 |
| Captain | Captain | Junior Kroupi | FWD | 4 | 4.5 | 9.21 | 13.08 | 18.58 | 12.00 | 167.6 | 136.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.64 | 13.06 | 21.76 | 2.00 | 79.2 | 84.0 |
| Bench 4 | Bench Boost | Richarlison de Andrade | FWD | 18 | 6.6 | 2.26 | 7.43 | 12.37 | 4.00 | 38.2 | 28.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.9 | 6.86 | 19.28 | 30.00 | 3.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.3 | 5.08 | 15.21 | 27.40 | 6.00 | 66.7 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.65 | 13.48 | 21.43 | 4.00 | 80.5 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.42 | 13.03 | 20.04 | 3.00 | 75.9 | 77.0 |
| Bench 3 | Bench Boost | Tijjani Reijnders | MID | 13 | 5.7 | 3.06 | 9.51 | 15.80 | 1.00 | 55.2 | 75.0 |