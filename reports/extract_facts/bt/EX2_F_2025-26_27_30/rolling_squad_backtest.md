# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 277.28
- Total actual points: 259.00
- Average predicted points: 69.32
- Average actual points: 64.75
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
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Erling Haaland
- Vice captain: Cole Palmer
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 73.75
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.82 | 13.39 | 21.14 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 6.94 | 19.46 | 29.88 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.94 | 14.04 | 22.25 | 11.00 | 90.0 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.0 | 3.92 | 11.28 | 17.63 | 6.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Hugo Bueno López | DEF | 20 | 4.3 | 3.91 | 11.14 | 18.11 | 4.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Reinildo Mandava | DEF | 17 | 3.8 | 2.65 | 7.09 | 10.79 | 0.00 | 71.5 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.23 | 23.99 | 37.93 | 6.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.43 | 16.82 | 26.56 | 7.00 | 90.0 | 79.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 4.77 | 13.06 | 19.54 | 2.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.6 | 6.63 | 18.92 | 29.57 | 4.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.6 | 6.96 | 18.56 | 30.05 | 3.00 | 90.0 | 74.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 6.62 | 18.00 | 28.95 | 4.00 | 90.0 | 86.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.9 | 5.26 | 14.56 | 23.54 | 2.00 | 84.5 | 90.0 |
| Bench 3 | Bench | Enzo Le Fée | MID | 17 | 4.9 | 3.69 | 10.49 | 16.40 | 10.00 | 88.3 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 0.00 -> 0.90
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Declan Rice
- Chip used: none
- Predicted score: 66.41
- Actual score: 62.00
- Transfer: Enzo Fernández -> Harry Wilson (projected gain 2.54, hit 0)
- Autosub: Hugo Bueno López replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.07 | 11.61 | 18.79 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.86 | 16.61 | 26.16 | 9.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.62 | 15.14 | 23.83 | 7.00 | 90.0 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.0 | 4.44 | 11.91 | 18.18 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Autosub In | Hugo Bueno López | DEF | 20 | 4.3 | 3.57 | 10.67 | 17.05 | 6.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Reinildo Mandava | DEF | 17 | 3.8 | 1.12 | 3.81 | 6.19 | 0.00 | 41.9 | 0.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.8 | 8.33 | 23.26 | 38.51 | 0.00 | 90.0 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.51 | 14.00 | 22.59 | 2.00 | 70.3 | 90.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 3.80 | 11.22 | 17.30 | 2.00 | 90.0 | 90.0 |
| Vice Captain | Captain | Declan Rice | MID | 1 | 7.6 | 6.18 | 17.96 | 28.13 | 5.00 | 90.0 | 75.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.87 | 16.67 | 26.51 | 8.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.71 | 14.97 | 24.61 | 1.00 | 70.5 | 85.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.70 | 13.21 | 20.63 | 12.00 | 87.2 | 71.0 |
| Bench 3 | Bench | Enzo Le Fée | MID | 17 | 4.9 | 3.16 | 9.57 | 16.03 | 2.00 | 83.7 | 90.0 |

## GW29

- Train rows: 182721
- Bank: 0.90 -> 0.40
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 66.29
- Actual score: 95.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.80) beats the best remaining Triple Captain opportunity (8.03).
- Transfer: Enzo Le Fée -> Elliot Anderson (projected gain 1.30, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.80) beats the best remaining Triple Captain opportunity (8.03).
- Autosub: Mateus Mané replaced Harry Wilson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.77 | 11.57 | 18.91 | 7.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.07 | 0.12 | 0.24 | 0.00 | 2.4 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.59 | 16.89 | 26.90 | 11.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.37 | 14.76 | 23.40 | 1.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Hugo Bueno López | DEF | 20 | 4.3 | 3.56 | 10.52 | 16.74 | 1.00 | 90.0 | 11.0 |
| XI | XI | James Hill | DEF | 4 | 4.0 | 3.57 | 10.29 | 16.20 | 8.00 | 86.9 | 90.0 |
| Bench 4 | Bench | Reinildo Mandava | DEF | 17 | 3.8 | 0.81 | 2.56 | 5.03 | 0.00 | 29.0 | 0.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.7 | 4.74 | 15.41 | 27.26 | 2.00 | 43.5 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.83 | 14.46 | 23.82 | 19.00 | 77.5 | 84.0 |
| Bench 2 | Autosub In | Mateus Mané | FWD | 20 | 4.6 | 3.60 | 10.44 | 16.18 | 2.00 | 90.0 | 69.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.80 | 18.92 | 30.19 | 7.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.85 | 16.00 | 26.74 | 9.00 | 76.9 | 84.0 |
| XI | XI | Declan Rice | MID | 1 | 7.5 | 4.84 | 15.22 | 24.73 | 3.00 | 90.0 | 90.0 |
| XI | Bench | Harry Wilson | MID | 10 | 5.9 | 4.50 | 12.52 | 20.00 | 0.00 | 75.4 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.82 | 11.73 | 18.76 | 12.00 | 79.2 | 90.0 |

## GW30

- Train rows: 183541
- Bank: 0.40 -> 0.00
- Free transfers: 2 -> 2
- Captain: João Pedro Junqueira de Jesus
- Vice captain: Antoine Semenyo
- Effective captain: João Pedro Junqueira de Jesus
- Chip used: bench_boost
- Predicted score: 70.83
- Actual score: 46.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.01) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Harry Wilson -> Ismaïla Sarr (projected gain 4.80, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.01) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.11 | 11.74 | 19.08 | 7.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.37 | 15.50 | 25.60 | 9.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.18 | 14.07 | 22.28 | 2.00 | 84.9 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.1 | 4.10 | 10.92 | 17.57 | 8.00 | 87.8 | 90.0 |
| Bench 2 | Bench Boost | Hugo Bueno López | DEF | 20 | 4.3 | 2.52 | 7.62 | 12.87 | 1.00 | 61.8 | 90.0 |
| Bench 4 | Bench Boost | Reinildo Mandava | DEF | 17 | 3.8 | 0.00 | 0.00 | 1.43 | 0.00 | 4.7 | 0.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.6 | 6.50 | 19.73 | 32.70 | 2.00 | 86.6 | 90.0 |
| Captain | Captain | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.92 | 18.72 | 30.11 | 2.00 | 90.0 | 90.0 |
| Bench 3 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 2.50 | 7.25 | 12.36 | 1.00 | 65.8 | 45.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 8.1 | 6.73 | 19.51 | 31.40 | 2.00 | 90.0 | 74.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.86 | 17.58 | 28.63 | 2.00 | 85.7 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.4 | 5.05 | 14.40 | 23.72 | 3.00 | 86.6 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.72 | 13.04 | 20.68 | 2.00 | 89.4 | 87.0 |
| XI | XI | Ismaïla Sarr | MID | 8 | 6.3 | 4.35 | 12.40 | 20.28 | 3.00 | 90.0 | 90.0 |