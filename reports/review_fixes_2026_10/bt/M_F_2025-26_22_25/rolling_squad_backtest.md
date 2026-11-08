# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW21
- Simulated weeks: GW22-GW25
- Total predicted points: 260.97
- Total actual points: 226.00
- Average predicted points: 65.24
- Average actual points: 56.50
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
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Guimarães Rodriguez Moura
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 61.91
- Actual score: 50.00
- Chip advisory: bench_boost (0.62): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Nathan Collins replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.68 | 10.96 | 18.05 | 6.00 | 85.2 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.5 | 3.41 | 10.34 | 16.96 | 1.00 | 89.3 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.56 | 13.33 | 20.93 | 8.00 | 88.5 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 13 | 5.3 | 4.51 | 13.17 | 21.32 | 0.00 | 91.6 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.6 | 4.43 | 12.78 | 19.07 | 8.00 | 71.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.41 | 11.91 | 19.41 | 2.00 | 84.7 | 90.0 |
| Bench 2 | Autosub In | Nathan Collins | DEF | 5 | 4.9 | 4.02 | 11.85 | 20.15 | 1.00 | 85.6 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 7.58 | 22.80 | 37.23 | 2.00 | 104.4 | 79.0 |
| Bench 3 | Bench | Dominic Calvert-Lewin | FWD | 11 | 5.9 | 4.00 | 12.50 | 19.97 | 2.00 | 73.6 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.5 | 3.15 | 8.97 | 13.64 | 2.00 | 72.8 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 4.95 | 15.45 | 25.35 | 2.00 | 89.5 | 90.0 |
| Vice Captain | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.1 | 5.29 | 15.05 | 24.44 | 3.00 | 94.0 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.21 | 14.45 | 23.39 | 10.00 | 74.1 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 4.98 | 14.28 | 24.00 | 2.00 | 81.0 | 90.0 |
| XI | XI | James Garner | MID | 9 | 5.1 | 4.73 | 14.03 | 22.24 | 4.00 | 91.1 | 90.0 |

## GW23

- Train rows: 177836
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Guimarães Rodriguez Moura
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 61.89
- Actual score: 34.00
- Transfer: Marc Guéhi -> Marcos Senesi Barón (projected gain 0.71, hit 0)
- Autosub: Nathan Collins replaced Bruno Guimarães Rodriguez Moura.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.84 | 11.42 | 18.67 | 1.00 | 84.8 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.5 | 3.19 | 9.33 | 15.48 | 1.00 | 81.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.7 | 4.72 | 13.91 | 21.18 | 1.00 | 80.0 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.62 | 12.68 | 20.86 | 4.00 | 83.6 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 4.14 | 11.77 | 18.42 | 3.00 | 86.7 | 90.0 |
| Bench 2 | Autosub In | Nathan Collins | DEF | 5 | 4.9 | 3.91 | 11.14 | 18.49 | 1.00 | 84.4 | 90.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 12 | 5.9 | 3.59 | 11.02 | 18.14 | 9.00 | 84.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 7.55 | 20.93 | 34.77 | 1.00 | 97.2 | 17.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 11 | 5.9 | 4.04 | 11.86 | 18.80 | 2.00 | 76.9 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.5 | 2.98 | 8.76 | 13.89 | 2.00 | 69.7 | 90.0 |
| Vice Captain | Bench | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.1 | 5.47 | 15.58 | 25.08 | 0.00 | 88.3 | 0.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.26 | 15.24 | 24.84 | 8.00 | 84.0 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 4.74 | 14.53 | 24.01 | 2.00 | 78.3 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 4.98 | 14.21 | 23.20 | 8.00 | 81.8 | 90.0 |
| XI | XI | James Garner | MID | 9 | 5.1 | 4.96 | 13.67 | 21.63 | 2.00 | 89.1 | 90.0 |

## GW24

- Train rows: 178639
- Bank: 0.50 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 65.33
- Actual score: 71.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.38) beats the best remaining Triple Captain opportunity (7.15).
- Transfer: Bruno Guimarães Rodriguez Moura -> Declan Rice (projected gain 5.16, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (6.38) beats the best remaining Triple Captain opportunity (7.15).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.74 | 10.96 | 17.97 | 6.00 | 83.2 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.5 | 2.69 | 8.70 | 14.66 | 10.00 | 80.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.7 | 4.56 | 13.46 | 21.72 | 8.00 | 78.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.42 | 12.85 | 20.80 | 4.00 | 92.1 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.10 | 11.90 | 19.49 | 2.00 | 82.2 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 4.18 | 11.66 | 18.34 | 8.00 | 90.5 | 90.0 |
| Bench 3 | Bench | Nathan Collins | DEF | 5 | 4.9 | 3.02 | 9.72 | 16.41 | 1.00 | 81.7 | 30.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 6.38 | 19.39 | 32.95 | 5.00 | 74.4 | 90.0 |
| Bench 2 | Bench | Dominic Calvert-Lewin | FWD | 11 | 5.9 | 3.81 | 10.98 | 17.96 | 2.00 | 77.0 | 84.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.5 | 2.91 | 8.19 | 13.75 | 2.00 | 68.2 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.55 | 16.26 | 26.55 | 7.00 | 93.6 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.4 | 5.42 | 16.04 | 25.54 | 3.00 | 91.2 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 5.34 | 15.31 | 24.72 | 2.00 | 89.0 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 4.66 | 13.94 | 23.38 | 12.00 | 76.5 | 86.0 |
| XI | XI | James Garner | MID | 9 | 5.1 | 4.24 | 12.58 | 20.39 | 4.00 | 83.5 | 90.0 |

## GW25

- Train rows: 179450
- Bank: 0.30 -> 0.60
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 71.84
- Actual score: 71.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (12.45) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Marcos Senesi Barón -> Nordi Mukiele (projected gain 0.67, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (12.45) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.08 | 11.58 | 18.78 | 7.00 | 84.1 | 90.0 |
| Bench 1 | Bench Boost | Caoimhín Kelleher | GK | 5 | 4.5 | 3.22 | 9.80 | 16.15 | 1.00 | 85.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 5.30 | 15.00 | 24.16 | 6.00 | 86.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.26 | 12.42 | 19.75 | 0.00 | 90.9 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.17 | 12.09 | 19.91 | 2.00 | 83.5 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.5 | 3.85 | 11.90 | 19.73 | 1.00 | 84.1 | 90.0 |
| Bench 4 | Bench Boost | Nathan Collins | DEF | 5 | 4.9 | 2.75 | 8.99 | 15.60 | 0.00 | 61.8 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.0 | 6.21 | 19.66 | 33.39 | 11.00 | 86.5 | 90.0 |
| Bench 2 | Bench Boost | Dominic Calvert-Lewin | FWD | 11 | 5.9 | 3.29 | 9.77 | 16.43 | 7.00 | 66.5 | 90.0 |
| Bench 3 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 3.19 | 9.14 | 15.03 | 2.00 | 73.0 | 90.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.4 | 5.55 | 16.09 | 26.24 | 5.00 | 85.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.36 | 16.04 | 26.49 | 2.00 | 93.9 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 5.00 | 14.71 | 23.73 | 10.00 | 84.7 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.03 | 14.63 | 24.40 | 2.00 | 83.6 | 90.0 |
| XI | XI | James Garner | MID | 9 | 5.1 | 4.37 | 12.60 | 20.16 | 4.00 | 86.0 | 90.0 |