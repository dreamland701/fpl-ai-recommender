# Classic ridge with vs without ['chance_pre_deadline'], 84 walk-forward weeks

- 1GW (n 65505): base: RMSE 1.9491, MAE 0.9972, bias +0.011, top-decile actual 4.053 | mkt: RMSE 1.9488, MAE 0.9977, bias +0.013, top-decile actual 4.052
- 3GW (n 63824): base: RMSE 4.0189, MAE 2.3854, bias +0.031, top-decile actual 11.005 | mkt: RMSE 4.0156, MAE 2.3878, bias +0.044, top-decile actual 11.007
- 5GW (n 60494): base: RMSE 5.8840, MAE 3.6511, bias +0.045, top-decile actual 17.685 | mkt: RMSE 5.8763, MAE 3.6534, bias +0.068, top-decile actual 17.696
- Appearance AUC: base 0.9356 | mkt 0.9363
- 1GW GK+DEF (n 28754): RMSE base 1.8431 | mkt 1.8431
- 1GW MID+FWD (n 36491): RMSE base 1.9658 | mkt 1.9655
- 1GW price >= 10 (n 501): RMSE base 4.6445 | mkt 4.6420
- 1GW minutes_avg high (played 60+ this week) (n 16956): RMSE base 3.3846 | mkt 3.3838
- 1GW RMSE: market model better in 46/84 weeks

GK/DEF who played 60+, by market clean-sheet probability tercile: mean forecast (base / mkt) vs actual

| tercile | n | cs prob | base | mkt | actual |
|---|---|---|---|---|---|
| 1 | 0 | nan | nan | nan | nan |
| 2 | 0 | nan | nan | nan | nan |
| 3 | 8093 | 0.00 | 2.43 | 2.43 | 3.31 |

Mean standardized 1GW ridge coefficient of each market column across the 84 fits:

- chance_pre_deadline: +0.0763
