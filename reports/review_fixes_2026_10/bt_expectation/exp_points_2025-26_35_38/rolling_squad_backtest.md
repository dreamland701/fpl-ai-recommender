# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 239.86
- Total actual points: 264.00
- Average predicted points: 59.96
- Average actual points: 66.00
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
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 52.93
- Actual score: 47.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.38 | 9.68 | 15.26 | 6.00 | 80.0 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.8 | 3.21 | 8.03 | 12.10 | 8.00 | 82.1 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.65 | 12.61 | 19.38 | 6.00 | 92.8 | 90.0 |
| Bench 4 | Bench | Virgil van Dijk | DEF | 12 | 6.2 | 3.46 | 10.61 | 16.55 | 1.00 | 72.8 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 4.02 | 10.55 | 15.22 | 1.00 | 59.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.1 | 3.81 | 10.50 | 15.33 | 6.00 | 80.3 | 90.0 |
| Bench 2 | Bench | Nikola Milenković | DEF | 16 | 5.1 | 3.59 | 10.18 | 14.81 | 1.00 | 78.6 | 45.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.43 | 12.60 | 20.85 | 6.00 | 82.0 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.8 | 3.64 | 11.18 | 17.35 | 2.00 | 64.9 | 87.0 |
| Bench 3 | Bench | Benjamin Sesko | FWD | 14 | 7.3 | 3.49 | 9.89 | 14.27 | 5.00 | 71.5 | 45.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 5.85 | 16.56 | 26.44 | 5.00 | 102.0 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 4.51 | 13.27 | 20.55 | 4.00 | 70.9 | 20.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.33 | 11.82 | 17.92 | 1.00 | 81.0 | 45.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.33 | 11.72 | 17.90 | 4.00 | 91.3 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.14 | 11.54 | 18.31 | 1.00 | 73.5 | 90.0 |

## GW36

