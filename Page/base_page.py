
# allure screenshot #

import allure
# class allurescreenshot:
#     def take_screenshot(driver, name="screenshot"):
#         allure.attach(driver.get_screenshot_as_png(), name=name, attachment_type=allure.attachment_type.PNG)

# slipage added #



# Retry Click method #

import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Project_1_CLMM_QA_Testnet.Page.test_page import allurescreenshot
from Project_1_CLMM_QA_Testnet.Testcases_Logs.Logging_utils import Logger

pyautogui = None
if os.environ.get("DISPLAY"):
    try:
        import pyautogui
    except ImportError:
        pyautogui = None

class StaticUtil:
    @staticmethod
    def retry_click(driver, by, locator, retries = 3, delay = 10, timeout=3):    
        for attempt in range(retries):
            try:
                driver.implicitly_wait(delay)
                WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((by, locator)))
                element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, locator)))
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)  
                element.click()
                driver.implicitly_wait(delay)
                return element
            except Exception as e:
                Logger.logger.error(f"❌ [{attempt+1}/{retries}] Retrying click on '{locator}' due to: {str(e).splitlines()[0]}")        # str(e).splitlines()[0]-- Avoid printing full stacktrace
                with allure.step(f"Failed to click on element static util"):
                    allurescreenshot.take_screenshot(driver, "Failed to click on element static util")

                allure.attach(f"Failed to click on element static util", name=f"Retrying click on '{locator}' - Attempt: {attempt+1}", attachment_type=allure.attachment_type.TEXT)
                # driver.refresh()

        Logger.logger.error(f"❌ Failed to click on element after {retries} retries: {locator}")
        raise TimeoutException(f"Element not clickable after {retries} retries: {locator}")
    

    @staticmethod
    def quick_wait(driver, by, locator, timeout=3):
        """Try to find element quickly, else return None."""
        try:
            return WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located((by, locator))
            )
        except:
            return None

    @staticmethod

    def Fluent_wait_and_click(driver, by, locator, timeout=15, poll_frequency=0.5):
        """Wait for an element to be clickable and click it using pyautogui if available."""
        try:
            element = WebDriverWait(driver, timeout, poll_frequency).until(
                EC.element_to_be_clickable((by, locator))
            )
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            element.click()
            Logger.logger.info(f"✅ Clicked element '{locator}' successfully")
        except Exception as e:
            Logger.logger.error(f"❌ Fluent wait failed for '{locator}': {str(e).splitlines()[0]}")
            raise

