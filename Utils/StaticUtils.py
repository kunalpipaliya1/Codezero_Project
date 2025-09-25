
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Project_2_Perpetuals_QA_Testnet.Testcases_Logs.Logging_utils import Logger
import os

# Only import pyautogui if DISPLAY is available
pyautogui = None
if os.environ.get("DISPLAY"):
    try:
        import pyautogui
    except ImportError:
        pyautogui = None
    
class StaticUtil:
    @staticmethod
    def retry_click(driver, by, locator, retries = 3, delay = 5, timeout=3, fail_if_disabled=True):    
        for attempt in range(retries):
            try:
                WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((by, locator)))
                element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, locator)))
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)  
                driver.implicitly_wait(delay)
                element.click()
                return element

            except Exception as e:
                Logger.logger.error(f"[{attempt+1}/{retries}] Retrying click on '{locator}' due to: {str(e).splitlines()[0]}")        # str(e).splitlines()[0]-- Avoid printing full stacktrace
                # driver.implicitly_wait(delay)
    
        msg = f"❌ Failed to click on element after {retries} retries: {locator}"
        if fail_if_disabled:
            Logger.logger.error(msg)
            raise TimeoutException(msg)
        else:
            Logger.logger.warning(f"⚠️ {msg} — proceeding without failure (button might be disabled)")
            return None
    
    def quick_wait(driver, by, locator, timeout=3):
        """Try to find element quickly, else return None."""
        try:
            return WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located((by, locator))
            )
        except TimeoutException:
            return None

