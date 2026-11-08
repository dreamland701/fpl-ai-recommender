# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 275.81
- Total actual points: 271.00
- Average predicted points: 68.95
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
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Gabriel dos Santos Magalhães
- Vice captain: Cole Palmer
- Effective captain: Gabriel dos Santos Magalhães
- Chip used: none
- Predicted score: 70.03
- Actual score: 44.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.81 | 13.29 | 16.87 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 1.9 | 0.0 |
| Captain | Captain | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 6.94 | 19.64 | 24.25 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.94 | 14.20 | 22.64 | 11.00 | 90.0 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.8 | 4.60 | 12.24 | 19.68 | 2.00 | 83.8 | 90.0 |
| Bench 3 | Bench | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 4.19 | 11.48 | 14.21 | 4.00 | 90.0 | 90.0 |
| Bench 4 | Bench | James Hill | DEF | 4 | 4.0 | 3.91 | 11.33 | 17.70 | 6.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.11 | 16.11 | 25.49 | 7.00 | 83.6 | 79.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.11 | 14.04 | 22.69 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Mateus Mané | FWD | 20 | 4.6 | 4.82 | 13.04 | 15.51 | 2.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.6 | 6.61 | 18.77 | 23.48 | 4.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.6 | 6.71 | 17.78 | 28.84 | 3.00 | 87.5 | 74.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 6.34 | 17.47 | 22.70 | 4.00 | 90.0 | 86.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.44 | 15.98 | 26.95 | 2.00 | 80.2 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.48 | 14.94 | 24.35 | 2.00 | 85.3 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 0.10 -> 0.60
- Free transfers: 2 -> 2
- Captain: Declan Rice
- Vice captain: Antoine Semenyo
- Effective captain: Declan Rice
- Chip used: none
- Predicted score: 62.93
- Actual score: 63.00
- Transfer: Trevoh Chalobah -> Marc Guéhi (projected gain 0.08, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.02 | 11.57 | 15.12 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 2.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.83 | 16.86 | 21.47 | 9.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.36 | 14.38 | 22.74 | 7.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Marc Guéhi | DEF | 13 | 5.2 | 4.23 | 12.10 | 15.36 | 6.00 | 84.3 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.0 | 4.43 | 11.92 | 18.23 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 3.47 | 10.16 | 12.46 | 9.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.27 | 14.06 | 22.80 | 6.00 | 85.3 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.43 | 13.81 | 22.54 | 2.00 | 68.8 | 90.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.6 | 3.88 | 11.40 | 14.03 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Declan Rice | MID | 1 | 7.6 | 6.12 | 18.04 | 22.75 | 5.00 | 90.0 | 75.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.87 | 16.73 | 21.44 | 8.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.68 | 16.14 | 27.00 | 13.00 | 86.1 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.68 | 14.88 | 24.51 | 1.00 | 70.1 | 85.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.13 | 14.16 | 22.92 | 2.00 | 82.9 | 90.0 |

## GW29

- Train rows: 182721
- Bank: 0.60 -> 0.10
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Bruno Borges Fernandes
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 68.29
- Actual score: 97.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.60) beats the best remaining Triple Captain opportunity (8.06).
- Transfer: Marc Guéhi -> James Tarkowski (projected gain 0.68, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.60) beats the best remaining Triple Captain opportunity (8.06).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.82 | 7.74 | 15.18 | 7.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.05 | 0.05 | 0.09 | 0.00 | 1.9 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.12 | 14.06 | 22.23 | 1.00 | 87.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.66 | 11.46 | 21.92 | 11.00 | 90.0 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.16 | 10.99 | 17.27 | 15.00 | 84.6 | 90.0 |
| Bench 3 | Bench | James Hill | DEF | 4 | 4.0 | 3.61 | 10.43 | 19.55 | 8.00 | 88.3 | 90.0 |
| Bench 4 | Bench | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 3.43 | 6.55 | 12.41 | 1.00 | 90.0 | 31.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.84 | 14.25 | 28.24 | 19.00 | 78.4 | 84.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.65 | 13.68 | 22.16 | 2.00 | 81.0 | 90.0 |
| Bench 2 | Bench | Mateus Mané | FWD | 20 | 4.6 | 3.66 | 7.03 | 13.08 | 2.00 | 90.0 | 69.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.9 | 6.57 | 18.30 | 30.27 | 8.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.89 | 15.89 | 31.62 | 9.00 | 78.5 | 84.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.60 | 12.41 | 29.62 | 7.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 3.96 | 11.66 | 19.53 | 1.00 | 70.2 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.5 | 4.83 | 10.20 | 19.89 | 3.00 | 90.0 | 90.0 |

## GW30

- Train rows: 183541
- Bank: 0.10 -> 0.80
- Free transfers: 2 -> 2
- Captain: João Pedro Junqueira de Jesus
- Vice captain: Bruno Borges Fernandes
- Effective captain: João Pedro Junqueira de Jesus
- Chip used: bench_boost
- Predicted score: 74.56
- Actual score: 67.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.43) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: James Tarkowski -> Marcos Senesi Barón (projected gain 0.69, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.43) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.07 | 7.81 | 15.32 | 7.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.03 | 0.07 | 0.00 | 2.6 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.14 | 13.99 | 22.39 | 2.00 | 84.1 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.39 | 11.89 | 18.92 | 10.00 | 90.0 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.1 | 4.06 | 10.80 | 17.53 | 8.00 | 86.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.32 | 10.44 | 20.78 | 9.00 | 90.0 | 90.0 |
| Bench 4 | Bench Boost | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 2.33 | 4.43 | 9.47 | 1.00 | 55.9 | 90.0 |
| Captain | Captain | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.94 | 18.25 | 29.76 | 2.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.25 | 14.35 | 22.87 | 6.00 | 87.8 | 90.0 |
| Bench 3 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 2.41 | 4.59 | 9.57 | 1.00 | 63.6 | 45.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.9 | 6.77 | 20.21 | 32.94 | 10.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.79 | 17.45 | 28.51 | 2.00 | 84.3 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 6.52 | 12.50 | 23.91 | 2.00 | 90.0 | 74.0 |
| Bench 2 | Bench Boost | Morgan Rogers | MID | 2 | 7.5 | 3.69 | 11.32 | 18.79 | 2.00 | 77.5 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.4 | 4.94 | 9.37 | 18.73 | 3.00 | 84.3 | 90.0 |