# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW5
- Simulated weeks: GW6-GW9
- Total predicted points: 271.26
- Total actual points: 294.00
- Average predicted points: 67.81
- Average actual points: 73.50
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
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 64.97
- Actual score: 70.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 4.70 | 13.85 | 23.54 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Freddie Woodman | GK | 12 | 3.9 | 0.00 | 0.00 | 0.71 | 0.00 | 6.4 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.59 | 15.10 | 22.00 | 7.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Trevoh Chalobah | DEF | 7 | 5.2 | 3.28 | 14.30 | 20.91 | -3.00 | 90.0 | 52.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 4.13 | 14.11 | 21.71 | 13.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Marc Guéhi | DEF | 8 | 4.7 | 3.32 | 12.30 | 18.56 | 7.00 | 85.7 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.56 | 12.28 | 18.59 | 2.00 | 78.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 6.61 | 19.55 | 33.01 | 16.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 5.74 | 16.22 | 27.17 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.71 | 8.50 | 15.08 | 2.00 | 78.7 | 79.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.7 | 6.26 | 16.92 | 26.81 | 7.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 6.01 | 16.52 | 27.54 | -1.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.1 | 4.61 | 14.32 | 24.16 | 2.00 | 69.1 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.10 | 13.70 | 23.43 | 2.00 | 86.8 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 5.03 | 13.61 | 22.07 | 2.00 | 90.0 | 82.0 |

## GW7

- Train rows: 165607
- Bank: 0.70 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 63.84
- Actual score: 88.00
- Transfer: Trevoh Chalobah -> Jurriën Timber (projected gain 2.66, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 4.10 | 13.18 | 21.92 | 6.00 | 82.7 | 90.0 |
| Bench 1 | Bench | Freddie Woodman | GK | 12 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 6.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 5.80 | 17.07 | 24.98 | 9.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 4.77 | 15.37 | 20.28 | 2.00 | 85.1 | 77.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.7 | 4.92 | 15.13 | 21.74 | 3.00 | 90.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 5.8 | 5.15 | 13.82 | 21.95 | 11.00 | 70.8 | 90.0 |
| Bench 2 | Bench | Micky van de Ven | DEF | 18 | 4.7 | 3.85 | 11.27 | 17.93 | 2.00 | 79.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.19 | 21.01 | 34.26 | 8.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.76 | 14.71 | 24.39 | 2.00 | 72.1 | 73.0 |
| Bench 4 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.92 | 8.69 | 14.41 | 1.00 | 66.5 | 68.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.7 | 6.10 | 17.53 | 25.44 | 18.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.15 | 13.02 | 20.26 | 3.00 | 69.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.1 | 4.36 | 12.52 | 20.81 | 6.00 | 70.7 | 76.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.34 | 12.00 | 18.28 | 12.00 | 73.9 | 89.0 |
| Bench 3 | Bench | Tijjani Reijnders | MID | 13 | 5.7 | 3.70 | 10.53 | 15.41 | 3.00 | 66.5 | 75.0 |

## GW8

- Train rows: 166350
- Bank: 0.10 -> 0.00
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Erling Haaland
- Effective captain: Antoine Semenyo
- Chip used: bench_boost
- Predicted score: 71.53
- Actual score: 73.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.88) beats the best remaining Bench Boost opportunity (11.41).
- Transfer: Tijjani Reijnders -> Moisés Caicedo Corozo (projected gain 1.16, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.88) beats the best remaining Bench Boost opportunity (11.41).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 4.29 | 13.22 | 22.01 | 6.00 | 85.5 | 90.0 |
| Bench 1 | Bench Boost | Freddie Woodman | GK | 12 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 6.3 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 5.8 | 5.72 | 16.35 | 25.03 | 6.00 | 80.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.2 | 5.48 | 16.29 | 24.95 | 12.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 3.88 | 14.17 | 19.66 | 2.00 | 77.7 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.06 | 11.45 | 20.59 | 4.00 | 90.0 | 90.0 |
| Bench 3 | Bench Boost | Micky van de Ven | DEF | 18 | 4.7 | 3.74 | 10.45 | 16.88 | 0.00 | 83.2 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.4 | 6.70 | 22.45 | 35.38 | 13.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.46 | 14.74 | 23.01 | 2.00 | 76.8 | 90.0 |
| Bench 4 | Bench Boost | Lyle Foster | FWD | 3 | 5.0 | 2.29 | 9.22 | 14.02 | 0.00 | 57.4 | 0.0 |
| Captain | Captain | Antoine Semenyo | MID | 4 | 7.8 | 6.95 | 18.54 | 29.24 | 4.00 | 90.0 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.29 | 15.75 | 22.60 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 3.85 | 14.10 | 20.56 | 8.00 | 73.5 | 84.0 |
| Bench 2 | Bench Boost | Bryan Mbeumo | MID | 14 | 8.0 | 3.82 | 12.27 | 20.15 | 9.00 | 65.2 | 90.0 |
| XI | XI | Moisés Caicedo Corozo | MID | 7 | 5.8 | 4.06 | 11.51 | 17.21 | 1.00 | 90.0 | 45.0 |

## GW9

- Train rows: 167095
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 70.93
- Actual score: 63.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.21) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Moisés Caicedo Corozo -> Elliot Anderson (projected gain 0.05, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (7.21) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 4.24 | 12.97 | 21.39 | 6.00 | 85.4 | 90.0 |
| Bench 1 | Bench | Freddie Woodman | GK | 12 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 6.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.2 | 6.11 | 17.21 | 26.86 | 9.00 | 90.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 5.9 | 5.10 | 15.45 | 23.82 | 6.00 | 72.6 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 5.10 | 13.25 | 20.17 | 5.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 3.66 | 12.49 | 19.78 | 4.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Micky van de Ven | DEF | 18 | 4.7 | 3.46 | 9.73 | 15.63 | 23.00 | 79.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.5 | 7.18 | 22.15 | 36.29 | 2.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.97 | 13.98 | 22.28 | 2.00 | 78.3 | 84.0 |
| Bench 4 | Bench | Lyle Foster | FWD | 3 | 5.0 | 1.54 | 2.46 | 6.06 | 7.00 | 17.6 | 13.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.9 | 6.51 | 18.59 | 27.76 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.0 | 4.69 | 13.58 | 22.32 | 15.00 | 84.6 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.47 | 13.49 | 21.19 | 4.00 | 82.8 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.51 | 13.14 | 19.54 | 3.00 | 76.7 | 77.0 |
| Bench 2 | Bench | Elliot Anderson | MID | 16 | 5.3 | 3.58 | 11.59 | 16.45 | 2.00 | 79.9 | 90.0 |