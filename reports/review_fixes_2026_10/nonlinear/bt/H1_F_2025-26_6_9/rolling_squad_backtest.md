# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW5
- Simulated weeks: GW6-GW9
- Total predicted points: 242.57
- Total actual points: 237.00
- Average predicted points: 60.64
- Average actual points: 59.25
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
- Vice captain: Mohammed Kudus
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 59.54
- Actual score: 29.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martín | GK | 1 | 5.6 | 3.71 | 11.62 | 19.86 | 2.00 | 86.2 | 90.0 |
| XI | XI | Gianluigi Donnarumma | GK | 13 | 5.6 | 4.36 | 11.13 | 18.35 | 2.00 | 87.0 | 90.0 |
| Bench 2 | Bench | Marcos Senesi Barón | DEF | 4 | 4.8 | 3.85 | 14.77 | 21.11 | 7.00 | 86.1 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.2 | 3.90 | 13.86 | 21.01 | -3.00 | 84.2 | 52.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 4.60 | 12.33 | 20.27 | 13.00 | 85.0 | 90.0 |
| Bench 3 | Bench | Marc Guéhi | DEF | 8 | 4.7 | 3.77 | 11.72 | 19.03 | 7.00 | 85.1 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.36 | 11.60 | 19.22 | 2.00 | 81.9 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 5.36 | 16.70 | 28.05 | 2.00 | 83.4 | 90.0 |
| XI | XI | Richarlison de Andrade | FWD | 18 | 6.8 | 5.15 | 12.76 | 21.23 | 2.00 | 78.1 | 90.0 |
| Bench 4 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.21 | 8.26 | 14.66 | 2.00 | 79.6 | 79.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.5 | 5.11 | 19.27 | 33.76 | 2.00 | 77.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.33 | 18.33 | 28.73 | 7.00 | 86.9 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.61 | 17.17 | 28.02 | -1.00 | 84.9 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 4.76 | 14.98 | 24.05 | 2.00 | 85.1 | 82.0 |
| Vice Captain | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.38 | 14.36 | 24.10 | 2.00 | 82.3 | 90.0 |

## GW7

