# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 272.71
- Total actual points: 238.00
- Average predicted points: 68.18
- Average actual points: 59.50
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW26 are included before the first simulated week.
- League-average scores were not available for this run.

## GW27

- Train rows: 181084
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Erling Haaland
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 71.28
- Actual score: 54.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.77 | 13.23 | 20.95 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.00 | 0.15 | 0.00 | 1.5 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 6.91 | 19.38 | 29.79 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.93 | 14.00 | 22.35 | 11.00 | 90.0 | 90.0 |
| XI | XI | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 4.23 | 11.66 | 18.22 | 4.00 | 90.0 | 90.0 |
| Bench 3 | Bench | James Hill | DEF | 4 | 4.0 | 3.90 | 11.28 | 17.77 | 6.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Hugo Bueno López | DEF | 20 | 4.3 | 3.94 | 11.28 | 18.43 | 4.00 | 90.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 7.29 | 20.86 | 34.47 | 6.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.15 | 16.25 | 25.61 | 7.00 | 83.3 | 79.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 4.86 | 13.34 | 20.02 | 2.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.6 | 6.57 | 18.79 | 29.41 | 4.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 6.74 | 18.11 | 29.25 | 3.00 | 87.2 | 74.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 6.29 | 17.25 | 27.82 | 4.00 | 90.0 | 86.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.9 | 5.24 | 14.53 | 23.53 | 2.00 | 83.2 | 90.0 |
| Bench 4 | Bench | Freddie Potts | MID | 19 | 4.4 | 2.03 | 5.41 | 8.52 | 0.00 | 47.9 | 0.0 |

## GW28

- Train rows: 181902
- Bank: 0.00 -> 0.90
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Declan Rice
- Chip used: none
- Predicted score: 65.18
- Actual score: 62.00
- Transfer: Enzo Fernández -> Harry Wilson (projected gain 2.27, hit 0)
- Autosub: Hugo Bueno López replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.00 | 11.41 | 18.57 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.23 | 0.20 | 0.38 | 0.00 | 2.6 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.81 | 16.47 | 26.04 | 9.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.33 | 14.46 | 22.84 | 7.00 | 90.0 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.0 | 4.50 | 12.14 | 18.43 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Autosub In | Hugo Bueno López | DEF | 20 | 4.3 | 3.69 | 11.01 | 17.50 | 6.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 3.52 | 10.33 | 15.87 | 9.00 | 90.0 | 90.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.8 | 7.90 | 22.72 | 36.82 | 0.00 | 90.0 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.45 | 13.88 | 22.51 | 2.00 | 68.6 | 90.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 3.93 | 11.60 | 17.82 | 2.00 | 90.0 | 90.0 |
| Vice Captain | Captain | Declan Rice | MID | 1 | 7.6 | 6.11 | 17.79 | 27.97 | 5.00 | 90.0 | 75.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.89 | 16.73 | 26.52 | 8.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.69 | 14.92 | 24.62 | 1.00 | 69.8 | 85.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.69 | 13.26 | 20.78 | 12.00 | 87.1 | 71.0 |
| Bench 4 | Bench | Freddie Potts | MID | 19 | 4.4 | 0.98 | 3.16 | 5.23 | 0.00 | 24.5 | 0.0 |

## GW29

- Train rows: 182721
- Bank: 0.90 -> 0.00
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 66.81
- Actual score: 77.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.55) beats the best remaining Triple Captain opportunity (7.73).
- Transfer: Yerson Mosquera Valdelamar -> Marc Guéhi (projected gain 2.05, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.55) beats the best remaining Triple Captain opportunity (7.73).
- Autosub: Hugo Bueno López replaced Harry Wilson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.79 | 11.55 | 18.82 | 7.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.08 | 0.08 | 0.26 | 0.00 | 0.9 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.64 | 16.93 | 26.92 | 11.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.10 | 14.23 | 22.50 | 1.00 | 87.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.59 | 12.75 | 20.13 | 1.00 | 88.5 | 90.0 |
| Bench 2 | Autosub In | Hugo Bueno López | DEF | 20 | 4.3 | 3.67 | 10.71 | 17.09 | 1.00 | 90.0 | 11.0 |
| Bench 3 | Bench | James Hill | DEF | 4 | 4.0 | 3.62 | 10.42 | 16.38 | 8.00 | 88.0 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.7 | 5.28 | 16.61 | 28.76 | 2.00 | 54.7 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.84 | 14.48 | 23.86 | 19.00 | 78.3 | 84.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 3.72 | 10.67 | 16.60 | 2.00 | 90.0 | 69.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.55 | 18.33 | 29.16 | 7.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.86 | 16.01 | 26.74 | 9.00 | 78.2 | 84.0 |
| XI | XI | Declan Rice | MID | 1 | 7.5 | 4.82 | 15.11 | 24.54 | 3.00 | 90.0 | 90.0 |
| XI | Bench | Harry Wilson | MID | 10 | 5.9 | 4.53 | 12.61 | 20.14 | 0.00 | 77.0 | 0.0 |
| Bench 4 | Bench | Freddie Potts | MID | 19 | 4.4 | 0.69 | 2.25 | 3.57 | 0.00 | 16.6 | 0.0 |

## GW30

- Train rows: 183541
- Bank: 0.00 -> 0.40
- Free transfers: 2 -> 2
- Captain: João Pedro Junqueira de Jesus
- Vice captain: Antoine Semenyo
- Effective captain: João Pedro Junqueira de Jesus
- Chip used: bench_boost
- Predicted score: 69.45
- Actual score: 45.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (4.99) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Harry Wilson -> Elliot Anderson (projected gain 5.86, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (4.99) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.02 | 11.54 | 18.86 | 7.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.13 | 0.22 | 0.00 | 1.5 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.29 | 15.31 | 25.41 | 9.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.12 | 14.00 | 22.27 | 2.00 | 83.3 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 3.97 | 11.22 | 18.01 | 2.00 | 82.9 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.1 | 4.13 | 10.99 | 17.68 | 8.00 | 86.4 | 90.0 |
| Bench 3 | Bench Boost | Hugo Bueno López | DEF | 20 | 4.3 | 2.42 | 7.56 | 12.95 | 1.00 | 58.3 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.6 | 6.28 | 19.26 | 32.20 | 2.00 | 83.9 | 90.0 |
| Captain | Captain | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.92 | 18.74 | 30.28 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 2.45 | 7.26 | 12.52 | 1.00 | 63.6 | 45.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 8.1 | 6.46 | 18.51 | 29.33 | 2.00 | 90.0 | 74.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.75 | 17.33 | 28.40 | 2.00 | 83.9 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.4 | 4.90 | 14.09 | 23.38 | 3.00 | 84.4 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.5 | 4.71 | 13.11 | 20.90 | 2.00 | 88.5 | 87.0 |
| Bench 4 | Bench Boost | Freddie Potts | MID | 19 | 4.4 | 0.12 | 0.69 | 1.98 | 0.00 | 5.1 | 0.0 |