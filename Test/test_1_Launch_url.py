        
import datetime
import os
import pytest
from selenium import webdriver
from Project_2_Perpetuals_QA_Testnet.Data.user_perps import screenshot_dir1
from Project_2_Perpetuals_QA_Testnet.Page.base_page import allurescreenshot
from Project_2_Perpetuals_QA_Testnet.Page.test_page import Launchpage
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from Project_2_Perpetuals_QA_Testnet.Utils.StaticUtils import StaticUtil
from Project_2_Perpetuals_QA_Testnet.Test.wallet_connection import wallet_connection_class
import allure

# @pytest.mark.dependency(name="launch")
from Project_2_Perpetuals_QA_Testnet.Testcases_Logs.Logging_utils import Logger
@allure.title("test_1_Launch_url")
@allure.description("Verify that CLMM login works with valid credentials")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Kunal Pipaliya QA Team")
@allure.story("Login Functionality")

@pytest.mark.usefixtures("call_main_url")
class TestCPMM:
    Logger.logger.info(f"✅ ==== Test 1: Launch CPMM URL started ====")
    
    def test_1_launch_CPMM_URL(self, call_main_url):
        allure.dynamic.description("Launch URL")

        driver = call_main_url

        lp = Launchpage(driver)
    
        driver.get(lp.Login_URL1())
        driver.delete_all_cookies()
        driver.implicitly_wait(3)

        Logger.logger.info(f"✅ Opened login URL -> {lp.Login_URL1()}")
        Logger.logger.info(f"✅ Total windows: {driver.window_handles}")

        driver.switch_to.window(driver.window_handles[1])

        StaticUtil.retry_click(driver, By.XPATH, lp.walletalreadyhavebtn())
        driver.implicitly_wait(3)

        driver.switch_to.window(driver.window_handles[1])

        # Click on the "Private Key" import option
        StaticUtil.retry_click(driver, By.XPATH, lp.privatekeybtn())

        # Handle custom dropdown: Click and choose 'Supra'
        StaticUtil.retry_click(driver, By.XPATH, lp.networkdropdown())

        # WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, lp.supranetworkoption())))
        StaticUtil.retry_click(driver, By.XPATH, lp.supranetworkoption())

        # Add 0.5 sec delay
        driver.implicitly_wait(3)
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
        driver.implicitly_wait(3)

        main_tab = driver.window_handles[0]
        for handle in driver.window_handles:
            if handle != main_tab:
                driver.switch_to.window(handle)
                driver.close()
        driver.switch_to.window(main_tab)
        Logger.logger.info(f"✅ Closed all tab and continuing with main tab")

        driver.switch_to.window(driver.window_handles[0])
    
        driver.implicitly_wait(3)

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
        #     driver.implicitly_wait(3)

        #     try:
        #         error_msg = WebDriverWait(driver, 5).until(
        #             EC.visibility_of_element_located((By.XPATH, login_failed_xpath))
        #         )
        #         Logger.logger.info(f"✅ Login failed as expected with wrong password: {pwd} -> {error_msg.text}")
        #     except:
        #         Logger.logger.error(f" Expected: Login may have passed with correct password {pwd}")
        driver.implicitly_wait(3)
        if lp.connection_wallet():
            Logger.logger.info(f"✅ Connected wallet with 1st attempt'")
        else:
            with allure.step("Connected wallet with 2nd attempt"):
                    allurescreenshot.take_screenshot(driver, "Connected wallet with 2nd attempt")
            lp.connection_wallet()

            Logger.logger.warning("⚠️ Connected wallet with 2nd attempt'")
                   
        wallet_connection_class.wallet_connection(driver)

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
            with allure.step("Hexadecimal not found"):
                    allurescreenshot.take_screenshot(driver, "Hexadecimal not found")
                    
            Logger.logger.error(f"❌ Hexadecimal not found")
            ss = screenshot_dir1.SCREENSHOT_DIRR

            os.makedirs(ss, exist_ok=True)
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = os.path.join(ss, f"test_1_Launch_url_Hash_not_found_{timestamp}.png")
            driver.save_screenshot(filename)   # Historical screenshot
            Logger.logger.error(f"❌ Screenshot saved: {filename}")

def run():
    Logger.logger.info(f"✅ Running test_1_Launch_url ...")
    import pytest
    pytest.main([__file__])   # this will run the tests inside this file

if __name__ == "__main__":
    run()           