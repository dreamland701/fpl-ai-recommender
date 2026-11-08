# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 283.02
- Total actual points: 244.00
- Average predicted points: 70.76
- Average actual points: 61.00
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
- Bank: 100.00 -> 1.20
- Free transfers: 1 -> 2
- Captain: Gabriel dos Santos Magalhães
- Vice captain: Antoine Semenyo
- Effective captain: Gabriel dos Santos Magalhães
- Chip used: none
- Predicted score: 69.49
- Actual score: 42.00
- Chip advisory: bench_boost (0.67): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub outfielders: Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 5.20 | 14.85 | 23.68 | 3.00 | 119.9 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 3.85 | 11.04 | 17.60 | 2.00 | 125.8 | 90.0 |
| Captain | Captain | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 7.35 | 21.04 | 32.90 | 2.00 | 141.2 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 5.60 | 15.64 | 24.11 | 3.00 | 117.8 | 56.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.15 | 14.61 | 23.47 | 11.00 | 97.8 | 90.0 |
| Bench 2 | Autosub In | Marc Guéhi | DEF | 13 | 5.2 | 5.10 | 14.44 | 22.72 | 2.00 | 97.9 | 90.0 |
| Bench 4 | Bench | Hugo Bueno López | DEF | 20 | 4.3 | 4.39 | 12.51 | 20.07 | 4.00 | 115.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 5.93 | 16.50 | 26.56 | 7.00 | 84.6 | 79.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 5.41 | 15.11 | 22.96 | 2.00 | 128.4 | 90.0 |
| Bench 3 | Bench | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 4.92 | 14.26 | 23.52 | 2.00 | 87.1 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.9 | 6.03 | 17.21 | 28.18 | 4.00 | 99.3 | 86.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.48 | 15.96 | 26.65 | 2.00 | 79.1 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.9 | 5.53 | 15.49 | 25.19 | 2.00 | 89.7 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 5.37 | 15.13 | 24.72 | 2.00 | 83.8 | 90.0 |
| XI | Bench | Florian Wirtz | MID | 12 | 8.4 | 5.11 | 14.82 | 23.78 | 0.00 | 87.7 | 0.0 |

## GW28

- Train rows: 181902
- Bank: 1.20 -> 1.00
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Antoine Semenyo
- Chip used: none
- Predicted score: 63.05
- Actual score: 68.00
- Chip advisory: bench_boost (0.62): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Florian Wirtz -> Bryan Mbeumo (projected gain 0.45, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.32 | 12.36 | 20.28 | 3.00 | 98.4 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 2.81 | 8.33 | 13.85 | 8.00 | 98.9 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.90 | 17.00 | 27.33 | 9.00 | 111.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.45 | 14.93 | 24.03 | 7.00 | 92.6 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.76 | 13.90 | 22.29 | 6.00 | 91.7 | 90.0 |
| Bench 3 | Bench | Jurriën Timber | DEF | 1 | 6.4 | 4.20 | 12.03 | 19.34 | 8.00 | 84.4 | 90.0 |
| Bench 4 | Bench | Hugo Bueno López | DEF | 20 | 4.3 | 4.14 | 11.90 | 19.02 | 6.00 | 104.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.61 | 16.95 | 27.27 | 2.00 | 85.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.29 | 14.88 | 24.27 | 6.00 | 85.7 | 90.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 4.34 | 12.50 | 19.53 | 2.00 | 103.7 | 90.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.0 | 5.95 | 17.44 | 28.34 | 8.00 | 93.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.39 | 15.74 | 26.36 | 13.00 | 82.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.29 | 14.86 | 24.06 | 2.00 | 85.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.6 | 4.81 | 14.02 | 22.50 | 2.00 | 75.7 | 85.0 |
| Bench 2 | Bench | Enzo Fernández | MID | 7 | 6.9 | 4.32 | 13.62 | 22.41 | 1.00 | 82.9 | 85.0 |

## GW29

- Train rows: 182721
- Bank: 1.00 -> 1.90
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Bruno Borges Fernandes
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 72.11
- Actual score: 85.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.76) beats the best remaining Triple Captain opportunity (7.97).
- Chip advisory: bench_boost (0.62): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Enzo Fernández -> Harry Wilson (projected gain 1.38, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.76) beats the best remaining Triple Captain opportunity (7.97).
- Autosub outfielders: Jurriën Timber.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.02 | 12.37 | 20.40 | 7.00 | 97.6 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 3.05 | 8.81 | 14.48 | 3.00 | 99.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.75 | 17.34 | 27.79 | 11.00 | 112.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.59 | 15.78 | 25.28 | 1.00 | 93.2 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 5.04 | 14.35 | 22.93 | 1.00 | 93.3 | 90.0 |
| Bench 2 | Autosub In | Jurriën Timber | DEF | 1 | 6.4 | 4.22 | 12.50 | 20.36 | 13.00 | 89.9 | 90.0 |
| Bench 3 | Bench | Hugo Bueno López | DEF | 20 | 4.3 | 4.15 | 11.77 | 18.63 | 1.00 | 102.3 | 11.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.55 | 16.40 | 27.04 | 19.00 | 86.2 | 84.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.07 | 14.87 | 24.05 | 2.00 | 86.5 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.6 | 4.02 | 11.35 | 17.67 | 2.00 | 97.4 | 69.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.76 | 19.33 | 31.04 | 7.00 | 104.3 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.9 | 6.12 | 18.05 | 29.92 | 8.00 | 93.8 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.7 | 4.95 | 14.43 | 23.20 | 1.00 | 77.9 | 76.0 |
| XI | Bench | Harry Wilson | MID | 10 | 5.9 | 4.92 | 13.85 | 22.33 | 0.00 | 82.8 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.82 | 13.82 | 22.55 | 1.00 | 82.4 | 90.0 |

