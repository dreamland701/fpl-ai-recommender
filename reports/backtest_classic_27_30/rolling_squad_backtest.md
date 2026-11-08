# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 271.34
- Total actual points: 258.00
- Average predicted points: 67.83
- Average actual points: 64.50
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
- Predicted score: 68.98
- Actual score: 43.00
- Chip advisory: bench_boost (0.67): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 5.05 | 14.46 | 23.04 | 3.00 | 117.4 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 3.79 | 10.80 | 17.16 | 2.00 | 124.2 | 90.0 |
| Captain | Captain | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 7.15 | 20.58 | 32.20 | 2.00 | 138.8 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 5.48 | 15.35 | 23.66 | 3.00 | 116.2 | 56.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.92 | 14.09 | 22.67 | 11.00 | 94.4 | 90.0 |
| Bench 2 | Bench | Marc Guéhi | DEF | 13 | 5.2 | 4.84 | 13.79 | 21.66 | 2.00 | 93.2 | 90.0 |
| Bench 4 | Bench | Nordi Mukiele | DEF | 17 | 4.6 | 4.01 | 11.47 | 18.67 | 1.00 | 84.7 | 11.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 5.82 | 16.09 | 25.83 | 7.00 | 81.5 | 79.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 5.20 | 14.46 | 21.92 | 2.00 | 124.7 | 90.0 |
| Bench 3 | Bench | Adam Armstrong | FWD | 20 | 5.5 | 4.27 | 11.99 | 19.15 | 2.00 | 127.9 | 62.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.9 | 5.84 | 16.78 | 27.46 | 4.00 | 94.9 | 86.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.5 | 6.22 | 16.71 | 27.11 | 3.00 | 84.2 | 74.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.58 | 16.40 | 27.40 | 2.00 | 81.4 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.9 | 5.40 | 15.12 | 24.56 | 2.00 | 87.1 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 5.17 | 14.72 | 24.09 | 2.00 | 80.6 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 0.30 -> 0.90
- Free transfers: 2 -> 2
- Captain: Gabriel dos Santos Magalhães
- Vice captain: Antoine Semenyo
- Effective captain: Gabriel dos Santos Magalhães
- Chip used: none
- Predicted score: 59.73
- Actual score: 63.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Nordi Mukiele -> James Hill (projected gain 0.16, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.19 | 12.09 | 19.85 | 3.00 | 96.9 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 2.61 | 7.98 | 13.32 | 8.00 | 97.3 | 90.0 |
| Captain | Captain | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.76 | 16.73 | 26.94 | 9.00 | 110.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.90 | 13.72 | 22.24 | 7.00 | 88.4 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.44 | 13.11 | 21.03 | 6.00 | 87.3 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.0 | 4.29 | 11.83 | 18.61 | 2.00 | 92.1 | 90.0 |
| Bench 2 | Bench | Jurriën Timber | DEF | 1 | 6.4 | 4.07 | 11.77 | 18.96 | 8.00 | 83.2 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.25 | 16.13 | 26.10 | 2.00 | 81.6 | 90.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.6 | 3.96 | 11.62 | 18.19 | 2.00 | 99.1 | 90.0 |
| Bench 4 | Bench | Adam Armstrong | FWD | 20 | 5.5 | 2.93 | 8.64 | 14.38 | 4.00 | 82.3 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.61 | 16.55 | 26.97 | 8.00 | 88.9 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.37 | 15.39 | 25.84 | 13.00 | 82.1 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.88 | 14.88 | 24.63 | 1.00 | 77.8 | 85.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.13 | 14.45 | 23.41 | 2.00 | 83.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.9 | 4.15 | 13.18 | 21.80 | 1.00 | 81.0 | 85.0 |

## GW29

- Train rows: 182721
- Bank: 0.90 -> 1.80
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Bruno Borges Fernandes
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 66.94
- Actual score: 93.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.27) beats the best remaining Triple Captain opportunity (7.53).
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Enzo Fernández -> Harry Wilson (projected gain 2.61, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.27) beats the best remaining Triple Captain opportunity (7.53).
- Autosub outfielders: Mateus Mané.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.87 | 12.05 | 19.92 | 7.00 | 95.5 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 2.81 | 8.44 | 13.93 | 3.00 | 98.4 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.54 | 16.96 | 27.32 | 11.00 | 111.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.08 | 14.58 | 23.46 | 1.00 | 88.8 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.64 | 13.33 | 21.32 | 1.00 | 88.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 3.97 | 11.97 | 19.61 | 13.00 | 87.7 | 90.0 |
| Bench 3 | Bench | James Hill | DEF | 4 | 4.1 | 3.73 | 10.92 | 17.45 | 8.00 | 89.4 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.02 | 15.02 | 25.02 | 19.00 | 80.1 | 84.0 |
| Bench 2 | Autosub In | Mateus Mané | FWD | 20 | 4.6 | 3.73 | 10.67 | 16.64 | 2.00 | 94.1 | 69.0 |
| Bench 4 | Bench | Adam Armstrong | FWD | 20 | 5.4 | 3.42 | 9.83 | 15.82 | 1.00 | 90.2 | 59.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.27 | 17.93 | 28.88 | 7.00 | 98.6 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.9 | 6.14 | 17.87 | 29.57 | 8.00 | 93.2 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.53 | 14.82 | 24.93 | 9.00 | 75.0 | 84.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.66 | 13.45 | 21.98 | 1.00 | 80.2 | 90.0 |
| XI | Bench | Harry Wilson | MID | 10 | 5.9 | 4.69 | 13.27 | 21.43 | 0.00 | 79.3 | 0.0 |

