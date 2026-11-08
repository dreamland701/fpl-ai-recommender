# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 266.01
- Total actual points: 230.00
- Average predicted points: 66.50
- Average actual points: 57.50
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
- Captain: Gabriel dos Santos Magalhães
- Vice captain: Erling Haaland
- Effective captain: Gabriel dos Santos Magalhães
- Chip used: none
- Predicted score: 69.10
- Actual score: 45.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.94 | 13.54 | 20.88 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 1.9 | 0.0 |
| Captain | Captain | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 6.86 | 19.72 | 30.00 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.90 | 13.92 | 22.19 | 11.00 | 90.0 | 90.0 |
| XI | XI | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 4.34 | 12.22 | 18.86 | 4.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Hugo Bueno López | DEF | 20 | 4.3 | 3.98 | 11.64 | 18.63 | 4.00 | 90.0 | 90.0 |
| Bench 3 | Bench | James Hill | DEF | 4 | 4.0 | 3.92 | 11.26 | 17.46 | 6.00 | 90.0 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.8 | 6.70 | 19.51 | 31.93 | 6.00 | 84.5 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.28 | 14.74 | 23.53 | 2.00 | 90.0 | 90.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 4.86 | 13.67 | 20.44 | 2.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.6 | 6.54 | 18.68 | 28.76 | 4.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 6.60 | 17.13 | 27.92 | 3.00 | 85.4 | 74.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 6.14 | 16.73 | 26.65 | 4.00 | 90.0 | 86.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.9 | 5.07 | 14.02 | 22.64 | 2.00 | 84.7 | 90.0 |
| Bench 4 | Bench | Alex Scott | MID | 4 | 5.0 | 3.73 | 10.51 | 16.82 | 5.00 | 82.1 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 0.10 -> 1.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Declan Rice
- Chip used: none
- Predicted score: 64.19
- Actual score: 63.00
- Transfer: Enzo Fernández -> Harry Wilson (projected gain 1.27, hit 0)
- Autosub: Mateus Mané replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.00 | 11.54 | 18.52 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 1.7 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.60 | 16.35 | 25.75 | 9.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.43 | 14.15 | 22.08 | 7.00 | 90.0 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.0 | 4.24 | 11.34 | 17.39 | 2.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Hugo Bueno López | DEF | 20 | 4.3 | 3.60 | 10.90 | 17.41 | 6.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 3.48 | 10.43 | 16.21 | 9.00 | 90.0 | 90.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.8 | 7.39 | 21.42 | 34.04 | 0.00 | 90.0 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.42 | 14.74 | 23.67 | 6.00 | 86.3 | 90.0 |
| Bench 2 | Autosub In | Mateus Mané | FWD | 20 | 4.6 | 3.78 | 11.60 | 18.02 | 2.00 | 90.0 | 90.0 |
| Vice Captain | Captain | Declan Rice | MID | 1 | 7.6 | 6.00 | 17.81 | 27.59 | 5.00 | 90.0 | 75.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.75 | 15.92 | 25.12 | 8.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.61 | 14.05 | 23.42 | 1.00 | 67.2 | 85.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.50 | 12.83 | 20.17 | 12.00 | 87.3 | 71.0 |
| XI | XI | Alex Scott | MID | 4 | 5.0 | 3.85 | 10.64 | 17.22 | 3.00 | 81.1 | 90.0 |

## GW29

- Train rows: 182721
- Bank: 1.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 64.40
- Actual score: 71.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.39) beats the best remaining Triple Captain opportunity (7.54).
- Transfer: Alex Scott -> Elliot Anderson (projected gain 1.02, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.39) beats the best remaining Triple Captain opportunity (7.54).
- Autosub: Mateus Mané replaced Harry Wilson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.87 | 11.67 | 18.92 | 7.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 1.3 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.51 | 16.67 | 26.28 | 11.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.22 | 13.99 | 21.73 | 1.00 | 88.9 | 90.0 |
| XI | XI | Hugo Bueno López | DEF | 20 | 4.3 | 3.49 | 10.27 | 16.16 | 1.00 | 90.0 | 11.0 |
| Bench 3 | Bench | James Hill | DEF | 4 | 4.0 | 3.48 | 9.98 | 15.62 | 8.00 | 86.8 | 90.0 |
| Bench 4 | Bench | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 3.37 | 9.83 | 15.42 | 1.00 | 90.0 | 31.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.7 | 4.49 | 15.35 | 26.10 | 2.00 | 44.1 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.73 | 13.79 | 22.18 | 2.00 | 82.9 | 90.0 |
| Bench 2 | Autosub In | Mateus Mané | FWD | 20 | 4.6 | 3.65 | 10.63 | 16.26 | 2.00 | 90.0 | 69.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.39 | 17.97 | 28.25 | 7.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.04 | 15.87 | 26.35 | 9.00 | 79.0 | 84.0 |
| XI | XI | Declan Rice | MID | 1 | 7.5 | 4.59 | 14.49 | 23.21 | 3.00 | 89.6 | 90.0 |
| XI | Bench | Harry Wilson | MID | 10 | 5.9 | 4.50 | 12.61 | 20.10 | 0.00 | 78.6 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.78 | 11.63 | 18.77 | 12.00 | 79.0 | 90.0 |

## GW30

- Train rows: 183541
- Bank: 0.60 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 68.32
- Actual score: 51.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.22) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Harry Wilson -> Ismaïla Sarr (projected gain 4.52, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.22) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.98 | 11.69 | 18.82 | 7.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.01 | 0.00 | 2.3 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.07 | 15.14 | 24.49 | 9.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.94 | 13.30 | 21.18 | 2.00 | 83.7 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.1 | 3.86 | 10.54 | 16.93 | 8.00 | 85.6 | 90.0 |
| Bench 3 | Bench Boost | Hugo Bueno López | DEF | 20 | 4.3 | 2.32 | 6.82 | 11.93 | 1.00 | 56.5 | 90.0 |
| Bench 4 | Bench Boost | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 2.32 | 6.39 | 11.37 | 1.00 | 55.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 6.31 | 19.04 | 30.97 | 2.00 | 85.5 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.24 | 14.25 | 22.18 | 6.00 | 89.3 | 90.0 |
| Bench 2 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 2.58 | 7.05 | 12.10 | 1.00 | 65.5 | 45.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 8.1 | 6.24 | 17.80 | 28.62 | 2.00 | 90.0 | 74.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.80 | 17.47 | 27.93 | 2.00 | 85.9 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.4 | 4.84 | 13.89 | 22.60 | 3.00 | 85.5 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.44 | 12.95 | 20.51 | 2.00 | 87.1 | 87.0 |
| XI | XI | Ismaïla Sarr | MID | 8 | 6.3 | 4.07 | 11.53 | 18.23 | 3.00 | 84.7 | 90.0 |