## GW30

- Train rows: 183541
- Bank: 1.90 -> 2.20
- Free transfers: 2 -> 2
- Captain: João Pedro Junqueira de Jesus
- Vice captain: Antoine Semenyo
- Effective captain: João Pedro Junqueira de Jesus
- Chip used: bench_boost
- Predicted score: 78.38
- Actual score: 49.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.90) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Harry Wilson -> Crysencio Summerville (projected gain 1.30, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.90) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.24 | 12.39 | 20.35 | 7.00 | 94.0 | 90.0 |
| Bench 1 | Bench Boost | José Malheiro de Sá | GK | 20 | 4.2 | 2.67 | 8.08 | 13.45 | 0.00 | 87.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.38 | 15.80 | 26.28 | 9.00 | 98.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 5.33 | 15.36 | 24.88 | 2.00 | 90.7 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 4.58 | 13.21 | 21.48 | 1.00 | 88.2 | 37.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.54 | 12.99 | 21.05 | 2.00 | 89.1 | 90.0 |
| Bench 4 | Bench Boost | Hugo Bueno López | DEF | 20 | 4.3 | 2.57 | 8.08 | 13.82 | 1.00 | 60.8 | 90.0 |
| Captain | Captain | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 7.08 | 20.01 | 32.63 | 2.00 | 101.2 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 5.35 | 14.78 | 23.70 | 6.00 | 87.9 | 90.0 |
| Bench 3 | Bench Boost | Mateus Mané | FWD | 20 | 4.6 | 2.59 | 7.63 | 13.32 | 1.00 | 66.6 | 45.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 8.2 | 6.92 | 19.89 | 31.70 | 2.00 | 106.3 | 74.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.0 | 6.65 | 19.88 | 32.37 | 10.00 | 100.3 | 90.0 |
| XI | XI | Crysencio Summerville | MID | 19 | 5.7 | 4.70 | 13.73 | 22.08 | 0.00 | 90.9 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.7 | 4.63 | 13.64 | 22.68 | 2.00 | 72.6 | 74.0 |
| Bench 2 | Bench Boost | Morgan Rogers | MID | 2 | 7.6 | 4.07 | 12.52 | 20.78 | 2.00 | 81.0 | 90.0 |