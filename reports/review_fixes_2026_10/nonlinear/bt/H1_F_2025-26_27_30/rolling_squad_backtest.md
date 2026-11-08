# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 244.75
- Total actual points: 284.00
- Average predicted points: 61.19
- Average actual points: 71.00
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
- Captain: Cole Palmer
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 61.82
- Actual score: 44.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.13 | 13.85 | 21.88 | 3.00 | 85.7 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 2.91 | 10.04 | 16.30 | 2.00 | 81.7 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.95 | 19.62 | 30.20 | 2.00 | 85.1 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 5.26 | 15.06 | 23.38 | 3.00 | 82.1 | 56.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.91 | 14.22 | 22.60 | 11.00 | 85.8 | 90.0 |
| Bench 2 | Bench | Marc Guéhi | DEF | 13 | 5.2 | 3.65 | 13.48 | 20.50 | 2.00 | 85.7 | 90.0 |
| Bench 4 | Bench | James Hill | DEF | 4 | 4.0 | 3.08 | 11.30 | 17.73 | 6.00 | 84.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.49 | 16.50 | 26.07 | 7.00 | 79.3 | 79.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 4.38 | 13.25 | 19.86 | 2.00 | 81.0 | 90.0 |
| Bench 3 | Bench | Adam Armstrong | FWD | 20 | 5.5 | 3.35 | 12.58 | 20.29 | 2.00 | 66.8 | 62.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.6 | 7.46 | 18.05 | 29.25 | 3.00 | 81.3 | 74.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 3.66 | 17.66 | 28.41 | 4.00 | 87.3 | 86.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 4.52 | 16.30 | 27.60 | 2.00 | 84.5 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.79 | 14.96 | 24.27 | 2.00 | 86.4 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.9 | 4.81 | 14.38 | 23.40 | 2.00 | 77.1 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 0.40 -> 1.30
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Morgan Rogers
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 55.82
- Actual score: 80.00
- Transfer: Enzo Fernández -> Harry Wilson (projected gain 1.35, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.92 | 11.82 | 19.21 | 3.00 | 87.6 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 2.73 | 7.71 | 12.95 | 8.00 | 82.2 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 4.72 | 16.52 | 26.10 | 9.00 | 86.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.62 | 14.73 | 23.18 | 7.00 | 86.8 | 90.0 |
| Bench 2 | Bench | Marc Guéhi | DEF | 13 | 5.2 | 3.98 | 12.20 | 19.25 | 6.00 | 83.5 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.20 | 11.91 | 19.30 | 8.00 | 59.7 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.0 | 4.39 | 11.84 | 18.13 | 2.00 | 83.6 | 90.0 |
| Bench 3 | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 2.61 | 13.99 | 22.71 | 2.00 | 64.9 | 90.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 3.66 | 11.19 | 17.14 | 2.00 | 84.6 | 90.0 |
| Bench 4 | Bench | Adam Armstrong | FWD | 20 | 5.4 | 2.09 | 9.29 | 15.33 | 4.00 | 52.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 4.60 | 16.88 | 26.93 | 8.00 | 86.5 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.8 | 6.39 | 16.35 | 27.33 | 13.00 | 83.5 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.03 | 14.69 | 24.29 | 1.00 | 68.5 | 85.0 |
| Vice Captain | XI | Morgan Rogers | MID | 2 | 7.7 | 4.77 | 14.10 | 22.65 | 2.00 | 85.6 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.15 | 13.37 | 20.95 | 12.00 | 85.2 | 71.0 |

## GW29

- Train rows: 182721
- Bank: 1.30 -> 0.90
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Bruno Borges Fernandes
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 61.68
- Actual score: 94.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.56) beats the best remaining Triple Captain opportunity (7.74).
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Morgan Rogers -> Matheus Santos Carneiro da Cunha (projected gain 3.44, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.56) beats the best remaining Triple Captain opportunity (7.74).
- Autosub: Matheus Santos Carneiro da Cunha replaced Harry Wilson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.72 | 12.00 | 19.55 | 7.00 | 88.3 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 3.21 | 7.77 | 13.03 | 3.00 | 86.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 4.58 | 17.12 | 27.16 | 11.00 | 86.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.83 | 14.35 | 22.57 | 1.00 | 86.3 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 3.93 | 13.09 | 21.47 | 13.00 | 82.5 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.07 | 13.07 | 20.52 | 1.00 | 84.4 | 90.0 |
| Bench 3 | Bench | James Hill | DEF | 4 | 4.0 | 3.37 | 10.37 | 16.23 | 8.00 | 86.7 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 3.59 | 14.72 | 24.25 | 19.00 | 72.4 | 84.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 3.71 | 10.39 | 15.98 | 2.00 | 78.4 | 69.0 |
| Bench 4 | Bench | Adam Armstrong | FWD | 20 | 5.4 | 3.10 | 9.99 | 15.87 | 1.00 | 81.3 | 59.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.56 | 18.81 | 29.81 | 7.00 | 86.9 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.9 | 4.97 | 18.43 | 30.40 | 8.00 | 83.8 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.11 | 15.81 | 26.42 | 9.00 | 72.2 | 84.0 |
| XI | Bench | Harry Wilson | MID | 10 | 5.9 | 4.47 | 12.72 | 20.27 | 0.00 | 76.9 | 0.0 |
| Bench 2 | Autosub In | Matheus Santos Carneiro da Cunha | MID | 14 | 8.0 | 3.58 | 11.64 | 18.57 | 2.00 | 72.3 | 90.0 |

## GW30

- Train rows: 183541
- Bank: 0.90 -> 0.00
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Antoine Semenyo
- Effective captain: Cole Palmer
- Chip used: bench_boost
- Predicted score: 65.42
- Actual score: 66.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.46) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: James Hill -> Marcos Senesi Barón (projected gain 1.15, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.46) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.13 | 12.01 | 19.58 | 7.00 | 87.0 | 90.0 |
| Bench 1 | Bench Boost | José Malheiro de Sá | GK | 20 | 4.2 | 2.76 | 7.68 | 12.82 | 0.00 | 86.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.09 | 15.45 | 25.61 | 9.00 | 87.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 3.37 | 13.98 | 22.24 | 2.00 | 84.8 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 4.00 | 13.55 | 22.19 | 1.00 | 80.8 | 37.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.51 | 11.94 | 18.90 | 10.00 | 86.2 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 3.80 | 11.58 | 18.53 | 2.00 | 84.1 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.94 | 19.05 | 30.74 | 2.00 | 81.5 | 90.0 |
| Bench 4 | Bench Boost | Adam Armstrong | FWD | 20 | 5.3 | 2.07 | 8.71 | 14.27 | 5.00 | 57.6 | 86.0 |
| Bench 3 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 2.74 | 7.15 | 12.31 | 1.00 | 57.2 | 45.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.9 | 5.11 | 20.28 | 32.93 | 10.00 | 86.3 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 8.1 | 5.39 | 18.84 | 29.80 | 2.00 | 86.4 | 74.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.6 | 5.68 | 17.05 | 27.94 | 2.00 | 78.6 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.0 | 4.25 | 12.37 | 19.62 | 8.00 | 71.7 | 90.0 |
| Bench 2 | Bench Boost | Harry Wilson | MID | 10 | 5.9 | 2.88 | 8.11 | 13.88 | 3.00 | 54.9 | 90.0 |