# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 249.36
- Total actual points: 271.00
- Average predicted points: 62.34
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
- Bank: 100.00 -> 0.40
- Free transfers: 1 -> 2
- Captain: Gabriel dos Santos Magalhães
- Vice captain: Cole Palmer
- Effective captain: Gabriel dos Santos Magalhães
- Chip used: none
- Predicted score: 62.00
- Actual score: 43.00
- Chip advisory: bench_boost (0.62): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.35 | 12.21 | 19.29 | 3.00 | 115.5 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 2.99 | 8.85 | 14.37 | 2.00 | 118.8 | 90.0 |
| Captain | Captain | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 6.10 | 17.29 | 26.62 | 2.00 | 134.5 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.70 | 13.28 | 20.61 | 3.00 | 114.0 | 56.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.44 | 12.53 | 19.92 | 11.00 | 99.8 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.33 | 11.88 | 18.07 | 2.00 | 95.7 | 90.0 |
| Bench 4 | Bench | James Hill | DEF | 4 | 4.0 | 3.52 | 9.96 | 15.63 | 6.00 | 95.5 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.58 | 14.69 | 23.22 | 7.00 | 86.2 | 79.0 |
| Bench 2 | Bench | Mateus Mané | FWD | 20 | 4.6 | 4.27 | 11.67 | 17.51 | 2.00 | 120.4 | 90.0 |
| Bench 3 | Bench | Adam Armstrong | FWD | 20 | 5.5 | 3.97 | 11.09 | 17.88 | 2.00 | 131.8 | 62.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.6 | 6.07 | 16.07 | 26.05 | 3.00 | 88.3 | 74.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.70 | 15.56 | 25.04 | 4.00 | 105.3 | 86.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.01 | 14.84 | 25.13 | 2.00 | 81.9 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.90 | 13.33 | 21.62 | 2.00 | 86.7 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.9 | 4.71 | 13.09 | 21.30 | 2.00 | 82.3 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 0.40 -> 0.40
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Antoine Semenyo
- Chip used: none
- Predicted score: 54.86
- Actual score: 69.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.69 | 10.52 | 17.10 | 3.00 | 95.8 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 2.24 | 6.86 | 11.53 | 8.00 | 96.2 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.17 | 14.70 | 23.23 | 9.00 | 111.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.03 | 13.11 | 20.63 | 7.00 | 101.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 3.86 | 11.09 | 17.50 | 6.00 | 85.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 3.72 | 10.95 | 17.75 | 8.00 | 82.3 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.0 | 3.92 | 10.54 | 16.14 | 2.00 | 91.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.38 | 13.94 | 22.63 | 2.00 | 67.9 | 90.0 |
| Bench 2 | Bench | Mateus Mané | FWD | 20 | 4.6 | 3.40 | 9.96 | 15.26 | 2.00 | 96.8 | 90.0 |
| Bench 4 | Bench | Adam Armstrong | FWD | 20 | 5.4 | 2.85 | 8.44 | 13.93 | 4.00 | 85.0 | 90.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.0 | 5.34 | 15.03 | 23.97 | 8.00 | 94.8 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.17 | 14.70 | 24.58 | 13.00 | 88.4 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.57 | 14.63 | 24.19 | 1.00 | 68.0 | 85.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.67 | 12.96 | 20.81 | 2.00 | 82.9 | 90.0 |
| Bench 3 | Bench | Enzo Fernández | MID | 7 | 6.8 | 3.25 | 11.29 | 19.10 | 1.00 | 65.6 | 85.0 |

## GW29

- Train rows: 182721
- Bank: 0.40 -> 1.10
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Bruno Borges Fernandes
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 62.91
- Actual score: 93.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.08) beats the best remaining Triple Captain opportunity (7.29).
- Transfer: Enzo Fernández -> Harry Wilson (projected gain 1.35, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.08) beats the best remaining Triple Captain opportunity (7.29).
- Autosub: Mateus Mané replaced Harry Wilson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.55 | 10.69 | 17.42 | 7.00 | 98.5 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 2.26 | 6.93 | 11.61 | 3.00 | 94.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.10 | 15.25 | 24.20 | 11.00 | 115.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.72 | 12.78 | 20.11 | 1.00 | 90.1 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 3.91 | 11.66 | 19.13 | 13.00 | 94.7 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.22 | 11.65 | 18.28 | 1.00 | 91.4 | 90.0 |
| Bench 3 | Bench | James Hill | DEF | 4 | 4.0 | 3.22 | 9.33 | 14.61 | 8.00 | 86.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.60 | 13.55 | 22.33 | 19.00 | 81.3 | 84.0 |
| Bench 2 | Autosub In | Mateus Mané | FWD | 20 | 4.6 | 3.23 | 9.26 | 14.24 | 2.00 | 92.5 | 69.0 |
| Bench 4 | Bench | Adam Armstrong | FWD | 20 | 5.4 | 3.11 | 8.90 | 14.14 | 1.00 | 91.3 | 59.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.08 | 16.76 | 26.56 | 7.00 | 108.9 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.9 | 5.94 | 16.42 | 27.09 | 8.00 | 98.1 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.55 | 14.92 | 24.92 | 9.00 | 76.5 | 84.0 |
| XI | Bench | Harry Wilson | MID | 10 | 6.0 | 4.37 | 11.99 | 19.10 | 0.00 | 78.1 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 3.72 | 11.27 | 18.87 | 1.00 | 67.2 | 90.0 |

## GW30

- Train rows: 183541
- Bank: 1.10 -> 0.20
- Free transfers: 2 -> 2
- Captain: João Pedro Junqueira de Jesus
- Vice captain: Bruno Borges Fernandes
- Effective captain: João Pedro Junqueira de Jesus
- Chip used: bench_boost
- Predicted score: 69.59
- Actual score: 66.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.87) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Harry Wilson -> Dominik Szoboszlai (projected gain 1.75, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.87) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.72 | 10.61 | 17.31 | 7.00 | 95.2 | 90.0 |
| Bench 1 | Bench Boost | José Malheiro de Sá | GK | 20 | 4.2 | 2.31 | 6.93 | 11.57 | 0.00 | 85.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 4.71 | 13.65 | 22.64 | 9.00 | 99.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.65 | 12.76 | 20.30 | 2.00 | 82.7 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 4.19 | 11.98 | 19.61 | 1.00 | 93.2 | 37.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 3.71 | 10.45 | 16.72 | 2.00 | 85.5 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.1 | 3.66 | 9.74 | 15.75 | 8.00 | 85.6 | 90.0 |
| Captain | Captain | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.37 | 16.84 | 27.17 | 2.00 | 102.1 | 90.0 |
| Bench 3 | Bench Boost | Adam Armstrong | FWD | 20 | 5.3 | 2.81 | 8.26 | 13.54 | 5.00 | 73.7 | 86.0 |
| Bench 4 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 2.49 | 7.19 | 12.39 | 1.00 | 64.8 | 45.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.9 | 5.98 | 17.92 | 29.11 | 10.00 | 101.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 5.81 | 16.65 | 26.34 | 2.00 | 105.3 | 74.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.20 | 15.75 | 25.81 | 2.00 | 79.6 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.9 | 4.36 | 12.19 | 19.05 | 11.00 | 81.6 | 90.0 |
| Bench 2 | Bench Boost | Morgan Rogers | MID | 2 | 7.5 | 3.26 | 10.45 | 17.38 | 2.00 | 73.8 | 90.0 |