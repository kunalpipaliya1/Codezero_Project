import pytest
from Project_2_Perpetuals_QA_Testnet.Testcases_Logs.Logging_utils import Logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import traceback
import cv2
import mss
import numpy as np
import datetime
import os
import time
import threading
import multiprocessing
from Project_2_Perpetuals_QA_Testnet.Testcases_Logs.Logging_utils import Logger
from Project_2_Perpetuals_QA_Testnet.Page.test_page import Launchpage
from Project_2_Perpetuals_QA_Testnet.Test.wallet_connection import wallet_connection_class
from Project_2_Perpetuals_QA_Testnet.Utils.StaticUtils import StaticUtil
from Project_2_Perpetuals_QA_Testnet.Data.user_perps import Starkey_wallet, Video_dir

VIDEO_DIR = Video_dir.VIDEO_DIR

os.makedirs(VIDEO_DIR, exist_ok=True)

def record_screen(filename, stop_event, fps=10.0):
    sct = mss.mss()
    monitor = sct.monitors[1]
    width, height = int(monitor["width"]), int(monitor["height"])

    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    filename = filename.replace(".mp4", ".avi")
    out = cv2.VideoWriter(filename, fourcc, fps, (width, height))

    if not out.isOpened():
        Logger.logger.error(f"❌ Could not open VideoWriter for {filename}")
        return
    try:
        while not stop_event.is_set():
            img = np.array(sct.grab(monitor))
            frame = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
            frame = cv2.resize(frame, (width, height))  # ✅ enforce size
            out.write(frame)
            time.sleep(1 / fps)
    finally:
        out.release()
        sct.close()
        Logger.logger.info(f"✅ Recording finalized: {filename}")
        
@pytest.fixture(scope="session")
def record_video():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = os.path.join(VIDEO_DIR, f"test_{timestamp}.mp4")

    stop_event = multiprocessing.Event()
    process = multiprocessing.Process(target=record_screen, args=(filename, stop_event))
    process.start()

    yield  # run tests

    # stop recording
    stop_event.set()
    process.join(timeout=5)   # allow process to flush frames
    if process.is_alive():
        process.terminate()
    Logger.logger.info(f"✅ 🎥 Video saved: {filename}")

# @pytest.fixture(scope="class")    # each test case separate browser
@pytest.fixture(scope="session")    # one browser across all tests.
# @pytest.fixture(scope="function")   # one browser per test call
def call_main_url(record_video):
    browser = "chrome"  # change this to "chrome" / "brave" when needed
    driver = None

    try:
        if browser == "chrome":

            options = Options()
            options.add_experimental_option("useAutomationExtension", False)
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option("enableExtensionTargets", value=True)
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")

            prefs = {
                "profile.default_content_setting_values.notifications": 2,  # disable notifications
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False,
                "download.default_directory": "/path/to/download/folder",
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "safebrowsing.enabled": True
            }

            options.add_experimental_option("useAutomationExtension", False)
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option("prefs", prefs)
            options.add_argument("disable-features=DisableLoadExtensionCommandLineSwitch")
            options.add_argument("disable-features=ExtensionsRequireVerification")
            # options.add_argument("--headless=new")   # preferred in latest Chrome
            # options.browser_version = "140"
            # options.add_extension(Starkey_wallet.Extension_Add)
            options.add_argument(Starkey_wallet.Extension_Add_argument)

            driver = webdriver.Chrome(options=options)
            lp = Launchpage(driver)
            driver.get(lp.Login_URL1()) 

        elif browser == "brave":
            options = Options()

            # options.add_experimental_option("useAutomationExtension", False)
            # options.add_experimental_option("excludeSwitches", ["enable-automation"])
            # options.add_experimental_option("enableExtensionTargets", value=True)

            prefs = {
                "profile.default_content_setting_values.notifications": 2,  # disable notifications
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False,
                "download.default_directory": "/path/to/download/folder",
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "safebrowsing.enabled": True
            }

            options.binary_location = "/usr/bin/brave-browser"   # Brave binary
            options.add_experimental_option("useAutomationExtension", False)
            options.add_experimental_option("enableExtensionTargets", value=True)
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option("prefs", prefs)
            options.add_argument("disable-features=DisableLoadExtensionCommandLineSwitch")
            options.add_argument("disable-features=ExtensionsRequireVerification")
            # options.add_extension(Starkey_wallet.Extension_Add)
            options.add_argument(Starkey_wallet.Extension_Add_argument)

            # IMPORTANT: must use ChromeDriver compatible with Brave
            driver = webdriver.Chrome(options=options)
            Logger.logger.info(f"✅ Brave launched successfully.")

        elif browser == "firefox":
            options = FirefoxOptions()
            driver = webdriver.Firefox(options=options)
            Logger.logger.info(f"✅ Firefox launched successfully.")

        else:
            raise ValueError(f"Unsupported browser: {browser}")

    except Exception as e:
        Logger.logger.error(f"Failed to launch {browser}: {e}")
        traceback.print_exc()

    if not driver:
        pytest.skip(f"Skipping tests because {browser} driver could not be started.")

    # ---- Common setup ----
    driver.delete_all_cookies()
    try:
        driver.execute_cdp_cmd("Network.clearBrowserCache", {})
        driver.execute_cdp_cmd("Network.clearBrowserCookies", {})
    except Exception as e:
        Logger.logger.error(f"CDP clear failed: {e}")
    time.sleep(2)
    driver.maximize_window()
    driver.implicitly_wait(2)

    yield driver
    driver.quit()

