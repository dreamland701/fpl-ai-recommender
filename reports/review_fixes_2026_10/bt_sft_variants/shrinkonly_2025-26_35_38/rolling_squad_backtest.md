# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 204.69
- Total actual points: 258.00
- Average predicted points: 51.17
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
- Predicted score: 46.11
- Actual score: 40.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Virgil van Dijk replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 2.78 | 8.51 | 13.99 | 6.00 | 80.0 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.8 | 2.57 | 7.01 | 11.35 | 8.00 | 82.1 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.17 | 12.38 | 19.16 | 6.00 | 92.8 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 3.32 | 9.59 | 14.16 | 0.00 | 81.5 | 45.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 3.33 | 9.33 | 14.34 | 1.00 | 59.7 | 90.0 |
| Bench 2 | Autosub In | Virgil van Dijk | DEF | 12 | 6.2 | 2.78 | 9.28 | 15.66 | 1.00 | 72.8 | 90.0 |
| XI | XI | Nikola Milenković | DEF | 16 | 5.1 | 3.13 | 8.97 | 13.91 | 1.00 | 78.6 | 45.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 3.93 | 11.72 | 19.48 | 6.00 | 82.0 | 90.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.3 | 2.20 | 6.00 | 9.16 | 2.00 | 62.2 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 1.40 | 4.56 | 8.27 | 6.00 | 33.6 | 69.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 5.32 | 16.59 | 27.55 | 5.00 | 102.0 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 14.0 | 3.54 | 12.12 | 20.61 | 0.00 | 60.5 | 0.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 3.96 | 11.96 | 19.22 | 4.00 | 70.9 | 20.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 3.61 | 10.85 | 16.68 | 4.00 | 91.3 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.70 | 10.62 | 16.63 | 1.00 | 81.0 | 45.0 |

## GW36

- Train rows: 188505
- Bank: 0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Nico O'Reilly
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 57.06
- Actual score: 71.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (12.84) beats the best remaining Bench Boost opportunity (10.45).
- Transfer: Daniel Muñoz Mejía -> Marc Guéhi (projected gain 2.82, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (12.84) beats the best remaining Bench Boost opportunity (10.45).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.18 | 9.25 | 15.14 | 9.00 | 84.8 | 90.0 |
| Bench 1 | Bench Boost | Caoimhín Kelleher | GK | 5 | 4.8 | 2.00 | 6.59 | 11.07 | 3.00 | 77.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.37 | 12.67 | 20.09 | 11.00 | 94.1 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.48 | 11.17 | 17.29 | 15.00 | 114.8 | 180.0 |
| Vice Captain | XI | Nico O'Reilly | DEF | 13 | 5.2 | 4.49 | 10.73 | 16.10 | 5.00 | 99.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.76 | 10.61 | 17.21 | 2.00 | 82.7 | 90.0 |
| Bench 2 | Bench Boost | Nikola Milenković | DEF | 16 | 5.1 | 2.48 | 7.31 | 11.93 | 2.00 | 64.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.06 | 10.30 | 17.60 | 2.00 | 72.7 | 90.0 |
| Bench 3 | Bench Boost | Junior Kroupi | FWD | 4 | 4.6 | 2.34 | 7.08 | 11.48 | 2.00 | 54.8 | 78.0 |
| Bench 4 | Bench Boost | Mateus Mané | FWD | 20 | 4.2 | 2.25 | 6.64 | 9.87 | 2.00 | 70.4 | 66.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 5.94 | 17.83 | 29.26 | 3.00 | 104.3 | 90.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 3.92 | 11.52 | 17.85 | 0.00 | 89.0 | 0.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.0 | 3.59 | 10.86 | 18.73 | 0.00 | 44.4 | 0.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 2.48 | 8.74 | 15.44 | 0.00 | 41.8 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 2.79 | 8.12 | 13.57 | 12.00 | 61.5 | 90.0 |

## GW37

- Train rows: 189343
- Bank: 0.70 -> 0.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 46.87
- Actual score: 74.00
- Transfer: Morgan Gibbs-White -> Antoine Semenyo (projected gain 7.28, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.00 | 10.51 | 16.85 | 6.00 | 86.2 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.8 | 2.75 | 7.96 | 13.12 | 2.00 | 86.0 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.21 | 13.48 | 21.50 | 6.00 | 93.8 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 3.90 | 11.61 | 19.37 | 2.00 | 111.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.25 | 9.66 | 16.12 | 14.00 | 83.7 | 90.0 |
| XI | XI | Nikola Milenković | DEF | 16 | 5.1 | 2.54 | 7.89 | 12.93 | 1.00 | 78.8 | 90.0 |
| Bench 3 | Bench | Nico O'Reilly | DEF | 13 | 5.2 | 2.05 | 6.80 | 11.89 | 2.00 | 49.3 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.95 | 11.24 | 18.74 | 2.00 | 83.4 | 90.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.2 | 2.12 | 5.93 | 9.21 | 11.00 | 57.9 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 1.71 | 5.69 | 9.64 | 8.00 | 44.9 | 75.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 5.81 | 17.04 | 27.93 | 9.00 | 108.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 4.63 | 13.61 | 22.13 | 1.00 | 104.5 | 55.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.0 | 2.78 | 9.29 | 16.76 | 1.00 | 31.8 | 16.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 2.87 | 8.85 | 15.09 | 12.00 | 75.9 | 90.0 |
| Bench 2 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.06 | 6.60 | 11.63 | 1.00 | 43.3 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 0.10 -> -0.00
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 54.66
- Actual score: 73.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.79) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Nikola Milenković -> Marcos Senesi Barón (projected gain 3.94, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (5.79) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Caoimhín Kelleher replaced David Raya Martín.
- Autosub: Mateus Mané replaced Marc Guéhi.
- Autosub: Junior Kroupi replaced Nico O'Reilly.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martín | GK | 1 | 6.1 | 3.64 | 10.24 | 16.34 | 0.00 | 84.0 | 0.0 |
| Bench 1 | Autosub In | Caoimhín Kelleher | GK | 5 | 4.8 | 2.26 | 7.11 | 11.84 | 6.00 | 82.5 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.40 | 12.51 | 20.27 | 1.00 | 86.4 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.32 | 12.14 | 19.50 | 2.00 | 99.9 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 13 | 5.1 | 3.94 | 11.02 | 17.70 | 0.00 | 97.5 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.2 | 3.76 | 10.89 | 17.76 | 2.00 | 94.3 | 90.0 |
| XI | Bench | Nico O'Reilly | DEF | 13 | 5.2 | 3.04 | 8.30 | 13.54 | 0.00 | 69.0 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 3.27 | 10.16 | 16.89 | 2.00 | 77.8 | 90.0 |
| Bench 3 | Autosub In | Junior Kroupi | FWD | 4 | 4.6 | 2.62 | 7.55 | 12.32 | 2.00 | 64.5 | 72.0 |
| Bench 2 | Autosub In | Mateus Mané | FWD | 20 | 4.2 | 2.63 | 6.96 | 11.05 | 2.00 | 67.2 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 5.79 | 17.27 | 28.72 | 14.00 | 106.7 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 4.29 | 12.08 | 19.65 | 6.00 | 81.5 | 57.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.0 | 3.21 | 10.08 | 17.53 | 6.00 | 39.2 | 73.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.43 | 10.05 | 16.78 | 2.00 | 89.7 | 64.0 |
| Bench 4 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 1.93 | 6.19 | 11.50 | 0.00 | 50.1 | 0.0 |