## GW30

- Train rows: 183541
- Bank: 1.80 -> 0.00
- Free transfers: 2 -> 2
- Captain: João Pedro Junqueira de Jesus
- Vice captain: Bruno Borges Fernandes
- Effective captain: João Pedro Junqueira de Jesus
- Chip used: bench_boost
- Predicted score: 75.68
- Actual score: 59.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.90) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Adam Armstrong -> Igor Thiago Nascimento Rodrigues (projected gain 2.05, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.90) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.07 | 12.03 | 19.80 | 7.00 | 92.0 | 90.0 |
| Bench 1 | Bench Boost | José Malheiro de Sá | GK | 20 | 4.2 | 2.59 | 7.93 | 13.23 | 0.00 | 86.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.21 | 15.58 | 26.01 | 9.00 | 98.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 5.15 | 14.81 | 23.92 | 2.00 | 85.9 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 4.29 | 12.61 | 20.61 | 1.00 | 85.9 | 37.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.26 | 12.28 | 19.95 | 2.00 | 84.7 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.1 | 3.99 | 11.21 | 18.48 | 8.00 | 86.3 | 90.0 |
| Captain | Captain | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 6.64 | 18.82 | 30.74 | 2.00 | 93.9 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 5.10 | 14.05 | 22.63 | 6.00 | 85.2 | 90.0 |
| Bench 4 | Bench Boost | Mateus Mané | FWD | 20 | 4.6 | 2.40 | 7.17 | 12.61 | 1.00 | 64.0 | 45.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 10.0 | 6.58 | 20.04 | 32.64 | 10.00 | 99.7 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.2 | 6.56 | 19.13 | 30.58 | 2.00 | 101.9 | 74.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.30 | 16.72 | 27.37 | 2.00 | 79.5 | 90.0 |
| Bench 2 | Bench Boost | Morgan Rogers | MID | 2 | 7.6 | 3.89 | 12.11 | 20.20 | 2.00 | 78.7 | 90.0 |
| Bench 3 | Bench Boost | Harry Wilson | MID | 10 | 6.0 | 3.01 | 9.32 | 15.80 | 3.00 | 46.6 | 90.0 |