#!/bin/bash
# ----------------------------------------------------------
# Automated pytest run with Allure report generation
# ----------------------------------------------------------

# === CONFIG ===
PROJECT_DIR="/Kunal_Pipaliya/Project_2_Perpetuals_QA_Testnet"
LOG_DIR="$PROJECT_DIR/Cron_Details/Cron_log"
NOW=$(date '+%Y-%m-%d_%H-%M-%S')           # current datetime for log name
LOGFILE="$LOG_DIR/cron_15min_${NOW}.log"   # datetime-stamped log file
LOCKFILE="/tmp/test_runner_15min.lock"     # unique lockfile
PYTHON="/usr/bin/python3"
PYTEST="/usr/local/bin/pytest"
ALLURE="/usr/bin/allure"                   # adjust if Allure binary is elsewhere
ALLURE_RESULTS="$PROJECT_DIR/Reports/Allure_Report/Allure_15min/allure-results"
ALLURE_REPORT="$PROJECT_DIR/Reports/Allure_Report/Allure_15min/allure-report"

# === ENVIRONMENT (for cron) ===
export PATH=$PATH:/usr/local/bin:/usr/bin:/bin:/home/codezeros/.local/bin
export HOME=/home/codezeros

# === PREPARE DIRECTORIES ===
mkdir -p "$LOG_DIR" "$ALLURE_RESULTS"

# === LOCK CHECK ===
if [ -f "$LOCKFILE" ]; then
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] Another run is still in progress. Exiting." \
        >> "$LOG_DIR/cron_skip.log"
    exit 1
fi
trap 'rm -f "$LOCKFILE"' EXIT
touch "$LOCKFILE"

# === MAIN EXECUTION ===
{
    echo "========== START RUN: $(date '+%Y-%m-%d %H:%M:%S') =========="
    cd "$PROJECT_DIR" || { echo "[ERROR] Failed to cd $PROJECT_DIR"; exit 1; }

    echo "[INFO] Running tests..."
    "$PYTEST" --alluredir="$ALLURE_RESULTS" -s -v

    if [ -d "$ALLURE_RESULTS" ] && [ "$(ls -A "$ALLURE_RESULTS")" ]; then
        echo "[INFO] Generating Allure report..."
        "$ALLURE" generate "$ALLURE_RESULTS" --clean -o "$ALLURE_REPORT"
        echo "[INFO] Allure report generated at: $ALLURE_REPORT"
    else
        echo "[ERROR] Allure results folder is empty. Skipping report generation."
    fi

    echo "=========== END RUN: $(date '+%Y-%m-%d %H:%M:%S') ==========="
} >> "$LOGFILE" 2>&1

