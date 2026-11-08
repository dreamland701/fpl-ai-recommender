# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 278.30
- Total actual points: 272.00
- Average predicted points: 69.58
- Average actual points: 68.00
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
- Predicted score: 69.94
- Actual score: 43.00
- Chip advisory: bench_boost (0.67): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 5.01 | 13.85 | 21.88 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 3.52 | 10.04 | 16.30 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 7.03 | 19.62 | 30.20 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 5.43 | 15.06 | 23.38 | 3.00 | 90.0 | 56.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.00 | 14.22 | 22.60 | 11.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.93 | 13.48 | 20.50 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | James Hill | DEF | 4 | 4.0 | 3.92 | 11.30 | 17.73 | 6.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.24 | 16.50 | 26.07 | 7.00 | 86.2 | 79.0 |
| Bench 2 | Bench | Mateus Mané | FWD | 20 | 4.6 | 4.88 | 13.25 | 19.86 | 2.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Adam Armstrong | FWD | 20 | 5.5 | 4.50 | 12.58 | 20.29 | 2.00 | 90.0 | 62.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.6 | 6.71 | 18.05 | 29.25 | 3.00 | 87.5 | 74.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 6.43 | 17.66 | 28.41 | 4.00 | 90.0 | 86.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.48 | 16.30 | 27.60 | 2.00 | 81.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.49 | 14.96 | 24.27 | 2.00 | 85.4 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.9 | 5.18 | 14.38 | 23.40 | 2.00 | 83.0 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 0.40 -> 1.30
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Antoine Semenyo
- Chip used: none
- Predicted score: 60.65
- Actual score: 73.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Enzo Fernández -> Harry Wilson (projected gain 1.52, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.15 | 11.82 | 19.21 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 2.53 | 7.71 | 12.95 | 8.00 | 90.0 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.81 | 16.52 | 26.10 | 9.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.44 | 14.73 | 23.18 | 7.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.28 | 12.20 | 19.25 | 6.00 | 85.4 | 90.0 |
| Bench 2 | Bench | Jurriën Timber | DEF | 1 | 6.4 | 4.06 | 11.91 | 19.30 | 8.00 | 82.1 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.0 | 4.41 | 11.84 | 18.13 | 2.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.49 | 13.99 | 22.71 | 2.00 | 69.9 | 90.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.6 | 3.79 | 11.19 | 17.14 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Adam Armstrong | FWD | 20 | 5.4 | 3.08 | 9.29 | 15.33 | 4.00 | 84.0 | 90.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.0 | 5.95 | 16.88 | 26.93 | 8.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.69 | 16.35 | 27.33 | 13.00 | 86.3 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.59 | 14.69 | 24.29 | 1.00 | 68.3 | 85.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.13 | 14.10 | 22.65 | 2.00 | 82.9 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.77 | 13.37 | 20.95 | 12.00 | 88.5 | 71.0 |

## GW29

- Train rows: 182721
- Bank: 1.30 -> 0.20
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Bruno Borges Fernandes
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 69.86
- Actual score: 99.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.71) beats the best remaining Triple Captain opportunity (8.11).
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Morgan Rogers -> Bryan Mbeumo (projected gain 2.85, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.71) beats the best remaining Triple Captain opportunity (8.11).
- Autosub: James Hill replaced Harry Wilson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.97 | 12.00 | 19.55 | 7.00 | 90.0 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 2.54 | 7.77 | 13.03 | 3.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.69 | 17.12 | 27.16 | 11.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.14 | 14.35 | 22.57 | 1.00 | 88.1 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 4.30 | 13.09 | 21.47 | 13.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.69 | 13.07 | 20.52 | 1.00 | 90.0 | 90.0 |
| Bench 2 | Autosub In | James Hill | DEF | 4 | 4.0 | 3.61 | 10.37 | 16.23 | 8.00 | 88.1 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.95 | 14.72 | 24.25 | 19.00 | 80.5 | 84.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.6 | 3.58 | 10.39 | 15.98 | 2.00 | 90.0 | 69.0 |
| Bench 4 | Bench | Adam Armstrong | FWD | 20 | 5.4 | 3.44 | 9.99 | 15.87 | 1.00 | 90.0 | 59.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.71 | 18.81 | 29.81 | 7.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.9 | 6.61 | 18.43 | 30.40 | 8.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.79 | 15.81 | 26.42 | 9.00 | 76.5 | 84.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.7 | 5.01 | 14.14 | 22.67 | 1.00 | 76.0 | 76.0 |
| XI | Bench | Harry Wilson | MID | 10 | 5.9 | 4.60 | 12.72 | 20.27 | 0.00 | 77.8 | 0.0 |

## GW30

- Train rows: 183541
- Bank: 0.20 -> 0.60
- Free transfers: 2 -> 2
- Captain: João Pedro Junqueira de Jesus
- Vice captain: Bruno Borges Fernandes
- Effective captain: João Pedro Junqueira de Jesus
- Chip used: bench_boost
- Predicted score: 77.85
- Actual score: 57.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.97) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Harry Wilson -> Elliot Anderson (projected gain 2.23, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.97) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.21 | 12.01 | 19.58 | 7.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | José Malheiro de Sá | GK | 20 | 4.2 | 2.58 | 7.68 | 12.82 | 0.00 | 86.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.33 | 15.45 | 25.61 | 9.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.14 | 13.98 | 22.24 | 2.00 | 83.9 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 4.72 | 13.55 | 22.19 | 1.00 | 90.0 | 37.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.11 | 11.58 | 18.53 | 2.00 | 84.7 | 90.0 |
| Bench 2 | Bench Boost | James Hill | DEF | 4 | 4.1 | 4.04 | 10.80 | 17.45 | 8.00 | 86.3 | 90.0 |
| Captain | Captain | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 7.05 | 19.05 | 30.74 | 2.00 | 90.0 | 90.0 |
| Bench 3 | Bench Boost | Adam Armstrong | FWD | 20 | 5.3 | 2.93 | 8.71 | 14.27 | 5.00 | 73.1 | 86.0 |
| Bench 4 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 2.43 | 7.15 | 12.31 | 1.00 | 63.9 | 45.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.9 | 6.79 | 20.28 | 32.93 | 10.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 6.59 | 18.84 | 29.80 | 2.00 | 90.0 | 74.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.64 | 17.05 | 27.94 | 2.00 | 81.2 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.7 | 4.60 | 13.48 | 22.36 | 2.00 | 71.8 | 74.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.5 | 4.64 | 12.88 | 20.50 | 2.00 | 87.5 | 87.0 |