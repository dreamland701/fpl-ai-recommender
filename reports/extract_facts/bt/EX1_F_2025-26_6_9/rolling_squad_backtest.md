# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW5
- Simulated weeks: GW6-GW9
- Total predicted points: 281.13
- Total actual points: 267.00
- Average predicted points: 70.28
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
- Bank: 100.00 -> 0.70
- Free transfers: 1 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 73.74
- Actual score: 58.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.80 | 11.43 | 19.34 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Freddie Woodman | GK | 12 | 3.9 | 0.18 | 0.62 | 1.93 | 0.00 | 6.3 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.53 | 15.16 | 21.54 | 7.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Trevoh Chalobah | DEF | 7 | 5.2 | 3.42 | 13.87 | 20.53 | -3.00 | 90.0 | 52.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.5 | 5.37 | 13.62 | 19.70 | 1.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Marc Guéhi | DEF | 8 | 4.7 | 3.50 | 11.72 | 18.47 | 7.00 | 85.6 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.25 | 11.42 | 18.37 | 2.00 | 78.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 9.51 | 24.33 | 40.14 | 16.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.36 | 17.14 | 28.46 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Richarlison de Andrade | FWD | 18 | 6.8 | 4.87 | 13.32 | 21.96 | 2.00 | 78.2 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 6.26 | 18.87 | 29.15 | 7.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 6.76 | 18.11 | 29.07 | -1.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 5.21 | 14.65 | 23.04 | 2.00 | 90.0 | 82.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.41 | 14.47 | 23.70 | 2.00 | 86.5 | 90.0 |
| XI | XI | Jack Grealish | MID | 9 | 6.9 | 5.76 | 14.32 | 23.53 | 2.00 | 87.9 | 90.0 |

## GW7

- Train rows: 165607
- Bank: 0.70 -> 1.80
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 63.90
- Actual score: 78.00
- Transfer: Trevoh Chalobah -> Omar Alderete (projected gain 2.32, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.94 | 11.31 | 18.24 | 6.00 | 82.6 | 90.0 |
| Bench 1 | Bench | Freddie Woodman | GK | 12 | 3.9 | 0.06 | 0.47 | 1.08 | 0.00 | 6.0 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.30 | 15.87 | 21.74 | 2.00 | 90.0 | 77.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.7 | 4.50 | 14.51 | 21.14 | 3.00 | 90.0 | 90.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.1 | 4.23 | 12.99 | 18.08 | 0.00 | 90.0 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.5 | 4.24 | 11.47 | 16.39 | 5.00 | 79.7 | 90.0 |
| Bench 2 | Bench | Micky van de Ven | DEF | 18 | 4.7 | 3.59 | 10.78 | 16.94 | 2.00 | 79.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 9.00 | 26.22 | 40.84 | 8.00 | 90.0 | 90.0 |
| Bench 3 | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 3.30 | 10.41 | 18.55 | 2.00 | 57.3 | 73.0 |
| Bench 4 | Bench | Richarlison de Andrade | FWD | 18 | 6.8 | 3.03 | 9.78 | 15.72 | 1.00 | 53.9 | 16.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.7 | 6.54 | 19.44 | 29.33 | 18.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.39 | 14.84 | 23.41 | 3.00 | 76.8 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.27 | 12.37 | 19.34 | 12.00 | 74.0 | 89.0 |
| XI | XI | Jack Grealish | MID | 9 | 6.9 | 3.78 | 11.90 | 18.67 | 10.00 | 66.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 3.70 | 11.34 | 16.91 | 3.00 | 66.8 | 75.0 |

## GW8

- Train rows: 166350
- Bank: 1.80 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 71.71
- Actual score: 83.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.09) beats the best remaining Triple Captain opportunity (8.81).
- Transfer: Micky van de Ven -> Gabriel dos Santos Magalhães (projected gain 6.18, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.09) beats the best remaining Triple Captain opportunity (8.81).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.85 | 11.21 | 18.24 | 6.00 | 85.5 | 90.0 |
| Bench 1 | Bench | Freddie Woodman | GK | 12 | 3.9 | 0.16 | 0.45 | 1.00 | 0.00 | 6.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 5.33 | 15.89 | 22.73 | 12.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.31 | 14.32 | 20.19 | 2.00 | 77.0 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.5 | 3.57 | 12.24 | 17.15 | 3.00 | 83.2 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.62 | 11.25 | 21.28 | 4.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Omar Alderete | DEF | 17 | 4.1 | 3.37 | 10.81 | 15.17 | 6.00 | 64.6 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 8.06 | 24.55 | 39.50 | 13.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.65 | 12.67 | 22.68 | 2.00 | 77.4 | 90.0 |
| Bench 3 | Bench | Richarlison de Andrade | FWD | 18 | 6.7 | 2.61 | 8.29 | 13.12 | 1.00 | 41.3 | 30.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.8 | 7.09 | 20.09 | 32.42 | 4.00 | 90.0 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.80 | 16.94 | 25.91 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.32 | 14.99 | 22.07 | 8.00 | 74.1 | 84.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 3.98 | 10.55 | 18.32 | 1.00 | 72.1 | 58.0 |
| Bench 4 | Bench | Jack Grealish | MID | 9 | 6.9 | 2.32 | 7.77 | 14.45 | 0.00 | 50.7 | 0.0 |

## GW9

- Train rows: 167095
- Bank: 0.20 -> 0.60
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 71.77
- Actual score: 48.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.65) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Jack Grealish -> Iliman Ndiaye (projected gain 4.96, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.65) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.96 | 11.41 | 18.49 | 6.00 | 85.5 | 90.0 |
| Bench 1 | Bench Boost | Freddie Woodman | GK | 12 | 3.9 | 0.08 | 0.35 | 0.88 | 0.00 | 5.9 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 5.70 | 16.33 | 24.84 | 9.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 5.02 | 14.66 | 21.16 | 5.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.16 | 13.25 | 21.45 | 4.00 | 90.0 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.5 | 3.97 | 11.55 | 18.05 | 1.00 | 85.2 | 90.0 |
| Bench 3 | Bench Boost | Omar Alderete | DEF | 17 | 4.1 | 2.91 | 8.99 | 13.35 | 0.00 | 65.2 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.5 | 7.89 | 24.78 | 41.04 | 2.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 3.48 | 10.26 | 17.66 | 2.00 | 59.8 | 84.0 |
| Bench 4 | Bench Boost | Richarlison de Andrade | FWD | 18 | 6.6 | 2.44 | 7.93 | 13.04 | 4.00 | 41.6 | 28.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.9 | 6.79 | 19.18 | 29.71 | 3.00 | 90.0 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 5.05 | 14.79 | 22.02 | 2.00 | 82.8 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.78 | 13.85 | 22.01 | 4.00 | 82.8 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.48 | 13.23 | 20.33 | 3.00 | 76.7 | 77.0 |
| Bench 2 | Bench Boost | Tijjani Reijnders | MID | 13 | 5.7 | 3.18 | 9.85 | 16.19 | 1.00 | 57.1 | 75.0 |