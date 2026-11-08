# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 245.79
- Total actual points: 225.00
- Average predicted points: 61.45
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
- Predicted score: 61.94
- Actual score: 40.00
- Chip advisory: bench_boost (0.62): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.40 | 12.80 | 21.04 | 3.00 | 115.5 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 3.36 | 9.99 | 16.35 | 2.00 | 118.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.69 | 16.97 | 26.45 | 2.00 | 134.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.41 | 13.07 | 21.85 | 11.00 | 99.8 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.38 | 12.23 | 19.46 | 2.00 | 95.7 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.8 | 4.52 | 12.16 | 20.05 | 2.00 | 85.2 | 90.0 |
| Bench 4 | Bench | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 3.92 | 11.82 | 18.01 | 4.00 | 115.6 | 90.0 |
| Bench 2 | Bench | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 4.27 | 14.86 | 23.93 | 2.00 | 94.7 | 90.0 |
| Bench 3 | Bench | Jarrod Bowen | FWD | 19 | 7.6 | 3.93 | 12.86 | 21.06 | 4.00 | 83.5 | 90.0 |
| XI | XI | Adam Armstrong | FWD | 20 | 5.5 | 4.47 | 12.33 | 19.25 | 2.00 | 131.8 | 62.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.6 | 6.28 | 17.30 | 30.01 | 3.00 | 88.3 | 74.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.6 | 5.78 | 16.18 | 25.76 | 4.00 | 114.7 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.73 | 15.01 | 24.66 | 4.00 | 105.3 | 86.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.9 | 5.24 | 14.54 | 24.16 | 2.00 | 82.3 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.77 | 13.22 | 21.53 | 2.00 | 86.7 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 0.60 -> 1.50
- Free transfers: 2 -> 2
- Captain: Declan Rice
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Declan Rice
- Chip used: none
- Predicted score: 56.74
- Actual score: 71.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Enzo Fernández -> Harry Wilson (projected gain 3.15, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.19 | 11.85 | 18.95 | 3.00 | 95.8 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 2.76 | 7.74 | 13.10 | 8.00 | 96.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.80 | 14.06 | 21.53 | 7.00 | 101.0 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.26 | 13.85 | 22.35 | 9.00 | 111.1 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 3.89 | 12.43 | 19.30 | 6.00 | 85.0 | 90.0 |
| Bench 2 | Bench | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 3.44 | 10.38 | 16.21 | 9.00 | 96.3 | 90.0 |
| Bench 4 | Bench | Trevoh Chalobah | DEF | 7 | 5.7 | 2.69 | 9.00 | 14.92 | 1.00 | 73.3 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.6 | 4.25 | 14.08 | 23.24 | 7.00 | 86.2 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 4.74 | 13.67 | 22.04 | 6.00 | 89.3 | 90.0 |
| Bench 3 | Bench | Adam Armstrong | FWD | 20 | 5.4 | 3.18 | 9.12 | 15.37 | 4.00 | 85.0 | 90.0 |
| Captain | Captain | Declan Rice | MID | 1 | 7.6 | 5.36 | 16.61 | 26.16 | 5.00 | 102.3 | 75.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.44 | 14.72 | 24.33 | 1.00 | 68.0 | 85.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.05 | 14.21 | 23.18 | 8.00 | 94.8 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.97 | 13.50 | 20.80 | 12.00 | 89.4 | 71.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.43 | 13.33 | 21.19 | 2.00 | 82.9 | 90.0 |

## GW29

- Train rows: 182721
- Bank: 1.50 -> 0.40
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 60.09
- Actual score: 61.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.96) beats the best remaining Triple Captain opportunity (7.03).
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Morgan Rogers -> Bryan Mbeumo (projected gain 1.85, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (5.96) beats the best remaining Triple Captain opportunity (7.03).
- Autosub: Adam Armstrong replaced Harry Wilson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.43 | 11.22 | 18.03 | 7.00 | 98.5 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 2.78 | 8.10 | 13.81 | 3.00 | 94.5 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 4.87 | 14.44 | 23.34 | 11.00 | 115.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.23 | 13.07 | 20.75 | 1.00 | 90.1 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.18 | 12.29 | 19.40 | 1.00 | 91.4 | 90.0 |
| Bench 4 | Bench | Trevoh Chalobah | DEF | 7 | 5.6 | 3.31 | 10.40 | 16.93 | 2.00 | 78.8 | 90.0 |
| Bench 3 | Bench | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 3.42 | 9.95 | 15.99 | 1.00 | 94.5 | 31.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 4.36 | 14.68 | 24.41 | 4.00 | 90.4 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.21 | 13.29 | 23.16 | 2.00 | 83.5 | 90.0 |
| Bench 2 | Autosub In | Adam Armstrong | FWD | 20 | 5.4 | 3.43 | 9.91 | 15.65 | 1.00 | 91.3 | 59.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 5.96 | 16.13 | 25.99 | 7.00 | 108.9 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.26 | 15.13 | 25.30 | 9.00 | 76.5 | 84.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.7 | 4.34 | 12.96 | 20.75 | 1.00 | 76.2 | 76.0 |
| XI | Bench | Harry Wilson | MID | 10 | 5.9 | 4.48 | 12.74 | 20.25 | 0.00 | 78.1 | 0.0 |
| XI | XI | Declan Rice | MID | 1 | 7.5 | 3.85 | 12.39 | 20.61 | 3.00 | 89.8 | 90.0 |

## GW30

- Train rows: 183541
- Bank: 0.40 -> 0.80
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Cole Palmer
- Effective captain: Antoine Semenyo
- Chip used: bench_boost
- Predicted score: 67.01
- Actual score: 53.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.83) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Harry Wilson -> Elliot Anderson (projected gain 2.02, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.83) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.26 | 11.96 | 19.57 | 7.00 | 95.2 | 90.0 |
| Bench 1 | Bench Boost | José Malheiro de Sá | GK | 20 | 4.2 | 2.81 | 7.73 | 13.11 | 0.00 | 85.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 4.28 | 12.80 | 21.90 | 9.00 | 99.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.45 | 12.53 | 19.93 | 2.00 | 82.7 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 3.86 | 10.63 | 17.11 | 2.00 | 85.5 | 90.0 |
| Bench 2 | Bench Boost | Trevoh Chalobah | DEF | 7 | 5.6 | 3.56 | 10.58 | 17.08 | 2.00 | 81.2 | 90.0 |
| Bench 4 | Bench Boost | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 2.34 | 6.56 | 10.93 | 1.00 | 56.6 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 4.63 | 14.40 | 22.94 | 6.00 | 90.2 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.63 | 13.25 | 21.14 | 6.00 | 90.4 | 90.0 |
| Bench 3 | Bench Boost | Adam Armstrong | FWD | 20 | 5.3 | 3.12 | 8.76 | 14.36 | 5.00 | 73.7 | 86.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.6 | 4.78 | 16.30 | 26.42 | 2.00 | 79.6 | 90.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 5.43 | 16.19 | 26.08 | 2.00 | 105.3 | 74.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.7 | 4.50 | 13.63 | 23.44 | 2.00 | 71.5 | 74.0 |
| XI | XI | Declan Rice | MID | 1 | 7.4 | 4.37 | 13.32 | 24.44 | 3.00 | 84.0 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.5 | 4.55 | 12.53 | 20.19 | 2.00 | 88.5 | 87.0 |