- Train rows: 188505
- Bank: 0.00 -> 1.00
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Rayan Cherki
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 68.54
- Actual score: 66.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (15.07) beats the best remaining Bench Boost opportunity (12.35).
- Transfer: Morgan Gibbs-White -> Rayan Cherki (projected gain 1.75, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (15.07) beats the best remaining Bench Boost opportunity (12.35).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.76 | 10.65 | 15.63 | 9.00 | 84.8 | 90.0 |
| Bench 1 | Bench Boost | Caoimhín Kelleher | GK | 5 | 4.8 | 2.30 | 7.12 | 10.46 | 3.00 | 77.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.87 | 13.53 | 18.72 | 11.00 | 94.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.27 | 11.43 | 17.18 | 2.00 | 82.7 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 5.28 | 11.43 | 15.00 | 5.00 | 99.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.1 | 3.81 | 11.07 | 15.44 | 5.00 | 81.1 | 90.0 |
| Bench 3 | Bench Boost | Nikola Milenković | DEF | 16 | 5.1 | 2.93 | 7.71 | 11.03 | 2.00 | 64.0 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 3.65 | 11.35 | 17.45 | 2.00 | 72.3 | 90.0 |
| Bench 2 | Bench Boost | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.31 | 11.20 | 19.12 | 2.00 | 72.7 | 90.0 |
| Bench 4 | Bench Boost | Benjamin Sesko | FWD | 14 | 7.3 | 2.76 | 7.44 | 11.02 | 0.00 | 56.4 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.78 | 19.12 | 28.05 | 3.00 | 104.3 | 90.0 |
| Vice Captain | XI | Rayan Cherki | MID | 13 | 6.6 | 6.05 | 12.94 | 17.87 | 5.00 | 103.9 | 70.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.39 | 12.70 | 18.59 | 0.00 | 89.0 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.20 | 11.53 | 17.80 | 2.00 | 74.2 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.39 | 9.28 | 14.05 | 12.00 | 61.5 | 90.0 |

## GW37

- Train rows: 189343
- Bank: 1.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 55.48
- Actual score: 71.00
- Transfer: Morgan Rogers -> Antoine Semenyo (projected gain 3.76, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.81 | 10.06 | 14.60 | 6.00 | 86.2 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.8 | 3.46 | 8.89 | 13.74 | 2.00 | 86.0 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 6.03 | 13.70 | 20.31 | 6.00 | 93.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.82 | 10.50 | 16.85 | 14.00 | 83.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.1 | 4.72 | 9.90 | 14.49 | 8.00 | 83.0 | 90.0 |
| XI | XI | Nikola Milenković | DEF | 16 | 5.1 | 2.89 | 8.85 | 12.71 | 1.00 | 78.8 | 90.0 |
| Bench 2 | Bench | Nico O'Reilly | DEF | 13 | 5.2 | 2.62 | 7.05 | 12.12 | 2.00 | 49.3 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.33 | 11.65 | 19.68 | 2.00 | 83.4 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 4.06 | 10.87 | 17.49 | 2.00 | 79.8 | 90.0 |
| Bench 4 | Bench | Benjamin Sesko | FWD | 14 | 7.3 | 1.99 | 5.34 | 9.25 | 0.00 | 31.8 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.52 | 17.09 | 27.38 | 9.00 | 108.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 5.03 | 13.27 | 20.54 | 1.00 | 104.5 | 55.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.6 | 3.24 | 10.27 | 16.12 | 1.00 | 49.0 | 34.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.51 | 9.72 | 15.20 | 12.00 | 75.9 | 90.0 |
| Bench 3 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.61 | 7.34 | 12.74 | 1.00 | 43.3 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 0.30 -> 1.00
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 62.92
- Actual score: 80.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.31) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Benjamin Sesko -> Richarlison de Andrade (projected gain 2.34, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (6.31) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Caoimhín Kelleher replaced David Raya Martín.
- Autosub: Rayan Cherki replaced William Saliba.
- Autosub: Nikola Milenković replaced Nico O'Reilly.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martín | GK | 1 | 6.1 | 4.22 | 11.50 | 17.78 | 0.00 | 84.0 | 0.0 |
| Bench 1 | Autosub In | Caoimhín Kelleher | GK | 5 | 4.8 | 2.71 | 6.64 | 10.56 | 6.00 | 82.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.69 | 12.11 | 18.80 | 1.00 | 86.4 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.87 | 11.60 | 17.74 | 2.00 | 99.9 | 90.0 |
| XI | Bench | William Saliba | DEF | 1 | 6.2 | 4.18 | 10.23 | 15.94 | 0.00 | 78.5 | 0.0 |
| XI | Bench | Nico O'Reilly | DEF | 13 | 5.2 | 3.86 | 9.01 | 13.60 | 0.00 | 69.0 | 0.0 |
| Bench 3 | Autosub In | Nikola Milenković | DEF | 16 | 5.1 | 2.92 | 6.64 | 11.61 | 4.00 | 72.6 | 90.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.8 | 5.07 | 11.35 | 17.87 | 12.00 | 99.6 | 90.0 |
| XI | XI | Richarlison de Andrade | FWD | 18 | 6.5 | 4.37 | 11.27 | 16.58 | 2.00 | 81.7 | 72.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 3.72 | 10.28 | 16.59 | 2.00 | 77.8 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.31 | 17.06 | 27.48 | 14.00 | 106.7 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 4.84 | 11.34 | 17.78 | 6.00 | 81.5 | 57.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.16 | 11.32 | 17.14 | 2.00 | 89.7 | 64.0 |
| Bench 2 | Autosub In | Rayan Cherki | MID | 13 | 6.5 | 3.43 | 9.20 | 14.66 | 1.00 | 48.7 | 32.0 |
| Bench 4 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.24 | 7.23 | 13.19 | 0.00 | 50.1 | 0.0 |