- Train rows: 165607
- Bank: 0.10 -> 0.40
- Free transfers: 2 -> 2
- Captain: Gabriel dos Santos Magalhães
- Vice captain: Bruno Borges Fernandes
- Effective captain: Gabriel dos Santos Magalhães
- Chip used: none
- Predicted score: 52.21
- Actual score: 69.00
- Transfer: Tijjani Reijnders -> Elliot Anderson (projected gain 0.12, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 4.53 | 11.46 | 18.63 | 6.00 | 88.3 | 90.0 |
| Bench 1 | Bench | Gianluigi Donnarumma | GK | 13 | 5.6 | 4.15 | 8.43 | 13.81 | 6.00 | 88.3 | 90.0 |
| Captain | Captain | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 5.02 | 15.25 | 22.19 | 9.00 | 85.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 4.26 | 15.21 | 20.45 | 2.00 | 88.2 | 77.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.7 | 3.58 | 14.78 | 21.60 | 3.00 | 85.6 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 3.42 | 10.72 | 16.99 | 2.00 | 83.7 | 90.0 |
| Bench 4 | Bench | Trevoh Chalobah | DEF | 7 | 5.2 | 1.45 | 9.14 | 13.75 | 0.00 | 9.9 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.73 | 13.11 | 21.70 | 2.00 | 67.5 | 73.0 |
| Bench 2 | Bench | Richarlison de Andrade | FWD | 18 | 6.8 | 3.01 | 9.58 | 15.58 | 1.00 | 74.5 | 16.0 |
| Bench 3 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.68 | 7.57 | 11.97 | 1.00 | 74.1 | 68.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 4.93 | 18.77 | 28.15 | 18.00 | 88.2 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.5 | 4.26 | 17.67 | 30.29 | 2.00 | 77.9 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.95 | 13.50 | 21.21 | 3.00 | 69.1 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 3.97 | 12.15 | 19.16 | 12.00 | 84.8 | 89.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.56 | 11.19 | 15.32 | 1.00 | 84.1 | 90.0 |

## GW8

- Train rows: 166350
- Bank: 0.40 -> 1.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Mohammed Kudus
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 65.91
- Actual score: 56.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.84) beats the best remaining Triple Captain opportunity (9.24).
- Transfer: Trevoh Chalobah -> Omar Alderete (projected gain 4.98, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.84) beats the best remaining Triple Captain opportunity (9.24).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martín | GK | 1 | 5.6 | 3.61 | 11.23 | 18.42 | 6.00 | 90.5 | 90.0 |
| XI | XI | Gianluigi Donnarumma | GK | 13 | 5.6 | 3.89 | 9.54 | 15.67 | 6.00 | 84.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.2 | 4.49 | 15.84 | 22.61 | 12.00 | 86.6 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 3.74 | 14.27 | 20.21 | 2.00 | 82.8 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.02 | 11.62 | 21.63 | 4.00 | 86.9 | 90.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.1 | 4.03 | 11.32 | 15.24 | 6.00 | 80.2 | 90.0 |
| Bench 2 | Bench | Micky van de Ven | DEF | 18 | 4.7 | 3.35 | 9.76 | 16.58 | 0.00 | 78.8 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.11 | 12.52 | 22.54 | 2.00 | 75.0 | 90.0 |
| Bench 4 | Bench | Richarlison de Andrade | FWD | 18 | 6.7 | 1.59 | 7.93 | 12.65 | 1.00 | 39.9 | 30.0 |
| Bench 3 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.93 | 5.95 | 12.04 | 0.00 | 61.2 | 0.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.8 | 4.94 | 20.46 | 32.91 | 4.00 | 86.9 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.4 | 7.81 | 17.13 | 29.34 | 2.00 | 84.8 | 84.0 |
| Vice Captain | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.01 | 15.97 | 23.92 | 2.00 | 86.7 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.50 | 14.20 | 20.99 | 8.00 | 79.3 | 84.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.76 | 10.14 | 15.59 | 4.00 | 74.1 | 90.0 |

## GW9

- Train rows: 167095
- Bank: 1.40 -> 0.20
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Marcos Senesi Barón
- Effective captain: Antoine Semenyo
- Chip used: bench_boost
- Predicted score: 64.90
- Actual score: 83.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.31) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Elliot Anderson -> Iliman Ndiaye (projected gain 3.83, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.31) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 4.04 | 11.49 | 18.74 | 6.00 | 87.8 | 90.0 |
| Bench 1 | Bench Boost | Gianluigi Donnarumma | GK | 13 | 5.6 | 3.50 | 9.44 | 15.67 | 2.00 | 86.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.2 | 4.89 | 16.31 | 24.78 | 9.00 | 86.0 | 90.0 |
| Vice Captain | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 5.00 | 14.78 | 21.38 | 5.00 | 84.3 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 2.60 | 13.51 | 21.88 | 4.00 | 86.7 | 90.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.1 | 2.99 | 10.05 | 15.10 | 0.00 | 68.6 | 0.0 |
| Bench 2 | Bench Boost | Micky van de Ven | DEF | 18 | 4.7 | 2.45 | 9.69 | 15.50 | 23.00 | 75.3 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.74 | 13.06 | 21.76 | 2.00 | 71.9 | 84.0 |
| Bench 3 | Bench Boost | Richarlison de Andrade | FWD | 18 | 6.6 | 1.80 | 7.43 | 12.37 | 4.00 | 35.4 | 28.0 |
| Bench 4 | Bench Boost | Lyle Foster | FWD | 3 | 5.0 | 1.52 | 3.31 | 7.60 | 7.00 | 26.5 | 13.0 |
| Captain | Captain | Antoine Semenyo | MID | 4 | 7.9 | 6.10 | 19.28 | 30.00 | 3.00 | 86.6 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.3 | 4.95 | 15.21 | 27.40 | 6.00 | 68.9 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.96 | 14.65 | 21.91 | 2.00 | 83.4 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.71 | 13.48 | 21.43 | 4.00 | 87.4 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.54 | 13.03 | 20.04 | 3.00 | 84.5 | 77.0 |