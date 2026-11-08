# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 276.80
- Total actual points: 280.00
- Average predicted points: 69.20
- Average actual points: 70.00
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
- Predicted score: 70.82
- Actual score: 44.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 5.01 | 13.85 | 17.54 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 7.03 | 19.82 | 24.50 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.00 | 14.37 | 22.91 | 11.00 | 90.0 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.8 | 4.67 | 12.44 | 19.98 | 2.00 | 85.2 | 90.0 |
| Bench 3 | Bench | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 4.32 | 11.79 | 14.60 | 4.00 | 90.0 | 90.0 |
| Bench 4 | Bench | James Hill | DEF | 4 | 4.0 | 3.92 | 11.34 | 17.72 | 6.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.24 | 16.48 | 26.05 | 7.00 | 86.2 | 79.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.13 | 14.08 | 22.76 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Mateus Mané | FWD | 20 | 4.6 | 4.88 | 13.15 | 15.66 | 2.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.6 | 6.62 | 18.78 | 23.50 | 4.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.6 | 6.71 | 17.80 | 28.86 | 3.00 | 87.5 | 74.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 6.43 | 17.74 | 23.03 | 4.00 | 90.0 | 86.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.48 | 16.12 | 27.13 | 2.00 | 81.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.49 | 14.96 | 24.39 | 2.00 | 85.4 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 0.10 -> 0.90
- Free transfers: 2 -> 2
- Captain: Declan Rice
- Vice captain: Antoine Semenyo
- Effective captain: Declan Rice
- Chip used: none
- Predicted score: 62.99
- Actual score: 63.00
- Transfer: Trevoh Chalobah -> Marcos Senesi Barón (projected gain 0.07, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.15 | 11.91 | 15.57 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.81 | 16.82 | 21.42 | 9.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.44 | 14.61 | 23.10 | 7.00 | 90.0 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.0 | 4.41 | 11.86 | 18.13 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.13 | 10.92 | 17.65 | 4.00 | 86.2 | 90.0 |
| Bench 4 | Bench | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 3.48 | 10.17 | 12.46 | 9.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.31 | 14.16 | 22.99 | 6.00 | 86.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.49 | 13.97 | 22.79 | 2.00 | 69.9 | 90.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.6 | 3.79 | 11.17 | 13.73 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Declan Rice | MID | 1 | 7.6 | 6.01 | 17.75 | 22.38 | 5.00 | 90.0 | 75.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.95 | 16.96 | 21.74 | 8.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.69 | 16.19 | 27.10 | 13.00 | 86.3 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.59 | 14.65 | 24.17 | 1.00 | 68.3 | 85.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.13 | 14.16 | 22.93 | 2.00 | 82.9 | 90.0 |

## GW29

- Train rows: 182721
- Bank: 0.90 -> 2.40
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Bruno Borges Fernandes
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 68.24
- Actual score: 98.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.71) beats the best remaining Triple Captain opportunity (8.11).
- Transfer: Declan Rice -> Harry Wilson (projected gain 1.97, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.71) beats the best remaining Triple Captain opportunity (8.11).
- Autosub: James Hill replaced Harry Wilson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.97 | 8.00 | 15.70 | 7.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.14 | 14.12 | 22.31 | 1.00 | 88.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.69 | 11.54 | 22.04 | 11.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 3.80 | 10.86 | 20.76 | 11.00 | 89.5 | 90.0 |
| Bench 2 | Autosub In | James Hill | DEF | 4 | 4.0 | 3.61 | 10.43 | 19.49 | 8.00 | 88.1 | 90.0 |
| Bench 4 | Bench | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 3.45 | 6.60 | 12.50 | 1.00 | 90.0 | 31.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.95 | 14.51 | 28.76 | 19.00 | 80.5 | 84.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.66 | 13.70 | 22.21 | 2.00 | 81.2 | 90.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.6 | 3.58 | 6.90 | 12.79 | 2.00 | 90.0 | 69.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.9 | 6.61 | 18.40 | 30.49 | 8.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.79 | 15.63 | 31.13 | 9.00 | 76.5 | 84.0 |
| XI | Bench | Harry Wilson | MID | 10 | 6.0 | 4.60 | 12.62 | 20.25 | 0.00 | 77.8 | 0.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.71 | 12.60 | 30.08 | 7.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 3.91 | 11.54 | 19.38 | 1.00 | 69.3 | 90.0 |

## GW30

- Train rows: 183541
- Bank: 2.40 -> 1.50
- Free transfers: 2 -> 2
- Captain: João Pedro Junqueira de Jesus
- Vice captain: Bruno Borges Fernandes
- Effective captain: João Pedro Junqueira de Jesus
- Chip used: bench_boost
- Predicted score: 74.74
- Actual score: 75.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.39) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Harry Wilson -> Dominik Szoboszlai (projected gain 4.21, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.39) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.21 | 8.06 | 15.80 | 7.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.7 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.14 | 13.97 | 22.37 | 2.00 | 83.9 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.44 | 12.03 | 19.13 | 10.00 | 90.0 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.1 | 4.04 | 10.74 | 17.44 | 8.00 | 86.3 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.33 | 10.47 | 20.84 | 9.00 | 90.0 | 90.0 |
| Bench 4 | Bench Boost | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 2.37 | 4.50 | 9.61 | 1.00 | 56.7 | 90.0 |
| Captain | Captain | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 7.05 | 18.52 | 30.20 | 2.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.29 | 14.46 | 23.05 | 6.00 | 88.6 | 90.0 |
| Bench 3 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 2.43 | 4.63 | 9.65 | 1.00 | 63.9 | 45.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.9 | 6.79 | 20.26 | 33.03 | 10.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.64 | 17.05 | 27.88 | 2.00 | 81.2 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.9 | 4.78 | 13.18 | 20.74 | 11.00 | 81.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 6.59 | 12.61 | 24.13 | 2.00 | 90.0 | 74.0 |
| Bench 2 | Bench Boost | Morgan Rogers | MID | 2 | 7.5 | 3.58 | 11.04 | 18.35 | 2.00 | 75.4 | 90.0 |