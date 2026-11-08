# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 220.43
- Total actual points: 220.00
- Average predicted points: 55.11
- Average actual points: 55.00
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
- Bank: 100.00 -> 1.60
- Free transfers: 1 -> 2
- Captain: Declan Rice
- Vice captain: Cole Palmer
- Effective captain: Declan Rice
- Chip used: none
- Predicted score: 57.09
- Actual score: 46.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub outfielders: Igor Thiago Nascimento Rodrigues.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.95 | 11.86 | 18.84 | 3.00 | 116.4 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 3.19 | 9.80 | 14.96 | 2.00 | 123.2 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.15 | 16.58 | 26.20 | 2.00 | 118.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.92 | 11.59 | 19.27 | 11.00 | 93.4 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 3.84 | 11.09 | 17.26 | 2.00 | 92.2 | 90.0 |
| Bench 3 | Bench | Hugo Bueno López | DEF | 20 | 4.3 | 3.40 | 10.53 | 16.32 | 4.00 | 110.6 | 90.0 |
| Bench 4 | Bench | Ibrahima Konaté | DEF | 12 | 5.4 | 3.12 | 9.53 | 15.08 | 9.00 | 89.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.82 | 13.29 | 21.33 | 7.00 | 84.5 | 79.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 4.10 | 11.86 | 17.72 | 2.00 | 123.7 | 90.0 |
| Bench 2 | Autosub In | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 3.65 | 11.70 | 19.03 | 2.00 | 84.7 | 90.0 |
| Captain | Captain | Declan Rice | MID | 1 | 7.5 | 6.05 | 17.58 | 28.07 | 4.00 | 125.6 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.5 | 5.82 | 15.41 | 24.61 | 3.00 | 86.2 | 74.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.9 | 4.84 | 14.08 | 23.46 | 4.00 | 93.9 | 86.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.9 | 4.60 | 13.32 | 21.56 | 2.00 | 88.1 | 90.0 |
| XI | Bench | Florian Wirtz | MID | 12 | 8.4 | 3.95 | 12.82 | 22.83 | 0.00 | 88.5 | 0.0 |

## GW28

