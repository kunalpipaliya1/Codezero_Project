        
import time , allure, pytest
from selenium.common.exceptions import InvalidSessionIdException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Project_1_CLMM_QA_Testnet.Test.wallet_connection import wallet_connection_class
from Project_1_CLMM_QA_Testnet.Test.Transaction_validation import Transaction_validation_class
from Project_1_CLMM_QA_Testnet.Testcases_Logs.Logging_utils import Logger
from Project_1_CLMM_QA_Testnet.Page.test_page import (Homepage, allurescreenshot, slipagechecker)
from Project_1_CLMM_QA_Testnet.Test.For_loop_class import (testcase_amounts, testcase_token_name)
from Project_1_CLMM_QA_Testnet.Page.base_page import StaticUtil

@allure.label("owner", "Kunal Pipaliya QA Team")
@allure.story("Earn to swapping Functionality")

@pytest.mark.usefixtures("call_main_url")
class TestCPMM:
    allure.dynamic.description("Earn to swapping page")
    @pytest.mark.parametrize("x_token, y_token", testcase_token_name.token_pairs)
    @pytest.mark.parametrize("amount", testcase_amounts.amounts)
    # @pytest.mark.repeat(1)
    def test_4_Earn_to_Swapping_Tab(self, call_main_url, x_token, y_token, amount):

        driver = call_main_url
        lp = Homepage(driver)

        Logger.logger.info(f"✅ \n=== Starting Earn to swapping_Tab ===")
        StaticUtil.retry_click(driver, By.XPATH, lp.Title_click1())

        try:
            StaticUtil.retry_click(driver, By.XPATH, lp.clickonearn())
        except InvalidSessionIdException:
            with allure.step("test_4_WebDriver session is invalid. Restarting driver..."):
                allurescreenshot.take_screenshot(driver, "test_4_WebDriver session is invalid. screenshot")

            Logger.logger.error(f"❌ test_4_WebDriver session is invalid. Restarting driver...")
            driver = call_main_url()  # Re-initialize
            StaticUtil.retry_click(driver, By.XPATH, lp.clickonearn())

        # click on Earns to pools
        time.sleep(1) 
        StaticUtil.retry_click(driver, By.XPATH, lp.clickonpool())

        # Filter by token
        StaticUtil.retry_click(driver, By.XPATH, lp.filterbytoken())

        # Wait for filter popup input to be visible
        try:
            driver.implicitly_wait(1)
            eth_input = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, lp.ethereuminput())))
            eth_input.clear()
            eth_input.send_keys(x_token)
            Logger.logger.info(f"✅ test_4_Entered token: {x_token}")
        except Exception as e:
            with allure.step(f"Failed to enter x_token {x_token}: {e}"):
                allurescreenshot.take_screenshot(driver, f"Failed to enter x_token {x_token}: {e} screenshot")
            Logger.logger.error(f"❌ test_4_Failed to enter x_token {x_token}: {e}")

        # selected tick mark
        StaticUtil.retry_click(driver, By.XPATH, lp.tickmark1())
        driver.implicitly_wait(1)

        try:
            driver.implicitly_wait(1)
            eth_input = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, lp.suprainput()))
            )
            eth_input.clear()
            eth_input.send_keys(y_token)
            Logger.logger.info(f"✅ test_4_Entered token: {y_token}")
        except Exception as e:
            with allure.step(f"test_4_Enter y_token {y_token}: {e}"):
                allurescreenshot.take_screenshot(driver, f"test_4_Failed to enter y_token {y_token}: {e} screenshot")
            Logger.logger.error(f"❌ test_4_Failed to enter y_token {y_token}: {e}")

        # selected tick mark
        StaticUtil.retry_click(driver, By.XPATH, lp.tickmark1())

        # Select V3 pool - concentrated
        StaticUtil.retry_click(driver, By.XPATH, lp.v3_pool())
    
        # select swap
        StaticUtil.retry_click(driver, By.XPATH, lp.swaptablerow())

        driver.implicitly_wait(1)

        slipagechecker.slipagecheck(driver)

        lp.earn2poolswap_x(amount)

        driver.implicitly_wait(1)

        lp.eventpointerr()
        lp.scroll_botton()
        
        # Check if element exists first
        elements = driver.find_elements(By.XPATH, lp.Acknowl())

        if not elements:   # Means element NOT present
            Logger.logger.info(f"✅ test_4_Swap Pool is verified")
        else:              # Element present → safe to click
            with allure.step("test_4_Element present → safe to click"):
                allurescreenshot.take_screenshot(driver, "⚠️ test_4_Element present → safe to click screenshot")

            StaticUtil.retry_click(driver, By.XPATH, lp.Acknowl())
            Logger.logger.info(f"⚠️ test_4_Swap Pool is unverified")    

        try:
            StaticUtil.retry_click(driver, By.XPATH, lp.swapbtn())
            Logger.logger.info(f"✅ test_4_Swap button is clickable and clicked")
            try:
                Error = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, lp.swaperrormsg1())))
                if Error.is_displayed():
                    Logger.logger.info(f"✅ test_4_Error is displayed")
                else:
                    with allure.step("test_4_Error is displayed"):
                        allurescreenshot.take_screenshot(driver, "test_4_Error is displayed screenshot")
                    Logger.logger.warning("⚠️ test_4_Error not displayed")
            except:
                    with allure.step("test_4_No error message element found"):
                        allurescreenshot.take_screenshot(driver, "test_4_No error message element found screenshot")
                    Logger.logger.error(f"❌ test_4_No error message element found")
        except:
            with allure.step("test_4_Swap button not clicked"):
                        allurescreenshot.take_screenshot(driver, "test_4_Swap button not clicked")
            Logger.logger.error(f"❌ test_4_Swap button not clicked")
        
        driver.switch_to.window(driver.window_handles[0])

        wallet_connection_class.wallet_connection(driver)
        Transaction_validation_class.Transaction_validation(driver)

        Logger.logger.info(f"✅ \n=== Completed Earn to swapping_Tab ===")

def run():
    Logger.logger.info(f"✅ Running test_4_Earn to swapping tab ...")
    import pytest
    pytest.main([__file__])   # this will run the tests inside this file

if __name__ == "__main__":
    run()          