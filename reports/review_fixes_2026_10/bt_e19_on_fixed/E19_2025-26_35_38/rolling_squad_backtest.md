# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 199.40
- Total actual points: 257.00
- Average predicted points: 49.85
- Average actual points: 64.25
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
- Bank: 100.00 -> 0.40
- Free transfers: 1 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 44.55
- Actual score: 45.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 2.71 | 8.38 | 13.74 | 6.00 | 82.0 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.8 | 2.65 | 7.09 | 10.83 | 8.00 | 86.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 3.84 | 12.12 | 19.24 | 6.00 | 91.8 | 90.0 |
| Bench 4 | Bench | Virgil van Dijk | DEF | 12 | 6.2 | 2.40 | 9.73 | 15.55 | 1.00 | 72.8 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 3.34 | 9.49 | 14.14 | 0.00 | 85.5 | 45.0 |
| Bench 2 | Bench | William Saliba | DEF | 1 | 6.1 | 3.10 | 9.39 | 14.78 | 6.00 | 83.3 | 90.0 |
| XI | XI | Nikola Milenković | DEF | 16 | 5.1 | 3.11 | 9.29 | 14.25 | 1.00 | 81.6 | 45.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.06 | 12.67 | 21.01 | 6.00 | 86.0 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.8 | 3.15 | 10.23 | 17.34 | 2.00 | 66.9 | 87.0 |
| Bench 3 | Bench | Benjamin Sesko | FWD | 14 | 7.3 | 2.98 | 8.58 | 14.09 | 5.00 | 78.5 | 45.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 4.81 | 15.14 | 26.23 | 5.00 | 101.0 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 3.60 | 11.65 | 19.62 | 4.00 | 72.9 | 20.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 3.68 | 11.40 | 15.92 | 4.00 | 90.3 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.59 | 11.14 | 17.46 | 1.00 | 83.0 | 45.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.5 | 3.86 | 10.08 | 15.95 | 5.00 | 76.3 | 90.0 |

## GW36

- Train rows: 188505
- Bank: 0.40 -> 0.90
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Rayan Cherki
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 54.90
- Actual score: 64.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (12.46) beats the best remaining Bench Boost opportunity (9.38).
- Transfer: Daniel Muñoz Mejía -> Nico O'Reilly (projected gain 3.33, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (12.46) beats the best remaining Bench Boost opportunity (9.38).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 2.69 | 8.24 | 13.34 | 9.00 | 85.8 | 90.0 |
| Bench 1 | Bench Boost | Caoimhín Kelleher | GK | 5 | 4.8 | 1.78 | 6.58 | 11.09 | 3.00 | 80.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.00 | 12.29 | 19.50 | 11.00 | 93.1 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.3 | 4.15 | 10.15 | 15.24 | 5.00 | 119.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.47 | 10.01 | 16.21 | 2.00 | 82.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.1 | 2.76 | 8.55 | 13.58 | 5.00 | 83.1 | 90.0 |
| Bench 2 | Bench Boost | Nikola Milenković | DEF | 16 | 5.1 | 2.64 | 7.70 | 12.57 | 2.00 | 72.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.14 | 11.15 | 19.25 | 2.00 | 74.7 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 2.69 | 10.11 | 17.25 | 2.00 | 73.3 | 90.0 |
| Bench 3 | Bench Boost | Benjamin Sesko | FWD | 14 | 7.3 | 2.52 | 7.62 | 12.33 | 0.00 | 45.4 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 5.98 | 17.63 | 28.70 | 3.00 | 103.3 | 90.0 |
| Vice Captain | XI | Rayan Cherki | MID | 13 | 6.5 | 4.86 | 11.78 | 18.22 | 5.00 | 92.9 | 70.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 3.67 | 10.86 | 16.94 | 0.00 | 88.0 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 2.82 | 8.54 | 14.15 | 12.00 | 70.5 | 90.0 |
| Bench 4 | Bench Boost | Morgan Gibbs-White | MID | 16 | 7.6 | 1.75 | 6.36 | 12.19 | 0.00 | 21.8 | 0.0 |

