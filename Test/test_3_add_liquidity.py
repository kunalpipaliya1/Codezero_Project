import os
import re
import time
import pytest
from selenium.webdriver.common.by import By
from Project_1_CLMM_QA_Testnet.Data.users_v3 import screenshot_dir1
from Project_1_CLMM_QA_Testnet.Page.test_page import allurescreenshot, slipagechecker
from Project_1_CLMM_QA_Testnet.Page.test_page import Homepage
from Project_1_CLMM_QA_Testnet.Test.Transaction_validation import Transaction_validation_class
from Project_1_CLMM_QA_Testnet.Test.wallet_connection import wallet_connection_class
from Project_1_CLMM_QA_Testnet.Page.base_page import StaticUtil
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import datetime
import allure
from Project_1_CLMM_QA_Testnet.Test.For_loop_class import FA_Address_full_short, testcase_amounts, testcase_fee_tier, testcase_token_name
from Project_1_CLMM_QA_Testnet.Testcases_Logs.Logging_utils import Logger
from selenium.common.exceptions import InvalidSessionIdException

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
            Logger.logger.error(f"❌ Screenshot saved: {filename}")

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
        Logger.logger.info(f"✅ Selecting Fee Tier:, {target_option.text.strip()}")
        target_option.click()

        # click on continue
        StaticUtil.retry_click(driver, By.XPATH, lp.clickoncontinue())
        driver.implicitly_wait(1)
        Logger.logger.info(f"✅ click on coutinue")
        driver.implicitly_wait(5)
        time.sleep(2)

        try:
            page_validate = driver.find_element(By.XPATH, lp.provideli())
            assert "Provide Liquidity" in page_validate.text

            Logger.logger.info(f"✅ Deposite amount page validated..")
            driver.implicitly_wait(5)

            Create_pool_min_print = driver.find_element(By.XPATH, lp.Create_pool_min_print_2()).text.strip()
            Logger.logger.info(f"✅ {Create_pool_min_print}, Minimum value in v3")
            Create_pool_max_print = driver.find_element(By.XPATH, lp.Create_pool_max_print1_2()).text.strip()
            Logger.logger.info(f"✅ {Create_pool_max_print}, Maximum value in v3")
            Live_Token_price = driver.find_element(By.XPATH, lp.Live_Token_price1_2()).text.strip()
            Logger.logger.info(f"✅ {Live_Token_price}, Live token price")
            
            driver.implicitly_wait(5)
            x_deposit_Ratio_text = driver.find_element(By.XPATH, lp.x_deposit_Ratio_text1_2()).text.strip()
            Logger.logger.info(f"✅ {x_deposit_Ratio_text}, x_deposit_Ratio_text")

            x_deposit_Ratio = float(re.findall(r"[\d.]+", x_deposit_Ratio_text)[-1])
            Logger.logger.info(f"✅ {x_deposit_Ratio}, x_deposit_Ratio")

            y_deposit_Ratio_text = driver.find_element(By.XPATH, lp.y_deposit_Ratio_text1_2()).text.strip()
            Logger.logger.info(f"✅ {y_deposit_Ratio_text}, y_deposit_Ratio_text")

            y_deposit_Ratio = float(re.findall(r"[\d.]+", y_deposit_Ratio_text)[-1])
            Logger.logger.info(f"✅ {y_deposit_Ratio}, y_deposit_Ratio")

            # Python calculation
            try:
                pc = float(Live_Token_price)  # same as you send in decimal input
                pmin = float(Create_pool_min_print)
                pmax = float(Create_pool_max_print)

                pc_sqrt = pc ** 0.5
                pmin_sqrt = pmin ** 0.5
                pmax_sqrt = pmax ** 0.5

                ratio_x = (1 / pc_sqrt) - (1 / pmax_sqrt)
                ratio_y = (pc_sqrt) - (pmin_sqrt)
                ratio = ratio_y / ratio_x
                total = ratio + pc

                token0_PR = (pc / total) * 100
                token1_PR = (ratio / total) * 100

                Logger.logger.info(f"✅ ---- Token Ratio Calculation ----")
                Logger.logger.info(f"✅ pc:, {pc}")
                Logger.logger.info(f"✅ pmin:, {pmin}")
                Logger.logger.info(f"✅ pmax:, {pmax}")
                Logger.logger.info(f"✅ Total Ratio:, {total}")
                Logger.logger.info(f"✅ {x_token} Ratio %:, {token0_PR} ==  Total Amount(UI) of {x_token} %: {x_deposit_Ratio}")
                Logger.logger.info(f"✅ {y_token} Ratio %:, {token1_PR} ==  Total Amount(UI) of {y_token} %: {y_deposit_Ratio}")
                Logger.logger.info(f"✅ Difference of {x_token} position: {token0_PR - x_deposit_Ratio}")
                Logger.logger.info(f"✅ Difference of {y_token} position: {token1_PR - y_deposit_Ratio}")
                Logger.logger.info(f"✅ --------------------------------")

                allure.attach(
                    f"pc: {pc}, pmin: {pmin}, pmax: {pmax}\n"
                    f"Total Ratio: , {total}\n"
                    f"{x_token} Ratio %: {token0_PR} == Total Amount(UI) of {x_token} %: {x_deposit_Ratio}\n"
                    f"{y_token} Ratio %: {token1_PR} == Total Amount(UI) of {y_token} %: {y_deposit_Ratio}\n"
                    f"Difference of {x_token} position, token0_PR - {x_deposit_Ratio}\n"
                    f"Difference of {y_token} position, token1_PR - {y_deposit_Ratio}\n",
                    name=f"Pool calculation fee Index_{fee_index}_amount_{amount}",
                    attachment_type=allure.attachment_type.TEXT
                )
                allure.attach(
                    f"x_token={x_token}, y_token={y_token}, fee_index={fee_index}, amount={amount}",
                    name="Test_Inputs", 
                    attachment_type=allure.attachment_type.TEXT)
    
            except Exception as e:
                with allure.step("Error in CLMM calculation"):
                    allurescreenshot.take_screenshot(driver, "Error in CLMM calculation")
                allure.attach(str(e), name="CLMM_Error", attachment_type=allure.attachment_type.TEXT)
                Logger.logger.error(f"Error in CLMM calculation: {e}")

            slipagechecker.slipagecheck(driver)

            lp.inputamount(amount)
            StaticUtil.retry_click(driver, By.XPATH, lp.clickonliquidity()) 

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