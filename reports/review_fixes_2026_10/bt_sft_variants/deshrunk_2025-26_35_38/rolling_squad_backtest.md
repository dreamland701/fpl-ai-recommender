# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 243.62
- Total actual points: 263.00
- Average predicted points: 60.91
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
- Predicted score: 53.72
- Actual score: 46.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.33 | 10.54 | 17.10 | 6.00 | 80.0 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.8 | 3.13 | 8.57 | 14.11 | 8.00 | 82.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.71 | 13.86 | 22.03 | 6.00 | 92.8 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 3.87 | 11.26 | 17.45 | 1.00 | 59.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.1 | 3.80 | 11.25 | 17.69 | 6.00 | 80.3 | 90.0 |
| Bench 4 | Bench | Virgil van Dijk | DEF | 12 | 6.2 | 3.33 | 11.19 | 18.54 | 1.00 | 72.8 | 90.0 |
| XI | XI | Nikola Milenković | DEF | 16 | 5.1 | 3.70 | 10.92 | 17.39 | 1.00 | 78.6 | 45.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.79 | 14.33 | 23.34 | 6.00 | 82.0 | 90.0 |
| Bench 3 | Bench | Jarrod Bowen | FWD | 19 | 7.8 | 3.50 | 12.06 | 19.35 | 2.00 | 64.9 | 87.0 |
| Bench 2 | Bench | Benjamin Sesko | FWD | 14 | 7.3 | 3.53 | 10.26 | 16.61 | 5.00 | 71.5 | 45.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 5.79 | 17.69 | 30.91 | 5.00 | 102.0 | 90.0 |
| Vice Captain | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 4.84 | 14.53 | 23.11 | 4.00 | 70.9 | 20.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.15 | 13.25 | 20.16 | 4.00 | 91.3 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.57 | 13.06 | 20.89 | 1.00 | 81.0 | 45.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.37 | 12.85 | 21.03 | 1.00 | 73.5 | 90.0 |

## GW36

