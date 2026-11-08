# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW5
- Simulated weeks: GW6-GW9
- Total predicted points: 267.42
- Total actual points: 243.00
- Average predicted points: 66.86
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
- Bank: 100.00 -> 0.30
- Free transfers: 1 -> 2
- Captain: Antoine Semenyo
- Vice captain: Bruno Borges Fernandes
- Effective captain: Antoine Semenyo
- Chip used: none
- Predicted score: 64.97
- Actual score: 47.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 4.17 | 12.09 | 20.95 | 2.00 | 97.5 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.20 | 10.04 | 17.77 | 1.00 | 100.5 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.77 | 15.11 | 22.23 | 7.00 | 100.9 | 90.0 |
| Bench 3 | Bench | Trevoh Chalobah | DEF | 7 | 5.2 | 3.41 | 13.69 | 21.49 | -3.00 | 99.8 | 52.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 4.11 | 12.71 | 21.45 | 13.00 | 96.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 5.03 | 12.65 | 21.05 | 2.00 | 72.1 | 90.0 |
| Bench 2 | Bench | Marc Guéhi | DEF | 8 | 4.7 | 3.79 | 12.11 | 20.25 | 7.00 | 88.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 5.92 | 16.59 | 28.61 | 2.00 | 94.5 | 90.0 |
| XI | XI | Richarlison de Andrade | FWD | 18 | 6.8 | 4.47 | 12.65 | 21.71 | 2.00 | 72.8 | 90.0 |
| Bench 4 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.82 | 8.22 | 15.34 | 2.00 | 77.5 | 79.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.5 | 5.95 | 19.67 | 34.87 | 2.00 | 83.4 | 90.0 |
| Captain | Captain | Antoine Semenyo | MID | 4 | 7.7 | 6.36 | 18.63 | 29.84 | 7.00 | 99.3 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 6.10 | 16.60 | 28.10 | -1.00 | 88.4 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 5.50 | 14.89 | 24.62 | 2.00 | 104.9 | 82.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.24 | 14.23 | 24.66 | 2.00 | 86.6 | 90.0 |

## GW7

