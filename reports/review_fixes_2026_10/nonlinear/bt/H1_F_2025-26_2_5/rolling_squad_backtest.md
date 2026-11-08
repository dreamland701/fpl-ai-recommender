# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 233.60
- Total actual points: 232.00
- Average predicted points: 58.40
- Average actual points: 58.00
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW1 are included before the first simulated week.
- League-average scores were not available for this run.

## GW2

- Train rows: 161967
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Cole Palmer
- Vice captain: Antoine Semenyo
- Effective captain: Antoine Semenyo
- Chip used: none
- Predicted score: 60.68
- Actual score: 45.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Tijjani Reijnders replaced Cole Palmer.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.5 | 2.19 | 10.49 | 16.97 | 0.00 | 84.1 | 0.0 |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 2.96 | 10.48 | 17.06 | 1.00 | 79.4 | 90.0 |
| XI | XI | Daniel Ballard | DEF | 17 | 4.6 | 4.71 | 17.21 | 27.28 | 1.00 | 84.9 | 8.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.17 | 12.38 | 19.76 | 6.00 | 88.0 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 3.59 | 12.13 | 19.26 | 5.00 | 85.2 | 68.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 4.12 | 12.12 | 19.41 | 6.00 | 89.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.46 | 11.72 | 19.24 | 3.00 | 86.6 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.6 | 5.42 | 14.57 | 23.70 | 2.00 | 77.1 | 87.0 |
| XI | XI | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 4.19 | 10.56 | 17.21 | 2.00 | 65.7 | 62.0 |
| Bench 4 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.88 | 7.39 | 12.02 | 2.00 | 58.1 | 85.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.5 | 6.14 | 22.59 | 37.98 | 5.00 | 78.2 | 90.0 |
| Bench 2 | Autosub In | Tijjani Reijnders | MID | 13 | 5.6 | 3.57 | 20.67 | 32.32 | 2.00 | 85.8 | 90.0 |
| Captain | Bench | Cole Palmer | MID | 7 | 10.5 | 7.11 | 17.32 | 28.70 | 0.00 | 81.6 | 0.0 |
| Vice Captain | Captain | Antoine Semenyo | MID | 4 | 7.1 | 6.68 | 16.65 | 25.84 | 6.00 | 89.3 | 90.0 |
| Bench 3 | Bench | Mohammed Kudus | MID | 18 | 6.5 | 3.31 | 14.94 | 24.53 | 3.00 | 84.3 | 85.0 |

## GW3

