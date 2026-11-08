# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW17
- Simulated weeks: GW18-GW21
- Total predicted points: 247.41
- Total actual points: 192.00
- Average predicted points: 61.85
- Average actual points: 48.00
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
- Captain: Hugo Ekitiké
- Vice captain: Phil Foden
- Effective captain: Hugo Ekitiké
- Chip used: none
- Predicted score: 63.43
- Actual score: 39.00
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Marcos Senesi Barón replaced Jurriën Timber.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.87 | 11.22 | 18.26 | 2.00 | 89.8 | 90.0 |
| Bench 1 | Bench | Gianluigi Donnarumma | GK | 13 | 5.7 | 3.32 | 9.61 | 15.88 | 2.00 | 85.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.05 | 13.90 | 21.92 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Jurriën Timber | DEF | 1 | 6.5 | 4.52 | 12.40 | 20.01 | 0.00 | 86.9 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.19 | 12.01 | 19.18 | 2.00 | 81.7 | 90.0 |
| Bench 2 | Autosub In | Marcos Senesi Barón | DEF | 4 | 4.9 | 3.93 | 11.52 | 18.25 | 2.00 | 81.2 | 90.0 |
| XI | XI | Ibrahima Konaté | DEF | 12 | 5.4 | 3.93 | 11.26 | 17.81 | 2.00 | 79.3 | 90.0 |
| Captain | Captain | Hugo Ekitiké | FWD | 12 | 9.0 | 7.03 | 17.87 | 27.13 | 5.00 | 90.0 | 85.0 |
| Bench 3 | Bench | Dominic Calvert-Lewin | FWD | 11 | 5.8 | 3.67 | 10.57 | 16.70 | 8.00 | 65.4 | 84.0 |
| Bench 4 | Bench | Raúl Jiménez Rodríguez | FWD | 10 | 6.3 | 3.22 | 9.20 | 15.18 | 9.00 | 70.2 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 9.0 | 5.70 | 17.70 | 28.45 | 2.00 | 82.7 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 5.69 | 16.16 | 25.51 | 5.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 5.66 | 15.76 | 24.82 | 1.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.30 | 15.33 | 24.31 | 9.00 | 83.3 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.0 | 5.47 | 14.86 | 22.94 | 2.00 | 87.7 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Matheus Santos Carneiro da Cunha
- Vice captain: Phil Foden
- Effective captain: Matheus Santos Carneiro da Cunha
- Chip used: none
- Predicted score: 55.82
- Actual score: 31.00
- Transfer: Jurriën Timber -> Reece James (projected gain 1.65, hit 0)
- Autosub: Raúl Jiménez Rodríguez replaced Declan Rice.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.73 | 10.81 | 17.71 | 2.00 | 86.4 | 90.0 |
| Bench 1 | Bench | Gianluigi Donnarumma | GK | 13 | 5.7 | 3.10 | 9.15 | 15.17 | 7.00 | 82.9 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.61 | 12.75 | 20.35 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.15 | 12.13 | 20.00 | 6.00 | 83.2 | 90.0 |
| XI | XI | Reece James | DEF | 7 | 5.7 | 4.32 | 11.71 | 18.62 | 1.00 | 85.5 | 45.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 3.86 | 11.41 | 17.81 | 3.00 | 86.8 | 90.0 |
| Bench 3 | Bench | Ibrahima Konaté | DEF | 12 | 5.4 | 3.20 | 9.28 | 15.09 | 7.00 | 76.6 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.43 | 12.89 | 20.03 | 2.00 | 54.9 | 90.0 |
| Bench 2 | Autosub In | Raúl Jiménez Rodríguez | FWD | 10 | 6.3 | 3.56 | 10.16 | 16.74 | 2.00 | 72.7 | 90.0 |
| Bench 4 | Bench | Dominic Calvert-Lewin | FWD | 11 | 5.8 | 2.96 | 9.23 | 15.48 | 1.00 | 54.0 | 20.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 9.0 | 5.36 | 16.84 | 28.08 | 3.00 | 83.0 | 90.0 |
| Captain | Captain | Matheus Santos Carneiro da Cunha | MID | 14 | 8.0 | 6.08 | 15.44 | 23.31 | 2.00 | 85.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.12 | 15.22 | 24.50 | 5.00 | 84.4 | 90.0 |
| XI | Bench | Declan Rice | MID | 1 | 7.2 | 4.28 | 13.02 | 21.27 | 0.00 | 70.8 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.81 | 12.51 | 20.34 | 1.00 | 73.2 | 81.0 |

## GW20

