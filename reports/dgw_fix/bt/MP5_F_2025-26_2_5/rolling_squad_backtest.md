# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 263.31
- Total actual points: 222.00
- Average predicted points: 65.83
- Average actual points: 55.50
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
- Predicted score: 73.55
- Actual score: 45.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Mohammed Kudus replaced Cole Palmer.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 4.26 | 10.60 | 17.27 | 1.00 | 89.2 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 4.0 | 0.51 | 0.63 | 1.07 | 0.00 | 12.0 | 0.0 |
| Vice Captain | XI | Daniel Ballard | DEF | 17 | 4.6 | 7.36 | 17.51 | 27.85 | 1.00 | 90.0 | 8.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.68 | 12.23 | 19.72 | 6.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 12 | 6.0 | 4.19 | 12.04 | 19.72 | 3.00 | 90.0 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 4.26 | 10.40 | 16.70 | 3.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Matty Cash | DEF | 2 | 4.5 | 3.68 | 9.57 | 15.41 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 5.83 | 17.93 | 29.76 | 9.00 | 90.0 | 79.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 9.0 | 5.29 | 14.14 | 23.41 | 2.00 | 90.0 | 90.0 |
| XI | XI | Junior Kroupi | FWD | 4 | 4.5 | 5.30 | 12.53 | 20.31 | 2.00 | 52.3 | 4.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.68 | 23.21 | 39.04 | 5.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 7.26 | 20.05 | 31.77 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 6.71 | 18.17 | 30.19 | 0.00 | 90.0 | 0.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.1 | 7.26 | 15.96 | 25.08 | 6.00 | 90.0 | 90.0 |
| Bench 2 | Autosub In | Mohammed Kudus | MID | 18 | 6.5 | 4.85 | 14.77 | 24.34 | 3.00 | 90.0 | 85.0 |

## GW3

- Train rows: 162672
- Bank: 0.10 -> 1.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bruno Borges Fernandes
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.04
- Actual score: 43.00
- Transfer: Cole Palmer -> Bruno Borges Fernandes (projected gain 8.92, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 2.80 | 7.91 | 12.97 | 8.00 | 78.8 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 4.0 | 0.28 | 0.50 | 0.88 | 0.00 | 6.2 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.07 | 10.84 | 17.88 | 8.00 | 76.4 | 90.0 |
| Bench 3 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 3.10 | 9.87 | 16.23 | 2.00 | 73.2 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 3.23 | 8.45 | 13.73 | 1.00 | 72.8 | 90.0 |
| XI | XI | Matty Cash | DEF | 2 | 4.5 | 3.16 | 8.25 | 13.35 | 0.00 | 76.2 | 73.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 2.38 | 6.70 | 11.43 | 0.00 | 21.0 | 0.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 4.51 | 15.17 | 24.92 | 2.00 | 75.9 | 78.0 |
| Bench 2 | Bench | Ollie Watkins | FWD | 2 | 8.9 | 3.62 | 11.48 | 19.51 | 2.00 | 66.6 | 90.0 |
| XI | XI | Junior Kroupi | FWD | 4 | 4.5 | 3.71 | 10.84 | 18.28 | 2.00 | 46.9 | 18.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.04 | 22.68 | 38.01 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.80 | 15.34 | 25.14 | 10.00 | 84.4 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 5.29 | 14.94 | 23.65 | 2.00 | 89.8 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 4.67 | 14.75 | 23.00 | 2.00 | 86.2 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.74 | 11.62 | 18.08 | 2.00 | 70.0 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 1.50 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Antoine Semenyo
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 70.36
- Actual score: 86.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.03) beats the best remaining Bench Boost opportunity (11.24).
- Transfer: Daniel Ballard -> Daniel Muñoz Mejía (projected gain 11.78, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.03) beats the best remaining Bench Boost opportunity (11.24).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 2.81 | 9.44 | 14.53 | 10.00 | 86.6 | 90.0 |
| Bench 1 | Bench Boost | Tom King | GK | 9 | 4.0 | 0.21 | 1.15 | 0.76 | 0.00 | 4.3 | 0.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.6 | 4.91 | 13.40 | 20.20 | 5.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.13 | 13.33 | 20.23 | 8.00 | 89.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 3.99 | 11.97 | 18.27 | 9.00 | 84.0 | 90.0 |
| Bench 4 | Bench Boost | Reinildo Mandava | DEF | 17 | 4.0 | 2.81 | 8.20 | 12.34 | 6.00 | 73.2 | 90.0 |
| Bench 3 | Bench Boost | Matty Cash | DEF | 2 | 4.5 | 2.81 | 8.16 | 12.36 | 5.00 | 71.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 5.21 | 15.30 | 23.47 | 2.00 | 69.7 | 71.0 |
| XI | XI | Junior Kroupi | FWD | 4 | 4.5 | 4.30 | 13.98 | 20.66 | 0.00 | 58.0 | 0.0 |
| Bench 2 | Bench Boost | Ollie Watkins | FWD | 2 | 8.9 | 3.71 | 11.62 | 18.68 | 2.00 | 67.9 | 82.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 8.09 | 23.93 | 38.04 | 9.00 | 90.0 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.2 | 5.64 | 16.34 | 23.85 | 13.00 | 82.8 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.82 | 14.14 | 22.70 | 2.00 | 71.6 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.08 | 12.44 | 18.85 | 3.00 | 68.4 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.76 | 11.61 | 17.83 | 3.00 | 75.6 | 90.0 |

## GW5

- Train rows: 164124
- Bank: 0.50 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Antoine Semenyo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 64.36
- Actual score: 48.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.71) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Matty Cash -> Micky van de Ven (projected gain 3.33, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.71) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 3.15 | 9.62 | 15.43 | 2.00 | 88.6 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 4.0 | 0.00 | 0.56 | 0.73 | 0.00 | 5.6 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.44 | 12.06 | 18.59 | 4.00 | 80.8 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.6 | 4.42 | 11.88 | 18.06 | 2.00 | 75.1 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.17 | 11.86 | 19.04 | 1.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.09 | 11.63 | 18.21 | 2.00 | 80.8 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 3.32 | 8.76 | 13.50 | -2.00 | 80.0 | 32.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 3.93 | 11.58 | 19.03 | 2.00 | 73.3 | 90.0 |
| Bench 3 | Bench | Hugo Ekitiké | FWD | 12 | 8.7 | 3.25 | 10.99 | 18.42 | 8.00 | 45.2 | 66.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 2.66 | 8.38 | 13.24 | 0.00 | 30.8 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.34 | 22.26 | 36.53 | 5.00 | 90.0 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.3 | 5.83 | 16.74 | 25.70 | 5.00 | 82.8 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.08 | 14.04 | 22.38 | 10.00 | 77.0 | 86.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 3.91 | 11.64 | 19.11 | 7.00 | 73.5 | 90.0 |
| Bench 2 | Bench | Tijjani Reijnders | MID | 13 | 5.6 | 3.26 | 10.25 | 17.01 | 9.00 | 76.6 | 90.0 |