- Train rows: 181902
- Bank: 1.60 -> 2.30
- Free transfers: 2 -> 2
- Captain: Declan Rice
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Declan Rice
- Chip used: none
- Predicted score: 50.70
- Actual score: 55.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Florian Wirtz -> Morgan Rogers (projected gain 2.98, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.39 | 10.29 | 16.75 | 3.00 | 95.9 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 2.41 | 6.58 | 11.12 | 8.00 | 96.3 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 4.76 | 14.03 | 22.74 | 9.00 | 109.6 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 3.94 | 12.01 | 18.93 | 6.00 | 88.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.90 | 11.02 | 17.94 | 7.00 | 89.4 | 90.0 |
| Bench 3 | Bench | Ibrahima Konaté | DEF | 12 | 5.4 | 3.21 | 9.29 | 14.54 | 1.00 | 88.6 | 90.0 |
| Bench 4 | Bench | Hugo Bueno López | DEF | 20 | 4.3 | 3.17 | 9.24 | 14.33 | 6.00 | 98.9 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.15 | 12.93 | 20.80 | 2.00 | 80.6 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 3.93 | 11.21 | 18.72 | 6.00 | 84.4 | 90.0 |
| Bench 2 | Bench | Mateus Mané | FWD | 20 | 4.6 | 3.26 | 10.32 | 15.99 | 2.00 | 98.1 | 90.0 |
| Captain | Captain | Declan Rice | MID | 1 | 7.6 | 4.98 | 15.15 | 24.15 | 5.00 | 105.0 | 75.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.73 | 13.25 | 22.21 | 2.00 | 85.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 4.31 | 12.55 | 20.97 | 8.00 | 68.9 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 3.88 | 12.48 | 20.23 | 1.00 | 81.8 | 85.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.9 | 3.75 | 11.38 | 18.40 | 1.00 | 84.0 | 85.0 |

## GW29

- Train rows: 182721
- Bank: 2.30 -> 0.40
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 52.82
- Actual score: 76.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (4.77) beats the best remaining Triple Captain opportunity (5.77).
- Transfer: Enzo Fernández -> Bryan Mbeumo (projected gain 3.22, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (4.77) beats the best remaining Triple Captain opportunity (5.77).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.17 | 9.25 | 15.72 | 7.00 | 94.5 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 2.21 | 6.14 | 10.43 | 3.00 | 97.4 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 3.94 | 12.96 | 21.32 | 11.00 | 110.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 3.98 | 12.28 | 19.46 | 1.00 | 88.8 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.04 | 11.83 | 19.12 | 1.00 | 89.0 | 90.0 |
| Bench 4 | Bench | Ibrahima Konaté | DEF | 12 | 5.4 | 3.03 | 9.05 | 14.19 | 2.00 | 83.0 | 78.0 |
| Bench 2 | Bench | Hugo Bueno López | DEF | 20 | 4.3 | 3.19 | 8.90 | 13.76 | 1.00 | 98.1 | 11.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.08 | 12.85 | 21.30 | 2.00 | 85.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 3.92 | 12.22 | 20.82 | 19.00 | 83.1 | 84.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.6 | 3.13 | 8.67 | 13.24 | 2.00 | 93.1 | 69.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 4.77 | 13.93 | 22.88 | 7.00 | 78.6 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.03 | 13.82 | 23.53 | 9.00 | 80.0 | 84.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.06 | 12.25 | 19.88 | 1.00 | 83.2 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.7 | 3.94 | 12.10 | 21.27 | 1.00 | 81.5 | 76.0 |
| XI | XI | Declan Rice | MID | 1 | 7.6 | 3.35 | 12.07 | 20.01 | 3.00 | 77.8 | 90.0 |

## GW30

- Train rows: 183541
- Bank: 0.40 -> 2.60
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Antoine Semenyo
- Chip used: bench_boost
- Predicted score: 59.82
- Actual score: 43.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.93) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Morgan Rogers -> Elliot Anderson (projected gain 1.10, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.93) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.37 | 9.93 | 16.40 | 7.00 | 91.0 | 90.0 |
| Bench 1 | Bench Boost | José Malheiro de Sá | GK | 20 | 4.2 | 1.99 | 5.83 | 9.33 | 0.00 | 87.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.05 | 12.81 | 20.42 | 2.00 | 86.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 4.11 | 11.58 | 20.01 | 9.00 | 97.1 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 3.46 | 10.78 | 17.55 | 2.00 | 86.7 | 90.0 |
| Bench 2 | Bench Boost | Ibrahima Konaté | DEF | 12 | 5.5 | 2.78 | 7.97 | 12.70 | 0.00 | 79.6 | 0.0 |
| Bench 4 | Bench Boost | Hugo Bueno López | DEF | 20 | 4.3 | 1.85 | 6.32 | 10.56 | 1.00 | 47.6 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 5.34 | 14.82 | 24.74 | 2.00 | 92.9 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 4.00 | 11.25 | 18.53 | 6.00 | 87.2 | 90.0 |
| Bench 3 | Bench Boost | Mateus Mané | FWD | 20 | 4.6 | 2.30 | 6.37 | 11.01 | 1.00 | 73.0 | 45.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.2 | 5.36 | 15.93 | 25.58 | 2.00 | 100.9 | 74.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.50 | 15.42 | 25.17 | 2.00 | 83.5 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.7 | 3.66 | 12.32 | 20.37 | 2.00 | 77.9 | 74.0 |
| XI | XI | Declan Rice | MID | 1 | 7.5 | 3.76 | 11.55 | 19.57 | 3.00 | 83.6 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.94 | 11.41 | 18.23 | 2.00 | 87.1 | 87.0 |