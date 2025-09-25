from selenium.webdriver.common.keys import Keys
import pytest
import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Project_2_Perpetuals_QA_Testnet.Page.base_page import allurescreenshot
from Project_2_Perpetuals_QA_Testnet.Page.test_page import Launchpage
from Project_2_Perpetuals_QA_Testnet.Test.Transaction_validation import Transaction_validation_class
from Project_2_Perpetuals_QA_Testnet.Test.wallet_connection import wallet_connection_class
from Project_2_Perpetuals_QA_Testnet.Utils.StaticUtils import StaticUtil
from Project_2_Perpetuals_QA_Testnet.Testcases_Logs.Logging_utils import Logger
import random

@pytest.mark.usefixtures("call_main_url")
class TestPoolCreation:
    Logger.logger.info(f"✅ ==== Test 4: test_4_perps_long_position_USD checking starting ====")
    # @pytest.mark.parametrize("loop_id", range(1))   # ✅ 10 invocations
    # @pytest.mark.parametrize("x_token, y_token", testcase_token_name.token_pairs)
    # @pytest.mark.parametrize("SL_random_price,TP_random_price", [(testcase_amounts.SL_random_price, testcase_amounts.TP_random_price)])
    # @pytest.mark.parametrize("session_id", [1, 2])
    @pytest.mark.repeat(2)
    # @pytest.mark.parametrize("fee_index", [0, 1, 2, 3], ids=["Fee_0.01%", "Fee_0.05%", "Fee_0.3%", "Fee_1%"])
    def test_4_perps_long_position_USD(self, call_main_url, random_prices):
        SL_random_price, TP_random_price = random_prices
        driver = call_main_url
        lp = Launchpage(driver)

        StaticUtil.retry_click(driver, By.XPATH, lp.token_selection())  # click on token name
        driver.implicitly_wait(3)
        Token_input = driver.find_element(By.XPATH, lp.token_search())
        Token_input.clear()
        Token_input.send_keys("ADA-USDT")
        StaticUtil.retry_click(driver, By.XPATH, lp.token_list())
        driver.implicitly_wait(3)

        Current_market_price = lp.Current_market_priceee()  # Current market price
        Index_Price = lp.Index_Priceee() # Index Price
        Funding_Rate = lp.Funding_Rateee()  # Funding Rate
        Market_Skew = lp.Market_Skewww()  # Market Skew
        

        Logger.logger.info(f"✅ Current_market_price_value: {Current_market_price}")
        Logger.logger.info(f"✅ Index_Price_value: {Index_Price}")
        Logger.logger.info(f"✅ Funding_Rate_per_hours_value: {Funding_Rate}")
        Logger.logger.info(f"✅ Market_Skew_value: {Market_Skew}")

        allure.attach(f"✅ Current_market_price_value: {Current_market_price}", name="Current market price", attachment_type=allure.attachment_type.TEXT)
        allure.attach(f"✅ Index_Price_value: {Index_Price}", name="Index price", attachment_type=allure.attachment_type.TEXT)
        allure.attach(f"✅ Funding_Rate_per_hours_value: {Funding_Rate}", name="Funding rate per hours value", attachment_type=allure.attachment_type.TEXT)
        allure.attach(f"✅ Market_Skew_value: {Market_Skew}", name="Market skew value", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Market value capture screenshot"):
            allurescreenshot.take_screenshot(driver, "Market value capture screenshot")
        Logger.logger.info(f"✅ Before proceed check market value")

        driver.implicitly_wait(3)
        StaticUtil.retry_click(driver, By.XPATH, lp.long_market_order_panel())
        StaticUtil.retry_click(driver, By.XPATH, lp.market_order_panel())
        Token_input_market = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, lp.input_decimal())))

        time.sleep(2)
        Token_input_market.send_keys(Keys.CONTROL, "a")
        Token_input_market.send_keys(Keys.DELETE)
        Token_input_market.send_keys(SL_random_price)
        Leverage_input = driver.find_element(By.XPATH, lp.type_number())
        Leverage_input.send_keys(Keys.CONTROL, "a")
        Leverage_input.send_keys(Keys.BACKSPACE)
        Leverage_input.send_keys(SL_random_price)
        driver.implicitly_wait(3)

        try:
            StaticUtil.retry_click(driver, By.XPATH, lp.buy_long())
            Logger.logger.info(f"✅ Position size greater then > 300")
        except Exception as e:
            Actual_result = "Position size should be minimum 300 USDC"
            Expected_result = driver.find_element(By.XPATH, lp.position_size())
            
            assert Actual_result in Expected_result.text.strip()
            Logger.logger.error(f"✅ Position size less then < 300, Message visible: {Expected_result}")

            Token_input_market.send_keys(Keys.CONTROL, "a")
            Token_input_market.send_keys(Keys.DELETE)
            Token_input_market.send_keys(SL_random_price)
            Leverage_input = driver.find_element(By.XPATH, lp.type_number())
            Leverage_input.send_keys(Keys.CONTROL, "a")
            Leverage_input.send_keys(Keys.BACKSPACE)
            Leverage_input.send_keys(SL_random_price)
            WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, lp.buy_long())))
            StaticUtil.retry_click(driver, By.XPATH, lp.buy_long())

        time.sleep(2)

        # @ SL Price start @@@@@@@@@
        Logger.logger.info(f"✅ SL Price start")
        Collateral_USDC = lp.Collateral_USDCC()
        Leverage_x = lp.Leverage_xx()
        Liquidation_price = lp.Liquidation_pricee()
        Position_Size_usdc = lp.Position_Size_usdcc()

        allure.attach(f"✅ Collateral_USDC: {Collateral_USDC}", name="Collateral_USDC", attachment_type=allure.attachment_type.TEXT)
        allure.attach(f"✅ Leverage_x: {Leverage_x}", name="Leverage_x", attachment_type=allure.attachment_type.TEXT)
        allure.attach(f"✅ Liquidation_price: {Current_market_price}", name="Liquidation_price", attachment_type=allure.attachment_type.TEXT)
        allure.attach(f"✅ Position_Size_usdc: {Position_Size_usdc}", name="Position_Size_usdc", attachment_type=allure.attachment_type.TEXT)

        try:
            
            Current_m_price =float(Current_market_price)
            liquidation_price = float(Liquidation_price)

            low = min(Current_m_price, liquidation_price)
            high = max(Current_m_price, liquidation_price)

            # random.randint only works with ints; if you need whole cents, scale up
            sl_usd_random_price = random.uniform(low, high)   # gives a float

            SL_Price = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, lp.SLprice_USDD())))
            SL_Price.clear()
            SL_Price.send_keys(str(round(sl_usd_random_price, 5)))

            driver.implicitly_wait(2)

        except Exception as e:
            with allure.step("❌ SL Price error"):
                    allurescreenshot.take_screenshot(driver, "❌ SL Price error")
            Logger.logger.error(f"❌ SL Price error: {e}")
        
        # @ SL Price end @@@@@@@@@

        Logger.logger.info(f"✅ TP Price start with USD")
        try:
            TP_Price = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, lp.TPprice_USDD())))
            TP_Price.send_keys(Keys.CONTROL, "a")
            TP_Price.send_keys(Keys.BACKSPACE)

            # Formula: TP Price = Market Price × ( 1 + (TPusd / PositionSize) ) 
            # where   TPusd = TP% × Collateral

            TP_usd = (900/100) * Collateral_USDC

            allure.attach(f"✅ TP_usd: {TP_usd}", name="TP_usd", attachment_type=allure.attachment_type.TEXT)
            
            TP_Price_cal = Current_market_price * (1 + (TP_usd / Position_Size_usdc))

            # Send the value to the element
            TP_Price.send_keys(str(round(TP_Price_cal)))

            Logger.logger.info(f"✅ TP Price calculation completed")

            allure.attach(f"✅  {str(TP_Price_cal)}", name="TP_calculated_price_in_USD", attachment_type=allure.attachment_type.TEXT)

        except Exception as e:
            with allure.step(f"❌ TP Price start with USD: {e}"):
                    allurescreenshot.take_screenshot(driver, f"❌ TP Price start with USD: {e}")
            Logger.logger.error(f"❌ TP Price start with USD: {e}")

        try:
            element = StaticUtil.retry_click(driver, By.XPATH, lp.final_buy_long(), fail_if_disabled=False)
            if element is None:
                Logger.logger.info(f"✅ Button is disabled, skipping click")
        except:
            Logger.logger.error(f"❌ Button is disabled")

        driver.switch_to.window(driver.window_handles[0])

        wallet_connection_class.wallet_connection(driver)
        driver.implicitly_wait(3)

        try:
            Transaction_validation_class.Transaction_validation(driver)
        except Exception as e:
            with allure.step(f"❌ Selenium session lost: {e}"):
                    allurescreenshot.take_screenshot(driver, f"❌ Selenium session lost: {e}")
            Logger.logger.error(f"❌ Selenium session lost: {e}")

Logger.logger.info(f"✅ ==== Test 4: test_4_perps_long_position_USD checking starting ====")

def run():
    Logger.logger.info(f"✅ Running test_4_perps_long_position_USD ...")
    import pytest
    pytest.main([__file__])   # this will run the tests inside this file

if __name__ == "__main__":
    run()  

    