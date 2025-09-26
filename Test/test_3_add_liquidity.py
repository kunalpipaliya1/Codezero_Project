
import time, os, re, allure, pytest, datetime
from selenium.webdriver.common.by import By
from selenium.common.exceptions import InvalidSessionIdException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Project_1_CLMM_QA_Testnet.Test.For_loop_class import (FA_Address_full_short, testcase_amounts, testcase_fee_tier, testcase_token_name)
from Project_1_CLMM_QA_Testnet.Testcases_Logs.Logging_utils import Logger
from Project_1_CLMM_QA_Testnet.Data.users_v3 import screenshot_dir1
from Project_1_CLMM_QA_Testnet.Page.test_page import (Homepage, allurescreenshot, slipagechecker)
from Project_1_CLMM_QA_Testnet.Test.Transaction_validation import Transaction_validation_class
from Project_1_CLMM_QA_Testnet.Test.wallet_connection import wallet_connection_class
from Project_1_CLMM_QA_Testnet.Page.base_page import StaticUtil
from Project_1_CLMM_QA_Testnet.Utils.CalculationUtils import CalculationUtils

@allure.label("owner", "Kunal Pipaliya QA Team")
@allure.story("Add liquidity on pool Functionality")

@pytest.mark.usefixtures("call_main_url")
class TestAddLiquidity: 
    allure.dynamic.description("Add liquidity page")
    @pytest.mark.parametrize("x_token, y_token", testcase_token_name.token_pairs)
    @pytest.mark.parametrize("amount", testcase_amounts.amounts)
    @pytest.mark.parametrize("fee_index, fee_label", testcase_fee_tier.Fee_tier)
    def test_3_add_Liquidity(self, call_main_url, x_token, y_token, amount, fee_index, fee_label):
        driver = call_main_url
        lp = Homepage(driver)
                    
        Logger.logger.info(f"✅ \n=== Starting Add liquidity attempt for Fee Tier Index and label: {fee_index} - {fee_label}, Amount: {amount} ===")
        
        StaticUtil.retry_click(driver, By.XPATH, lp.Title_click1())

        try:
            StaticUtil.retry_click(driver, By.XPATH, lp.clickonearn())
        except InvalidSessionIdException:
            with allure.step("test_3_WebDriver session is invalid. Restarting driver..."):
                allurescreenshot.take_screenshot(driver, "test_3_WebDriver session is invalid.")

            Logger.logger.error(f"❌ test_3_WebDriver session is invalid. Restarting driver...")
            driver = call_main_url()  # Re-initialize
            StaticUtil.retry_click(driver, By.XPATH, lp.clickonearn())

        StaticUtil.retry_click(driver, By.XPATH, lp.clickonpool())

        try:
            StaticUtil.retry_click(driver, By.XPATH, lp.clickonliquidity())
        except Exception as e:

            with allure.step("test_3_Add_liquidity_click_on_liquidity_failed"):
                allurescreenshot.take_screenshot(driver, "test_3_Add_liquidity_click_on_liquidity_failed")

            ss = screenshot_dir1.SCREENSHOT_DIRR

            os.makedirs(ss, exist_ok=True)
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = os.path.join(ss, f"test_3_Add_liquidity_click_on_liquidity_failed_{timestamp}.png")
            driver.save_screenshot(filename)   # Historical screenshot
            Logger.logger.error(f"❌ test_3_Screenshot saved: {filename}")

        try:
            # Base token
            StaticUtil.retry_click(driver, By.XPATH, lp.clickontokenpair())
            Token_x = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, lp.clickonxy())))
            Token_x.clear()
            Token_x.send_keys(x_token)
            FA_Address_full_short.FA_Address_Full_Short_X_Token(driver)
        except:
            Logger.logger.error(f"❌ test_3_Having error while entering the {Token_x}")
            with allure.step(f"test_3_Having error while entering the {Token_x}"):
                allurescreenshot.take_screenshot(driver, f"test_3_Having error while entering the {Token_x}")

        try:
            # Quote token
            StaticUtil.retry_click(driver, By.XPATH, lp.basequery())
            Token_y = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, lp.clickonxy())))
            Token_y.clear()
            Token_y.send_keys(y_token)
            FA_Address_full_short.FA_Address_Full_Short_Y_Token(driver)
        except:
            Logger.logger.error(f"❌ test_3_Having error while entering the {Token_y}")
            with allure.step(f"test_3_Having error while entering the {Token_y}"):
                allurescreenshot.take_screenshot(driver, f"test_3_Having error while entering the {Token_y}")

        Logger.logger.info(f"✅ x and y amount is entered")

        StaticUtil.retry_click(driver, By.XPATH, lp.concen_v3_tab())

        # 1️⃣ Click the dropdown
        dropdown_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, lp.feetierdropdown())) 
        )
        dropdown_button.click()
        driver.implicitly_wait(1)  # optional, let options render

        # 2️⃣ Wait for options to appear
        options = WebDriverWait(driver, 20).until(
            EC.visibility_of_all_elements_located((By.XPATH, lp.fetchfee()))
        )

        # 3️⃣ Select option by fee_index
        target_option = options[fee_index]  # 0,1,2,3
        Logger.logger.info(f"✅ test_3_Selecting Fee Tier:, {target_option.text.strip()}")
        target_option.click()

        # click on continue
        StaticUtil.retry_click(driver, By.XPATH, lp.clickoncontinue())
        driver.implicitly_wait(1)
        Logger.logger.info(f"✅ test_3_click on coutinue")
        driver.implicitly_wait(5)
        time.sleep(2)

        try:
            page_validate = driver.find_element(By.XPATH, lp.provideli())
            assert "Provide Liquidity" in page_validate.text

            Logger.logger.info(f"✅ test_3_Deposite amount page validated..")
            driver.implicitly_wait(5)

            CalculationUtils.calculate_apr(driver, x_token, y_token, fee_index, amount)

            slipagechecker.slipagecheck(driver)

            driver.find_element(By.XPATH, lp.inputamount()).send_keys(amount)
            time.sleep(0.5)

            x_token_value = driver.find_element(By.XPATH, "(//*[@class='text-lighterGray text-sm'])[1]").text
            y_token_value = driver.find_element(By.XPATH, "(//*[@class='text-lighterGray text-sm'])[2]").text

            try:
                StaticUtil.retry_click(driver, By.XPATH, lp.clickonliquidity())
                Logger.logger.info(f"✅ test_3_Add liquidity button found and clicked")
            except Exception as e:
                Error_element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//button[span[contains(text(), 'Insufficient balance')]]")))
                Error_element_text = Error_element.text
                print(Error_element_text)
                if Error_element_text.is_displayed():
                    Logger.logger.error(f"❌ test_3_Insufficient balance button found skip the test: {e}")
                    with allure.step("❌ test_3_Insufficient balance button found skip the test"):
                        allure.attach(f"x token name: {x_token_value} --> x token name:{y_token_value}", name="x_y_token_name", attachment_type=allure.attachment_type.TEXT)

                        allurescreenshot.take_screenshot(driver, "❌ test_3_Insufficient balance button found skip the test screenshot")
                    pytest.skip("❌ test_3_Insufficient balance button found skip the test") 

        except:
            with allure.step("Pool not found"):
                allurescreenshot.take_screenshot(driver, "Pool not found")
            Logger.logger.error(f"❌ Pool not found")
            driver.implicitly_wait(5)
            
            StaticUtil.retry_click(driver, By.XPATH, lp.createpool1())
            StaticUtil.retry_click(driver, By.XPATH, lp.clickoncontinue())
            lp.inputamount(amount)
            StaticUtil.retry_click(driver, By.XPATH, lp.customtab())
            StaticUtil.retry_click(driver, By.XPATH, lp.clickoncontinue())
            driver.implicitly_wait(5)
            lp.inputamount(amount)
            StaticUtil.retry_click(driver, By.XPATH, lp.pooladd())

        wallet_connection_class.wallet_connection(driver)
        Transaction_validation_class.Transaction_validation(driver)       
        Logger.logger.info(f"✅ === Completed attempt for Fee Tier {fee_index} ===\n")

def run():
    Logger.logger.info(f"✅ Running test_3_add_liquidity ...")
    import pytest
    pytest.main([__file__])   # this will run the tests inside this file

if __name__ == "__main__":
    run()  