# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 204.68
- Total actual points: 263.00
- Average predicted points: 51.17
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
- Predicted score: 45.18
- Actual score: 46.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 2.81 | 8.98 | 14.34 | 6.00 | 80.0 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.8 | 2.65 | 7.19 | 11.73 | 8.00 | 82.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 3.94 | 11.82 | 18.54 | 6.00 | 92.8 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 3.25 | 9.60 | 14.65 | 1.00 | 59.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.1 | 3.20 | 9.59 | 14.88 | 6.00 | 80.3 | 90.0 |
| Bench 4 | Bench | Virgil van Dijk | DEF | 12 | 6.2 | 2.80 | 9.53 | 15.55 | 1.00 | 72.8 | 90.0 |
| XI | XI | Nikola Milenković | DEF | 16 | 5.1 | 3.11 | 9.29 | 14.65 | 1.00 | 78.6 | 45.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.06 | 12.37 | 19.81 | 6.00 | 82.0 | 90.0 |
| Bench 3 | Bench | Jarrod Bowen | FWD | 19 | 7.8 | 2.95 | 10.33 | 16.24 | 2.00 | 64.9 | 87.0 |
| Bench 2 | Bench | Benjamin Sesko | FWD | 14 | 7.3 | 2.98 | 8.68 | 13.89 | 5.00 | 71.5 | 45.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 4.81 | 15.14 | 26.23 | 5.00 | 102.0 | 90.0 |
| Vice Captain | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 4.10 | 12.55 | 19.62 | 4.00 | 70.9 | 20.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 3.48 | 11.40 | 17.02 | 4.00 | 91.3 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.89 | 11.24 | 17.76 | 1.00 | 81.0 | 45.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 3.73 | 11.06 | 17.87 | 1.00 | 73.5 | 90.0 |

## GW36

