# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 238.16
- Total actual points: 254.00
- Average predicted points: 59.54
- Average actual points: 63.50
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
- Predicted score: 54.03
- Actual score: 40.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Nico O'Reilly replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.31 | 10.08 | 16.74 | 6.00 | 80.0 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.8 | 3.05 | 8.39 | 13.73 | 8.00 | 82.1 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.94 | 14.42 | 22.64 | 6.00 | 92.8 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 3.94 | 11.29 | 16.94 | 0.00 | 81.5 | 45.0 |
| Bench 2 | Autosub In | Nico O'Reilly | DEF | 13 | 5.2 | 3.95 | 11.00 | 17.15 | 1.00 | 59.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 3.30 | 10.93 | 18.65 | 1.00 | 72.8 | 90.0 |
| XI | XI | Nikola Milenković | DEF | 16 | 5.1 | 3.71 | 10.59 | 16.65 | 1.00 | 78.6 | 45.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.66 | 13.67 | 23.01 | 6.00 | 82.0 | 90.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.3 | 2.62 | 7.26 | 11.23 | 2.00 | 62.2 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 1.67 | 5.65 | 10.22 | 6.00 | 33.6 | 69.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.31 | 19.14 | 32.23 | 5.00 | 102.0 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 14.0 | 4.20 | 14.13 | 24.30 | 0.00 | 60.5 | 0.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 4.70 | 13.95 | 22.72 | 4.00 | 70.9 | 20.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.28 | 12.70 | 19.82 | 4.00 | 91.3 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.39 | 12.44 | 19.76 | 1.00 | 81.0 | 45.0 |

## GW36

- Train rows: 188505
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 66.86
- Actual score: 64.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (14.10) beats the best remaining Bench Boost opportunity (12.55).
- Transfer: Daniel Muñoz Mejía -> Marcos Senesi Barón (projected gain 11.48, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (14.10) beats the best remaining Bench Boost opportunity (12.55).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.79 | 10.94 | 17.84 | 9.00 | 84.8 | 90.0 |
| Bench 1 | Bench Boost | Caoimhín Kelleher | GK | 5 | 4.8 | 2.38 | 7.88 | 13.19 | 3.00 | 77.8 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.20 | 14.89 | 23.50 | 11.00 | 94.1 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 5.35 | 12.65 | 18.94 | 5.00 | 99.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.47 | 12.51 | 20.21 | 2.00 | 82.7 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.2 | 4.26 | 12.37 | 19.87 | 8.00 | 89.2 | 90.0 |
| XI | XI | Nikola Milenković | DEF | 16 | 5.1 | 2.94 | 8.70 | 14.17 | 2.00 | 64.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.64 | 12.15 | 20.65 | 2.00 | 72.7 | 90.0 |
| Bench 3 | Bench Boost | Junior Kroupi | FWD | 4 | 4.6 | 2.78 | 8.44 | 13.66 | 2.00 | 54.8 | 78.0 |
| Bench 2 | Bench Boost | Mateus Mané | FWD | 20 | 4.2 | 2.67 | 7.93 | 11.81 | 2.00 | 70.4 | 66.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 7.08 | 20.83 | 34.00 | 3.00 | 104.3 | 90.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.67 | 13.56 | 20.94 | 0.00 | 89.0 | 0.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.0 | 4.27 | 12.80 | 21.94 | 0.00 | 44.4 | 0.0 |
| Bench 4 | Bench Boost | Morgan Gibbs-White | MID | 16 | 7.6 | 2.95 | 10.36 | 18.19 | 0.00 | 41.8 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.32 | 9.64 | 16.05 | 12.00 | 61.5 | 90.0 |

## GW37

- Train rows: 189343
- Bank: 0.60 -> 0.00
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 53.41
- Actual score: 77.00
- Transfer: Morgan Gibbs-White -> Antoine Semenyo (projected gain 26.12, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.74 | 12.41 | 19.76 | 6.00 | 86.2 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.8 | 3.25 | 9.36 | 15.35 | 2.00 | 86.0 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 6.17 | 15.96 | 25.28 | 6.00 | 93.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.85 | 11.39 | 18.91 | 14.00 | 83.7 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.2 | 3.36 | 10.36 | 18.09 | 4.00 | 72.9 | 90.0 |
| XI | XI | Nikola Milenković | DEF | 16 | 5.1 | 3.01 | 9.27 | 15.12 | 1.00 | 78.8 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 2.43 | 7.97 | 13.89 | 2.00 | 49.3 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.68 | 13.28 | 22.00 | 2.00 | 83.4 | 90.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.2 | 2.52 | 6.93 | 10.72 | 11.00 | 57.9 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 2.03 | 6.65 | 11.23 | 8.00 | 44.9 | 75.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.89 | 20.21 | 32.88 | 9.00 | 108.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 5.48 | 16.11 | 26.02 | 1.00 | 104.5 | 55.0 |
| Bench 3 | Bench | Mohamed Salah | MID | 12 | 14.0 | 3.30 | 10.94 | 19.65 | 1.00 | 31.8 | 16.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.40 | 10.42 | 17.69 | 12.00 | 75.9 | 90.0 |
| Bench 2 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.45 | 7.73 | 13.59 | 1.00 | 43.3 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 63.86
- Actual score: 73.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.82) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Nikola Milenković -> Marc Guéhi (projected gain 10.61, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (6.82) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Caoimhín Kelleher replaced David Raya Martín.
- Autosub: Junior Kroupi replaced Marc Guéhi.
- Autosub: Mohamed Salah replaced Nico O'Reilly.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martín | GK | 1 | 6.1 | 4.30 | 12.10 | 19.20 | 0.00 | 84.0 | 0.0 |
| Bench 1 | Autosub In | Caoimhín Kelleher | GK | 5 | 4.8 | 2.69 | 8.47 | 14.04 | 6.00 | 82.5 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.19 | 14.74 | 23.71 | 1.00 | 86.4 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 5.10 | 14.30 | 22.82 | 2.00 | 99.9 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 13 | 5.1 | 4.65 | 13.01 | 20.76 | 0.00 | 97.5 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.2 | 4.44 | 12.85 | 20.83 | 2.00 | 94.3 | 90.0 |
| XI | Bench | Nico O'Reilly | DEF | 13 | 5.2 | 3.60 | 9.85 | 16.00 | 0.00 | 69.0 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 3.87 | 12.01 | 19.83 | 2.00 | 77.8 | 90.0 |
| Bench 2 | Autosub In | Junior Kroupi | FWD | 4 | 4.6 | 3.11 | 8.98 | 14.59 | 2.00 | 64.5 | 72.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.2 | 3.12 | 8.29 | 13.14 | 2.00 | 67.2 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.82 | 20.26 | 33.40 | 14.00 | 106.7 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.06 | 14.24 | 23.00 | 6.00 | 81.5 | 57.0 |
| Bench 3 | Autosub In | Mohamed Salah | MID | 12 | 14.0 | 3.80 | 11.91 | 20.56 | 6.00 | 39.2 | 73.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.06 | 11.88 | 19.70 | 2.00 | 89.7 | 64.0 |
| Bench 4 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.31 | 7.40 | 13.66 | 0.00 | 50.1 | 0.0 |