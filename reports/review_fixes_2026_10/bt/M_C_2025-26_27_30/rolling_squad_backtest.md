# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 288.18
- Total actual points: 251.00
- Average predicted points: 72.04
- Average actual points: 62.75
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
- Bank: 100.00 -> 1.00
- Free transfers: 1 -> 2
- Captain: Gabriel dos Santos Magalhães
- Vice captain: Declan Rice
- Effective captain: Gabriel dos Santos Magalhães
- Chip used: none
- Predicted score: 71.59
- Actual score: 44.00
- Chip advisory: bench_boost (0.67): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 5.17 | 14.79 | 23.50 | 3.00 | 119.9 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 3.86 | 11.06 | 17.70 | 2.00 | 125.8 | 90.0 |
| Captain | Captain | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 7.32 | 21.00 | 32.42 | 2.00 | 141.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.13 | 14.67 | 23.53 | 11.00 | 97.8 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 5.08 | 14.43 | 22.34 | 2.00 | 98.0 | 90.0 |
| Bench 3 | Bench | Hugo Bueno López | DEF | 20 | 4.3 | 4.40 | 12.55 | 20.38 | 4.00 | 115.0 | 90.0 |
| Bench 4 | Bench | Nordi Mukiele | DEF | 17 | 4.6 | 4.27 | 12.17 | 20.02 | 1.00 | 89.5 | 11.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 5.96 | 16.54 | 26.73 | 7.00 | 84.6 | 79.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 5.42 | 14.96 | 22.54 | 2.00 | 128.4 | 90.0 |
| Bench 2 | Bench | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 4.94 | 14.30 | 23.69 | 2.00 | 87.1 | 90.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.5 | 7.23 | 20.85 | 32.45 | 4.00 | 127.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.9 | 6.01 | 17.21 | 28.39 | 4.00 | 99.3 | 86.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.48 | 16.04 | 27.23 | 2.00 | 79.1 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.5 | 5.91 | 15.87 | 26.06 | 3.00 | 80.0 | 74.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.9 | 5.56 | 15.56 | 25.41 | 2.00 | 89.7 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 1.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Declan Rice
- Vice captain: Antoine Semenyo
- Effective captain: Declan Rice
- Chip used: none
- Predicted score: 65.35
- Actual score: 67.00
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Enzo Fernández -> Morgan Rogers (projected gain 2.28, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.33 | 12.40 | 20.33 | 3.00 | 98.4 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 2.84 | 8.39 | 14.06 | 8.00 | 98.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.91 | 17.06 | 27.25 | 9.00 | 111.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.42 | 14.88 | 23.99 | 7.00 | 92.6 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.76 | 13.93 | 22.23 | 6.00 | 91.7 | 90.0 |
| Bench 3 | Bench | Hugo Bueno López | DEF | 20 | 4.3 | 4.17 | 12.03 | 19.20 | 6.00 | 103.9 | 90.0 |
| Bench 4 | Bench | Nordi Mukiele | DEF | 17 | 4.6 | 2.76 | 9.08 | 15.29 | 0.00 | 60.7 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 5.64 | 17.01 | 27.37 | 2.00 | 84.9 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.32 | 14.99 | 24.64 | 6.00 | 85.6 | 90.0 |
| Bench 2 | Bench | Mateus Mané | FWD | 20 | 4.6 | 4.38 | 12.54 | 19.47 | 2.00 | 103.6 | 90.0 |
| Captain | Captain | Declan Rice | MID | 1 | 7.5 | 6.25 | 18.18 | 28.70 | 5.00 | 106.2 | 75.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.9 | 5.95 | 17.51 | 28.41 | 8.00 | 93.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.40 | 15.82 | 26.77 | 13.00 | 82.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.5 | 4.87 | 14.83 | 24.22 | 1.00 | 73.5 | 85.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.26 | 14.82 | 24.04 | 2.00 | 85.5 | 90.0 |

## GW29

- Train rows: 182721
- Bank: 0.20 -> 0.70
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Bruno Borges Fernandes
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 72.18
- Actual score: 83.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.74) beats the best remaining Triple Captain opportunity (7.95).
- Chip advisory: bench_boost (0.62): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Nordi Mukiele -> James Hill (projected gain 0.08, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.74) beats the best remaining Triple Captain opportunity (7.95).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.04 | 12.43 | 20.50 | 7.00 | 97.5 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 3.04 | 8.84 | 14.61 | 3.00 | 99.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.77 | 17.41 | 27.85 | 11.00 | 112.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.56 | 15.73 | 25.18 | 1.00 | 93.3 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 5.02 | 14.30 | 22.81 | 1.00 | 93.4 | 90.0 |
| Bench 2 | Bench | Hugo Bueno López | DEF | 20 | 4.3 | 4.14 | 11.86 | 18.82 | 1.00 | 102.3 | 11.0 |
| Bench 4 | Bench | James Hill | DEF | 4 | 4.1 | 3.91 | 11.31 | 17.87 | 8.00 | 91.8 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 5.58 | 16.49 | 27.33 | 19.00 | 86.1 | 84.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.10 | 14.95 | 24.29 | 2.00 | 86.4 | 90.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.6 | 4.01 | 11.45 | 17.79 | 2.00 | 97.4 | 69.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.0 | 6.74 | 19.40 | 31.22 | 7.00 | 104.3 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 6.10 | 18.10 | 30.18 | 8.00 | 93.8 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.5 | 5.38 | 16.40 | 26.38 | 3.00 | 97.4 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.5 | 4.60 | 14.76 | 24.74 | 9.00 | 71.9 | 84.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.83 | 13.86 | 22.77 | 1.00 | 82.4 | 90.0 |

