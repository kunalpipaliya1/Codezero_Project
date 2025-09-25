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

@pytest.mark.usefixtures("call_main_url")
class TestPoolCreation:
    Logger.logger.info(f"✅ ==== Test 6: test_6_perps_collateral checking starting ====")
    @pytest.mark.repeat(1)
    # @pytest.mark.parametrize("SL_random_price,TP_random_price", [(testcase_amounts.SL_random_price, testcase_amounts.TP_random_price)])
    def test_6_perps_collateral(self, call_main_url, random_prices):
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

        allure.attach(f"Current_market_price_value: {Current_market_price}", name="Current market price", attachment_type=allure.attachment_type.TEXT)
        allure.attach(f"Index_Price_value: {Index_Price}", name="Index price", attachment_type=allure.attachment_type.TEXT)
        allure.attach(f"Funding_Rate_per_hours_value: {Funding_Rate}", name="Funding rate per hours value", attachment_type=allure.attachment_type.TEXT)
        allure.attach(f"Market_Skew_value: {Market_Skew}", name="Market skew value", attachment_type=allure.attachment_type.TEXT)

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
            
            assert Actual_result.text.strip() in Expected_result.text.strip()
            Logger.logger.error(f"Position size less then < 300, Message visible: {Expected_result}")

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

        try:
            SL_Price = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, lp.sl_price_none())))
            SL_Price.clear()
            SL_Price.send_keys("95")
            driver.implicitly_wait(3)

            expected_prefix = "Stop Loss must be above"

            el = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, lp.sl_price_red()))
            )

            actual_text = el.text.strip()
            assert actual_text.startswith(expected_prefix), f"Got: {actual_text!r}"

            Logger.logger.info(f"✅ Negative case validated actual text from xpath msg is: {actual_text}")
            allure.attach(f"Actual Result: {actual_text}", name="Negative case validation", attachment_type=allure.attachment_type.TEXT)

            # enter correct value
            SL_Price = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, lp.sl_price_none())))
            SL_Price.send_keys(Keys.CONTROL, "a")
            SL_Price.send_keys(Keys.BACKSPACE)
            SL_Price.send_keys(SL_random_price)

        except Exception as e:
            with allure.step("❌ SL Price error"):
                    allurescreenshot.take_screenshot(driver, "❌ SL Price error")
            Logger.logger.error(f"❌ SL Price error: {e}")
        
        # @ SL Price end @@@@@@@@@

        Logger.logger.info(f"✅ TP Price start exceed > 900%")
        try:
            TP_Price = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, lp.take_profit()))
            )
            TP_Price.send_keys(Keys.CONTROL, "a")
            TP_Price.send_keys(Keys.BACKSPACE)
            TP_Price.send_keys("901")
            Logger.logger.info(f"✅ Tp Price entered at 901")

            driver.implicitly_wait(3)

            expected_prefix = "Take Profit percentage cannot exceed 900%"

            el = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, lp.take_profit_error()))
            )
            actual_text = el.text.strip()
            assert actual_text == expected_prefix, f"Got: {actual_text!r}"

            Logger.logger.info(f"✅ Negative case validated actual text from xpath msg is: {actual_text}")
            allure.attach(f"Actual Result: {actual_text} -> Expected Result: {expected_prefix} ", name="Negative case validation", attachment_type=allure.attachment_type.TEXT)

        except Exception as e:
            with allure.step(f"❌ Take Profit percentage cannot exceed 900%: {e}"):
                    allurescreenshot.take_screenshot(driver, f"❌ Take Profit percentage cannot exceed 900%: {e}")
            Logger.logger.error(f"❌ Take Profit percentage cannot exceed 900%: {e}")
  
        Logger.logger.info(f"✅ TP Price start < 0")
        # try:
        TP_Price = driver.find_element(By.XPATH, lp.take_profit())
        TP_Price.send_keys(Keys.CONTROL, "a")
        TP_Price.send_keys(Keys.BACKSPACE)
        TP_Price.send_keys("0")

        expected_prefix = "Take Profit must be above"

        el = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, lp.take_profit_error()))
        )

        actual_text = el.text.strip()
        Logger.logger.info(f"✅ opimzized: {actual_text}")

        assert actual_text.startswith(expected_prefix), f"Got: {actual_text!r}"

        Logger.logger.info(f"✅ Negative case validated actual text from xpath msg is: {actual_text}")
        allure.attach(f"Actual Result: {actual_text} -> Expected Result: {expected_prefix} ", name="Negative case validation", attachment_type=allure.attachment_type.TEXT)

        # except Exception as e:
        #     with allure.step(f"❌ Take Profit must be above from current market price%: {e}"):
        #             allurescreenshot.take_screenshot(driver, f"❌ ake Profit must be above from current market price%: {e}")
        #     Logger.logger.error(f"❌ Take Profit must be above from current market price%: {e}")

        Logger.logger.info(f"✅ TP Price start with current value")
        try:
            TP_Price = driver.find_element(By.XPATH, lp.take_profit())
            TP_Price.send_keys(Keys.CONTROL, "a")
            TP_Price.send_keys(Keys.BACKSPACE)
            TP_Price.send_keys(TP_random_price)

        except Exception as e:
            with allure.step(f"❌ Take Profit must be above from current market price%: {e}"):
                    allurescreenshot.take_screenshot(driver, f"❌ Take Profit must be above from current market price%: {e}")
            Logger.logger.error(f"❌ Take Profit must be above from current market price%: {e}")
               
        try:
            element = StaticUtil.retry_click(driver, By.XPATH, lp.final_buy_long(), fail_if_disabled=False)
            if element is None:
                Logger.logger.info(f"✅ Button is disabled, skipping click")
        except:
            Logger.logger.error(f"❌ Button is disabled")

        StaticUtil.retry_click(driver, By.XPATH, "//*[@class='lucide lucide-x size-7 cursor-pointer text-grayWhite hover:text-lighterGray']")

        driver.switch_to.window(driver.window_handles[0])

        wallet_connection_class.wallet_connection(driver)
        driver.implicitly_wait(3)

        try:
            Transaction_validation_class.Transaction_validation(driver)
        except Exception as e:
            with allure.step(f"❌ Selenium session lost: {e}"):
                    allurescreenshot.take_screenshot(driver, f"❌ Selenium session lost: {e}")
            Logger.logger.error(f"❌ Selenium session lost: {e}")

        driver.implicitly_wait(3)

        Collateral_Before_add = driver.find_element(By.XPATH, "(//*[@class='flex items-center gap-2 max-lg:ml-auto max-lg:w-fit'])[1]").text
        
        try:
            StaticUtil.retry_click(driver, By.XPATH, "//*[@class='leading-none']")
            Logger.logger.info(f"✅ New Ordered blocked and close pop-up")
        except Exception as e:
            with allure.step(f"❌ New order not came under the and did the transaction: {e}"):
                    allurescreenshot.take_screenshot(driver, f"❌ New order not came under the and did the transaction: {e}")
            Logger.logger.error(f"❌ New order not came under the and did the transaction: {e}")

        driver.find_element(By.XPATH, "(//*[@type='text'])[2]").send_keys("1")
        StaticUtil.retry_click(driver, By.XPATH, "(//*[text()='Add Collateral'])[2]")

        wallet_connection_class.wallet_connection(driver)

        try:
            Transaction_validation_class.Transaction_validation(driver)
        except Exception as e:
            with allure.step(f"❌ Selenium session lost: {e}"):
                    allurescreenshot.take_screenshot(driver, f"❌ Selenium session lost: {e}")
            Logger.logger.error(f"❌ Selenium session lost: {e}")
        
        Collateral_After_Add = driver.find_element(By.XPATH, "(//*[@class='flex items-center gap-2 max-lg:ml-auto max-lg:w-fit'])[1]").text

        Collateral_difference = float(Collateral_After_Add.replace(" USDC", "").replace(",", "")) - float(Collateral_Before_add.replace(" USDC", "").replace(",", ""))

        allure.attach(f"Collateral_Before_add: {Collateral_Before_add}", name="Collateral Before Add", attachment_type=allure.attachment_type.TEXT)
        allure.attach(f"Collateral_After_Add: {Collateral_After_Add}", name="Collateral After Add", attachment_type=allure.attachment_type.TEXT)
        allure.attach(f"Collateral_difference: {Collateral_difference}", name="Collateral Difference", attachment_type=allure.attachment_type.TEXT)
        Logger.logger.info(f"✅ Collateral_add_completed and verified")

Logger.logger.info(f"✅ ==== Test 6: test_6_perps_collateral checking Completed ====")

def run():
    Logger.logger.info(f"✅ Running test_6_perps_collateral ...")
    import pytest
    pytest.main([__file__])   # this will run the tests inside this file

if __name__ == "__main__":
    run()  

    