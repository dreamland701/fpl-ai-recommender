# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 269.53
- Total actual points: 218.00
- Average predicted points: 67.38
- Average actual points: 54.50
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
- Captain: Tijjani Reijnders
- Vice captain: Mohamed Salah
- Effective captain: Tijjani Reijnders
- Chip used: none
- Predicted score: 75.52
- Actual score: 47.00
- Chip advisory: bench_boost (0.62): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Virgil van Dijk replaced Cole Palmer.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 4.59 | 11.02 | 17.84 | 6.00 | 119.3 | 90.0 |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.5 | 3.91 | 10.07 | 16.56 | 0.00 | 103.6 | 0.0 |
| XI | XI | Daniel Ballard | DEF | 17 | 4.6 | 6.21 | 15.87 | 25.84 | 1.00 | 112.6 | 8.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 5.28 | 12.69 | 20.16 | 6.00 | 121.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 5.19 | 12.43 | 19.80 | 6.00 | 123.4 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 4.84 | 11.88 | 18.99 | 5.00 | 104.9 | 68.0 |
| Bench 2 | Autosub In | Virgil van Dijk | DEF | 12 | 6.0 | 4.54 | 11.66 | 19.10 | 3.00 | 106.9 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.6 | 5.83 | 14.69 | 23.77 | 2.00 | 109.5 | 87.0 |
| Bench 4 | Bench | Lukas Nmecha | FWD | 11 | 5.0 | 2.80 | 7.89 | 13.42 | 1.00 | 50.5 | 32.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 3.75 | 6.45 | 9.78 | 2.00 | 48.4 | 4.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 8.15 | 22.84 | 38.18 | 5.00 | 120.7 | 90.0 |
| Captain | Captain | Tijjani Reijnders | MID | 13 | 5.6 | 8.59 | 20.83 | 32.33 | 2.00 | 155.2 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 6.31 | 17.24 | 28.72 | 0.00 | 106.6 | 0.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.1 | 6.51 | 15.25 | 23.95 | 6.00 | 126.2 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 5.43 | 14.74 | 24.17 | 3.00 | 109.3 | 85.0 |

## GW3

- Train rows: 162672
- Bank: 0.10 -> 1.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Chris Wood
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 59.92
- Actual score: 43.00
- Transfer: Cole Palmer -> Bruno Borges Fernandes (projected gain 6.36, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 2.92 | 8.87 | 14.83 | 2.00 | 80.0 | 90.0 |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.5 | 1.70 | 4.45 | 7.58 | 0.00 | 44.7 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 4.88 | 13.27 | 20.72 | 6.00 | 86.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.03 | 10.35 | 17.13 | 8.00 | 70.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 3.42 | 9.66 | 15.93 | 1.00 | 71.3 | 4.0 |
| Bench 2 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 2.88 | 9.46 | 15.58 | 2.00 | 70.0 | 90.0 |
| Bench 3 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 2.20 | 6.64 | 11.58 | 0.00 | 19.4 | 0.0 |
| Vice Captain | XI | Chris Wood | FWD | 16 | 7.6 | 6.06 | 15.89 | 24.52 | 2.00 | 92.9 | 72.0 |
| XI | XI | Junior Kroupi | FWD | 4 | 4.5 | 3.04 | 6.27 | 10.10 | 2.00 | 49.4 | 18.0 |
| Bench 4 | Bench | Lukas Nmecha | FWD | 11 | 5.0 | 2.20 | 6.18 | 10.27 | 2.00 | 41.5 | 69.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.33 | 22.41 | 37.28 | 3.00 | 102.8 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 5.67 | 15.88 | 24.38 | 2.00 | 93.9 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.91 | 15.65 | 25.54 | 10.00 | 87.4 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 5.47 | 15.30 | 24.06 | 2.00 | 95.1 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.86 | 12.19 | 18.84 | 2.00 | 72.7 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 1.50 -> 1.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Antoine Semenyo
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 68.50
- Actual score: 71.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.76) beats the best remaining Bench Boost opportunity (10.44).
- Transfer: Chris Wood -> João Pedro Junqueira de Jesus (projected gain 9.95, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.76) beats the best remaining Bench Boost opportunity (10.44).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 4.00 | 12.42 | 17.87 | 6.00 | 94.6 | 90.0 |
| Bench 1 | Bench Boost | Marco Bizot | GK | 2 | 4.5 | 2.26 | 7.50 | 9.92 | 0.00 | 70.9 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.05 | 13.67 | 19.61 | 8.00 | 88.7 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 3.79 | 12.89 | 18.46 | 1.00 | 70.2 | 45.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.04 | 12.69 | 18.19 | 9.00 | 86.1 | 90.0 |
| Bench 3 | Bench Boost | William Saliba | DEF | 1 | 6.0 | 2.10 | 7.80 | 11.60 | 0.00 | 33.1 | 0.0 |
| Bench 4 | Bench Boost | Daniel Ballard | DEF | 17 | 4.6 | 1.51 | 5.69 | 7.99 | 0.00 | 18.3 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.85 | 18.15 | 26.16 | 7.00 | 86.1 | 78.0 |
| XI | XI | Junior Kroupi | FWD | 4 | 4.5 | 3.47 | 8.74 | 11.25 | 0.00 | 55.4 | 0.0 |
| Bench 2 | Bench Boost | Lukas Nmecha | FWD | 11 | 5.0 | 2.41 | 8.32 | 11.32 | 1.00 | 50.9 | 21.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.84 | 24.01 | 36.94 | 9.00 | 105.0 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.2 | 6.14 | 18.19 | 25.32 | 13.00 | 89.9 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.73 | 15.10 | 23.13 | 2.00 | 69.5 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 3.80 | 13.17 | 18.98 | 3.00 | 66.7 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.67 | 12.34 | 17.86 | 3.00 | 74.3 | 90.0 |

## GW5

- Train rows: 164124
- Bank: 1.40 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Antoine Semenyo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 65.58
- Actual score: 57.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.83) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Daniel Ballard -> Pedro Porro Sauceda (projected gain 7.47, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.83) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 3.41 | 10.92 | 16.52 | 2.00 | 81.5 | 90.0 |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.5 | 0.95 | 3.59 | 5.04 | 0.00 | 33.1 | 0.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.6 | 4.25 | 12.30 | 18.93 | 1.00 | 82.6 | 88.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.55 | 12.23 | 18.63 | 4.00 | 80.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.08 | 11.78 | 17.92 | 2.00 | 80.1 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.1 | 2.96 | 9.82 | 16.06 | 0.00 | 54.7 | 63.0 |
| Bench 4 | Bench | William Saliba | DEF | 1 | 6.0 | 1.59 | 5.64 | 9.25 | 2.00 | 23.3 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.32 | 16.10 | 25.50 | 2.00 | 79.9 | 90.0 |
| Bench 3 | Bench | Lukas Nmecha | FWD | 11 | 5.0 | 1.92 | 6.14 | 9.60 | 1.00 | 36.1 | 1.0 |
| Bench 2 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 2.70 | 5.67 | 7.49 | 0.00 | 42.8 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.46 | 22.48 | 36.12 | 5.00 | 100.9 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.3 | 6.45 | 17.95 | 27.09 | 5.00 | 88.6 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.07 | 14.16 | 22.45 | 10.00 | 74.4 | 86.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 3.84 | 11.94 | 19.28 | 7.00 | 72.7 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.28 | 10.56 | 17.21 | 9.00 | 73.8 | 90.0 |