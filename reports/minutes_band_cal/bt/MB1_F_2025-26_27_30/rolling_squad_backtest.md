# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 255.08
- Total actual points: 234.00
- Average predicted points: 63.77
- Average actual points: 58.50
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
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Erling Haaland
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 66.92
- Actual score: 54.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.29 | 11.84 | 19.07 | 3.00 | 83.1 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.5 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 6.42 | 17.96 | 27.87 | 2.00 | 83.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.42 | 12.57 | 20.30 | 11.00 | 83.1 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.8 | 4.71 | 12.24 | 19.52 | 2.00 | 83.1 | 90.0 |
| Bench 3 | Bench | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 3.68 | 9.99 | 15.87 | 4.00 | 83.1 | 90.0 |
| Bench 4 | Bench | Hugo Bueno López | DEF | 20 | 4.3 | 3.38 | 9.62 | 16.07 | 4.00 | 83.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 6.81 | 19.51 | 32.60 | 6.00 | 83.1 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.21 | 16.27 | 25.55 | 7.00 | 82.8 | 79.0 |
| Bench 2 | Bench | Mateus Mané | FWD | 20 | 4.6 | 4.30 | 11.66 | 17.65 | 2.00 | 83.1 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.6 | 6.09 | 17.35 | 27.46 | 4.00 | 83.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.82 | 15.92 | 25.98 | 4.00 | 83.1 | 86.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.58 | 15.04 | 24.23 | 2.00 | 84.6 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.9 | 5.31 | 14.55 | 23.48 | 2.00 | 82.8 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.45 | 12.19 | 19.61 | 5.00 | 82.2 | 76.0 |

## GW28

- Train rows: 181902
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Declan Rice
- Chip used: none
- Predicted score: 59.91
- Actual score: 46.00
- Transfer: none
- No transfer was applied this week.
- Autosub: Mateus Mané replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.50 | 10.00 | 16.66 | 3.00 | 83.1 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.6 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.31 | 15.05 | 24.12 | 9.00 | 83.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.84 | 13.02 | 20.81 | 7.00 | 83.1 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.7 | 3.14 | 9.68 | 16.22 | 1.00 | 76.9 | 90.0 |
| Bench 3 | Bench | Hugo Bueno López | DEF | 20 | 4.3 | 3.12 | 9.33 | 15.14 | 6.00 | 83.1 | 90.0 |
| Bench 4 | Bench | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 2.96 | 8.64 | 13.52 | 9.00 | 83.1 | 90.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.8 | 7.36 | 21.14 | 34.84 | 0.00 | 83.1 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.53 | 14.06 | 22.85 | 2.00 | 72.0 | 90.0 |
| Bench 2 | Autosub In | Mateus Mané | FWD | 20 | 4.6 | 3.36 | 9.91 | 15.45 | 2.00 | 83.1 | 90.0 |
| Vice Captain | Captain | Declan Rice | MID | 1 | 7.6 | 5.60 | 16.35 | 26.02 | 5.00 | 83.1 | 75.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.35 | 15.17 | 24.55 | 8.00 | 83.1 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.23 | 14.21 | 22.64 | 2.00 | 82.2 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.20 | 12.27 | 19.58 | 1.00 | 80.5 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.8 | 3.49 | 11.54 | 19.49 | 1.00 | 72.7 | 85.0 |

## GW29

- Train rows: 182721
- Bank: 0.10 -> -0.00
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Erling Haaland
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 61.83
- Actual score: 96.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.09) beats the best remaining Triple Captain opportunity (7.19).
- Transfer: Trevoh Chalobah -> James Tarkowski (projected gain 0.83, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.09) beats the best remaining Triple Captain opportunity (7.19).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.31 | 10.18 | 16.94 | 7.00 | 83.1 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.4 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.15 | 15.54 | 25.00 | 11.00 | 83.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.62 | 12.83 | 20.49 | 1.00 | 80.8 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.26 | 11.12 | 17.19 | 15.00 | 84.0 | 90.0 |
| Bench 3 | Bench | Hugo Bueno López | DEF | 20 | 4.3 | 3.10 | 9.17 | 14.82 | 1.00 | 83.1 | 11.0 |
| Bench 4 | Bench | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 2.92 | 8.50 | 13.69 | 1.00 | 83.1 | 31.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.7 | 5.46 | 17.14 | 29.48 | 2.00 | 57.8 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.88 | 14.49 | 23.81 | 19.00 | 79.9 | 84.0 |
| Bench 2 | Bench | Mateus Mané | FWD | 20 | 4.6 | 3.15 | 9.11 | 14.31 | 2.00 | 83.1 | 69.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.09 | 17.07 | 27.37 | 7.00 | 83.1 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.5 | 4.32 | 13.72 | 22.63 | 3.00 | 83.1 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.95 | 11.91 | 18.80 | 12.00 | 79.6 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 4.06 | 11.62 | 19.41 | 1.00 | 73.4 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 3.55 | 11.31 | 18.91 | 4.00 | 74.0 | 78.0 |

## GW30

- Train rows: 183541
- Bank: -0.00 -> -0.00
- Free transfers: 2 -> 2
- Captain: João Pedro Junqueira de Jesus
- Vice captain: Erling Haaland
- Effective captain: João Pedro Junqueira de Jesus
- Chip used: bench_boost
- Predicted score: 66.43
- Actual score: 38.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.48) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.48) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.57 | 10.21 | 17.03 | 7.00 | 83.2 | 90.0 |
| Bench 1 | Bench Boost | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 1.1 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.25 | 14.09 | 22.23 | 2.00 | 83.3 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 4.83 | 13.96 | 23.53 | 9.00 | 83.2 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 2.85 | 9.10 | 15.15 | 0.00 | 79.3 | 0.0 |
| Bench 2 | Bench Boost | Hugo Bueno López | DEF | 20 | 4.3 | 2.52 | 7.76 | 13.20 | 1.00 | 61.5 | 90.0 |
| Bench 4 | Bench Boost | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 2.45 | 7.16 | 12.59 | 1.00 | 59.0 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 6.44 | 19.50 | 32.35 | 2.00 | 82.9 | 90.0 |
| Captain | Captain | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.45 | 17.35 | 28.33 | 2.00 | 83.2 | 90.0 |
| Bench 3 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 2.51 | 7.34 | 12.61 | 1.00 | 66.7 | 45.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 6.03 | 17.22 | 27.54 | 2.00 | 83.2 | 74.0 |
| XI | XI | Declan Rice | MID | 1 | 7.4 | 5.04 | 14.27 | 23.49 | 3.00 | 83.5 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.6 | 4.13 | 12.19 | 19.81 | 2.00 | 77.8 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.20 | 11.58 | 18.72 | 2.00 | 81.9 | 87.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 3.73 | 11.31 | 18.72 | 2.00 | 79.0 | 90.0 |