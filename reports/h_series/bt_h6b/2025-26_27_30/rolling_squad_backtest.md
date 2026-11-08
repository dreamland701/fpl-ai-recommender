# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 269.08
- Total actual points: 278.00
- Average predicted points: 67.27
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
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Gabriel dos Santos Magalhães
- Vice captain: Cole Palmer
- Effective captain: Gabriel dos Santos Magalhães
- Chip used: none
- Predicted score: 68.16
- Actual score: 44.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.93 | 13.73 | 21.57 | 3.00 | 91.2 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.00 | 0.11 | 0.00 | 2.4 | 0.0 |
| Captain | Captain | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 6.66 | 18.83 | 28.61 | 2.00 | 87.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.73 | 13.92 | 21.88 | 11.00 | 91.9 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.69 | 13.01 | 19.53 | 2.00 | 90.3 | 90.0 |
| Bench 4 | Bench | James Hill | DEF | 4 | 4.0 | 3.78 | 10.75 | 16.72 | 6.00 | 89.9 | 90.0 |
| Bench 3 | Bench | Hugo Bueno López | DEF | 20 | 4.3 | 3.87 | 10.55 | 16.92 | 4.00 | 89.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.04 | 16.01 | 25.16 | 7.00 | 83.0 | 79.0 |
| Bench 2 | Bench | Jarrod Bowen | FWD | 19 | 7.6 | 4.30 | 13.48 | 22.40 | 4.00 | 85.4 | 90.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 4.51 | 12.45 | 17.80 | 2.00 | 86.4 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.6 | 6.45 | 18.71 | 29.04 | 4.00 | 89.7 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.6 | 6.62 | 18.63 | 30.50 | 3.00 | 87.4 | 74.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 6.07 | 17.05 | 27.63 | 4.00 | 89.8 | 86.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.55 | 16.40 | 27.54 | 2.00 | 83.9 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.26 | 15.15 | 24.20 | 2.00 | 85.1 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Declan Rice
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Declan Rice
- Chip used: none
- Predicted score: 60.97
- Actual score: 64.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.10 | 11.59 | 19.01 | 3.00 | 91.2 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.25 | 0.24 | 0.34 | 0.00 | 3.2 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.64 | 16.14 | 25.33 | 9.00 | 89.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.17 | 14.48 | 22.38 | 7.00 | 91.2 | 90.0 |
| Bench 2 | Bench | Marc Guéhi | DEF | 13 | 5.2 | 4.24 | 12.16 | 18.95 | 6.00 | 86.2 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.0 | 4.34 | 11.28 | 17.28 | 2.00 | 90.3 | 90.0 |
| Bench 4 | Bench | Hugo Bueno López | DEF | 20 | 4.3 | 3.52 | 9.48 | 14.81 | 6.00 | 87.9 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.6 | 4.34 | 14.03 | 22.59 | 7.00 | 86.8 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.43 | 13.51 | 21.77 | 2.00 | 69.8 | 90.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.6 | 3.56 | 10.10 | 15.03 | 2.00 | 85.7 | 90.0 |
| Captain | Captain | Declan Rice | MID | 1 | 7.6 | 6.03 | 17.87 | 28.10 | 5.00 | 89.4 | 75.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.61 | 16.11 | 26.72 | 13.00 | 86.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.51 | 15.50 | 25.06 | 8.00 | 88.1 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.75 | 15.35 | 25.72 | 1.00 | 74.2 | 85.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.03 | 14.36 | 22.62 | 2.00 | 84.6 | 90.0 |

## GW29

- Train rows: 182721
- Bank: 0.10 -> 1.70
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Antoine Semenyo
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 67.25
- Actual score: 94.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.42) beats the best remaining Triple Captain opportunity (7.87).
- Transfer: Morgan Rogers -> Harry Wilson (projected gain 0.24, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (6.42) beats the best remaining Triple Captain opportunity (7.87).
- Autosub: James Hill replaced Harry Wilson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.80 | 11.10 | 18.36 | 7.00 | 89.7 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.10 | 0.14 | 0.24 | 0.00 | 1.5 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.25 | 15.68 | 24.93 | 11.00 | 87.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.95 | 14.31 | 22.35 | 1.00 | 88.5 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.44 | 12.38 | 19.35 | 1.00 | 88.9 | 90.0 |
| Bench 2 | Autosub In | James Hill | DEF | 4 | 4.0 | 3.52 | 9.78 | 15.29 | 8.00 | 88.1 | 90.0 |
| Bench 3 | Bench | Hugo Bueno López | DEF | 20 | 4.3 | 3.49 | 9.46 | 14.95 | 1.00 | 88.9 | 11.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 4.86 | 14.30 | 22.75 | 4.00 | 89.2 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.73 | 13.97 | 22.98 | 19.00 | 78.0 | 84.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.6 | 3.35 | 9.19 | 13.90 | 2.00 | 86.2 | 69.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.9 | 6.42 | 17.72 | 29.10 | 8.00 | 90.0 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 8.1 | 6.22 | 17.36 | 28.11 | 7.00 | 88.7 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.91 | 16.34 | 27.56 | 9.00 | 80.4 | 84.0 |
| XI | XI | Declan Rice | MID | 1 | 7.5 | 4.26 | 13.31 | 21.91 | 3.00 | 82.2 | 90.0 |
| XI | Bench | Harry Wilson | MID | 10 | 6.0 | 4.58 | 12.28 | 18.91 | 0.00 | 79.1 | 0.0 |

## GW30

- Train rows: 183541
- Bank: 1.70 -> 0.80
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 72.71
- Actual score: 76.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.69) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Harry Wilson -> Dominik Szoboszlai (projected gain 2.66, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.69) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.04 | 11.19 | 18.51 | 7.00 | 89.2 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.11 | 0.17 | 0.00 | 2.3 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 4.96 | 14.34 | 24.12 | 9.00 | 87.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.03 | 13.90 | 22.00 | 2.00 | 86.9 | 90.0 |
| Bench 2 | Bench Boost | Marc Guéhi | DEF | 13 | 5.2 | 3.89 | 10.65 | 17.25 | 2.00 | 83.0 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.1 | 4.09 | 10.13 | 16.78 | 8.00 | 86.7 | 90.0 |
| Bench 4 | Bench Boost | Hugo Bueno López | DEF | 20 | 4.3 | 2.39 | 7.42 | 12.70 | 1.00 | 58.4 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.55 | 17.51 | 27.60 | 2.00 | 84.4 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 4.65 | 14.32 | 23.39 | 6.00 | 89.0 | 90.0 |
| Bench 3 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 2.41 | 7.11 | 12.24 | 1.00 | 63.6 | 45.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.9 | 6.66 | 19.79 | 32.14 | 10.00 | 90.9 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.77 | 17.75 | 29.24 | 2.00 | 85.2 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 6.12 | 17.10 | 27.83 | 2.00 | 87.2 | 74.0 |
| XI | XI | Declan Rice | MID | 1 | 7.4 | 4.88 | 13.71 | 22.98 | 3.00 | 84.5 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.9 | 4.61 | 13.12 | 19.96 | 11.00 | 80.9 | 90.0 |