- Train rows: 175452
- Bank: 0.70 -> 1.00
- Free transfers: 2 -> 2
- Captain: Morgan Rogers
- Vice captain: Phil Foden
- Effective captain: Morgan Rogers
- Chip used: triple_captain
- Predicted score: 61.61
- Actual score: 43.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.87) beats the best remaining Triple Captain opportunity (7.20).
- Transfer: Declan Rice -> Rayan Cherki (projected gain 5.18, hit 0)
- Chip used: Triple Captain on Morgan Rogers. Optimizer chose Triple Captain here because the current estimated captain upside (5.87) beats the best remaining Triple Captain opportunity (7.20).
- Autosub: Dominic Calvert-Lewin replaced Hugo Ekitiké.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.90 | 11.44 | 18.63 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Gianluigi Donnarumma | GK | 13 | 5.7 | 3.54 | 10.37 | 16.86 | 2.00 | 87.9 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.46 | 12.62 | 20.36 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.03 | 11.83 | 19.72 | 1.00 | 86.5 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 3.89 | 11.14 | 18.41 | 1.00 | 84.6 | 90.0 |
| Bench 3 | Bench | Ibrahima Konaté | DEF | 12 | 5.4 | 3.18 | 9.63 | 16.10 | 1.00 | 79.5 | 90.0 |
| Bench 4 | Bench | Reece James | DEF | 7 | 5.7 | 2.42 | 8.55 | 14.66 | 1.00 | 64.6 | 90.0 |
| XI | Bench | Hugo Ekitiké | FWD | 12 | 9.0 | 4.61 | 14.27 | 23.31 | 0.00 | 68.4 | 0.0 |
| XI | XI | Raúl Jiménez Rodríguez | FWD | 10 | 6.2 | 3.75 | 10.29 | 16.82 | 5.00 | 75.8 | 84.0 |
| Bench 2 | Autosub In | Dominic Calvert-Lewin | FWD | 11 | 5.8 | 3.32 | 9.39 | 15.82 | 2.00 | 48.2 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.9 | 5.86 | 17.51 | 28.99 | 2.00 | 87.4 | 90.0 |
| Captain | Captain | Morgan Rogers | MID | 2 | 7.4 | 5.87 | 16.31 | 25.95 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.27 | 15.44 | 24.76 | 1.00 | 90.0 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.8 | 4.89 | 14.39 | 23.23 | 4.00 | 74.2 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.1 | 3.34 | 10.48 | 17.06 | 9.00 | 54.0 | 90.0 |

## GW21

- Train rows: 176242
- Bank: 1.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Igor Thiago Nascimento Rodrigues
- Vice captain: Phil Foden
- Effective captain: Igor Thiago Nascimento Rodrigues
- Chip used: bench_boost
- Predicted score: 66.55
- Actual score: 79.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.45) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Raúl Jiménez Rodríguez -> Igor Thiago Nascimento Rodrigues (projected gain 5.56, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.45) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.54 | 10.44 | 17.04 | 6.00 | 86.1 | 90.0 |
| Bench 1 | Bench Boost | Gianluigi Donnarumma | GK | 13 | 5.7 | 3.39 | 9.95 | 16.31 | 1.00 | 87.8 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.48 | 12.36 | 19.98 | 6.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.33 | 10.57 | 17.81 | 6.00 | 84.1 | 90.0 |
| XI | XI | Reece James | DEF | 7 | 5.7 | 3.63 | 10.40 | 16.82 | 1.00 | 80.4 | 25.0 |
| Bench 3 | Bench Boost | Ibrahima Konaté | DEF | 12 | 5.4 | 2.89 | 9.43 | 16.01 | 7.00 | 79.7 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 3.39 | 9.28 | 16.29 | 6.00 | 73.6 | 90.0 |
| Captain | Captain | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.78 | 15.44 | 24.82 | 12.00 | 90.0 | 81.0 |
| Bench 2 | Bench Boost | Dominic Calvert-Lewin | FWD | 11 | 5.8 | 3.18 | 10.10 | 16.36 | 8.00 | 62.4 | 86.0 |
| Bench 4 | Bench Boost | Hugo Ekitiké | FWD | 12 | 9.0 | 2.00 | 8.54 | 15.44 | 0.00 | 22.6 | 0.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.8 | 5.52 | 15.91 | 26.68 | 2.00 | 82.5 | 72.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 5.17 | 14.81 | 24.14 | 6.00 | 90.0 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.8 | 5.08 | 14.41 | 23.08 | 1.00 | 83.2 | 17.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 4.76 | 13.45 | 21.58 | 3.00 | 76.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.1 | 4.64 | 13.21 | 21.73 | 2.00 | 77.2 | 73.0 |