# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW5
- Simulated weeks: GW6-GW9
- Total predicted points: 273.43
- Total actual points: 257.00
- Average predicted points: 68.36
- Average actual points: 64.25
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
- Captain: Erling Haaland
- Vice captain: Tijjani Reijnders
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 71.97
- Actual score: 57.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Gianluigi Donnarumma | GK | 13 | 5.6 | 5.05 | 12.13 | 19.67 | 2.00 | 105.9 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 4.0 | 0.09 | 0.43 | 1.70 | 0.00 | 4.8 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.17 | 14.17 | 20.46 | 7.00 | 92.8 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.2 | 3.49 | 13.68 | 20.83 | -3.00 | 101.4 | 52.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.26 | 11.36 | 18.70 | 2.00 | 80.5 | 90.0 |
| Bench 4 | Bench | Omar Alderete | DEF | 17 | 4.0 | 1.73 | 9.54 | 14.20 | 17.00 | 84.0 | 90.0 |
| Bench 2 | Bench | Joe Rodon | DEF | 11 | 4.0 | 3.47 | 8.85 | 14.09 | 7.00 | 76.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 10.47 | 25.71 | 40.99 | 16.00 | 120.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 5.48 | 16.09 | 27.19 | 2.00 | 88.8 | 90.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 1.82 | 3.75 | 7.07 | 12.00 | 32.9 | 18.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.5 | 5.73 | 19.22 | 33.50 | 2.00 | 83.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.67 | 17.73 | 28.13 | 7.00 | 90.8 | 90.0 |
| Vice Captain | XI | Tijjani Reijnders | MID | 13 | 5.7 | 6.35 | 15.78 | 24.86 | 2.00 | 115.8 | 82.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.53 | 14.21 | 22.19 | 2.00 | 93.1 | 80.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.30 | 14.07 | 23.50 | 2.00 | 86.7 | 90.0 |

## GW7

- Train rows: 165607
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 59.00
- Actual score: 69.00
- Transfer: Gianluigi Donnarumma -> David Raya Martín (projected gain 3.20, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 4.56 | 12.11 | 19.53 | 6.00 | 92.9 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 4.0 | 0.00 | 0.17 | 0.79 | 0.00 | 4.0 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.06 | 14.94 | 20.03 | 2.00 | 84.6 | 77.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.0 | 3.59 | 12.21 | 17.20 | 0.00 | 82.7 | 90.0 |
| Bench 2 | Bench | Micky van de Ven | DEF | 18 | 4.7 | 3.19 | 10.25 | 16.39 | 2.00 | 73.8 | 90.0 |
| XI | XI | Joe Rodon | DEF | 11 | 4.0 | 3.60 | 9.70 | 13.83 | 1.00 | 81.2 | 90.0 |
| Bench 3 | Bench | Trevoh Chalobah | DEF | 7 | 5.2 | 2.53 | 9.05 | 13.66 | 0.00 | 54.0 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.38 | 24.62 | 38.40 | 8.00 | 87.3 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 3.31 | 12.66 | 21.22 | 2.00 | 65.0 | 73.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 2.52 | 5.76 | 9.21 | 0.00 | 38.4 | 0.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.7 | 6.06 | 18.33 | 27.66 | 18.00 | 93.5 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.5 | 5.02 | 17.07 | 29.62 | 2.00 | 71.0 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 3.42 | 12.25 | 18.13 | 7.00 | 65.2 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 3.87 | 11.81 | 18.82 | 12.00 | 69.0 | 89.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 3.76 | 11.31 | 16.93 | 3.00 | 67.3 | 75.0 |

## GW8

- Train rows: 166350
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 69.90
- Actual score: 68.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.57) beats the best remaining Triple Captain opportunity (9.31).
- Transfer: Micky van de Ven -> Chris Richards (projected gain 1.56, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.57) beats the best remaining Triple Captain opportunity (9.31).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 4.12 | 11.51 | 18.70 | 6.00 | 85.7 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 4.0 | 0.00 | 0.10 | 0.67 | 0.00 | 3.0 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 3.91 | 13.79 | 19.74 | 2.00 | 73.8 | 90.0 |
| XI | XI | Chris Richards | DEF | 8 | 4.5 | 4.01 | 11.27 | 17.07 | 3.00 | 90.7 | 90.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.0 | 3.72 | 11.07 | 14.79 | 6.00 | 66.9 | 90.0 |
| XI | XI | Joe Rodon | DEF | 11 | 4.0 | 3.41 | 10.50 | 13.45 | 1.00 | 72.4 | 90.0 |
| Bench 3 | Bench | Trevoh Chalobah | DEF | 7 | 5.1 | 2.05 | 6.20 | 11.32 | 6.00 | 30.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 8.20 | 24.07 | 38.57 | 13.00 | 93.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.14 | 12.06 | 21.97 | 2.00 | 71.3 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 1.81 | 3.47 | 6.23 | 24.00 | 32.5 | 148.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.8 | 6.55 | 19.62 | 32.03 | 4.00 | 111.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.4 | 5.62 | 17.21 | 29.38 | 2.00 | 77.6 | 84.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.44 | 15.72 | 23.66 | 2.00 | 98.9 | 90.0 |
| Bench 2 | Bench | Iliman Ndiaye | MID | 9 | 6.5 | 3.32 | 12.09 | 19.89 | 4.00 | 73.3 | 85.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 4.39 | 11.00 | 18.65 | 1.00 | 76.4 | 58.0 |

## GW9

- Train rows: 167095
- Bank: 0.20 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Junior Kroupi
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 72.57
- Actual score: 63.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.09) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Trevoh Chalobah -> Marc Guéhi (projected gain 3.13, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.09) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 4.34 | 11.90 | 19.28 | 6.00 | 90.3 | 90.0 |
| Bench 1 | Bench Boost | Hákon Rafn Valdimarsson | GK | 5 | 3.9 | 0.01 | 0.00 | 0.22 | 0.00 | 4.1 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 5.09 | 14.82 | 21.46 | 5.00 | 95.4 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.9 | 3.56 | 12.84 | 21.13 | 4.00 | 84.3 | 90.0 |
| Bench 3 | Bench Boost | Chris Richards | DEF | 8 | 4.5 | 2.78 | 9.81 | 16.55 | 2.00 | 81.5 | 90.0 |
| XI | XI | Joe Rodon | DEF | 11 | 4.0 | 3.78 | 9.33 | 13.72 | 13.00 | 76.6 | 90.0 |
| Bench 4 | Bench Boost | Omar Alderete | DEF | 17 | 4.0 | 2.70 | 9.29 | 14.23 | 0.00 | 65.8 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.5 | 7.69 | 24.31 | 40.43 | 2.00 | 100.9 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.99 | 13.60 | 22.35 | 2.00 | 83.4 | 84.0 |
| Vice Captain | XI | Junior Kroupi | FWD | 4 | 4.5 | 6.66 | 13.36 | 18.19 | 12.00 | 111.3 | 136.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.9 | 6.24 | 18.61 | 29.25 | 3.00 | 89.9 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.3 | 5.04 | 15.41 | 27.58 | 6.00 | 66.3 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.99 | 14.58 | 21.94 | 2.00 | 81.8 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 3.89 | 12.61 | 19.66 | 3.00 | 70.0 | 77.0 |
| Bench 2 | Bench Boost | Tijjani Reijnders | MID | 13 | 5.7 | 3.11 | 9.65 | 15.96 | 1.00 | 54.4 | 75.0 |