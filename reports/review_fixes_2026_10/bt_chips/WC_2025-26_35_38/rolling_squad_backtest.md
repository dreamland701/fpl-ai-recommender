# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 250.83
- Total actual points: 237.00
- Average predicted points: 62.71
- Average actual points: 59.25
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
- Predicted score: 54.68
- Actual score: 40.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Virgil van Dijk replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.31 | 10.08 | 16.74 | 6.00 | 80.0 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.8 | 3.05 | 8.39 | 13.73 | 8.00 | 82.1 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.94 | 14.42 | 22.64 | 6.00 | 92.8 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 3.94 | 11.29 | 16.94 | 0.00 | 81.5 | 45.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 3.95 | 11.00 | 17.15 | 1.00 | 59.7 | 90.0 |
| Bench 2 | Autosub In | Virgil van Dijk | DEF | 12 | 6.2 | 3.30 | 10.93 | 18.65 | 1.00 | 72.8 | 90.0 |
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
- Bank: 0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Nico O'Reilly
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 67.93
- Actual score: 71.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (14.55) beats the best remaining Bench Boost opportunity (12.43).
- Transfer: Daniel Muñoz Mejía -> Marc Guéhi (projected gain 3.21, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (14.55) beats the best remaining Bench Boost opportunity (12.43).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.79 | 10.94 | 17.84 | 9.00 | 84.8 | 90.0 |
| Bench 1 | Bench Boost | Caoimhín Kelleher | GK | 5 | 4.8 | 2.38 | 7.88 | 13.19 | 3.00 | 77.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.20 | 14.89 | 23.50 | 11.00 | 94.1 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 5.33 | 13.15 | 20.30 | 15.00 | 114.8 | 180.0 |
| Vice Captain | XI | Nico O'Reilly | DEF | 13 | 5.2 | 5.35 | 12.65 | 18.94 | 5.00 | 99.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.47 | 12.51 | 20.21 | 2.00 | 82.7 | 90.0 |
| Bench 2 | Bench Boost | Nikola Milenković | DEF | 16 | 5.1 | 2.94 | 8.70 | 14.17 | 2.00 | 64.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.64 | 12.15 | 20.65 | 2.00 | 72.7 | 90.0 |
| Bench 3 | Bench Boost | Junior Kroupi | FWD | 4 | 4.6 | 2.78 | 8.44 | 13.66 | 2.00 | 54.8 | 78.0 |
| Bench 4 | Bench Boost | Mateus Mané | FWD | 20 | 4.2 | 2.67 | 7.93 | 11.81 | 2.00 | 70.4 | 66.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 7.08 | 20.83 | 34.00 | 3.00 | 104.3 | 90.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.67 | 13.56 | 20.94 | 0.00 | 89.0 | 0.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.0 | 4.27 | 12.80 | 21.94 | 0.00 | 44.4 | 0.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 2.95 | 10.36 | 18.19 | 0.00 | 41.8 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.32 | 9.64 | 16.05 | 12.00 | 61.5 | 90.0 |

## GW37

- Train rows: 189343
- Bank: 0.70 -> 0.50
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: wildcard
- Predicted score: 61.41
- Actual score: 55.00
- Transfer: none
- Chip used: Wildcard — full rebuild projects +22.39 squad value (threshold 12).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.1 | 4.74 | 12.41 | 19.76 | 6.00 | 86.2 | 90.0 |
| Bench 1 | Bench | Gianluigi Donnarumma | GK | 13 | 5.6 | 3.53 | 10.90 | 17.66 | 1.00 | 102.2 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.3 | 6.17 | 15.96 | 25.28 | 6.00 | 93.8 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.62 | 13.73 | 22.75 | 2.00 | 111.5 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.2 | 4.36 | 12.45 | 19.06 | 2.00 | 101.0 | 60.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.45 | 12.07 | 19.29 | 3.00 | 85.8 | 90.0 |
| XI | XI | Jaydee Canvot | DEF | 8 | 4.5 | 4.18 | 11.73 | 18.33 | 3.00 | 106.2 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.68 | 13.28 | 22.00 | 2.00 | 83.4 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 4.11 | 12.26 | 20.87 | 2.00 | 79.8 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.52 | 6.93 | 10.72 | 11.00 | 57.9 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.89 | 20.21 | 32.88 | 9.00 | 108.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 5.48 | 16.11 | 26.02 | 1.00 | 104.5 | 55.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.0 | 4.85 | 13.38 | 21.00 | 10.00 | 60.6 | 90.0 |
| Bench 2 | Bench | Dominik Szoboszlai | MID | 12 | 7.0 | 4.05 | 11.95 | 20.14 | 9.00 | 78.6 | 90.0 |
| Bench 3 | Bench | Mathias Jensen | MID | 5 | 4.9 | 3.90 | 11.43 | 18.36 | 2.00 | 83.9 | 62.0 |

## GW38

- Train rows: 190183
- Bank: 0.50 -> 0.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 66.81
- Actual score: 71.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.82) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: James Tarkowski -> Virgil van Dijk (projected gain 3.90, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (6.82) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Mateus Mané replaced Marc Guéhi.
- Autosub: Mathias Jensen replaced Bukayo Saka.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martín | GK | 1 | 6.1 | 4.30 | 12.10 | 19.20 | 0.00 | 84.0 | 0.0 |
| Bench 1 | Bench | Gianluigi Donnarumma | GK | 13 | 5.6 | 3.28 | 9.39 | 15.27 | 0.00 | 85.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.3 | 5.19 | 14.74 | 23.71 | 1.00 | 86.4 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 5.10 | 14.30 | 22.82 | 2.00 | 99.9 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 13 | 5.1 | 4.65 | 13.01 | 20.76 | 0.00 | 97.5 | 0.0 |
| Bench 2 | Bench | Maxence Lacroix | DEF | 8 | 5.2 | 3.21 | 9.93 | 15.70 | 0.00 | 75.0 | 0.0 |
| XI | Bench | Jaydee Canvot | DEF | 8 | 4.5 | 3.22 | 9.37 | 14.86 | 0.00 | 84.4 | 0.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.7 | 5.43 | 14.22 | 23.04 | 12.00 | 99.6 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 3.87 | 12.01 | 19.83 | 2.00 | 77.8 | 90.0 |
| Bench 3 | Autosub In | Mateus Mané | FWD | 20 | 4.2 | 3.12 | 8.29 | 13.14 | 2.00 | 67.2 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.82 | 20.26 | 33.40 | 14.00 | 106.7 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.06 | 14.24 | 23.00 | 6.00 | 81.5 | 57.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 10.0 | 4.61 | 14.02 | 22.07 | 0.00 | 63.4 | 0.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.92 | 13.74 | 22.74 | 2.00 | 90.7 | 90.0 |
| Bench 4 | Autosub In | Mathias Jensen | MID | 5 | 4.9 | 3.01 | 9.36 | 15.39 | 2.00 | 69.4 | 82.0 |