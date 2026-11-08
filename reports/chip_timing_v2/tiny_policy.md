# Tiny chip policy vs planner (whole-half returns, chips only, forecast captain)

12 half-seasons; policy = 1637 parameters; 300 updates x 64 rollouts per half; greedy play at test time.

| Held-out half | Planner | Tiny policy | vs planner | Hindsight ceiling | Policy chips |
|---|---|---|---|---|---|
| 2020-21:1 | 1013 | 1065 | +52 | 1102 | [(2, 'free_hit'), (4, 'triple_captain'), (5, 'bench_boost'), (18, 'wildcard')] |
| 2020-21:2 | 1129 | 1144 | +15 | 1201 | [(20, 'free_hit'), (24, 'triple_captain'), (25, 'bench_boost'), (26, 'wildcard')] |
| 2021-22:1 | 1000 | 971 | -29 | 1093 | [(2, 'bench_boost'), (5, 'free_hit'), (10, 'triple_captain'), (13, 'wildcard')] |
| 2021-22:2 | 1095 | 1110 | +15 | 1306 | [(20, 'bench_boost'), (23, 'wildcard'), (26, 'triple_captain'), (27, 'free_hit')] |
| 2022-23:1 | 836 | 891 | +55 | 1092 | [(2, 'bench_boost'), (11, 'triple_captain'), (12, 'free_hit'), (17, 'wildcard')] |
| 2022-23:2 | 1078 | 1112 | +34 | 1284 | [(24, 'free_hit'), (25, 'triple_captain'), (27, 'bench_boost'), (29, 'wildcard')] |
| 2023-24:1 | 1074 | 1063 | -11 | 1112 | [(2, 'bench_boost'), (7, 'free_hit'), (10, 'triple_captain'), (18, 'wildcard')] |
| 2023-24:2 | 1189 | 1140 | -49 | 1349 | [(20, 'bench_boost'), (24, 'triple_captain'), (25, 'free_hit'), (29, 'wildcard')] |
| 2024-25:1 | 1098 | 1111 | +13 | 1192 | [(2, 'bench_boost'), (4, 'triple_captain')] |
| 2024-25:2 | 1061 | 1157 | +96 | 1227 | [(23, 'bench_boost'), (24, 'triple_captain'), (25, 'free_hit'), (33, 'wildcard')] |
| 2025-26:1 | 999 | 981 | -18 | 1097 | [(2, 'bench_boost'), (3, 'free_hit'), (5, 'wildcard'), (15, 'triple_captain')] |
| 2025-26:2 | 1206 | 1126 | -80 | 1297 | [(20, 'triple_captain'), (21, 'free_hit'), (22, 'bench_boost'), (23, 'wildcard')] |
| **total** | 12778 | 12871 | +93 | 14352 | |

G7b/G8 split (train on the other 10 halves): held-out 2220 vs planner 2395 (-175); 2025-26:2: 1100 chips [(20, 'bench_boost'), (22, 'wildcard'), (26, 'triple_captain'), (32, 'free_hit')]; 2023-24:2: 1120 chips [(20, 'wildcard'), (21, 'bench_boost'), (24, 'triple_captain'), (25, 'free_hit')]
