# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW5
- Simulated weeks: GW6-GW9
- Total predicted points: 282.48
- Total actual points: 291.00
- Average predicted points: 70.62
- Average actual points: 72.75
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
- Predicted score: 67.71
- Actual score: 57.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.81 | 11.39 | 19.28 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Freddie Woodman | GK | 12 | 3.9 | 0.18 | 0.66 | 2.05 | 0.00 | 6.3 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.20 | 14.59 | 20.34 | 7.00 | 90.0 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.2 | 3.42 | 13.88 | 20.53 | -3.00 | 90.0 | 52.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.27 | 11.37 | 18.25 | 2.00 | 79.0 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.0 | 3.30 | 10.24 | 14.23 | 6.00 | 86.0 | 90.0 |
| Bench 3 | Bench | Omar Alderete | DEF | 17 | 4.0 | 2.09 | 10.18 | 14.45 | 17.00 | 87.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.90 | 25.17 | 41.14 | 16.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 5.97 | 16.30 | 26.87 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 1.76 | 3.66 | 6.44 | 12.00 | 22.5 | 18.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 6.25 | 19.70 | 33.82 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.92 | 18.19 | 27.82 | 7.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 5.26 | 14.75 | 23.14 | 2.00 | 90.0 | 82.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.40 | 14.44 | 21.95 | 2.00 | 90.0 | 80.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.40 | 14.41 | 23.58 | 2.00 | 86.6 | 90.0 |

## GW7

- Train rows: 165607
- Bank: 0.10 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 63.28
- Actual score: 67.00
- Transfer: Trevoh Chalobah -> Marc Guéhi (projected gain 4.01, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.95 | 11.26 | 18.10 | 6.00 | 83.1 | 90.0 |
| Bench 1 | Bench | Freddie Woodman | GK | 12 | 3.9 | 0.05 | 0.51 | 1.18 | 0.00 | 5.6 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.01 | 15.15 | 20.35 | 2.00 | 84.8 | 77.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.53 | 14.61 | 21.35 | 3.00 | 90.0 | 90.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.0 | 4.24 | 13.04 | 18.18 | 0.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Micky van de Ven | DEF | 18 | 4.7 | 3.57 | 10.68 | 16.87 | 2.00 | 79.7 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.58 | 9.85 | 13.67 | 3.00 | 77.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.72 | 25.44 | 39.48 | 8.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.09 | 13.07 | 21.46 | 2.00 | 72.3 | 73.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 2.95 | 5.66 | 8.76 | 0.00 | 36.0 | 0.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 6.22 | 18.67 | 28.01 | 18.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 6.30 | 18.50 | 31.25 | 2.00 | 87.5 | 90.0 |
| Bench 3 | Bench | Iliman Ndiaye | MID | 9 | 6.5 | 3.47 | 12.52 | 18.51 | 7.00 | 67.9 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.25 | 12.25 | 19.26 | 12.00 | 73.9 | 89.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 3.67 | 11.18 | 16.72 | 3.00 | 66.4 | 75.0 |

## GW8

- Train rows: 166350
- Bank: 0.50 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 73.13
- Actual score: 83.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.44) beats the best remaining Triple Captain opportunity (9.17).
- Transfer: Tijjani Reijnders -> Moisés Caicedo Corozo (projected gain 3.24, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.44) beats the best remaining Triple Captain opportunity (9.17).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.84 | 11.13 | 18.08 | 6.00 | 85.5 | 90.0 |
| Bench 1 | Bench | Freddie Woodman | GK | 12 | 3.9 | 0.15 | 0.49 | 1.09 | 0.00 | 5.9 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.31 | 14.27 | 20.18 | 2.00 | 77.5 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.93 | 11.41 | 14.87 | 17.00 | 76.9 | 90.0 |
| Bench 2 | Bench | Omar Alderete | DEF | 17 | 4.0 | 3.81 | 11.34 | 15.17 | 6.00 | 71.3 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.61 | 11.34 | 21.31 | 4.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Micky van de Ven | DEF | 18 | 4.7 | 3.61 | 9.64 | 16.34 | 0.00 | 83.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 8.07 | 24.51 | 39.47 | 13.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.64 | 12.51 | 22.34 | 2.00 | 77.8 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 1.86 | 3.69 | 6.23 | 24.00 | 21.6 | 148.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.8 | 7.11 | 20.24 | 32.74 | 4.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.4 | 6.14 | 17.89 | 30.19 | 2.00 | 84.9 | 84.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.52 | 15.94 | 23.89 | 2.00 | 90.0 | 90.0 |
| XI | XI | Moisés Caicedo Corozo | MID | 7 | 5.8 | 4.79 | 13.67 | 20.33 | 1.00 | 90.0 | 45.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.02 | 12.71 | 20.35 | 4.00 | 81.5 | 85.0 |

## GW9

- Train rows: 167095
- Bank: 0.40 -> 1.10
- Free transfers: 2 -> 2
- Captain: Junior Kroupi
- Vice captain: Erling Haaland
- Effective captain: Junior Kroupi
- Chip used: bench_boost
- Predicted score: 78.37
- Actual score: 84.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.37) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Moisés Caicedo Corozo -> Granit Xhaka (projected gain 0.01, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.37) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.96 | 11.34 | 18.34 | 6.00 | 85.7 | 90.0 |
| Bench 1 | Bench Boost | Freddie Woodman | GK | 12 | 3.9 | 0.07 | 0.38 | 0.98 | 0.00 | 5.7 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 5.04 | 14.68 | 21.25 | 5.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.16 | 13.25 | 21.49 | 4.00 | 90.0 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.86 | 11.14 | 17.15 | 2.00 | 82.1 | 90.0 |
| Bench 3 | Bench Boost | Micky van de Ven | DEF | 18 | 4.7 | 3.37 | 9.61 | 15.28 | 23.00 | 80.4 | 90.0 |
| Bench 4 | Bench Boost | Omar Alderete | DEF | 17 | 4.0 | 2.46 | 8.40 | 13.21 | 0.00 | 55.9 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.5 | 7.89 | 24.72 | 40.98 | 2.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.63 | 12.95 | 21.44 | 2.00 | 79.0 | 84.0 |
| Captain | Captain | Junior Kroupi | FWD | 4 | 4.5 | 8.57 | 12.35 | 17.44 | 12.00 | 154.7 | 136.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.9 | 6.79 | 19.16 | 29.79 | 3.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.3 | 5.49 | 16.04 | 28.35 | 6.00 | 75.1 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 5.06 | 14.79 | 22.09 | 2.00 | 83.3 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.46 | 13.12 | 20.17 | 3.00 | 76.8 | 77.0 |
| Bench 2 | Bench Boost | Granit Xhaka | MID | 17 | 5.1 | 3.99 | 11.28 | 18.71 | 2.00 | 86.0 | 90.0 |