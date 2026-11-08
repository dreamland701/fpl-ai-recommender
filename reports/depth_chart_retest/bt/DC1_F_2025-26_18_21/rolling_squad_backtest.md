# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW17
- Simulated weeks: GW18-GW21
- Total predicted points: 268.09
- Total actual points: 172.00
- Average predicted points: 67.02
- Average actual points: 43.00
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
- Predicted score: 66.47
- Actual score: 40.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.07 | 11.67 | 19.03 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Krisztián Hegyi | GK | 19 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 2.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.89 | 13.36 | 20.99 | 2.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.01 | 11.53 | 18.25 | 2.00 | 81.6 | 90.0 |
| XI | XI | Matheus Nunes | DEF | 13 | 5.4 | 3.64 | 11.04 | 18.14 | 4.00 | 82.9 | 90.0 |
| Bench 3 | Bench | Nordi Mukiele | DEF | 17 | 4.2 | 3.43 | 9.42 | 14.85 | 4.00 | 83.0 | 90.0 |
| Bench 4 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.53 | 7.60 | 12.14 | 2.00 | 67.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.49 | 24.97 | 41.31 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 7.04 | 18.91 | 28.33 | 5.00 | 88.6 | 85.0 |
| Bench 2 | Bench | Dominic Calvert-Lewin | FWD | 11 | 5.8 | 3.89 | 11.70 | 18.62 | 8.00 | 67.4 | 84.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.50 | 17.46 | 28.12 | 2.00 | 80.7 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 5.76 | 16.44 | 25.84 | 5.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 5.39 | 15.62 | 24.47 | 1.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.23 | 15.43 | 24.41 | 9.00 | 82.2 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 4.8 | 3.95 | 11.86 | 18.76 | 4.00 | 79.6 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 59.32
- Actual score: 34.00
- Transfer: Matheus Nunes -> Marc Guéhi (projected gain 1.30, hit 0)
- Autosub: Dominic Calvert-Lewin replaced Declan Rice.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.96 | 11.29 | 18.45 | 2.00 | 88.1 | 90.0 |
| Bench 1 | Bench | Krisztián Hegyi | GK | 19 | 3.9 | 0.07 | 0.15 | 0.21 | 0.00 | 3.1 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.28 | 11.85 | 18.97 | 2.00 | 87.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.01 | 11.64 | 19.22 | 6.00 | 81.4 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 3.88 | 11.15 | 17.44 | 3.00 | 86.7 | 90.0 |
| Bench 3 | Bench | Nordi Mukiele | DEF | 17 | 4.2 | 2.94 | 8.67 | 14.21 | 11.00 | 81.6 | 90.0 |
| Bench 4 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.43 | 7.60 | 12.36 | 8.00 | 69.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.11 | 24.04 | 40.10 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.61 | 14.01 | 21.78 | 2.00 | 56.8 | 90.0 |
| Bench 2 | Autosub In | Dominic Calvert-Lewin | FWD | 11 | 5.8 | 3.16 | 10.41 | 17.51 | 1.00 | 56.1 | 20.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 9.0 | 5.23 | 16.42 | 27.53 | 3.00 | 82.3 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 4.96 | 14.68 | 23.66 | 5.00 | 83.0 | 90.0 |
| XI | Bench | Declan Rice | MID | 1 | 7.2 | 4.43 | 13.32 | 21.64 | 0.00 | 73.4 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.68 | 12.65 | 20.56 | 1.00 | 72.8 | 81.0 |
| XI | XI | Anton Stach | MID | 11 | 4.8 | 4.05 | 12.41 | 20.10 | 5.00 | 79.1 | 90.0 |

## GW20

- Train rows: 175452
- Bank: 0.10 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 73.01
- Actual score: 33.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.96) beats the best remaining Bench Boost opportunity (11.31).
- Transfer: Declan Rice -> Rayan Cherki (projected gain 5.47, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.96) beats the best remaining Bench Boost opportunity (11.31).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.06 | 11.85 | 19.16 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Krisztián Hegyi | GK | 19 | 3.9 | 0.14 | 0.28 | 0.40 | 0.00 | 4.2 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.14 | 11.63 | 18.61 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.85 | 11.28 | 18.75 | 1.00 | 84.2 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 3.83 | 11.16 | 18.52 | 1.00 | 82.4 | 90.0 |
| Bench 2 | Bench Boost | Nordi Mukiele | DEF | 17 | 4.2 | 3.64 | 10.18 | 16.73 | 4.00 | 90.0 | 90.0 |
| Bench 4 | Bench Boost | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.76 | 7.73 | 11.99 | 2.00 | 76.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.31 | 24.49 | 40.53 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.79 | 14.81 | 24.31 | 0.00 | 69.7 | 0.0 |
| Bench 3 | Bench Boost | Dominic Calvert-Lewin | FWD | 11 | 5.8 | 3.43 | 10.00 | 16.85 | 2.00 | 48.9 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.9 | 5.70 | 17.49 | 28.77 | 2.00 | 85.8 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 5.53 | 15.94 | 25.18 | 5.00 | 90.0 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.8 | 5.09 | 15.58 | 25.04 | 4.00 | 75.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.05 | 14.79 | 23.70 | 1.00 | 90.0 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 4.8 | 4.39 | 12.13 | 19.75 | 4.00 | 82.6 | 90.0 |

## GW21

- Train rows: 176242
- Bank: 0.40 -> 2.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 69.30
- Actual score: 65.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.16) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Hugo Ekitiké -> Igor Thiago Nascimento Rodrigues (projected gain 6.31, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.16) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.75 | 10.84 | 17.77 | 6.00 | 87.3 | 90.0 |
| Bench 1 | Bench | Krisztián Hegyi | GK | 19 | 3.9 | 0.06 | 0.13 | 0.14 | 0.00 | 3.5 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.21 | 11.52 | 18.52 | 6.00 | 87.6 | 90.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 12 | 5.9 | 3.15 | 10.01 | 16.84 | 6.00 | 81.8 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.2 | 3.41 | 9.78 | 16.13 | 3.00 | 87.2 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 3.29 | 9.13 | 16.24 | 6.00 | 71.0 | 90.0 |
| Bench 4 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.43 | 7.18 | 11.50 | 0.00 | 73.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.16 | 24.16 | 39.43 | 6.00 | 90.0 | 90.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.98 | 16.68 | 26.59 | 12.00 | 90.0 | 81.0 |
| Bench 2 | Bench | Dominic Calvert-Lewin | FWD | 11 | 5.8 | 3.23 | 10.42 | 16.97 | 8.00 | 62.1 | 86.0 |
| XI | XI | Phil Foden | MID | 13 | 8.8 | 5.40 | 15.85 | 26.60 | 2.00 | 81.3 | 72.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.8 | 5.16 | 15.13 | 24.18 | 1.00 | 83.0 | 17.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 4.94 | 13.93 | 22.78 | 6.00 | 89.7 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 4.51 | 13.23 | 21.38 | 3.00 | 73.7 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 4.8 | 4.16 | 11.72 | 19.54 | 2.00 | 82.0 | 79.0 |