# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 230.99
- Total actual points: 266.00
- Average predicted points: 57.75
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
- Predicted score: 57.43
- Actual score: 43.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.08 | 11.74 | 18.67 | 3.00 | 115.5 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 2.86 | 8.49 | 13.77 | 2.00 | 118.8 | 90.0 |
| Captain | Captain | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.67 | 16.67 | 25.98 | 2.00 | 134.5 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.40 | 12.78 | 19.99 | 3.00 | 114.0 | 56.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.17 | 12.06 | 19.30 | 11.00 | 99.8 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.07 | 11.43 | 17.46 | 2.00 | 95.7 | 90.0 |
| Bench 4 | Bench | James Hill | DEF | 4 | 4.0 | 3.33 | 9.56 | 15.02 | 6.00 | 95.5 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.14 | 14.01 | 22.35 | 7.00 | 86.2 | 79.0 |
| Bench 2 | Bench | Mateus Mané | FWD | 20 | 4.6 | 4.01 | 11.23 | 16.90 | 2.00 | 120.4 | 90.0 |
| Bench 3 | Bench | Adam Armstrong | FWD | 20 | 5.5 | 3.74 | 10.66 | 17.27 | 2.00 | 131.8 | 62.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.6 | 5.58 | 15.33 | 25.15 | 3.00 | 88.3 | 74.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.30 | 15.00 | 24.41 | 4.00 | 105.3 | 86.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 4.53 | 13.83 | 23.70 | 2.00 | 81.9 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.53 | 12.70 | 20.77 | 2.00 | 86.7 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.9 | 4.28 | 12.20 | 20.01 | 2.00 | 82.3 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 0.40 -> 1.30
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Antoine Semenyo
- Chip used: none
- Predicted score: 50.51
- Actual score: 73.00
- Transfer: Enzo Fernández -> Harry Wilson (projected gain 1.36, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.46 | 10.14 | 16.42 | 3.00 | 95.8 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 2.15 | 6.46 | 10.78 | 8.00 | 96.2 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 4.80 | 14.35 | 22.63 | 9.00 | 111.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.68 | 12.75 | 19.99 | 7.00 | 101.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 3.54 | 10.49 | 16.45 | 6.00 | 85.0 | 90.0 |
| Bench 2 | Bench | Jurriën Timber | DEF | 1 | 6.4 | 3.38 | 10.23 | 16.50 | 8.00 | 82.3 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.0 | 3.67 | 10.16 | 15.45 | 2.00 | 91.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 3.66 | 12.09 | 19.57 | 2.00 | 67.9 | 90.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.6 | 3.20 | 9.59 | 14.56 | 2.00 | 96.8 | 90.0 |
| Bench 4 | Bench | Adam Armstrong | FWD | 20 | 5.4 | 2.65 | 7.88 | 12.92 | 4.00 | 85.0 | 90.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.0 | 4.95 | 14.68 | 23.37 | 8.00 | 94.8 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 4.75 | 14.20 | 23.73 | 13.00 | 88.4 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 3.82 | 12.71 | 20.99 | 1.00 | 68.0 | 85.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.22 | 12.18 | 19.51 | 2.00 | 82.9 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.00 | 11.54 | 17.99 | 12.00 | 89.4 | 71.0 |

## GW29

- Train rows: 182721
- Bank: 1.30 -> 0.20
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Bruno Borges Fernandes
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 58.60
- Actual score: 93.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.62) beats the best remaining Triple Captain opportunity (6.74).
- Transfer: Morgan Rogers -> Bryan Mbeumo (projected gain 2.48, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (5.62) beats the best remaining Triple Captain opportunity (6.74).
- Autosub: Mateus Mané replaced Harry Wilson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.34 | 10.23 | 16.71 | 7.00 | 98.5 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 2.17 | 6.55 | 10.92 | 3.00 | 94.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 4.74 | 14.69 | 23.47 | 11.00 | 115.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.39 | 12.28 | 19.39 | 1.00 | 90.1 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 3.66 | 11.18 | 18.41 | 13.00 | 94.7 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 3.94 | 11.16 | 17.57 | 1.00 | 91.4 | 90.0 |
| Bench 3 | Bench | James Hill | DEF | 4 | 4.0 | 3.01 | 8.81 | 13.77 | 8.00 | 86.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.15 | 12.60 | 20.89 | 19.00 | 81.3 | 84.0 |
| Bench 2 | Autosub In | Mateus Mané | FWD | 20 | 4.6 | 3.05 | 8.83 | 13.54 | 2.00 | 92.5 | 69.0 |
| Bench 4 | Bench | Adam Armstrong | FWD | 20 | 5.4 | 2.94 | 8.48 | 13.44 | 1.00 | 91.3 | 59.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 5.62 | 16.17 | 25.82 | 7.00 | 108.9 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.9 | 5.49 | 15.84 | 26.35 | 8.00 | 98.1 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.01 | 13.55 | 22.81 | 9.00 | 76.5 | 84.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.7 | 4.16 | 12.09 | 19.48 | 1.00 | 76.2 | 76.0 |
| XI | Bench | Harry Wilson | MID | 10 | 5.9 | 3.86 | 10.86 | 17.35 | 0.00 | 78.1 | 0.0 |

## GW30

- Train rows: 183541
- Bank: 0.20 -> 0.60
- Free transfers: 2 -> 2
- Captain: João Pedro Junqueira de Jesus
- Vice captain: Bruno Borges Fernandes
- Effective captain: João Pedro Junqueira de Jesus
- Chip used: bench_boost
- Predicted score: 64.45
- Actual score: 57.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.15) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Harry Wilson -> Elliot Anderson (projected gain 1.90, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.15) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.49 | 10.13 | 16.53 | 7.00 | 95.2 | 90.0 |
| Bench 1 | Bench Boost | José Malheiro de Sá | GK | 20 | 4.2 | 2.17 | 6.44 | 10.65 | 0.00 | 85.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 4.38 | 13.07 | 21.77 | 9.00 | 99.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.19 | 11.82 | 18.84 | 2.00 | 82.7 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 3.91 | 11.45 | 18.79 | 1.00 | 93.2 | 37.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 3.41 | 9.77 | 15.61 | 2.00 | 85.5 | 90.0 |
| Bench 2 | Bench Boost | James Hill | DEF | 4 | 4.1 | 3.37 | 9.10 | 14.67 | 8.00 | 85.6 | 90.0 |
| Captain | Captain | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.88 | 16.14 | 26.22 | 2.00 | 102.1 | 90.0 |
| Bench 3 | Bench Boost | Adam Armstrong | FWD | 20 | 5.3 | 2.50 | 7.32 | 11.91 | 5.00 | 73.7 | 86.0 |
| Bench 4 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 2.11 | 5.99 | 10.21 | 1.00 | 64.8 | 45.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.9 | 5.52 | 17.19 | 28.13 | 10.00 | 101.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 5.38 | 15.96 | 25.40 | 2.00 | 105.3 | 74.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.62 | 14.43 | 23.78 | 2.00 | 79.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.7 | 3.76 | 11.39 | 18.94 | 2.00 | 71.5 | 74.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.5 | 3.88 | 10.88 | 17.32 | 2.00 | 88.5 | 87.0 |