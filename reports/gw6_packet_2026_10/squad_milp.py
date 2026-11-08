"""Re-export of fpl_ai.squad_milp (the exact squad optimizer now lives in the package)."""
import sys

sys.path.insert(0, "/home/wescheng/projects/fpl/fpl/src")
from fpl_ai.squad_milp import HIT, optimize  # noqa: E402,F401
