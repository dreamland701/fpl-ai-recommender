# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 271.24
- Total actual points: 264.00
- Average predicted points: 67.81
- Average actual points: 66.00
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
- Captain: Gabriel dos Santos Magalhães
- Vice captain: Cole Palmer
- Effective captain: Gabriel dos Santos Magalhães
- Chip used: none
- Predicted score: 68.95
- Actual score: 43.00
- Chip advisory: bench_boost (0.67): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 5.03 | 14.38 | 22.79 | 3.00 | 117.5 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 3.80 | 10.80 | 17.20 | 2.00 | 124.2 | 90.0 |
| Captain | Captain | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 7.13 | 20.53 | 31.69 | 2.00 | 138.8 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 5.46 | 15.21 | 23.21 | 3.00 | 116.3 | 56.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.90 | 14.14 | 22.68 | 11.00 | 94.4 | 90.0 |
| Bench 2 | Bench | Marc Guéhi | DEF | 13 | 5.2 | 4.82 | 13.75 | 21.23 | 2.00 | 93.2 | 90.0 |
| Bench 4 | Bench | Nordi Mukiele | DEF | 17 | 4.6 | 4.02 | 11.46 | 18.81 | 1.00 | 84.7 | 11.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 5.85 | 16.11 | 25.96 | 7.00 | 81.5 | 79.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 5.21 | 14.31 | 21.45 | 2.00 | 124.6 | 90.0 |
| Bench 3 | Bench | Adam Armstrong | FWD | 20 | 5.5 | 4.28 | 12.01 | 19.32 | 2.00 | 127.9 | 62.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.9 | 5.82 | 16.77 | 27.63 | 4.00 | 94.9 | 86.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.5 | 6.26 | 16.76 | 27.36 | 3.00 | 84.2 | 74.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.58 | 16.46 | 27.95 | 2.00 | 81.4 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.9 | 5.43 | 15.18 | 24.74 | 2.00 | 87.1 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 5.17 | 14.73 | 24.31 | 2.00 | 80.6 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 0.30 -> 0.90
- Free transfers: 2 -> 2
- Captain: Gabriel dos Santos Magalhães
- Vice captain: Antoine Semenyo
- Effective captain: Gabriel dos Santos Magalhães
- Chip used: none
- Predicted score: 59.78
- Actual score: 63.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Nordi Mukiele -> James Hill (projected gain 0.14, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.20 | 12.11 | 19.83 | 3.00 | 96.8 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 2.64 | 8.02 | 13.45 | 8.00 | 97.3 | 90.0 |
| Captain | Captain | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.77 | 16.77 | 26.81 | 9.00 | 110.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.87 | 13.66 | 22.13 | 7.00 | 88.5 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.44 | 13.12 | 20.92 | 6.00 | 87.3 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.0 | 4.27 | 11.85 | 18.40 | 2.00 | 92.1 | 90.0 |
| Bench 2 | Bench | Jurriën Timber | DEF | 1 | 6.4 | 4.08 | 11.80 | 18.87 | 8.00 | 83.2 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 5.28 | 16.17 | 26.15 | 2.00 | 81.6 | 90.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.6 | 3.99 | 11.63 | 18.10 | 2.00 | 99.1 | 90.0 |
| Bench 4 | Bench | Adam Armstrong | FWD | 20 | 5.5 | 2.96 | 8.70 | 14.58 | 4.00 | 82.2 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.9 | 5.61 | 16.60 | 26.99 | 8.00 | 88.9 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.38 | 15.45 | 26.16 | 13.00 | 82.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.5 | 4.91 | 14.94 | 24.57 | 1.00 | 77.7 | 85.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 5.10 | 14.39 | 23.33 | 2.00 | 83.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.9 | 4.18 | 13.26 | 22.02 | 1.00 | 81.0 | 85.0 |

## GW29

- Train rows: 182721
- Bank: 0.90 -> 1.80
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Bruno Borges Fernandes
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 66.90
- Actual score: 99.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.25) beats the best remaining Triple Captain opportunity (7.51).
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Enzo Fernández -> Harry Wilson (projected gain 2.41, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.25) beats the best remaining Triple Captain opportunity (7.51).
- Autosub: James Hill replaced Harry Wilson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.88 | 12.09 | 19.95 | 7.00 | 95.5 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 2.80 | 8.45 | 13.99 | 3.00 | 98.4 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.56 | 17.01 | 27.31 | 11.00 | 111.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.05 | 14.51 | 23.30 | 1.00 | 88.9 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.62 | 13.25 | 21.14 | 1.00 | 88.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 3.99 | 12.01 | 19.72 | 13.00 | 87.7 | 90.0 |
| Bench 2 | Autosub In | James Hill | DEF | 4 | 4.0 | 3.75 | 10.90 | 17.24 | 8.00 | 89.3 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 5.05 | 15.09 | 25.25 | 19.00 | 80.0 | 84.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.6 | 3.72 | 10.74 | 16.71 | 2.00 | 94.1 | 69.0 |
| Bench 4 | Bench | Adam Armstrong | FWD | 20 | 5.4 | 3.41 | 9.90 | 15.88 | 1.00 | 90.2 | 59.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.0 | 6.25 | 17.96 | 28.96 | 7.00 | 98.6 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 6.12 | 17.88 | 29.74 | 8.00 | 93.2 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.5 | 4.56 | 14.91 | 25.18 | 9.00 | 74.9 | 84.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 4.67 | 13.46 | 22.14 | 1.00 | 80.2 | 90.0 |
| XI | Bench | Harry Wilson | MID | 10 | 5.9 | 4.66 | 13.29 | 21.49 | 0.00 | 79.3 | 0.0 |

