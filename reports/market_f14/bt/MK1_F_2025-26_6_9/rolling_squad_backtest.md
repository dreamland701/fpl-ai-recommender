# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW5
- Simulated weeks: GW6-GW9
- Total predicted points: 280.56
- Total actual points: 295.00
- Average predicted points: 70.14
- Average actual points: 73.75
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
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 69.17
- Actual score: 57.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Gianluigi Donnarumma | GK | 13 | 5.6 | 4.36 | 12.13 | 19.67 | 2.00 | 88.9 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.9 | 0.13 | 0.55 | 2.00 | 0.00 | 4.9 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.15 | 14.17 | 20.46 | 7.00 | 90.0 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.2 | 3.42 | 13.68 | 20.83 | -3.00 | 90.0 | 52.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.27 | 11.36 | 18.70 | 2.00 | 81.1 | 90.0 |
| Bench 3 | Bench | Omar Alderete | DEF | 17 | 4.0 | 2.01 | 9.54 | 14.20 | 17.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Joe Rodon | DEF | 11 | 4.0 | 3.42 | 8.85 | 14.09 | 7.00 | 77.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 9.41 | 25.71 | 40.99 | 16.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 5.86 | 16.09 | 27.19 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 1.66 | 3.75 | 7.07 | 12.00 | 25.2 | 18.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 5.96 | 19.22 | 33.50 | 2.00 | 85.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.89 | 17.73 | 28.13 | 7.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 5.63 | 15.78 | 24.86 | 2.00 | 90.0 | 82.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.50 | 14.21 | 22.19 | 2.00 | 90.0 | 80.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.31 | 14.07 | 23.50 | 2.00 | 86.8 | 90.0 |

## GW7

- Train rows: 165607
- Bank: 0.10 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 60.12
- Actual score: 71.00
- Transfer: Trevoh Chalobah -> Marc Guéhi (projected gain 4.46, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Gianluigi Donnarumma | GK | 13 | 5.6 | 2.73 | 8.90 | 14.47 | 6.00 | 69.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.9 | 0.00 | 0.09 | 0.60 | 0.00 | 1.4 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.03 | 14.94 | 20.03 | 2.00 | 86.4 | 77.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.54 | 14.12 | 20.71 | 3.00 | 90.0 | 90.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.0 | 4.02 | 12.21 | 17.20 | 0.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Micky van de Ven | DEF | 18 | 4.7 | 3.45 | 10.25 | 16.39 | 2.00 | 80.7 | 90.0 |
| Bench 2 | Bench | Joe Rodon | DEF | 11 | 4.0 | 3.46 | 9.70 | 13.83 | 1.00 | 78.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.46 | 24.62 | 38.40 | 8.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 3.79 | 12.66 | 21.22 | 2.00 | 73.0 | 73.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 3.00 | 5.76 | 9.21 | 0.00 | 45.1 | 0.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.7 | 6.23 | 18.33 | 27.66 | 18.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.5 | 5.56 | 17.07 | 29.62 | 2.00 | 80.1 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 3.51 | 12.25 | 18.13 | 7.00 | 67.1 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.12 | 11.81 | 18.82 | 12.00 | 74.0 | 89.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 3.66 | 11.31 | 16.93 | 3.00 | 64.9 | 75.0 |

## GW8

- Train rows: 166350
- Bank: 0.50 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 71.17
- Actual score: 72.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.35) beats the best remaining Triple Captain opportunity (9.07).
- Transfer: Tijjani Reijnders -> Moisés Caicedo Corozo (projected gain 2.24, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.35) beats the best remaining Triple Captain opportunity (9.07).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Gianluigi Donnarumma | GK | 13 | 5.6 | 3.48 | 10.16 | 16.43 | 6.00 | 79.5 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.9 | 0.03 | 0.06 | 0.53 | 0.00 | 2.8 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.15 | 13.79 | 19.74 | 2.00 | 79.1 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.72 | 11.65 | 21.44 | 4.00 | 90.0 | 90.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.0 | 3.85 | 11.07 | 14.79 | 6.00 | 71.3 | 90.0 |
| Bench 3 | Bench | Joe Rodon | DEF | 11 | 4.0 | 3.49 | 10.50 | 13.45 | 1.00 | 75.5 | 90.0 |
| Bench 2 | Bench | Micky van de Ven | DEF | 18 | 4.7 | 3.64 | 9.71 | 16.49 | 0.00 | 83.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 7.98 | 24.07 | 38.57 | 13.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.45 | 12.06 | 21.97 | 2.00 | 78.0 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 1.59 | 3.47 | 6.23 | 24.00 | 21.9 | 148.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.8 | 6.95 | 19.62 | 32.03 | 4.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.4 | 5.64 | 17.21 | 29.38 | 2.00 | 76.3 | 84.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.48 | 15.72 | 23.66 | 2.00 | 90.0 | 90.0 |
| XI | XI | Moisés Caicedo Corozo | MID | 7 | 5.8 | 4.66 | 13.24 | 19.73 | 1.00 | 89.1 | 45.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 3.83 | 12.09 | 19.89 | 4.00 | 82.6 | 85.0 |

## GW9

- Train rows: 167095
- Bank: 0.40 -> 0.30
- Free transfers: 2 -> 2
- Captain: Junior Kroupi
- Vice captain: Erling Haaland
- Effective captain: Junior Kroupi
- Chip used: bench_boost
- Predicted score: 80.09
- Actual score: 95.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.97) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Gianluigi Donnarumma -> David Raya Martín (projected gain 2.26, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.97) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.7 | 4.18 | 11.90 | 19.28 | 6.00 | 86.3 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.9 | 0.00 | 0.03 | 0.50 | 0.00 | 2.4 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 5.12 | 14.82 | 21.46 | 5.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.06 | 12.84 | 21.13 | 4.00 | 90.0 | 90.0 |
| XI | XI | Joe Rodon | DEF | 11 | 4.0 | 3.58 | 9.33 | 13.72 | 13.00 | 71.9 | 90.0 |
| Bench 4 | Bench Boost | Omar Alderete | DEF | 17 | 4.0 | 3.11 | 9.29 | 14.23 | 0.00 | 77.1 | 0.0 |
| Bench 3 | Bench Boost | Micky van de Ven | DEF | 18 | 4.7 | 3.25 | 9.28 | 14.97 | 23.00 | 81.6 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.5 | 7.78 | 24.31 | 40.43 | 2.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.85 | 13.60 | 22.35 | 2.00 | 78.1 | 84.0 |
| Captain | Captain | Junior Kroupi | FWD | 4 | 4.5 | 9.45 | 13.36 | 18.19 | 12.00 | 160.2 | 136.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.9 | 6.69 | 18.61 | 29.25 | 3.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.3 | 5.09 | 15.41 | 27.58 | 6.00 | 66.2 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 5.07 | 14.58 | 21.94 | 2.00 | 83.3 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.29 | 12.61 | 19.66 | 3.00 | 77.5 | 77.0 |
| Bench 2 | Bench Boost | Moisés Caicedo Corozo | MID | 7 | 5.8 | 4.12 | 12.43 | 17.93 | 2.00 | 64.5 | 90.0 |