- Train rows: 188505
- Bank: 0.00 -> 1.00
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Rayan Cherki
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 57.97
- Actual score: 66.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (12.83) beats the best remaining Bench Boost opportunity (9.66).
- Transfer: Morgan Gibbs-White -> Rayan Cherki (projected gain 3.26, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (12.83) beats the best remaining Bench Boost opportunity (9.66).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.19 | 9.54 | 15.54 | 9.00 | 84.8 | 90.0 |
| Bench 1 | Bench Boost | Caoimhín Kelleher | GK | 5 | 4.8 | 1.88 | 6.18 | 10.29 | 3.00 | 77.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.10 | 11.79 | 18.40 | 11.00 | 94.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.57 | 10.61 | 17.01 | 2.00 | 82.7 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 4.15 | 9.95 | 14.94 | 5.00 | 99.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.1 | 3.56 | 9.75 | 15.38 | 5.00 | 81.1 | 90.0 |
| Bench 3 | Bench Boost | Nikola Milenković | DEF | 16 | 5.1 | 2.24 | 6.70 | 10.97 | 2.00 | 64.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.04 | 11.05 | 18.85 | 2.00 | 72.7 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 2.99 | 10.21 | 17.35 | 2.00 | 72.3 | 90.0 |
| Bench 4 | Bench Boost | Benjamin Sesko | FWD | 14 | 7.3 | 2.12 | 6.82 | 10.83 | 0.00 | 56.4 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 5.98 | 16.83 | 28.00 | 3.00 | 104.3 | 90.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.07 | 11.96 | 18.54 | 0.00 | 89.0 | 0.0 |
| Vice Captain | XI | Rayan Cherki | MID | 13 | 6.6 | 4.76 | 11.58 | 17.82 | 5.00 | 103.9 | 70.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 3.51 | 10.90 | 17.54 | 2.00 | 74.2 | 90.0 |
| Bench 2 | Bench Boost | Elliot Anderson | MID | 16 | 5.6 | 2.82 | 8.34 | 13.85 | 12.00 | 61.5 | 90.0 |

## GW37

- Train rows: 189343
- Bank: 1.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 47.62
- Actual score: 71.00
- Transfer: Morgan Rogers -> Antoine Semenyo (projected gain 3.60, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.74 | 9.11 | 14.46 | 6.00 | 86.2 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.8 | 2.85 | 8.26 | 13.85 | 2.00 | 86.0 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.07 | 12.86 | 20.18 | 6.00 | 93.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.25 | 10.09 | 16.81 | 14.00 | 83.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.1 | 3.74 | 9.26 | 14.46 | 8.00 | 83.0 | 90.0 |
| XI | XI | Nikola Milenković | DEF | 16 | 5.1 | 2.61 | 7.77 | 12.62 | 1.00 | 78.8 | 90.0 |
| Bench 3 | Bench | Nico O'Reilly | DEF | 13 | 5.2 | 1.93 | 6.87 | 11.99 | 2.00 | 49.3 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.08 | 11.78 | 19.50 | 2.00 | 83.4 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 3.41 | 10.16 | 17.17 | 2.00 | 79.8 | 90.0 |
| Bench 4 | Bench | Benjamin Sesko | FWD | 14 | 7.3 | 1.74 | 5.26 | 9.14 | 0.00 | 31.8 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 5.89 | 16.61 | 27.48 | 9.00 | 108.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 4.28 | 12.51 | 20.32 | 1.00 | 104.5 | 55.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.6 | 2.76 | 9.62 | 16.08 | 1.00 | 49.0 | 34.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 2.90 | 8.92 | 15.09 | 12.00 | 75.9 | 90.0 |
| Bench 2 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.25 | 7.13 | 12.49 | 1.00 | 43.3 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 0.30 -> 1.00
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 53.92
- Actual score: 80.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.52) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Benjamin Sesko -> Richarlison de Andrade (projected gain 2.26, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (5.52) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Caoimhín Kelleher replaced David Raya Martín.
- Autosub: Rayan Cherki replaced William Saliba.
- Autosub: Nikola Milenković replaced Nico O'Reilly.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martín | GK | 1 | 6.1 | 3.80 | 11.00 | 17.70 | 0.00 | 84.0 | 0.0 |
| Bench 1 | Autosub In | Caoimhín Kelleher | GK | 5 | 4.8 | 2.09 | 6.17 | 10.54 | 6.00 | 82.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.09 | 11.64 | 18.61 | 1.00 | 86.4 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.00 | 11.00 | 17.72 | 2.00 | 99.9 | 90.0 |
| XI | Bench | William Saliba | DEF | 1 | 6.2 | 3.38 | 9.95 | 15.84 | 0.00 | 78.5 | 0.0 |
| XI | Bench | Nico O'Reilly | DEF | 13 | 5.2 | 3.00 | 8.15 | 13.20 | 0.00 | 69.0 | 0.0 |
| Bench 4 | Autosub In | Nikola Milenković | DEF | 16 | 5.1 | 2.18 | 6.58 | 11.42 | 4.00 | 72.6 | 90.0 |
| XI | XI | Richarlison de Andrade | FWD | 18 | 6.5 | 4.06 | 10.77 | 16.41 | 2.00 | 81.7 | 72.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.8 | 4.23 | 10.62 | 17.74 | 12.00 | 99.6 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 3.17 | 9.91 | 16.73 | 2.00 | 77.8 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 5.52 | 16.26 | 27.40 | 14.00 | 106.7 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 3.96 | 10.64 | 17.70 | 6.00 | 81.5 | 57.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.66 | 10.18 | 17.00 | 2.00 | 89.7 | 64.0 |
| Bench 2 | Autosub In | Rayan Cherki | MID | 13 | 6.5 | 2.82 | 8.76 | 14.17 | 1.00 | 48.7 | 32.0 |
| Bench 3 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.21 | 6.90 | 13.06 | 0.00 | 50.1 | 0.0 |