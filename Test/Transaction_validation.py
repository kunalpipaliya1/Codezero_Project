        
import pytest
from selenium import webdriver
from Project_2_Perpetuals_QA_Testnet.Data.user_perps import screenshot_dir1
from Project_2_Perpetuals_QA_Testnet.Page.base_page import allurescreenshot
from Project_2_Perpetuals_QA_Testnet.Page.test_page import Launchpage
from selenium.webdriver.chrome.options import Options
import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from Project_2_Perpetuals_QA_Testnet.Utils.StaticUtils import StaticUtil
import datetime
import allure
from Project_2_Perpetuals_QA_Testnet.Testcases_Logs.Logging_utils import Logger

class Transaction_validation_class:
    def Transaction_validation(driver):
        Logger.logger.info(f"✅ ==== Transaction Validation started ====")

        # driver = call_main_url
        lp = Launchpage(driver)
        try:
            WebDriverWait(driver, 60).until(EC.visibility_of_any_elements_located((By.XPATH, lp.tx_validation())))
            Logger.logger.info(f"✅ Transaction validation element is visible")
            
        except:
            Logger.logger.error(f"❌ Transaction validation element not found within 60s", "To refresh")
            with allure.step("View Exp. pop-up not visible"):
                    allurescreenshot.take_screenshot(driver, "Transaction page pop-up")
            driver.refresh()
        driver.implicitly_wait(5)
        Transaction_view = driver.find_element(By.XPATH, lp.txviewsection())
        Supra_scan_href = f"{Transaction_view.text.strip()} -> {Transaction_view.get_attribute('href')}"
        # driver.switch_to.window(driver.window_handles[-1])

        Logger.logger.info(f"✅ Supra_scan_href_address: {Supra_scan_href}")
        allure.attach(f"Supra_scan_href_address: {Supra_scan_href}", name="Supra_Scan href", attachment_type=allure.attachment_type.TEXT)

        try:
            # Wait for transaction status to appear
            Transaction_status = WebDriverWait(driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, lp.txsubmitt()))
            )
            status_text = Transaction_status.text.strip()
            Logger.logger.info(f"ℹ️ Transaction status: {status_text}")

            driver.implicitly_wait(5)
            time.sleep(2)           
            StaticUtil.retry_click(driver, By.XPATH, lp.viewexpo())

            driver.switch_to.window(driver.window_handles[1])
            driver.implicitly_wait(5)            

            # supra scan enter:
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, lp.txfindstatus())))
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, lp.vmstatuscheck())))

            User_transaction_status = driver.find_element(By.XPATH, lp.txfindstatus()).text.strip()
            Logger.logger.info(f"✅ After switch to supra scan check title: {driver.title}")

            if "Transaction submitted" in status_text and User_transaction_status == "Success":
                VM_Status = driver.find_element(By.XPATH, lp.vmstatuscheck()).text.strip()
                Logger.logger.info(f"✅ Success Transaction: {VM_Status}")

            elif "Transaction Failed" in status_text or User_transaction_status == "Failed":
                VM_Status = driver.find_element(By.XPATH, lp.vmstatuscheck()).text.strip()
                Logger.logger.info(f"✅ ❌ Failed Transaction: {VM_Status}")

                with allure.step("Transaction Failed screenshots"):
                    allurescreenshot.take_screenshot(driver, "Transaction page status")

            else:
                Logger.logger.warning(f"⚠️ Unexpected transaction status: {status_text}, user status: {User_transaction_status}")
                with allure.step("Unexpected transaction status"):
                    allurescreenshot.take_screenshot(driver, "Transaction page")

            try:
                Sender_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, lp.senderelement1()))
                )
                Sender_text = Sender_element.text.strip()
                Sender_href = Sender_element.get_attribute('href')
                Logger.logger.info(f"✅ Sender: {Sender_text} -> {Sender_href}")
                allure.attach(f"Sender: {Sender_text} -> {Sender_href}", name="Sender_element", attachment_type=allure.attachment_type.TEXT)

                with allure.step("Success Transaction Screenshot"):
                    allurescreenshot.take_screenshot(driver, "Supra scan page")

            except TimeoutException:
                Logger.logger.error(f"❌ Sender element not found")
                with allure.step("Sender element not found"):
                    allurescreenshot.take_screenshot(driver, "Supra_scan_page")

            try:
                Recipient_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, lp.receiverelement1()))
                )

                Recipient_text = Recipient_element.text.strip()
                Recipient_href = Recipient_element.get_attribute('href')
                Logger.logger.info(f"✅ Recipient: {Recipient_text} -> {Recipient_href}")
                allure.attach(f"Recipient: {Recipient_text} -> {Recipient_href}", name="Recipient_element", attachment_type=allure.attachment_type.TEXT)
            except TimeoutException:
                Logger.logger.error(f"❌ Recipient element not found")

                with allure.step("Recipient element not found"):
                    allurescreenshot.take_screenshot(driver, "Supra_scan_page")

        except (TimeoutException, NoSuchElementException) as e:
            Logger.logger.error(f"❌ Exception while checking transaction: {e}")
            with allure.step("Exception while checking transaction"):
                    allurescreenshot.take_screenshot(driver, "Supra_scan_page")


        driver.switch_to.window(driver.window_handles[-1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        driver.implicitly_wait(5)            
        # WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, lp.txclose1())))
        

        # # ✅ Close transaction popup (index 1) and go back to main window
        # try:
        #     try:
        #         if len(driver.window_handles) > 1:
        #             driver.switch_to.window(driver.window_handles[-1])
        #             driver.close()
        #             driver.switch_to.window(driver.window_handles[0])
        #             Logger.logger.info(f"✅ Closed transaction popup and returned to main window")
        #         else:
        #             Logger.logger.info(f"✅ No popup window to close")
        #     except Exception as e:
        #         Logger.logger.error(f"⚠️ Error closing popup: {e}")

        #         driver.switch_to.window(driver.window_handles[0])  # back to main
        #         Logger.logger.info(f"✅ Back to main window after closing popup")

        # except Exception as e:
        #     Logger.logger.error(f"⚠️ Error while closing transaction popup: {e}")

        StaticUtil.retry_click(driver, By.XPATH, lp.txclose1())

        
        Logger.logger.info(f"✅ ==== Transaction Validation completed ====")
            



