# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 227.81
- Total actual points: 245.00
- Average predicted points: 56.95
- Average actual points: 61.25
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW26 are included before the first simulated week.
- League-average scores were not available for this run.

## GW27

- Train rows: 181084
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Cole Palmer
- Vice captain: Antoine Semenyo
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 56.79
- Actual score: 40.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Mateus Mané replaced Florian Wirtz.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.84 | 11.25 | 17.68 | 3.00 | 114.5 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 2.80 | 9.04 | 14.10 | 2.00 | 117.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 4.92 | 15.62 | 24.20 | 2.00 | 114.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.04 | 11.72 | 19.20 | 11.00 | 98.8 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 3.92 | 10.78 | 16.10 | 2.00 | 94.7 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.8 | 3.76 | 10.61 | 16.20 | 2.00 | 87.2 | 90.0 |
| Bench 4 | Bench | Hugo Bueno López | DEF | 20 | 4.3 | 3.18 | 9.93 | 15.67 | 4.00 | 108.2 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 4.40 | 12.90 | 20.38 | 2.00 | 97.7 | 90.0 |
| Bench 3 | Bench | Jarrod Bowen | FWD | 19 | 7.6 | 3.46 | 11.50 | 19.30 | 4.00 | 85.5 | 90.0 |
| Bench 2 | Autosub In | Mateus Mané | FWD | 20 | 4.6 | 3.75 | 10.65 | 15.66 | 2.00 | 119.4 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.6 | 6.42 | 16.75 | 26.75 | 3.00 | 90.3 | 74.0 |
| XI | XI | Declan Rice | MID | 1 | 7.6 | 5.41 | 15.83 | 25.21 | 4.00 | 113.7 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.47 | 14.96 | 24.41 | 4.00 | 104.3 | 86.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.40 | 12.96 | 20.77 | 2.00 | 89.7 | 90.0 |
| XI | Bench | Florian Wirtz | MID | 12 | 8.4 | 3.80 | 12.67 | 22.51 | 0.00 | 87.8 | 0.0 |

## GW28

