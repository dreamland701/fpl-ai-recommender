# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW5
- Simulated weeks: GW6-GW9
- Total predicted points: 281.04
- Total actual points: 267.00
- Average predicted points: 70.26
- Average actual points: 66.75
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
- Bank: 100.00 -> 0.60
- Free transfers: 1 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 73.62
- Actual score: 58.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.82 | 11.46 | 19.28 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Václav Hladký | GK | 3 | 4.0 | 0.00 | 0.24 | 1.43 | 0.00 | 3.3 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.50 | 15.12 | 21.44 | 7.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Trevoh Chalobah | DEF | 7 | 5.2 | 3.31 | 13.86 | 20.46 | -3.00 | 90.0 | 52.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.5 | 5.37 | 13.61 | 19.62 | 1.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Marc Guéhi | DEF | 8 | 4.7 | 3.50 | 11.77 | 18.42 | 7.00 | 85.7 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.30 | 11.48 | 18.34 | 2.00 | 79.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 9.49 | 24.15 | 39.71 | 16.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.37 | 17.14 | 28.37 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Richarlison de Andrade | FWD | 18 | 6.8 | 4.90 | 13.36 | 21.92 | 2.00 | 78.8 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 6.22 | 18.84 | 29.04 | 7.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 6.67 | 17.90 | 28.84 | -1.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 5.20 | 14.67 | 22.99 | 2.00 | 90.0 | 82.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.43 | 14.49 | 23.62 | 2.00 | 87.0 | 90.0 |
| XI | XI | Jack Grealish | MID | 9 | 6.9 | 5.77 | 14.30 | 23.42 | 2.00 | 88.2 | 90.0 |

## GW7

- Train rows: 165607
- Bank: 0.60 -> 1.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 63.70
- Actual score: 78.00
- Transfer: Trevoh Chalobah -> Omar Alderete (projected gain 2.28, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.97 | 11.35 | 18.21 | 6.00 | 83.4 | 90.0 |
| Bench 1 | Bench | Václav Hladký | GK | 3 | 4.0 | 0.00 | 0.23 | 0.87 | 0.00 | 2.4 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.20 | 15.68 | 21.61 | 2.00 | 88.8 | 77.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.7 | 4.47 | 14.52 | 21.13 | 3.00 | 90.0 | 90.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.1 | 4.21 | 13.00 | 18.06 | 0.00 | 90.0 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.5 | 4.28 | 11.50 | 16.39 | 5.00 | 80.7 | 90.0 |
| Bench 2 | Bench | Micky van de Ven | DEF | 18 | 4.7 | 3.63 | 10.82 | 16.96 | 2.00 | 81.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.97 | 26.15 | 40.72 | 8.00 | 90.0 | 90.0 |
| Bench 3 | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 3.52 | 10.77 | 18.88 | 2.00 | 62.6 | 73.0 |
| Bench 4 | Bench | Richarlison de Andrade | FWD | 18 | 6.8 | 3.11 | 9.88 | 15.78 | 1.00 | 56.0 | 16.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.7 | 6.41 | 19.24 | 29.20 | 18.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.35 | 14.65 | 23.30 | 3.00 | 76.1 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.31 | 12.41 | 19.36 | 12.00 | 75.0 | 89.0 |
| XI | XI | Jack Grealish | MID | 9 | 6.9 | 3.83 | 11.95 | 18.70 | 10.00 | 67.4 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 3.72 | 11.37 | 16.92 | 3.00 | 67.2 | 75.0 |

## GW8

- Train rows: 166350
- Bank: 1.70 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 71.81
- Actual score: 83.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.09) beats the best remaining Triple Captain opportunity (8.81).
- Transfer: Micky van de Ven -> Gabriel dos Santos Magalhães (projected gain 6.15, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.09) beats the best remaining Triple Captain opportunity (8.81).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.88 | 11.23 | 18.21 | 6.00 | 86.1 | 90.0 |
| Bench 1 | Bench | Václav Hladký | GK | 3 | 4.0 | 0.21 | 0.33 | 0.79 | 0.00 | 1.9 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 5.34 | 15.91 | 22.74 | 12.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.32 | 14.39 | 20.20 | 2.00 | 77.4 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.5 | 3.58 | 12.34 | 17.16 | 3.00 | 83.6 | 90.0 |
| Bench 2 | Bench | Omar Alderete | DEF | 17 | 4.1 | 3.30 | 11.09 | 15.76 | 6.00 | 62.5 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.60 | 11.04 | 21.27 | 4.00 | 90.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 8.06 | 24.52 | 39.44 | 13.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.71 | 12.73 | 22.74 | 2.00 | 79.0 | 90.0 |
| Bench 3 | Bench | Richarlison de Andrade | FWD | 18 | 6.7 | 2.71 | 8.47 | 13.25 | 1.00 | 44.2 | 30.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.8 | 7.08 | 20.00 | 32.39 | 4.00 | 90.0 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.82 | 17.00 | 25.93 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.27 | 14.97 | 22.00 | 8.00 | 72.8 | 84.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 4.02 | 10.53 | 18.35 | 1.00 | 73.2 | 58.0 |
| Bench 4 | Bench | Jack Grealish | MID | 9 | 6.9 | 2.10 | 7.23 | 13.82 | 0.00 | 45.7 | 0.0 |

## GW9

- Train rows: 167095
- Bank: 0.10 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 71.91
- Actual score: 48.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.50) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Jack Grealish -> Iliman Ndiaye (projected gain 4.92, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.50) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.99 | 11.46 | 18.50 | 6.00 | 86.3 | 90.0 |
| Bench 1 | Bench Boost | Václav Hladký | GK | 3 | 4.0 | 0.10 | 0.31 | 0.81 | 0.00 | 1.3 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 5.70 | 16.33 | 24.84 | 9.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 5.02 | 14.71 | 21.17 | 5.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.16 | 13.25 | 21.46 | 4.00 | 90.0 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.5 | 3.98 | 11.60 | 18.04 | 1.00 | 85.5 | 90.0 |
| Bench 4 | Bench Boost | Omar Alderete | DEF | 17 | 4.1 | 2.55 | 8.27 | 12.43 | 0.00 | 56.7 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.5 | 7.90 | 24.76 | 40.99 | 2.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 3.66 | 10.61 | 17.99 | 2.00 | 64.2 | 84.0 |
| Bench 3 | Bench Boost | Richarlison de Andrade | FWD | 18 | 6.6 | 2.56 | 8.14 | 13.23 | 4.00 | 45.1 | 28.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.9 | 6.81 | 19.24 | 29.70 | 3.00 | 90.0 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 5.07 | 14.87 | 22.01 | 2.00 | 83.3 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.73 | 13.75 | 21.97 | 4.00 | 81.5 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.51 | 13.28 | 20.35 | 3.00 | 77.6 | 77.0 |
| Bench 2 | Bench Boost | Tijjani Reijnders | MID | 13 | 5.7 | 3.26 | 10.00 | 16.24 | 1.00 | 59.3 | 75.0 |