## GW37

- Train rows: 189343
- Bank: 0.90 -> 0.30
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 46.72
- Actual score: 71.00
- Transfer: Morgan Gibbs-White -> Antoine Semenyo (projected gain 5.14, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.14 | 10.51 | 16.56 | 6.00 | 87.2 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.8 | 3.15 | 8.86 | 14.65 | 2.00 | 87.0 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.07 | 12.66 | 19.98 | 6.00 | 92.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.1 | 3.84 | 9.56 | 14.86 | 8.00 | 86.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.25 | 8.99 | 14.81 | 14.00 | 85.7 | 90.0 |
| XI | XI | Nikola Milenković | DEF | 16 | 5.1 | 2.61 | 7.97 | 13.02 | 1.00 | 81.8 | 90.0 |
| Bench 4 | Bench | Nico O'Reilly | DEF | 13 | 5.3 | 1.73 | 5.27 | 9.29 | 2.00 | 32.3 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.18 | 11.78 | 19.60 | 2.00 | 87.4 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 3.01 | 8.36 | 14.87 | 2.00 | 59.8 | 90.0 |
| Bench 3 | Bench | Benjamin Sesko | FWD | 14 | 7.3 | 1.84 | 5.56 | 9.64 | 0.00 | 21.8 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 5.59 | 16.81 | 27.18 | 9.00 | 97.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 4.18 | 12.21 | 20.02 | 1.00 | 94.5 | 55.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 2.80 | 8.52 | 14.49 | 12.00 | 78.9 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.5 | 2.46 | 8.12 | 13.68 | 1.00 | 48.0 | 34.0 |
| Bench 2 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.15 | 7.13 | 12.49 | 1.00 | 58.3 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 0.30 -> 0.50
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 53.23
- Actual score: 77.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.52) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Nikola Milenković -> Sven Botman (projected gain 2.58, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (5.52) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Caoimhín Kelleher replaced David Raya Martín.
- Autosub: Rayan Cherki replaced William Saliba.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martín | GK | 1 | 6.1 | 3.50 | 9.90 | 15.70 | 0.00 | 86.0 | 0.0 |
| Bench 1 | Autosub In | Caoimhín Kelleher | GK | 5 | 4.8 | 2.39 | 7.77 | 12.94 | 6.00 | 83.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 3.99 | 11.44 | 18.11 | 1.00 | 86.4 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.10 | 11.10 | 17.52 | 2.00 | 98.9 | 90.0 |
| XI | Bench | William Saliba | DEF | 1 | 6.2 | 3.68 | 10.45 | 16.24 | 0.00 | 80.5 | 0.0 |
| XI | XI | Sven Botman | DEF | 15 | 4.9 | 3.47 | 10.33 | 15.83 | 3.00 | 85.7 | 90.0 |
| XI | Bench | Nico O'Reilly | DEF | 13 | 5.3 | 3.00 | 8.45 | 13.60 | 0.00 | 75.0 | 0.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.8 | 4.63 | 11.82 | 18.94 | 12.00 | 102.6 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 2.97 | 9.71 | 15.93 | 2.00 | 78.8 | 90.0 |
| Bench 4 | Bench | Benjamin Sesko | FWD | 14 | 7.2 | 1.34 | 5.00 | 9.19 | 0.00 | 18.4 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 5.52 | 17.06 | 28.40 | 14.00 | 95.7 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 3.96 | 11.24 | 17.90 | 6.00 | 84.5 | 57.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.36 | 9.78 | 16.20 | 2.00 | 89.7 | 64.0 |
| Bench 2 | Autosub In | Rayan Cherki | MID | 13 | 6.5 | 2.62 | 7.76 | 12.97 | 1.00 | 59.7 | 32.0 |
| Bench 3 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.01 | 6.60 | 12.26 | 0.00 | 61.1 | 0.0 |