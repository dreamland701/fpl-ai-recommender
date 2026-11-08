# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW5
- Simulated weeks: GW6-GW9
- Total predicted points: 282.81
- Total actual points: 282.00
- Average predicted points: 70.70
- Average actual points: 70.50
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
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 66.80
- Actual score: 62.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.80 | 11.42 | 19.37 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Karl Darlow | GK | 11 | 4.0 | 1.99 | 5.52 | 9.50 | 2.00 | 62.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.23 | 14.60 | 20.35 | 7.00 | 90.0 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.2 | 3.43 | 13.90 | 20.57 | -3.00 | 90.0 | 52.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.7 | 3.50 | 11.69 | 18.46 | 7.00 | 85.7 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.0 | 3.29 | 10.24 | 14.23 | 6.00 | 85.9 | 90.0 |
| Bench 3 | Bench | Omar Alderete | DEF | 17 | 4.0 | 2.09 | 10.21 | 14.53 | 17.00 | 87.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.83 | 24.50 | 39.73 | 16.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 5.96 | 16.34 | 27.02 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 1.57 | 3.61 | 6.58 | 12.00 | 18.9 | 18.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 6.23 | 19.78 | 34.14 | 2.00 | 89.7 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.92 | 18.22 | 27.92 | 7.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 5.25 | 14.73 | 23.18 | 2.00 | 90.0 | 82.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.40 | 14.45 | 22.02 | 2.00 | 90.0 | 80.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.41 | 14.42 | 23.68 | 2.00 | 86.8 | 90.0 |

## GW7

- Train rows: 165607
- Bank: 0.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 63.28
- Actual score: 71.00
- Transfer: Tijjani Reijnders -> Elliot Anderson (projected gain 1.29, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.94 | 11.29 | 18.24 | 6.00 | 82.7 | 90.0 |
| Bench 1 | Bench | Karl Darlow | GK | 11 | 4.0 | 2.05 | 5.83 | 9.43 | 1.00 | 69.3 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.03 | 15.17 | 20.33 | 2.00 | 85.1 | 77.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.7 | 4.55 | 14.61 | 21.29 | 3.00 | 90.0 | 90.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.0 | 4.27 | 13.06 | 18.14 | 0.00 | 90.0 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.63 | 9.88 | 13.53 | 3.00 | 79.6 | 90.0 |
| Bench 4 | Bench | Trevoh Chalobah | DEF | 7 | 5.2 | 2.49 | 8.57 | 12.79 | 0.00 | 50.2 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.72 | 25.52 | 39.60 | 8.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.12 | 13.15 | 21.61 | 2.00 | 73.9 | 73.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 2.82 | 5.64 | 8.90 | 0.00 | 33.5 | 0.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.7 | 6.24 | 18.70 | 27.98 | 18.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.5 | 6.23 | 18.55 | 31.56 | 2.00 | 85.7 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 3.54 | 12.76 | 18.95 | 7.00 | 71.5 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.29 | 12.30 | 19.25 | 12.00 | 75.7 | 89.0 |
| Bench 2 | Bench | Elliot Anderson | MID | 16 | 5.4 | 3.26 | 11.36 | 15.57 | 1.00 | 80.9 | 90.0 |

## GW8

- Train rows: 166350
- Bank: 0.30 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 71.54
- Actual score: 86.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.46) beats the best remaining Triple Captain opportunity (9.19).
- Transfer: Marc Guéhi -> Dan Burn (projected gain 0.36, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.46) beats the best remaining Triple Captain opportunity (9.19).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.84 | 11.17 | 18.20 | 6.00 | 85.5 | 90.0 |
| Bench 1 | Bench | Karl Darlow | GK | 11 | 4.0 | 2.12 | 5.86 | 9.43 | 1.00 | 69.3 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.36 | 14.35 | 20.15 | 2.00 | 79.5 | 90.0 |
| XI | XI | Dan Burn | DEF | 15 | 5.1 | 3.80 | 11.63 | 17.42 | 2.00 | 90.0 | 90.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.0 | 3.88 | 11.61 | 15.63 | 6.00 | 74.6 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.98 | 11.45 | 14.75 | 17.00 | 79.0 | 90.0 |
| Bench 3 | Bench | Trevoh Chalobah | DEF | 7 | 5.1 | 2.25 | 6.90 | 11.98 | 6.00 | 35.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 8.09 | 24.61 | 39.63 | 13.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.64 | 12.54 | 22.42 | 2.00 | 78.5 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 1.68 | 3.64 | 6.35 | 24.00 | 18.1 | 148.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.8 | 7.16 | 20.23 | 32.65 | 4.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.4 | 6.05 | 17.91 | 30.49 | 2.00 | 83.0 | 84.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.53 | 15.92 | 23.83 | 2.00 | 90.0 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.03 | 12.76 | 20.37 | 4.00 | 81.5 | 85.0 |
| Bench 2 | Bench | Elliot Anderson | MID | 16 | 5.4 | 3.79 | 10.31 | 15.93 | 4.00 | 81.1 | 90.0 |

## GW9

- Train rows: 167095
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Junior Kroupi
- Vice captain: Erling Haaland
- Effective captain: Junior Kroupi
- Chip used: bench_boost
- Predicted score: 81.19
- Actual score: 63.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (12.93) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Trevoh Chalobah -> Marc Guéhi (projected gain 2.84, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (12.93) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.95 | 11.38 | 18.47 | 6.00 | 85.4 | 90.0 |
| Bench 1 | Bench Boost | Karl Darlow | GK | 11 | 4.0 | 2.09 | 5.65 | 9.04 | 0.00 | 66.9 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 5.03 | 14.68 | 21.23 | 5.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.9 | 4.17 | 13.27 | 21.51 | 4.00 | 90.0 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.89 | 11.20 | 17.16 | 2.00 | 82.8 | 90.0 |
| Bench 3 | Bench Boost | Dan Burn | DEF | 15 | 5.1 | 3.66 | 10.44 | 16.40 | 2.00 | 77.2 | 90.0 |
| Bench 4 | Bench Boost | Omar Alderete | DEF | 17 | 4.0 | 2.95 | 9.13 | 13.61 | 0.00 | 68.4 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.5 | 7.91 | 24.82 | 41.16 | 2.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.64 | 12.98 | 21.54 | 2.00 | 80.0 | 84.0 |
| Captain | Captain | Junior Kroupi | FWD | 4 | 4.5 | 8.67 | 12.34 | 17.39 | 12.00 | 158.5 | 136.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.9 | 6.81 | 19.22 | 29.82 | 3.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.3 | 5.45 | 16.08 | 28.59 | 6.00 | 75.0 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 5.06 | 14.82 | 22.08 | 2.00 | 83.3 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.50 | 13.14 | 20.19 | 3.00 | 78.4 | 77.0 |
| Bench 2 | Bench Boost | Elliot Anderson | MID | 16 | 5.3 | 3.74 | 10.91 | 16.54 | 2.00 | 81.6 | 90.0 |