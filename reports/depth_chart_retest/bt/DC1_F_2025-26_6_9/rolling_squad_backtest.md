# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW5
- Simulated weeks: GW6-GW9
- Total predicted points: 278.84
- Total actual points: 274.00
- Average predicted points: 69.71
- Average actual points: 68.50
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
- Bank: 100.00 -> 0.30
- Free transfers: 1 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 69.17
- Actual score: 58.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 4.13 | 12.37 | 20.96 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Freddie Woodman | GK | 12 | 3.9 | 0.15 | 0.55 | 1.88 | 0.00 | 4.6 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.22 | 14.52 | 19.59 | 7.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Trevoh Chalobah | DEF | 7 | 5.2 | 3.39 | 13.81 | 19.90 | -3.00 | 90.0 | 52.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.6 | 4.08 | 12.02 | 19.06 | 1.00 | 81.8 | 27.0 |
| Bench 4 | Bench | Marc Guéhi | DEF | 8 | 4.7 | 3.34 | 11.28 | 17.51 | 7.00 | 84.2 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.11 | 10.97 | 17.57 | 2.00 | 77.6 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.89 | 24.75 | 40.00 | 16.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.19 | 17.02 | 27.98 | 2.00 | 90.0 | 90.0 |
| XI | XI | Viktor Gyökeres | FWD | 1 | 9.0 | 4.79 | 15.01 | 25.47 | 2.00 | 79.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.76 | 17.80 | 26.89 | 7.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 6.47 | 17.53 | 27.52 | -1.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 5.20 | 14.65 | 22.78 | 2.00 | 90.0 | 82.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.43 | 14.49 | 23.66 | 2.00 | 87.6 | 90.0 |
| Bench 2 | Bench | Anton Stach | MID | 11 | 5.0 | 4.67 | 12.07 | 18.68 | 2.00 | 88.1 | 90.0 |

## GW7

- Train rows: 165607
- Bank: 0.30 -> 1.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 64.55
- Actual score: 67.00
- Transfer: Trevoh Chalobah -> Omar Alderete (projected gain 2.70, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 4.30 | 12.33 | 19.95 | 6.00 | 86.5 | 90.0 |
| Bench 1 | Bench | Freddie Woodman | GK | 12 | 3.9 | 0.02 | 0.37 | 0.95 | 0.00 | 4.0 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.02 | 15.12 | 20.16 | 2.00 | 85.1 | 77.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.7 | 4.40 | 14.25 | 20.67 | 3.00 | 90.0 | 90.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.1 | 4.25 | 12.96 | 17.88 | 0.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Micky van de Ven | DEF | 18 | 4.7 | 3.43 | 10.31 | 16.28 | 2.00 | 78.5 | 90.0 |
| Bench 3 | Bench | Pedro Porro Sauceda | DEF | 18 | 5.6 | 3.39 | 9.54 | 15.56 | 7.00 | 56.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.80 | 25.81 | 40.07 | 8.00 | 90.0 | 90.0 |
| XI | XI | Viktor Gyökeres | FWD | 1 | 9.0 | 5.55 | 15.62 | 25.12 | 2.00 | 78.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.41 | 14.09 | 23.20 | 2.00 | 75.9 | 73.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.7 | 6.11 | 18.37 | 27.43 | 18.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.04 | 13.83 | 21.63 | 3.00 | 69.7 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.22 | 12.23 | 19.23 | 12.00 | 74.7 | 89.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 3.64 | 11.15 | 16.63 | 3.00 | 67.6 | 75.0 |
| Bench 4 | Bench | Anton Stach | MID | 11 | 5.0 | 3.19 | 9.91 | 14.80 | 2.00 | 75.8 | 66.0 |

## GW8

- Train rows: 166350
- Bank: 1.40 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 71.91
- Actual score: 82.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.14) beats the best remaining Triple Captain opportunity (8.87).
- Transfer: Pedro Porro Sauceda -> Gabriel dos Santos Magalhães (projected gain 4.44, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.14) beats the best remaining Triple Captain opportunity (8.87).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 4.19 | 12.18 | 19.85 | 6.00 | 88.9 | 90.0 |
| Bench 1 | Bench | Freddie Woodman | GK | 12 | 3.9 | 0.13 | 0.36 | 0.87 | 0.00 | 4.3 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 5.15 | 15.40 | 22.05 | 12.00 | 89.5 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.27 | 14.25 | 20.01 | 2.00 | 76.6 | 90.0 |
| Bench 2 | Bench | Omar Alderete | DEF | 17 | 4.1 | 3.68 | 11.13 | 14.79 | 6.00 | 69.8 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.47 | 10.87 | 20.78 | 4.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Micky van de Ven | DEF | 18 | 4.7 | 3.41 | 9.20 | 15.63 | 0.00 | 80.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 8.12 | 24.73 | 39.85 | 13.00 | 90.0 | 90.0 |
| XI | XI | Viktor Gyökeres | FWD | 1 | 9.0 | 4.40 | 13.51 | 21.89 | 2.00 | 66.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.82 | 13.26 | 23.64 | 2.00 | 79.3 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.8 | 6.88 | 19.55 | 31.62 | 4.00 | 90.0 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.36 | 15.56 | 23.35 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.19 | 14.75 | 21.70 | 8.00 | 71.4 | 84.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 3.83 | 10.23 | 17.91 | 1.00 | 70.2 | 58.0 |
| Bench 3 | Bench | Anton Stach | MID | 11 | 5.0 | 3.53 | 9.63 | 15.06 | 2.00 | 71.0 | 72.0 |

## GW9

- Train rows: 167095
- Bank: 0.70 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 73.21
- Actual score: 67.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.59) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Tijjani Reijnders -> Moisés Caicedo Corozo (projected gain 2.68, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.59) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 4.32 | 12.44 | 20.19 | 6.00 | 89.6 | 90.0 |
| Bench 1 | Bench Boost | Freddie Woodman | GK | 12 | 3.9 | 0.07 | 0.27 | 0.75 | 0.00 | 5.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 5.53 | 15.83 | 24.15 | 9.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.99 | 14.57 | 21.06 | 5.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.11 | 13.12 | 21.27 | 4.00 | 90.0 | 90.0 |
| Bench 3 | Bench Boost | Micky van de Ven | DEF | 18 | 4.7 | 3.28 | 9.27 | 14.78 | 23.00 | 81.6 | 90.0 |
| Bench 4 | Bench Boost | Omar Alderete | DEF | 17 | 4.1 | 2.81 | 8.76 | 12.92 | 0.00 | 64.6 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.5 | 7.89 | 24.80 | 41.12 | 2.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.82 | 13.62 | 22.65 | 2.00 | 80.7 | 84.0 |
| XI | XI | Viktor Gyökeres | FWD | 1 | 9.0 | 4.55 | 13.44 | 22.35 | 2.00 | 69.6 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.9 | 6.60 | 18.58 | 28.73 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.65 | 13.52 | 21.61 | 4.00 | 81.6 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.44 | 13.01 | 20.09 | 3.00 | 78.8 | 77.0 |
| XI | XI | Moisés Caicedo Corozo | MID | 7 | 5.9 | 3.84 | 11.70 | 16.74 | 2.00 | 68.2 | 90.0 |
| Bench 2 | Bench Boost | Anton Stach | MID | 11 | 5.0 | 3.39 | 9.03 | 13.65 | 0.00 | 65.7 | 0.0 |