## GW30

- Train rows: 183541
- Bank: 1.80 -> 0.00
- Free transfers: 2 -> 2
- Captain: João Pedro Junqueira de Jesus
- Vice captain: Bruno Borges Fernandes
- Effective captain: João Pedro Junqueira de Jesus
- Chip used: bench_boost
- Predicted score: 75.60
- Actual score: 59.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.91) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Adam Armstrong -> Igor Thiago Nascimento Rodrigues (projected gain 2.09, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.91) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.07 | 12.06 | 19.88 | 7.00 | 92.0 | 90.0 |
| Bench 1 | Bench Boost | José Malheiro de Sá | GK | 20 | 4.2 | 2.61 | 7.94 | 13.26 | 0.00 | 86.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.22 | 15.58 | 26.01 | 9.00 | 98.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.13 | 14.75 | 23.80 | 2.00 | 86.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 4.30 | 12.67 | 20.73 | 1.00 | 85.9 | 37.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.23 | 12.23 | 19.87 | 2.00 | 84.8 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.0 | 4.02 | 11.15 | 18.25 | 8.00 | 86.2 | 90.0 |
| Captain | Captain | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 6.62 | 18.85 | 31.01 | 2.00 | 93.9 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 5.07 | 14.11 | 22.80 | 6.00 | 85.2 | 90.0 |
| Bench 4 | Bench Boost | Mateus Mané | FWD | 20 | 4.6 | 2.42 | 7.21 | 12.60 | 1.00 | 63.9 | 45.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.9 | 6.61 | 20.16 | 33.01 | 10.00 | 99.7 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 6.53 | 19.17 | 30.80 | 2.00 | 101.9 | 74.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.5 | 5.28 | 16.81 | 27.59 | 2.00 | 79.5 | 90.0 |
| Bench 2 | Bench Boost | Morgan Rogers | MID | 2 | 7.6 | 3.88 | 12.13 | 20.24 | 2.00 | 78.7 | 90.0 |
| Bench 3 | Bench Boost | Harry Wilson | MID | 10 | 5.9 | 3.00 | 9.41 | 16.00 | 3.00 | 46.7 | 90.0 |