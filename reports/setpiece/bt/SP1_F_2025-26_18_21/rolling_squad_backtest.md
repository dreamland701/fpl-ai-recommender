# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW17
- Simulated weeks: GW18-GW21
- Total predicted points: 260.97
- Total actual points: 184.00
- Average predicted points: 65.24
- Average actual points: 46.00
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW17 are included before the first simulated week.
- League-average scores were not available for this run.

## GW18

- Train rows: 173897
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Erling Haaland
- Vice captain: Hugo Ekitiké
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 66.58
- Actual score: 42.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.77 | 10.80 | 17.63 | 2.00 | 87.8 | 90.0 |
| Bench 1 | Bench | Blondy Nna Noukeu | GK | 17 | 3.9 | 0.19 | 0.20 | 0.34 | 0.00 | 4.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.01 | 13.65 | 21.42 | 2.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.13 | 11.73 | 18.74 | 2.00 | 80.3 | 90.0 |
| XI | XI | Matheus Nunes | DEF | 13 | 5.4 | 3.69 | 11.30 | 18.65 | 4.00 | 84.4 | 90.0 |
| Bench 2 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 2.68 | 8.07 | 12.57 | 2.00 | 68.9 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.56 | 7.62 | 12.14 | 2.00 | 68.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.34 | 24.40 | 40.27 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 6.86 | 18.27 | 27.23 | 5.00 | 86.6 | 85.0 |
| Bench 4 | Bench | Zian Flemming | FWD | 3 | 5.3 | 2.39 | 6.98 | 11.58 | 1.00 | 45.4 | 2.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.65 | 17.63 | 28.26 | 2.00 | 81.5 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 5.86 | 16.77 | 26.47 | 5.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 5.63 | 16.12 | 25.17 | 1.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.29 | 15.53 | 24.59 | 9.00 | 82.7 | 90.0 |
| XI | XI | Granit Xhaka | MID | 17 | 5.2 | 4.02 | 11.76 | 18.87 | 6.00 | 84.6 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 58.81
- Actual score: 45.00
- Transfer: Matheus Nunes -> Michael Keane (projected gain 0.65, hit 0)
- Autosub: Jaka Bijol replaced Michael Keane.
- Autosub: Gabriel Gudmundsson replaced Declan Rice.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.63 | 10.36 | 16.96 | 2.00 | 84.4 | 90.0 |
| Bench 1 | Bench | Blondy Nna Noukeu | GK | 17 | 3.9 | 0.00 | 0.08 | 0.28 | 0.00 | 5.4 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.50 | 12.37 | 19.78 | 2.00 | 89.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.12 | 11.87 | 19.56 | 6.00 | 82.6 | 90.0 |
| XI | Bench | Michael Keane | DEF | 9 | 4.8 | 3.94 | 11.36 | 17.75 | 0.00 | 89.5 | 0.0 |
| Bench 2 | Autosub In | Jaka Bijol | DEF | 11 | 3.9 | 2.54 | 7.85 | 12.79 | 7.00 | 69.3 | 90.0 |
| Bench 3 | Autosub In | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.44 | 7.58 | 12.31 | 8.00 | 70.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 7.95 | 23.46 | 39.04 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.40 | 13.28 | 20.53 | 2.00 | 54.1 | 90.0 |
| Bench 4 | Bench | Zian Flemming | FWD | 3 | 5.3 | 1.62 | 5.45 | 9.44 | 0.00 | 27.3 | 0.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 9.0 | 5.36 | 16.55 | 27.62 | 3.00 | 82.8 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.13 | 15.13 | 24.42 | 5.00 | 84.4 | 90.0 |
| XI | Bench | Declan Rice | MID | 1 | 7.2 | 4.51 | 13.62 | 22.21 | 0.00 | 74.0 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.86 | 12.95 | 20.93 | 1.00 | 74.2 | 81.0 |
| XI | XI | Granit Xhaka | MID | 17 | 5.2 | 3.46 | 10.86 | 18.06 | 5.00 | 84.6 | 90.0 |

