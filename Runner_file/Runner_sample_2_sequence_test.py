import datetime
import os
import sys
import shutil
import time
import pytest
import subprocess
from Project_2_Perpetuals_QA_Testnet.Data.user_perps import Runner_sample_1_parallel_test
from Project_2_Perpetuals_QA_Testnet.Testcases_Logs.Logging_utils import Logger

# Add project root to sys.path (so imports work)
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

BASE_DIR = Runner_sample_1_parallel_test.BASE_DIR
ALLURE_RESULTS = Runner_sample_1_parallel_test.ALLURE_RESULTS
ALLURE_REPORT_DIR = Runner_sample_1_parallel_test.ALLURE_REPORT_DIR

scripts = [
    f"{BASE_DIR}/Test/test_2_perps_long_position.py",
    # f"{BASE_DIR}/Test/test_3_perps_short_position.py",
    # f"{BASE_DIR}/Test/test_4_perps_long_position_USD.py",
    # f"{BASE_DIR}/Test/test_5_perps_short_position_USD.py"
]

for i in range(1, 1000):  # Repeat 100 times

    Logger.logger.info(f"✅ \n ---- Running Test Iteration: {i} ----\n")

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Clean old results
    if os.path.exists(ALLURE_RESULTS):
        shutil.rmtree(ALLURE_RESULTS)
    os.makedirs(ALLURE_RESULTS, exist_ok=True)

    Logger.logger.info(f"✅ \n ---- Running Selected Tests ----\n")

    # If you need sequence test enable below @@@@@@@@@@@@@

    # ✅ run each script twice with 2-second delay
    for script in scripts:
        for _ in range(1):
            Logger.logger.info(f"✅ \n ---- Running {script} ----\n")
            exit_code = pytest.main([
                script,
                "-v", "-s",
                f"--alluredir={ALLURE_RESULTS}"
            ])
            if exit_code != 0:
                Logger.logger.error(f"❌ Test failed: {script}")
            time.sleep(2)
    # If you need sequence test enable above @@@@@@@@@@@@@

    Logger.logger.info(f"✅ \n ---- Generating Allure Report ----\n")
    subprocess.run([
        "allure", "generate",
        ALLURE_RESULTS,
        "-o", ALLURE_REPORT_DIR,
        "--clean", "--single-file"
    ], check=True)

    if exit_code != 0:
        Logger.logger.error(f"❌ Tests failed")
        sys.exit(exit_code)


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
    subprocess.run([
        "python3", Runner_sample_1_parallel_test.Email
    ], check=True)

    # Optional --- Open live Allure server (for local viewing only) ---Logger.logger.info(f"✅ \n ---- Opening Allure Serve ----\n")
    subprocess.run([
        "allure", "serve", ALLURE_RESULTS # , "-p", "2222", 
    ], check=True)


if __name__ == "__main__":
    pytest.main(["-n", "auto", "tests/"])