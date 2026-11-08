# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW5
- Simulated weeks: GW6-GW9
- Total predicted points: 280.38
- Total actual points: 269.00
- Average predicted points: 70.10
- Average actual points: 67.25
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
- Predicted score: 66.87
- Actual score: 57.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.76 | 11.17 | 18.10 | 2.00 | 89.0 | 90.0 |
| Bench 1 | Bench | Freddie Woodman | GK | 12 | 3.9 | 0.21 | 0.62 | 1.12 | 0.00 | 4.0 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.28 | 14.95 | 21.63 | 7.00 | 90.0 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.2 | 3.50 | 14.30 | 21.83 | -3.00 | 90.0 | 52.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.40 | 11.91 | 19.48 | 2.00 | 80.9 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.0 | 3.40 | 10.65 | 15.55 | 6.00 | 86.9 | 90.0 |
| Bench 3 | Bench | Omar Alderete | DEF | 17 | 4.0 | 2.15 | 10.62 | 15.79 | 17.00 | 88.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.89 | 24.42 | 39.68 | 16.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 5.69 | 15.08 | 24.92 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 1.41 | 2.99 | 5.41 | 12.00 | 15.5 | 18.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 6.17 | 19.64 | 34.19 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.80 | 17.72 | 27.55 | 7.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 5.03 | 13.95 | 22.23 | 2.00 | 90.0 | 82.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.25 | 13.84 | 22.99 | 2.00 | 85.7 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.20 | 13.80 | 21.46 | 2.00 | 90.0 | 80.0 |

## GW7

- Train rows: 165607
- Bank: 0.10 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 63.07
- Actual score: 66.00
- Transfer: Trevoh Chalobah -> Marc Guéhi (projected gain 4.31, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.88 | 11.07 | 17.32 | 6.00 | 80.3 | 90.0 |
| Bench 1 | Bench | Freddie Woodman | GK | 12 | 3.9 | 0.08 | 0.48 | 0.58 | 0.00 | 3.8 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.06 | 15.38 | 20.93 | 2.00 | 85.4 | 77.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.58 | 14.85 | 21.83 | 3.00 | 90.0 | 90.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.0 | 4.32 | 13.35 | 18.88 | 0.00 | 90.0 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 3.64 | 11.08 | 17.55 | 2.00 | 81.6 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.67 | 10.22 | 14.33 | 3.00 | 78.6 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.81 | 25.49 | 39.30 | 8.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 3.86 | 12.04 | 19.50 | 2.00 | 70.3 | 73.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 2.85 | 5.27 | 8.03 | 0.00 | 30.8 | 0.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 6.22 | 18.51 | 31.60 | 2.00 | 87.2 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 6.09 | 18.10 | 26.99 | 18.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Iliman Ndiaye | MID | 9 | 6.5 | 3.35 | 12.05 | 17.79 | 7.00 | 66.8 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.13 | 11.82 | 18.49 | 12.00 | 73.3 | 89.0 |
| Bench 2 | Bench | Tijjani Reijnders | MID | 13 | 5.7 | 3.51 | 10.60 | 15.77 | 3.00 | 65.5 | 75.0 |

## GW8

- Train rows: 166350
- Bank: 0.50 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 72.40
- Actual score: 83.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.48) beats the best remaining Triple Captain opportunity (9.21).
- Transfer: Tijjani Reijnders -> Moisés Caicedo Corozo (projected gain 1.27, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.48) beats the best remaining Triple Captain opportunity (9.21).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.79 | 10.92 | 17.47 | 6.00 | 83.4 | 90.0 |
| Bench 1 | Bench | Freddie Woodman | GK | 12 | 3.9 | 0.19 | 0.43 | 0.67 | 0.00 | 4.3 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.34 | 14.51 | 20.64 | 2.00 | 78.4 | 90.0 |
| Bench 2 | Bench | Omar Alderete | DEF | 17 | 4.0 | 3.85 | 11.72 | 15.92 | 6.00 | 71.9 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.99 | 11.70 | 15.32 | 17.00 | 77.5 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.65 | 11.30 | 21.75 | 4.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Micky van de Ven | DEF | 18 | 4.7 | 3.67 | 9.91 | 16.95 | 0.00 | 84.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 8.10 | 24.58 | 39.28 | 13.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.34 | 11.54 | 20.47 | 2.00 | 75.3 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 1.59 | 3.33 | 5.43 | 24.00 | 16.1 | 148.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.8 | 6.97 | 19.51 | 31.40 | 4.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.4 | 6.10 | 18.08 | 30.77 | 2.00 | 84.4 | 84.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.42 | 15.54 | 23.02 | 2.00 | 90.0 | 90.0 |
| XI | XI | Moisés Caicedo Corozo | MID | 7 | 5.8 | 4.59 | 12.98 | 18.81 | 1.00 | 89.7 | 45.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 3.90 | 12.27 | 19.53 | 4.00 | 80.6 | 85.0 |

## GW9

- Train rows: 167095
- Bank: 0.40 -> 0.00
- Free transfers: 2 -> 2
- Captain: Junior Kroupi
- Vice captain: Erling Haaland
- Effective captain: Junior Kroupi
- Chip used: bench_boost
- Predicted score: 78.04
- Actual score: 63.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.01) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Micky van de Ven -> Dan Burn (projected gain 0.02, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.01) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.91 | 11.10 | 17.77 | 6.00 | 83.5 | 90.0 |
| Bench 1 | Bench Boost | Freddie Woodman | GK | 12 | 3.9 | 0.12 | 0.34 | 0.64 | 0.00 | 4.4 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 5.01 | 14.67 | 21.30 | 5.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.20 | 13.39 | 21.87 | 4.00 | 90.0 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.93 | 11.34 | 17.55 | 2.00 | 83.2 | 90.0 |
| Bench 3 | Bench Boost | Dan Burn | DEF | 15 | 5.1 | 3.71 | 10.77 | 17.21 | 2.00 | 76.7 | 90.0 |
| Bench 4 | Bench Boost | Omar Alderete | DEF | 17 | 4.0 | 2.95 | 9.20 | 13.89 | 0.00 | 65.5 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.5 | 7.89 | 24.69 | 40.68 | 2.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.36 | 12.14 | 19.80 | 2.00 | 76.8 | 84.0 |
| Captain | Captain | Junior Kroupi | FWD | 4 | 4.5 | 8.43 | 12.06 | 16.56 | 12.00 | 152.2 | 136.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.9 | 6.61 | 18.55 | 28.61 | 3.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.3 | 5.49 | 16.38 | 29.20 | 6.00 | 74.4 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.91 | 14.36 | 21.22 | 2.00 | 82.0 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.35 | 12.82 | 19.57 | 3.00 | 76.5 | 77.0 |
| Bench 2 | Bench Boost | Moisés Caicedo Corozo | MID | 7 | 5.8 | 3.74 | 11.29 | 16.05 | 2.00 | 67.9 | 90.0 |