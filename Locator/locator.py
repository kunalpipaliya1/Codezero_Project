class locater_login_URL():
    
    xpath = "//*[@id='password']"
    Home_page_validate = "/html/body/div/div/div[2]/form/button/span"
    Dashboard_validate = "//a[@href='/dashboard']"
    actual_result = "/html/body/div[1]/div[1]/div/div[2]/div[1]/div"
    xpath_dashboard = "/html/body/div[1]/div[1]/div/nav/ul/li[1]/a"
    wallet_allow = "/html/body/div[1]/div[1]/div/div[2]/div[2]/div[1]/button"
    Login_validator_Link_text = "Claim Testnet "
    starkey_install_button_click = "/html/body/div[2]/ol/li/div/div/a/button/span[1]" # click operation
    click_on_chrome = "/html/body/div/div[3]/section[1]/div/div/div/div[1]/div/div/div[2]/div/div/a[1]"
    add_to_chrome = "//button[@id='add-chrome']" #"/html/body/c-wiz/div/div/main/div/section[1]/section/div/div[1]/div[2]/div/button/span[6]" # //*[@id="yDmH0d"]/c-wiz/div/div/main/div/section[1]/section/div/div[1]/div[2]/div/button/span[4]
    Click_on_Connect_wallet = "//span[text()='Connect wallet']" # "/html/body/div[1]/div[1]/div/div[2]/div[2]/div[1]/button/span"
    Get_a_new_wallet_click = "//*[@id='root']/div/div[1]/div/div[2]/div[2]/div[2]/button[1]"
    Enter_private_key = "//*[@id='privateKeyInput']"
    Enter_user_name = "//*[@name='username']"
    Enter_set_password = "//*[@name='password']"
    Enter_confirm_password = "//*[@name='confirmPassword']"
    Click_next_button = "//*[@id='create-next-btn']"
    skiptab = "//*[@id='root']/div/div[1]/div/div[2]/div/div[2]/div[1]/button"
    open_wallet = "//*[@id='root']/div/div[1]/div/div[2]/div/div[2]/button"
    reconnect_wallet = "/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div[2]/button"
    Allow_button = "//*[@id='root']/div/div[1]/div/div[2]/div/div[2]/div[2]/button[2]"
    click_on_trade = "//*[text()='Trade']" # drop down
    Trade_to_swap_click = "(//a[text()='Swap'])[1]"
    select_market = "/html/body/div[1]/div[2]/div/div/div[1]/div[1]/button[1]/div/div" # drop down
    select_market_supra = "//span[@class='text-xs sm:text-base' and text()='SUPRA-USDT']"
    Connect_wallet = "/html/body/div[1]/div[2]/div/div[2]/div/div/div[3]/div[2]/button/span"
    wallet_already_have_btn = "//button[contains(text(), 'I already have one')]"
    private_key_btn = "//*[text()='Private Key']"
    network_dropdown = "//*[text()='Network']"
    supra_network_option = "//*[text()='Supra']"
    next_btn = "//button[text()='Next']"
    all_networks_tab = "//span[text()='All Networks']"
    testnet_btn = "//button[text()='Testnet']"
    password_input = "//*[@id='password-input']"
    login_failed_msg = "//*[contains(text(), 'Invalid password. Please try again.')]"
    hash_text = "//*[@class='style_button__bI4Ti ui-group ui-relative ui-cursor-pointer ui-rounded-xl ui-overflow-hidden ui-font-semibold ui-flex ui-gap-2.5 ui-items-center ui-w-fit hover:ui-brightness-[1.15] ui-transition-[filter] ui-duration-500 ui-ease-smooth ui-justify-center ui-px-3.5 md:ui-px-5 ui-py-2 md:ui-py-2.5 ui-h-11 theme-gradient-border-button']"
    starkey_confirm_or_allow = "//button[normalize-space(text())='Confirm' or normalize-space(text())='Connect' or normalize-space(text())='Allow']" # "//*[text()='Confirm'] | //*[text()='Allow']"

class locater_perps():
    token_name = "//*[@class='text-xs sm:text-base']"
    TX_validation = "//*[text()='Transaction Success']"
    TX_View = "//a[starts-with(@href, 'https://testnet.suprascan.io/')]"
    TX_submitted = "//*[text()='Transaction submitted']"
    view_exp = "//*[@class=' ui-flex ui-items-center ui-gap-1.5 ui-text-secondary ui-transition-colors ui-duration-300 hover:ui-text-primary']"
    Transaction_close = "//*[text()='Close']"
    User_TX_status = "//*[@class='flex w-full items-center justify-start gap-1 text-lg font-medium text-txt-success-light dark:text-txt-success mobile:w-auto']"
    VM_status = "(//*[@class='flex items-end text-sm [word-break:break-word] mobile:text-base undefined'])[5]"
    Current_market_price = "//*[@class='min-w-[5rem] text-lg font-medium text-success']" # Current market price
    Index_Price = "//*[@class='min-w-[5rem] text-sm font-medium ']" # Index Price
    Funding_Rate = "(//*[@class='min-w-[5rem] text-sm font-medium'])[1]" # Funding Rate
    Market_Skew = "(//*[@class='min-w-[5rem] text-sm font-medium'])[2]" # Market Skew
    Transaction_failed_ok = "//*[@text()='OK']"
    Transaction_failed = "//*[text()='Transaction failed']"
    Token_selection = "//*[@class='truncate']"
    Token_search = "//*[@placeholder='Search']"
    Token_list = "//*[@class='text-xs sm:text-sm']"
    Long_market_order_panel = "(//*[text()='Long'])[1]"
    Market_order_panel = "//*[text()='Market']"
    Input_decimal = "//*[@inputmode='decimal']"
    Type_number = "//*[@type='number']"
    Buy_Long = "//*[text()='Buy / Long']"   #*(first click – may fail if min size not met)*
    Position_size = "//*[text()='Position size should be minimum 300 USDC ']"
    SL_Price_None =  "/html/body/div[4]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[2]/div/input"
    SL_Price_Red = "//*[@class='text-red-500 text-xs mt-1 px-1']"   # have duplicate
    Take_profit = "(//*[@type='text'])[5]"
    Take_profit_error = "//*[@class='text-red-500 text-xs mt-1 px-1']"
    SL_Price_Nonee =  "/html/body/div[4]/div/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div[2]/div/input"
    SL_Price_Red = "//*[@class='text-red-500 text-xs mt-1 px-1']"   # have duplicate
    Final_Buy_Long = "(//*[text()='Buy / Long'])[2]"

    Short_market_order_panel = "(//*[text()='Short'])[1]"
    Buy_Short = "//*[text()='Sell / Short']"
    Final_Buy_Short = "//*[text()='Sell/Short']"

    SLprice_USD = "(//*[@inputmode='decimal'])[2]"
    TPprice_USD = "(//*[@inputmode='decimal'])[3]"

    Collateral_USDC = "(//*[@class='text-sm text-white'])[1]"
    Leverage_x = "(//*[@class='text-sm text-white'])[2]"
    Liquidation_price = "(//*[@class='text-sm text-white flex items-center gap-1'])[1]"
    Position_Size_usdc = "(//*[@class='text-sm text-white flex items-center gap-1'])[2]"

    sender_element = "(//a[starts-with(@href, '/address/')])[1]"
    receiver_element = "(//a[starts-with(@href, '/address/')])[2]"