- Train rows: 165607
- Bank: 0.30 -> 1.40
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Mohamed Salah
- Effective captain: Antoine Semenyo
- Chip used: none
- Predicted score: 59.11
- Actual score: 76.00
- Transfer: Trevoh Chalobah -> Omar Alderete (projected gain 2.13, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 4.04 | 11.50 | 18.93 | 6.00 | 86.0 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.19 | 9.77 | 16.47 | 2.00 | 96.4 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.31 | 15.33 | 20.77 | 2.00 | 88.9 | 77.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.7 | 5.01 | 15.04 | 22.08 | 3.00 | 104.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 5.41 | 15.04 | 21.99 | 9.00 | 98.4 | 90.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.1 | 4.16 | 12.83 | 18.09 | 0.00 | 93.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.81 | 12.24 | 18.36 | 1.00 | 81.9 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 3.74 | 13.09 | 21.78 | 2.00 | 65.8 | 73.0 |
| Bench 3 | Bench | Richarlison de Andrade | FWD | 18 | 6.8 | 2.85 | 9.66 | 15.87 | 1.00 | 51.9 | 16.0 |
| Bench 4 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.52 | 7.69 | 12.23 | 1.00 | 66.3 | 68.0 |
| Captain | Captain | Antoine Semenyo | MID | 4 | 7.7 | 6.53 | 18.95 | 28.48 | 18.00 | 100.7 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 5.52 | 17.42 | 30.18 | 2.00 | 75.9 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.90 | 13.64 | 21.40 | 3.00 | 64.1 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.14 | 12.22 | 19.33 | 12.00 | 73.1 | 89.0 |
| Bench 2 | Bench | Tijjani Reijnders | MID | 13 | 5.7 | 3.49 | 10.79 | 16.36 | 3.00 | 63.2 | 75.0 |

## GW8

- Train rows: 166350
- Bank: 1.40 -> 0.80
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Mohammed Kudus
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 70.00
- Actual score: 59.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.68) beats the best remaining Triple Captain opportunity (9.42).
- Transfer: Richarlison de Andrade -> Nick Woltemade (projected gain 3.95, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (7.68) beats the best remaining Triple Captain opportunity (9.42).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.87 | 11.33 | 18.68 | 6.00 | 87.6 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.59 | 9.91 | 16.22 | 9.00 | 97.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.2 | 5.20 | 15.63 | 22.25 | 12.00 | 91.8 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.49 | 14.32 | 20.23 | 2.00 | 78.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.92 | 11.79 | 21.92 | 4.00 | 94.9 | 90.0 |
| Bench 3 | Bench | Omar Alderete | DEF | 17 | 4.1 | 3.74 | 11.48 | 15.49 | 6.00 | 71.3 | 90.0 |
| Bench 2 | Bench | Virgil van Dijk | DEF | 12 | 6.1 | 3.78 | 9.77 | 18.01 | 3.00 | 86.1 | 90.0 |
| XI | XI | Nick Woltemade | FWD | 15 | 7.3 | 5.01 | 13.63 | 21.88 | 8.00 | 89.9 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.47 | 12.68 | 22.82 | 2.00 | 77.1 | 90.0 |
| Bench 4 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.48 | 5.82 | 11.98 | 0.00 | 55.7 | 0.0 |
| Captain | Captain | Antoine Semenyo | MID | 4 | 7.8 | 7.65 | 20.56 | 33.00 | 4.00 | 120.9 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.4 | 5.39 | 17.35 | 29.64 | 2.00 | 73.8 | 84.0 |
| Vice Captain | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.81 | 16.28 | 24.25 | 2.00 | 102.2 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 3.98 | 14.06 | 20.74 | 8.00 | 67.1 | 84.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 3.91 | 10.54 | 18.27 | 1.00 | 71.2 | 58.0 |

## GW9

- Train rows: 167095
- Bank: 0.80 -> 0.00
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Nick Woltemade
- Effective captain: Antoine Semenyo
- Chip used: bench_boost
- Predicted score: 73.34
- Actual score: 61.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (12.10) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Tijjani Reijnders -> Iliman Ndiaye (projected gain 2.85, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (12.10) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 4.02 | 11.56 | 18.90 | 6.00 | 88.1 | 90.0 |
| Bench 1 | Bench Boost | Martin Dúbravka | GK | 3 | 4.0 | 3.52 | 10.03 | 16.59 | 2.00 | 97.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.2 | 5.59 | 16.06 | 24.35 | 9.00 | 96.5 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 5.00 | 14.80 | 21.39 | 5.00 | 94.7 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.47 | 13.84 | 22.24 | 4.00 | 93.2 | 90.0 |
| Bench 2 | Bench Boost | Virgil van Dijk | DEF | 12 | 6.0 | 4.04 | 11.99 | 18.97 | 3.00 | 88.1 | 90.0 |
| Bench 3 | Bench Boost | Omar Alderete | DEF | 17 | 4.1 | 3.34 | 10.25 | 15.41 | 0.00 | 74.6 | 0.0 |
| Vice Captain | XI | Nick Woltemade | FWD | 15 | 7.3 | 5.62 | 15.20 | 22.78 | 2.00 | 88.9 | 85.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.55 | 13.25 | 22.03 | 2.00 | 78.2 | 84.0 |
| Bench 4 | Bench Boost | Lyle Foster | FWD | 3 | 5.0 | 1.17 | 3.39 | 7.77 | 7.00 | 25.9 | 13.0 |
| Captain | Captain | Antoine Semenyo | MID | 4 | 7.9 | 6.62 | 19.26 | 30.04 | 3.00 | 99.8 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.3 | 4.73 | 15.42 | 27.64 | 6.00 | 62.6 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 5.11 | 14.73 | 21.99 | 2.00 | 84.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.56 | 13.47 | 21.27 | 4.00 | 78.5 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.38 | 13.15 | 20.13 | 3.00 | 75.0 | 77.0 |