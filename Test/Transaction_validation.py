import allure
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Project_1_CLMM_QA_Testnet.Page.test_page import Homepage
from Project_1_CLMM_QA_Testnet.Data.users_v3 import screenshot_dir1
from Project_1_CLMM_QA_Testnet.Page.base_page import StaticUtil
from Project_1_CLMM_QA_Testnet.Testcases_Logs.Logging_utils import Logger

class Transaction_validation_class:
    def Transaction_validation(driver):
        Logger.logger.info(f"✅ ==== Transaction Validation started ====")

        # driver = call_main_url
        lp = Homepage(driver)
        try:
            WebDriverWait(driver, 60).until(EC.visibility_of_any_elements_located((By.XPATH, lp.tx_validation())))
            Logger.logger.info(f"✅ Transaction validation element is visible")
            
        except:
            driver.save_screenshot(screenshot_dir1.SCREENSHOT_DIRR_Transaction)
            Logger.logger.error(f"❌ Transaction validation element not found within 60s", "Navigate to back window")
            driver.refresh()

        Transaction_view = driver.find_element(By.XPATH, lp.txviewsection())
        Supra_scan_href = f"{Transaction_view.text.strip()} -> {Transaction_view.get_attribute('href')}"

        Logger.logger.info(Supra_scan_href)
        allure.attach(f"Supra_scan_href_address: {Supra_scan_href}", name="Supra_Scan href", attachment_type=allure.attachment_type.TEXT)

        try:

            # Wait for transaction status to appear
            Transaction_status = WebDriverWait(driver, 15).until(
                EC.visibility_of_element_located((By.XPATH, lp.txsubmitt()))
            )
            status_text = Transaction_status.text.strip()
            Logger.logger.info(f"ℹ️ Transaction status: {status_text}")
            
            StaticUtil.retry_click(driver, By.XPATH, lp.viewexpo())

            driver.switch_to.window(driver.window_handles[1])
            # time.sleep(2)
            driver.implicitly_wait(2)

            # supra scan enter:
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, lp.txfindstatus())))
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, lp.vmstatuscheck())))

            User_transaction_status = driver.find_element(By.XPATH, lp.txfindstatus()).text.strip()
            Logger.logger.info(f"✅ After switch to supra scan check title: {driver.title}")

            if "Transaction Submitted" in status_text and User_transaction_status == "Success":
                VM_Status = driver.find_element(By.XPATH, lp.vmstatuscheck()).text.strip()
                Logger.logger.info(f"✅ Success Transaction: {VM_Status}")

            elif "Transaction Failed" in status_text or User_transaction_status == "Failed":
                driver.save_screenshot(screenshot_dir1.SCREENSHOT_DIRR_Transaction)
                VM_Status = driver.find_element(By.XPATH, lp.vmstatuscheck()).text.strip()
                driver.save_screenshot(screenshot_dir1.SCREENSHOT_DIRR_Transaction)
                Logger.logger.info(f"✅ ❌ Failed Transaction: {VM_Status}")

            else:
                Logger.logger.warning(f"⚠️ Unexpected transaction status: {status_text}, user status: {User_transaction_status}")

            try:
                Sender_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, lp.senderelement1()))
                )
                Sender_text = Sender_element.text.strip()
                Sender_href = Sender_element.get_attribute('href')
                Logger.logger.info(f"✅ Sender: {Sender_text} -> {Sender_href}")
                allure.attach(f"Sender: {Sender_text} -> {Sender_href}", name="Sender_element", attachment_type=allure.attachment_type.TEXT)
            except TimeoutException:
                Logger.logger.error(f"❌ Sender element not found")
                driver.save_screenshot(screenshot_dir1.SCREENSHOT_DIRR_Transaction)

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
                driver.save_screenshot(screenshot_dir1.SCREENSHOT_DIRR_Transaction)

        except (TimeoutException, NoSuchElementException) as e:
            driver.save_screenshot(screenshot_dir1.SCREENSHOT_DIRR_Transaction)
            Logger.logger.error(f"❌ Exception while checking transaction: {e}")

        # ✅ Close transaction popup (index 1) and go back to main window
        try:
            try:
                if len(driver.window_handles) > 1:
                    driver.switch_to.window(driver.window_handles[-1])
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
                    Logger.logger.info(f"✅ Closed transaction popup and returned to main window")
                else:
                    Logger.logger.info(f"✅ No popup window to close")
            except Exception as e:
                Logger.logger.error(f"⚠️ Error closing popup: {e}")

            driver.switch_to.window(driver.window_handles[0])  # back to main
            Logger.logger.info(f"✅ Back to main window after closing popup")

        except Exception as e:
            Logger.logger.error(f"⚠️ Error while closing transaction popup: {e}")

        StaticUtil.retry_click(driver, By.XPATH, lp.txclose1())
        driver.implicitly_wait(2)
        Logger.logger.info(f"✅ ==== Transaction Validation completed ====")
            



