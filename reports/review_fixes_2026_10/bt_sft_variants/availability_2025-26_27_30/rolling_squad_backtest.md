# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 279.57
- Total actual points: 266.00
- Average predicted points: 69.89
- Average actual points: 66.50
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
- Bank: 100.00 -> 0.40
- Free transfers: 1 -> 2
- Captain: Gabriel dos Santos Magalhães
- Vice captain: Cole Palmer
- Effective captain: Gabriel dos Santos Magalhães
- Chip used: none
- Predicted score: 69.80
- Actual score: 43.00
- Chip advisory: bench_boost (0.67): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.94 | 13.85 | 21.88 | 3.00 | 106.5 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 3.40 | 10.04 | 16.30 | 2.00 | 117.8 | 90.0 |
| Captain | Captain | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 6.92 | 19.62 | 30.20 | 2.00 | 133.5 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 5.33 | 15.06 | 23.38 | 3.00 | 105.0 | 56.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.04 | 14.22 | 22.60 | 11.00 | 96.8 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.92 | 13.48 | 20.50 | 2.00 | 93.7 | 90.0 |
| Bench 4 | Bench | James Hill | DEF | 4 | 4.0 | 3.99 | 11.30 | 17.73 | 6.00 | 93.5 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.27 | 16.50 | 26.07 | 7.00 | 87.2 | 79.0 |
| Bench 2 | Bench | Mateus Mané | FWD | 20 | 4.6 | 4.85 | 13.25 | 19.86 | 2.00 | 119.4 | 90.0 |
| Bench 3 | Bench | Adam Armstrong | FWD | 20 | 5.5 | 4.50 | 12.58 | 20.29 | 2.00 | 130.8 | 62.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.6 | 6.82 | 18.05 | 29.25 | 3.00 | 89.3 | 74.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 6.47 | 17.66 | 28.41 | 4.00 | 100.3 | 86.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.50 | 16.30 | 27.60 | 2.00 | 84.9 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.50 | 14.96 | 24.27 | 2.00 | 87.7 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.9 | 5.18 | 14.38 | 23.40 | 2.00 | 85.3 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 0.40 -> 1.30
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Antoine Semenyo
- Chip used: none
- Predicted score: 60.89
- Actual score: 73.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Enzo Fernández -> Harry Wilson (projected gain 1.52, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.14 | 11.82 | 19.21 | 3.00 | 93.8 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 2.51 | 7.71 | 12.95 | 8.00 | 94.2 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.81 | 16.52 | 26.10 | 9.00 | 103.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.65 | 14.73 | 23.18 | 7.00 | 97.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.24 | 12.20 | 19.25 | 6.00 | 87.0 | 90.0 |
| Bench 2 | Bench | Jurriën Timber | DEF | 1 | 6.4 | 4.04 | 11.91 | 19.30 | 8.00 | 85.3 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.0 | 4.41 | 11.84 | 18.13 | 2.00 | 90.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.39 | 13.99 | 22.71 | 2.00 | 66.9 | 90.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.6 | 3.82 | 11.19 | 17.14 | 2.00 | 94.8 | 90.0 |
| Bench 4 | Bench | Adam Armstrong | FWD | 20 | 5.4 | 3.13 | 9.29 | 15.33 | 4.00 | 87.0 | 90.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.0 | 6.00 | 16.88 | 26.93 | 8.00 | 92.8 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.75 | 16.35 | 27.33 | 13.00 | 89.4 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.59 | 14.69 | 24.29 | 1.00 | 76.0 | 85.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.08 | 14.10 | 22.65 | 2.00 | 81.9 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.82 | 13.37 | 20.95 | 12.00 | 89.4 | 71.0 |

## GW29

- Train rows: 182721
- Bank: 1.30 -> 0.20
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Bruno Borges Fernandes
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 70.72
- Actual score: 93.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.82) beats the best remaining Triple Captain opportunity (8.18).
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Morgan Rogers -> Bryan Mbeumo (projected gain 2.85, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.82) beats the best remaining Triple Captain opportunity (8.18).
- Autosub: Mateus Mané replaced Harry Wilson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.99 | 12.00 | 19.55 | 7.00 | 95.5 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 2.54 | 7.77 | 13.03 | 3.00 | 92.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.73 | 17.12 | 27.16 | 11.00 | 114.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.29 | 14.35 | 22.57 | 1.00 | 90.1 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 4.38 | 13.09 | 21.47 | 13.00 | 92.7 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.74 | 13.07 | 20.52 | 1.00 | 91.4 | 90.0 |
| Bench 3 | Bench | James Hill | DEF | 4 | 4.0 | 3.57 | 10.37 | 16.23 | 8.00 | 87.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 5.00 | 14.72 | 24.25 | 19.00 | 80.3 | 84.0 |
| Bench 2 | Autosub In | Mateus Mané | FWD | 20 | 4.6 | 3.63 | 10.39 | 15.98 | 2.00 | 91.5 | 69.0 |
| Bench 4 | Bench | Adam Armstrong | FWD | 20 | 5.4 | 3.49 | 9.99 | 15.87 | 1.00 | 90.3 | 59.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.82 | 18.81 | 29.81 | 7.00 | 98.9 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.9 | 6.66 | 18.43 | 30.40 | 8.00 | 95.1 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.82 | 15.81 | 26.42 | 9.00 | 81.5 | 84.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.7 | 5.00 | 14.14 | 22.67 | 1.00 | 81.2 | 76.0 |
| XI | Bench | Harry Wilson | MID | 10 | 5.9 | 4.64 | 12.72 | 20.27 | 0.00 | 82.1 | 0.0 |

