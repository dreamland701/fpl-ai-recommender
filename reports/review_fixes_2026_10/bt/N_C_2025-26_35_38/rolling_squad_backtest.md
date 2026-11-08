# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 243.43
- Total actual points: 267.00
- Average predicted points: 60.86
- Average actual points: 66.75
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
- Predicted score: 54.28
- Actual score: 40.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Virgil van Dijk replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.49 | 10.52 | 17.26 | 6.00 | 82.6 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.8 | 3.18 | 8.67 | 14.00 | 8.00 | 83.0 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.14 | 14.88 | 23.17 | 6.00 | 95.6 | 90.0 |
| Bench 2 | Autosub In | Virgil van Dijk | DEF | 12 | 6.2 | 3.37 | 11.21 | 18.93 | 1.00 | 73.6 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 3.91 | 11.21 | 16.76 | 0.00 | 81.3 | 45.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 3.83 | 10.83 | 16.85 | 1.00 | 59.1 | 90.0 |
| XI | XI | Nikola Milenković | DEF | 16 | 5.1 | 3.42 | 10.23 | 16.15 | 1.00 | 78.5 | 45.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.84 | 14.09 | 23.44 | 6.00 | 83.4 | 90.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.3 | 2.57 | 7.13 | 10.96 | 2.00 | 60.2 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 1.74 | 5.70 | 10.21 | 6.00 | 33.7 | 69.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.42 | 19.43 | 32.48 | 5.00 | 102.6 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 14.0 | 4.21 | 14.38 | 24.55 | 0.00 | 61.0 | 0.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.43 | 13.10 | 20.23 | 4.00 | 91.4 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 4.05 | 12.95 | 21.44 | 4.00 | 70.4 | 20.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.10 | 12.04 | 19.19 | 1.00 | 79.9 | 45.0 |

## GW36

- Train rows: 188505
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Nico O'Reilly
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 69.08
- Actual score: 72.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (15.24) beats the best remaining Bench Boost opportunity (11.85).
- Transfer: Nikola Milenković -> Marc Guéhi (projected gain 4.54, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (15.24) beats the best remaining Bench Boost opportunity (11.85).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.95 | 11.33 | 18.32 | 9.00 | 87.6 | 90.0 |
| Bench 1 | Bench Boost | Caoimhín Kelleher | GK | 5 | 4.8 | 2.47 | 8.12 | 13.47 | 3.00 | 79.3 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.35 | 15.27 | 23.98 | 11.00 | 97.3 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 5.48 | 13.38 | 20.51 | 15.00 | 115.3 | 180.0 |
| Vice Captain | XI | Nico O'Reilly | DEF | 13 | 5.2 | 5.48 | 12.84 | 19.07 | 5.00 | 99.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.30 | 12.40 | 20.13 | 2.00 | 84.9 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 4.21 | 10.16 | 15.09 | 3.00 | 87.7 | 171.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.69 | 12.35 | 20.89 | 2.00 | 74.3 | 90.0 |
| Bench 3 | Bench Boost | Junior Kroupi | FWD | 4 | 4.6 | 2.89 | 8.72 | 13.97 | 2.00 | 56.0 | 78.0 |
| Bench 4 | Bench Boost | Mateus Mané | FWD | 20 | 4.2 | 2.69 | 7.99 | 11.82 | 2.00 | 70.7 | 66.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.92 | 20.67 | 33.83 | 3.00 | 106.0 | 90.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.33 | 13.03 | 20.20 | 0.00 | 88.6 | 0.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.0 | 4.11 | 12.77 | 21.96 | 0.00 | 45.5 | 0.0 |
| Bench 2 | Bench Boost | Morgan Gibbs-White | MID | 16 | 7.6 | 2.97 | 10.67 | 18.61 | 0.00 | 42.9 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.33 | 9.74 | 16.15 | 12.00 | 61.9 | 90.0 |

## GW37

- Train rows: 189343
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 55.78
- Actual score: 80.00
- Transfer: Nico O'Reilly -> Maxence Lacroix (projected gain 4.69, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.39 | 11.90 | 19.16 | 6.00 | 88.0 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.8 | 3.09 | 9.13 | 15.10 | 2.00 | 87.5 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.85 | 15.53 | 24.80 | 6.00 | 96.3 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.71 | 13.82 | 22.82 | 2.00 | 110.4 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.2 | 4.39 | 12.47 | 19.09 | 2.00 | 101.4 | 60.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 4.19 | 11.85 | 18.20 | 6.00 | 93.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.88 | 11.55 | 19.12 | 14.00 | 85.3 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.65 | 13.30 | 22.13 | 2.00 | 85.7 | 90.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.2 | 2.67 | 7.31 | 11.23 | 11.00 | 61.9 | 90.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 2.07 | 6.48 | 10.92 | 8.00 | 43.3 | 75.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 7.07 | 20.56 | 33.31 | 9.00 | 110.8 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.0 | 3.33 | 11.15 | 19.94 | 1.00 | 33.6 | 16.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.59 | 10.75 | 18.08 | 12.00 | 77.1 | 90.0 |
| Bench 4 | Bench | Morgan Gibbs-White | MID | 16 | 7.5 | 2.01 | 8.10 | 14.76 | 7.00 | 30.1 | 90.0 |
| Bench 2 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.65 | 8.03 | 13.92 | 1.00 | 44.1 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Virgil van Dijk
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 64.29
- Actual score: 75.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.99) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Maxence Lacroix -> Marcos Senesi Barón (projected gain 2.65, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (6.99) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Caoimhín Kelleher replaced David Raya Martín.
- Autosub: Junior Kroupi replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martín | GK | 1 | 6.1 | 4.07 | 11.80 | 18.93 | 0.00 | 87.2 | 0.0 |
| Bench 1 | Autosub In | Caoimhín Kelleher | GK | 5 | 4.8 | 2.60 | 8.34 | 13.91 | 6.00 | 83.3 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.00 | 14.40 | 23.40 | 1.00 | 90.1 | 45.0 |
| Vice Captain | XI | Virgil van Dijk | DEF | 12 | 6.1 | 5.17 | 14.38 | 22.94 | 2.00 | 101.2 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 13 | 5.1 | 4.52 | 12.79 | 20.50 | 0.00 | 96.7 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.2 | 4.45 | 12.77 | 20.65 | 2.00 | 93.3 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 3.75 | 10.86 | 17.33 | 1.00 | 84.6 | 45.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 3.92 | 11.98 | 19.85 | 2.00 | 79.5 | 90.0 |
| Bench 2 | Autosub In | Junior Kroupi | FWD | 4 | 4.6 | 3.14 | 8.87 | 14.37 | 2.00 | 63.5 | 72.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.2 | 3.00 | 8.39 | 13.33 | 2.00 | 68.3 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.99 | 20.53 | 33.75 | 14.00 | 109.4 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 4.28 | 12.52 | 20.98 | 9.00 | 74.2 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.30 | 12.39 | 20.30 | 2.00 | 89.7 | 64.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.0 | 3.86 | 12.03 | 20.75 | 6.00 | 40.6 | 73.0 |
| Bench 4 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.37 | 7.49 | 13.78 | 0.00 | 51.3 | 0.0 |