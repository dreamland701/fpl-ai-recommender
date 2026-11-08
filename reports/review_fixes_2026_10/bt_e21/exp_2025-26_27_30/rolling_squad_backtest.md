# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 269.62
- Total actual points: 278.00
- Average predicted points: 67.40
- Average actual points: 69.50
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
- Captain: Cole Palmer
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 67.27
- Actual score: 44.00
- Chip advisory: bench_boost (0.67): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.67 | 11.62 | 16.60 | 3.00 | 114.5 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 3.36 | 9.55 | 14.69 | 2.00 | 108.8 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 6.40 | 17.27 | 24.87 | 2.00 | 123.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.01 | 13.07 | 20.13 | 11.00 | 96.8 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 5.15 | 12.76 | 18.79 | 3.00 | 113.0 | 56.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.68 | 11.74 | 17.05 | 2.00 | 75.7 | 90.0 |
| Bench 4 | Bench | James Hill | DEF | 4 | 4.0 | 3.88 | 10.78 | 16.31 | 6.00 | 93.5 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.06 | 14.27 | 21.62 | 7.00 | 87.2 | 79.0 |
| Bench 2 | Bench | Mateus Mané | FWD | 20 | 4.6 | 4.65 | 11.90 | 16.76 | 2.00 | 110.4 | 90.0 |
| Bench 3 | Bench | Adam Armstrong | FWD | 20 | 5.5 | 4.36 | 10.88 | 16.65 | 2.00 | 124.8 | 62.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.6 | 6.72 | 15.95 | 24.86 | 3.00 | 89.3 | 74.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 6.13 | 15.40 | 22.98 | 4.00 | 95.3 | 86.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.31 | 14.31 | 22.88 | 2.00 | 61.9 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.31 | 13.32 | 19.79 | 2.00 | 66.7 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.9 | 5.13 | 12.81 | 20.10 | 2.00 | 62.3 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 0.40 -> 1.30
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 59.01
- Actual score: 78.00
- Transfer: Enzo Fernández -> Harry Wilson (projected gain 0.81, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.03 | 11.27 | 17.72 | 3.00 | 93.8 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 2.51 | 7.71 | 12.95 | 8.00 | 96.2 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.52 | 14.62 | 21.88 | 9.00 | 103.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.47 | 13.34 | 20.38 | 7.00 | 97.0 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.0 | 4.37 | 11.54 | 17.11 | 2.00 | 90.6 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.25 | 11.34 | 17.33 | 6.00 | 87.0 | 90.0 |
| Bench 2 | Bench | Jurriën Timber | DEF | 1 | 6.4 | 4.15 | 11.20 | 17.26 | 8.00 | 85.3 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.25 | 12.75 | 19.69 | 2.00 | 50.9 | 90.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.6 | 3.83 | 10.78 | 15.11 | 2.00 | 94.8 | 90.0 |
| Bench 4 | Bench | Adam Armstrong | FWD | 20 | 5.4 | 3.17 | 8.96 | 13.44 | 4.00 | 87.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.61 | 14.59 | 22.75 | 13.00 | 68.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.49 | 14.56 | 21.67 | 8.00 | 74.8 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.58 | 13.30 | 21.44 | 1.00 | 48.0 | 85.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.98 | 12.70 | 19.79 | 2.00 | 62.9 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.85 | 11.93 | 17.36 | 12.00 | 89.4 | 71.0 |

## GW29

- Train rows: 182721
- Bank: 1.30 -> 0.20
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Bruno Borges Fernandes
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 68.16
- Actual score: 99.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.44) beats the best remaining Triple Captain opportunity (7.85).
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Morgan Rogers -> Bryan Mbeumo (projected gain 1.73, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.44) beats the best remaining Triple Captain opportunity (7.85).
- Autosub: James Hill replaced Harry Wilson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.78 | 10.17 | 15.23 | 7.00 | 95.5 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 2.54 | 7.77 | 13.03 | 3.00 | 94.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.37 | 14.88 | 21.82 | 11.00 | 114.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.06 | 12.99 | 19.42 | 1.00 | 90.1 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 4.42 | 11.96 | 19.19 | 13.00 | 92.7 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.60 | 11.32 | 17.18 | 1.00 | 90.4 | 90.0 |
| Bench 2 | Autosub In | James Hill | DEF | 4 | 4.0 | 3.63 | 9.99 | 14.42 | 8.00 | 87.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.85 | 13.10 | 21.01 | 19.00 | 61.3 | 84.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.6 | 3.58 | 9.52 | 13.63 | 2.00 | 91.5 | 69.0 |
| Bench 4 | Bench | Adam Armstrong | FWD | 20 | 5.4 | 3.52 | 9.35 | 14.01 | 1.00 | 90.3 | 59.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.9 | 6.39 | 16.30 | 24.99 | 8.00 | 95.1 | 90.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.44 | 16.18 | 24.66 | 7.00 | 98.9 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.78 | 13.80 | 22.19 | 9.00 | 56.5 | 84.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.7 | 4.83 | 12.62 | 19.65 | 1.00 | 56.2 | 76.0 |
| XI | Bench | Harry Wilson | MID | 10 | 5.9 | 4.75 | 11.35 | 17.96 | 0.00 | 58.1 | 0.0 |

## GW30

- Train rows: 183541
- Bank: 0.20 -> 0.60
- Free transfers: 2 -> 2
- Captain: João Pedro Junqueira de Jesus
- Vice captain: Bruno Borges Fernandes
- Effective captain: João Pedro Junqueira de Jesus
- Chip used: bench_boost
- Predicted score: 75.17
- Actual score: 57.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (12.08) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Harry Wilson -> Elliot Anderson (projected gain 0.67, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (12.08) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.99 | 10.85 | 18.12 | 7.00 | 93.2 | 90.0 |
| Bench 1 | Bench Boost | José Malheiro de Sá | GK | 20 | 4.2 | 2.55 | 7.68 | 12.82 | 0.00 | 85.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 4.90 | 13.04 | 20.91 | 9.00 | 96.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.92 | 12.47 | 19.47 | 2.00 | 62.7 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 4.54 | 11.49 | 18.63 | 1.00 | 92.2 | 37.0 |
| Bench 2 | Bench Boost | Marc Guéhi | DEF | 13 | 5.2 | 4.10 | 10.86 | 16.47 | 2.00 | 87.5 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.1 | 4.21 | 10.35 | 15.87 | 8.00 | 87.6 | 90.0 |
| Captain | Captain | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.64 | 16.54 | 25.98 | 2.00 | 92.1 | 90.0 |
| Bench 3 | Bench Boost | Adam Armstrong | FWD | 20 | 5.3 | 2.95 | 8.40 | 13.17 | 5.00 | 79.7 | 86.0 |
| Bench 4 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 2.48 | 7.15 | 12.31 | 1.00 | 64.8 | 45.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.9 | 6.54 | 17.85 | 27.63 | 10.00 | 93.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 6.16 | 16.03 | 24.60 | 2.00 | 95.3 | 74.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.46 | 14.90 | 24.15 | 2.00 | 83.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.7 | 4.56 | 12.29 | 19.22 | 2.00 | 77.5 | 74.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.5 | 4.52 | 11.37 | 18.11 | 2.00 | 68.5 | 87.0 |