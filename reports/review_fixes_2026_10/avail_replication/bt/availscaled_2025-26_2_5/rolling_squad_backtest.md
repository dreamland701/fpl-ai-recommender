# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 268.51
- Total actual points: 220.00
- Average predicted points: 67.13
- Average actual points: 55.00
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
- Predicted score: 73.40
- Actual score: 41.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Eliezer Mayenda Dossou replaced Cole Palmer.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.5 | 4.06 | 10.49 | 16.97 | 0.00 | 92.3 | 0.0 |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 4.17 | 10.48 | 17.06 | 1.00 | 84.9 | 90.0 |
| XI | XI | Daniel Ballard | DEF | 17 | 4.6 | 7.26 | 17.21 | 27.28 | 1.00 | 99.2 | 8.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.83 | 12.38 | 19.76 | 6.00 | 111.4 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 4.88 | 12.13 | 19.26 | 5.00 | 96.3 | 68.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 4.72 | 12.12 | 19.41 | 6.00 | 114.3 | 90.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 12 | 6.0 | 4.20 | 11.72 | 19.24 | 3.00 | 101.2 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.6 | 5.15 | 14.57 | 23.70 | 2.00 | 88.7 | 87.0 |
| Bench 2 | Autosub In | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 4.35 | 10.70 | 17.44 | 2.00 | 70.0 | 62.0 |
| Bench 4 | Bench | Lukas Nmecha | FWD | 11 | 5.0 | 2.80 | 10.17 | 17.52 | 1.00 | 21.4 | 32.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.5 | 7.50 | 22.59 | 37.98 | 5.00 | 115.6 | 90.0 |
| Captain | Captain | Tijjani Reijnders | MID | 13 | 5.6 | 7.92 | 20.67 | 32.32 | 2.00 | 152.8 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 6.33 | 17.32 | 28.70 | 0.00 | 94.4 | 0.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.1 | 7.70 | 16.65 | 25.84 | 6.00 | 118.0 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 5.03 | 14.94 | 24.53 | 3.00 | 93.6 | 85.0 |

## GW3

- Train rows: 162672
- Bank: 0.10 -> 1.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Chris Wood
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 61.23
- Actual score: 49.00
- Transfer: Cole Palmer -> Bruno Borges Fernandes (projected gain 7.36, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 2.84 | 8.09 | 13.29 | 8.00 | 80.1 | 90.0 |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.5 | 1.85 | 5.66 | 9.81 | 0.00 | 53.1 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 5.06 | 14.16 | 22.13 | 6.00 | 90.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.48 | 11.76 | 19.48 | 8.00 | 84.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 3.84 | 10.83 | 17.73 | 1.00 | 78.9 | 4.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 3.17 | 10.36 | 16.95 | 2.00 | 75.3 | 90.0 |
| Bench 2 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 3.12 | 9.58 | 16.59 | 0.00 | 3.4 | 0.0 |
| Vice Captain | XI | Chris Wood | FWD | 16 | 7.6 | 6.92 | 16.82 | 25.71 | 2.00 | 91.9 | 72.0 |
| Bench 3 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 3.10 | 9.46 | 15.74 | 2.00 | 58.6 | 64.0 |
| Bench 4 | Bench | Lukas Nmecha | FWD | 11 | 5.0 | 3.00 | 8.84 | 14.65 | 2.00 | 54.7 | 69.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 6.97 | 22.35 | 37.38 | 3.00 | 106.5 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 6.18 | 16.40 | 26.77 | 10.00 | 92.7 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 5.18 | 15.85 | 24.47 | 2.00 | 98.4 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 5.59 | 15.54 | 24.38 | 2.00 | 98.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 4.00 | 12.91 | 19.93 | 2.00 | 72.9 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 1.50 -> 1.90
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Antoine Semenyo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 67.85
- Actual score: 82.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.07) beats the best remaining Triple Captain opportunity (9.90).
- Transfer: William Saliba -> Daniel Muñoz Mejía (projected gain 4.46, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.07) beats the best remaining Triple Captain opportunity (9.90).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 2.81 | 9.56 | 14.59 | 10.00 | 86.0 | 90.0 |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.5 | 2.36 | 7.69 | 11.05 | 0.00 | 74.8 | 0.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.6 | 5.14 | 13.99 | 20.80 | 5.00 | 99.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.25 | 13.48 | 20.19 | 8.00 | 95.9 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 4.06 | 13.12 | 19.69 | 1.00 | 73.9 | 45.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.22 | 12.74 | 19.15 | 9.00 | 88.2 | 90.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 1.75 | 6.95 | 11.04 | 0.00 | 7.2 | 0.0 |
| Bench 3 | Bench | Chris Wood | FWD | 16 | 7.6 | 1.93 | 11.78 | 18.87 | 1.00 | 35.1 | 59.0 |
| XI | XI | Lukas Nmecha | FWD | 11 | 5.0 | 2.97 | 9.86 | 14.45 | 1.00 | 62.1 | 21.0 |
| Bench 2 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.73 | 9.65 | 14.75 | 0.00 | 62.5 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 8.04 | 23.79 | 37.44 | 9.00 | 106.4 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.2 | 6.13 | 17.71 | 25.52 | 13.00 | 97.1 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.20 | 15.95 | 25.42 | 2.00 | 76.2 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.24 | 13.60 | 20.45 | 3.00 | 70.8 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.70 | 12.03 | 18.29 | 3.00 | 74.5 | 90.0 |

## GW5

- Train rows: 164124
- Bank: 1.90 -> 0.80
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Antoine Semenyo
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 66.02
- Actual score: 48.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.33) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Tijjani Reijnders -> Enzo Fernández (projected gain 3.22, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.33) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 3.09 | 9.60 | 15.40 | 2.00 | 86.8 | 90.0 |
| Bench 1 | Bench Boost | Marco Bizot | GK | 2 | 4.5 | 0.82 | 3.12 | 4.96 | 0.00 | 29.1 | 0.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.6 | 4.63 | 13.02 | 19.64 | 2.00 | 76.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.68 | 12.70 | 19.58 | 4.00 | 86.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.27 | 12.30 | 19.10 | 2.00 | 84.0 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.1 | 3.54 | 11.46 | 18.91 | 0.00 | 63.6 | 63.0 |
| Bench 4 | Bench Boost | Daniel Ballard | DEF | 17 | 4.6 | 1.22 | 4.04 | 6.37 | 1.00 | 13.6 | 53.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.6 | 4.42 | 13.37 | 22.12 | 2.00 | 69.2 | 74.0 |
| Bench 2 | Bench Boost | Lukas Nmecha | FWD | 11 | 5.0 | 2.78 | 8.29 | 13.62 | 1.00 | 25.8 | 1.0 |
| Bench 3 | Bench Boost | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 1.46 | 4.89 | 8.01 | 1.00 | 26.4 | 10.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.26 | 22.10 | 36.06 | 5.00 | 101.8 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.3 | 6.33 | 18.13 | 27.63 | 5.00 | 93.9 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.36 | 15.30 | 24.44 | 10.00 | 80.7 | 86.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 4.82 | 14.15 | 21.64 | 1.00 | 74.2 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.06 | 12.46 | 20.41 | 7.00 | 76.1 | 90.0 |