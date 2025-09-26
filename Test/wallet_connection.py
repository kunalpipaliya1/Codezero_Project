import datetime, os, allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from Project_1_CLMM_QA_Testnet.Data.users_v3 import screenshot_dir1
from Project_1_CLMM_QA_Testnet.Page.test_page import Homepage, allurescreenshot
from Project_1_CLMM_QA_Testnet.Page.base_page import StaticUtil
from Project_1_CLMM_QA_Testnet.Testcases_Logs.Logging_utils import Logger

class wallet_connection_class:
    def wallet_connection(driver):
        Logger.logger.info(f"✅ ==== Wallet connection checking process started ====")

        lp = Homepage(driver)
        driver.implicitly_wait(2)
        try:
            main_window_handle = driver.current_window_handle
        except Exception as e:
            Logger.logger.error(f"❌ Failed to get main window handle: {e}")
            return
        
        # Wait for popup
        WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)

        # Switch to popup window
        try:
            driver.switch_to.window(driver.window_handles[1])
            Logger.logger.info(f"✅ Switched to wallet window")
        except Exception as e:
            Logger.logger.error(f"❌ Failed to switch to wallet window: {e}")
            with allure.step("Failed to switch to wallet window"):
                    allurescreenshot.take_screenshot(driver, "wallet page")
            return
        
        # Click Allow/Confirm
        try:
            if StaticUtil.retry_click(driver, By.XPATH, lp.starkeyconfirmation()):
                Logger.logger.info(f"✅ Confirm clicked")
            else:
                Logger.logger.warning("⚠️ Confirm/Allow button not found after retries")
                with allure.step("wallet confirmation page error"):
                    allurescreenshot.take_screenshot(driver, "wallet page")

                driver.find_element(By.XPATH, lp.Transactionfailed()).text

                ss = screenshot_dir1.SCREENSHOT_DIRR

                os.makedirs(ss, exist_ok=True)
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                filename = os.path.join(ss, f"Transaction Failed starkey wallet_{timestamp}.png")
                driver.save_screenshot(filename)   # Historical screenshot
                Logger.logger.error(f"❌ Screenshot saved: {filename}")
                try:
                    StaticUtil.retry_click(driver, By.XPATH, lp.Transactionfailed_ok())
                    Logger.logger.warning("⚠️ Warning Transaction Failed in starkey wallet")
                except Exception as e:
                    Logger.logger.error(f"❌ If starkey wallet hanged mode try to close {e}")

                    # handles = driver.window_handles
                    # if len(handles) > 1:
                    #     driver.switch_to.window(handles[1])
                    #     driver.close()
                    #     driver.switch_to.window(handles[0])
                    # Logger.logger.info(f"✅ Closed popup and returned to main window")

        except Exception as e:
            Logger.logger.error(f"❌ button is not found")

        driver.implicitly_wait(2)

        # Switch back to main window
        try:
            driver.switch_to.window(main_window_handle)
            Logger.logger.info(f"✅ Switched back to main window. Title: {driver.title}")
        except Exception as e:
            Logger.logger.error(f"❌ Failed to switch back to main window: {e}")
        Logger.logger.info(f"✅ ==== Wallet connection checking process completed ====")        