- Train rows: 188505
- Bank: 0.00 -> 1.00
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Rayan Cherki
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 69.38
- Actual score: 66.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (14.73) beats the best remaining Bench Boost opportunity (11.75).
- Transfer: Morgan Gibbs-White -> Rayan Cherki (projected gain 3.97, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (14.73) beats the best remaining Bench Boost opportunity (11.75).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.79 | 11.23 | 18.24 | 9.00 | 84.8 | 90.0 |
| Bench 1 | Bench Boost | Caoimhín Kelleher | GK | 5 | 4.8 | 2.26 | 7.47 | 12.41 | 3.00 | 77.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.94 | 14.00 | 21.81 | 11.00 | 94.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.29 | 12.51 | 20.01 | 2.00 | 82.7 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 5.01 | 11.87 | 17.79 | 5.00 | 99.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.1 | 4.18 | 11.49 | 18.06 | 5.00 | 81.1 | 90.0 |
| Bench 3 | Bench Boost | Nikola Milenković | DEF | 16 | 5.1 | 2.71 | 8.10 | 13.21 | 2.00 | 64.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.62 | 12.90 | 21.91 | 2.00 | 72.7 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 3.57 | 12.03 | 20.36 | 2.00 | 72.3 | 90.0 |
| Bench 4 | Bench Boost | Benjamin Sesko | FWD | 14 | 7.3 | 2.64 | 8.38 | 13.29 | 0.00 | 56.4 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 7.12 | 19.83 | 32.73 | 3.00 | 104.3 | 90.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.81 | 14.00 | 21.63 | 0.00 | 89.0 | 0.0 |
| Vice Captain | XI | Rayan Cherki | MID | 13 | 6.6 | 5.76 | 13.75 | 21.08 | 5.00 | 103.9 | 70.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.20 | 12.80 | 20.56 | 2.00 | 74.2 | 90.0 |
| Bench 2 | Bench Boost | Elliot Anderson | MID | 16 | 5.6 | 3.35 | 9.86 | 16.33 | 12.00 | 61.5 | 90.0 |

## GW37

- Train rows: 189343
- Bank: 1.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 56.53
- Actual score: 71.00
- Transfer: Morgan Rogers -> Antoine Semenyo (projected gain 4.53, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.48 | 11.00 | 17.38 | 6.00 | 86.2 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.8 | 3.36 | 9.66 | 16.08 | 2.00 | 86.0 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 6.03 | 15.33 | 23.95 | 6.00 | 93.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.85 | 11.82 | 19.59 | 14.00 | 83.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.1 | 4.48 | 11.15 | 17.29 | 8.00 | 83.0 | 90.0 |
| XI | XI | Nikola Milenković | DEF | 16 | 5.1 | 3.08 | 9.16 | 14.82 | 1.00 | 78.8 | 90.0 |
| Bench 3 | Bench | Nico O'Reilly | DEF | 13 | 5.2 | 2.31 | 8.04 | 14.00 | 2.00 | 49.3 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.81 | 13.82 | 22.77 | 2.00 | 83.4 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 4.06 | 12.03 | 20.26 | 2.00 | 79.8 | 90.0 |
| Bench 4 | Bench | Benjamin Sesko | FWD | 14 | 7.3 | 2.07 | 6.17 | 10.71 | 0.00 | 31.8 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.96 | 19.78 | 32.43 | 9.00 | 108.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 5.14 | 15.01 | 24.21 | 1.00 | 104.5 | 55.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.6 | 3.26 | 11.28 | 18.78 | 1.00 | 49.0 | 34.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.44 | 10.49 | 17.68 | 12.00 | 75.9 | 90.0 |
| Bench 2 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.63 | 8.26 | 14.45 | 1.00 | 43.3 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 0.30 -> 1.00
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 63.99
- Actual score: 80.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.54) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Benjamin Sesko -> Richarlison de Andrade (projected gain 2.44, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (6.54) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Caoimhín Kelleher replaced David Raya Martín.
- Autosub: Rayan Cherki replaced William Saliba.
- Autosub: Nikola Milenković replaced Nico O'Reilly.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martín | GK | 1 | 6.1 | 4.47 | 12.86 | 20.56 | 0.00 | 84.0 | 0.0 |
| Bench 1 | Autosub In | Caoimhín Kelleher | GK | 5 | 4.8 | 2.51 | 7.53 | 12.74 | 6.00 | 82.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.89 | 13.87 | 22.05 | 1.00 | 86.4 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.78 | 13.17 | 21.05 | 2.00 | 99.9 | 90.0 |
| XI | Bench | William Saliba | DEF | 1 | 6.2 | 4.03 | 11.80 | 18.68 | 0.00 | 78.5 | 0.0 |
| XI | Bench | Nico O'Reilly | DEF | 13 | 5.2 | 3.57 | 9.69 | 15.65 | 0.00 | 69.0 | 0.0 |
| Bench 3 | Autosub In | Nikola Milenković | DEF | 16 | 5.1 | 2.63 | 7.87 | 13.59 | 4.00 | 72.6 | 90.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.8 | 5.06 | 12.77 | 21.09 | 12.00 | 99.6 | 90.0 |
| XI | XI | Richarlison de Andrade | FWD | 18 | 6.5 | 4.77 | 12.65 | 19.23 | 2.00 | 81.7 | 72.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 3.77 | 11.76 | 19.67 | 2.00 | 77.8 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.54 | 19.26 | 32.07 | 14.00 | 106.7 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 4.73 | 12.80 | 21.05 | 6.00 | 81.5 | 57.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.29 | 12.01 | 19.93 | 2.00 | 89.7 | 64.0 |
| Bench 2 | Autosub In | Rayan Cherki | MID | 13 | 6.5 | 3.34 | 10.36 | 16.75 | 1.00 | 48.7 | 32.0 |
| Bench 4 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.58 | 8.10 | 15.21 | 0.00 | 50.1 | 0.0 |