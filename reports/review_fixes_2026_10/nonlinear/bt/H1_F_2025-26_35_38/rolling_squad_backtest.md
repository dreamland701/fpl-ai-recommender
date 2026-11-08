# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 235.74
- Total actual points: 233.00
- Average predicted points: 58.94
- Average actual points: 58.25
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
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 51.24
- Actual score: 42.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martín | GK | 1 | 6.0 | 3.24 | 10.08 | 16.74 | 6.00 | 88.0 | 90.0 |
| XI | XI | Caoimhín Kelleher | GK | 5 | 4.8 | 4.01 | 8.39 | 13.73 | 8.00 | 87.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.41 | 14.42 | 22.64 | 6.00 | 87.2 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 4.00 | 11.29 | 16.94 | 0.00 | 85.3 | 45.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 3.31 | 11.00 | 17.15 | 1.00 | 83.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 3.24 | 10.93 | 18.65 | 1.00 | 74.6 | 90.0 |
| XI | XI | Nikola Milenković | DEF | 16 | 5.1 | 3.33 | 10.59 | 16.65 | 1.00 | 78.6 | 45.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.65 | 13.67 | 23.01 | 6.00 | 83.9 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.3 | 2.34 | 7.26 | 11.23 | 2.00 | 35.2 | 90.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 2.73 | 5.65 | 10.22 | 6.00 | 63.6 | 69.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.07 | 19.14 | 32.23 | 5.00 | 87.1 | 90.0 |
| Bench 2 | Bench | Mohamed Salah | MID | 12 | 14.0 | 2.91 | 14.13 | 24.30 | 0.00 | 43.8 | 0.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 4.04 | 13.95 | 22.72 | 4.00 | 70.8 | 20.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.04 | 12.70 | 19.82 | 4.00 | 81.2 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.06 | 12.44 | 19.76 | 1.00 | 83.6 | 45.0 |

## GW36

- Train rows: 188505
- Bank: 0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Nico O'Reilly
- Vice captain: Marc Guéhi
- Effective captain: Nico O'Reilly
- Chip used: triple_captain
- Predicted score: 66.94
- Actual score: 75.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (11.06) beats the best remaining Triple Captain opportunity (7.18).
- Chip advisory: triple_captain (0.67): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Daniel Muñoz Mejía -> Marc Guéhi (projected gain 2.98, hit 0)
- Chip used: Triple Captain on Nico O'Reilly. Optimizer chose Triple Captain here because the current estimated captain upside (11.06) beats the best remaining Triple Captain opportunity (7.18).
- Autosub: Nikola Milenković replaced Carlos Henrique Casimiro.
- Autosub: Mateus Mané replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.87 | 10.94 | 17.84 | 9.00 | 91.8 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.8 | 2.18 | 7.88 | 13.19 | 3.00 | 87.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.61 | 14.89 | 23.50 | 11.00 | 86.7 | 90.0 |
| Vice Captain | XI | Marc Guéhi | DEF | 13 | 5.1 | 5.88 | 13.15 | 20.30 | 15.00 | 147.5 | 180.0 |
| Captain | Captain | Nico O'Reilly | DEF | 13 | 5.2 | 8.31 | 12.65 | 18.94 | 5.00 | 159.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.88 | 12.51 | 20.21 | 2.00 | 84.7 | 90.0 |
| Bench 2 | Autosub In | Nikola Milenković | DEF | 16 | 5.1 | 2.60 | 8.70 | 14.17 | 2.00 | 58.4 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.42 | 12.15 | 20.65 | 2.00 | 86.2 | 90.0 |
| XI | XI | Junior Kroupi | FWD | 4 | 4.6 | 3.51 | 8.44 | 13.66 | 2.00 | 64.9 | 78.0 |
| Bench 4 | Autosub In | Mateus Mané | FWD | 20 | 4.2 | 2.20 | 7.93 | 11.81 | 2.00 | 75.2 | 66.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 5.85 | 20.83 | 34.00 | 3.00 | 86.5 | 90.0 |
| XI | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.04 | 13.56 | 20.94 | 0.00 | 82.3 | 0.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 14.0 | 3.22 | 12.80 | 21.94 | 0.00 | 32.7 | 0.0 |
| Bench 3 | Bench | Morgan Gibbs-White | MID | 16 | 7.6 | 2.51 | 10.36 | 18.19 | 0.00 | 23.1 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.72 | 9.64 | 16.05 | 12.00 | 65.3 | 90.0 |

