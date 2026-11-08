# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 248.42
- Total actual points: 229.00
- Average predicted points: 62.10
- Average actual points: 57.25
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
- Vice captain: Antoine Semenyo
- Effective captain: Tijjani Reijnders
- Chip used: none
- Predicted score: 70.50
- Actual score: 49.00
- Chip advisory: bench_boost (0.62): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Virgil van Dijk replaced Cole Palmer.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.5 | 3.82 | 9.80 | 15.89 | 0.00 | 93.3 | 0.0 |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 3.92 | 9.79 | 15.97 | 1.00 | 85.9 | 90.0 |
| XI | XI | Daniel Ballard | DEF | 17 | 4.6 | 6.89 | 16.19 | 25.69 | 1.00 | 100.2 | 8.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.55 | 11.61 | 18.55 | 6.00 | 112.4 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 4.60 | 11.37 | 18.08 | 5.00 | 97.3 | 68.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 4.42 | 11.29 | 18.10 | 6.00 | 115.3 | 90.0 |
| Bench 2 | Autosub In | Virgil van Dijk | DEF | 12 | 6.0 | 3.96 | 11.01 | 18.12 | 3.00 | 102.2 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 5.92 | 17.58 | 29.05 | 9.00 | 105.4 | 79.0 |
| Bench 4 | Bench | Lukas Nmecha | FWD | 11 | 5.0 | 2.85 | 9.98 | 16.92 | 1.00 | 39.4 | 32.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 3.90 | 7.38 | 11.14 | 2.00 | 50.8 | 4.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.5 | 7.11 | 21.48 | 36.22 | 5.00 | 116.6 | 90.0 |
| Captain | Captain | Tijjani Reijnders | MID | 13 | 5.6 | 7.55 | 19.63 | 30.67 | 2.00 | 153.8 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 5.98 | 16.38 | 27.24 | 0.00 | 95.4 | 0.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.1 | 7.34 | 15.65 | 24.29 | 6.00 | 130.0 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.66 | 13.85 | 22.77 | 3.00 | 105.6 | 85.0 |

## GW3

- Train rows: 162672
- Bank: 0.10 -> 1.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bruno Borges Fernandes
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 53.53
- Actual score: 49.00
- Transfer: Cole Palmer -> Bruno Borges Fernandes (projected gain 7.02, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 2.43 | 6.90 | 11.40 | 8.00 | 78.1 | 90.0 |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.5 | 1.85 | 5.58 | 9.51 | 0.00 | 36.1 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 4.58 | 12.78 | 19.97 | 6.00 | 84.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.01 | 10.50 | 17.40 | 8.00 | 76.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 3.36 | 9.35 | 15.35 | 1.00 | 73.9 | 4.0 |
| Bench 2 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 2.95 | 9.18 | 15.56 | 0.00 | 17.4 | 0.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 2.69 | 8.78 | 14.43 | 2.00 | 72.3 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 4.51 | 14.95 | 24.51 | 2.00 | 80.2 | 78.0 |
| Bench 3 | Bench | Lukas Nmecha | FWD | 11 | 5.0 | 2.71 | 7.93 | 13.00 | 2.00 | 38.7 | 69.0 |
| XI | XI | Junior Kroupi | FWD | 4 | 4.5 | 2.97 | 6.52 | 10.50 | 2.00 | 48.3 | 18.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 6.25 | 20.10 | 33.76 | 3.00 | 106.5 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.78 | 15.29 | 24.98 | 10.00 | 85.7 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 4.79 | 14.64 | 22.53 | 2.00 | 94.4 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 5.18 | 14.27 | 22.38 | 2.00 | 95.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.41 | 11.01 | 16.98 | 2.00 | 69.9 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 1.50 -> 1.90
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Antoine Semenyo
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 65.92
- Actual score: 75.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.92) beats the best remaining Bench Boost opportunity (11.38).
- Transfer: William Saliba -> Daniel Muñoz Mejía (projected gain 2.45, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.92) beats the best remaining Bench Boost opportunity (11.38).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 2.32 | 8.17 | 12.39 | 10.00 | 86.0 | 90.0 |
| Bench 1 | Bench Boost | Marco Bizot | GK | 2 | 4.5 | 2.04 | 6.68 | 9.56 | 0.00 | 66.8 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.96 | 12.60 | 18.81 | 8.00 | 91.9 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.6 | 4.62 | 12.52 | 18.52 | 5.00 | 97.3 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 3.48 | 11.29 | 16.85 | 1.00 | 69.9 | 45.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 3.68 | 11.17 | 16.74 | 9.00 | 85.2 | 90.0 |
| Bench 4 | Bench Boost | Daniel Ballard | DEF | 17 | 4.6 | 1.72 | 6.49 | 10.44 | 0.00 | 17.2 | 0.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 5.24 | 15.60 | 23.70 | 2.00 | 71.7 | 71.0 |
| Bench 3 | Bench Boost | Lukas Nmecha | FWD | 11 | 5.0 | 2.59 | 8.46 | 12.46 | 1.00 | 48.1 | 21.0 |
| XI | XI | Junior Kroupi | FWD | 4 | 4.5 | 3.42 | 8.31 | 11.51 | 0.00 | 54.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.36 | 21.78 | 34.24 | 9.00 | 104.4 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.2 | 5.92 | 17.07 | 24.50 | 13.00 | 90.1 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.55 | 13.90 | 22.14 | 2.00 | 70.2 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 3.57 | 11.55 | 17.28 | 3.00 | 66.8 | 90.0 |
| Bench 2 | Bench Boost | Tijjani Reijnders | MID | 13 | 5.6 | 3.09 | 10.22 | 15.45 | 3.00 | 73.5 | 90.0 |

## GW5

- Train rows: 164124
- Bank: 1.90 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Antoine Semenyo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 58.47
- Actual score: 56.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.93) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Tijjani Reijnders -> Xavi Simons (projected gain 2.90, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (6.93) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 2.63 | 8.31 | 13.36 | 2.00 | 86.8 | 90.0 |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.5 | 0.82 | 3.12 | 4.96 | 0.00 | 29.1 | 0.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.6 | 3.99 | 11.22 | 16.88 | 2.00 | 73.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.13 | 11.09 | 17.04 | 4.00 | 82.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 3.72 | 10.68 | 16.54 | 2.00 | 81.0 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.1 | 3.02 | 9.78 | 16.14 | 0.00 | 55.6 | 63.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 1.22 | 4.04 | 6.37 | 1.00 | 13.6 | 53.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 3.27 | 11.96 | 20.05 | 8.00 | 42.1 | 66.0 |
| Bench 3 | Bench | Lukas Nmecha | FWD | 11 | 5.0 | 2.46 | 7.27 | 11.88 | 1.00 | 35.8 | 1.0 |
| Bench 2 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 2.65 | 5.41 | 7.69 | 0.00 | 41.6 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 6.55 | 20.01 | 32.73 | 5.00 | 99.8 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.3 | 5.87 | 16.76 | 25.47 | 5.00 | 88.9 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.72 | 13.45 | 21.45 | 10.00 | 75.7 | 86.0 |
| XI | XI | Xavi Simons | MID | 18 | 7.0 | 4.01 | 12.20 | 19.69 | 1.00 | 72.7 | 29.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 3.45 | 10.63 | 17.44 | 7.00 | 72.1 | 90.0 |