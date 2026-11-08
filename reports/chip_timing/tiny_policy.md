# Tiny chip policy vs planner (whole-half returns, chips only, forecast captain)

12 half-seasons; policy = 1445 parameters; 300 updates x 64 rollouts per half; greedy play at test time.

| Held-out half | Planner | Tiny policy | vs planner | Hindsight ceiling | Policy chips |
|---|---|---|---|---|---|
| 2020-21:1 | 1013 | 973 | -40 | 1102 | [(2, 'free_hit'), (7, 'bench_boost'), (10, 'triple_captain'), (15, 'wildcard')] |
| 2020-21:2 | 1129 | 1066 | -63 | 1201 | [(20, 'free_hit'), (25, 'bench_boost'), (26, 'triple_captain'), (29, 'wildcard')] |
| 2021-22:1 | 1000 | 1003 | +3 | 1093 | [(2, 'bench_boost'), (3, 'free_hit'), (4, 'triple_captain'), (13, 'wildcard')] |
| 2021-22:2 | 1095 | 1118 | +23 | 1306 | [(25, 'free_hit'), (26, 'wildcard'), (27, 'triple_captain'), (35, 'bench_boost')] |
| 2022-23:1 | 836 | 893 | +57 | 1092 | [(2, 'free_hit'), (10, 'triple_captain'), (11, 'bench_boost'), (12, 'wildcard')] |
| 2022-23:2 | 1078 | 1142 | +64 | 1284 | [(23, 'free_hit'), (25, 'bench_boost'), (27, 'triple_captain'), (28, 'wildcard')] |
| 2023-24:1 | 1074 | 1075 | +1 | 1112 | [(3, 'free_hit'), (10, 'bench_boost'), (13, 'triple_captain')] |
| 2023-24:2 | 1189 | 1149 | -40 | 1349 | [(21, 'free_hit'), (24, 'triple_captain'), (25, 'bench_boost'), (26, 'wildcard')] |
| 2024-25:1 | 1098 | 1115 | +17 | 1192 | [(2, 'bench_boost'), (3, 'triple_captain')] |
| 2024-25:2 | 1061 | 1135 | +74 | 1227 | [(24, 'bench_boost'), (25, 'wildcard'), (26, 'triple_captain')] |
| 2025-26:1 | 999 | 981 | -18 | 1097 | [(2, 'bench_boost'), (3, 'free_hit'), (5, 'wildcard'), (15, 'triple_captain')] |
| 2025-26:2 | 1206 | 1057 | -149 | 1297 | [(20, 'free_hit'), (21, 'bench_boost'), (22, 'wildcard'), (31, 'triple_captain')] |
| **total** | 12778 | 12707 | -71 | 14352 | |

G7b/G8 split (train on the other 10 halves): held-out 2361 vs planner 2395 (-34); 2025-26:2: 1088 chips [(20, 'bench_boost'), (22, 'wildcard'), (23, 'free_hit'), (24, 'triple_captain')]; 2023-24:2: 1273 chips [(20, 'bench_boost'), (21, 'wildcard'), (22, 'free_hit'), (24, 'triple_captain')]
