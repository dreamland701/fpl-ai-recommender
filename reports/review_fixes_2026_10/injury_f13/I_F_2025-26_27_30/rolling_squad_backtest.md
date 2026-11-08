# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 283.53
- Total actual points: 271.00
- Average predicted points: 70.88
- Average actual points: 67.75
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
- Vice captain: Cole Palmer
- Effective captain: Gabriel dos Santos Magalhães
- Chip used: none
- Predicted score: 70.21
- Actual score: 43.00
- Chip advisory: bench_boost (0.67): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.94 | 13.84 | 21.86 | 3.00 | 115.7 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 3.41 | 10.09 | 16.38 | 2.00 | 119.1 | 90.0 |
| Captain | Captain | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 6.88 | 19.50 | 30.02 | 2.00 | 134.9 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 5.35 | 15.12 | 23.46 | 3.00 | 113.4 | 56.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.04 | 14.20 | 22.56 | 11.00 | 99.8 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.91 | 13.49 | 20.53 | 2.00 | 95.4 | 90.0 |
| Bench 4 | Bench | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 4.27 | 11.81 | 18.42 | 4.00 | 115.7 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.33 | 16.65 | 26.27 | 7.00 | 86.0 | 79.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.38 | 14.46 | 23.27 | 2.00 | 94.3 | 90.0 |
| Bench 2 | Bench | Mateus Mané | FWD | 20 | 4.6 | 4.87 | 13.31 | 19.97 | 2.00 | 120.6 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.6 | 6.79 | 17.99 | 29.18 | 3.00 | 88.5 | 74.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 6.51 | 17.78 | 28.58 | 4.00 | 104.6 | 86.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.60 | 16.52 | 27.90 | 2.00 | 81.6 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.59 | 15.15 | 24.51 | 2.00 | 86.3 | 90.0 |
| Bench 3 | Bench | Elliot Anderson | MID | 16 | 5.4 | 4.35 | 12.07 | 19.59 | 5.00 | 82.5 | 76.0 |

## GW28

- Train rows: 181902
- Bank: 0.10 -> 1.60
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Bruno Borges Fernandes
- Effective captain: Antoine Semenyo
- Chip used: none
- Predicted score: 61.73
- Actual score: 66.00
- Chip advisory: bench_boost (0.62): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Jurriën Timber -> Marcos Senesi Barón (projected gain 0.01, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.15 | 11.81 | 19.18 | 3.00 | 96.0 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 2.53 | 7.75 | 13.03 | 8.00 | 96.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.77 | 16.40 | 25.94 | 9.00 | 111.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.66 | 14.73 | 23.16 | 7.00 | 101.1 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.23 | 12.21 | 19.27 | 6.00 | 84.7 | 90.0 |
| Bench 2 | Bench | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.16 | 10.93 | 17.59 | 4.00 | 86.2 | 90.0 |
| Bench 4 | Bench | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 3.51 | 10.18 | 15.62 | 9.00 | 96.4 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.57 | 14.79 | 23.69 | 6.00 | 89.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.47 | 14.16 | 22.94 | 2.00 | 67.6 | 90.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.6 | 3.84 | 11.26 | 17.24 | 2.00 | 96.9 | 90.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.0 | 6.05 | 17.03 | 27.14 | 8.00 | 94.0 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.84 | 16.56 | 27.61 | 13.00 | 88.1 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.58 | 14.66 | 24.25 | 1.00 | 68.2 | 85.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.17 | 14.27 | 22.86 | 2.00 | 82.6 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.19 | 12.22 | 19.56 | 1.00 | 79.4 | 90.0 |

## GW29

- Train rows: 182721
- Bank: 1.60 -> 1.70
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Bruno Borges Fernandes
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 70.45
- Actual score: 94.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.88) beats the best remaining Triple Captain opportunity (8.29).
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Morgan Rogers -> Declan Rice (projected gain 3.71, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.88) beats the best remaining Triple Captain opportunity (8.29).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.00 | 12.01 | 19.54 | 7.00 | 98.6 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 2.55 | 7.81 | 13.10 | 3.00 | 94.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.70 | 17.03 | 27.03 | 11.00 | 115.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.32 | 14.38 | 22.59 | 1.00 | 90.1 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.73 | 13.07 | 20.54 | 1.00 | 91.0 | 90.0 |
| Bench 2 | Bench | Marcos Senesi Barón | DEF | 4 | 4.9 | 3.80 | 10.75 | 17.11 | 11.00 | 88.9 | 90.0 |
| Bench 4 | Bench | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 3.49 | 10.05 | 15.83 | 1.00 | 94.6 | 31.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 5.08 | 14.91 | 24.50 | 19.00 | 81.0 | 84.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.85 | 14.24 | 22.79 | 2.00 | 83.1 | 90.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.6 | 3.65 | 10.45 | 16.07 | 2.00 | 92.6 | 69.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.88 | 18.96 | 30.01 | 7.00 | 108.2 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.9 | 6.76 | 18.64 | 30.67 | 8.00 | 97.8 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.81 | 15.77 | 26.36 | 9.00 | 76.6 | 84.0 |
| XI | XI | Declan Rice | MID | 1 | 7.5 | 4.76 | 15.18 | 24.57 | 3.00 | 89.1 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.82 | 11.68 | 18.59 | 12.00 | 80.0 | 90.0 |

## GW30

- Train rows: 183541
- Bank: 1.70 -> 1.80
- Free transfers: 2 -> 2
- Captain: João Pedro Junqueira de Jesus
- Vice captain: Bruno Borges Fernandes
- Effective captain: João Pedro Junqueira de Jesus
- Chip used: bench_boost
- Predicted score: 81.13
- Actual score: 68.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.19) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Yerson Mosquera Valdelamar -> James Hill (projected gain 0.10, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.19) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.22 | 12.01 | 19.58 | 7.00 | 95.3 | 90.0 |
| Bench 1 | Bench Boost | José Malheiro de Sá | GK | 20 | 4.2 | 2.56 | 7.72 | 12.89 | 0.00 | 85.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.29 | 15.36 | 25.49 | 9.00 | 99.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.11 | 14.01 | 22.27 | 2.00 | 82.7 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.48 | 11.95 | 18.89 | 10.00 | 94.0 | 90.0 |
| Bench 2 | Bench Boost | Marc Guéhi | DEF | 13 | 5.2 | 4.10 | 11.58 | 18.54 | 2.00 | 85.1 | 90.0 |
| Bench 3 | Bench Boost | James Hill | DEF | 4 | 4.2 | 4.03 | 10.72 | 17.32 | 8.00 | 85.0 | 90.0 |
| Captain | Captain | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 7.31 | 19.26 | 31.02 | 2.00 | 101.7 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.45 | 14.66 | 23.25 | 6.00 | 90.1 | 90.0 |
| Bench 4 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 2.50 | 7.21 | 12.41 | 1.00 | 64.9 | 45.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.9 | 6.87 | 20.53 | 33.26 | 10.00 | 101.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 6.64 | 18.99 | 30.01 | 2.00 | 104.5 | 74.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.61 | 16.99 | 27.85 | 2.00 | 79.8 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.4 | 4.96 | 14.18 | 23.49 | 3.00 | 83.3 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.70 | 12.88 | 20.49 | 2.00 | 87.9 | 87.0 |