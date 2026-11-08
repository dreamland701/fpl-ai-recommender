# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 277.59
- Total actual points: 266.00
- Average predicted points: 69.40
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
- Predicted score: 68.68
- Actual score: 43.00
- Chip advisory: bench_boost (0.67): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.83 | 13.69 | 21.65 | 3.00 | 114.8 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 3.42 | 10.16 | 16.48 | 2.00 | 120.2 | 90.0 |
| Captain | Captain | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 6.78 | 19.46 | 29.97 | 2.00 | 134.5 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 5.22 | 14.90 | 23.13 | 3.00 | 112.9 | 56.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.19 | 14.39 | 22.75 | 11.00 | 100.7 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.84 | 13.33 | 20.31 | 2.00 | 96.2 | 90.0 |
| Bench 4 | Bench | James Hill | DEF | 4 | 4.0 | 4.03 | 11.38 | 17.75 | 6.00 | 95.2 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.99 | 16.12 | 25.58 | 7.00 | 85.9 | 79.0 |
| Bench 2 | Bench | Mateus Mané | FWD | 20 | 4.6 | 4.79 | 13.31 | 19.92 | 2.00 | 120.1 | 90.0 |
| Bench 3 | Bench | Adam Armstrong | FWD | 20 | 5.5 | 4.49 | 12.67 | 20.40 | 2.00 | 132.1 | 62.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.6 | 6.54 | 17.57 | 28.64 | 3.00 | 88.3 | 74.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 6.32 | 17.38 | 28.08 | 4.00 | 106.8 | 86.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.64 | 16.43 | 27.73 | 2.00 | 83.1 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.53 | 15.00 | 24.33 | 2.00 | 88.7 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.9 | 5.02 | 14.18 | 23.14 | 2.00 | 81.4 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 0.40 -> 1.30
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Virgil van Dijk
- Effective captain: Antoine Semenyo
- Chip used: none
- Predicted score: 60.31
- Actual score: 73.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Enzo Fernández -> Harry Wilson (projected gain 1.74, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.03 | 11.50 | 18.78 | 3.00 | 92.4 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 2.68 | 7.98 | 13.40 | 8.00 | 98.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.71 | 16.24 | 25.73 | 9.00 | 108.4 | 90.0 |
| Vice Captain | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.91 | 15.23 | 23.85 | 7.00 | 101.6 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.20 | 12.19 | 19.32 | 6.00 | 85.2 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.0 | 4.24 | 11.59 | 17.86 | 2.00 | 92.9 | 90.0 |
| Bench 3 | Bench | Jurriën Timber | DEF | 1 | 6.4 | 3.93 | 11.58 | 18.85 | 8.00 | 78.9 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.29 | 13.69 | 22.31 | 2.00 | 65.1 | 90.0 |
| Bench 2 | Bench | Mateus Mané | FWD | 20 | 4.6 | 3.99 | 11.36 | 17.44 | 2.00 | 99.4 | 90.0 |
| Bench 4 | Bench | Adam Armstrong | FWD | 20 | 5.4 | 3.28 | 9.45 | 15.62 | 4.00 | 87.1 | 90.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.0 | 5.95 | 16.96 | 27.14 | 8.00 | 95.6 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.80 | 16.54 | 27.64 | 13.00 | 89.8 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.49 | 14.37 | 23.85 | 1.00 | 65.4 | 85.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.07 | 14.17 | 22.88 | 2.00 | 85.6 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.65 | 13.04 | 20.59 | 12.00 | 88.8 | 71.0 |

## GW29

- Train rows: 182721
- Bank: 1.30 -> 0.20
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Bruno Borges Fernandes
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 71.59
- Actual score: 93.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.99) beats the best remaining Triple Captain opportunity (8.25).
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Morgan Rogers -> Bryan Mbeumo (projected gain 2.76, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.99) beats the best remaining Triple Captain opportunity (8.25).
- Autosub: Mateus Mané replaced Harry Wilson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.07 | 12.07 | 19.66 | 7.00 | 98.2 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 2.69 | 8.05 | 13.42 | 3.00 | 95.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.88 | 17.30 | 27.41 | 11.00 | 115.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.39 | 14.70 | 23.10 | 1.00 | 91.5 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.88 | 13.40 | 21.02 | 1.00 | 94.2 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 4.51 | 13.19 | 21.62 | 13.00 | 94.5 | 90.0 |
| Bench 3 | Bench | James Hill | DEF | 4 | 4.0 | 3.56 | 10.34 | 16.25 | 8.00 | 88.1 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 5.17 | 14.93 | 24.54 | 19.00 | 82.7 | 84.0 |
| Bench 2 | Autosub In | Mateus Mané | FWD | 20 | 4.6 | 3.68 | 10.45 | 16.06 | 2.00 | 92.8 | 69.0 |
| Bench 4 | Bench | Adam Armstrong | FWD | 20 | 5.4 | 3.55 | 10.06 | 15.97 | 1.00 | 91.4 | 59.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.99 | 19.30 | 30.53 | 7.00 | 112.1 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.9 | 6.36 | 18.54 | 30.69 | 8.00 | 99.2 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.06 | 15.98 | 26.66 | 9.00 | 78.7 | 84.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.7 | 4.80 | 14.15 | 22.75 | 1.00 | 76.4 | 76.0 |
| XI | Bench | Harry Wilson | MID | 10 | 5.9 | 4.50 | 12.46 | 19.93 | 0.00 | 77.1 | 0.0 |

## GW30

- Train rows: 183541
- Bank: 0.20 -> 0.60
- Free transfers: 2 -> 2
- Captain: João Pedro Junqueira de Jesus
- Vice captain: Bruno Borges Fernandes
- Effective captain: João Pedro Junqueira de Jesus
- Chip used: bench_boost
- Predicted score: 77.00
- Actual score: 57.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.79) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Harry Wilson -> Elliot Anderson (projected gain 2.42, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.79) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.22 | 12.00 | 19.56 | 7.00 | 94.3 | 90.0 |
| Bench 1 | Bench Boost | José Malheiro de Sá | GK | 20 | 4.2 | 2.50 | 7.62 | 12.74 | 0.00 | 85.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.38 | 15.52 | 25.69 | 9.00 | 99.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 4.79 | 13.62 | 22.27 | 1.00 | 92.4 | 37.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.75 | 13.61 | 21.84 | 2.00 | 83.6 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.15 | 11.61 | 18.60 | 2.00 | 86.5 | 90.0 |
| Bench 2 | Bench Boost | James Hill | DEF | 4 | 4.1 | 3.94 | 10.76 | 17.48 | 8.00 | 87.9 | 90.0 |
| Captain | Captain | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.92 | 18.77 | 30.35 | 2.00 | 101.1 | 90.0 |
| Bench 3 | Bench Boost | Adam Armstrong | FWD | 20 | 5.3 | 2.91 | 8.65 | 14.17 | 5.00 | 73.0 | 86.0 |
| Bench 4 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 2.44 | 7.08 | 12.21 | 1.00 | 64.0 | 45.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.9 | 6.80 | 20.12 | 32.73 | 10.00 | 105.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 6.67 | 18.84 | 29.81 | 2.00 | 106.9 | 74.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.28 | 16.94 | 27.85 | 2.00 | 77.5 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.7 | 4.63 | 13.55 | 22.50 | 2.00 | 74.2 | 74.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.5 | 4.72 | 13.03 | 20.77 | 2.00 | 89.1 | 87.0 |