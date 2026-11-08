# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 228.03
- Total actual points: 263.00
- Average predicted points: 57.01
- Average actual points: 65.75
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW34 are included before the first simulated week.
- League-average scores were not available for this run.

## GW35

- Train rows: 187673
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Morgan Gibbs-White
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 50.12
- Actual score: 46.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.22 | 10.28 | 16.59 | 6.00 | 80.0 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.8 | 3.06 | 8.50 | 13.97 | 8.00 | 82.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.35 | 13.13 | 20.79 | 6.00 | 92.8 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 3.66 | 10.91 | 16.89 | 1.00 | 59.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.1 | 3.61 | 10.89 | 17.12 | 6.00 | 80.3 | 90.0 |
| Bench 4 | Bench | Virgil van Dijk | DEF | 12 | 6.2 | 3.22 | 10.84 | 17.79 | 1.00 | 72.8 | 90.0 |
| XI | XI | Nikola Milenković | DEF | 16 | 5.1 | 3.52 | 10.60 | 16.90 | 1.00 | 78.6 | 45.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.47 | 13.68 | 22.06 | 6.00 | 82.0 | 90.0 |
| Bench 3 | Bench | Jarrod Bowen | FWD | 19 | 7.8 | 3.37 | 11.64 | 18.49 | 2.00 | 64.9 | 87.0 |
| Bench 2 | Bench | Benjamin Sesko | FWD | 14 | 7.3 | 3.40 | 9.99 | 16.14 | 5.00 | 71.5 | 45.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 5.22 | 16.45 | 28.48 | 5.00 | 102.0 | 90.0 |
| Vice Captain | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 4.51 | 13.86 | 21.86 | 4.00 | 70.9 | 20.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 3.89 | 12.71 | 19.26 | 4.00 | 91.3 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.30 | 12.55 | 20.01 | 1.00 | 81.0 | 45.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.14 | 12.37 | 20.12 | 1.00 | 73.5 | 90.0 |

## GW36

