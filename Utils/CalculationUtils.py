import allure
from Project_1_CLMM_QA_Testnet.Testcases_Logs.Logging_utils import Logger

class CalculationUtils:

    @staticmethod
    def calculate_apr(Live_Token_price, Create_pool_min_print, Create_pool_max_print, x_token, y_token, x_deposit_Ratio, y_deposit_Ratio, fee_index, amount):
        try:
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

            Logger.logger.info(f"✅ ---- Token Ratio Calculation ----")
            Logger.logger.info(f"✅ pc:", pc)
            Logger.logger.info(f"✅ pmin:", pmin)
            Logger.logger.info(f"✅ pmax:", pmax)
            Logger.logger.info(f"✅ Total Ratio:", total)
            Logger.logger.info(f"✅ {x_token} Ratio %:", token0_PR, f" == Total Amount(UI) of {x_token} %:", x_deposit_Ratio)
            Logger.logger.info(f"✅ {y_token} Ratio %:", token1_PR, f" == Total Amount(UI) of {y_token} %:", y_deposit_Ratio)
            Logger.logger.info(f"✅ Difference of {x_token} position", token0_PR - x_deposit_Ratio)
            Logger.logger.info(f"✅ Difference of {y_token} position", token1_PR - y_deposit_Ratio)
            Logger.logger.info(f"✅ --------------------------------")

            allure.attach(f"pc: {pc}, pmin: {pmin}, pmax: {pmax}", 
                        name=f"Pool calculation fee Index_{fee_index}_amount_{amount}", 
                        attachment_type=allure.attachment_type.TEXT)
            allure.attach(f"x_token={x_token}, y_token={y_token}, fee_index={fee_index}, amount={amount}",
                        name="Test_Inputs", 
                        attachment_type=allure.attachment_type.TEXT)

        except Exception as e:
            allure.attach(str(e), name="CLMM_Error", attachment_type=allure.attachment_type.TEXT)
            Logger.logger.info(f"✅ Error in CLMM calculation:", e)