# Classic ridge with vs without ['status_flag_pre_deadline', 'news_flag_pre_deadline'], 84 walk-forward weeks

- 1GW (n 65505): base: RMSE 1.9592, MAE 0.9906, bias -0.012, top-decile actual 4.001 | mkt: RMSE 1.9491, MAE 0.9972, bias +0.011, top-decile actual 4.053
- 3GW (n 63824): base: RMSE 4.0481, MAE 2.3798, bias -0.021, top-decile actual 10.919 | mkt: RMSE 4.0189, MAE 2.3854, bias +0.031, top-decile actual 11.005
- 5GW (n 60494): base: RMSE 5.9256, MAE 3.6481, bias -0.028, top-decile actual 17.612 | mkt: RMSE 5.8840, MAE 3.6511, bias +0.045, top-decile actual 17.685
- Appearance AUC: base 0.9307 | mkt 0.9356
- 1GW GK+DEF (n 28754): RMSE base 1.8486 | mkt 1.8431
- 1GW MID+FWD (n 36491): RMSE base 1.9732 | mkt 1.9658
- 1GW price >= 10 (n 501): RMSE base 4.7419 | mkt 4.6445
- 1GW minutes_avg high (played 60+ this week) (n 16956): RMSE base 3.3967 | mkt 3.3846
- 1GW RMSE: market model better in 58/84 weeks

GK/DEF who played 60+, by market clean-sheet probability tercile: mean forecast (base / mkt) vs actual

| tercile | n | cs prob | base | mkt | actual |
|---|---|---|---|---|---|
| 1 | 0 | nan | nan | nan | nan |
| 2 | 0 | nan | nan | nan | nan |
| 3 | 8093 | 0.00 | 2.41 | 2.43 | 3.31 |

Mean standardized 1GW ridge coefficient of each market column across the 84 fits:

- status_flag_pre_deadline: -0.4359
- news_flag_pre_deadline: +0.1973
