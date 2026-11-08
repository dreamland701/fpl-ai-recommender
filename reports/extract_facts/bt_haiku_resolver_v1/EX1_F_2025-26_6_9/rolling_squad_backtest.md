# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW5
- Simulated weeks: GW6-GW9
- Total predicted points: 288.03
- Total actual points: 286.00
- Average predicted points: 72.01
- Average actual points: 71.50
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
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 67.98
- Actual score: 62.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.80 | 11.42 | 19.33 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 2.98 | 9.29 | 15.95 | 1.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.17 | 14.44 | 20.11 | 7.00 | 90.0 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.2 | 3.39 | 13.89 | 20.53 | -3.00 | 90.0 | 52.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.7 | 3.82 | 12.67 | 20.00 | 7.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.0 | 3.26 | 10.24 | 14.20 | 6.00 | 85.5 | 90.0 |
| Bench 3 | Bench | Omar Alderete | DEF | 17 | 4.0 | 2.06 | 10.22 | 14.51 | 17.00 | 87.6 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.90 | 24.26 | 40.78 | 16.00 | 90.0 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.79 | 18.37 | 30.64 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 1.71 | 3.76 | 6.72 | 12.00 | 21.3 | 18.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.5 | 6.34 | 20.04 | 34.42 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.86 | 18.13 | 27.74 | 7.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 5.20 | 14.65 | 23.06 | 2.00 | 90.0 | 82.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.43 | 14.46 | 23.73 | 2.00 | 86.9 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.37 | 14.41 | 21.96 | 2.00 | 90.0 | 80.0 |

## GW7

- Train rows: 165607
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 62.72
- Actual score: 72.00
- Transfer: João Pedro Junqueira de Jesus -> Jarrod Bowen (projected gain 0.01, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.94 | 11.30 | 18.24 | 6.00 | 82.6 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 2.99 | 9.11 | 15.09 | 2.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 4.99 | 15.09 | 20.20 | 2.00 | 84.3 | 77.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.7 | 4.50 | 14.53 | 21.15 | 3.00 | 90.0 | 90.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.0 | 4.24 | 13.03 | 18.08 | 0.00 | 90.0 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.59 | 9.87 | 13.57 | 3.00 | 77.9 | 90.0 |
| Bench 4 | Bench | Trevoh Chalobah | DEF | 7 | 5.2 | 1.71 | 6.62 | 9.97 | 0.00 | 35.8 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.69 | 25.45 | 39.38 | 8.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Jarrod Bowen | FWD | 19 | 7.7 | 3.45 | 11.04 | 17.99 | 2.00 | 81.5 | 90.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 2.99 | 5.81 | 9.09 | 0.00 | 36.3 | 0.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 6.37 | 18.90 | 31.96 | 2.00 | 87.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 6.22 | 18.65 | 27.81 | 18.00 | 90.0 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 3.49 | 12.65 | 18.64 | 7.00 | 68.2 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.28 | 12.37 | 19.33 | 12.00 | 74.3 | 89.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 3.71 | 11.35 | 16.90 | 3.00 | 66.9 | 75.0 |

## GW8

- Train rows: 166350
- Bank: 0.00 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 72.89
- Actual score: 89.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.46) beats the best remaining Triple Captain opportunity (9.19).
- Transfer: Jarrod Bowen -> Nick Woltemade (projected gain 2.15, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.46) beats the best remaining Triple Captain opportunity (9.19).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.85 | 11.20 | 18.23 | 6.00 | 85.5 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.48 | 9.46 | 15.29 | 9.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.32 | 14.37 | 20.19 | 2.00 | 77.6 | 90.0 |
| Bench 2 | Bench | Omar Alderete | DEF | 17 | 4.0 | 3.82 | 11.48 | 15.32 | 6.00 | 71.4 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.95 | 11.48 | 14.84 | 17.00 | 77.3 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.61 | 11.19 | 21.31 | 4.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Trevoh Chalobah | DEF | 7 | 5.1 | 2.36 | 7.21 | 12.25 | 6.00 | 37.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 8.09 | 24.60 | 39.54 | 13.00 | 90.0 | 90.0 |
| XI | XI | Nick Woltemade | FWD | 15 | 7.3 | 4.57 | 13.22 | 21.15 | 8.00 | 81.3 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 1.84 | 3.80 | 6.53 | 24.00 | 20.6 | 148.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.8 | 7.10 | 20.08 | 32.44 | 4.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.4 | 6.19 | 18.24 | 30.90 | 2.00 | 85.0 | 84.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 6.02 | 17.27 | 25.90 | 2.00 | 90.0 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.04 | 12.81 | 20.40 | 4.00 | 81.7 | 85.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 3.98 | 10.53 | 18.33 | 1.00 | 72.1 | 58.0 |

## GW9

- Train rows: 167095
- Bank: 0.40 -> 0.00
- Free transfers: 2 -> 2
- Captain: Junior Kroupi
- Vice captain: Erling Haaland
- Effective captain: Junior Kroupi
- Chip used: bench_boost
- Predicted score: 84.44
- Actual score: 63.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.86) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Trevoh Chalobah -> James Tarkowski (projected gain 0.41, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.86) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.96 | 11.40 | 18.49 | 6.00 | 85.4 | 90.0 |
| Bench 1 | Bench Boost | Martin Dúbravka | GK | 3 | 4.0 | 3.36 | 9.42 | 15.51 | 2.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 5.03 | 14.69 | 21.20 | 5.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.16 | 13.25 | 21.48 | 4.00 | 90.0 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.5 | 3.98 | 11.59 | 18.09 | 1.00 | 85.5 | 90.0 |
| Bench 2 | Bench Boost | Nordi Mukiele | DEF | 17 | 4.0 | 3.91 | 11.24 | 17.20 | 2.00 | 83.1 | 90.0 |
| Bench 4 | Bench Boost | Omar Alderete | DEF | 17 | 4.0 | 2.92 | 9.04 | 13.37 | 0.00 | 65.7 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.5 | 7.90 | 24.80 | 41.06 | 2.00 | 90.0 | 90.0 |
| XI | XI | Nick Woltemade | FWD | 15 | 7.3 | 5.19 | 15.15 | 22.54 | 2.00 | 79.5 | 85.0 |
| Captain | Captain | Junior Kroupi | FWD | 4 | 4.5 | 9.26 | 13.26 | 18.97 | 12.00 | 179.5 | 136.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.9 | 6.82 | 19.23 | 29.76 | 3.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.3 | 5.98 | 17.64 | 29.22 | 6.00 | 78.5 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 5.06 | 14.83 | 22.05 | 2.00 | 83.4 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.49 | 13.23 | 20.34 | 3.00 | 77.0 | 77.0 |
| Bench 3 | Bench Boost | Tijjani Reijnders | MID | 13 | 5.7 | 3.18 | 9.88 | 16.17 | 1.00 | 57.3 | 75.0 |