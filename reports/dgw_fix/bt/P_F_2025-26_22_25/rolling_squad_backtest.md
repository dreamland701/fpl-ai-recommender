# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW21
- Simulated weeks: GW22-GW25
- Total predicted points: 268.00
- Total actual points: 228.00
- Average predicted points: 67.00
- Average actual points: 57.00
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW21 are included before the first simulated week.
- League-average scores were not available for this run.

## GW22

- Train rows: 177037
- Bank: 100.00 -> 0.30
- Free transfers: 1 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Guimarães Rodriguez Moura
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 64.60
- Actual score: 46.00
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: James Tarkowski replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.85 | 11.19 | 21.87 | 6.00 | 89.8 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.6 | 3.38 | 9.77 | 15.91 | 1.00 | 88.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 5.01 | 13.48 | 23.36 | 8.00 | 79.9 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.3 | 4.57 | 12.97 | 20.95 | 0.00 | 90.0 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 4.48 | 12.64 | 23.89 | 5.00 | 85.9 | 90.0 |
| Bench 2 | Autosub In | James Tarkowski | DEF | 9 | 5.7 | 4.25 | 12.59 | 19.92 | 8.00 | 86.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.49 | 12.09 | 19.62 | 2.00 | 89.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.37 | 24.99 | 40.81 | 2.00 | 90.0 | 79.0 |
| Bench 3 | Bench | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 4.07 | 12.35 | 19.48 | 2.00 | 77.2 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.5 | 2.90 | 8.08 | 14.65 | 2.00 | 68.2 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.40 | 15.89 | 25.76 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 5.63 | 15.61 | 24.85 | 3.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.05 | 14.36 | 23.96 | 2.00 | 84.8 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 5.00 | 13.85 | 22.45 | 2.00 | 90.0 | 87.0 |
| XI | XI | James Garner | MID | 9 | 5.2 | 4.37 | 13.07 | 20.78 | 4.00 | 89.2 | 90.0 |

## GW23

- Train rows: 177836
- Bank: 0.30 -> 0.60
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 63.45
- Actual score: 43.00
- Transfer: Virgil van Dijk -> Trevoh Chalobah (projected gain 1.32, hit 0)
- Autosub: Dominic Calvert-Lewin replaced Bruno Guimarães Rodriguez Moura.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.96 | 11.24 | 21.95 | 1.00 | 88.9 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.6 | 3.08 | 8.98 | 14.82 | 1.00 | 82.9 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.90 | 13.28 | 21.55 | 4.00 | 89.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 4.62 | 13.13 | 23.47 | 1.00 | 79.8 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 4.33 | 12.38 | 23.49 | 1.00 | 86.2 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.6 | 4.49 | 12.34 | 19.24 | 4.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Marc Guéhi | DEF | 8 | 5.2 | 2.85 | 8.00 | 13.89 | 6.00 | 49.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.46 | 23.75 | 39.17 | 1.00 | 90.0 | 17.0 |
| Bench 2 | Autosub In | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 3.62 | 10.79 | 17.22 | 2.00 | 73.3 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.5 | 2.55 | 7.93 | 15.11 | 2.00 | 69.8 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.67 | 15.42 | 24.75 | 8.00 | 90.0 | 90.0 |
| XI | XI | James Garner | MID | 9 | 5.2 | 5.00 | 13.96 | 21.99 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 4.58 | 13.49 | 21.96 | 0.00 | 76.8 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.71 | 13.34 | 21.88 | 8.00 | 78.5 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.27 | 11.80 | 19.62 | 10.00 | 76.4 | 90.0 |

## GW24

- Train rows: 178639
- Bank: 0.60 -> 1.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 67.41
- Actual score: 62.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.81) beats the best remaining Triple Captain opportunity (7.42).
- Transfer: Bruno Guimarães Rodriguez Moura -> Enzo Fernández (projected gain 3.18, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (6.81) beats the best remaining Triple Captain opportunity (7.42).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.98 | 15.01 | 22.01 | 6.00 | 88.2 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.6 | 2.63 | 8.33 | 13.91 | 10.00 | 81.4 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 5.02 | 18.95 | 26.94 | 8.00 | 87.6 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 4.07 | 15.73 | 23.14 | 5.00 | 81.2 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.6 | 4.82 | 12.86 | 20.09 | 3.00 | 90.0 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.05 | 11.99 | 19.80 | 2.00 | 82.8 | 90.0 |
| Bench 2 | Bench | Marc Guéhi | DEF | 8 | 5.2 | 3.86 | 10.81 | 17.95 | 3.00 | 76.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.0 | 6.81 | 20.77 | 35.54 | 5.00 | 80.8 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.5 | 2.97 | 10.61 | 15.57 | 2.00 | 67.5 | 90.0 |
| Bench 3 | Bench | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 3.48 | 10.15 | 16.69 | 2.00 | 72.4 | 84.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.92 | 16.67 | 27.06 | 7.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.51 | 15.39 | 24.64 | 2.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 5.23 | 13.87 | 22.33 | 8.00 | 83.3 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.33 | 12.84 | 20.98 | 2.00 | 86.7 | 90.0 |
| XI | XI | James Garner | MID | 9 | 5.2 | 4.06 | 12.30 | 20.03 | 4.00 | 82.2 | 90.0 |

## GW25

- Train rows: 179450
- Bank: 1.10 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 72.54
- Actual score: 77.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.08) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Marc Guéhi -> Virgil van Dijk (projected gain 0.80, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.08) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.26 | 15.51 | 22.46 | 7.00 | 87.6 | 90.0 |
| Bench 1 | Bench Boost | Caoimhín Kelleher | GK | 5 | 4.6 | 3.02 | 8.95 | 14.68 | 1.00 | 83.4 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 5.52 | 20.14 | 28.83 | 6.00 | 89.2 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 4.49 | 16.03 | 23.43 | 6.00 | 79.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.22 | 12.51 | 19.81 | 0.00 | 90.0 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.6 | 4.40 | 12.26 | 19.31 | 4.00 | 86.7 | 90.0 |
| Bench 2 | Bench Boost | James Tarkowski | DEF | 9 | 5.7 | 4.08 | 11.76 | 19.47 | 2.00 | 82.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 6.73 | 20.96 | 35.64 | 11.00 | 90.0 | 90.0 |
| Bench 4 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 2.94 | 11.26 | 16.42 | 2.00 | 69.4 | 90.0 |
| Bench 3 | Bench Boost | Dominic Calvert-Lewin | FWD | 11 | 5.9 | 3.04 | 8.96 | 15.09 | 7.00 | 64.2 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.39 | 15.84 | 26.09 | 2.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 4.73 | 13.80 | 22.29 | 10.00 | 81.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 4.67 | 13.48 | 21.74 | 2.00 | 77.9 | 90.0 |
| XI | XI | James Garner | MID | 9 | 5.2 | 4.22 | 12.14 | 19.47 | 4.00 | 83.2 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.09 | 11.87 | 18.92 | 2.00 | 80.2 | 90.0 |