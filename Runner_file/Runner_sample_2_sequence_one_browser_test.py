import datetime
import os
import sys
import shutil
import time
import pytest
import subprocess
from Project_2_Perpetuals_QA_Testnet.Testcases_Logs.Logging_utils import Logger
from Project_2_Perpetuals_QA_Testnet.Data.user_perps import *

# Add project root to sys.path (so imports work)
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

BASE_DIR = Runner_sample_1_parallel_test.BASE_DIR
ALLURE_RESULTS = Runner_sample_1_parallel_test.ALLURE_RESULTS
ALLURE_REPORT_DIR = Runner_sample_1_parallel_test.ALLURE_REPORT_DIR

scripts = [
    # f"{BASE_DIR}/Test/test_2_perps_long_position.py",
    # f"{BASE_DIR}/Test/test_3_perps_short_position.py",
    # f"{BASE_DIR}/Test/test_4_perps_long_position_USD.py",
    # f"{BASE_DIR}/Test/test_5_perps_short_position_USD.py",
    f"{BASE_DIR}/Test/test_6_perps_collateral.py"

]

for i in range(1, 3):  # Repeat 100 times

    Logger.logger.info(f"✅ \n ---- Running Test Iteration: {i} ----\n")

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # ALLURE_RESULTS = f"{BASE_DIR}/Reports/Allure_Report/General_output/Report_output_{timestamp}"
    # ALLURE_REPORT_DIR = f"{BASE_DIR}/Reports/Allure_Report/General_output/Index_HTML_{timestamp}"

    # Clean old results
    if os.path.exists(ALLURE_RESULTS):
        shutil.rmtree(ALLURE_RESULTS)
    os.makedirs(ALLURE_RESULTS, exist_ok=True)

    Logger.logger.info(f"✅ \n ---- Running Selected Tests ----\n")

    # one broswer open all case
    exit_code = pytest.main(
        [*scripts, "-v", "-s", f"--alluredir={ALLURE_RESULTS}"]
    )


    # Optional: Open live server (attachments also visible here)
    # subprocess.run(["allure", "serve", ALLURE_RESULTS], check=True)

    # Move generated single-file index.html into allure-report folder
    ALLURE_REPORT_DIR = Runner_sample_1_parallel_test.ALLURE_REPORT_DIR
    os.makedirs(ALLURE_REPORT_DIR, exist_ok=True)

    if os.path.exists("index.html"):
        shutil.move("index.html", os.path.join(ALLURE_REPORT_DIR, "index.html"))

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # ALLURE_REPORT_DIR1 = f"/Kunal_Pipaliya/Project_2_Perpetuals_QA_Testnet/Reports/Allure_Report/General_output/Index_HTML1{timestamp}"
    # os.makedirs(ALLURE_REPORT_DIR1, exist_ok=True)

    # if os.path.exists("index.html"):
    #     shutil.move("index.html", os.path.join(ALLURE_REPORT_DIR1, "index.html"))    

    #  --- Send Email with report after Allure is generated ---
    Logger.logger.info(f"✅ \n ---- Sending Email ----\n")

    subprocess.run(
        ["python3", "-m", "Project_2_Perpetuals_QA_Testnet.Email.Email"],
        check=True
    )

    # Optional --- Open live Allure server (for local viewing only) ---Logger.logger.info(f"✅ \n ---- Opening Allure Serve ----\n")
    subprocess.run([
        "allure", "generate", ALLURE_RESULTS, "-o", ALLURE_REPORT_DIR, "--clean"
    ], check=True)

    subprocess.run([
        "allure", "serve", "--port", "2222", ALLURE_RESULTS
    ], check=True)


if __name__ == "__main__":
    pytest.main(["-n", "auto", "tests/"])