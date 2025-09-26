        
import time, datetime, os, allure, pytest

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import InvalidSessionIdException
from Project_1_CLMM_QA_Testnet.Test.For_loop_class import FA_Address_full_short, testcase_amounts, testcase_fee_tier, testcase_token_name
from Project_1_CLMM_QA_Testnet.Test.Transaction_validation import Transaction_validation_class
from Project_1_CLMM_QA_Testnet.Test.wallet_connection import wallet_connection_class
from Project_1_CLMM_QA_Testnet.Page.base_page import StaticUtil
from Project_1_CLMM_QA_Testnet.Testcases_Logs.Logging_utils import Logger
from Project_1_CLMM_QA_Testnet.Data.users_v3 import screenshot_dir1
from Project_1_CLMM_QA_Testnet.Page.test_page import (Homepage, allurescreenshot, slipagechecker)

@allure.label("owner", "Kunal Pipaliya QA Team")
@allure.story("Position increase Functionality")

@pytest.mark.usefixtures("call_main_url")
class TestCPMM:
    allure.dynamic.description("Position increase page")
    @pytest.mark.parametrize("x_token,y_token", testcase_token_name.token_pairs)
    @pytest.mark.parametrize("amount", testcase_amounts.amounts)
    @pytest.mark.parametrize("fee_index, fee_label", testcase_fee_tier.Fee_tier)
    def test_5_my_position_increase(self, call_main_url, x_token, y_token, amount, fee_index, fee_label):

        driver = call_main_url
        lp = Homepage(driver)
        Logger.logger.info(f"✅ \n=== Starting increase position attempt for Fee Tier Index and label: {fee_index} - {fee_label}, Amount: {amount} ===")
        StaticUtil.retry_click(driver, By.XPATH, lp.Title_click1())

        try:
            StaticUtil.retry_click(driver, By.XPATH, lp.clickonearn())
        except InvalidSessionIdException:
            with allure.step("test_5_my_position_increase"):
                allurescreenshot.take_screenshot(driver, "test_5_my_position_increase")

            Logger.logger.error(f"❌ test_5_my_position_increase")
            driver = call_main_url()  # Re-initialize
            StaticUtil.retry_click(driver, By.XPATH, lp.clickonearn())

        StaticUtil.retry_click(driver, By.XPATH, lp.clickonpool())       

        StaticUtil.retry_click(driver, By.XPATH, lp.clickonliquidity())

        StaticUtil.retry_click(driver, By.XPATH, lp.clickontokenpair())
        Token_x = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, lp.tokensearch())))
        Token_x.clear()
        Token_x.send_keys(x_token)
        FA_Address_full_short.FA_Address_Full_Short_X_Token(driver)
        
        StaticUtil.retry_click(driver, By.XPATH, lp.basequery())
        Token_y = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, lp.tokensearch())))
        Token_y.clear()
        Token_y.send_keys(y_token)
        FA_Address_full_short.FA_Address_Full_Short_Y_Token(driver)

        # Pool Type
        StaticUtil.retry_click(driver, By.XPATH, lp.pooltype())

        # 1️⃣ Click the dropdown
        dropdown_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, lp.feetierdropdown()))
        )
        dropdown_button.click()
        # time.sleep(1)  # optional, let options render

        # 2️⃣ Wait for options to appear
        options = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, lp.fetchfee()))
        )

        # 3️⃣ Select option by fee_index
        target_option = options[fee_index]  # 0,1,2,3
        Logger.logger.info(f"✅ Selecting Fee Tier:, {target_option.text.strip()}")
        target_option.click()

        # Click on continue
        StaticUtil.retry_click(driver, By.XPATH, lp.clickoncontinue())

        try:
            if not lp.poolerrorfound():
                # Direct flow
                if StaticUtil.retry_click(driver, By.XPATH, lp.myposition()):
                    Logger.logger.info(f"✅ Position found")
                else:
                    StaticUtil.retry_click(driver, By.XPATH, lp.Explorepoolclick())
                    Logger.logger.warning("⚠️ No Position found")                    
                
                StaticUtil.retry_click(driver, By.XPATH, lp.clickpo1())

                try:
                    if StaticUtil.retry_click(driver, By.XPATH, lp.positionindex6_6()):
                        Logger.logger.info(f"✅ Clicked index 6 - InActive")
                    elif StaticUtil.retry_click(driver, By.XPATH, lp.positionindex7_7()):
                        Logger.logger.warning("⚠️ Clicked index 6 - Active")
                    elif StaticUtil.retry_click(driver, By.XPATH, lp.positionindex8_8()):
                        Logger.logger.warning("⚠️ Clicked index 7 - Active")
                    elif StaticUtil.retry_click(driver, By.XPATH, lp.positionindex6_6Inactive()):
                        Logger.logger.warning("⚠️ Clicked index 8 - Active")
                    else:
                        No_position_found = driver.find_element(By.XPATH, lp.no_position_found()).text
                        Logger.logger.error(f"No any position found click on explore pool {No_position_found}")
                        
                        StaticUtil.retry_click(driver, By.XPATH, lp.positionnclick())
                        Logger.logger.error(f"❌ No matching elements found.")

                except Exception as e:
                    Logger.logger.error(f"Error occured while click on arrow >: {e}") 
                
                StaticUtil.retry_click(driver, By.XPATH, lp.clickonincrease())
                slipagechecker.slipagecheck(driver)
                driver.implicitly_wait(5)
                time.sleep(1)
                driver.find_element(By.XPATH, lp.enterinput()).send_keys(amount)
                driver.implicitly_wait(5)
                time.sleep(1)
                StaticUtil.retry_click(driver, By.XPATH, lp.increaseliquidity())
            else:
                # Indirect fallback flow
                StaticUtil.retry_click(driver, By.XPATH, lp.createpool1())
                StaticUtil.retry_click(driver, By.XPATH, lp.clickoncontinue())
                
                driver.find_element(By.XPATH, lp.enterinput()).send_keys(amount)

                StaticUtil.retry_click(driver, By.XPATH, lp.customtab())
                StaticUtil.retry_click(driver, By.XPATH, lp.clickoncontinue())

                time.sleep(1)
                driver.find_element(By.XPATH, lp.enterinput()).send_keys(amount)

                lp.scroll_botton()

                StaticUtil.retry_click(driver, By.XPATH, lp.pooladd())
        except Exception as e:
            Logger.logger.error(f"❌ Error occurred: {e}")

            ss = screenshot_dir1.SCREENSHOT_DIRR

            os.makedirs(ss, exist_ok=True)
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = os.path.join(ss, f"test_5_position_increase_failed_{timestamp}.png")
            driver.save_screenshot(filename)   # Historical screenshot
            Logger.logger.error(f"❌ Screenshot saved: {filename}")

        driver.implicitly_wait(2)
        driver.switch_to.window(driver.window_handles[0])

        wallet_connection_class.wallet_connection(driver)
        Transaction_validation_class.Transaction_validation(driver)
        
def run():
    Logger.logger.info(f"✅ Running test_5_position_increase ...")
    import pytest
    pytest.main([__file__])   # this will run the tests inside this file

if __name__ == "__main__":
    run()              