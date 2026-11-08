# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 250.60
- Total actual points: 270.00
- Average predicted points: 62.65
- Average actual points: 67.50
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
- Bank: 100.00 -> 0.90
- Free transfers: 1 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Morgan Gibbs-White
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 57.57
- Actual score: 38.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Konstantinos Mavropanos replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.85 | 11.90 | 18.95 | 6.00 | 84.1 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.8 | 3.02 | 8.63 | 14.10 | 8.00 | 79.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.13 | 15.66 | 24.06 | 6.00 | 91.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 4.55 | 14.52 | 23.14 | 1.00 | 88.9 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.1 | 3.78 | 11.60 | 17.89 | 4.00 | 79.5 | 90.0 |
| Bench 2 | Autosub In | Konstantinos Mavropanos | DEF | 19 | 4.5 | 3.72 | 11.32 | 18.78 | -1.00 | 76.6 | 90.0 |
| XI | XI | Neco Williams | DEF | 16 | 4.8 | 3.74 | 11.26 | 18.12 | 1.00 | 78.6 | 45.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 4.80 | 14.93 | 23.68 | 2.00 | 85.2 | 87.0 |
| Bench 3 | Bench | Valentín Castellanos | FWD | 19 | 5.5 | 3.24 | 9.41 | 15.07 | 1.00 | 70.1 | 64.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.3 | 2.91 | 8.25 | 12.63 | 2.00 | 65.4 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.3 | 6.30 | 19.86 | 32.96 | 5.00 | 99.1 | 90.0 |
| Vice Captain | XI | Morgan Gibbs-White | MID | 16 | 7.5 | 5.23 | 15.80 | 25.25 | 4.00 | 83.5 | 20.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 14.0 | 4.80 | 15.29 | 24.85 | 0.00 | 71.8 | 0.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.7 | 4.68 | 13.99 | 21.56 | 4.00 | 98.3 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.40 | 12.83 | 20.42 | 1.00 | 83.3 | 45.0 |

## GW36

