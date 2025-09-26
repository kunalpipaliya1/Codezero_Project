import datetime, os, sys, shutil, pytest, subprocess
from Testcases_Logs.Logging_utils import Logger
from Data.users_v3 import Runner_details_2_Harsh

# -------------------- PATHS --------------------
BASE_DIR = Runner_details_2_Harsh.BASE_DIR
ALLURE_JSON_DIR  = Runner_details_2_Harsh.ALLURE_JSON_DIR # json data
ALLURE_RESULTS   = Runner_details_2_Harsh.ALLURE_RESULTS # json results
ALLURE_FULL_DIR  = Runner_details_2_Harsh.ALLURE_REPORT_DIR # full html report
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
INDEX_HTML_DIR = os.path.join(Runner_details_2_Harsh.INDEX_HTML_DIR, f"report_{timestamp}") # single file html report

# Ensure project root is importable
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# ---------------------- CLEAN OLD ----------------------
for p in [ALLURE_RESULTS, ALLURE_JSON_DIR, ALLURE_FULL_DIR, INDEX_HTML_DIR]:
    shutil.rmtree(p, ignore_errors=True)
    os.makedirs(p, exist_ok=True)

# ---------------------- TEST SCRIPTS -------------------
scripts = [
    f"{BASE_DIR}/Test/test_1_Launch_url.py",
    # f"{BASE_DIR}/Test/test_2_create_pool.py",
    # f"{BASE_DIR}/Test/test_3_add_liquidity.py",
    # f"{BASE_DIR}/Test/test_5_position_increase.py",
    # f"{BASE_DIR}/Test/test_6_position_remove.py",
    f"{BASE_DIR}/Test/test_7_From_Trade_to_Swap_wallet.py",
    # f"{BASE_DIR}/Test/test_8_claim_testnet.py",
    # f"{BASE_DIR}/Test/test_4_Earn_to_Swapping_Tab.py"
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
    ['cmd.exe', '/c', ALLURE_CLI, 'generate', ALLURE_RESULTS, '-o', ALLURE_FULL_DIR, '--clean', '--single-file'],
    check=True
)
Logger.logger.info(f":white_check_mark: Allure report generated at {ALLURE_FULL_DIR}")


Logger.logger.info("✅ ---- Test Run Completed ----")
