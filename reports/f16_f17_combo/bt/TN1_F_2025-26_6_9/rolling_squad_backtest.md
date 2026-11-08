# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW5
- Simulated weeks: GW6-GW9
- Total predicted points: 283.47
- Total actual points: 290.00
- Average predicted points: 70.87
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
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 67.47
- Actual score: 57.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.83 | 11.46 | 19.33 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Gabriel Słonina | GK | 7 | 4.0 | 0.36 | 0.98 | 2.26 | 0.00 | 9.7 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.23 | 14.60 | 20.30 | 7.00 | 90.0 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.2 | 3.30 | 13.89 | 20.52 | -3.00 | 90.0 | 52.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.31 | 11.46 | 18.39 | 2.00 | 80.2 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.0 | 3.22 | 10.24 | 14.19 | 6.00 | 84.5 | 90.0 |
| Bench 3 | Bench | Omar Alderete | DEF | 17 | 4.0 | 1.98 | 10.24 | 14.51 | 17.00 | 85.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.81 | 24.44 | 39.58 | 16.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.01 | 16.39 | 27.00 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 1.60 | 3.62 | 6.48 | 12.00 | 17.5 | 18.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 6.25 | 19.81 | 34.09 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.91 | 18.22 | 27.85 | 7.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 5.23 | 14.76 | 23.15 | 2.00 | 90.0 | 82.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.34 | 14.48 | 22.00 | 2.00 | 90.0 | 80.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.43 | 14.44 | 23.63 | 2.00 | 87.3 | 90.0 |

## GW7

- Train rows: 165607
- Bank: 0.00 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 63.26
- Actual score: 66.00
- Transfer: Trevoh Chalobah -> Marc Guéhi (projected gain 4.83, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.97 | 11.35 | 18.24 | 6.00 | 83.6 | 90.0 |
| Bench 1 | Bench | Gabriel Słonina | GK | 7 | 4.0 | 0.34 | 0.80 | 1.43 | 0.00 | 8.6 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 4.94 | 15.00 | 20.21 | 2.00 | 82.9 | 77.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.52 | 14.62 | 21.28 | 3.00 | 90.0 | 90.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.0 | 4.24 | 13.07 | 18.12 | 0.00 | 90.0 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 3.62 | 10.77 | 16.96 | 2.00 | 81.1 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.0 | 3.59 | 9.87 | 13.61 | 3.00 | 77.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.72 | 25.48 | 39.51 | 8.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.15 | 13.25 | 21.76 | 2.00 | 73.9 | 73.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 3.23 | 5.96 | 9.26 | 0.00 | 44.3 | 0.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 6.26 | 18.59 | 31.55 | 2.00 | 86.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 6.13 | 18.52 | 27.86 | 18.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Iliman Ndiaye | MID | 9 | 6.5 | 3.47 | 12.63 | 18.64 | 7.00 | 68.1 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.29 | 12.34 | 19.35 | 12.00 | 75.0 | 89.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 3.69 | 11.29 | 16.85 | 3.00 | 67.0 | 75.0 |

## GW8

- Train rows: 166350
- Bank: 0.40 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 73.39
- Actual score: 83.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.47) beats the best remaining Triple Captain opportunity (9.20).
- Transfer: Tijjani Reijnders -> Moisés Caicedo Corozo (projected gain 3.45, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.47) beats the best remaining Triple Captain opportunity (9.20).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.87 | 11.20 | 18.19 | 6.00 | 86.2 | 90.0 |
| Bench 1 | Bench | Gabriel Słonina | GK | 7 | 4.0 | 0.25 | 0.67 | 1.32 | 0.00 | 9.5 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.34 | 14.45 | 20.24 | 2.00 | 78.1 | 90.0 |
| Bench 3 | Bench | Omar Alderete | DEF | 17 | 4.0 | 3.65 | 11.70 | 16.01 | 6.00 | 67.0 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.96 | 11.57 | 14.86 | 17.00 | 77.7 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.61 | 11.01 | 21.35 | 4.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Micky van de Ven | DEF | 18 | 4.7 | 3.66 | 9.72 | 16.44 | 0.00 | 84.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 8.09 | 24.57 | 39.56 | 13.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.67 | 12.63 | 22.60 | 2.00 | 78.7 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 1.71 | 3.64 | 6.28 | 24.00 | 16.7 | 148.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.8 | 7.14 | 20.11 | 32.61 | 4.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.4 | 6.10 | 18.00 | 30.52 | 2.00 | 84.0 | 84.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.54 | 15.96 | 23.83 | 2.00 | 90.0 | 90.0 |
| XI | XI | Moisés Caicedo Corozo | MID | 7 | 5.8 | 4.83 | 13.90 | 20.25 | 1.00 | 90.0 | 45.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.05 | 12.81 | 20.39 | 4.00 | 82.2 | 85.0 |

## GW9

- Train rows: 167095
- Bank: 0.30 -> 0.30
- Free transfers: 2 -> 2
- Captain: Junior Kroupi
- Vice captain: Erling Haaland
- Effective captain: Junior Kroupi
- Chip used: bench_boost
- Predicted score: 79.36
- Actual score: 84.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.79) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.79) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.99 | 11.44 | 18.50 | 6.00 | 86.4 | 90.0 |
| Bench 1 | Bench Boost | Gabriel Słonina | GK | 7 | 3.9 | 0.43 | 0.68 | 1.13 | 0.00 | 7.4 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 5.03 | 14.74 | 21.24 | 5.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.17 | 13.27 | 21.52 | 4.00 | 90.0 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.91 | 11.25 | 17.15 | 2.00 | 83.1 | 90.0 |
| Bench 3 | Bench Boost | Micky van de Ven | DEF | 18 | 4.7 | 3.40 | 9.73 | 15.47 | 23.00 | 81.4 | 90.0 |
| Bench 4 | Bench Boost | Omar Alderete | DEF | 17 | 4.0 | 2.47 | 8.11 | 12.18 | 0.00 | 55.6 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.5 | 7.92 | 24.80 | 41.11 | 2.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.66 | 13.09 | 21.68 | 2.00 | 79.8 | 84.0 |
| Captain | Captain | Junior Kroupi | FWD | 4 | 4.5 | 8.76 | 12.50 | 17.59 | 12.00 | 160.1 | 136.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.9 | 6.83 | 19.29 | 29.81 | 3.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.3 | 5.47 | 16.17 | 28.70 | 6.00 | 74.5 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 5.07 | 14.91 | 22.08 | 2.00 | 83.8 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.49 | 13.21 | 20.30 | 3.00 | 77.6 | 77.0 |
| Bench 2 | Bench Boost | Moisés Caicedo Corozo | MID | 7 | 5.8 | 4.00 | 12.11 | 17.25 | 2.00 | 70.9 | 90.0 |