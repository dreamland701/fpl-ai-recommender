# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 261.83
- Total actual points: 224.00
- Average predicted points: 65.46
- Average actual points: 56.00
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
- Bank: 100.00 -> 0.30
- Free transfers: 1 -> 2
- Captain: Cole Palmer
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 67.15
- Actual score: 40.00
- Chip advisory: bench_boost (0.67): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.74 | 12.69 | 19.15 | 3.00 | 106.5 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 3.32 | 9.63 | 14.77 | 2.00 | 117.8 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 6.37 | 17.33 | 24.72 | 2.00 | 133.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.17 | 13.08 | 20.14 | 11.00 | 96.8 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.64 | 12.11 | 17.82 | 2.00 | 93.7 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.8 | 4.54 | 11.56 | 18.31 | 2.00 | 87.2 | 90.0 |
| Bench 3 | Bench | Nordi Mukiele | DEF | 17 | 4.6 | 4.27 | 10.72 | 16.87 | 1.00 | 87.8 | 11.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.03 | 12.55 | 22.14 | 2.00 | 92.7 | 90.0 |
| Bench 4 | Bench | Adam Armstrong | FWD | 20 | 5.5 | 4.25 | 11.85 | 18.07 | 2.00 | 130.8 | 62.0 |
| Bench 2 | Bench | Jarrod Bowen | FWD | 19 | 7.6 | 4.37 | 11.75 | 20.17 | 4.00 | 85.5 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.6 | 6.25 | 17.45 | 24.33 | 4.00 | 113.7 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.6 | 6.89 | 16.81 | 27.30 | 3.00 | 89.3 | 74.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 6.18 | 16.16 | 23.07 | 4.00 | 100.3 | 86.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.9 | 5.19 | 13.73 | 22.33 | 2.00 | 85.3 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.27 | 13.54 | 20.41 | 2.00 | 87.7 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 0.30 -> 1.20
- Free transfers: 2 -> 2
- Captain: Declan Rice
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Declan Rice
- Chip used: none
- Predicted score: 59.75
- Actual score: 71.00
- Transfer: Enzo Fernández -> Harry Wilson (projected gain 2.37, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.18 | 11.43 | 17.67 | 3.00 | 93.8 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 2.57 | 7.52 | 11.37 | 8.00 | 94.2 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.49 | 14.92 | 20.65 | 9.00 | 103.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.35 | 13.50 | 21.31 | 7.00 | 97.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.13 | 11.35 | 18.00 | 6.00 | 87.0 | 90.0 |
| Bench 3 | Bench | Trevoh Chalobah | DEF | 7 | 5.7 | 2.74 | 8.58 | 13.89 | 1.00 | 79.3 | 90.0 |
| Bench 4 | Bench | Nordi Mukiele | DEF | 17 | 4.6 | 1.57 | 5.22 | 8.09 | 0.00 | 30.4 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.09 | 13.38 | 21.46 | 6.00 | 89.3 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.6 | 4.22 | 12.79 | 21.24 | 7.00 | 87.2 | 90.0 |
| Bench 2 | Bench | Adam Armstrong | FWD | 20 | 5.4 | 3.12 | 8.95 | 13.47 | 4.00 | 87.0 | 90.0 |
| Captain | Captain | Declan Rice | MID | 1 | 7.6 | 5.82 | 16.23 | 24.95 | 5.00 | 98.3 | 75.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.18 | 14.97 | 21.80 | 8.00 | 92.8 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.52 | 14.02 | 23.04 | 1.00 | 76.0 | 85.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.20 | 13.00 | 20.92 | 2.00 | 81.9 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.74 | 12.96 | 20.00 | 12.00 | 89.4 | 71.0 |

## GW29

- Train rows: 182721
- Bank: 1.20 -> 0.10
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 66.56
- Actual score: 61.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.47) beats the best remaining Triple Captain opportunity (7.64).
- Transfer: Morgan Rogers -> Bryan Mbeumo (projected gain 2.00, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.47) beats the best remaining Triple Captain opportunity (7.64).
- Autosub: Adam Armstrong replaced Harry Wilson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.83 | 10.02 | 17.26 | 7.00 | 95.5 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 2.58 | 7.05 | 11.76 | 3.00 | 92.5 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.24 | 14.97 | 21.78 | 11.00 | 114.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.15 | 12.71 | 20.14 | 1.00 | 90.1 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.57 | 11.22 | 18.34 | 1.00 | 91.4 | 90.0 |
| Bench 3 | Bench | Trevoh Chalobah | DEF | 7 | 5.6 | 3.19 | 9.70 | 15.78 | 2.00 | 82.8 | 90.0 |
| Bench 4 | Bench | Nordi Mukiele | DEF | 17 | 4.5 | 1.01 | 3.88 | 7.74 | 0.00 | 24.4 | 0.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.11 | 13.58 | 22.62 | 4.00 | 90.4 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.60 | 12.55 | 20.71 | 2.00 | 85.5 | 90.0 |
| Bench 2 | Autosub In | Adam Armstrong | FWD | 20 | 5.4 | 3.35 | 9.08 | 14.39 | 1.00 | 90.3 | 59.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.47 | 16.63 | 24.98 | 7.00 | 98.9 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.76 | 14.54 | 24.56 | 9.00 | 81.5 | 84.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.7 | 5.03 | 12.97 | 20.07 | 1.00 | 81.2 | 76.0 |
| XI | Bench | Harry Wilson | MID | 10 | 5.9 | 4.64 | 12.36 | 19.24 | 0.00 | 82.1 | 0.0 |
| XI | XI | Declan Rice | MID | 1 | 7.5 | 4.23 | 12.34 | 19.19 | 3.00 | 89.8 | 90.0 |

