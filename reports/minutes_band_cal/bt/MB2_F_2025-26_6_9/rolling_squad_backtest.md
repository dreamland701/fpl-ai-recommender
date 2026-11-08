# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW5
- Simulated weeks: GW6-GW9
- Total predicted points: 266.26
- Total actual points: 271.00
- Average predicted points: 66.57
- Average actual points: 67.75
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
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 67.15
- Actual score: 58.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.32 | 9.95 | 17.24 | 2.00 | 83.2 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.67 | 1.53 | 3.28 | 0.00 | 7.1 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 4.75 | 13.13 | 18.22 | 7.00 | 83.2 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.5 | 4.97 | 12.74 | 17.92 | 1.00 | 83.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.96 | 12.44 | 19.52 | 2.00 | 74.3 | 90.0 |
| Bench 3 | Bench | Micky van de Ven | DEF | 18 | 4.7 | 4.28 | 11.41 | 18.44 | 2.00 | 79.7 | 90.0 |
| Bench 4 | Bench | Nordi Mukiele | DEF | 17 | 4.0 | 3.26 | 10.09 | 13.88 | 6.00 | 83.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.83 | 24.50 | 39.73 | 16.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 5.48 | 14.87 | 24.89 | 2.00 | 83.2 | 90.0 |
| Bench 2 | Bench | Viktor Gyökeres | FWD | 1 | 9.0 | 4.40 | 13.90 | 23.73 | 2.00 | 76.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.44 | 16.75 | 25.79 | 7.00 | 83.2 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.92 | 15.90 | 25.56 | -1.00 | 83.2 | 90.0 |
| XI | XI | Jack Grealish | MID | 9 | 6.9 | 5.38 | 13.54 | 22.11 | 2.00 | 79.8 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 4.76 | 13.27 | 21.06 | 2.00 | 83.2 | 82.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 4.50 | 11.57 | 18.13 | 2.00 | 83.8 | 90.0 |

## GW7

- Train rows: 165607
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 61.60
- Actual score: 66.00
- Transfer: Tijjani Reijnders -> Jaidon Anthony (projected gain 0.43, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.90 | 11.15 | 17.88 | 6.00 | 80.6 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.32 | 1.24 | 2.42 | 0.00 | 8.1 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.00 | 15.03 | 19.97 | 2.00 | 83.1 | 77.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.04 | 12.39 | 18.23 | 1.00 | 82.7 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.5 | 4.23 | 11.45 | 16.35 | 5.00 | 80.2 | 90.0 |
| Bench 3 | Bench | Micky van de Ven | DEF | 18 | 4.7 | 3.59 | 10.74 | 16.97 | 2.00 | 80.7 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.0 | 3.60 | 9.88 | 13.65 | 3.00 | 78.6 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.25 | 24.08 | 37.50 | 8.00 | 83.2 | 90.0 |
| XI | XI | Viktor Gyökeres | FWD | 1 | 9.0 | 5.17 | 14.53 | 23.37 | 2.00 | 74.9 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.09 | 13.16 | 21.72 | 2.00 | 72.8 | 73.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.78 | 17.27 | 25.88 | 18.00 | 83.2 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.10 | 14.10 | 22.18 | 3.00 | 72.6 | 90.0 |
| XI | XI | Jack Grealish | MID | 9 | 6.9 | 3.84 | 11.98 | 18.96 | 10.00 | 69.5 | 90.0 |
| XI | XI | Jaidon Anthony | MID | 3 | 5.7 | 3.93 | 11.86 | 18.19 | 1.00 | 83.4 | 58.0 |
| Bench 4 | Bench | Anton Stach | MID | 11 | 5.0 | 3.18 | 9.83 | 14.70 | 2.00 | 76.2 | 66.0 |

## GW8

- Train rows: 166350
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 66.91
- Actual score: 84.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.66) beats the best remaining Triple Captain opportunity (8.34).
- Transfer: Jack Grealish -> Mohammed Kudus (projected gain 4.48, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (7.66) beats the best remaining Triple Captain opportunity (8.34).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.81 | 11.03 | 17.85 | 6.00 | 83.4 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.39 | 1.09 | 2.06 | 0.00 | 7.6 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.34 | 14.37 | 20.27 | 2.00 | 78.4 | 90.0 |
| Bench 3 | Bench | James Tarkowski | DEF | 9 | 5.5 | 3.52 | 12.07 | 16.75 | 3.00 | 81.1 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.96 | 11.47 | 14.87 | 17.00 | 77.9 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 3.58 | 9.55 | 16.03 | 0.00 | 81.1 | 90.0 |
| Bench 4 | Bench | Virgil van Dijk | DEF | 12 | 6.1 | 3.50 | 8.29 | 16.00 | 3.00 | 81.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 7.63 | 23.20 | 37.59 | 13.00 | 83.3 | 90.0 |
| XI | XI | Viktor Gyökeres | FWD | 1 | 9.0 | 4.09 | 12.57 | 20.40 | 2.00 | 66.8 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.61 | 12.56 | 22.54 | 2.00 | 77.5 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.8 | 6.70 | 18.83 | 30.62 | 4.00 | 83.3 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.28 | 14.89 | 21.92 | 8.00 | 74.2 | 84.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.8 | 5.07 | 14.52 | 21.80 | 2.00 | 83.3 | 90.0 |
| Bench 2 | Bench | Jaidon Anthony | MID | 3 | 5.7 | 3.57 | 10.06 | 16.20 | 2.00 | 69.0 | 82.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 3.58 | 9.66 | 15.02 | 2.00 | 72.9 | 72.0 |

## GW9

- Train rows: 167095
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 70.61
- Actual score: 63.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.66) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Virgil van Dijk -> Jurriën Timber (projected gain 2.04, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.66) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.92 | 11.25 | 18.14 | 6.00 | 83.4 | 90.0 |
| Bench 1 | Bench Boost | Antonín Kinský | GK | 18 | 3.9 | 0.29 | 0.97 | 1.90 | 0.00 | 6.8 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.57 | 13.29 | 19.23 | 5.00 | 83.2 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.0 | 4.39 | 12.52 | 19.45 | 6.00 | 73.3 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.5 | 3.92 | 11.41 | 17.69 | 1.00 | 83.1 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.87 | 11.07 | 16.82 | 2.00 | 80.7 | 90.0 |
| Bench 4 | Bench Boost | Micky van de Ven | DEF | 18 | 4.7 | 3.36 | 9.64 | 15.43 | 23.00 | 80.6 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.5 | 7.44 | 23.43 | 39.16 | 2.00 | 83.2 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.61 | 13.00 | 21.65 | 2.00 | 78.9 | 84.0 |
| XI | XI | Viktor Gyökeres | FWD | 1 | 9.0 | 4.26 | 12.61 | 21.03 | 2.00 | 69.3 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.9 | 6.35 | 17.84 | 27.82 | 3.00 | 83.2 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.74 | 13.67 | 21.64 | 4.00 | 80.7 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.8 | 4.47 | 13.15 | 20.31 | 3.00 | 77.4 | 77.0 |
| Bench 2 | Bench Boost | Jaidon Anthony | MID | 3 | 5.7 | 3.61 | 10.06 | 16.02 | 2.00 | 73.7 | 76.0 |
| Bench 3 | Bench Boost | Anton Stach | MID | 11 | 5.0 | 3.37 | 9.15 | 13.98 | 0.00 | 65.9 | 0.0 |