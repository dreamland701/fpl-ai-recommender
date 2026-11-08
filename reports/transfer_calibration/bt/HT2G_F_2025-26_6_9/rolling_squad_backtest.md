# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW5
- Simulated weeks: GW6-GW9
- Total predicted points: 283.35
- Total actual points: 262.00
- Average predicted points: 70.84
- Average actual points: 65.50
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
- Predicted score: 67.57
- Actual score: 57.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.80 | 11.42 | 19.37 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Freddie Woodman | GK | 12 | 3.9 | 0.19 | 0.64 | 1.97 | 0.00 | 6.4 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.23 | 14.60 | 20.35 | 7.00 | 90.0 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.2 | 3.43 | 13.90 | 20.57 | -3.00 | 90.0 | 52.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.26 | 11.39 | 18.40 | 2.00 | 78.9 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.0 | 3.29 | 10.24 | 14.23 | 6.00 | 85.9 | 90.0 |
| Bench 3 | Bench | Omar Alderete | DEF | 17 | 4.0 | 2.09 | 10.21 | 14.53 | 17.00 | 87.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.83 | 24.50 | 39.73 | 16.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 5.96 | 16.34 | 27.02 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 1.69 | 3.72 | 6.68 | 12.00 | 20.8 | 18.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 6.23 | 19.78 | 34.14 | 2.00 | 89.7 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.92 | 18.22 | 27.92 | 7.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 5.25 | 14.73 | 23.18 | 2.00 | 90.0 | 82.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.40 | 14.45 | 22.02 | 2.00 | 90.0 | 80.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.41 | 14.42 | 23.68 | 2.00 | 86.8 | 90.0 |

## GW7

- Train rows: 165607
- Bank: 0.10 -> -0.00
- Free transfers: 2 -> 1
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 63.86
- Actual score: 66.00
- Transfer: Nordi Mukiele, Tijjani Reijnders -> Marc Guéhi, Granit Xhaka (projected gain 5.71, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.94 | 11.29 | 18.24 | 6.00 | 82.7 | 90.0 |
| Bench 1 | Bench | Freddie Woodman | GK | 12 | 3.9 | 0.07 | 0.48 | 1.10 | 0.00 | 6.0 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.03 | 15.17 | 20.33 | 2.00 | 85.1 | 77.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.55 | 14.61 | 21.29 | 3.00 | 90.0 | 90.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.0 | 4.27 | 13.06 | 18.14 | 0.00 | 90.0 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 3.58 | 10.72 | 16.92 | 2.00 | 79.9 | 90.0 |
| Bench 4 | Bench | Trevoh Chalobah | DEF | 7 | 5.2 | 2.34 | 8.16 | 12.18 | 0.00 | 46.6 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.72 | 25.52 | 39.60 | 8.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.08 | 13.14 | 21.67 | 2.00 | 72.1 | 73.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 2.94 | 5.75 | 9.01 | 0.00 | 35.5 | 0.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.7 | 6.24 | 18.70 | 27.98 | 18.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.5 | 6.23 | 18.55 | 31.56 | 2.00 | 85.7 | 90.0 |
| Bench 2 | Bench | Iliman Ndiaye | MID | 9 | 6.5 | 3.47 | 12.57 | 18.60 | 7.00 | 68.0 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.25 | 12.29 | 19.31 | 12.00 | 73.9 | 89.0 |
| XI | XI | Granit Xhaka | MID | 17 | 5.0 | 4.25 | 12.21 | 17.10 | 3.00 | 89.5 | 90.0 |

## GW8

- Train rows: 166350
- Bank: -0.00 -> -0.00
- Free transfers: 1 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 72.56
- Actual score: 76.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.46) beats the best remaining Triple Captain opportunity (9.19).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.46) beats the best remaining Triple Captain opportunity (9.19).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.84 | 11.17 | 18.20 | 6.00 | 85.5 | 90.0 |
| Bench 1 | Bench | Freddie Woodman | GK | 12 | 3.9 | 0.17 | 0.46 | 1.02 | 0.00 | 6.3 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.32 | 14.36 | 20.23 | 2.00 | 77.7 | 90.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.0 | 3.80 | 11.42 | 15.26 | 6.00 | 71.1 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.63 | 11.27 | 21.36 | 4.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Micky van de Ven | DEF | 18 | 4.7 | 3.62 | 9.68 | 16.39 | 0.00 | 83.2 | 90.0 |
| Bench 3 | Bench | Trevoh Chalobah | DEF | 7 | 5.1 | 2.31 | 7.01 | 12.09 | 6.00 | 36.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 8.09 | 24.61 | 39.63 | 13.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.60 | 12.54 | 22.49 | 2.00 | 76.8 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 1.80 | 3.75 | 6.46 | 24.00 | 20.1 | 148.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.8 | 7.16 | 20.23 | 32.65 | 4.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.4 | 6.05 | 17.91 | 30.49 | 2.00 | 83.0 | 84.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.53 | 15.92 | 23.83 | 2.00 | 90.0 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.03 | 12.76 | 20.37 | 4.00 | 81.5 | 85.0 |
| XI | XI | Granit Xhaka | MID | 17 | 5.0 | 4.34 | 11.03 | 17.65 | 5.00 | 84.6 | 90.0 |

## GW9

- Train rows: 167095
- Bank: -0.00 -> 0.10
- Free transfers: 2 -> 1
- Captain: Junior Kroupi
- Vice captain: Erling Haaland
- Effective captain: Junior Kroupi
- Chip used: bench_boost
- Predicted score: 79.36
- Actual score: 63.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.35) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Trevoh Chalobah, Micky van de Ven -> Daniel Muñoz Mejía, Nordi Mukiele (projected gain 2.88, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.35) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.95 | 11.38 | 18.47 | 6.00 | 85.4 | 90.0 |
| Bench 1 | Bench Boost | Freddie Woodman | GK | 12 | 3.9 | 0.09 | 0.36 | 0.89 | 0.00 | 6.0 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 5.03 | 14.68 | 21.23 | 5.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.17 | 13.27 | 21.51 | 4.00 | 90.0 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.6 | 3.95 | 12.46 | 19.98 | 2.00 | 90.0 | 90.0 |
| Bench 3 | Bench Boost | Nordi Mukiele | DEF | 17 | 4.1 | 3.89 | 11.20 | 17.16 | 2.00 | 82.8 | 90.0 |
| Bench 4 | Bench Boost | Omar Alderete | DEF | 17 | 4.0 | 2.88 | 8.93 | 13.25 | 0.00 | 64.9 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.5 | 7.91 | 24.82 | 41.16 | 2.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.60 | 12.99 | 21.61 | 2.00 | 78.3 | 84.0 |
| Captain | Captain | Junior Kroupi | FWD | 4 | 4.5 | 8.59 | 12.35 | 17.46 | 12.00 | 155.1 | 136.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.9 | 6.81 | 19.22 | 29.82 | 3.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.3 | 5.41 | 16.08 | 28.66 | 6.00 | 73.3 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 5.06 | 14.82 | 22.08 | 2.00 | 83.3 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.46 | 13.15 | 20.27 | 3.00 | 76.7 | 77.0 |
| Bench 2 | Bench Boost | Granit Xhaka | MID | 17 | 5.0 | 4.00 | 11.30 | 18.74 | 2.00 | 86.3 | 90.0 |