## GW20

- Train rows: 175452
- Bank: 0.60 -> 0.90
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 67.35
- Actual score: 30.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.89) beats the best remaining Bench Boost opportunity (7.46).
- Transfer: Declan Rice -> Rayan Cherki (projected gain 5.44, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.89) beats the best remaining Bench Boost opportunity (7.46).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.74 | 10.93 | 17.68 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Blondy Nna Noukeu | GK | 17 | 3.9 | 0.11 | 0.42 | 0.68 | 0.00 | 6.6 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.37 | 12.21 | 19.52 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.00 | 11.68 | 19.36 | 1.00 | 86.1 | 90.0 |
| XI | XI | Jaka Bijol | DEF | 11 | 3.9 | 2.96 | 8.11 | 13.37 | 4.00 | 74.5 | 90.0 |
| Bench 2 | Bench Boost | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.83 | 7.92 | 12.29 | 2.00 | 78.4 | 90.0 |
| Bench 3 | Bench Boost | Michael Keane | DEF | 9 | 4.8 | 1.96 | 6.18 | 10.75 | 0.00 | 42.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.14 | 23.90 | 39.46 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.53 | 13.93 | 22.82 | 0.00 | 66.6 | 0.0 |
| Bench 4 | Bench Boost | Zian Flemming | FWD | 3 | 5.3 | 0.99 | 4.01 | 7.11 | 0.00 | 21.4 | 0.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.9 | 5.81 | 17.55 | 28.76 | 2.00 | 86.1 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 5.75 | 16.37 | 25.75 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.28 | 15.40 | 24.70 | 1.00 | 90.0 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.8 | 4.83 | 14.62 | 23.38 | 4.00 | 72.9 | 90.0 |
| XI | XI | Granit Xhaka | MID | 17 | 5.2 | 3.92 | 11.50 | 18.92 | 4.00 | 90.0 | 90.0 |

## GW21

- Train rows: 176242
- Bank: 0.90 -> 2.90
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 68.23
- Actual score: 67.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.97) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Hugo Ekitiké -> Igor Thiago Nascimento Rodrigues (projected gain 7.68, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (7.97) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.42 | 9.90 | 16.26 | 6.00 | 83.6 | 90.0 |
| Bench 1 | Bench | Blondy Nna Noukeu | GK | 17 | 3.9 | 0.05 | 0.33 | 0.54 | 0.00 | 5.4 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.41 | 12.01 | 19.27 | 6.00 | 89.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.33 | 10.47 | 17.55 | 6.00 | 84.1 | 90.0 |
| XI | XI | Michael Keane | DEF | 9 | 4.8 | 3.27 | 8.62 | 13.94 | 5.00 | 69.5 | 82.0 |
| Bench 2 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 3.09 | 8.50 | 14.13 | 3.00 | 78.9 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.52 | 7.44 | 11.91 | 0.00 | 75.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 7.97 | 23.51 | 38.29 | 6.00 | 90.0 | 90.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.71 | 16.08 | 25.79 | 12.00 | 90.0 | 81.0 |
| Bench 4 | Bench | Zian Flemming | FWD | 3 | 5.3 | 0.90 | 2.84 | 5.34 | 0.00 | 15.5 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 8.8 | 5.47 | 15.82 | 26.44 | 2.00 | 81.4 | 72.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 5.19 | 14.60 | 23.90 | 6.00 | 90.0 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.8 | 4.98 | 14.45 | 22.99 | 1.00 | 81.4 | 17.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 4.72 | 13.60 | 21.86 | 3.00 | 75.1 | 90.0 |
| XI | XI | Granit Xhaka | MID | 17 | 5.2 | 3.82 | 11.24 | 18.70 | 2.00 | 90.0 | 90.0 |