# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 244.07
- Total actual points: 258.00
- Average predicted points: 61.02
- Average actual points: 64.50
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
- Predicted score: 54.93
- Actual score: 40.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Virgil van Dijk replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.33 | 10.12 | 16.78 | 6.00 | 79.9 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.8 | 3.06 | 8.38 | 13.68 | 8.00 | 82.0 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.94 | 14.40 | 22.61 | 6.00 | 92.9 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 3.93 | 11.26 | 16.90 | 0.00 | 81.8 | 45.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 3.95 | 11.02 | 17.18 | 1.00 | 59.3 | 90.0 |
| Bench 2 | Autosub In | Virgil van Dijk | DEF | 12 | 6.2 | 3.34 | 10.97 | 18.67 | 1.00 | 72.7 | 90.0 |
| XI | XI | Nikola Milenković | DEF | 16 | 5.1 | 3.70 | 10.57 | 16.59 | 1.00 | 78.0 | 45.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.74 | 13.85 | 23.24 | 6.00 | 81.6 | 90.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.3 | 2.63 | 7.29 | 11.30 | 2.00 | 62.4 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 1.69 | 5.66 | 10.22 | 6.00 | 33.6 | 69.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.40 | 19.37 | 32.55 | 5.00 | 101.6 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 4.76 | 14.06 | 22.85 | 4.00 | 70.7 | 20.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 14.0 | 4.09 | 13.85 | 23.92 | 0.00 | 61.2 | 0.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.28 | 12.70 | 19.81 | 4.00 | 90.8 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.40 | 12.47 | 19.77 | 1.00 | 80.4 | 45.0 |

## GW36

- Train rows: 188505
- Bank: 0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Nico O'Reilly
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 68.28
- Actual score: 71.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (14.58) beats the best remaining Bench Boost opportunity (12.48).
- Transfer: Daniel Muñoz Mejía -> Marc Guéhi (projected gain 3.23, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (14.58) beats the best remaining Bench Boost opportunity (12.48).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.82 | 10.99 | 17.89 | 9.00 | 84.8 | 90.0 |
| Bench 1 | Bench Boost | Caoimhín Kelleher | GK | 5 | 4.8 | 2.39 | 7.87 | 13.14 | 3.00 | 77.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.21 | 14.89 | 23.50 | 11.00 | 94.2 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 5.33 | 13.15 | 20.30 | 15.00 | 114.3 | 180.0 |
| Vice Captain | XI | Nico O'Reilly | DEF | 13 | 5.2 | 5.37 | 12.70 | 19.00 | 5.00 | 99.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.51 | 12.55 | 20.23 | 2.00 | 82.6 | 90.0 |
| Bench 2 | Bench Boost | Nikola Milenković | DEF | 16 | 5.1 | 2.93 | 8.68 | 14.11 | 2.00 | 63.5 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.72 | 12.33 | 20.88 | 2.00 | 72.3 | 90.0 |
| Bench 3 | Bench Boost | Junior Kroupi | FWD | 4 | 4.6 | 2.80 | 8.46 | 13.67 | 2.00 | 54.8 | 78.0 |
| Bench 4 | Bench Boost | Mateus Mané | FWD | 20 | 4.2 | 2.68 | 7.97 | 11.89 | 2.00 | 70.6 | 66.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 7.18 | 21.06 | 34.31 | 3.00 | 104.0 | 90.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.67 | 13.58 | 20.93 | 0.00 | 88.3 | 0.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.0 | 4.16 | 12.51 | 21.55 | 0.00 | 45.1 | 0.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 3.01 | 10.48 | 18.33 | 0.00 | 41.6 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.33 | 9.66 | 16.05 | 12.00 | 60.9 | 90.0 |

## GW37

- Train rows: 189343
- Bank: 0.70 -> 0.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 55.86
- Actual score: 74.00
- Transfer: Morgan Gibbs-White -> Antoine Semenyo (projected gain 8.81, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.77 | 12.45 | 19.81 | 6.00 | 86.2 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.8 | 3.27 | 9.35 | 15.29 | 2.00 | 85.9 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 6.18 | 15.97 | 25.28 | 6.00 | 93.9 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.61 | 13.72 | 22.73 | 2.00 | 110.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.89 | 11.45 | 18.96 | 14.00 | 83.5 | 90.0 |
| XI | XI | Nikola Milenković | DEF | 16 | 5.1 | 3.00 | 9.25 | 15.06 | 1.00 | 78.2 | 90.0 |
| Bench 3 | Bench | Nico O'Reilly | DEF | 13 | 5.2 | 2.44 | 8.02 | 13.95 | 2.00 | 48.7 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.77 | 13.46 | 22.24 | 2.00 | 83.0 | 90.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.2 | 2.53 | 6.97 | 10.79 | 11.00 | 58.1 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 2.05 | 6.67 | 11.24 | 8.00 | 44.9 | 75.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.99 | 20.43 | 33.19 | 9.00 | 108.3 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 5.54 | 16.26 | 26.23 | 1.00 | 103.7 | 55.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.0 | 3.18 | 10.66 | 19.26 | 1.00 | 32.5 | 16.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.41 | 10.43 | 17.68 | 12.00 | 75.3 | 90.0 |
| Bench 2 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.45 | 7.74 | 13.59 | 1.00 | 42.7 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 0.10 -> -0.00
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 65.00
- Actual score: 73.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.92) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Nikola Milenković -> Marcos Senesi Barón (projected gain 4.56, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (6.92) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Caoimhín Kelleher replaced David Raya Martín.
- Autosub: Mateus Mané replaced Marc Guéhi.
- Autosub: Junior Kroupi replaced Nico O'Reilly.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martín | GK | 1 | 6.1 | 4.34 | 12.16 | 19.26 | 0.00 | 83.9 | 0.0 |
| Bench 1 | Autosub In | Caoimhín Kelleher | GK | 5 | 4.8 | 2.70 | 8.45 | 13.98 | 6.00 | 82.5 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.21 | 14.77 | 23.74 | 1.00 | 86.4 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 5.14 | 14.36 | 22.87 | 2.00 | 99.7 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 13 | 5.1 | 4.65 | 12.99 | 20.72 | 0.00 | 97.0 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.2 | 4.47 | 12.87 | 20.82 | 2.00 | 94.2 | 90.0 |
| XI | Bench | Nico O'Reilly | DEF | 13 | 5.2 | 3.61 | 9.87 | 16.02 | 0.00 | 68.4 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 3.95 | 12.17 | 20.02 | 2.00 | 77.5 | 90.0 |
| Bench 3 | Autosub In | Junior Kroupi | FWD | 4 | 4.6 | 3.13 | 9.00 | 14.59 | 2.00 | 64.4 | 72.0 |
| Bench 2 | Autosub In | Mateus Mané | FWD | 20 | 4.2 | 3.13 | 8.33 | 13.20 | 2.00 | 67.4 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.92 | 20.50 | 33.71 | 14.00 | 106.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.11 | 14.38 | 23.20 | 6.00 | 80.8 | 57.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.07 | 11.89 | 19.69 | 2.00 | 89.1 | 64.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.0 | 3.70 | 11.68 | 20.25 | 6.00 | 39.8 | 73.0 |
| Bench 4 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.30 | 7.40 | 13.65 | 0.00 | 49.5 | 0.0 |