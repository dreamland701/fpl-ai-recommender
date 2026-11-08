# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW38
- Total predicted points: 745.86
- Total actual points: 690.00
- Average predicted points: 62.16
- Average actual points: 57.50
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
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.94 | 13.85 | 21.88 | 3.00 | 115.5 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 3.40 | 10.04 | 16.30 | 2.00 | 118.8 | 90.0 |
| Captain | Captain | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 6.92 | 19.62 | 30.20 | 2.00 | 134.5 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 5.33 | 15.06 | 23.38 | 3.00 | 114.0 | 56.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.04 | 14.22 | 22.60 | 11.00 | 99.8 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.92 | 13.48 | 20.50 | 2.00 | 95.7 | 90.0 |
| Bench 4 | Bench | James Hill | DEF | 4 | 4.0 | 3.99 | 11.30 | 17.73 | 6.00 | 95.5 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.27 | 16.50 | 26.07 | 7.00 | 86.2 | 79.0 |
| Bench 2 | Bench | Mateus Mané | FWD | 20 | 4.6 | 4.85 | 13.25 | 19.86 | 2.00 | 120.4 | 90.0 |
| Bench 3 | Bench | Adam Armstrong | FWD | 20 | 5.5 | 4.50 | 12.58 | 20.29 | 2.00 | 131.8 | 62.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.6 | 6.82 | 18.05 | 29.25 | 3.00 | 88.3 | 74.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 6.47 | 17.66 | 28.41 | 4.00 | 105.3 | 86.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.50 | 16.30 | 27.60 | 2.00 | 81.9 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.50 | 14.96 | 24.27 | 2.00 | 86.7 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.9 | 5.18 | 14.38 | 23.40 | 2.00 | 82.3 | 90.0 |

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
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.14 | 11.82 | 19.21 | 3.00 | 95.8 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 2.51 | 7.71 | 12.95 | 8.00 | 96.2 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.81 | 16.52 | 26.10 | 9.00 | 111.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.65 | 14.73 | 23.18 | 7.00 | 101.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.24 | 12.20 | 19.25 | 6.00 | 85.0 | 90.0 |
| Bench 2 | Bench | Jurriën Timber | DEF | 1 | 6.4 | 4.04 | 11.91 | 19.30 | 8.00 | 82.3 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.0 | 4.41 | 11.84 | 18.13 | 2.00 | 91.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.39 | 13.99 | 22.71 | 2.00 | 67.9 | 90.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.6 | 3.82 | 11.19 | 17.14 | 2.00 | 96.8 | 90.0 |
| Bench 4 | Bench | Adam Armstrong | FWD | 20 | 5.4 | 3.13 | 9.29 | 15.33 | 4.00 | 85.0 | 90.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.0 | 6.00 | 16.88 | 26.93 | 8.00 | 94.8 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.75 | 16.35 | 27.33 | 13.00 | 88.4 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.59 | 14.69 | 24.29 | 1.00 | 68.0 | 85.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.08 | 14.10 | 22.65 | 2.00 | 82.9 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.82 | 13.37 | 20.95 | 12.00 | 89.4 | 71.0 |

## GW29

- Train rows: 182721
- Bank: 1.30 -> 0.20
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Bruno Borges Fernandes
- Effective captain: Antoine Semenyo
- Chip used: none
- Predicted score: 63.90
- Actual score: 86.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Morgan Rogers -> Bryan Mbeumo (projected gain 2.85, hit 0)
- Autosub: Mateus Mané replaced Harry Wilson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.99 | 12.00 | 19.55 | 7.00 | 98.5 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 2.54 | 7.77 | 13.03 | 3.00 | 94.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.73 | 17.12 | 27.16 | 11.00 | 115.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.29 | 14.35 | 22.57 | 1.00 | 90.1 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 4.38 | 13.09 | 21.47 | 13.00 | 94.7 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.74 | 13.07 | 20.52 | 1.00 | 91.4 | 90.0 |
| Bench 3 | Bench | James Hill | DEF | 4 | 4.0 | 3.57 | 10.37 | 16.23 | 8.00 | 86.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 5.00 | 14.72 | 24.25 | 19.00 | 81.3 | 84.0 |
| Bench 2 | Autosub In | Mateus Mané | FWD | 20 | 4.6 | 3.63 | 10.39 | 15.98 | 2.00 | 92.5 | 69.0 |
| Bench 4 | Bench | Adam Armstrong | FWD | 20 | 5.4 | 3.49 | 9.99 | 15.87 | 1.00 | 91.3 | 59.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.82 | 18.81 | 29.81 | 7.00 | 108.9 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.9 | 6.66 | 18.43 | 30.40 | 8.00 | 98.1 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.82 | 15.81 | 26.42 | 9.00 | 76.5 | 84.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.7 | 5.00 | 14.14 | 22.67 | 1.00 | 76.2 | 76.0 |
| XI | Bench | Harry Wilson | MID | 10 | 5.9 | 4.64 | 12.72 | 20.27 | 0.00 | 78.1 | 0.0 |

