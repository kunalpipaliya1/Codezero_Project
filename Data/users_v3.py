class CLMM_Login:
    # privatekey= "0x004f949f238991902f8c4513b5a08e03c6ec6c3617f0cb3ebb41f9a1571cb5e7" # Harsh
    privatekey = "0xdad0a10cf48d9c429bc818cd26a186afbfe291d5c0320ab03202a7b31c1f6e50" # Harsh_2
    # privatekey= "0x186e736ddb98c66134dfc9e609c2f3d2f2bcc5344d40cc51059feb3a1e4eed85" # Kunal


class credentials1():
    password_test = ["test", "jWIdzCH5IgqLafuw"]      # correct password: "jWIdzCH5IgqLafuw"

class URL():    
    URL1 = "https://qa-clmm.dexlyn.com/"
    # URL1 = "https://testnet-app.dexlyn.com/"

class wallet_details():
    Username = "Kunal"
    Password = "Rjio@3000"

class Runner_details_1_Kunal():
    BASE_DIR = "/Kunal_Pipaliya/Project_1_CLMM_QA_Testnet"
    ALLURE_JSON_DIR = "/Kunal_Pipaliya/Project_1_CLMM_QA_Testnet/Reports/Allure_Report/General_output/Allure_JSON_Backup"
    ALLURE_RESULTS = "/Kunal_Pipaliya/Project_1_CLMM_QA_Testnet/Reports/Allure_Report/General_output/Allure_Reports_Json_Data"
    ALLURE_REPORT_DIR = "/Kunal_Pipaliya/Project_1_CLMM_QA_Testnet/Reports/Allure_Report/General_output/Allure_Report_output"
    INDEX_HTML_DIR = "/Kunal_Pipaliya/Project_1_CLMM_QA_Testnet/Reports/Allure_Report/General_output/Index_HTML"
    EMAIL_MODULE = "Project_1_CLMM_QA_Testnet.Email.Email"
    EMAIL_CWD = "/Kunal_Pipaliya" 

class Runner_details_2_Harsh():
    BASE_DIR = "C:\\Dex\\Project_1_CLMM_QA_Testnetv6\\Project_1_CLMM_QA_Testnet"
    ALLURE_JSON_DIR = "C:\\Dex\\Project_1_CLMM_QA_Testnetv6\\Project_1_CLMM_QA_Testnet\\Reports\\Allure_Report\\General_output\\Allure_JSON_Backup"
    ALLURE_RESULTS = "C:\\Dex\\Project_1_CLMM_QA_Testnetv6\\Project_1_CLMM_QA_Testnet\\Reports\\Allure_Report\\General_output\\Allure_Reports_Json_Data"
    ALLURE_REPORT_DIR = "C:\\Dex\\Project_1_CLMM_QA_Testnetv6\\Project_1_CLMM_QA_Testnet\\Reports\\Allure_Report\\General_output\\Allure_Report_output"
    INDEX_HTML_DIR = "C:\\Dex\\Project_1_CLMM_QA_Testnetv6\\Project_1_CLMM_QA_Testnet\\Reports\\Allure_Report\\General_output\\Index_HTML"
    EMAIL_MODULE = "Project_1_CLMM_QA_Testnet.Email.Email"
    EMAIL_CWD = "/Project_1_CLMM_QA_Testnet" 

class screenshot_dir1():
    import datetime
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    SCREENSHOT_DIRR = "/Kunal_Pipaliya/Project_1_CLMM_QA_Testnet/Screenshots"
    SCREENSHOT_DIRR_Transaction = f"/Kunal_Pipaliya/Project_1_CLMM_QA_Testnet/Screenshots/Transaction_validation_element_not_found_{timestamp}.png"

class Logging_utils():
    import datetime
    filename = f"/Kunal_Pipaliya/Project_1_CLMM_QA_Testnet/Reports/Test_cases_logs/Testcases_log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"

class Video_dir():
    VIDEO_DIR = "/Kunal_Pipaliya/Project_1_CLMM_QA_Testnet/Video_Recording/"

class Starkey_wallet():
    Extension_Add_argument = "--load-extension=/Kunal_Pipaliya/Project_1_CLMM_QA_Testnet/Extensions/Chrome_extension_11_09/Chrome_Production_Wallet_Extension_11_09" 
    Extension_Add = "/Kunal_Pipaliya/Project_1_CLMM_QA_Testnet/Extensions/Chrome_extension_03_09/Chrome_Production_Wallet_Extension_03_09.crx"

class Email():
    source_folder = "/Kunal_Pipaliya/Project_1_CLMM_QA_Testnet/Reports/Allure_Report/General_output/Index_HTML"
    output_folder = "/Kunal_Pipaliya/Project_1_CLMM_QA_Testnet/Reports/zip_Folder"