## GW30

- Train rows: 183541
- Bank: 0.70 -> 2.60
- Free transfers: 2 -> 2
- Captain: João Pedro Junqueira de Jesus
- Vice captain: Antoine Semenyo
- Effective captain: João Pedro Junqueira de Jesus
- Chip used: bench_boost
- Predicted score: 79.06
- Actual score: 57.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (12.12) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Morgan Rogers -> Crysencio Summerville (projected gain 1.99, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (12.12) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.24 | 12.45 | 20.51 | 7.00 | 94.0 | 90.0 |
| Bench 1 | Bench Boost | José Malheiro de Sá | GK | 20 | 4.2 | 2.69 | 8.12 | 13.57 | 0.00 | 87.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.39 | 15.82 | 26.32 | 9.00 | 98.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.30 | 15.33 | 24.81 | 2.00 | 90.7 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.51 | 12.97 | 21.03 | 2.00 | 89.2 | 90.0 |
| Bench 2 | Bench Boost | James Hill | DEF | 4 | 4.1 | 4.23 | 11.78 | 19.28 | 8.00 | 90.2 | 90.0 |
| Bench 4 | Bench Boost | Hugo Bueno López | DEF | 20 | 4.3 | 2.59 | 8.14 | 14.00 | 1.00 | 60.8 | 90.0 |
| Captain | Captain | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 7.06 | 20.06 | 32.96 | 2.00 | 101.2 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.32 | 14.87 | 23.95 | 6.00 | 88.0 | 90.0 |
| Bench 3 | Bench Boost | Mateus Mané | FWD | 20 | 4.6 | 2.61 | 7.69 | 13.36 | 1.00 | 66.6 | 45.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.9 | 6.68 | 20.01 | 32.77 | 10.00 | 100.2 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 8.0 | 6.89 | 19.96 | 31.98 | 2.00 | 106.4 | 74.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.5 | 5.10 | 16.28 | 26.75 | 2.00 | 76.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.5 | 4.69 | 13.77 | 23.09 | 3.00 | 79.7 | 90.0 |
| XI | XI | Crysencio Summerville | MID | 19 | 5.7 | 4.68 | 13.75 | 22.23 | 0.00 | 91.0 | 0.0 |