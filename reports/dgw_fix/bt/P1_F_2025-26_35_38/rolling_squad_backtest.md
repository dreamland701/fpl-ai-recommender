# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 257.28
- Total actual points: 264.00
- Average predicted points: 64.32
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
- Predicted score: 55.94
- Actual score: 40.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Virgil van Dijk replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.45 | 10.08 | 16.74 | 6.00 | 81.8 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.8 | 3.03 | 8.39 | 13.73 | 8.00 | 81.9 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.12 | 14.42 | 22.64 | 6.00 | 90.0 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 3.93 | 11.29 | 16.94 | 0.00 | 81.2 | 45.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 3.84 | 11.00 | 17.15 | 1.00 | 57.8 | 90.0 |
| Bench 2 | Autosub In | Virgil van Dijk | DEF | 12 | 6.2 | 3.62 | 10.93 | 18.65 | 1.00 | 78.2 | 90.0 |
| XI | XI | Nikola Milenković | DEF | 16 | 5.1 | 3.83 | 10.59 | 16.65 | 1.00 | 82.0 | 45.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.71 | 13.67 | 23.01 | 6.00 | 83.1 | 90.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.3 | 2.73 | 7.26 | 11.23 | 2.00 | 64.7 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 1.63 | 5.65 | 10.22 | 6.00 | 33.1 | 69.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.41 | 19.14 | 32.23 | 5.00 | 90.0 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 14.0 | 4.44 | 14.13 | 24.30 | 0.00 | 63.2 | 0.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 4.91 | 13.95 | 22.72 | 4.00 | 76.5 | 20.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.43 | 12.70 | 19.82 | 4.00 | 90.0 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.46 | 12.44 | 19.76 | 1.00 | 83.0 | 45.0 |

## GW36

- Train rows: 188505
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Marc Guéhi
- Vice captain: Nico O'Reilly
- Effective captain: Marc Guéhi
- Chip used: triple_captain
- Predicted score: 75.96
- Actual score: 96.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (11.31) beats the best remaining Triple Captain opportunity (8.80).
- Chip advisory: triple_captain (0.62): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Nikola Milenković -> Marc Guéhi (projected gain 3.31, hit 0)
- Chip used: Triple Captain on Marc Guéhi. Optimizer chose Triple Captain here because the current estimated captain upside (11.31) beats the best remaining Triple Captain opportunity (8.80).
- Autosub: Junior Kroupi replaced Carlos Henrique Casimiro.
- Autosub: Mateus Mané replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.78 | 10.94 | 17.84 | 9.00 | 83.8 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.8 | 2.43 | 7.88 | 13.19 | 3.00 | 79.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.26 | 14.89 | 23.50 | 11.00 | 90.0 | 90.0 |
| Captain | Captain | Marc Guéhi | DEF | 13 | 5.1 | 8.21 | 13.15 | 20.30 | 15.00 | 180.0 | 180.0 |
| Vice Captain | XI | Nico O'Reilly | DEF | 13 | 5.2 | 7.87 | 12.65 | 18.94 | 5.00 | 145.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.66 | 12.51 | 20.21 | 2.00 | 86.1 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 6.24 | 10.17 | 15.16 | 3.00 | 118.8 | 171.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.85 | 12.15 | 20.65 | 2.00 | 76.6 | 90.0 |
| Bench 3 | Autosub In | Junior Kroupi | FWD | 4 | 4.6 | 2.73 | 8.44 | 13.66 | 2.00 | 55.0 | 78.0 |
| Bench 4 | Autosub In | Mateus Mané | FWD | 20 | 4.2 | 2.70 | 7.93 | 11.81 | 2.00 | 71.2 | 66.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 7.17 | 20.83 | 34.00 | 3.00 | 90.0 | 90.0 |
| XI | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.82 | 13.56 | 20.94 | 0.00 | 90.0 | 0.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 14.0 | 4.29 | 12.80 | 21.94 | 0.00 | 43.0 | 0.0 |
| Bench 2 | Bench | Morgan Gibbs-White | MID | 16 | 7.6 | 3.13 | 10.36 | 18.19 | 0.00 | 46.7 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.37 | 9.64 | 16.05 | 12.00 | 63.0 | 90.0 |

## GW37

- Train rows: 189343
- Bank: 0.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 56.43
- Actual score: 74.00
- Transfer: Morgan Gibbs-White -> Declan Rice (projected gain 4.72, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.80 | 12.41 | 19.76 | 6.00 | 87.2 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.8 | 3.30 | 9.36 | 15.35 | 2.00 | 87.0 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 6.27 | 15.96 | 25.28 | 6.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.74 | 13.73 | 22.75 | 2.00 | 90.0 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 4.31 | 11.80 | 18.11 | 6.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.95 | 11.39 | 18.91 | 14.00 | 85.2 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 2.50 | 7.97 | 13.89 | 2.00 | 51.9 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.68 | 13.28 | 22.00 | 2.00 | 83.9 | 90.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.47 | 6.93 | 10.72 | 11.00 | 56.9 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 2.07 | 6.65 | 11.23 | 8.00 | 46.4 | 75.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.89 | 20.21 | 32.88 | 9.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 4.63 | 12.17 | 19.72 | 5.00 | 76.8 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.0 | 3.30 | 10.94 | 19.65 | 1.00 | 30.1 | 16.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.46 | 10.42 | 17.69 | 12.00 | 77.5 | 90.0 |
| Bench 2 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.47 | 7.73 | 13.59 | 1.00 | 43.1 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 0.30 -> 0.30
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 68.95
- Actual score: 54.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.36) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Nico O'Reilly -> Marcos Senesi Barón (projected gain 3.00, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.36) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.1 | 4.38 | 12.10 | 19.20 | 0.00 | 84.9 | 0.0 |
| Bench 1 | Bench Boost | Caoimhín Kelleher | GK | 5 | 4.8 | 2.76 | 8.47 | 14.04 | 6.00 | 83.8 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.35 | 14.74 | 23.71 | 1.00 | 88.5 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 5.14 | 14.30 | 22.82 | 2.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.70 | 13.01 | 20.76 | 0.00 | 90.0 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.2 | 4.41 | 12.85 | 20.83 | 2.00 | 90.0 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 3.63 | 10.60 | 17.00 | 1.00 | 84.0 | 45.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 4.04 | 12.01 | 19.83 | 2.00 | 80.5 | 90.0 |
| Bench 3 | Bench Boost | Junior Kroupi | FWD | 4 | 4.6 | 3.06 | 8.98 | 14.59 | 2.00 | 64.2 | 72.0 |
| Bench 2 | Bench Boost | Mateus Mané | FWD | 20 | 4.2 | 3.12 | 8.29 | 13.14 | 2.00 | 68.1 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.83 | 20.26 | 33.40 | 14.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 4.45 | 12.79 | 20.37 | 0.00 | 79.8 | 0.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.0 | 3.79 | 11.91 | 20.56 | 6.00 | 37.0 | 73.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.05 | 11.88 | 19.70 | 2.00 | 90.0 | 64.0 |
| Bench 4 | Bench Boost | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.42 | 7.40 | 13.66 | 0.00 | 51.8 | 0.0 |