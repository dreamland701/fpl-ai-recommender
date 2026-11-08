#!/usr/bin/env bash
# Programme item 1 launcher: 21 windows for the five regime configs, then the live window for them + ST1_F.
cd /home/wescheng/projects/fpl/fpl
CONFIGS="RP_F RG1_F RW1_F RW2_F RGW_F" WINDOWS=all JOBS=6 /usr/bin/bash /home/wescheng/projects/fpl/fpl/scripts/run_regime_backtests.sh
CONFIGS="ST1_F RP_F RG1_F RW1_F RW2_F RGW_F" WINDOWS=live JOBS=6 /usr/bin/bash /home/wescheng/projects/fpl/fpl/scripts/run_regime_backtests.sh
echo "$(date '+%F %T') REGIME BENCH COMPLETE" >> reports/regime/bt/progress.log
