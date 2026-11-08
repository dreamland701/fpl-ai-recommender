# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 263.49
- Total actual points: 225.00
- Average predicted points: 65.87
- Average actual points: 56.25
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
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 4.26 | 10.60 | 17.27 | 1.00 | 89.2 | 90.0 |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.5 | 4.14 | 10.43 | 17.04 | 0.00 | 90.0 | 0.0 |
| Vice Captain | XI | Daniel Ballard | DEF | 17 | 4.6 | 7.36 | 17.51 | 27.85 | 1.00 | 90.0 | 8.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.68 | 12.23 | 19.72 | 6.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 12 | 6.0 | 4.19 | 12.04 | 19.72 | 3.00 | 90.0 | 90.0 |
| Bench 2 | Autosub In | William Saliba | DEF | 1 | 6.0 | 4.53 | 11.98 | 19.35 | 6.00 | 90.0 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 4.79 | 11.88 | 19.13 | 5.00 | 90.0 | 68.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 5.83 | 17.93 | 29.76 | 9.00 | 90.0 | 79.0 |
| XI | XI | Junior Kroupi | FWD | 4 | 4.5 | 5.30 | 12.53 | 20.31 | 2.00 | 52.3 | 4.0 |
| Bench 4 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.92 | 7.28 | 11.85 | 2.00 | 70.5 | 85.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.68 | 23.21 | 39.04 | 5.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 7.26 | 20.05 | 31.77 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 6.71 | 18.17 | 30.19 | 0.00 | 90.0 | 0.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.1 | 7.26 | 15.96 | 25.08 | 6.00 | 90.0 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.85 | 14.77 | 24.34 | 3.00 | 90.0 | 85.0 |

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
- Transfer: Cole Palmer -> Bruno Borges Fernandes (projected gain 5.66, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 2.80 | 7.91 | 12.97 | 8.00 | 78.8 | 90.0 |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.5 | 1.31 | 3.96 | 6.91 | 0.00 | 36.0 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 4.45 | 12.74 | 20.15 | 6.00 | 78.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.07 | 10.84 | 17.88 | 8.00 | 76.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 3.64 | 10.14 | 16.67 | 1.00 | 74.4 | 4.0 |
| Bench 2 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 3.10 | 9.87 | 16.23 | 2.00 | 73.2 | 90.0 |
| Bench 3 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 2.38 | 6.70 | 11.43 | 0.00 | 21.0 | 0.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 4.51 | 15.17 | 24.92 | 2.00 | 75.9 | 78.0 |
| XI | XI | Junior Kroupi | FWD | 4 | 4.5 | 3.71 | 10.84 | 18.28 | 2.00 | 46.9 | 18.0 |
| Bench 4 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.33 | 7.11 | 11.65 | 6.00 | 64.6 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.04 | 22.68 | 38.01 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.80 | 15.34 | 25.14 | 10.00 | 84.4 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 5.29 | 14.94 | 23.65 | 2.00 | 89.8 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 4.67 | 14.75 | 23.00 | 2.00 | 86.2 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.74 | 11.62 | 18.08 | 2.00 | 70.0 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 1.50 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Jack Grealish
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 70.77
- Actual score: 70.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.12) beats the best remaining Bench Boost opportunity (10.77).
- Transfer: Tijjani Reijnders -> Jack Grealish (projected gain 5.20, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.12) beats the best remaining Bench Boost opportunity (10.77).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 2.81 | 9.44 | 14.53 | 10.00 | 86.6 | 90.0 |
| Bench 1 | Bench Boost | Marco Bizot | GK | 2 | 4.5 | 2.13 | 6.69 | 9.76 | 0.00 | 67.3 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.13 | 13.33 | 20.23 | 8.00 | 89.7 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 3.85 | 12.00 | 18.24 | 1.00 | 70.0 | 45.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 3.99 | 11.97 | 18.27 | 9.00 | 84.0 | 90.0 |
| Bench 3 | Bench Boost | William Saliba | DEF | 1 | 6.0 | 2.29 | 7.39 | 11.92 | 0.00 | 34.7 | 0.0 |
| Bench 4 | Bench Boost | Daniel Ballard | DEF | 17 | 4.6 | 1.29 | 4.74 | 7.53 | 0.00 | 17.9 | 0.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 5.21 | 15.30 | 23.47 | 2.00 | 69.7 | 71.0 |
| XI | XI | Junior Kroupi | FWD | 4 | 4.5 | 4.30 | 13.98 | 20.66 | 0.00 | 58.0 | 0.0 |
| Bench 2 | Bench Boost | Lyle Foster | FWD | 3 | 5.0 | 2.92 | 8.73 | 13.11 | 2.00 | 73.1 | 85.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 8.09 | 23.93 | 38.04 | 9.00 | 90.0 | 90.0 |
| Vice Captain | XI | Jack Grealish | MID | 9 | 6.8 | 6.13 | 16.81 | 24.54 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 5.64 | 16.34 | 23.85 | 13.00 | 82.8 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.82 | 14.14 | 22.70 | 2.00 | 71.6 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.08 | 12.44 | 18.85 | 3.00 | 68.4 | 90.0 |

## GW5

- Train rows: 164124
- Bank: 0.30 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Antoine Semenyo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 62.34
- Actual score: 55.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.71) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: William Saliba -> Pedro Porro Sauceda (projected gain 3.77, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.71) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 3.15 | 9.62 | 15.43 | 2.00 | 88.6 | 90.0 |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.5 | 0.83 | 3.12 | 5.02 | 0.00 | 29.6 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.44 | 12.06 | 18.59 | 4.00 | 80.8 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.6 | 4.28 | 11.96 | 18.83 | 1.00 | 82.1 | 88.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.09 | 11.63 | 18.21 | 2.00 | 80.8 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.1 | 3.20 | 9.96 | 16.46 | 0.00 | 57.5 | 63.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 1.28 | 3.91 | 6.12 | 1.00 | 14.5 | 53.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 3.25 | 10.99 | 18.42 | 8.00 | 45.2 | 66.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 2.66 | 8.38 | 13.24 | 0.00 | 30.8 | 0.0 |
| Bench 2 | Bench | Lyle Foster | FWD | 3 | 5.0 | 3.04 | 8.29 | 13.33 | 6.00 | 73.3 | 85.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.34 | 22.26 | 36.53 | 5.00 | 90.0 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.3 | 5.83 | 16.74 | 25.70 | 5.00 | 82.8 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.08 | 14.04 | 22.38 | 10.00 | 77.0 | 86.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 3.91 | 11.64 | 19.11 | 7.00 | 73.5 | 90.0 |
| XI | XI | Jack Grealish | MID | 9 | 6.8 | 3.11 | 9.92 | 15.04 | 1.00 | 43.9 | 90.0 |