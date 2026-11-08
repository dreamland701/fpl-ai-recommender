# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW5
- Simulated weeks: GW6-GW9
- Total predicted points: 259.37
- Total actual points: 207.00
- Average predicted points: 64.84
- Average actual points: 51.75
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
- Bank: 100.00 -> 0.20
- Free transfers: 1 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Antoine Semenyo
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 65.52
- Actual score: 27.00
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martín | GK | 1 | 5.6 | 3.89 | 11.51 | 19.74 | 2.00 | 95.7 | 90.0 |
| XI | XI | Gianluigi Donnarumma | GK | 13 | 5.6 | 4.20 | 11.01 | 18.22 | 2.00 | 95.4 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.64 | 14.80 | 21.16 | 7.00 | 100.2 | 90.0 |
| Bench 3 | Bench | Trevoh Chalobah | DEF | 7 | 5.2 | 3.54 | 13.89 | 21.02 | -3.00 | 99.7 | 52.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.5 | 5.04 | 12.87 | 18.63 | 1.00 | 86.1 | 90.0 |
| Bench 2 | Bench | Marc Guéhi | DEF | 8 | 4.7 | 3.62 | 11.75 | 19.03 | 7.00 | 86.5 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.39 | 11.65 | 19.32 | 2.00 | 80.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.04 | 16.74 | 28.09 | 2.00 | 94.4 | 90.0 |
| XI | XI | Richarlison de Andrade | FWD | 18 | 6.8 | 4.74 | 12.76 | 21.24 | 2.00 | 73.5 | 90.0 |
| Bench 4 | Bench | Wilson Isidor | FWD | 17 | 5.5 | 3.19 | 8.91 | 15.29 | 2.00 | 60.8 | 84.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.7 | 6.34 | 18.40 | 28.80 | 7.00 | 98.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.5 | 5.14 | 17.86 | 31.76 | 2.00 | 86.2 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.0 | 6.53 | 17.42 | 28.33 | -1.00 | 89.7 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 5.50 | 14.89 | 23.94 | 2.00 | 105.8 | 82.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.44 | 14.32 | 24.06 | 2.00 | 86.6 | 90.0 |

## GW7

