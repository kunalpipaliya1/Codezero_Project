
from Project_1_CLMM_QA_Testnet.Test.FA_Address import FA_Address_set
from Project_1_CLMM_QA_Testnet.Utils.FA_Utils import FA_Address_click
import random

class testcase_amounts:
    # amounts = list(range(1, 5)) # range or 5 and 6 both value enter
    # amounts = range(5, 6)   # exact 5 value enter
    amounts =[random.randint(1, 20)]   # pick one random integer from 1 to 100

class testcase_fee_tier:
    fee_indices = [1]
    fee_labels = ["Fee_0.01%", "Fee_0.05%", "Fee_0.3%", "Fee_1%"]
    Fee_tier = list(zip(fee_indices, fee_labels))

class testcase_token_name:
    token_pairs = [("HYPE", "POB")]

class FA_Address_full_short:
    @staticmethod
    def FA_Address_Full_Short_X_Token(driver):
        Expected_full = FA_Address_set.HYPE_Full
        Expected_short = FA_Address_set.HYPE_Short
        FA_Address_click.click_fa_address(driver, Expected_full, Expected_short)

    @staticmethod
    def FA_Address_Full_Short_Y_Token(driver):
        Expected_full = FA_Address_set.POB_Full
        Expected_short = FA_Address_set.POB_Short
        FA_Address_click.click_fa_address(driver, Expected_full, Expected_short)