- Train rows: 162672
- Bank: 0.10 -> 1.50
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Chris Wood
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 51.05
- Actual score: 56.00
- Transfer: Cole Palmer -> Bruno Borges Fernandes (projected gain 8.72, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 2.90 | 7.90 | 13.00 | 8.00 | 85.4 | 90.0 |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.5 | 1.02 | 4.04 | 7.00 | 0.00 | 25.3 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 3.89 | 13.34 | 20.85 | 6.00 | 75.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 3.04 | 10.63 | 17.61 | 8.00 | 85.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 3.34 | 10.21 | 16.71 | 1.00 | 86.5 | 4.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 3.22 | 9.99 | 16.34 | 2.00 | 84.4 | 90.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 1.28 | 6.84 | 11.85 | 0.00 | 14.7 | 0.0 |
| Vice Captain | XI | Chris Wood | FWD | 16 | 7.6 | 5.34 | 16.82 | 25.71 | 2.00 | 81.8 | 72.0 |
| Bench 2 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.96 | 7.74 | 12.88 | 2.00 | 52.9 | 64.0 |
| Bench 3 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.06 | 7.26 | 11.86 | 6.00 | 65.5 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.5 | 4.92 | 22.35 | 37.38 | 3.00 | 83.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 4.62 | 15.85 | 24.47 | 2.00 | 86.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.0 | 6.13 | 15.62 | 25.49 | 10.00 | 87.1 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.27 | 15.54 | 24.38 | 2.00 | 83.1 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.23 | 12.27 | 18.96 | 2.00 | 85.0 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 1.50 -> 1.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Antoine Semenyo
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 57.90
- Actual score: 76.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.31) beats the best remaining Bench Boost opportunity (7.58).
- Transfer: Chris Wood -> João Pedro Junqueira de Jesus (projected gain 10.03, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.31) beats the best remaining Bench Boost opportunity (7.58).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 3.03 | 9.56 | 14.59 | 10.00 | 86.7 | 90.0 |
| Bench 1 | Bench Boost | Marco Bizot | GK | 2 | 4.5 | 2.01 | 6.86 | 9.85 | 0.00 | 70.8 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 3.76 | 13.48 | 20.19 | 8.00 | 85.7 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 3.63 | 12.48 | 18.72 | 1.00 | 80.1 | 45.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 3.76 | 12.22 | 18.38 | 9.00 | 84.8 | 90.0 |
| Bench 4 | Bench Boost | William Saliba | DEF | 1 | 6.0 | 0.61 | 7.36 | 11.81 | 0.00 | 16.5 | 0.0 |
| Bench 3 | Bench Boost | Daniel Ballard | DEF | 17 | 4.6 | 0.88 | 4.97 | 7.89 | 0.00 | 11.7 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.74 | 17.76 | 26.46 | 7.00 | 85.8 | 78.0 |
| XI | XI | Lyle Foster | FWD | 3 | 5.0 | 3.19 | 8.99 | 13.35 | 2.00 | 82.0 | 85.0 |
| Bench 2 | Bench Boost | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.77 | 7.98 | 12.20 | 0.00 | 46.6 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 6.19 | 23.79 | 37.44 | 9.00 | 85.9 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.2 | 4.86 | 17.71 | 25.52 | 13.00 | 89.1 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.25 | 14.63 | 23.32 | 2.00 | 87.0 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.21 | 12.90 | 19.41 | 3.00 | 86.8 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.82 | 11.88 | 18.07 | 3.00 | 80.9 | 90.0 |

## GW5

- Train rows: 164124
- Bank: 1.40 -> 0.40
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Mohamed Salah
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 63.98
- Actual score: 55.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.15) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Daniel Ballard -> Daniel Muñoz Mejía (projected gain 2.04, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (7.15) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 3.18 | 9.60 | 15.40 | 2.00 | 84.2 | 90.0 |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.5 | 0.71 | 3.12 | 4.96 | 0.00 | 24.6 | 0.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.6 | 3.91 | 12.41 | 18.72 | 2.00 | 84.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.53 | 12.17 | 18.76 | 4.00 | 85.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.26 | 11.78 | 18.28 | 2.00 | 86.2 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.1 | 3.02 | 10.00 | 16.50 | 0.00 | 61.1 | 63.0 |
| Bench 4 | Bench | William Saliba | DEF | 1 | 6.0 | 1.35 | 5.60 | 9.61 | 2.00 | 33.3 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.10 | 16.46 | 26.20 | 2.00 | 81.1 | 90.0 |
| XI | XI | Lyle Foster | FWD | 3 | 5.0 | 3.55 | 8.44 | 13.50 | 6.00 | 79.9 | 85.0 |
| Bench 3 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 1.35 | 4.89 | 8.01 | 1.00 | 24.4 | 10.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 6.62 | 22.10 | 36.06 | 5.00 | 86.1 | 90.0 |
| Captain | Captain | Antoine Semenyo | MID | 4 | 7.3 | 7.13 | 17.90 | 27.28 | 5.00 | 89.5 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.40 | 14.28 | 22.82 | 10.00 | 80.0 | 86.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.02 | 11.86 | 19.44 | 7.00 | 80.0 | 90.0 |
| Bench 2 | Bench | Tijjani Reijnders | MID | 13 | 5.6 | 2.57 | 10.54 | 17.52 | 9.00 | 82.0 | 90.0 |