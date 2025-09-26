import time, datetime, os, allure, pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import InvalidSessionIdException
from Project_1_CLMM_QA_Testnet.Page.test_page import (Homepage, allurescreenshot, slipagechecker)
from Project_1_CLMM_QA_Testnet.Page.base_page import StaticUtil
from Project_1_CLMM_QA_Testnet.Test.Transaction_validation import Transaction_validation_class
from Project_1_CLMM_QA_Testnet.Test.wallet_connection import wallet_connection_class
from Project_1_CLMM_QA_Testnet.Testcases_Logs.Logging_utils import Logger
from Project_1_CLMM_QA_Testnet.Test.For_loop_class import (testcase_amounts, testcase_token_name, FA_Address_full_short, testcase_fee_tier)
from Project_1_CLMM_QA_Testnet.Data.users_v3 import screenshot_dir1

@allure.label("owner", "Kunal Pipaliya QA Team")
@allure.story("Create pool Functionality")

@pytest.mark.usefixtures("call_main_url")
class TestPoolCreation:
    Logger.logger.info(f"✅ ==== Test 2: Create pool started ====")
    allure.dynamic.description("Create pool page")

    @pytest.mark.parametrize("x_token, y_token", testcase_token_name.token_pairs)
    @pytest.mark.parametrize("amount", testcase_amounts.amounts)
    @pytest.mark.parametrize("fee_index, fee_label", testcase_fee_tier.Fee_tier)

    def test_2_pre_create_pool(self, call_main_url, x_token, y_token, amount, fee_index, fee_label):
        driver = call_main_url
        lp = Homepage(driver)

        # for fee_index in fee_tiers:
        Logger.logger.info(f"✅ \n=== Starting pool creation attempt for Fee Tier Index and label: {fee_index} - {fee_label}, Amount: {amount} ===")

        StaticUtil.retry_click(driver, By.XPATH, lp.Title_click1())

        try:
            StaticUtil.retry_click(driver, By.XPATH, lp.clickonearn())
        except InvalidSessionIdException:
            Logger.logger.error(f"❌ WebDriver session is invalid. Restarting driver...")
            driver = call_main_url()  # Re-initialize
            with allure.step("❌ test_2_webdriver session is invalid"):
                allurescreenshot.take_screenshot(driver, "test_2_webdriver invalid screenshot")
            StaticUtil.retry_click(driver, By.XPATH, lp.clickonearn())

        # click on Earns to pools       
        StaticUtil.retry_click(driver, By.XPATH, lp.clickonpool())

        try:
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, lp.poolpagetitle1())))
        except:
            pytest.fail("test_2_Liquidity Pools page title did not appear")

            with allure.step("test_2_Liquidity Pools page title did not appear"):
                take_screenshot(driver, "test_2_Liquidity pools page title not appear screenshot")

            ss = screenshot_dir1.SCREENSHOT_DIRR
            
            os.makedirs(ss, exist_ok=True)
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = os.path.join(ss, f"test_2_Create_pool_page_title_not_found_{timestamp}.png")
            driver.save_screenshot(filename)   # Historical screenshot
            Logger.logger.error(f"❌ Screenshot saved: {filename}")

        pool_page_verify = StaticUtil.quick_wait(driver, By.XPATH, lp.poolpagetitle1())

        if not pool_page_verify:
            pytest.fail("❌ Liquidity Pools page title did not appear")

        assert "Liquidity Pools" in pool_page_verify.text.strip()

        Logger.logger.info(f"✅ Getting pool page name: {pool_page_verify.text.strip()}")
        Logger.logger.info(f"✅ Liquidity Pools page validated...!!")
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, lp.createpool1())))
        StaticUtil.retry_click(driver, By.XPATH, lp.createpool1())

        # Before the Create pool clear the objects
        try:
            StaticUtil.retry_click(driver, By.XPATH, lp.clrbtn())
            Logger.logger.info(f"✅ Create pool page cleared")
        except:
            Logger.logger.info(f"✅ ❌ test_2_Create pool page not clearing")
            with allure.step("test_2_Create pool page not clearing"):
                allurescreenshot.take_screenshot(driver, "test_2_Create pool page not clearing screenshot")

        try:
            # Base token
            StaticUtil.retry_click(driver, By.XPATH, lp.clickbasetoken())
            Token_x = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, lp.tokensearch())))
            Token_x.clear()
            Token_x.send_keys(x_token)
            FA_Address_full_short.FA_Address_Full_Short_X_Token(driver)
        except:
            Logger.logger.error(f"❌ test_2_Having error while entering the {Token_x}")
            with allure.step(f"test_2_Having error while entering the {Token_x}"):
                allurescreenshot.take_screenshot(driver, f"test_2_Having error while entering the {Token_x}")
        
        try:
            # Quote token
            StaticUtil.retry_click(driver, By.XPATH, lp.quoteetoken())
            Token_y = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, lp.tokensearch())))
            Token_y.clear()
            Token_y.send_keys(y_token)
            FA_Address_full_short.FA_Address_Full_Short_Y_Token(driver)
        except:
            Logger.logger.error(f"❌ test_2_Having error while entering the {Token_y}")
            with allure.step(f"test_2_Having error while entering the {Token_y}"):
                allurescreenshot.take_screenshot(driver, f"test_2_Having error while entering the {Token_y}")

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
        driver.implicitly_wait(1)

        # Pool creation validation
        try:
            pool_exists = None
            RecreatePool = None
            try:
                pool_exists = lp.poolexistt()
                Logger.logger.info(f"✅ Pool already exists: {pool_exists.text.strip()}")
            except:
                try:
                    RecreatePool = driver.find_element(By.XPATH, lp.RecreatePool())
                    Logger.logger.info(f"✅ Recreate pool: {RecreatePool.text.strip()}")
                except Exception as e:
                    with allure.step("test_2_Initial price element not found"):
                        allurescreenshot.take_screenshot(driver, "Initial price element not found")
                    Logger.logger.error(f"❌ test_2_Neither existing pool not 'Set initial price' found")
                    pytest.fail(f"❌ test_2_Neither existing pool not 'Set initial price' found: {e}")

            if pool_exists and "Add Liquidity" in pool_exists.text:
                try:
                    time.sleep(1)
                    StaticUtil.retry_click(driver, By.XPATH, lp.clickonliquidity())
                    Logger.logger.info(f"✅ Pool already exists for Fee Tier {pool_exists.text}")
                except Exception as e:
                    with allure.step(f"test_2_Failed to click on Add Liquidity"):
                        allurescreenshot.take_screenshot(driver, f"❌ test_2_Failed to click on Add Liquidity")
                    pytest.fail(f"❌ test_2_Failed to click on Add Liquidity: {e}")

                slipagechecker.slipagecheck(driver)
                
                driver.implicitly_wait(3)
                 # Second input box
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, lp.enterinput())))
                inbox_box = driver.find_element(By.XPATH, lp.enterinput())
                inbox_box.clear()
                inbox_box.send_keys(str(amount))

                # Final pool add click
                StaticUtil.retry_click(driver, By.XPATH, lp.clickonliquidity())

            # Case 2: Add Liquidity not in first check → recheck
            elif RecreatePool and "Set initial price" in RecreatePool.text:
            # else:
                # pool_not_exists = lp.poolexistt()
                Logger.logger.warning(f"⚠️ Recreate pool name: {RecreatePool.text}")
                
                # if "Set initial price" in RecreatePool.text.strip():
                try:
                    driver.implicitly_wait(2)
                    time.sleep(1)
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, lp.enterinput())))
                    amount_box1 = driver.find_element(By.XPATH, lp.enterinput())
                    amount_box1.clear()
                    amount_box1.send_keys(str(amount))

                    StaticUtil.retry_click(driver, By.XPATH, lp.customtab())
                    StaticUtil.retry_click(driver, By.XPATH, lp.clickoncontinue())

                    driver.implicitly_wait(2)
                    time.sleep(1)
                    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, lp.enterinput())))
                    amount_box1 = driver.find_element(By.XPATH, lp.enterinput())
                    amount_box1.clear()
                    amount_box1.send_keys(str(amount))
                    WebDriverWait(driver, 5).until(
                        lambda d: d.find_element(By.XPATH, lp.enterinput()).get_attribute("value") == str(amount)
                    )

                    # Final pool add click
                    StaticUtil.retry_click(driver, By.XPATH, lp.pooladd())
                    Logger.logger.info(f"✅ Pool created successfully")

                except Exception as e:
                    with allure.step("test_2_Failed while creating pool"):
                        allurescreenshot.take_screenshot(driver, "test_2_Failed while creating pool")
                    Logger.logger.error(f"❌ test_2_Failed while creating pool")
                    pytest.fail(f"❌ test_2_Failed while creating pool: {e}")
                    
            else:
                Logger.logger.warning(pytest.fail("❌ test_2_Unexpected pool state (neither Add Liquidity nor Set initial price)"))

        except Exception as e:
            with allure.step("test_2_Create pool failed.."):
                allurescreenshot.take_screenshot(driver, "test_2_Create pool failed..")
            
            ss = screenshot_dir1.SCREENSHOT_DIRR
            os.makedirs(ss, exist_ok=True)
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = os.path.join(ss, f"test_2_Create_pool_failed_{timestamp}.png")
            driver.save_screenshot(filename)   # Historical screenshot
            Logger.logger.error(f"❌ test_2_Screenshot saved: {filename}")
            pytest.fail(f"❌ test_2_Create pool failed due to unexpected error: {e}")


# ❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌Don't close below is import to learn❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌

    #     try:
    #         WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, lp.poolexistt())))
    #         pool_exists = lp.poolexistt()
    #         Logger.logger.info(pool_exists.text.strip())
    #     except Exception as e:
    #         self._take_screenshot(driver, "test_2_Create_pool_failed")
    #         pytest.fail(f"❌ Create pool failed: {e}")            

    #     if "Add Liquidity" in pool_exists.text.strip():
    #         self._add_liquidity(driver, lp, amount)
    #     else:
    #         self._create_pool(driver, lp, amount)
        
    #     driver.switch_to.window(driver.window_handles[0])
    #     wallet_connection_class.wallet_connection(driver)
    #     time.sleep(2)
    #     Transaction_validation_class.Transaction_validation(driver)
    #     Logger.logger.info(f"✅ === Completed attempt for Fee Tier {fee_index} ===\n")

    # # ---------- helper methods ----------
    # def _add_liquidity(self, driver, lp, amount,call_main_url):
    #     driver = call_main_url
    #     lp = Homepage(driver)
    #     StaticUtil.retry_click(driver, By.XPATH, lp.clickonliquidity())
    #     inbox_box = driver.find_element(By.XPATH, lp.enterinput())
    #     inbox_box.clear()
    #     inbox_box.send_keys(str(amount))
    #     StaticUtil.retry_click(driver, By.XPATH, lp.clickonliquidity())
    #     Logger.logger.info(f"✅ Pool already existed, liquidity added")

    # def _create_pool(self, driver, lp, amount,call_main_url):
    #     driver = call_main_url
    #     lp = Homepage(driver)
    #     amount_box = WebDriverWait(driver, 30).until(
    #         EC.presence_of_element_located((By.XPATH, lp.inputamount()))
    #     )
    #     amount_box.clear()
    #     amount_box.send_keys(str(amount))
    #     driver.find_element(By.XPATH, lp.customtab()).click()

    #     min_val = driver.find_element(By.XPATH, "(//*[@class='text-center'])[1]")
    #     max_val = driver.find_element(By.XPATH, "(//*[@class='text-center'])[2]")

    #     Logger.logger.info(f"✅ Min value: {min_val.text}, Max value: {max_val.text}")
    #     # Optional: any extra calculations here…

    #     StaticUtil.retry_click(driver, By.XPATH, lp.clickoncontinue())
    #     inbox_box = driver.find_element(By.XPATH, lp.enterinput())
    #     inbox_box.clear()
    #     inbox_box.send_keys(str(amount))
    #     StaticUtil.retry_click(driver, By.XPATH, lp.pooladd())
    #     Logger.logger.info(f"✅ Pool created successfully")

    # def _take_screenshot(self, driver, name):
    #     ss = screenshot_dir1.SCREENSHOT_DIRR
    #     os.makedirs(screenshot_dir, exist_ok=True)
    #     timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    #     filename = os.path.join(screenshot_dir, f"{name}_{timestamp}.png")
    #     driver.save_screenshot(filename)
    #     Logger.logger.error(f"❌ Screenshot saved: {filename}")

# ❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌Don't close above is import to learn❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌
        
        driver.implicitly_wait(2)
        driver.switch_to.window(driver.window_handles[0])

        wallet_connection_class.wallet_connection(driver)
        Transaction_validation_class.Transaction_validation(driver)
            
        Logger.logger.info(f"✅ === Completed attempt for Fee Tier {fee_index} ===\n")

def run():
    Logger.logger.info(f"✅ Running test_2_Create_pool ...")
    import pytest
    pytest.main([__file__])   # this will run the tests inside this file

if __name__ == "__main__":
    run()  

    