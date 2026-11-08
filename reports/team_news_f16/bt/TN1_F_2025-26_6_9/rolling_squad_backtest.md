# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW5
- Simulated weeks: GW6-GW9
- Total predicted points: 283.13
- Total actual points: 290.00
- Average predicted points: 70.78
- Average actual points: 72.50
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
- Predicted score: 67.49
- Actual score: 57.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.83 | 11.46 | 19.34 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Freddie Woodman | GK | 12 | 3.9 | 0.03 | 0.39 | 1.62 | 0.00 | 1.9 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.23 | 14.59 | 20.30 | 7.00 | 90.0 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.2 | 3.31 | 13.89 | 20.52 | -3.00 | 90.0 | 52.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.31 | 11.46 | 18.39 | 2.00 | 80.3 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.0 | 3.22 | 10.24 | 14.19 | 6.00 | 84.4 | 90.0 |
| Bench 3 | Bench | Omar Alderete | DEF | 17 | 4.0 | 1.99 | 10.24 | 14.51 | 17.00 | 85.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.81 | 24.44 | 39.58 | 16.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.01 | 16.39 | 27.01 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 1.59 | 3.62 | 6.48 | 12.00 | 17.4 | 18.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 6.26 | 19.82 | 34.09 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.91 | 18.23 | 27.86 | 7.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 5.23 | 14.76 | 23.16 | 2.00 | 90.0 | 82.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.35 | 14.48 | 22.00 | 2.00 | 90.0 | 80.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.43 | 14.45 | 23.63 | 2.00 | 87.4 | 90.0 |

## GW7

- Train rows: 165607
- Bank: 0.10 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 63.27
- Actual score: 66.00
- Transfer: Trevoh Chalobah -> Marc Guéhi (projected gain 4.83, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.98 | 11.35 | 18.24 | 6.00 | 83.6 | 90.0 |
| Bench 1 | Bench | Freddie Woodman | GK | 12 | 3.9 | 0.00 | 0.21 | 0.74 | 0.00 | 1.3 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 4.94 | 14.99 | 20.21 | 2.00 | 82.8 | 77.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.52 | 14.62 | 21.28 | 3.00 | 90.0 | 90.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.0 | 4.24 | 13.06 | 18.12 | 0.00 | 90.0 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 3.63 | 10.78 | 16.96 | 2.00 | 81.2 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.0 | 3.58 | 9.87 | 13.61 | 3.00 | 77.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.72 | 25.48 | 39.52 | 8.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.16 | 13.25 | 21.76 | 2.00 | 74.0 | 73.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 3.23 | 5.95 | 9.26 | 0.00 | 44.2 | 0.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 6.26 | 18.60 | 31.55 | 2.00 | 86.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 6.13 | 18.52 | 27.86 | 18.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Iliman Ndiaye | MID | 9 | 6.5 | 3.48 | 12.63 | 18.64 | 7.00 | 68.1 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.29 | 12.34 | 19.35 | 12.00 | 75.1 | 89.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 3.69 | 11.30 | 16.85 | 3.00 | 67.0 | 75.0 |

## GW8

- Train rows: 166350
- Bank: 0.50 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 73.41
- Actual score: 83.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.47) beats the best remaining Triple Captain opportunity (9.20).
- Transfer: Tijjani Reijnders -> Moisés Caicedo Corozo (projected gain 3.44, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.47) beats the best remaining Triple Captain opportunity (9.20).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.87 | 11.21 | 18.19 | 6.00 | 86.2 | 90.0 |
| Bench 1 | Bench | Freddie Woodman | GK | 12 | 3.9 | 0.01 | 0.20 | 0.68 | 0.00 | 1.7 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.34 | 14.44 | 20.24 | 2.00 | 78.1 | 90.0 |
| Bench 3 | Bench | Omar Alderete | DEF | 17 | 4.0 | 3.65 | 11.70 | 16.01 | 6.00 | 67.0 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.96 | 11.56 | 14.85 | 17.00 | 77.7 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.61 | 11.03 | 21.34 | 4.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Micky van de Ven | DEF | 18 | 4.7 | 3.67 | 9.73 | 16.44 | 0.00 | 84.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 8.09 | 24.58 | 39.56 | 13.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.68 | 12.64 | 22.60 | 2.00 | 78.7 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 1.70 | 3.64 | 6.28 | 24.00 | 16.6 | 148.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.8 | 7.14 | 20.12 | 32.61 | 4.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.4 | 6.10 | 18.00 | 30.52 | 2.00 | 84.0 | 84.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.54 | 15.96 | 23.83 | 2.00 | 90.0 | 90.0 |
| XI | XI | Moisés Caicedo Corozo | MID | 7 | 5.8 | 4.83 | 13.90 | 20.25 | 1.00 | 90.0 | 45.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.05 | 12.81 | 20.39 | 4.00 | 82.2 | 85.0 |

## GW9

- Train rows: 167095
- Bank: 0.40 -> 0.40
- Free transfers: 2 -> 2
- Captain: Junior Kroupi
- Vice captain: Erling Haaland
- Effective captain: Junior Kroupi
- Chip used: bench_boost
- Predicted score: 78.96
- Actual score: 84.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.37) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.37) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.99 | 11.44 | 18.49 | 6.00 | 86.4 | 90.0 |
| Bench 1 | Bench Boost | Freddie Woodman | GK | 12 | 3.9 | 0.00 | 0.10 | 0.57 | 0.00 | 1.5 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 5.03 | 14.73 | 21.24 | 5.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.17 | 13.27 | 21.51 | 4.00 | 90.0 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.91 | 11.25 | 17.15 | 2.00 | 83.2 | 90.0 |
| Bench 3 | Bench Boost | Micky van de Ven | DEF | 18 | 4.7 | 3.40 | 9.73 | 15.47 | 23.00 | 81.5 | 90.0 |
| Bench 4 | Bench Boost | Omar Alderete | DEF | 17 | 4.0 | 2.47 | 8.11 | 12.17 | 0.00 | 55.7 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.5 | 7.92 | 24.81 | 41.11 | 2.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.66 | 13.09 | 21.68 | 2.00 | 79.8 | 84.0 |
| Captain | Captain | Junior Kroupi | FWD | 4 | 4.5 | 8.76 | 12.50 | 17.59 | 12.00 | 160.2 | 136.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.9 | 6.84 | 19.29 | 29.81 | 3.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.3 | 5.47 | 16.17 | 28.70 | 6.00 | 74.6 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 5.07 | 14.91 | 22.07 | 2.00 | 83.8 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.50 | 13.21 | 20.31 | 3.00 | 77.7 | 77.0 |
| Bench 2 | Bench Boost | Moisés Caicedo Corozo | MID | 7 | 5.8 | 4.01 | 12.11 | 17.25 | 2.00 | 71.0 | 90.0 |