## GW30

- Train rows: 183541
- Bank: 0.10 -> 0.50
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Cole Palmer
- Effective captain: Antoine Semenyo
- Chip used: bench_boost
- Predicted score: 68.37
- Actual score: 52.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.45) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Harry Wilson -> Elliot Anderson (projected gain 2.66, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.45) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.04 | 10.85 | 18.15 | 7.00 | 93.2 | 90.0 |
| Bench 1 | Bench Boost | José Malheiro de Sá | GK | 20 | 4.2 | 2.40 | 7.08 | 11.40 | 0.00 | 87.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 4.73 | 12.79 | 20.38 | 9.00 | 96.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.06 | 12.68 | 19.08 | 2.00 | 85.7 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.05 | 10.41 | 15.89 | 2.00 | 87.5 | 90.0 |
| Bench 2 | Bench Boost | Trevoh Chalobah | DEF | 7 | 5.6 | 3.59 | 9.72 | 15.48 | 2.00 | 84.2 | 90.0 |
| Bench 4 | Bench Boost | Nordi Mukiele | DEF | 17 | 4.5 | 0.59 | 2.36 | 5.42 | 0.00 | 12.2 | 0.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 4.64 | 13.50 | 22.17 | 6.00 | 90.2 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.05 | 13.07 | 20.64 | 6.00 | 90.4 | 90.0 |
| Bench 3 | Bench Boost | Adam Armstrong | FWD | 20 | 5.3 | 2.86 | 8.16 | 13.08 | 5.00 | 79.7 | 86.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.00 | 16.10 | 24.84 | 2.00 | 95.3 | 74.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.6 | 5.54 | 15.39 | 25.09 | 2.00 | 83.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.7 | 4.52 | 12.78 | 21.33 | 2.00 | 77.5 | 74.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.5 | 4.49 | 12.28 | 19.01 | 2.00 | 89.5 | 87.0 |
| XI | XI | Declan Rice | MID | 1 | 7.4 | 4.80 | 12.20 | 21.65 | 3.00 | 83.0 | 90.0 |