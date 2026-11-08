# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 221.83
- Total actual points: 225.00
- Average predicted points: 55.46
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
- Predicted score: 56.36
- Actual score: 40.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.94 | 11.45 | 18.78 | 3.00 | 106.5 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 2.90 | 8.64 | 14.10 | 2.00 | 117.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.22 | 15.62 | 24.20 | 2.00 | 133.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.94 | 11.72 | 19.60 | 11.00 | 96.8 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 3.92 | 10.88 | 17.20 | 2.00 | 93.7 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.8 | 4.06 | 10.81 | 17.80 | 2.00 | 87.2 | 90.0 |
| Bench 4 | Bench | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 3.46 | 10.46 | 15.76 | 4.00 | 114.6 | 90.0 |
| Bench 2 | Bench | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 3.80 | 13.50 | 21.68 | 2.00 | 92.7 | 90.0 |
| Bench 3 | Bench | Jarrod Bowen | FWD | 19 | 7.6 | 3.46 | 11.50 | 18.80 | 4.00 | 85.5 | 90.0 |
| XI | XI | Adam Armstrong | FWD | 20 | 5.5 | 4.00 | 10.98 | 16.99 | 2.00 | 130.8 | 62.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.6 | 5.82 | 15.95 | 27.75 | 3.00 | 89.3 | 74.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.6 | 5.31 | 14.83 | 23.51 | 4.00 | 113.7 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.27 | 13.66 | 22.41 | 4.00 | 100.3 | 86.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.9 | 4.78 | 13.18 | 21.90 | 2.00 | 85.3 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.30 | 11.86 | 19.27 | 2.00 | 87.7 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 0.60 -> 1.50
- Free transfers: 2 -> 2
- Captain: Declan Rice
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Declan Rice
- Chip used: none
- Predicted score: 51.36
- Actual score: 71.00
- Transfer: Enzo Fernández -> Harry Wilson (projected gain 3.15, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.74 | 10.52 | 16.71 | 3.00 | 93.8 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 2.31 | 6.41 | 10.85 | 8.00 | 94.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.35 | 12.73 | 19.28 | 7.00 | 97.0 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 4.81 | 12.52 | 20.10 | 9.00 | 103.1 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 3.44 | 11.10 | 17.05 | 6.00 | 87.0 | 90.0 |
| Bench 2 | Bench | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 2.99 | 9.05 | 13.97 | 9.00 | 94.3 | 90.0 |
| Bench 4 | Bench | Trevoh Chalobah | DEF | 7 | 5.7 | 2.25 | 7.66 | 12.67 | 1.00 | 79.3 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.6 | 3.81 | 12.75 | 20.99 | 7.00 | 87.2 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 4.29 | 12.34 | 19.80 | 6.00 | 89.3 | 90.0 |
| Bench 3 | Bench | Adam Armstrong | FWD | 20 | 5.4 | 2.73 | 7.79 | 13.13 | 4.00 | 87.0 | 90.0 |
| Captain | Captain | Declan Rice | MID | 1 | 7.6 | 4.91 | 15.27 | 23.92 | 5.00 | 98.3 | 75.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 3.99 | 13.39 | 22.09 | 1.00 | 76.0 | 85.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 4.60 | 12.88 | 20.93 | 8.00 | 92.8 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.52 | 12.17 | 18.55 | 12.00 | 89.4 | 71.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 3.98 | 12.00 | 18.95 | 2.00 | 81.9 | 90.0 |

## GW29

- Train rows: 182721
- Bank: 1.50 -> 0.40
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 54.37
- Actual score: 61.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.52) beats the best remaining Triple Captain opportunity (6.51).
- Transfer: Morgan Rogers -> Bryan Mbeumo (projected gain 1.85, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (5.52) beats the best remaining Triple Captain opportunity (6.51).
- Autosub: Adam Armstrong replaced Harry Wilson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 2.99 | 9.90 | 15.85 | 7.00 | 95.5 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 2.34 | 6.77 | 11.63 | 3.00 | 92.5 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 4.43 | 13.12 | 21.16 | 11.00 | 114.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 3.79 | 11.75 | 18.57 | 1.00 | 90.1 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 3.74 | 10.97 | 17.22 | 1.00 | 91.4 | 90.0 |
| Bench 4 | Bench | Trevoh Chalobah | DEF | 7 | 5.6 | 2.88 | 9.08 | 14.75 | 2.00 | 82.8 | 90.0 |
| Bench 3 | Bench | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 2.98 | 8.63 | 13.80 | 1.00 | 92.5 | 31.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 3.92 | 13.35 | 22.23 | 4.00 | 90.4 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.77 | 11.96 | 20.98 | 2.00 | 85.5 | 90.0 |
| Bench 2 | Autosub In | Adam Armstrong | FWD | 20 | 5.4 | 2.99 | 8.59 | 13.47 | 1.00 | 90.3 | 59.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 5.52 | 14.81 | 23.81 | 7.00 | 98.9 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 3.82 | 13.81 | 23.12 | 9.00 | 81.5 | 84.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.7 | 3.90 | 11.64 | 18.57 | 1.00 | 81.2 | 76.0 |
| XI | Bench | Harry Wilson | MID | 10 | 5.9 | 4.04 | 11.42 | 18.07 | 0.00 | 82.1 | 0.0 |
| XI | XI | Declan Rice | MID | 1 | 7.5 | 3.42 | 11.06 | 18.43 | 3.00 | 89.8 | 90.0 |

## GW30

- Train rows: 183541
- Bank: 0.40 -> 0.80
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Cole Palmer
- Effective captain: Antoine Semenyo
- Chip used: bench_boost
- Predicted score: 59.74
- Actual score: 53.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.01) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Harry Wilson -> Elliot Anderson (projected gain 2.02, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.01) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.81 | 10.61 | 17.28 | 7.00 | 93.2 | 90.0 |
| Bench 1 | Bench Boost | José Malheiro de Sá | GK | 20 | 4.2 | 2.35 | 6.38 | 10.82 | 0.00 | 87.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 3.82 | 11.45 | 19.61 | 9.00 | 96.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 3.99 | 11.18 | 17.64 | 2.00 | 85.7 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 3.41 | 9.28 | 14.83 | 2.00 | 87.5 | 90.0 |
| Bench 2 | Bench Boost | Trevoh Chalobah | DEF | 7 | 5.6 | 3.11 | 9.23 | 14.79 | 2.00 | 84.2 | 90.0 |
| Bench 4 | Bench Boost | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 1.88 | 5.21 | 8.64 | 1.00 | 39.6 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 4.17 | 13.05 | 20.65 | 6.00 | 90.2 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.18 | 11.90 | 18.85 | 6.00 | 90.4 | 90.0 |
| Bench 3 | Bench Boost | Adam Armstrong | FWD | 20 | 5.3 | 2.66 | 7.41 | 12.07 | 5.00 | 79.7 | 86.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.6 | 4.33 | 14.95 | 24.14 | 2.00 | 83.6 | 90.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 4.98 | 14.84 | 23.80 | 2.00 | 95.3 | 74.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.7 | 4.05 | 12.28 | 21.16 | 2.00 | 77.5 | 74.0 |
| XI | XI | Declan Rice | MID | 1 | 7.4 | 3.91 | 11.97 | 22.16 | 3.00 | 83.0 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.5 | 4.10 | 11.18 | 17.90 | 2.00 | 89.5 | 87.0 |