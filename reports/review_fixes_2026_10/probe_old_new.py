import sys, json
"""Old-vs-new behaviour of the scoring rules and delta parser (run under either code tree)."""
from fpl_ai import backtest, llm_adjust, config
from fpl_ai.types import SquadPlayer
pos = ["GK"]*2 + ["DEF"]*5 + ["MID"]*5 + ["FWD"]*3
squad = [SquadPlayer(i, f"P{i}", i, p, 5.0) for i, p in enumerate(pos, start=1)]
starters = [1, 3, 4, 5, 8, 9, 10, 11, 13, 14, 15]; bench = [2, 6, 12, 7]
minutes = {i: (0.0 if i in {9, 10, 11, 13} else 90.0) for i in range(1, 16)}
counted, notes = backtest._apply_automatic_substitutions(squad, starters, bench, {i: 2.0 for i in range(1, 16)}, minutes)
shapes = sorted((f["DEF"], f["MID"], f["FWD"]) for f in config.STARTING_FORMATIONS)
import pandas as pd
frame = pd.DataFrame([{"player_id": i, "price": 5.4, "price_pre_deadline": 5.4} for i in range(1, 16)])
sell = backtest._refresh_squad_prices(squad, frame)[0].sell_price
nan = llm_adjust.parse_delta_response('{"delta_points_1gw": NaN, "delta_points_3gw": 1.0}')
print(json.dumps({"formations": shapes, "autosub_counted_players": len(counted), "autosubs_made": len(notes),
                  "sell_price_buy5.0_now5.4": sell, "parsed_NaN_response": nan}))