## GW30

- Train rows: 183541
- Bank: 0.20 -> 0.60
- Free transfers: 2 -> 2
- Captain: João Pedro Junqueira de Jesus
- Vice captain: Bruno Borges Fernandes
- Effective captain: João Pedro Junqueira de Jesus
- Chip used: bench_boost
- Predicted score: 78.16
- Actual score: 57.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (12.05) beats the best remaining Bench Boost opportunity (0.00).
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Harry Wilson -> Elliot Anderson (projected gain 2.24, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (12.05) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.21 | 12.01 | 19.58 | 7.00 | 93.2 | 90.0 |
| Bench 1 | Bench Boost | José Malheiro de Sá | GK | 20 | 4.2 | 2.55 | 7.68 | 12.82 | 0.00 | 87.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.32 | 15.45 | 25.61 | 9.00 | 96.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.09 | 13.98 | 22.24 | 2.00 | 85.7 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 4.74 | 13.55 | 22.19 | 1.00 | 92.2 | 37.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.11 | 11.58 | 18.53 | 2.00 | 87.5 | 90.0 |
| Bench 2 | Bench Boost | James Hill | DEF | 4 | 4.1 | 4.05 | 10.80 | 17.45 | 8.00 | 65.6 | 90.0 |
| Captain | Captain | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 7.21 | 19.05 | 30.74 | 2.00 | 101.1 | 90.0 |
| Bench 3 | Bench Boost | Adam Armstrong | FWD | 20 | 5.3 | 2.96 | 8.71 | 14.27 | 5.00 | 79.7 | 86.0 |
| Bench 4 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 2.48 | 7.15 | 12.31 | 1.00 | 73.8 | 45.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.9 | 6.76 | 20.28 | 32.93 | 10.00 | 97.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 6.58 | 18.84 | 29.80 | 2.00 | 95.3 | 74.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.63 | 17.05 | 27.94 | 2.00 | 83.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.7 | 4.55 | 13.48 | 22.36 | 2.00 | 77.5 | 74.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.5 | 4.70 | 12.88 | 20.50 | 2.00 | 89.5 | 87.0 |