- Train rows: 188505
- Bank: 0.00 -> 1.00
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Rayan Cherki
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 65.42
- Actual score: 66.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (14.69) beats the best remaining Bench Boost opportunity (11.41).
- Transfer: Morgan Gibbs-White -> Rayan Cherki (projected gain 3.31, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (14.69) beats the best remaining Bench Boost opportunity (11.41).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.65 | 10.88 | 17.67 | 9.00 | 84.8 | 90.0 |
| Bench 1 | Bench Boost | Caoimhín Kelleher | GK | 5 | 4.8 | 2.35 | 7.52 | 12.42 | 3.00 | 77.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.57 | 13.13 | 20.53 | 11.00 | 94.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.04 | 11.95 | 19.14 | 2.00 | 82.7 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 4.62 | 11.29 | 17.07 | 5.00 | 99.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.1 | 4.03 | 11.09 | 17.51 | 5.00 | 81.1 | 90.0 |
| Bench 3 | Bench Boost | Nikola Milenković | DEF | 16 | 5.1 | 2.71 | 8.04 | 13.10 | 2.00 | 64.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.50 | 12.39 | 20.98 | 2.00 | 72.7 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 3.46 | 11.55 | 19.48 | 2.00 | 72.3 | 90.0 |
| Bench 4 | Bench Boost | Benjamin Sesko | FWD | 14 | 7.3 | 2.58 | 8.16 | 12.95 | 0.00 | 56.4 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.45 | 18.17 | 30.13 | 3.00 | 104.3 | 90.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.53 | 13.30 | 20.67 | 0.00 | 89.0 | 0.0 |
| Vice Captain | XI | Rayan Cherki | MID | 13 | 6.6 | 5.22 | 12.92 | 19.95 | 5.00 | 103.9 | 70.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 3.98 | 12.24 | 19.67 | 2.00 | 74.2 | 90.0 |
| Bench 2 | Bench Boost | Elliot Anderson | MID | 16 | 5.6 | 3.28 | 9.68 | 15.98 | 12.00 | 61.5 | 90.0 |

## GW37

- Train rows: 189343
- Bank: 1.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 52.76
- Actual score: 71.00
- Transfer: Morgan Rogers -> Antoine Semenyo (projected gain 3.60, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.17 | 10.28 | 16.35 | 6.00 | 86.2 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.8 | 3.28 | 9.43 | 15.73 | 2.00 | 86.0 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.50 | 14.03 | 22.06 | 6.00 | 93.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.68 | 11.26 | 18.69 | 14.00 | 83.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.1 | 4.17 | 10.43 | 16.34 | 8.00 | 83.0 | 90.0 |
| XI | XI | Nikola Milenković | DEF | 16 | 5.1 | 3.04 | 8.94 | 14.51 | 1.00 | 78.8 | 90.0 |
| Bench 3 | Bench | Nico O'Reilly | DEF | 13 | 5.2 | 2.36 | 8.04 | 13.87 | 2.00 | 49.3 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.51 | 12.95 | 21.38 | 2.00 | 83.4 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 3.84 | 11.33 | 19.05 | 2.00 | 79.8 | 90.0 |
| Bench 4 | Bench | Benjamin Sesko | FWD | 14 | 7.3 | 2.17 | 6.43 | 11.03 | 0.00 | 31.8 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.31 | 17.78 | 29.36 | 9.00 | 108.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 4.71 | 13.68 | 22.20 | 1.00 | 104.5 | 55.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.6 | 3.19 | 10.79 | 17.96 | 1.00 | 49.0 | 34.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.33 | 10.09 | 16.97 | 12.00 | 75.9 | 90.0 |
| Bench 2 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.68 | 8.30 | 14.37 | 1.00 | 43.3 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 0.30 -> 1.00
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 59.72
- Actual score: 80.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.96) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Benjamin Sesko -> Richarlison de Andrade (projected gain 2.14, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (5.96) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Caoimhín Kelleher replaced David Raya Martín.
- Autosub: Rayan Cherki replaced William Saliba.
- Autosub: Nikola Milenković replaced Nico O'Reilly.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martín | GK | 1 | 6.1 | 4.25 | 12.31 | 19.80 | 0.00 | 84.0 | 0.0 |
| Bench 1 | Autosub In | Caoimhín Kelleher | GK | 5 | 4.8 | 2.53 | 7.48 | 12.64 | 6.00 | 82.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.54 | 12.96 | 20.71 | 1.00 | 86.4 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.45 | 12.32 | 19.83 | 2.00 | 99.9 | 90.0 |
| XI | Bench | William Saliba | DEF | 1 | 6.2 | 3.83 | 11.26 | 17.94 | 0.00 | 78.5 | 0.0 |
| XI | Bench | Nico O'Reilly | DEF | 13 | 5.2 | 3.45 | 9.46 | 15.30 | 0.00 | 69.0 | 0.0 |
| Bench 4 | Autosub In | Nikola Milenković | DEF | 16 | 5.1 | 2.63 | 7.89 | 13.52 | 4.00 | 72.6 | 90.0 |
| XI | XI | Richarlison de Andrade | FWD | 18 | 6.5 | 4.51 | 12.08 | 18.52 | 2.00 | 81.7 | 72.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.8 | 4.68 | 11.93 | 19.84 | 12.00 | 99.6 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 3.62 | 11.22 | 18.83 | 2.00 | 77.8 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 5.96 | 17.58 | 29.50 | 14.00 | 106.7 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 4.41 | 11.95 | 19.81 | 6.00 | 81.5 | 57.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.11 | 11.49 | 19.11 | 2.00 | 89.7 | 64.0 |
| Bench 2 | Autosub In | Rayan Cherki | MID | 13 | 6.5 | 3.27 | 10.07 | 16.27 | 1.00 | 48.7 | 32.0 |
| Bench 3 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.65 | 8.21 | 15.16 | 0.00 | 50.1 | 0.0 |