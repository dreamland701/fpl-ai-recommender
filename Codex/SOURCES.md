# External source notes

Checked 2026-10-03. Only primary sources support technical/rule recommendations. These sources establish rules and tools; the repository diagnosis and proposed architecture are this review's analysis.

| Source | Used for |
|---|---|
| [Premier League: 2026/27 changes](https://www.premierleague.com/en/news/4679873) | Current chip periods, saved-transfer limit, BPS changes, and later finalization of scores |
| [Premier League: making transfers](https://www.premierleague.com/en/news/2174907) | Transfer rights, hits, club constraints, and selling-price profit sharing |
| [Premier League: 2025/26 changes](https://www.premierleague.com/en/news/4373187) | Rule-era boundary for the two-set chip system |
| [Premier League: defensive contribution scoring](https://www.premierleague.com/en/news/4361991) | Role-dependent thresholds and per-match scoring context |
| [FPL official 2026/27 updates](https://fantasy.premierleague.com/help/new) | BPS changes requiring scoring-era review |
| [TRL SFT trainer](https://huggingface.co/docs/trl/main/sft_trainer) | Token likelihood/completion-only loss semantics; local code and installed versions remain the authority for this run |
| [scikit-learn TimeSeriesSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html) | Chronological splitting and the concept of a gap; project-specific horizon/group logic is still necessary |
| [LightGBM parameters](https://lightgbm.readthedocs.io/en/latest/Parameters.html) | Available objectives for a proposed tabular baseline, not a guarantee of improved FPL results |
| [OR-Tools CP-SAT](https://developers.google.com/optimization/cp/cp_solver) | Exact integer-constraint optimization as a proposed deterministic benchmark |

The official rules page at `https://fantasy.premierleague.com/en/help/rules` returned no extractable body through the browser. The review therefore relies on the readable official explanatory articles above for the checked current rule claims. Detailed historical rules should be archived and verified during the proposed rules-engine implementation.

Search also surfaced secondary sites and social posts; they were not used to certify scoring rules or technical recommendations. No present-day article was inserted into a historical feature packet.
