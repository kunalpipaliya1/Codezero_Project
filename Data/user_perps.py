class credentials1():
    password_test = ["abcd123#@", "jWIdzCH5IgqLafuw"]      # correct password: "jWIdzCH5IgqLafuw"
    privatekey= "0x186e736ddb98c66134dfc9e609c2f3d2f2bcc5344d40cc51059feb3a1e4eed85"

class URL():    
    # URL1 = "https://qa-clmm.dexlyn.com/"
    # URL1 = "https://testnet-app.dexlyn.com/"
    # URL1 = "https://qa-perps.dexlyn.com/ETH_USD"
    URL1 = "https://testnet-perps.dexlyn.com/ETH_USD"

class Extension:
    chrome_extension = "chrome-extension://hcjhpkgbmechpabifbggldplacolbkoh/fullpage.html"

class CLMM_Login:
    privatekey= "0x186e736ddb98c66134dfc9e609c2f3d2f2bcc5344d40cc51059feb3a1e4eed85"

class Email():
    source_folder = "/Kunal_Pipaliya/Project_1_CLMM_QA_Testnet/Reports/Allure_Report/General_output/Index_HTML"
    output_folder = "/Kunal_Pipaliya/Project_1_CLMM_QA_Testnet/Reports/zip_Folder"    

class Runner_sample_1_parallel_test():
    BASE_DIR = "/Kunal_Pipaliya/Project_2_Perpetuals_QA_Testnet"
    ALLURE_RESULTS = "/Kunal_Pipaliya/Project_2_Perpetuals_QA_Testnet/Reports/Allure_Report/General_output/Report_output"
    ALLURE_REPORT_DIR = "/Kunal_Pipaliya/Project_2_Perpetuals_QA_Testnet/Reports/Allure_Report/General_output/Index_HTML"
    Email = "/Kunal_Pipaliya/Project_2_Perpetuals_QA_Testnet/Email"

class screenshot_dir1():
    import datetime
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    SCREENSHOT_DIRR = "/Kunal_Pipaliya/Project_2_Perpetuals_QA_Testnet/Screenshots"
    SCREENSHOT_DIRR_Transaction = f"/Kunal_Pipaliya/Project_2_Perpetuals_QA_Testnet/Screenshots/Transaction_validation_element_not_found_{timestamp}.png"    

class Logging_utils():
    import datetime
    filename = f"/Kunal_Pipaliya/Project_2_Perpetuals_QA_Testnet/Reports/Test_cases_logs/Testcases_log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"

class Video_dir():
    VIDEO_DIR = "/Kunal_Pipaliya/Project_2_Perpetuals_QA_Testnet/Video_Recording/"

class Starkey_wallet():
    Extension_Add_argument = "--load-extension=/Kunal_Pipaliya/Project_2_Perpetuals_QA_Testnet/Extensions/Chrome_extension_11_09/Chrome_Production_Wallet_Extension_11_09" 
    Extension_Add = "/Kunal_Pipaliya/Project_1_CLMM_Project_2_Perpetuals_QA_TestnetQA_Testnet/Extensions/Chrome_extension_03_09/Chrome_Production_Wallet_Extension_03_09.crx"    