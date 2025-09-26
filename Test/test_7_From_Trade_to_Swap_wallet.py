        
import time, allure, pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import InvalidSessionIdException
from Project_1_CLMM_QA_Testnet.Test.For_loop_class import FA_Address_full_short, testcase_amounts, testcase_token_name
from Project_1_CLMM_QA_Testnet.Test.Transaction_validation import Transaction_validation_class
from Project_1_CLMM_QA_Testnet.Page.base_page import StaticUtil
from Project_1_CLMM_QA_Testnet.Test.wallet_connection import wallet_connection_class
from Project_1_CLMM_QA_Testnet.Testcases_Logs.Logging_utils import Logger
from Project_1_CLMM_QA_Testnet.Page.test_page import (Homepage, allurescreenshot, slipagechecker)

@allure.label("owner", "Kunal Pipaliya QA Team")
@allure.story("Trade to swapping Functionality")

@pytest.mark.usefixtures("call_main_url")
class TestCPMM:

        allure.dynamic.description("Trade to swapping page")
        @pytest.mark.parametrize("x_token, y_token", testcase_token_name.token_pairs)
        @pytest.mark.parametrize("amount", testcase_amounts.amounts)
        # @pytest.mark.repeat(3)
        def test_7_From_Trade_to_Swap_wallet(self, call_main_url, x_token, y_token, amount):
            driver = call_main_url
            lp = Homepage(driver)

            try:
                StaticUtil.retry_click(driver, By.XPATH, lp.clickonearn())
            except InvalidSessionIdException:
                Logger.logger.error(f"❌ WebDriver session is invalid. Restarting driver...")
                driver = call_main_url()  # Re-initialize
                with allure.step(f"❌ test_2_webdriver session is invalid"):
                    allurescreenshot.take_screenshot(driver, "test_2_webdriver invalid screenshot")
                StaticUtil.retry_click(driver, By.XPATH, lp.clickonearn())

            # click on Earns to pools       
            StaticUtil.retry_click(driver, By.XPATH, lp.clickonpool())

            time.sleep(2)

            Logger.logger.info(f"✅ \n=== Starting Trade to swapping_Tab ===")
            StaticUtil.retry_click(driver, By.XPATH, lp.Title_click1())

            try:
                StaticUtil.retry_click(driver, By.XPATH, lp.click_trade())
            except InvalidSessionIdException:
                with allure.step(f"❌ test_7_WebDriver session is invalid. Restarting driver..."):
                    allurescreenshot.take_screenshot(driver, f"❌ test_7_WebDriver session is invalid. screenshot")

                Logger.logger.error(f"❌ test_7_WebDriver session is invalid. Restarting driver...")
                driver = call_main_url()  # Re-initialize
                StaticUtil.retry_click(driver, By.XPATH, lp.click_trade())

            # click on Trade to pools       
            StaticUtil.retry_click(driver, By.XPATH, lp.Tradetoswapclickk())

            slipagechecker.slipagecheck(driver)
            # driver.implicitly_wait(5)

            try:
            # Base token
                StaticUtil.retry_click(driver, By.XPATH, lp.Swapx_exchangee())
                Token_x = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, lp.tokensearch())))
                Token_x.clear()
                Token_x.send_keys(x_token)
                FA_Address_full_short.FA_Address_Full_Short_X_Token(driver)
            except:
                Logger.logger.error(f"❌ test_7_base token entering the {Token_x}")
                with allure.step(f"❌ test_7_base token entering the {Token_x}"):
                    allurescreenshot.take_screenshot(driver, f"❌ test_7_base token entering the {Token_x}")

            try:
            # Quote token
                StaticUtil.retry_click(driver, By.XPATH, lp.Swapy_exchangee())
                Token_y = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, lp.tokensearch())))
                Token_y.clear()
                Token_y.send_keys(y_token)
                FA_Address_full_short.FA_Address_Full_Short_Y_Token(driver)
            except:
                Logger.logger.error(f"❌ test_7_Quote token entering the {Token_y}")
                with allure.step(f"❌ test_7_Quote token entering the {Token_y}"):
                    allurescreenshot.take_screenshot(driver, f"❌ test_7_Quote token entering the {Token_y}")

            driver.implicitly_wait(5)
            driver.find_element(By.XPATH, lp.Swap_x_value()).send_keys(amount)

            ele_x = lp.Swap_x_onedollar_value(timeout=20)
            if ele_x:
                x_price_in_usd = ele_x.text.strip().replace('$','')
                Logger.logger.info(f"✅ test_7_{x_token} value {amount} => {x_price_in_usd}")
            else:
                with allure.step(f"❌ test_7_Could not find x_price_in_usd element"):
                    allurescreenshot.take_screenshot(driver, f"❌ test_7_Could not find x_price_in_usd element")
                Logger.logger.error(f"❌ test_7_Could not find x_price_in_usd element")

            # Check if element exists first
            driver.implicitly_wait(3)
            elements = driver.find_elements(By.XPATH, lp.Acknowl())

            if not elements:   # Means element NOT present
                Logger.logger.error(f"❌ test_7_Swap Pool is verified")
            else:              # Element present → safe to click
                with allure.step(f"✅ test_7_Element present → safe to click"):
                    allurescreenshot.take_screenshot(driver, "✅ test_7_Element present → safe to click screenshot")
                StaticUtil.retry_click(driver, By.XPATH, lp.Acknowl())
                Logger.logger.info(f"✅ test_7_Swap Pool is unverified")

            lp.eventpointerr()
            lp.scroll_botton()

            try:
                StaticUtil.retry_click(driver, By.XPATH, lp.swapbtn())
                Logger.logger.info(f"✅ test_7_Swap button is clickable and clicked")

                try:
                    Error = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, lp.swaperrormsg1())))
                    if Error.is_displayed():
                        Logger.logger.info(f"✅ test_7_Error is displayed")
                    else:
                        with allure.step(f"✅ test_7_Error is displayed"):
                            allurescreenshot.take_screenshot(driver, "test_7_Error is displayed screenshot")
                        Logger.logger.warning("⚠️ test_7_Error not displayed")
                except:
                    with allure.step(f"❌ test_7_No error message element found"):
                        allurescreenshot.take_screenshot(driver, "test_7_No error message element found screenshot")
                    Logger.logger.error(f"❌ test_7_No error message element found")
            except:
                with allure.step(f"❌ test_7_Swap button not clicked"):
                        allurescreenshot.take_screenshot(driver, f"❌ test_7_Swap button not clicked")
                Logger.logger.error(f"❌ test_7_Swap button is disabled")

            wallet_connection_class.wallet_connection(driver)
            Transaction_validation_class.Transaction_validation(driver)

            Logger.logger.info(f"✅ \n=== Completed Trade to swapping_Tab ===")

def run():
    Logger.logger.info(f"✅ Running test_7_From_Trade_to_Swap_wallet ...")
    import pytest
    pytest.main([__file__])   # this will run the tests inside this file

if __name__ == "__main__":
    run()                       