- Train rows: 165607
- Bank: 0.20 -> 0.80
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Marcos Senesi Barón
- Effective captain: Antoine Semenyo
- Chip used: none
- Predicted score: 56.94
- Actual score: 74.00
- Transfer: Micky van de Ven -> Omar Alderete (projected gain 2.46, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 4.03 | 11.38 | 18.55 | 6.00 | 85.9 | 90.0 |
| Bench 1 | Bench | Gianluigi Donnarumma | GK | 13 | 5.6 | 2.62 | 8.34 | 13.72 | 6.00 | 70.9 | 90.0 |
| Vice Captain | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.24 | 15.25 | 20.55 | 2.00 | 88.0 | 77.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.7 | 4.85 | 14.79 | 21.62 | 3.00 | 101.8 | 90.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.1 | 4.36 | 13.21 | 18.47 | 0.00 | 92.3 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.5 | 4.13 | 11.28 | 16.11 | 5.00 | 77.3 | 90.0 |
| Bench 4 | Bench | Trevoh Chalobah | DEF | 7 | 5.2 | 2.58 | 9.16 | 13.79 | 0.00 | 50.4 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 3.74 | 13.17 | 21.75 | 2.00 | 66.2 | 73.0 |
| Bench 2 | Bench | Richarlison de Andrade | FWD | 18 | 6.8 | 2.90 | 9.59 | 15.60 | 1.00 | 50.9 | 16.0 |
| Bench 3 | Bench | Wilson Isidor | FWD | 17 | 5.5 | 2.82 | 7.96 | 12.56 | 1.00 | 58.2 | 58.0 |
| Captain | Captain | Antoine Semenyo | MID | 4 | 7.7 | 6.46 | 18.83 | 28.21 | 18.00 | 97.7 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.5 | 5.03 | 16.37 | 28.50 | 2.00 | 78.1 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.94 | 13.78 | 21.55 | 3.00 | 63.4 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.17 | 12.14 | 19.14 | 12.00 | 72.2 | 89.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 3.53 | 11.00 | 16.55 | 3.00 | 65.1 | 75.0 |

## GW8

- Train rows: 166350
- Bank: 0.80 -> 0.70
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Mohammed Kudus
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 66.56
- Actual score: 48.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.45) beats the best remaining Triple Captain opportunity (9.14).
- Transfer: Tijjani Reijnders -> Moisés Caicedo Corozo (projected gain 3.11, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (7.45) beats the best remaining Triple Captain opportunity (9.14).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.81 | 11.13 | 18.32 | 6.00 | 86.8 | 90.0 |
| Bench 1 | Bench | Gianluigi Donnarumma | GK | 13 | 5.6 | 3.25 | 9.42 | 15.54 | 6.00 | 82.5 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.36 | 14.30 | 20.28 | 2.00 | 78.4 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.5 | 3.44 | 12.02 | 16.93 | 3.00 | 81.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.78 | 11.65 | 21.66 | 4.00 | 93.9 | 90.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.1 | 3.80 | 11.42 | 15.43 | 6.00 | 69.3 | 90.0 |
| Bench 4 | Bench | Trevoh Chalobah | DEF | 7 | 5.1 | 2.13 | 6.39 | 11.41 | 6.00 | 30.9 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.55 | 12.60 | 22.61 | 2.00 | 75.8 | 90.0 |
| Bench 3 | Bench | Richarlison de Andrade | FWD | 18 | 6.7 | 2.30 | 7.92 | 12.67 | 1.00 | 35.7 | 30.0 |
| Bench 2 | Bench | Wilson Isidor | FWD | 17 | 5.5 | 2.96 | 7.49 | 12.24 | 2.00 | 53.6 | 75.0 |
| Captain | Captain | Antoine Semenyo | MID | 4 | 7.8 | 7.42 | 20.49 | 32.95 | 4.00 | 119.1 | 90.0 |
| Vice Captain | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.68 | 15.94 | 23.89 | 2.00 | 100.7 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.4 | 4.99 | 15.90 | 27.67 | 2.00 | 76.9 | 84.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.01 | 14.46 | 21.31 | 8.00 | 65.6 | 84.0 |
| XI | XI | Moisés Caicedo Corozo | MID | 7 | 5.8 | 4.87 | 13.51 | 19.93 | 1.00 | 90.2 | 45.0 |

## GW9

- Train rows: 167095
- Bank: 0.70 -> 1.70
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Junior Kroupi
- Effective captain: Antoine Semenyo
- Chip used: bench_boost
- Predicted score: 70.35
- Actual score: 58.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (12.28) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Wilson Isidor -> Junior Kroupi (projected gain 3.73, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (12.28) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.97 | 11.40 | 18.65 | 6.00 | 87.8 | 90.0 |
| Bench 1 | Bench Boost | Gianluigi Donnarumma | GK | 13 | 5.6 | 2.98 | 9.33 | 15.56 | 2.00 | 81.8 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 5.03 | 14.75 | 21.40 | 5.00 | 93.8 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.28 | 13.52 | 21.89 | 4.00 | 92.3 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.5 | 3.87 | 11.39 | 17.85 | 1.00 | 83.4 | 90.0 |
| Bench 3 | Bench Boost | Omar Alderete | DEF | 17 | 4.1 | 3.34 | 10.14 | 15.27 | 0.00 | 73.0 | 0.0 |
| Bench 2 | Bench Boost | Trevoh Chalobah | DEF | 7 | 5.1 | 3.39 | 9.38 | 14.92 | 1.00 | 60.1 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.49 | 13.13 | 21.84 | 2.00 | 76.6 | 84.0 |
| Vice Captain | XI | Junior Kroupi | FWD | 4 | 4.5 | 5.81 | 13.06 | 18.57 | 12.00 | 106.7 | 136.0 |
| Bench 4 | Bench Boost | Richarlison de Andrade | FWD | 18 | 6.6 | 2.09 | 7.45 | 12.41 | 4.00 | 34.6 | 28.0 |
| Captain | Captain | Antoine Semenyo | MID | 4 | 7.9 | 6.83 | 19.31 | 30.02 | 3.00 | 96.8 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.3 | 4.37 | 14.09 | 25.86 | 6.00 | 66.4 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.80 | 13.73 | 21.74 | 4.00 | 79.8 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.32 | 13.03 | 20.06 | 3.00 | 73.6 | 77.0 |
| XI | XI | Moisés Caicedo Corozo | MID | 7 | 5.8 | 3.94 | 11.64 | 16.84 | 2.00 | 67.1 | 90.0 |