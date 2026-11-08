# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 269.08
- Total actual points: 225.00
- Average predicted points: 67.27
- Average actual points: 56.25
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
- Bank: 100.00 -> 0.60
- Free transfers: 1 -> 2
- Captain: Cole Palmer
- Vice captain: Declan Rice
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 68.42
- Actual score: 40.00
- Chip advisory: bench_boost (0.67): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.79 | 13.55 | 21.99 | 3.00 | 115.5 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 3.44 | 10.19 | 16.63 | 2.00 | 118.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 6.48 | 18.56 | 28.42 | 2.00 | 134.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.81 | 13.88 | 22.89 | 11.00 | 99.8 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.77 | 12.93 | 20.24 | 2.00 | 95.7 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.8 | 4.85 | 12.70 | 20.76 | 2.00 | 85.2 | 90.0 |
| Bench 4 | Bench | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 4.17 | 12.27 | 18.54 | 4.00 | 115.6 | 90.0 |
| Bench 2 | Bench | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 4.73 | 15.68 | 25.04 | 2.00 | 94.7 | 90.0 |
| Bench 3 | Bench | Jarrod Bowen | FWD | 19 | 7.6 | 4.18 | 13.46 | 21.95 | 4.00 | 83.5 | 90.0 |
| XI | XI | Adam Armstrong | FWD | 20 | 5.5 | 4.76 | 12.90 | 20.01 | 2.00 | 131.8 | 62.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.6 | 7.05 | 18.66 | 31.86 | 3.00 | 88.3 | 74.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.6 | 6.48 | 17.66 | 27.64 | 4.00 | 114.7 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 6.43 | 16.32 | 26.41 | 4.00 | 105.3 | 86.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.9 | 5.68 | 15.37 | 25.29 | 2.00 | 82.3 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.27 | 14.13 | 22.77 | 2.00 | 86.7 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 0.60 -> 1.50
- Free transfers: 2 -> 2
- Captain: Declan Rice
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Declan Rice
- Chip used: none
- Predicted score: 61.98
- Actual score: 71.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Enzo Fernández -> Harry Wilson (projected gain 3.49, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.43 | 12.19 | 19.50 | 3.00 | 95.8 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 2.68 | 7.65 | 13.02 | 8.00 | 96.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.33 | 14.71 | 22.47 | 7.00 | 101.0 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.82 | 14.68 | 23.58 | 9.00 | 111.1 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.15 | 12.82 | 19.84 | 6.00 | 85.0 | 90.0 |
| Bench 2 | Bench | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 3.55 | 10.54 | 16.39 | 9.00 | 96.3 | 90.0 |
| Bench 4 | Bench | Trevoh Chalobah | DEF | 7 | 5.7 | 2.70 | 9.11 | 15.17 | 1.00 | 73.3 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.6 | 4.52 | 14.63 | 24.07 | 7.00 | 86.2 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.23 | 14.31 | 23.01 | 6.00 | 89.3 | 90.0 |
| Bench 3 | Bench | Adam Armstrong | FWD | 20 | 5.4 | 3.22 | 9.20 | 15.53 | 4.00 | 85.0 | 90.0 |
| Captain | Captain | Declan Rice | MID | 1 | 7.6 | 5.96 | 17.55 | 27.55 | 5.00 | 102.3 | 75.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.76 | 15.36 | 25.38 | 1.00 | 68.0 | 85.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.64 | 15.09 | 24.49 | 8.00 | 94.8 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 5.34 | 14.01 | 21.52 | 12.00 | 89.4 | 71.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.85 | 13.91 | 22.08 | 2.00 | 82.9 | 90.0 |

## GW29

- Train rows: 182721
- Bank: 1.50 -> 0.40
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 66.19
- Actual score: 61.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.72) beats the best remaining Triple Captain opportunity (7.93).
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Morgan Rogers -> Bryan Mbeumo (projected gain 2.22, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.72) beats the best remaining Triple Captain opportunity (7.93).
- Autosub: Adam Armstrong replaced Harry Wilson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.64 | 11.67 | 18.69 | 7.00 | 98.5 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 2.70 | 8.00 | 13.73 | 3.00 | 94.5 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.42 | 15.54 | 24.85 | 11.00 | 115.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.70 | 13.82 | 21.75 | 1.00 | 90.1 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.54 | 12.88 | 20.17 | 1.00 | 91.4 | 90.0 |
| Bench 4 | Bench | Trevoh Chalobah | DEF | 7 | 5.6 | 3.40 | 10.62 | 17.28 | 2.00 | 78.8 | 90.0 |
| Bench 3 | Bench | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 3.53 | 10.15 | 16.22 | 1.00 | 94.5 | 31.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 4.77 | 15.46 | 25.50 | 4.00 | 90.4 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.57 | 14.00 | 24.15 | 2.00 | 83.5 | 90.0 |
| Bench 2 | Autosub In | Adam Armstrong | FWD | 20 | 5.4 | 3.55 | 10.10 | 15.89 | 1.00 | 91.3 | 59.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.72 | 17.45 | 27.79 | 7.00 | 108.9 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.63 | 16.07 | 26.72 | 9.00 | 76.5 | 84.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.7 | 4.75 | 13.68 | 21.75 | 1.00 | 76.2 | 76.0 |
| XI | Bench | Harry Wilson | MID | 10 | 5.9 | 4.81 | 13.28 | 20.99 | 0.00 | 78.1 | 0.0 |
| XI | XI | Declan Rice | MID | 1 | 7.5 | 4.21 | 13.23 | 21.82 | 3.00 | 89.8 | 90.0 |

## GW30

- Train rows: 183541
- Bank: 0.40 -> 0.80
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Cole Palmer
- Effective captain: Antoine Semenyo
- Chip used: bench_boost
- Predicted score: 72.48
- Actual score: 53.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.82) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Harry Wilson -> Elliot Anderson (projected gain 2.41, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.82) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.53 | 12.48 | 20.34 | 7.00 | 95.2 | 90.0 |
| Bench 1 | Bench Boost | José Malheiro de Sá | GK | 20 | 4.2 | 2.74 | 7.62 | 13.00 | 0.00 | 85.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 4.77 | 13.82 | 23.46 | 9.00 | 99.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.89 | 13.34 | 21.05 | 2.00 | 82.7 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.10 | 11.09 | 17.74 | 2.00 | 85.5 | 90.0 |
| Bench 2 | Bench Boost | Trevoh Chalobah | DEF | 7 | 5.6 | 3.73 | 10.87 | 17.48 | 2.00 | 81.2 | 90.0 |
| Bench 4 | Bench Boost | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 2.23 | 6.33 | 10.74 | 1.00 | 56.6 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.01 | 15.23 | 24.18 | 6.00 | 90.2 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.13 | 14.14 | 22.36 | 6.00 | 90.4 | 90.0 |
| Bench 3 | Bench Boost | Adam Armstrong | FWD | 20 | 5.3 | 3.13 | 8.80 | 14.43 | 5.00 | 73.7 | 86.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.18 | 17.71 | 28.20 | 2.00 | 105.3 | 74.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.6 | 5.34 | 17.56 | 28.29 | 2.00 | 79.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.7 | 4.84 | 14.37 | 24.58 | 2.00 | 71.5 | 74.0 |
| XI | XI | Declan Rice | MID | 1 | 7.4 | 4.78 | 14.15 | 25.71 | 3.00 | 84.0 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.5 | 4.92 | 13.18 | 21.08 | 2.00 | 88.5 | 87.0 |