- Train rows: 188505
- Bank: 0.90 -> 0.60
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Marc Guéhi
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 70.62
- Actual score: 68.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (14.84) beats the best remaining Bench Boost opportunity (13.63).
- Transfer: Neco Williams -> Marc Guéhi (projected gain 4.58, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (14.84) beats the best remaining Bench Boost opportunity (13.63).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.97 | 11.45 | 19.13 | 9.00 | 87.0 | 90.0 |
| Bench 1 | Bench Boost | Caoimhín Kelleher | GK | 5 | 4.8 | 2.69 | 8.81 | 14.54 | 3.00 | 82.2 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.41 | 15.44 | 24.77 | 11.00 | 95.8 | 90.0 |
| Vice Captain | XI | Marc Guéhi | DEF | 13 | 5.1 | 5.76 | 14.28 | 22.45 | 15.00 | 119.4 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 4.75 | 13.02 | 21.63 | 2.00 | 89.5 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.1 | 4.29 | 11.62 | 18.96 | 1.00 | 87.7 | 90.0 |
| Bench 2 | Bench Boost | Konstantinos Mavropanos | DEF | 19 | 4.5 | 3.30 | 9.72 | 16.53 | 4.00 | 78.5 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 4.49 | 13.13 | 22.48 | 2.00 | 86.1 | 90.0 |
| Bench 4 | Bench Boost | Valentín Castellanos | FWD | 19 | 5.5 | 2.70 | 8.51 | 13.91 | 1.00 | 59.6 | 66.0 |
| Bench 3 | Bench Boost | Mateus Mané | FWD | 20 | 4.3 | 2.83 | 8.38 | 12.66 | 2.00 | 73.0 | 66.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.3 | 6.99 | 21.07 | 34.72 | 3.00 | 103.3 | 90.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.7 | 4.78 | 13.94 | 21.62 | 0.00 | 93.9 | 0.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.5 | 4.36 | 13.27 | 22.69 | 0.00 | 67.3 | 0.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.0 | 3.90 | 11.38 | 20.10 | 0.00 | 44.4 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.41 | 10.10 | 16.77 | 12.00 | 64.9 | 90.0 |

## GW37

- Train rows: 189343
- Bank: 0.60 -> 0.00
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 56.69
- Actual score: 65.00
- Transfer: Morgan Gibbs-White -> Antoine Semenyo (projected gain 8.41, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.66 | 12.43 | 20.06 | 6.00 | 87.0 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.8 | 3.27 | 9.55 | 15.84 | 2.00 | 87.1 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 6.07 | 16.32 | 26.17 | 6.00 | 93.9 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 5.00 | 14.93 | 24.78 | 2.00 | 116.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.87 | 11.88 | 19.88 | 14.00 | 84.1 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.1 | 4.11 | 11.85 | 18.86 | 0.00 | 82.1 | 90.0 |
| XI | XI | Konstantinos Mavropanos | DEF | 19 | 4.5 | 3.44 | 10.30 | 17.02 | 3.00 | 80.3 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 3.99 | 12.25 | 21.03 | 2.00 | 78.7 | 90.0 |
| Bench 4 | Bench | Valentín Castellanos | FWD | 19 | 5.5 | 2.54 | 7.68 | 12.84 | 6.00 | 54.8 | 64.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.58 | 7.37 | 11.54 | 11.00 | 59.1 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.3 | 6.69 | 19.82 | 32.58 | 9.00 | 103.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 5.66 | 16.88 | 27.47 | 1.00 | 107.1 | 55.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.70 | 11.29 | 19.01 | 12.00 | 81.6 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.0 | 2.81 | 9.60 | 17.44 | 1.00 | 28.2 | 16.0 |
| Bench 2 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.7 | 2.78 | 8.63 | 15.08 | 1.00 | 47.9 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 0.00 -> 4.00
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 65.72
- Actual score: 99.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.71) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Mohamed Salah -> Bukayo Saka (projected gain 5.72, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (6.71) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Caoimhín Kelleher replaced David Raya Martín.
- Autosub: Mateus Mané replaced Marc Guéhi.
- Autosub: Valentín Castellanos replaced Bukayo Saka.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martín | GK | 1 | 6.0 | 4.26 | 12.35 | 19.94 | 0.00 | 85.0 | 0.0 |
| Bench 1 | Autosub In | Caoimhín Kelleher | GK | 5 | 4.8 | 2.88 | 9.03 | 15.03 | 6.00 | 86.0 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.43 | 15.50 | 25.03 | 1.00 | 90.9 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.92 | 14.31 | 23.17 | 2.00 | 96.2 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 13 | 5.1 | 4.78 | 13.78 | 22.27 | 0.00 | 100.2 | 0.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.1 | 3.93 | 11.28 | 18.21 | 10.00 | 79.4 | 90.0 |
| XI | XI | Konstantinos Mavropanos | DEF | 19 | 4.5 | 3.89 | 10.95 | 17.66 | 8.00 | 85.2 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 4.20 | 11.82 | 19.92 | 12.00 | 80.6 | 90.0 |
| Bench 2 | Autosub In | Mateus Mané | FWD | 20 | 4.2 | 3.36 | 9.17 | 14.53 | 2.00 | 72.4 | 90.0 |
| Bench 3 | Autosub In | Valentín Castellanos | FWD | 19 | 5.5 | 3.20 | 8.53 | 13.91 | 8.00 | 57.6 | 87.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.3 | 6.71 | 20.17 | 33.50 | 14.00 | 103.2 | 90.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 10.0 | 5.10 | 14.85 | 23.15 | 0.00 | 74.2 | 0.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 5.06 | 14.62 | 23.79 | 6.00 | 82.0 | 57.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.00 | 12.10 | 20.17 | 2.00 | 90.6 | 64.0 |
| Bench 4 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.86 | 8.45 | 15.14 | 0.00 | 59.1 | 0.0 |