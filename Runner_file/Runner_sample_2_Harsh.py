import os
import subprocess
import pytest
from Testcases_Logs.Logging_utils import Logger
from Project_1_CLMM_QA_Testnet.Data.users_v3 import Runner_details_2_Harsh


# -------------------- Paths --------------------
BASE_DIR = Runner_details_2_Harsh.BASE_DIR
ALLURE_RESULTS = Runner_details_2_Harsh.ALLURE_RESULTS
ALLURE_REPORT_DIR = Runner_details_2_Harsh.ALLURE_REPORT_DIR

# Ensure directories exist
os.makedirs(ALLURE_RESULTS, exist_ok=True)
os.makedirs(ALLURE_REPORT_DIR, exist_ok=True)
# -------------------- Change working directory --------------------
os.chdir(BASE_DIR)
# -------------------- Select Test Scripts --------------------
scripts = [
    os.path.join(BASE_DIR, "Test", "test_1_Launch_url.py"),
    # os.path.join(BASE_DIR, "Test", "test_2_create_pool.py"),
    # os.path.join(BASE_DIR, "Test", "test_3_add_liquidity.py"),
    os.path.join(BASE_DIR, "Test", "test_4_Earn_to_Swapping_Tab.py"),
    # os.path.join(BASE_DIR, "Test", "test_5_position_increase.py"),
    # os.path.join(BASE_DIR, "Test", "test_6_position_remove.py"),
    # os.path.join(BASE_DIR, "Test", "test_7_From_Trade_to_Swap_wallet.py"),
    # os.path.join(BASE_DIR, "Test", "test_8_claim_testnet.py"),
]
Logger.logger.info(f"Found test scripts: {scripts}")
# -------------------- Run Pytest --------------------
pytest_args = scripts + [
    "-v", "-s",
    f"--alluredir={ALLURE_RESULTS}",
]
Logger.logger.info("\n ---- Running Selected Tests ----\n")
exit_code = pytest.main(pytest_args)
if exit_code != 0:
    Logger.logger.error(f"\n:x: Tests failed with exit code {exit_code}")
# -------------------- Generate Allure Report --------------------
Logger.logger.info("\n ---- Generating Allure Report ----\n")
ALLURE_CLI = r"C:\Users\webclues\scoop\shims\allure.cmd"
subprocess.run(
    ['cmd.exe', '/c', ALLURE_CLI, 'generate', ALLURE_RESULTS, '-o', ALLURE_REPORT_DIR, '--clean', '--single-file'],
    check=True
)
Logger.logger.info(f":white_check_mark: Allure report generated at {ALLURE_REPORT_DIR}")


