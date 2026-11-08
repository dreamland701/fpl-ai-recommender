# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 279.99
- Total actual points: 224.00
- Average predicted points: 70.00
- Average actual points: 56.00
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
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Eliezer Mayenda Dossou replaced Cole Palmer.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.5 | 4.06 | 10.49 | 16.97 | 0.00 | 93.3 | 0.0 |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 4.17 | 10.48 | 17.06 | 1.00 | 85.9 | 90.0 |
| XI | XI | Daniel Ballard | DEF | 17 | 4.6 | 7.26 | 17.21 | 27.28 | 1.00 | 100.2 | 8.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.83 | 12.38 | 19.76 | 6.00 | 112.4 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 4.88 | 12.13 | 19.26 | 5.00 | 97.3 | 68.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 4.72 | 12.12 | 19.41 | 6.00 | 115.3 | 90.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 12 | 6.0 | 4.20 | 11.72 | 19.24 | 3.00 | 102.2 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.6 | 5.15 | 14.57 | 23.70 | 2.00 | 103.7 | 87.0 |
| Bench 2 | Autosub In | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 4.29 | 10.56 | 17.21 | 2.00 | 69.0 | 62.0 |
| Bench 4 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.93 | 7.39 | 12.02 | 2.00 | 71.0 | 85.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.5 | 7.50 | 22.59 | 37.98 | 5.00 | 116.6 | 90.0 |
| Captain | Captain | Tijjani Reijnders | MID | 13 | 5.6 | 7.92 | 20.67 | 32.32 | 2.00 | 153.8 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 6.33 | 17.32 | 28.70 | 0.00 | 95.4 | 0.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.1 | 7.70 | 16.65 | 25.84 | 6.00 | 130.0 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 5.03 | 14.94 | 24.53 | 3.00 | 105.6 | 85.0 |

## GW3

- Train rows: 162672
- Bank: 0.10 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Mohamed Salah
- Chip used: wildcard
- Predicted score: 63.44
- Actual score: 46.00
- Chip advisory: bench_boost (0.57): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Transfer: none
- Chip used: Wildcard — full rebuild projects +19.06 squad value (threshold 12).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.5 | 3.92 | 10.59 | 17.31 | 1.00 | 94.8 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 5.0 | 3.69 | 9.61 | 15.48 | 2.00 | 84.5 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.6 | 4.95 | 13.48 | 21.29 | 4.00 | 96.5 | 70.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.1 | 4.77 | 13.34 | 20.85 | 6.00 | 84.8 | 90.0 |
| Bench 2 | Bench | Daniel Muñoz Mejía | DEF | 8 | 5.5 | 3.43 | 10.87 | 17.74 | 9.00 | 87.1 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 5.6 | 3.76 | 10.77 | 17.33 | 2.00 | 62.1 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.6 | 3.86 | 10.64 | 16.78 | 1.00 | 85.9 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 6.97 | 18.67 | 29.42 | 9.00 | 115.5 | 90.0 |
| Bench 4 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.33 | 7.26 | 11.86 | 6.00 | 64.7 | 90.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 2.97 | 6.52 | 10.50 | 2.00 | 48.3 | 18.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 6.97 | 22.35 | 37.38 | 3.00 | 106.5 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.3 | 5.18 | 15.85 | 24.47 | 2.00 | 94.4 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.89 | 15.62 | 25.49 | 10.00 | 85.7 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.6 | 5.59 | 15.54 | 24.38 | 2.00 | 95.0 | 90.0 |
| XI | XI | Cody Gakpo | MID | 12 | 7.6 | 4.59 | 14.35 | 23.08 | 3.00 | 94.1 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Antoine Semenyo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 70.85
- Actual score: 81.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.42) beats the best remaining Triple Captain opportunity (10.25).
- Transfer: Jordan Pickford -> David Raya Martín (projected gain 2.05, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.42) beats the best remaining Triple Captain opportunity (10.25).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 3.97 | 12.00 | 18.11 | 6.00 | 92.1 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 5.0 | 1.97 | 7.91 | 12.32 | 1.00 | 77.0 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.5 | 5.14 | 13.99 | 20.80 | 5.00 | 97.3 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.1 | 3.86 | 12.48 | 18.72 | 1.00 | 69.9 | 45.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 5.6 | 3.77 | 11.55 | 16.98 | 8.00 | 60.9 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.6 | 3.82 | 11.26 | 16.86 | 6.00 | 66.0 | 90.0 |
| Bench 3 | Bench | Micky van de Ven | DEF | 18 | 4.6 | 3.23 | 10.12 | 14.90 | 14.00 | 74.7 | 79.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 5.94 | 17.76 | 26.46 | 7.00 | 85.8 | 78.0 |
| Bench 4 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.93 | 8.99 | 13.35 | 2.00 | 72.6 | 85.0 |
| Bench 2 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 3.42 | 8.31 | 11.51 | 0.00 | 54.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 8.04 | 23.79 | 37.44 | 9.00 | 104.4 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.3 | 6.13 | 17.71 | 25.52 | 13.00 | 90.1 | 90.0 |
| XI | XI | Cody Gakpo | MID | 12 | 7.6 | 5.31 | 15.38 | 22.73 | 3.00 | 84.2 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.77 | 14.63 | 23.32 | 2.00 | 70.2 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.6 | 4.02 | 12.90 | 19.41 | 3.00 | 66.8 | 90.0 |

## GW5

- Train rows: 164124
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Antoine Semenyo
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 72.30
- Actual score: 56.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (12.85) beats the best remaining Bench Boost opportunity (0.00).
- Chip advisory: bench_boost (0.57): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Transfer: Marc Cucurella Saseta -> Virgil van Dijk (projected gain 0.46, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (12.85) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 3.39 | 10.77 | 16.91 | 2.00 | 81.6 | 90.0 |
| Bench 1 | Bench Boost | Matz Sels | GK | 16 | 5.0 | 2.96 | 8.60 | 13.76 | 3.00 | 85.1 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.5 | 4.41 | 12.41 | 18.72 | 2.00 | 73.7 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.6 | 4.34 | 12.23 | 19.43 | 1.00 | 92.6 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.6 | 4.27 | 12.22 | 19.13 | 1.00 | 81.7 | 88.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.48 | 12.17 | 18.76 | 4.00 | 82.1 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 5.6 | 3.84 | 11.34 | 18.05 | 1.00 | 67.7 | 79.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.55 | 16.46 | 26.20 | 2.00 | 80.9 | 90.0 |
| Bench 3 | Bench Boost | Lyle Foster | FWD | 3 | 5.0 | 3.05 | 8.44 | 13.50 | 6.00 | 73.1 | 85.0 |
| Bench 4 | Bench Boost | Junior Kroupi | FWD | 4 | 4.5 | 2.65 | 5.41 | 7.69 | 0.00 | 41.6 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.26 | 22.10 | 36.06 | 5.00 | 99.8 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.4 | 6.25 | 17.90 | 27.28 | 5.00 | 88.9 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.00 | 14.28 | 22.82 | 10.00 | 75.7 | 86.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.6 | 3.87 | 11.86 | 19.44 | 7.00 | 72.1 | 90.0 |
| Bench 2 | Bench Boost | Cody Gakpo | MID | 12 | 7.6 | 3.70 | 11.78 | 18.94 | 2.00 | 60.3 | 60.0 |