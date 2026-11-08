# Honest Backtest Report

- Train seasons: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25
- Test window: 2025-26 GW1-GW30
- Train rows: 161277
- Test rows: 23086

## Summary Metrics

| Metric | Model | Baseline | Baseline Name |
| --- | ---: | ---: | --- |
| points_1gw_rmse | 2.0281 | 2.2176 | points_avg_3 |
| minutes_rmse | 24.4833 | 24.5636 | minutes_avg_3 |

## By Position

| Position | Samples | Points 1GW RMSE | Minutes RMSE |
| --- | ---: | ---: | ---: |
| GK | 2657 | 1.5625 | 19.8412 |
| DEF | 7582 | 2.2026 | 27.1495 |
| MID | 10313 | 1.9820 | 24.0148 |
| FWD | 2534 | 2.1003 | 22.2657 |

## Notes

- This report uses a time-based split: train on seasons strictly before the test window.
- GW31 of 2025-26 remains excluded from both training and backtests.
- Metrics below are holdout-set RMSE values, not training-set fit statistics.
- The current feature set includes ICT/bonus/BPS across all seasons plus xG/xA/xGI/xGC/starts/defensive contribution when the raw source provides them.