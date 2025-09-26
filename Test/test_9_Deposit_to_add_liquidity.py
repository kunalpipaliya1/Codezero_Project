import time, allure, pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import InvalidSessionIdException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Project_1_CLMM_QA_Testnet.Test.For_loop_class import (testcase_amounts, Deposite_to_add_liq)
from Project_1_CLMM_QA_Testnet.Testcases_Logs.Logging_utils import Logger
from Project_1_CLMM_QA_Testnet.Page.test_page import (Homepage, allurescreenshot, slipagechecker)
from Project_1_CLMM_QA_Testnet.Test.Transaction_validation import Transaction_validation_class
from Project_1_CLMM_QA_Testnet.Test.wallet_connection import wallet_connection_class
from Project_1_CLMM_QA_Testnet.Page.base_page import StaticUtil
from Project_1_CLMM_QA_Testnet.Utils.CalculationUtils import CalculationUtils

@allure.label("owner", "Kunal Pipaliya QA Team")
@allure.story("Deposit to Add liquidity pool Functionality")
@pytest.mark.parametrize("index", Deposite_to_add_liq.for_loop)
@pytest.mark.usefixtures("call_main_url")
class TestAddLiquidity: 
    allure.dynamic.description("Add liquidity page")
    @pytest.mark.parametrize("amount", testcase_amounts.amounts)
    def test_9_Deposit_to_add_liquidity(self, call_main_url, amount, index):
        driver = call_main_url
        lp = Homepage(driver)
           
        # for index, button in enumerate(deposit_buttons):
        Logger.logger.info(f"✅ test_9_Processing Deposit button {index + 1}")
        StaticUtil.retry_click(driver, By.XPATH, lp.Title_click1())

        try:
            StaticUtil.retry_click(driver, By.XPATH, lp.clickonearn())
        except InvalidSessionIdException:
            with allure.step("test_9_WebDriver session is invalid. Restarting driver..."):
                allurescreenshot.take_screenshot(driver, "test_9_WebDriver session is invalid.")

            Logger.logger.error(f"❌ test_9_WebDriver session is invalid. Restarting driver...")
            driver = call_main_url()  # Re-initialize
            StaticUtil.retry_click(driver, By.XPATH, lp.clickonearn())
        time.sleep(0.3)
        StaticUtil.retry_click(driver, By.XPATH, lp.clickonpool())

        driver.execute_script("window.scrollBy(0, 400);")

        # Pools = driver.find_element(By.XPATH, lp.Poolss())
        # Pool_size = driver.find_element(By.XPATH, lp.Pool_sizee())

        Pools = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, lp.Poolss()))).text
        Pool_size = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, lp.Pool_sizee()))).text
        driver.implicitly_wait(5)
        
        allure.attach(f"Pool Type: {Pools} and {Pool_size}", name="Pool Type", attachment_type=allure.attachment_type.TEXT)

        allurescreenshot.take_screenshot(driver, "Total pool size screenshot")

        button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, f"(//*[text()='Deposit'])[{index+1}]"))
        )
        button.click()
        Logger.logger.info(f"✅ test_9_Clicked Deposit button {index + 1}")
        

        try:
            page_validate = driver.find_element(By.XPATH, lp.provideli())
            assert "Provide Liquidity" in page_validate.text
            Logger.logger.info(f"✅ test_9_Deposit page validated for button {index + 1}")

            CalculationUtils.calculate_apr(driver, amount)
            slipagechecker.slipagecheck(driver)
            driver.find_element(By.XPATH, lp.inputamount()).send_keys(amount)
            time.sleep(0.5)

            x_token_value = driver.find_element(By.XPATH, lp.x_toke_valuee()).text
            y_token_value = driver.find_element(By.XPATH, lp.y_toke_valuee()).text

            if StaticUtil.retry_click(driver, By.XPATH, lp.clickonliquidity()):
                Logger.logger.info(f"✅ test_9_Add liquidity button found and clicked")
            else:
                Error_element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, lp.Error_elementt())))
                Error_element_text = Error_element.text
                print(Error_element_text)
                if Error_element_text.is_displayed():
                    Logger.logger.error(f"❌ test_9_Insufficient balance button found skip the test")
                    with allure.step("❌ test_9_Insufficient balance button found skip the test"):
                        allure.attach(f"x token name: {x_token_value} --> x token name:{y_token_value}", name="x_y_token_name", attachment_type=allure.attachment_type.TEXT)

                        allurescreenshot.take_screenshot(driver, "❌ test_9_Insufficient balance button found skip the test screenshot")
                    pytest.skip("❌ test_9_Insufficient balance button found skip the test")

        except:
            with allure.step("Pool not found"):
                allurescreenshot.take_screenshot(driver, f"Pool not found for button {index + 1}")
            Logger.logger.error(f"❌ Pool not found for button {index + 1}")
            
            StaticUtil.retry_click(driver, By.XPATH, lp.createpool1())
            StaticUtil.retry_click(driver, By.XPATH, lp.clickoncontinue())
            driver.implicitly_wait(5)
            driver.find_element(By.XPATH, lp.inputamount()).send_keys(amount)

            StaticUtil.retry_click(driver, By.XPATH, lp.customtab())
            StaticUtil.retry_click(driver, By.XPATH, lp.clickoncontinue())
            driver.implicitly_wait(5)
            driver.find_element(By.XPATH, lp.inputamount()).send_keys(amount)

            StaticUtil.retry_click(driver, By.XPATH, lp.pooladd())

        wallet_connection_class.wallet_connection(driver)
        Transaction_validation_class.Transaction_validation(driver)       
        Logger.logger.info(f"✅ Processing Deposit button {index + 1} completed")

def run():
    Logger.logger.info(f"✅ Running test_9_Deposit_to_add_liquidity ...")
    import pytest
    pytest.main([__file__])   # this will run the tests inside this file

if __name__ == "__main__":
    run()  