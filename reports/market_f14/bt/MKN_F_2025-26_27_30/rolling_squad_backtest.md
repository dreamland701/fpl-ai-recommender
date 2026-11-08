# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 281.81
- Total actual points: 253.00
- Average predicted points: 70.45
- Average actual points: 63.25
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
- Captain: Gabriel dos Santos Magalhães
- Vice captain: Declan Rice
- Effective captain: Gabriel dos Santos Magalhães
- Chip used: none
- Predicted score: 72.23
- Actual score: 47.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 5.43 | 14.42 | 22.54 | 3.00 | 119.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 7.35 | 20.11 | 30.75 | 2.00 | 137.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.46 | 14.79 | 23.35 | 11.00 | 105.9 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.96 | 13.65 | 20.82 | 2.00 | 99.3 | 90.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.0 | 4.01 | 11.45 | 18.04 | 6.00 | 98.1 | 90.0 |
| Bench 4 | Bench | James Justin | DEF | 11 | 3.9 | 2.49 | 8.26 | 13.82 | 2.00 | 73.3 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.8 | 6.66 | 20.41 | 33.89 | 6.00 | 86.9 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.21 | 16.14 | 25.31 | 7.00 | 82.9 | 79.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 4.46 | 12.90 | 19.57 | 2.00 | 115.6 | 90.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.6 | 6.91 | 19.23 | 29.90 | 4.00 | 117.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 6.27 | 17.43 | 28.14 | 4.00 | 104.6 | 86.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.23 | 15.94 | 27.14 | 2.00 | 78.8 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.9 | 5.95 | 14.89 | 23.59 | 2.00 | 90.3 | 90.0 |
| Bench 3 | Bench | Ilia Gruev | MID | 11 | 4.7 | 2.68 | 8.65 | 13.99 | 1.00 | 74.2 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Declan Rice
- Chip used: none
- Predicted score: 65.19
- Actual score: 64.00
- Transfer: none
- No transfer was applied this week.
- Autosub: Ilia Gruev replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.53 | 12.30 | 19.84 | 3.00 | 102.1 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 6.10 | 16.89 | 26.59 | 9.00 | 116.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 6.28 | 15.53 | 24.22 | 7.00 | 111.5 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.35 | 12.36 | 19.44 | 6.00 | 85.7 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.0 | 4.56 | 11.98 | 18.26 | 2.00 | 93.8 | 90.0 |
| Bench 3 | Bench | James Justin | DEF | 11 | 3.9 | 2.61 | 8.50 | 13.62 | 2.00 | 80.0 | 86.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.8 | 7.26 | 21.94 | 36.04 | 0.00 | 100.7 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 3.33 | 13.19 | 22.24 | 2.00 | 57.4 | 90.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 3.55 | 10.90 | 16.83 | 2.00 | 93.9 | 90.0 |
| Vice Captain | Captain | Declan Rice | MID | 1 | 7.6 | 6.34 | 17.90 | 27.95 | 5.00 | 108.0 | 75.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.81 | 16.69 | 26.69 | 8.00 | 91.3 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.82 | 16.30 | 27.12 | 13.00 | 88.4 | 90.0 |
| Bench 4 | Bench | Enzo Fernández | MID | 7 | 6.8 | 2.53 | 10.68 | 18.69 | 1.00 | 59.6 | 85.0 |
| Bench 2 | Autosub In | Ilia Gruev | MID | 11 | 4.7 | 2.65 | 8.62 | 13.60 | 2.00 | 76.4 | 74.0 |

## GW29

- Train rows: 182721
- Bank: 0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 70.57
- Actual score: 83.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.11) beats the best remaining Triple Captain opportunity (8.39).
- Transfer: Enzo Fernández -> Harry Wilson (projected gain 1.85, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (7.11) beats the best remaining Triple Captain opportunity (8.39).
- Autosub: James Hill replaced Harry Wilson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.34 | 12.39 | 19.99 | 7.00 | 101.3 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 6.10 | 17.53 | 27.64 | 11.00 | 118.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.72 | 14.85 | 23.17 | 1.00 | 95.7 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 5.20 | 13.58 | 21.09 | 1.00 | 96.7 | 90.0 |
| Bench 2 | Autosub In | James Hill | DEF | 4 | 4.0 | 3.61 | 10.44 | 16.37 | 8.00 | 89.1 | 90.0 |
| XI | XI | James Justin | DEF | 11 | 3.9 | 3.64 | 8.98 | 13.61 | 2.00 | 86.4 | 73.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.7 | 4.68 | 15.92 | 27.55 | 2.00 | 44.3 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.71 | 14.49 | 24.08 | 19.00 | 78.3 | 84.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.6 | 3.00 | 9.71 | 15.25 | 2.00 | 87.4 | 69.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 7.11 | 18.98 | 29.82 | 7.00 | 110.5 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.9 | 5.43 | 17.18 | 29.13 | 8.00 | 86.3 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.5 | 5.20 | 15.56 | 24.96 | 3.00 | 94.6 | 90.0 |
| XI | Bench | Harry Wilson | MID | 10 | 6.0 | 4.21 | 12.26 | 19.79 | 0.00 | 74.8 | 0.0 |
| Bench 3 | Bench | Ilia Gruev | MID | 11 | 4.7 | 3.43 | 8.58 | 13.35 | 3.00 | 74.6 | 61.0 |

## GW30

- Train rows: 183541
- Bank: 0.70 -> 1.20
- Free transfers: 2 -> 2
- Captain: João Pedro Junqueira de Jesus
- Vice captain: Antoine Semenyo
- Effective captain: João Pedro Junqueira de Jesus
- Chip used: bench_boost
- Predicted score: 73.82
- Actual score: 59.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.52) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Harry Wilson -> Elliot Anderson (projected gain 5.01, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.52) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.70 | 12.53 | 20.17 | 7.00 | 99.0 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.78 | 15.92 | 26.11 | 9.00 | 103.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.46 | 14.45 | 22.83 | 2.00 | 88.4 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.28 | 11.85 | 18.91 | 2.00 | 88.4 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.1 | 4.17 | 11.03 | 17.79 | 8.00 | 88.1 | 90.0 |
| Bench 2 | Bench Boost | James Justin | DEF | 11 | 3.9 | 2.84 | 7.84 | 12.63 | 6.00 | 74.2 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.6 | 5.79 | 18.62 | 31.25 | 2.00 | 77.7 | 90.0 |
| Captain | Captain | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.57 | 18.15 | 29.48 | 2.00 | 93.0 | 90.0 |
| Bench 4 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 2.23 | 6.84 | 11.94 | 1.00 | 63.2 | 45.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.9 | 6.47 | 19.84 | 32.30 | 10.00 | 98.3 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 8.1 | 6.54 | 18.77 | 29.68 | 2.00 | 104.5 | 74.0 |
| XI | XI | Declan Rice | MID | 1 | 7.4 | 5.39 | 14.51 | 23.75 | 3.00 | 87.8 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.5 | 4.58 | 12.79 | 20.45 | 2.00 | 86.1 | 87.0 |
| Bench 3 | Bench Boost | Ilia Gruev | MID | 11 | 4.7 | 2.46 | 7.02 | 11.53 | 1.00 | 59.2 | 45.0 |