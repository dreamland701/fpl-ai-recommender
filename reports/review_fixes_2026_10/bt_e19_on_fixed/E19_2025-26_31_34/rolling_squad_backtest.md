# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 218.59
- Total actual points: 281.00
- Average predicted points: 54.65
- Average actual points: 70.25
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW30 are included before the first simulated week.
- League-average scores were not available for this run.

## GW31

- Train rows: 184363
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Anthony Gordon
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 57.39
- Actual score: 66.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Junior Kroupi replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez Romero | GK | 2 | 5.1 | 3.13 | 8.06 | 12.81 | 6.00 | 92.3 | 90.0 |
| Bench 1 | Bench | David Raya Martín | GK | 1 | 6.0 | 2.13 | 8.04 | 13.88 | 0.00 | 55.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.99 | 14.51 | 22.99 | 3.00 | 112.9 | 90.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 4.86 | 12.04 | 18.32 | 0.00 | 114.0 | 36.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 4.16 | 11.21 | 17.63 | 1.00 | 96.6 | 90.0 |
| Bench 2 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 2.88 | 10.58 | 18.76 | 0.00 | 59.3 | 0.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.08 | 9.34 | 14.89 | -1.00 | 86.6 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.81 | 12.87 | 20.73 | 4.00 | 101.6 | 90.0 |
| Bench 3 | Autosub In | Junior Kroupi | FWD | 4 | 4.7 | 2.50 | 6.84 | 10.51 | 5.00 | 70.2 | 17.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.5 | 0.81 | 3.67 | 7.99 | 0.00 | 21.7 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.41 | 18.71 | 30.33 | 13.00 | 125.8 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 14.0 | 4.55 | 14.72 | 24.91 | 0.00 | 79.7 | 0.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.76 | 14.54 | 22.92 | 3.00 | 102.3 | 90.0 |
| Vice Captain | XI | Anthony Gordon | MID | 15 | 7.3 | 5.79 | 14.27 | 21.23 | 10.00 | 111.4 | 88.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.45 | 11.83 | 18.85 | 9.00 | 92.7 | 86.0 |

## GW32

- Train rows: 185188
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jan Paul van Hecke
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 49.30
- Actual score: 72.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.11) beats the best remaining Bench Boost opportunity (14.75).
- Transfer: Malick Thiaw -> Jan Paul van Hecke (projected gain 2.80, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.11) beats the best remaining Bench Boost opportunity (14.75).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 2.61 | 7.77 | 13.12 | 1.00 | 71.4 | 90.0 |
| Bench 1 | Bench Boost | Emiliano Martínez Romero | GK | 2 | 5.1 | 2.11 | 6.34 | 10.26 | 0.00 | 80.3 | 0.0 |
| Vice Captain | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 4.11 | 10.51 | 16.05 | 5.00 | 95.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 3.34 | 10.35 | 17.86 | 4.00 | 73.6 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.24 | 9.87 | 15.49 | 3.00 | 96.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 2.33 | 9.12 | 15.27 | 9.00 | 70.5 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 2.45 | 8.00 | 12.87 | 4.00 | 84.9 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.38 | 11.34 | 17.67 | 13.00 | 81.1 | 90.0 |
| Bench 3 | Bench Boost | Junior Kroupi | FWD | 4 | 4.7 | 1.95 | 6.37 | 10.00 | 6.00 | 39.6 | 84.0 |
| Bench 4 | Bench Boost | Mateus Mané | FWD | 20 | 4.4 | 1.07 | 3.71 | 7.31 | 1.00 | 31.5 | 29.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 5.71 | 17.76 | 29.10 | 4.00 | 105.9 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.0 | 3.70 | 12.08 | 20.99 | 8.00 | 65.7 | 89.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 2.74 | 9.28 | 14.37 | 3.00 | 63.9 | 70.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 2.86 | 8.80 | 14.69 | 5.00 | 57.5 | 90.0 |
| Bench 2 | Bench Boost | Harry Wilson | MID | 10 | 6.0 | 1.98 | 7.76 | 13.18 | 2.00 | 60.2 | 79.0 |

