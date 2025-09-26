import time, datetime, os, multiprocessing, tempfile, pytest, traceback, cv2, mss, numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium import webdriver
from Project_1_CLMM_QA_Testnet.Testcases_Logs.Logging_utils import Logger
from selenium.webdriver.chrome.options import Options
from Project_1_CLMM_QA_Testnet.Data.users_v3 import (Starkey_wallet, Video_dir)

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
# @pytest.fixture(scope="function")
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
            # options.binary_location = "/usr/bin/chromium-browser"
            options.add_experimental_option("useAutomationExtension", False)
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option("prefs", prefs)
            options.add_argument("disable-features=DisableLoadExtensionCommandLineSwitch")
            options.add_argument("disable-features=ExtensionsRequireVerification")
            tmp_profile = tempfile.mkdtemp()
            options.add_argument(f"--user-data-dir={tmp_profile}")
            # options.add_argument("--headless=new")   # preferred in latest Chrome
            # options.browser_version = "140"
            # options.add_extension(Starkey_wallet.Extension_Add)
            options.add_argument(Starkey_wallet.Extension_Add_argument)

            driver = webdriver.Chrome(options=options)
            Logger.logger.info(f"✅ Chrome launched successfully.")

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
            options.add_argument("--disable-features=ExtensionsManifestV3Only")
            # IMPORTANT: must use ChromeDriver compatible with Brave
            # options.add_extension(Starkey_wallet.Extension_Add)
            options.add_argument(Starkey_wallet.Extension_Add_argument)
            driver = webdriver.Chrome(options=options)
            Logger.logger.info(f"✅ brave launched successfully.")

        elif browser == "firefox":
            options = FirefoxOptions()
            options.binary_location = "/usr/bin/firefox"  # replace with output of 'which firefox'
            options.set_preference("dom.webnotifications.enabled", False)
            options.set_preference("signon.rememberSignons", False)
            options.set_preference("browser.download.folderList", 2)
            options.set_preference("browser.download.dir", "/home/codezeros/Kunal_Pipaliya/Project_1_CLMM_QA_Testnet/Downloads")
            options.set_preference("browser.download.useDownloadDir", True)
            options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")

            driver = webdriver.Firefox(options=options)
            Logger.logger.info(f"✅ Firefox launched successfully.")
        
        elif browser == "edge":
            options = EdgeOptions()
            options.add_experimental_option("useAutomationExtension", False)
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_argument("disable-features=DisableLoadExtensionCommandLineSwitch")
            options.add_argument("disable-features=ExtensionsRequireVerification")
            driver = webdriver.Edge(options=options)
            Logger.logger.info(f"✅ Edge launched successfully.")

        elif browser == "safari":
            # SafariDriver comes pre-installed with Safari on macOS
            driver = webdriver.Safari()
            Logger.logger.info(f"✅ Safari launched successfully.")
            
        else:
            raise ValueError(f"Unsupported browser: {browser}")

    except Exception as e:
        Logger.logger.error(f"❌ Failed to launch {browser}: {e}")
        traceback.print_exc()

    if not driver:
        pytest.skip(f"Skipping tests because {browser} driver could not be started.")

    # ---- Common setup ----
    driver.delete_all_cookies()
    try:
        driver.execute_cdp_cmd("Network.clearBrowserCache", {})
        driver.execute_cdp_cmd("Network.clearBrowserCookies", {})
    except Exception as e:
        Logger.logger.error(f"❌ CDP clear failed: {e}")

    driver.maximize_window()
    driver.implicitly_wait(2)

    yield driver
    driver.quit()


import pytest
from Project_1_CLMM_QA_Testnet.Testcases_Logs.Logging_utils import Logger

@pytest.fixture(autouse=True)
def attach_logs_after_test(request):
    yield
    Logger.attach_log_to_allure()
    Logger.logger.info(f"✅ 📎 Logs attached to Allure for test: {request.node.name}")


# import pytest
# from Project_1_CLMM_QA_Testnet.Testcases_Logs.Logging_utils import Logger

# @pytest.fixture(autouse=True)
# def attach_logs_after_test():
#     yield
#     Logger.attach_log_to_allure()