@pytest.fixture(autouse=True)
def attach_logs_after_test(request):
    yield
    Logger.attach_log_to_allure()
    Logger.logger.info(f"✅ 📎 Logs attached to Allure for test: {request.node.name}")

@pytest.fixture(scope="session", autouse=True)
def login_and_connect_wallet(call_main_url):
    driver = call_main_url
    lp = Launchpage(driver)
    driver.get(lp.Login_URL1())
    driver.delete_all_cookies()
    time.sleep(1)

    Logger.logger.info(f"✅ Opened login URL -> {lp.Login_URL1()}")
    Logger.logger.info(f"✅ Total windows: {driver.window_handles}")

    if len(driver.window_handles) > 1:
        driver.switch_to.window(driver.window_handles[1])
    else:
        Logger.logger.warning("⚠️ Only one window open, skipping switch")

    StaticUtil.retry_click(driver, By.XPATH, lp.walletalreadyhavebtn())
    time.sleep(1)

    driver.switch_to.window(driver.window_handles[1])

    # Click on the "Private Key" import option
    StaticUtil.retry_click(driver, By.XPATH, lp.privatekeybtn())

    # Handle custom dropdown: Click and choose 'Supra'
    StaticUtil.retry_click(driver, By.XPATH, lp.networkdropdown())

    # WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, lp.supranetworkoption())))
    StaticUtil.retry_click(driver, By.XPATH, lp.supranetworkoption())

    # Add 0.5 sec delay
    time.sleep(0.5)
    lp.Privatekey()

    # Click on next button
    StaticUtil.retry_click(driver, By.XPATH, lp.nextbtn())

    # creation page details filling
    lp.Add_username()
    lp.setpassword1()
    lp.confirmpassword1()
    lp.clicknext()
    lp.open_wall()

    # select all network
    StaticUtil.retry_click(driver, By.XPATH, lp.fetcallnetwork())

    # click on the Testnet
    StaticUtil.retry_click(driver, By.XPATH, lp.testnetclick())     # click on Testnet
    time.sleep(1)

    main_tab = driver.window_handles[0]
    for handle in driver.window_handles:
        if handle != main_tab:
            driver.switch_to.window(handle)
            driver.close()
    driver.switch_to.window(main_tab)
    Logger.logger.info(f"✅ Closed all tab and continuing with main tab")

    driver.switch_to.window(driver.window_handles[0])

    time.sleep(0.5)

    # @@ Below enable only for CLMM-QA @@
    
    # login_failed_xpath = lp.loginfailedmsg()

    # for pwd in lp.creden:
    #     Logger.logger.info(f"✅ \n Trying wrong password: {pwd}")

    #     # Enter password
    #     password_input = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, lp.webportal_xpath)))
    #     password_input.clear()
    #     password_input.send_keys(pwd)

    #     # Click Login
    #     lp.click_on_login()
    #     time.sleep(0.2)

    #     try:
    #         error_msg = WebDriverWait(driver, 5).until(
    #             EC.visibility_of_element_located((By.XPATH, login_failed_xpath))
    #         )
    #         Logger.logger.info(f"✅ Login failed as expected with wrong password: {pwd} -> {error_msg.text}")
    #     except:
    #         Logger.logger.error(f" Expected: Login may have passed with correct password {pwd}")
    time.sleep(2)
    if lp.connection_wallet():
        Logger.logger.info(f"✅ Connected wallet with 1st attempt")
    elif lp.connection_wallet():
        Logger.logger.warning("⚠️ Connected wallet with 2nd attempt")
    else:
        Logger.logger.error(f"❌ Wallet is not connecting...")


    wallet_connection_class.wallet_connection(driver)

    Logger.logger.info(f"✅ Wallet setup complete for session")

    # Validate the Hash

    Hash_print = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, lp.hashtext())))   # waiting for hash
    Transaction_hash_validate = Hash_print.text.strip()
    Logger.logger.info(f"✅ Transaction_hash: {Transaction_hash_validate}")
    
    import re
    pattern = r'^0x[0-9a-zA-Z]+'

    try:
        if re.match(pattern, Transaction_hash_validate):
            Logger.logger.info(f"✅ Valid Hex: {Transaction_hash_validate}")
        else:
            Logger.logger.error(f"inValid Hex: {Transaction_hash_validate}")
    except:
        Logger.logger.error(f"❌ Hexadecimal not found")
        screenshot_dir = "/Kunal_Pipaliya/Project_2_Perpetuals_QA_Testnet/Screenshots"

        os.makedirs(screenshot_dir, exist_ok=True)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = os.path.join(screenshot_dir, f"test_1_Launch_url_Hash_not_found_{timestamp}.png")
        driver.save_screenshot(filename)   # Historical screenshot
        Logger.logger.error(f"❌ Screenshot saved: {filename}")
    return driver

@pytest.fixture
# class testcase_amounts:
def random_prices():

    # amounts = list(range(1, 2)) # range or 5 and 6 both value enter
    # amounts = range(12, 13)   # exact 5 value enter

    # SL_random_price =[random.randint(1, 100)]   # pick one random integer from 1 to 100
    # TP_random_price =[random.randint(1, 100)]   # pick one random integer from 1 to 100

    SL_random_price =random.randint(40, 40)   # Stop Loss
    TP_random_price = random.randint(50, 500)   # Take Profit
    return SL_random_price, TP_random_price
