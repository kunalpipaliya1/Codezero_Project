# from lib2to3.pgen2 import driver
import allure, re
from Project_1_CLMM_QA_Testnet.Testcases_Logs.Logging_utils import Logger
from selenium.webdriver.common.by import By
from Project_1_CLMM_QA_Testnet.Page.test_page import (Homepage, allurescreenshot, slipagechecker)

class CalculationUtils:
    @staticmethod
    def extract_and_pool_data(driver):
        lp = Homepage(driver)

        # Extract and log pool data
        Create_pool_min_print = driver.find_element(By.XPATH, lp.Create_pool_min_print_2()).text.strip()
        Logger.logger.info(f"✅ Minimum value in v3: {Create_pool_min_print}")

        Create_pool_max_print = driver.find_element(By.XPATH, lp.Create_pool_max_print1_2()).text.strip()
        Logger.logger.info(f"✅ Maximum value in v3: {Create_pool_max_print}")

        Live_Token_price = driver.find_element(By.XPATH, lp.Live_Token_price1_2()).text.strip()
        Logger.logger.info(f"✅ Live token price: {Live_Token_price}")
        
        driver.implicitly_wait(5)

        x_deposit_Ratio_text = driver.find_element(By.XPATH, lp.x_deposit_Ratio_text1_2()).text.strip()
        x_deposit_Ratio = float(re.findall(r"[\d.]+", x_deposit_Ratio_text)[-1])
        Logger.logger.info(f"✅ x_deposit_Ratio: {x_deposit_Ratio}")

        y_deposit_Ratio_text = driver.find_element(By.XPATH, lp.y_deposit_Ratio_text1_2()).text.strip()
        y_deposit_Ratio = float(re.findall(r"[\d.]+", y_deposit_Ratio_text)[-1])
        Logger.logger.info(f"✅ y_deposit_Ratio: {y_deposit_Ratio}")

        # ✅ RETURN the values
        return (
            Live_Token_price, Create_pool_min_print, Create_pool_max_print, x_deposit_Ratio, y_deposit_Ratio
        )

    @staticmethod
    def calculate_apr(driver, amount):

        
        try:
            (Live_Token_price, 
             Create_pool_min_print, 
             Create_pool_max_print, 
             x_deposit_Ratio, 
             y_deposit_Ratio) = CalculationUtils.extract_and_pool_data(driver)

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

            Logger.logger.info(f"✅ ---- Token Ratio Calculation starting ----")
            Logger.logger.info(f"✅ pc: {pc}")
            Logger.logger.info(f"✅ pmin: {pmin}")
            Logger.logger.info(f"✅ pmax: {pmax}")
            Logger.logger.info(f"✅ Total Ratio: {total}")
            # Logger.logger.info(f"✅ {x_token} Ratio %: {token0_PR}, == Total Amount(UI) of {x_token} %: {x_deposit_Ratio}")
            # Logger.logger.info(f"✅ {y_token} Ratio %: {token1_PR}, == Total Amount(UI) of {y_token} %: {y_deposit_Ratio}")
            # Logger.logger.info(f"✅ Difference of {x_token} position: {token0_PR - x_deposit_Ratio}")
            # Logger.logger.info(f"✅ Difference of {y_token} position: {token1_PR - y_deposit_Ratio}")
            Logger.logger.info(f"✅ ---- Token Ratio Calculation completed ----")

            allure.attach(f"pc: {pc}, pmin: {pmin}, pmax: {pmax}", 
                        name=f"Pool calculation fee Index_amount_{amount}", 
                        attachment_type=allure.attachment_type.TEXT)
            allure.attach(f"amount={amount}",
                        name="Test_Inputs", 
                        attachment_type=allure.attachment_type.TEXT)

        except Exception as e:
            allure.attach(str(e), name="CLMM_Error", attachment_type=allure.attachment_type.TEXT)
            Logger.logger.error(f"❌ Error in CLMM calculation: {e}")