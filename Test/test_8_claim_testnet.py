import re
import time
import allure
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Project_1_CLMM_QA_Testnet.Data.users_v3 import wallet_details
from Project_1_CLMM_QA_Testnet.Page.test_page import allurescreenshot
from Project_1_CLMM_QA_Testnet.Page.test_page import Homepage
from Project_1_CLMM_QA_Testnet.Testcases_Logs.Logging_utils import Logger
from Project_1_CLMM_QA_Testnet.Page.base_page import StaticUtil
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException

@allure.label("owner", "Kunal Pipaliya QA Team")
@allure.story("Homepage claim Functionality")

@pytest.mark.usefixtures("call_main_url")
class TestCPMM:  
    def test_8_claim_testnet(self, call_main_url):
        allure.dynamic.description("Claim page")
        driver = call_main_url
        lp = Homepage(driver)
        Logger.logger.info(f"✅ === Starting claim testnet ===\n")

        # Click on claim button
        StaticUtil.retry_click(driver, By.XPATH, lp.Title_click1())
        time.sleep(2)
        StaticUtil.retry_click(driver, By.XPATH, lp.Homepage_claim1())

        try:
            main_window_handle = driver.current_window_handle
        except Exception as e:
            with allure.step(f"❌ test_8_Failed to get main window handle"):
                allurescreenshot.take_screenshot(driver, f"❌ test_8_Failed to get main window handle")
            pytest.fail(f"❌ test_8_Failed to get main window handle: {e}")
        driver.implicitly_wait(2)
        time.sleep(2)

        handles = driver.window_handles
        if len(handles) > 1:
            driver.switch_to.window(handles[1])
            Logger.logger.info(f"✅ new window detected; move to main window")

        else:
            with allure.step(f"⚠️ test_8_No new window detected; staying on main window"):
                allurescreenshot.take_screenshot(driver, f"⚠️ test_8_No new window detected; staying on main window")
            Logger.logger.warning("⚠️ test_8_No new window detected; staying on main window")
            return
           
        try:
            password_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, lp.wallet_password_1()))
            )
            password_input.send_keys(wallet_details.Password)
            StaticUtil.retry_click(driver, By.XPATH, lp.wallet_login_btn_1())
        except Exception as e:
            with allure.step(f"✅ test_8_Wallet login not required, skipping. screenshot"):
                allurescreenshot.take_screenshot(driver, f"✅ test_8_Wallet login not required, skipping.")
            Logger.logger.info(f"✅ test_8_Wallet login not required, skipping.")

        # Handle message popup
        actual_result = None
        # try:
        element = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(
                (By.XPATH, lp.wallet_popup_msg_1())
            )
        )
        actual_result = element.text.strip()
        Logger.logger.info(f"✅ test_8_result: {actual_result}")

        if actual_result == "Simulation executed successfully.":
            time.sleep(2)
            try:
                driver.switch_to.window(main_window_handle)
                msg_pop_up = WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located((By.XPATH, "//*[@class='ui-text-sm ui-opacity-90']"))
                )
                msg_pop_up_validate = "USDC successfully claimed!"
                assert msg_pop_up.text.strip() == msg_pop_up_validate, f"Expected pop-up message to be '{msg_pop_up_validate}', but got '{msg_pop_up.text.strip()}'"
                
                Logger.logger.info(f"✅ test_8_Claimed is successfully Pop-UP message is present : {msg_pop_up.text.strip()}")
            except Exception as e:
                with allure.step(f"❌ test_8_Claimed is successfully Pop-UP message is absent screenshot"):
                    try:
                        allurescreenshot.take_screenshot(driver, f"❌ test_8_Claimed is successfully Pop-UP message is absent screenshot")
                    except WebDriverException as e:
                        Logger.logger.error(f"❌ test_8_Claimed is successfully Pop-UP message is absent: {e}")

            StaticUtil.retry_click(driver, By.XPATH, lp.starkeyconfirmation())
            Logger.logger.info(f"✅ Starkey confirmation clicked after success message.")

        elif re.search(r"Transaction simulation failed.*E_MINT_LIMIT_EXCEEDED\(0x3\)", actual_result, re.S):
            with allure.step(f"✅ test_8_Transaction simulation failed. working as expected. screenshot"):
                allurescreenshot.take_screenshot(driver, f"✅ test_8_Transaction simulation failed. working as expected.")
            Logger.logger.info(f"✅ test_8_Transaction simulation failed. working as expected.")

            StaticUtil.retry_click(driver, By.XPATH, lp.starkeyconfirmation())

            try:
                driver.switch_to.window(main_window_handle)
                msg_pop_up = WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located((By.XPATH, "//*[@class='ui-text-sm ui-opacity-90']"))   # lp.msg_pop_up_below_1()
                )
                msg_pop_up_validate = "You have already claimed USDC once in the past 24 hours. Please try again tomorrow."
                assert msg_pop_up.text.strip() == msg_pop_up_validate, f"Expected pop-up message to be '{msg_pop_up_validate}', but got '{msg_pop_up.text.strip()}'"
                Logger.logger.info(f"✅ test_8_Claimed is failed Pop-UP message is present : {msg_pop_up.text.strip()}")
            except WebDriverException as e:
                Logger.logger.error(f"❌ Could not find pop-up or browser is closed: {e}")
            except Exception as e:
                with allure.step(f"⚠️ test_8_Claimed is failed Pop-UP message is absent screenshot"): 
                    try:
                        allurescreenshot.take_screenshot(driver, f"⚠️ test_8_Claimed is failed Pop-UP message is absent screenshot")
                    except WebDriverException as e:
                        Logger.logger.error(f"❌ test_8_Claimed is failed Pop-UP message is absent: {e}")

        else:
            with allure.step(f"❌ test_8_No message pop-up in wallet"):
                allurescreenshot.take_screenshot(driver, f"❌ test_8_No message pop-up in wallet")
            Logger.logger.error(f"❌ test_8_No message pop-up in wallet")
           
        try:
            ### --- EXTRA CHECK before switching back ---
            if main_window_handle in driver.window_handles:
                driver.switch_to.window(main_window_handle)
                Logger.logger.info(f"✅ test_8_Switched back to main window. Title: {driver.title}")
            else:
                Logger.logger.warning("⚠️ Main window handle not found in current handles; cannot switch back.")
        except Exception as e:
            with allure.step(f"⚠️ test_8_Failed to switch back to main window: {e}"):
                allurescreenshot.take_screenshot(driver, f"⚠️ test_8_Failed to switch back to main window: {e}")
            Logger.logger.error(f"⚠️ test_8_Failed to switch back to main window: {e}")
    
        Logger.logger.info(f"✅ === Completed claim testnet ===\n")

def run():
    Logger.logger.info(f"✅ Running test_8_claim_testnet ...")
    import pytest
    pytest.main([__file__])

if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        print("\nStopped by user.")