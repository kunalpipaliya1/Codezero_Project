from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from Project_1_CLMM_QA_Testnet.Locator.locator import locate
from Project_2_Perpetuals_QA_Testnet.Locator.locator import locater_login_URL
from Project_2_Perpetuals_QA_Testnet.Locator.locator import locater_perps
from Project_2_Perpetuals_QA_Testnet.Data.user_perps import *
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from Project_2_Perpetuals_QA_Testnet.Testcases_Logs.Logging_utils import Logger

class Launchpage():

    def __init__(self, driver):
        self.driver = driver
        self.loc = locater_login_URL
        self.DEXLYN_page_creds = credentials1
        self.Supra_Private_Key = CLMM_Login
        self.chrome_ex = Extension.chrome_extension
        self.webportal_xpath = locater_login_URL.xpath
        self.login = locater_login_URL.Home_page_validate
        self.creden = credentials1.password_test
        self.privateekey = CLMM_Login.privatekey
        self.private = locater_login_URL.Enter_private_key
        self.actual = locater_login_URL.actual_result
        self.dashboard = locater_login_URL.xpath_dashboard
        self.wallet_access = locater_login_URL.wallet_allow
        self.validator = locater_login_URL.Login_validator_Link_text
        self.installstarkey = locater_login_URL.starkey_install_button_click
        self.switch_window_chrome = locater_login_URL.click_on_chrome
        self.addchrome = locater_login_URL.add_to_chrome
        self.Click_on_Connect_wallet1 = locater_login_URL.Click_on_Connect_wallet
        self.Get_a_new_wallet_click1 = locater_login_URL.Get_a_new_wallet_click
        self.addusername = locater_login_URL.Enter_user_name
        self.setpassword = locater_login_URL.Enter_set_password
        self.confirmpassword = locater_login_URL.Enter_confirm_password
        self.clicknextbutton = locater_login_URL.Click_next_button
        self.skip = locater_login_URL.skiptab
        self.openwallet = locater_login_URL.open_wallet
        self.reconnectwall = locater_login_URL.reconnect_wallet
        self.allow = locater_login_URL.Allow_button
        self.click_ontrade = locater_login_URL.click_on_trade
        self.select_market1 = locater_login_URL.select_market
        self.supra = locater_login_URL.select_market_supra
        self.connectwallet = locater_login_URL.Connect_wallet
        self.wallet_already_have_btn1 = locater_login_URL.wallet_already_have_btn
        self.Transaction_failed_ok = locater_perps.Transaction_failed_ok
        self.private_key_btn1 = locater_login_URL.private_key_btn
        self.network_dropdown1 = locater_login_URL.network_dropdown
        self.supra_network_option1 = locater_login_URL.supra_network_option
        self.next_btn1 = locater_login_URL.next_btn
        self.all_networks_tab1 = locater_login_URL.all_networks_tab
        self.testnet_btn1 = locater_login_URL.testnet_btn
        self.password_input1 = locater_login_URL.password_input
        self.login_failed_msg1 = locater_login_URL.login_failed_msg
        self.hash_text1 = locater_login_URL.hash_text
        self.starkeyconfirmorallow = locater_login_URL.starkey_confirm_or_allow 
        self.tx_valid = locater_perps.TX_validation
        self.tokennamee = locater_perps.token_name   
        self.txview = locater_perps.TX_View
        self.tx_submit = locater_perps.TX_submitted
        self.viewexp = locater_perps.view_exp
        self.txclose = locater_perps.Transaction_close
        self.txstatus = locater_perps.User_TX_status
        self.vmstatus = locater_perps.VM_status
        self.Current_market_pricee = locater_perps.Current_market_price
        self.Index_Pricee = locater_perps.Index_Price
        self.Funding_Ratee = locater_perps.Funding_Rate
        self.Market_Skeww = locater_perps.Market_Skew
        self.Transaction_failed = locater_perps.Transaction_failed

        self.senderelement = locater_perps.sender_element
        self.receiverelement = locater_perps.receiver_element

        self.Token_selection         = locater_perps.Token_selection
        self.Token_search            = locater_perps.Token_search
        self.Token_list              = locater_perps.Token_list

        self.Long_market_order_panel = locater_perps.Long_market_order_panel
        self.Market_order_panel      = locater_perps.Market_order_panel
        self.Input_decimal           = locater_perps.Input_decimal
        self.Type_number             = locater_perps.Type_number
        self.Buy_Long                = locater_perps.Buy_Long
        self.Position_size           = locater_perps.Position_size

        self.SL_Price_None           = locater_perps.SL_Price_None
        self.SL_Price_Nonee          = locater_perps.SL_Price_Nonee

        self.SL_Price_Red            = locater_perps.SL_Price_Red   # duplicate ok if needed

        self.Take_profit             = locater_perps.Take_profit
        self.Take_profit_error       = locater_perps.Take_profit_error

        self.Final_Buy_Long          = locater_perps.Final_Buy_Long

        self.Short_market_order_panel = locater_perps.Short_market_order_panel
        self.Buy_Short = locater_perps.Buy_Short
        self.Final_Buy_Short = locater_perps.Final_Buy_Short

        self.SLprice_USD = locater_perps.SLprice_USD
        self.TPprice_USD = locater_perps.TPprice_USD

        self.Collateral_USDC = locater_perps.Collateral_USDC
        self.Leverage_x = locater_perps.Leverage_x
        self.Liquidation_price = locater_perps.Liquidation_price
        self.Position_Size_usdc = locater_perps.Position_Size_usdc

    def click_element(self, driver, by, locator, delay=10):
        Logger.logger.info(f"✅ 👉 Trying to click locator: {locator}")
        try:
            WebDriverWait(driver, delay).until(EC.element_to_be_clickable((by, locator))).click()
            return True
        except:
            Logger.logger.error(f"Failed to click element -> {locator}")
            return False
            
    def get_element(self,  by, locator, timeout=10, visible = True):
        try:
            # element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((by, locator)))
            # return element

            if visible:
                return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((by, locator)))
            else:
                return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, locator)))
            
        except TimeoutException:
            Logger.logger.error(f"Timeout: Element not found or not visible -> {locator}")
            return None
        except Exception as e:
            Logger.logger.error(f"Error occurred while finding element: {locator} -> {e}")
            return None

    def chorme_exten(self):
        return Extension.chrome_extension
        
    def Login_URL1(self):
        return URL.URL1
    
    def pop_close(self):
        self.get_element(By.XPATH, self.close_po)

    def entering_password(self):
        self.get_element(By.XPATH, self.webportal_xpath).send_keys(self.creden)
    
    def Privatekey(self):
        # private_key_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.private)))
        self.get_element(By.XPATH, self.private).send_keys(str(self.privateekey))

    def click_on_login(self):
        self.click_element(self.driver, By.XPATH, self.login)
    
    def login_validate(self):
        return self.get_element(By.LINK_TEXT, self.validator).text

    def actualresult(self):
        # element = self.get_element(By.XPATH, self.actual)
        # return element.text
        return self.get_element(By.XPATH, self.actual).text

    def dashboard_click(self):
        self.get_element(By.XPATH, self.dashboard)
    
    def wallet_access_button(self):
        self.click_element(self.driver, By.XPATH, self.wallet_access)

    # def install_starKey(self):
    #     self.click_element(self.driver, By.XPATH, self.installstarkey)

    # def chrome_click(self):
    #     self.click_element(self.driver, By.XPATH, self.switch_window_chrome)

    def chrome_extention(self):
        return self.addchrome

    def connection_wallet(self, timeout=1):
        try:
            # Wait until button is clickable
            click_button = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((By.XPATH, self.Click_on_Connect_wallet1))
            )

            try:
                click_button.click()
                Logger.logger.info(f"✅ Wallet connect button clicked (Selenium)")
            except:
                # Fallback to JS click if normal click fails
                self.driver.execute_script("arguments[0].click();", click_button)
                Logger.logger.error(f"❌ ⚡ Wallet connect button clicked (JS fallback)")
            return True

        except TimeoutException:
            Logger.logger.error(f"❌ Wallet connect button not clickable within {timeout}s")
            return False

    def wallettextmsgpopup(self):
        self.click_element(self.driver, By.XPATH, self.wallet_msg)

    def new_wallet_click(self):
        self.click_element(self.driver, By.XPATH, self.Get_a_new_wallet_click1)

    def Add_username(self):
        self.get_element(By.XPATH, self.addusername).send_keys("Kunal")
    
    def setpassword1(self):
        self.get_element(By.XPATH, self.setpassword).send_keys("Rjio@1234")
    
    def confirmpassword1(self):
        self.get_element(By.XPATH, self.confirmpassword).send_keys("Rjio@1234")

    def clicknext(self):
        self.click_element(self.driver, By.XPATH, self.clicknextbutton)

    def skiptask(self):
        self.click_element(self.driver, By.XPATH, self.skip)

    def open_wall(self):
        self.click_element(self.driver, By.XPATH, self.openwallet)

    def reconnect(self):
        self.click_element(self.driver, By.XPATH, self.reconnectwall)

    def allowbutton(self):
        self.click_element(self.driver, By.XPATH, self.allow)

    def click_trade(self):
        return self.click_ontrade
    
    def Tradetoswapclickk(self):
        return self.Tradetoswapclick

    # def selectmarket(self):
    #     self.click_element(self.driver, By.XPATH, self.select_market1)

    # def select_supra(self):
    #     self.click_element(self.driver, By.XPATH, self.supra)

    # def click_clmm(self):
    #     self.click_element(self.driver, By.XPATH, self.CLMMClick)

    def tokennameadd(self):    
        return self.get_element(By.XPATH, self.tokennamee).text
    
    def Swap_x_exchan(self, value="SUPRA"):
        ele18 = self.get_element(By.XPATH, self.Swapx_exchange)
        if not ele18:
            raise Exception(f"Swap_x_exchan: Element not found with locator {self.Swapx_exchange}")
        ele18.click()
        ele181 = self.get_element(By.XPATH, self.Token)
        if not ele181:
            raise Exception(f"Swap_x_exchan: Element not found with locator {self.Swapx_exchange}")
        ele181.clear()
        ele181.send_keys(value + Keys.TAB + Keys.ENTER)
        time.sleep(1) 

    def Swap_y_exchan(self, value="johnnytest"):
        ele19 = self.get_element(By.XPATH, self.Swapy_exchange)
        if not ele19:
            raise Exception(f"Swap_x_exchan: Element not found with locator {self.Swapy_exchange}")
        ele19.click()
        ele191 = self.get_element(By.XPATH, self.Token)
        if not ele191:
            raise Exception(f"Swap_x_exchan: Element not found with locator {self.Swapy_exchange}")
        ele191.clear()
        ele191.send_keys(value + Keys.TAB + Keys.ENTER)
        time.sleep(1)

    def Swap_x_value(self, value="1"):
        ele20 = self.get_element(By.XPATH, self.Swapx_value)
        ele20.clear()
        ele20.send_keys(value)
        time.sleep(2)
        # WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element_attribute((By.XPATH,self.x_onedollar)))
        return ele20
    
    # def Swap_x_onedollar_value(self):   
    #     ele = self.get_element(By.XPATH, self.x_onedollar)
    #     return ele

    def Swap_x_onedollar_value(self, timeout=15):
        return self.get_element(By.XPATH, self.x_onedollar, timeout=timeout)

    def Swap_y_value(self, value="1"):
        ele21 = self.get_element(By.XPATH, self.Swapy_value)
        ele21.clear()
        ele21.send_keys(value)
        time.sleep(1)
        # WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element_attribute((By.XPATH,self.y_onedollar), "value", str(value)))
        return ele21

    def Swap_y_onedollar_value(self):
        ele = self.get_element(By.XPATH, self.y_onedollar)
        return ele

    # def Acknowl(self, timeout=5):
    #     try:
    #         button = WebDriverWait(self.driver, timeout).until(
    #             EC.element_to_be_clickable((By.ID, self.ackno_click))
    #         )
    #         # button.click()
    #         self.driver.execute_script("arguments[0].click();", button)  # JS click, fires once
    #         Logger.logger.info(f"✅ Acknowledge button visible and clicked")
    #         return True
    #     except Exception:
    #         Logger.logger.error(f"❌ Acknowledge button not visible")
    #         return False


    def earn2poolswap_y(self, value="1"):
        y_usd = self.get_element(By.XPATH, self.yusdinput())
        y_usd.clear()
        y_usd.send_keys(value)
        time.sleep(1)

    # def earn2poolonedoller_y(self):
    #     y_usd = self.get_element(By.XPATH, self.yusdbtn())
    #     return y_usd

        # x_pay

        # x_usd = driver.find_element(By.XPATH, lp.xusdinput())
        # x_usd.clear()
        # x_usd.send_keys(amount)
        # x_usd = driver.find_element(By.XPATH, lp.xusdbtn())
        # x_price_in_usd_from_earn = x_usd.text.strip().replace('$','')
        # Logger.logger.info(x_price_in_usd_from_earn)

        # x_usd = driver.find_element(By.XPATH, lp.xusdinput())
        # x_usd.clear()
        # x_usd.send_keys(amount)
        # x_usd = driver.find_element(By.XPATH, lp.xusdbtn())
        # x_price_in_usd_from_earn = x_usd.text.strip().replace('$','')
        # Logger.logger.info(x_price_in_usd_from_earn)

    def earn2poolswap_x(self, value="1"):
        x_usd = self.get_element(By.XPATH, self.xusdinput())
        x_usd.clear()
        x_usd.send_keys(value)
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.yamountvalidate)))

    def earn2poolonedoller_x(self):
        x_usd = self.get_element(By.XPATH, self.xusdbtn())
        return x_usd

    def scroll_botton(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
    def Acknowl(self):
        return self.ackno_click
        
    def Swap_Button_Click(self):
        return self.swapbutton

    def Connectwallet1(self):
        self.click_element(self.driver, By.XPATH, self.connectwallet)

    def Transactionfailed_ok(self):
        return self.Transaction_failed_ok
    
    def Transactionfailed(self):
        return self.Transaction_failed
        
    def Click_swap(self):
        return self.swapp_button11

    def swaperrormsg1(self):
        return self.swaperrormsg

    def starkeyconfirmation(self):
        return self.starkeyconfirmorallow

    def starkeydismiss(self):
        self.click_element(self.driver, By.XPATH, self.starrkeydeny)
    
    def starkeypopread(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_any_elements_located((By.XPATH, self.starkeypopmsg)))
        
    def tx_validation(self):
        return self.tx_valid
    
    def senderelement1(self):
        return self.senderelement

    def receiverelement1(self):
        return self.receiverelement
    
    def txsubmitt(self):
        return self.tx_submit
    
    def txviewsection(self):
        return self.txview
    
    def viewexpo(self):
        return self.viewexp
    
    def txfindstatus(self):
        return self.txstatus
    
    def vmstatuscheck(self):
        return self.vmstatus

    def clickonearn(self):
        return self.click_on_earn1
    
    def clickonpool(self):
        return self.click_on_pool1
    
    def poolerrorfound(self):
        element = self.get_element(By.XPATH, self.poolcheckerror)
        if element:
            return element.text.strip() != ""
        return False

    
    def clickonliquidity(self):
        return self.click_on_liquidity1
    
    def clickontokenpair(self):
        return self.click_on_base_token_pair1
    
    def clickonxy(self):
        return self.click_on_Token_x_y1

    def element_visibilityviewexpo(self):
        return self.element_visiibility_x_y1
    
    def basequery(self):
        return self.click_on_base_query_pair1
    
    def pooltype(self):
        return self.pool_type1

    def feetierdropdown(self):
        return self.fee_tier_dropdown1
    
    def fetchfee(self):
        return self.fetch_fee_tier1
    
    def clickoncontinue(self):
        return self.click_on_continue1
    
    def myposition(self):
        return self.my_position1
    
    # def totalliquidity(self):
    #     return self.total_liqudity1

    def clickpo1(self):
        return self.click_on_po1
    
    def arrowclick(self):
        return self.click_on_arrow1
    
    def clickonincrease(self):
        return self.click_on_increase1
    
    def enterinput(self):
        return self.enter_input1
    
    def Explorepoolclick(self):
        return self.explorepooll 
    
    def increaseliquidity(self):
        return self.Increase_liquidity1

    def removeliq(self):
        return self.remove_liquidity12
    
    def slidermove(self):
        return self.slider1
    
    def finalremoveliqu(self):
        return self.remove_liq1

    def walletalreadyhavebtn(self):
        return self.wallet_already_have_btn1

    def privatekeybtn(self):
        return self.private_key_btn1

    def networkdropdown(self):
        return self.network_dropdown1



    
    def supranetworkoption(self):
        return self.supra_network_option1

    def nextbtn(self):
        return self.next_btn1
    
    def fetcallnetwork(self):
        return self.all_networks_tab1
    
    def testnetclick(self):
        return self.testnet_btn1
    
    def passwdinput(self):
        # self.click_element(self.driver, By.XPATH, self.password_input1)
        return self.password_input1
    
    def loginfailedmsg(self):
        return self.login_failed_msg1

    def hashtext(self):
        return self.hash_text1
    
    def poolpagetitle1(self):
        return self.poolpagetitle

    def createpool1(self):
        # return "//button[contains(text(),'Create Pool')]"
        return self.createpool
    
    def clrbtn(self):
        return self.clearbtn
   
    def clickbasetoken(self):
        return self.click_on_basetoken
    
    def tokensearch(self):
        return self.token_search

    def quoteetoken(self):
        # self.click_element(self.driver, By.XPATH, self.quotetoken)
        return self.quotetoken
    
    def standardtab(self):
        return self.standtab
   
    def concen_v3_tab(self):
        return self.concenttab
    
    def continuebtn(self):
        return self.continue_btn

    # def poolexistt(self):   
    #     # return self.get_element(By.XPATH, self.poolexist).text.strip()
    
    #     element = self.get_element(By.XPATH, self.poolexist)

    #     if element:
    #         return element.text.strip()
    #     return ""
    

    def poolexistt(self):
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, self.poolexist))
        )
        # self.get_element(By.XPATH, self.poolexist).text.strip()

    # def inputamount(self):
    #     return self.setinitialprice
    # def inputamount(self, value='1'):
    #     # return self.get_element(By.XPATH, self.setinitialprice)
    #     ele20 = self.get_element(By.XPATH, self.inputamount)
    #     ele20.clear()
    #     ele20.send_keys(value)
    #     time.sleep(1)
    #     return ele20

   
    def Current_market_priceee(self):
        return float(self.get_element(By.XPATH, self.Current_market_pricee).text.strip())
    
    def Index_Priceee(self):
        return self.get_element(By.XPATH, self.Index_Pricee).text.strip()
    
    def Funding_Rateee(self):
        return self.get_element(By.XPATH, self.Funding_Ratee).text.strip()
    
    def Market_Skewww(self):
        return self.get_element(By.XPATH, self.Market_Skeww).text.strip()
    
    def inputamount(self, value='1'):
        try:
            ele20 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.enter_input1)))
            if ele20:
                ele20.clear()
                ele20.send_keys(str(value))
                assert ele20.get_attribute("value") == str(value), "Amount not correctly entered!"
                time.sleep(1)
                Logger.logger.info(f"✅ Entered amount: {value}")
                return ele20
            else:
                raise Exception(f"Amount input field not found:")
        except Exception as e:
            Logger.logger.error(f"❌ Failed to enter amount: {e}")
            return None

    def customtab(self):
        return self.customrangetab
    
    def pooladd(self):
        return self.poolfinal
        # self.click_element(By.XPATH, self.poolfinal)
    
    def provideli(self):
        return self.provideliqui

    def ypriceenter(self):
        return self.ypriceusd

    def ypriceenterverify(self):
        return self.ypriceusdverify

    def xpriceenter(self):
        return self.xpriceusd

    def xpriceenterverify(self):
        return self.xpriceusdverify
    
    def txclose1(self):
        return self.txclose
    
    def earntab(self):
        return self.earn_tab1

    def poolbtn(self):
        return self.pool_button1

    def positiontext(self):
        return self.positions_text1

    def filterbytoken(self):
        return self.filter_by_token1
    
    def ethereuminput(self):
        return self.ethereum_input1

    def tickmark1(self):
        return self.tickmark

    def suprainput(self):
        return self.supra_input1

    def v3_pool(self):
        return self.v3_pool1
    
    def swaptablerow(self):
        return self.swap_table_row1

    def clmmbtn(self):
        return self.clmm_button1
    
    def xusdinput(self):
        return self.x_usd_input1

    def xusdbtn(self):
        return self.x_usd_button1

    def yusdinput(self):
        return self.y_usd_input1

    # def yusdbtn(self):
    #     return self.y_usd_button1
    
    def termscheckbox(self):
        return self.terms_checkbox1

    def swapbtn(self):
        return self.swapp_button11

    def Highpricetextmsg(self):
        try:
            element_highmsg = WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located((By.XPATH, self.Highpriceimpact))
            )
            return element_highmsg.text.strip()
        except Exception:
            return None
        
    def slipagecheck(self):
        self.click_element(self.driver, By.XPATH, self.slipage_check)
    
    def slipage2check(self):
        self.click_element(self.driver, By.XPATH, self.slipage_2)

    def savebtnclick(self):
        self.click_element(self.driver, By.XPATH, self.savebtton)

    def positionnclick(self):
        return self.clickonposs

    def no_position_found(self):
        return self.noposition_found
    
    def positionindex8_8(self):
        return self.positionindex8
    
    def positionindex7_7(self):
        return self.positionindex7
    
    def positionindex6_6(self):
        return self.positionindex6
    
    def positionindex6_6Inactive(self):
        return self.positionindex6inactivee
    
    






    def token_selection(self):
        return self.Token_selection

    def token_search(self):
        return self.Token_search

    def token_list(self):
        return self.Token_list

    def long_market_order_panel(self):
        return self.Long_market_order_panel

    def market_order_panel(self):
        return self.Market_order_panel

    def input_decimal(self):
        return self.Input_decimal

    def type_number(self):
        return self.Type_number

    def buy_long(self):
        return self.Buy_Long

    def position_size(self):
        return self.Position_size

    def sl_price_none(self):
        return self.SL_Price_None

    def sl_price_none1(self):
        return self.SL_Price_Nonee
    
    def sl_price_red(self):
        return self.SL_Price_Red

    def take_profit(self):
        return self.Take_profit

    def take_profit_error(self):
        return self.Take_profit_error

    def final_buy_long(self):
        return self.Final_Buy_Long
    

    def Short_market_order_panell(self):
        return self.Short_market_order_panel

    def Buy_Shortt(self):
        return self.Buy_Short

    def Final_Buy_Shortt(self):
        return self.Final_Buy_Short
    
    def SLprice_USDD(self):
        return self.SLprice_USD

    def TPprice_USDD(self):
        return self.TPprice_USD
    
    
    


    def Collateral_USDCC(self):
        return float(self.driver.find_element(By.XPATH, "(//*[@class='text-sm text-white'])[1]").text.replace("USDC","").strip())

    def Leverage_xx(self):
        return float(self.driver.find_element(By.XPATH, "(//*[@class='text-sm text-white'])[2]").text.replace("x","").strip())

    def Liquidation_pricee(self):
        return float(self.driver.find_element(By.XPATH, "(//*[@class='text-sm text-white flex items-center gap-1'])[1]").text.strip())

    def Position_Size_usdcc(self):
        return float(self.driver.find_element(By.XPATH, "(//*[@class='text-sm text-white flex items-center gap-1'])[2]").text.replace("USDC","").replace(",", "").strip())
    