## GW30

- Train rows: 183541
- Bank: 0.20 -> 0.60
- Free transfers: 2 -> 2
- Captain: João Pedro Junqueira de Jesus
- Vice captain: Bruno Borges Fernandes
- Effective captain: João Pedro Junqueira de Jesus
- Chip used: none
- Predicted score: 66.12
- Actual score: 43.00
- Transfer: Harry Wilson -> Elliot Anderson (projected gain 2.24, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.21 | 12.01 | 19.58 | 7.00 | 95.2 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 2.55 | 7.68 | 12.82 | 0.00 | 85.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.32 | 15.45 | 25.61 | 9.00 | 99.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.09 | 13.98 | 22.24 | 2.00 | 82.7 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 4.74 | 13.55 | 22.19 | 1.00 | 93.2 | 37.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.11 | 11.58 | 18.53 | 2.00 | 85.5 | 90.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.1 | 4.05 | 10.80 | 17.45 | 8.00 | 85.6 | 90.0 |
| Captain | Captain | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 7.21 | 19.05 | 30.74 | 2.00 | 102.1 | 90.0 |
| Bench 3 | Bench | Adam Armstrong | FWD | 20 | 5.3 | 2.96 | 8.71 | 14.27 | 5.00 | 73.7 | 86.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.5 | 2.48 | 7.15 | 12.31 | 1.00 | 64.8 | 45.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.9 | 6.76 | 20.28 | 32.93 | 10.00 | 101.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 6.58 | 18.84 | 29.80 | 2.00 | 105.3 | 74.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.63 | 17.05 | 27.94 | 2.00 | 79.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.7 | 4.55 | 13.48 | 22.36 | 2.00 | 71.5 | 74.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.5 | 4.70 | 12.88 | 20.50 | 2.00 | 88.5 | 87.0 |

## GW31

- Train rows: 184363
- Bank: 0.60 -> 0.70
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 64.45
- Actual score: 39.00
- Transfer: Marc Guéhi -> Malick Thiaw (projected gain 3.59, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martín | GK | 1 | 6.0 | 3.23 | 10.84 | 18.38 | 0.00 | 75.0 | 0.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 1.53 | 6.09 | 10.88 | 0.00 | 64.9 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 5.99 | 16.81 | 26.49 | 3.00 | 113.9 | 90.0 |
| XI | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 4.48 | 14.58 | 24.76 | 0.00 | 79.3 | 0.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 5.96 | 14.44 | 21.92 | 0.00 | 111.0 | 36.0 |
| XI | XI | James Hill | DEF | 4 | 4.1 | 3.88 | 11.04 | 17.89 | -1.00 | 85.6 | 90.0 |
| Bench 2 | Bench | Jurriën Timber | DEF | 1 | 6.3 | 3.10 | 10.95 | 18.63 | 0.00 | 56.5 | 0.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.61 | 18.57 | 29.75 | 2.00 | 99.2 | 77.0 |
| Bench 3 | Bench | Adam Armstrong | FWD | 20 | 5.3 | 2.17 | 7.80 | 13.62 | 0.00 | 59.6 | 0.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.5 | 1.11 | 4.57 | 9.29 | 0.00 | 32.7 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.0 | 7.61 | 22.01 | 35.43 | 13.00 | 126.8 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.81 | 17.17 | 28.07 | 2.00 | 89.5 | 90.0 |
| XI | Bench | Antoine Semenyo | MID | 13 | 8.1 | 5.11 | 16.10 | 27.06 | 0.00 | 73.6 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.6 | 4.24 | 13.10 | 21.95 | 2.00 | 74.6 | 70.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.5 | 3.92 | 10.90 | 18.01 | 5.00 | 72.7 | 90.0 |

## GW32

- Train rows: 185188
- Bank: 0.70 -> 1.30
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Cole Palmer
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 54.59
- Actual score: 43.00
- Transfer: Malick Thiaw -> Jan Paul van Hecke (projected gain 4.30, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 2.91 | 8.87 | 15.22 | 1.00 | 60.4 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 1.31 | 4.38 | 7.86 | 1.00 | 47.5 | 90.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 4.71 | 12.11 | 18.35 | 5.00 | 91.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 3.94 | 11.75 | 20.26 | 4.00 | 62.6 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.1 | 3.74 | 11.17 | 17.69 | 3.00 | 95.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.43 | 11.12 | 18.47 | 9.00 | 71.5 | 90.0 |
| Bench 2 | Bench | Jurriën Timber | DEF | 1 | 6.3 | 2.21 | 8.15 | 14.57 | 0.00 | 41.8 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.70 | 15.24 | 25.51 | 2.00 | 77.2 | 81.0 |
| Bench 3 | Bench | Adam Armstrong | FWD | 20 | 5.2 | 1.64 | 5.31 | 9.69 | 2.00 | 42.0 | 70.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.4 | 1.07 | 3.71 | 7.31 | 1.00 | 31.5 | 29.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.0 | 6.91 | 21.16 | 34.20 | 4.00 | 106.9 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.6 | 4.92 | 15.38 | 25.47 | 4.00 | 83.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 4.26 | 13.19 | 22.52 | 2.00 | 56.2 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.6 | 3.98 | 12.07 | 20.14 | 1.00 | 66.7 | 20.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.5 | 4.17 | 11.97 | 19.40 | 4.00 | 81.0 | 90.0 |

## GW33

- Train rows: 186014
- Bank: 1.30 -> 2.30
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Cole Palmer
- Chip used: bench_boost
- Predicted score: 74.70
- Actual score: 55.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (15.14) beats the best remaining Bench Boost opportunity (12.52).
- Chip advisory: triple_captain (0.60): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Jurriën Timber -> Marcos Senesi Barón (projected gain 6.07, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (15.14) beats the best remaining Bench Boost opportunity (12.52).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 2.83 | 9.44 | 16.01 | 1.00 | 74.9 | 90.0 |
| Bench 1 | Bench Boost | José Malheiro de Sá | GK | 20 | 4.2 | 2.15 | 6.64 | 11.04 | 0.00 | 72.5 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.2 | 6.41 | 14.92 | 22.47 | 6.00 | 126.8 | 180.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 5.64 | 13.06 | 19.35 | 12.00 | 109.7 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.07 | 12.61 | 20.89 | 8.00 | 84.1 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.1 | 5.07 | 11.99 | 18.52 | 5.00 | 111.9 | 180.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 3.42 | 11.30 | 19.69 | 0.00 | 65.7 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.73 | 17.73 | 28.18 | 0.00 | 118.3 | 0.0 |
| Bench 3 | Bench Boost | Adam Armstrong | FWD | 20 | 5.2 | 2.17 | 6.61 | 11.43 | 2.00 | 57.6 | 90.0 |
| Bench 4 | Bench Boost | Mateus Mané | FWD | 20 | 4.3 | 1.37 | 4.69 | 8.58 | 1.00 | 39.7 | 52.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.5 | 7.63 | 19.18 | 30.05 | 2.00 | 129.2 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.0 | 6.26 | 18.85 | 31.54 | 6.00 | 88.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 6.33 | 16.66 | 26.77 | 5.00 | 109.6 | 154.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.5 | 4.21 | 11.16 | 17.85 | 2.00 | 74.6 | 90.0 |
| Bench 2 | Bench Boost | Bryan Mbeumo | MID | 14 | 8.5 | 2.75 | 9.28 | 16.33 | 3.00 | 41.2 | 86.0 |

## GW34

- Train rows: 186843
- Bank: 2.30 -> 1.30
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Ollie Watkins
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 66.81
- Actual score: 50.00
- Transfer: João Pedro Junqueira de Jesus -> Ollie Watkins (projected gain 8.85, hit 0)
- Autosub: Bryan Mbeumo replaced Marcos Senesi Barón.
- Autosub: Adam Armstrong replaced Jan Paul van Hecke.
- Autosub: Mateus Mané replaced Antoine Semenyo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.80 | 12.79 | 20.31 | 10.00 | 101.3 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 1.04 | 3.51 | 6.37 | 2.00 | 35.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 6.77 | 17.92 | 28.08 | 4.00 | 126.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 6.05 | 15.84 | 25.50 | 8.00 | 105.5 | 90.0 |
| XI | Bench | Marcos Senesi Barón | DEF | 4 | 5.2 | 4.45 | 13.76 | 22.43 | 0.00 | 101.1 | 0.0 |
| XI | Bench | Jan Paul van Hecke | DEF | 6 | 4.5 | 4.37 | 13.54 | 22.00 | 0.00 | 98.4 | 0.0 |
| XI | Bench | James Hill | DEF | 4 | 4.1 | 3.94 | 12.18 | 20.26 | 0.00 | 96.0 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.7 | 7.33 | 18.44 | 28.19 | 2.00 | 122.9 | 79.0 |
| Bench 3 | Autosub In | Adam Armstrong | FWD | 20 | 5.2 | 2.43 | 6.93 | 11.80 | 2.00 | 61.4 | 90.0 |
| Bench 4 | Autosub In | Mateus Mané | FWD | 20 | 4.3 | 2.19 | 6.37 | 10.47 | 2.00 | 54.8 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.0 | 7.73 | 21.33 | 35.30 | 5.00 | 123.9 | 90.0 |
| XI | Bench | Antoine Semenyo | MID | 13 | 8.1 | 5.37 | 16.60 | 27.41 | 0.00 | 90.6 | 0.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 4.14 | 13.57 | 23.32 | 0.00 | 61.8 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.5 | 4.13 | 11.81 | 18.80 | 9.00 | 83.3 | 90.0 |
| Bench 2 | Autosub In | Bryan Mbeumo | MID | 14 | 8.5 | 3.92 | 11.47 | 19.03 | 3.00 | 70.2 | 73.0 |

## GW35

- Train rows: 187673
- Bank: 1.30 -> 0.70
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 46.98
- Actual score: 33.00
- Transfer: Marcos Senesi Barón -> Daniel Muñoz Mejía (projected gain 3.75, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.31 | 10.08 | 16.74 | 6.00 | 80.0 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 2.16 | 5.72 | 9.18 | 0.00 | 63.9 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 4.94 | 14.42 | 22.64 | 6.00 | 92.8 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 3.94 | 11.29 | 16.94 | 0.00 | 81.5 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 3.30 | 10.93 | 18.65 | 1.00 | 72.8 | 90.0 |
| Bench 2 | Bench | Jan Paul van Hecke | DEF | 6 | 4.5 | 2.43 | 7.72 | 13.37 | 2.00 | 47.2 | 90.0 |
| Bench 4 | Bench | James Hill | DEF | 4 | 4.1 | 2.07 | 6.34 | 11.35 | 10.00 | 47.6 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.7 | 2.55 | 8.70 | 14.81 | 1.00 | 35.6 | 30.0 |
| XI | XI | Adam Armstrong | FWD | 20 | 5.2 | 2.81 | 7.46 | 12.00 | 2.00 | 65.3 | 90.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.3 | 2.62 | 7.26 | 11.23 | 2.00 | 62.2 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.1 | 6.31 | 19.14 | 32.23 | 5.00 | 102.0 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.5 | 4.39 | 12.44 | 19.76 | 1.00 | 81.0 | 45.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.4 | 3.58 | 10.53 | 17.84 | 2.00 | 64.4 | 74.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 2.93 | 9.93 | 17.17 | 2.00 | 42.5 | 74.0 |
| Bench 3 | Bench | Cole Palmer | MID | 7 | 10.5 | 2.20 | 8.20 | 15.30 | 0.00 | 29.5 | 90.0 |

## GW36

- Train rows: 188505
- Bank: 0.70 -> 0.40
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Antoine Semenyo
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 64.54
- Actual score: 70.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (9.83) beats the best remaining Triple Captain opportunity (8.69).
- Transfer: Elliot Anderson -> Carlos Henrique Casimiro (projected gain 3.93, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (9.83) beats the best remaining Triple Captain opportunity (8.69).
- Autosub: James Hill replaced Carlos Henrique Casimiro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.79 | 10.94 | 17.84 | 9.00 | 84.8 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 0.56 | 2.21 | 4.22 | 0.00 | 26.7 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.20 | 14.89 | 23.50 | 11.00 | 94.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.47 | 12.51 | 20.21 | 2.00 | 82.7 | 90.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 4.17 | 10.83 | 17.28 | 6.00 | 81.8 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 4.24 | 10.17 | 15.16 | 3.00 | 87.2 | 171.0 |
| Bench 2 | Autosub In | James Hill | DEF | 4 | 4.1 | 3.22 | 9.34 | 15.21 | 6.00 | 76.7 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.7 | 3.79 | 10.95 | 18.40 | 9.00 | 47.9 | 90.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.67 | 7.93 | 11.81 | 2.00 | 70.4 | 66.0 |
| Bench 4 | Bench | Adam Armstrong | FWD | 20 | 5.2 | 2.59 | 7.63 | 12.12 | 2.00 | 68.5 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.1 | 7.08 | 20.83 | 34.00 | 3.00 | 104.3 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.77 | 14.41 | 22.63 | 12.00 | 96.9 | 180.0 |
| XI | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.67 | 13.56 | 20.94 | 0.00 | 89.0 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 3.78 | 11.20 | 18.27 | 1.00 | 65.5 | 15.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.3 | 3.42 | 11.00 | 18.79 | 2.00 | 58.4 | 90.0 |

## GW37

- Train rows: 189343
- Bank: 0.40 -> 0.00
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 55.60
- Actual score: 77.00
- Transfer: Carlos Henrique Casimiro -> Bernardo Mota Veiga de Carvalho e Silva (projected gain 3.17, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.74 | 12.41 | 19.76 | 6.00 | 86.2 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 0.63 | 1.86 | 3.35 | 3.00 | 22.5 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 6.17 | 15.96 | 25.28 | 6.00 | 93.8 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 4.14 | 11.80 | 18.11 | 6.00 | 92.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 3.85 | 11.39 | 18.91 | 14.00 | 83.7 | 90.0 |
| Bench 2 | Bench | Jan Paul van Hecke | DEF | 6 | 4.6 | 2.85 | 8.61 | 14.92 | 2.00 | 68.1 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.1 | 2.86 | 8.61 | 14.23 | 1.00 | 66.4 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.7 | 3.29 | 10.90 | 18.83 | 15.00 | 60.9 | 90.0 |
| Bench 3 | Bench | Adam Armstrong | FWD | 20 | 5.2 | 2.78 | 7.70 | 11.98 | 2.00 | 66.2 | 71.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.52 | 6.93 | 10.72 | 11.00 | 57.9 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.1 | 6.89 | 20.21 | 32.88 | 9.00 | 108.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.48 | 16.11 | 26.02 | 1.00 | 104.5 | 55.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.3 | 4.08 | 11.98 | 20.08 | 2.00 | 66.1 | 88.0 |
| XI | XI | Bernardo Mota Veiga de Carvalho e Silva | MID | 13 | 6.2 | 3.92 | 11.75 | 19.39 | 1.00 | 87.7 | 55.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 3.29 | 9.57 | 16.03 | 7.00 | 47.2 | 79.0 |

## GW38

- Train rows: 190183
- Bank: 0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 57.49
- Actual score: 78.00
- Transfer: Daniel Muñoz Mejía -> Marc Guéhi (projected gain 2.41, hit 0)
- Autosub: José Malheiro de Sá replaced David Raya Martín.
- Autosub: James Hill replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martín | GK | 1 | 6.1 | 4.30 | 12.10 | 19.20 | 0.00 | 84.0 | 0.0 |
| Bench 1 | Autosub In | José Malheiro de Sá | GK | 20 | 4.2 | 1.54 | 4.23 | 6.81 | 6.00 | 47.5 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.19 | 14.74 | 23.71 | 1.00 | 86.4 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.10 | 14.30 | 22.82 | 2.00 | 99.9 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 13 | 5.1 | 4.65 | 13.01 | 20.76 | 0.00 | 97.5 | 0.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.6 | 3.64 | 10.46 | 16.76 | 1.00 | 79.5 | 90.0 |
| Bench 2 | Autosub In | James Hill | DEF | 4 | 4.1 | 3.46 | 9.80 | 15.27 | 3.00 | 80.1 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.7 | 3.37 | 12.09 | 20.95 | 13.00 | 67.7 | 90.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.2 | 3.12 | 8.29 | 13.14 | 2.00 | 67.2 | 90.0 |
| Bench 4 | Bench | Adam Armstrong | FWD | 20 | 5.1 | 2.77 | 7.29 | 11.48 | 7.00 | 60.2 | 73.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.1 | 6.82 | 20.26 | 33.40 | 14.00 | 106.7 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.06 | 14.24 | 23.00 | 6.00 | 81.5 | 57.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.3 | 4.67 | 12.89 | 20.96 | 8.00 | 83.7 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 4.07 | 11.78 | 19.21 | 9.00 | 65.8 | 73.0 |
| XI | XI | Bernardo Mota Veiga de Carvalho e Silva | MID | 13 | 6.2 | 3.79 | 10.84 | 17.12 | 1.00 | 68.8 | 58.0 |