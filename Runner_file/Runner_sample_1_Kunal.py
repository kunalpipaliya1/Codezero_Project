import os
import sys
import shutil
import pytest
import subprocess
from Project_1_CLMM_QA_Testnet.Testcases_Logs.Logging_utils import Logger
from Project_1_CLMM_QA_Testnet.Data.users_v3 import Runner_details_1_Kunal

# ---------------------- PATHS ----------------------
BASE_DIR = Runner_details_1_Kunal.BASE_DIR
ALLURE_JSON_DIR  = Runner_details_1_Kunal.ALLURE_JSON_DIR # json data
ALLURE_RESULTS   = Runner_details_1_Kunal.ALLURE_RESULTS # json results
ALLURE_FULL_DIR  = Runner_details_1_Kunal.ALLURE_REPORT_DIR # full html report
INDEX_HTML_DIR   = Runner_details_1_Kunal.INDEX_HTML_DIR # single file html report


# Ensure project root is importable
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# ---------------------- CLEAN OLD ----------------------
for p in [ALLURE_RESULTS, ALLURE_JSON_DIR, ALLURE_FULL_DIR, INDEX_HTML_DIR]:
    shutil.rmtree(p, ignore_errors=True)
    os.makedirs(p, exist_ok=True)

# ---------------------- TEST SCRIPTS -------------------
scripts = [
    f"{BASE_DIR}/Test/test_1_Launch_url.py",
    f"{BASE_DIR}/Test/test_2_create_pool.py",
    f"{BASE_DIR}/Test/test_3_add_liquidity.py",
    f"{BASE_DIR}/Test/test_5_position_increase.py",
    f"{BASE_DIR}/Test/test_6_position_remove.py",
    f"{BASE_DIR}/Test/test_7_From_Trade_to_Swap_wallet.py",
    f"{BASE_DIR}/Test/test_8_claim_testnet.py",
    f"{BASE_DIR}/Test/test_4_Earn_to_Swapping_Tab.py"

]

pytest_args = scripts + ["-v", "-s", f"--alluredir={ALLURE_RESULTS}"]

Logger.logger.info("✅ ---- Running Selected Tests ----")
pytest.main(pytest_args)

Logger.logger.info("✅ ---- Generating Allure Report ----")

# ---------------------- COPY JSON ----------------------
shutil.copytree(ALLURE_RESULTS, ALLURE_JSON_DIR, dirs_exist_ok=True)
Logger.logger.info(f"✅ Allure JSON saved at: {ALLURE_JSON_DIR}")

# ---------------------- FULL HTML REPORT ---------------
subprocess.run(
    ["allure", "generate", ALLURE_RESULTS, "-o", ALLURE_FULL_DIR, "--clean"],
    check=True
)
Logger.logger.info(f"✅ Full Allure HTML report saved at: {ALLURE_FULL_DIR}")

# ---------------------- SINGLE-FILE INDEX --------------
subprocess.run(
    ["allure", "generate", ALLURE_RESULTS, "-o", INDEX_HTML_DIR, "--clean", "--single-file"],
    check=True
)
single_index_path = os.path.join(INDEX_HTML_DIR, "index.html")
Logger.logger.info(f"✅ Single-file report saved at: {single_index_path}")

# ---------------------- EMAIL --------------------------
Logger.logger.info("✅ ---- Sending Email ----")
subprocess.run(
    ["python3", "-m", Runner_details_1_Kunal.EMAIL_MODULE],
    check=True,
    cwd=Runner_details_1_Kunal.EMAIL_CWD
)

Logger.logger.info("✅ ---- Test Run Completed ----")