- Train rows: 181902
- Bank: 0.00 -> 2.50
- Free transfers: 2 -> 2
- Captain: Declan Rice
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Declan Rice
- Chip used: none
- Predicted score: 51.86
- Actual score: 71.00
- Transfer: Florian Wirtz -> Harry Wilson (projected gain 2.45, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.34 | 10.02 | 16.11 | 3.00 | 94.8 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 2.31 | 6.31 | 10.75 | 8.00 | 95.2 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 4.81 | 13.82 | 21.90 | 9.00 | 110.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.65 | 12.03 | 18.88 | 7.00 | 102.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 3.74 | 11.10 | 17.15 | 6.00 | 86.0 | 90.0 |
| Bench 3 | Bench | Hugo Bueno López | DEF | 20 | 4.3 | 3.09 | 9.06 | 13.83 | 6.00 | 97.8 | 90.0 |
| Bench 4 | Bench | Trevoh Chalobah | DEF | 7 | 5.7 | 2.35 | 8.16 | 13.27 | 1.00 | 75.3 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.6 | 3.81 | 12.75 | 20.59 | 7.00 | 87.2 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 4.39 | 11.84 | 19.30 | 6.00 | 92.3 | 90.0 |
| Bench 2 | Bench | Mateus Mané | FWD | 20 | 4.6 | 3.12 | 9.89 | 14.94 | 2.00 | 95.8 | 90.0 |
| Captain | Captain | Declan Rice | MID | 1 | 7.6 | 4.91 | 14.87 | 23.22 | 5.00 | 101.3 | 75.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.68 | 12.90 | 21.45 | 2.00 | 84.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 4.70 | 12.88 | 20.93 | 8.00 | 74.8 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 3.59 | 12.29 | 19.89 | 1.00 | 72.0 | 85.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.32 | 12.27 | 18.55 | 12.00 | 91.4 | 71.0 |

## GW29

- Train rows: 182721
- Bank: 2.50 -> 0.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Antoine Semenyo
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 57.37
- Actual score: 69.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.56) beats the best remaining Triple Captain opportunity (6.83).
- Transfer: Morgan Rogers -> Bruno Borges Fernandes (projected gain 6.19, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (5.56) beats the best remaining Triple Captain opportunity (6.83).
- Autosub: Mateus Mané replaced Harry Wilson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.29 | 9.20 | 15.35 | 7.00 | 97.5 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 1.94 | 5.47 | 9.53 | 3.00 | 93.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 4.13 | 13.12 | 21.16 | 11.00 | 114.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.19 | 12.05 | 18.57 | 1.00 | 90.1 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.14 | 11.57 | 18.32 | 1.00 | 92.4 | 90.0 |
| Bench 4 | Bench | Trevoh Chalobah | DEF | 7 | 5.6 | 2.88 | 8.98 | 14.45 | 2.00 | 82.8 | 90.0 |
| XI | XI | Hugo Bueno López | DEF | 20 | 4.3 | 3.06 | 8.53 | 13.12 | 1.00 | 96.3 | 11.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.17 | 13.06 | 21.28 | 2.00 | 86.5 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 4.02 | 12.35 | 21.93 | 4.00 | 89.4 | 90.0 |
| Bench 2 | Autosub In | Mateus Mané | FWD | 20 | 4.6 | 3.03 | 8.39 | 12.58 | 2.00 | 91.5 | 69.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.0 | 5.56 | 16.03 | 26.00 | 8.00 | 97.1 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 8.1 | 5.32 | 14.81 | 23.81 | 7.00 | 88.9 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.32 | 14.81 | 25.02 | 9.00 | 81.5 | 84.0 |
| XI | Bench | Harry Wilson | MID | 10 | 5.9 | 4.04 | 11.22 | 17.67 | 0.00 | 82.1 | 0.0 |
| Bench 3 | Bench | Declan Rice | MID | 1 | 7.5 | 2.92 | 11.06 | 18.43 | 3.00 | 69.8 | 90.0 |

## GW30

- Train rows: 183541
- Bank: 0.10 -> 0.50
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Antoine Semenyo
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 61.79
- Actual score: 65.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.36) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Harry Wilson -> Elliot Anderson (projected gain 3.27, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.36) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.51 | 9.91 | 16.18 | 7.00 | 94.2 | 90.0 |
| Bench 1 | Bench Boost | José Malheiro de Sá | GK | 20 | 4.2 | 1.95 | 5.58 | 8.92 | 0.00 | 86.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 3.99 | 11.98 | 18.74 | 2.00 | 83.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 4.22 | 11.45 | 19.61 | 9.00 | 98.6 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 3.31 | 10.08 | 16.13 | 2.00 | 87.5 | 90.0 |
| Bench 2 | Bench Boost | Trevoh Chalobah | DEF | 7 | 5.6 | 3.11 | 8.43 | 13.39 | 2.00 | 84.2 | 90.0 |
| Bench 4 | Bench Boost | Hugo Bueno López | DEF | 20 | 4.3 | 1.92 | 6.22 | 10.31 | 1.00 | 48.3 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.28 | 11.70 | 18.95 | 6.00 | 92.4 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 3.77 | 11.35 | 18.55 | 6.00 | 90.2 | 90.0 |
| Bench 3 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 2.38 | 6.35 | 10.71 | 1.00 | 73.8 | 45.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.0 | 5.46 | 16.28 | 26.93 | 10.00 | 100.9 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.83 | 15.75 | 25.74 | 2.00 | 83.6 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 8.1 | 5.38 | 15.64 | 24.80 | 2.00 | 104.3 | 74.0 |
| XI | XI | Declan Rice | MID | 1 | 7.4 | 4.01 | 11.67 | 19.26 | 3.00 | 87.0 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.5 | 4.20 | 11.58 | 18.20 | 2.00 | 89.5 | 87.0 |