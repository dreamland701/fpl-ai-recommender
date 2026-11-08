# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 265.00
- Total actual points: 244.00
- Average predicted points: 66.25
- Average actual points: 61.00
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
- Captain: Mohamed Salah
- Vice captain: Daniel Ballard
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 73.64
- Actual score: 51.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: William Saliba replaced Cole Palmer.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.5 | 4.14 | 10.49 | 16.97 | 0.00 | 90.0 | 0.0 |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 4.26 | 10.48 | 17.06 | 1.00 | 89.2 | 90.0 |
| Vice Captain | XI | Daniel Ballard | DEF | 17 | 4.6 | 7.36 | 17.21 | 27.28 | 1.00 | 90.0 | 8.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.68 | 12.38 | 19.76 | 6.00 | 90.0 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 4.79 | 12.13 | 19.26 | 5.00 | 90.0 | 68.0 |
| Bench 2 | Autosub In | William Saliba | DEF | 1 | 6.0 | 4.53 | 12.12 | 19.41 | 6.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 12 | 6.0 | 4.19 | 11.72 | 19.24 | 3.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 5.83 | 18.49 | 30.51 | 9.00 | 90.0 | 79.0 |
| Bench 4 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.92 | 7.39 | 12.02 | 2.00 | 70.5 | 85.0 |
| XI | XI | Junior Kroupi | FWD | 4 | 4.5 | 5.30 | 7.38 | 11.14 | 2.00 | 52.3 | 4.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.68 | 22.59 | 37.98 | 5.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 7.26 | 20.67 | 32.32 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 6.71 | 17.32 | 28.70 | 0.00 | 90.0 | 0.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.1 | 7.26 | 16.65 | 25.84 | 6.00 | 90.0 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.85 | 14.94 | 24.53 | 3.00 | 90.0 | 85.0 |

## GW3

- Train rows: 162672
- Bank: 0.10 -> 1.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bruno Borges Fernandes
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 56.74
- Actual score: 49.00
- Transfer: Cole Palmer -> Bruno Borges Fernandes (projected gain 5.81, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 2.80 | 7.90 | 13.00 | 8.00 | 78.8 | 90.0 |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.5 | 1.31 | 4.04 | 7.00 | 0.00 | 36.0 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 4.45 | 13.34 | 20.85 | 6.00 | 78.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.07 | 10.63 | 17.61 | 8.00 | 76.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 3.64 | 10.21 | 16.71 | 1.00 | 74.4 | 4.0 |
| Bench 2 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 3.10 | 9.99 | 16.34 | 2.00 | 73.2 | 90.0 |
| Bench 3 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 2.38 | 6.84 | 11.85 | 0.00 | 21.0 | 0.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 4.51 | 15.79 | 25.89 | 2.00 | 75.9 | 78.0 |
| Bench 4 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.33 | 7.26 | 11.86 | 6.00 | 64.6 | 90.0 |
| XI | XI | Junior Kroupi | FWD | 4 | 4.5 | 3.71 | 6.52 | 10.50 | 2.00 | 46.9 | 18.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.04 | 22.35 | 37.38 | 3.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 4.67 | 15.85 | 24.47 | 2.00 | 86.2 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.80 | 15.62 | 25.49 | 10.00 | 84.4 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 5.29 | 15.54 | 24.38 | 2.00 | 89.8 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.74 | 12.27 | 18.96 | 2.00 | 70.0 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 1.50 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Antoine Semenyo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 68.93
- Actual score: 76.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.46) beats the best remaining Triple Captain opportunity (10.30).
- Transfer: Marco Bizot -> David Raya Martín (projected gain 2.48, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.46) beats the best remaining Triple Captain opportunity (10.30).
- Autosub: Lyle Foster replaced Junior Kroupi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 3.89 | 12.00 | 18.11 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Robin Roefs | GK | 17 | 4.5 | 2.81 | 9.56 | 14.59 | 10.00 | 86.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.13 | 13.48 | 20.19 | 8.00 | 89.7 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 3.85 | 12.48 | 18.72 | 1.00 | 70.0 | 45.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 3.99 | 12.22 | 18.38 | 9.00 | 84.0 | 90.0 |
| Bench 3 | Bench | William Saliba | DEF | 1 | 6.0 | 2.29 | 7.36 | 11.81 | 0.00 | 34.7 | 0.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 1.29 | 4.97 | 7.89 | 0.00 | 17.9 | 0.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 5.21 | 15.91 | 24.20 | 2.00 | 69.7 | 71.0 |
| Bench 2 | Autosub In | Lyle Foster | FWD | 3 | 5.0 | 2.92 | 8.99 | 13.35 | 2.00 | 73.1 | 85.0 |
| XI | Bench | Junior Kroupi | FWD | 4 | 4.5 | 4.30 | 8.31 | 11.51 | 0.00 | 58.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 8.09 | 23.79 | 37.44 | 9.00 | 90.0 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.2 | 5.64 | 17.71 | 25.52 | 13.00 | 82.8 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.82 | 14.63 | 23.32 | 2.00 | 71.6 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.08 | 12.90 | 19.41 | 3.00 | 68.4 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.76 | 11.88 | 18.07 | 3.00 | 75.6 | 90.0 |

## GW5

- Train rows: 164124
- Bank: 0.50 -> 0.90
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Antoine Semenyo
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 65.69
- Actual score: 68.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.62) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: William Saliba -> Daniel Muñoz Mejía (projected gain 4.08, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.62) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 3.40 | 10.77 | 16.91 | 2.00 | 81.4 | 90.0 |
| Bench 1 | Bench Boost | Robin Roefs | GK | 17 | 4.5 | 3.15 | 9.60 | 15.40 | 2.00 | 88.6 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.6 | 4.42 | 12.41 | 18.72 | 2.00 | 75.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.44 | 12.17 | 18.76 | 4.00 | 80.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.09 | 11.78 | 18.28 | 2.00 | 80.8 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.1 | 3.20 | 10.00 | 16.50 | 0.00 | 57.5 | 63.0 |
| Bench 4 | Bench Boost | Daniel Ballard | DEF | 17 | 4.6 | 1.28 | 4.04 | 6.37 | 1.00 | 14.5 | 53.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 3.25 | 11.30 | 18.96 | 8.00 | 45.2 | 66.0 |
| Bench 2 | Bench Boost | Lyle Foster | FWD | 3 | 5.0 | 3.04 | 8.44 | 13.50 | 6.00 | 73.3 | 85.0 |
| Bench 3 | Bench Boost | Junior Kroupi | FWD | 4 | 4.5 | 2.66 | 5.41 | 7.69 | 0.00 | 30.8 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.34 | 22.10 | 36.06 | 5.00 | 90.0 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.3 | 5.83 | 17.90 | 27.28 | 5.00 | 82.8 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.08 | 14.28 | 22.82 | 10.00 | 77.0 | 86.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 3.91 | 11.86 | 19.44 | 7.00 | 73.5 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.26 | 10.54 | 17.52 | 9.00 | 76.6 | 90.0 |