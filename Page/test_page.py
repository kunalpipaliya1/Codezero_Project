import time, allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from Project_1_CLMM_QA_Testnet.Locator.locator import locate
from Project_1_CLMM_QA_Testnet.Data.users_v3 import (CLMM_Login, credentials1, URL, wallet_details)
from Project_1_CLMM_QA_Testnet.Testcases_Logs.Logging_utils import Logger

class slipagechecker:
    @staticmethod
    def slipagecheck(driver):
        lp = Homepage(driver)
        driver.implicitly_wait(5)
        import time
        time.sleep(1)
        lp.slipagecheck()
        lp.slipage2check()
        lp.savebtnclick()
        time.sleep(1)

class allurescreenshot:
    def take_screenshot(driver, name="screenshot"):
        allure.attach(driver.get_screenshot_as_png(), name=name, attachment_type=allure.attachment_type.PNG)

class Homepage():

    def __init__(self, driver):
        self.driver = driver
        self.loc = locate
        self.DEXLYN_page_creds = credentials1
        self.Supra_Private_Key = CLMM_Login
        self.webportal_xpath = locate.xpath
        self.login = locate.Home_page_validate
        self.creden = credentials1.password_test
        self.privateekey = CLMM_Login.privatekey
        self.private = locate.Enter_private_key
        self.actual = locate.actual_result
        self.dashboard = locate.xpath_dashboard
        self.wallet_access = locate.wallet_allow
        self.validator = locate.Login_validator_Link_text
        self.installstarkey = locate.starkey_install_button_click
        self.switch_window_chrome = locate.click_on_chrome
        self.addchrome = locate.add_to_chrome
        self.Click_on_Connect_wallet1 = locate.Click_on_Connect_wallet
        self.Get_a_new_wallet_click1 = locate.Get_a_new_wallet_click
        self.addusername = locate.Enter_user_name
        self.setpassword = locate.Enter_set_password
        self.confirmpassword = locate.Enter_confirm_password
        self.clicknextbutton = locate.Click_next_button
        self.skip = locate.skiptab
        self.openwallet = locate.open_wallet
        self.reconnectwall = locate.reconnect_wallet
        self.allow = locate.Allow_button
        self.mainpage_login = locate.main_page_login
        self.click_ontrade = locate.click_on_trade
        self.select_market1 = locate.select_market
        self.supra = locate.select_market_supra
        self.Swapx_exchange = locate.Swap_x_Exchange
        self.Swapy_exchange = locate.Swap_y_Exchange
        self.Swapx_value = locate.Swap_x_Valuee
        self.Swapy_value = locate.Swap_y_Valuee
        self.swapbutton = locate.Swap_button
        self.Token = locate.Token_search
        self.x_onedollar = locate.x_one_dollar_value
        self.y_onedollar = locate.y_one_dollar_value
        self.swapp_button11 = locate.swap_button_direct
        self.poolcheckerror = locate.pool_not_found_error
        self.ackno_click = locate.acknow_click
        self.txclose = locate.Transaction_close
        self.yamountvalidate = locate.y_amount_validate
        self.starkeyconfirmorallow = locate.starkey_confirm_or_allow 
        self.starrkeydeny = locate.starkey_deny
        self.starkeypopmsg = locate.starkey_deny_popup_msg
        self.wallet_msg = locate.wallet_msg_display
        self.tx_valid = locate.TX_validation
        self.tx_submit = locate.TX_submitted
        self.txview = locate.TX_View
        self.eventpointer = locate.event_pointer
        self.viewexp = locate.view_exp
        self.Transaction_failed_ok = locate.Transaction_failed_ok
        self.Transaction_failed = locate.Transaction_failed
        self.txstatus = locate.User_TX_status
        self.vmstatus = locate.VM_status
        self.swaperrormsg = locate.Swap_error_msg
        self.provideliqui = locate.provide_liquidity
        self.Tradetoswapclick = locate.Trade_to_swap_click
        self.clickonposs = locate.click_onPos
        self.noposition_found = locate.Nopositionfound
        self.my_position1 = locate.my_position
        self.senderelement = locate.sender_element
        self.receiverelement = locate.receiver_element
        self.explorepooll = locate.click_on_explorepools
        self.click_on_po1 = locate.click_on_po
        self.click_on_arrow1 = locate.click_on_arrow   
        self.enter_input1 = locate.enter_input
        self.remove_liquidity12 = locate.Remove_liquidity1
        self.slider1 = locate.slider
        self.remove_liq1 = locate.Remove_liqu
        self.wallet_already_have_btn1 = locate.wallet_already_have_btn
        self.private_key_btn1 = locate.private_key_btn
        self.network_dropdown1 = locate.network_dropdown
        self.supra_network_option1 = locate.supra_network_option
        self.next_btn1 = locate.next_btn
        self.all_networks_tab1 = locate.all_networks_tab
        self.testnet_btn1 = locate.testnet_btn
        self.password_input1 = locate.password_input
        self.login_failed_msg1 = locate.login_failed_msg
        self.hash_text1 = locate.hash_text
        self.slipage_check = locate.slipage_check
        self.slipage_2 = locate.slipage_check_2
        self.savebtton = locate.savebtn
        self.ypriceusd = locate.y_price_usd
        self.ypriceusdverify = locate.y_price_usd_Verify
        self.xpriceusd = locate.x_price_usd
        self.xpriceusdverify = locate.x_price_usd_Verify
        self.poolpagetitle = locate.pool_page_title
        self.createpool = locate.create_pool_btn
        self.clearbtn = locate.clear_btn
        self.quotetoken = locate.quote_token_dropdown
        self.standtab = locate.standard_tab
        self.concenttab = locate.concentrated_tab
        self.Recreate_pool = locate.RecreatePool_loc
        self.amountinput = locate.amount_input
        self.customrangetab = locate.custom_range_tab 
        self.poolfinal = locate.create_pool_final_btn 
        self.setinitialprice = locate.Createpoolsetprice
        self.Title_click = locate.Title_click
        self.Homepageclaim = locate.Homepage_claim
        self.wallet_password1 = locate.wallet_password
        self.wallet_login_btn1 = locate.wallet_login_btn
        self.wallet_popup_msg1 = locate.wallet_popup_msg
        self.msg_pop_up_below1 = locate.msg_pop_up_below
        self.Create_pool_min_print1 = locate.Create_pool_min_print
        self.Create_pool_max_print1 = locate.Create_pool_max_print
        self.Live_Token_price1 = locate.Live_Token_price
        self.x_deposit_Ratio_text1 = locate.x_deposit_Ratio_text
        self.y_deposit_Ratio_text1 = locate.y_deposit_Ratio_text
        self.earn_tab1 = locate.earn_tab
        self.pool_button1 = locate.pool_button
        self.positions_text1 = locate.positions_text
        self.filter_by_token1 = locate.filter_by_token
        self.ethereum_input1 = locate.ethereum_input
        self.tickmark = locate.tick
        self.supra_input1 = locate.supra_input
        self.v3_pool1 = locate.v3_pool
        self.swap_table_row1 = locate.swap_table_row
        self.clmm_button1 = locate.clmm_button
        self.y_usd_input1 = locate.y_usd_input
        self.x_usd_input1 = locate.x_usd_input
        self.x_usd_button1 = locate.x_usd_button
        self.terms_checkbox1 = locate.terms_checkbox
        self.Highpriceimpact = locate.High_price_impact_msg
        self.positionindex8 = locate.Index_8
        self.positionindex7 = locate.Index_7
        self.positionindex6 = locate.Index_6
        self.positionindex6inactivee = locate.Index_6inactive
        self.click_on_increase1 = locate.click_on_increase
        self.Increase_liquidity1 = locate.Increase_liquidity
        self.click_on_earn1 = locate.click_on_earn
        self.click_on_pool1 = locate.click_on_pool
        self.click_on_liquidity1 = locate.click_on_liquidity
        self.click_on_base_token_pair1 = locate.click_on_base_token_pair
        self.click_on_Token_x_y1 = locate.click_on_Token_x_y
        self.element_visiibility_x_y1 = locate.element_visiibility_x_y
        self.click_on_base_query_pair1 = locate.click_on_base_query_pair
        self.pool_type1 = locate.pool_type
        self.fee_tier_dropdown1 = locate.fee_tier_dropdown
        self.fetch_fee_tier1 = locate.fetch_fee_tier
        self.click_on_continue1 = locate.click_on_continue
        self.token_search = locate.token_search_input
        self.click_on_basetoken = locate.base_token_dropdown
        self.poolexist = locate.pool_exists_text
        self.Remove_max1 = locate.Remove_max

    def click_element(self, driver, by, locator, delay=2):
        Logger.logger.info(f"✅ 👉 Trying to click locator: {locator}")
        try:
            self.driver.implicitly_wait(5)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by, locator))).click()
            self.driver.implicitly_wait(5)
            return True
        except:
            Logger.logger.error(f"Failed to click element: {locator}")
            return False
            
    def get_element(self,  by, locator, timeout=10, visible = True):
        try:
            if visible:
                self.driver.implicitly_wait(5)
                return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((by, locator)))
            else:
                self.driver.implicitly_wait(5)
                return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, locator)))
            
        except TimeoutException:
            Logger.logger.error(f"Timeout: Element not found or not visible -> {locator}")
            return None
        except Exception as e:
            Logger.logger.error(f"Error occurred while finding element: {locator} -> {e}")
            return None
        

            
    def Login_URL1(self):
        return URL.URL1

    def entering_password(self):
        input_field= self.get_element(By.XPATH, self.webportal_xpath)
        input_field.clear()
        input_field.send_keys(self.creden)

    def Click_on_login(self):
        return self.mainpage_login
    
    def Privatekey(self):
        input_field = self.get_element(By.XPATH, self.private)
        input_field.clear()
        input_field.send_keys(self.privateekey)

    def senderelement1(self):
        return self.senderelement

    def receiverelement1(self):
        return self.receiverelement

    def connection_wallet(self, timeout=5):
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
        input_field = self.get_element(By.XPATH, self.addusername)
        input_field.clear()
        input_field.send_keys(wallet_details.Username)
    
    def setpassword1(self):
        input_field = self.get_element(By.XPATH, self.setpassword)
        input_field.clear()
        input_field.send_keys(wallet_details.Password)

    def confirmpassword1(self):
        input_field = self.get_element(By.XPATH, self.confirmpassword)
        input_field.clear()
        input_field.send_keys(wallet_details.Password)

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

    def Create_pool_min_print_2(self):
        return self.Create_pool_min_print1
        
    def Create_pool_max_print1_2(self):
        return self.Create_pool_max_print1
    
    def Live_Token_price1_2(self):
        return self.Live_Token_price1
    
    def x_deposit_Ratio_text1_2(self):
        return self.x_deposit_Ratio_text1
    
    def y_deposit_Ratio_text1_2(self):
        return self.y_deposit_Ratio_text1
    
    def Swap_x_value(self):
        return self.Swapx_value

    def Swap_x_onedollar_value(self, timeout=15):
        return self.get_element(By.XPATH, self.x_onedollar, timeout=timeout)

    def Swap_y_value(self, value="1"):
        ele21 = self.get_element(By.XPATH, self.Swapy_value)
        ele21.clear()
        ele21.send_keys(value)
        time.sleep(1)
        return ele21

    def Swap_y_onedollar_value(self):
        ele = self.get_element(By.XPATH, self.y_onedollar)
        return ele

    def earn2poolswap_y(self, value="1"):
        y_usd = self.get_element(By.XPATH, self.yusdinput())
        y_usd.clear()
        y_usd.send_keys(value)
        time.sleep(1)

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
    
    def RecreatePool(self):
        return self.Recreate_pool

    def swaperrormsg1(self):
        return self.swaperrormsg

    def starkeyconfirmation(self):
        return self.starkeyconfirmorallow
    
    def starkeypopread(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_any_elements_located((By.XPATH, self.starkeypopmsg)))
        
    def tx_validation(self):
        return self.tx_valid
    
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
    
    def clickbasetoken(self):
        return self.click_on_basetoken
    
    def tokensearch(self):
        return self.token_search

    def quoteetoken(self):
        return self.quotetoken
    
    def Swapx_exchangee(self):
        return self.Swapx_exchange
    
    def Swapy_exchangee(self):
        return self.Swapy_exchange

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
    
    def Removemax2(self):
        return self.Remove_max1
        
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
        return self.password_input1
    
    def loginfailedmsg(self):
        return self.login_failed_msg1
    
    def Transactionfailed_ok(self):
        return self.Transaction_failed_ok
    
    def Transactionfailed(self):
        return self.Transaction_failed
    
    def hashtext(self):
        return self.hash_text1
    
    def poolpagetitle1(self):
        return self.poolpagetitle

    def createpool1(self):
        return self.createpool
    
    def clrbtn(self):
        return self.clearbtn
   
    
    
    def standardtab(self):
        return self.standtab
   
    def concen_v3_tab(self):
        return self.concenttab
    
    def poolexistt(self):
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, self.poolexist))
        )
    
    def inputamount(self):
        return self.enter_input1
        # try:
        #     ele20 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.enter_input1)))
        #     if ele20:
        #         ele20.clear()
        #         ele20.send_keys(str(value))
        #         assert ele20.get_attribute("value") == str(value), "Amount not correctly entered!"
        #         time.sleep(1)
        #         Logger.logger.info(f"✅ Entered amount: {value}")
        #         return ele20
        #     else:
        #         raise Exception(f"Amount input field not found:")
        # except Exception as e:
        #     Logger.logger.error(f"❌ Failed to enter amount: {e}")
        #     return None

    def customtab(self):
        return self.customrangetab
    
    def pooladd(self):
        return self.poolfinal
    
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

    def Homepage_claim1(self):
        return self.Homepageclaim

    def Title_click1(self):
        return self.Title_click

    def wallet_password_1(self):
        return self.wallet_password1

    def wallet_login_btn_1(self):
        return self.wallet_login_btn1

    def wallet_popup_msg_1(self):
        return self.wallet_popup_msg1

    def msg_pop_up_below_1(self):
        return self.msg_pop_up_below1
    
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

    def eventpointerr(self):
        self.click_element(self.driver, By.XPATH, self.eventpointer)

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
    