## GW37

- Train rows: 189343
- Bank: 0.70 -> 0.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 51.78
- Actual score: 65.00
- Transfer: Morgan Gibbs-White -> Antoine Semenyo (projected gain 9.41, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 5.24 | 12.41 | 19.76 | 6.00 | 88.1 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.8 | 3.00 | 9.36 | 15.35 | 2.00 | 88.7 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.65 | 15.96 | 25.28 | 6.00 | 83.5 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 3.33 | 13.73 | 22.75 | 2.00 | 85.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.38 | 11.39 | 18.91 | 14.00 | 87.0 | 90.0 |
| XI | XI | Nikola Milenković | DEF | 16 | 5.1 | 2.66 | 9.27 | 15.12 | 1.00 | 82.0 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 3.40 | 7.97 | 13.89 | 2.00 | 73.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.69 | 13.28 | 22.00 | 2.00 | 83.2 | 90.0 |
| Bench 2 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.56 | 6.93 | 10.72 | 11.00 | 47.1 | 90.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 2.49 | 6.65 | 11.23 | 8.00 | 65.2 | 75.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.11 | 20.21 | 32.88 | 9.00 | 87.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 4.17 | 16.11 | 26.02 | 1.00 | 79.3 | 55.0 |
| Bench 4 | Bench | Mohamed Salah | MID | 12 | 14.0 | 1.37 | 10.94 | 19.65 | 1.00 | 23.8 | 16.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.41 | 10.42 | 17.69 | 12.00 | 80.7 | 90.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 3.61 | 7.73 | 13.59 | 1.00 | 78.4 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 0.10 -> -0.00
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Mohamed Salah
- Effective captain: Antoine Semenyo
- Chip used: bench_boost
- Predicted score: 65.79
- Actual score: 51.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (12.90) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Nikola Milenković -> Marcos Senesi Barón (projected gain 4.61, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (12.90) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.1 | 3.76 | 12.10 | 19.20 | 0.00 | 89.7 | 0.0 |
| Bench 1 | Bench Boost | Caoimhín Kelleher | GK | 5 | 4.8 | 3.02 | 8.47 | 14.04 | 6.00 | 86.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.02 | 14.74 | 23.71 | 1.00 | 84.1 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.15 | 14.30 | 22.82 | 2.00 | 86.3 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.54 | 13.01 | 20.76 | 0.00 | 85.3 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.2 | 3.71 | 12.85 | 20.83 | 2.00 | 85.3 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 4.21 | 9.85 | 16.00 | 0.00 | 81.5 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 4.23 | 12.01 | 19.83 | 2.00 | 84.1 | 90.0 |
| Bench 3 | Bench Boost | Junior Kroupi | FWD | 4 | 4.6 | 3.24 | 8.98 | 14.59 | 2.00 | 75.5 | 72.0 |
| Bench 2 | Bench Boost | Mateus Mané | FWD | 20 | 4.2 | 3.62 | 8.29 | 13.14 | 2.00 | 76.3 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 4.65 | 20.26 | 33.40 | 14.00 | 86.3 | 90.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.0 | 5.29 | 14.24 | 23.00 | 6.00 | 69.8 | 57.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.0 | 5.27 | 11.91 | 20.56 | 6.00 | 60.0 | 73.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.77 | 11.88 | 19.70 | 2.00 | 83.0 | 64.0 |
| Bench 4 | Bench Boost | Carlos Henrique Casimiro | MID | 14 | 5.8 | 3.03 | 7.40 | 13.66 | 0.00 | 51.8 | 0.0 |