## GW33

- Train rows: 186014
- Bank: 0.60 -> 1.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Marcos Senesi Barón
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 54.26
- Actual score: 93.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (9.51) beats the best remaining Triple Captain opportunity (4.96).
- Transfer: Harry Wilson -> Pascal Groß (projected gain 1.74, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (9.51) beats the best remaining Triple Captain opportunity (4.96).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 2.43 | 8.24 | 14.01 | 1.00 | 78.9 | 90.0 |
| Bench 1 | Bench | Emiliano Martínez Romero | GK | 2 | 5.1 | 1.40 | 3.91 | 6.54 | 2.00 | 60.2 | 90.0 |
| Vice Captain | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 5.21 | 11.72 | 16.97 | 6.00 | 146.8 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.07 | 10.41 | 17.39 | 8.00 | 83.1 | 90.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 4.54 | 9.86 | 14.25 | 12.00 | 129.7 | 180.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.97 | 8.79 | 13.52 | 5.00 | 131.9 | 180.0 |
| Bench 3 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 2.22 | 7.30 | 13.69 | 0.00 | 45.7 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.15 | 12.57 | 20.68 | 2.00 | 80.5 | 90.0 |
| XI | XI | Junior Kroupi | FWD | 4 | 4.6 | 3.39 | 7.44 | 11.79 | 10.00 | 73.3 | 137.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.3 | 1.37 | 4.69 | 8.58 | 1.00 | 39.7 | 52.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 5.26 | 16.85 | 29.24 | 6.00 | 87.4 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.0 | 4.29 | 13.37 | 23.07 | 10.00 | 73.4 | 90.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 4.46 | 10.04 | 15.02 | 16.00 | 103.5 | 180.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 2.95 | 8.91 | 14.89 | 5.00 | 58.7 | 90.0 |
| Bench 2 | Bench | Anthony Gordon | MID | 15 | 7.3 | 2.82 | 8.35 | 14.01 | 0.00 | 66.1 | 0.0 |

## GW34

- Train rows: 186843
- Bank: 1.10 -> 0.90
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Virgil van Dijk
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 57.65
- Actual score: 50.00
- Transfer: Anthony Gordon -> Morgan Gibbs-White (projected gain 7.49, hit 0)
- Autosub: Mateus Mané replaced Marcos Senesi Barón.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.30 | 11.69 | 18.11 | 10.00 | 105.3 | 90.0 |
| Bench 1 | Bench | Emiliano Martínez Romero | GK | 2 | 5.1 | 2.10 | 6.13 | 10.02 | 3.00 | 80.8 | 90.0 |
| Vice Captain | XI | Virgil van Dijk | DEF | 12 | 6.2 | 5.77 | 15.62 | 24.88 | 4.00 | 125.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.25 | 14.54 | 23.10 | 8.00 | 109.5 | 90.0 |
| XI | Bench | Marcos Senesi Barón | DEF | 4 | 5.1 | 2.75 | 9.76 | 16.43 | 0.00 | 81.1 | 0.0 |
| XI | Bench | Jan Paul van Hecke | DEF | 6 | 4.5 | 2.67 | 9.54 | 16.00 | 0.00 | 78.4 | 0.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.2 | 2.54 | 8.18 | 14.26 | 0.00 | 76.0 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.26 | 15.21 | 24.16 | 1.00 | 106.7 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 1.63 | 7.22 | 12.70 | 0.00 | 39.5 | 0.0 |
| Bench 3 | Autosub In | Mateus Mané | FWD | 20 | 4.3 | 1.89 | 5.27 | 8.17 | 2.00 | 44.8 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.63 | 18.83 | 31.30 | 5.00 | 122.9 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.0 | 5.63 | 16.18 | 27.35 | 1.00 | 105.6 | 58.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.5 | 5.44 | 15.55 | 24.89 | 13.00 | 109.1 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.64 | 12.78 | 20.32 | 1.00 | 95.3 | 90.0 |
| XI | Bench | Pascal Groß | MID | 6 | 5.5 | 2.65 | 11.87 | 19.74 | 0.00 | 77.4 | 0.0 |