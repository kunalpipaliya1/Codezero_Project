import allure, logging
from Project_1_CLMM_QA_Testnet.Data.users_v3 import Logging_utils

class Logger:
    filename = Logging_utils.filename

    # Logging configuration
    logging.basicConfig(
        level=logging.INFO,   # DEBUG, INFO, WARNING, ERROR, CRITICAL
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(filename, encoding="utf-8"),   # encoding
            logging.StreamHandler()                # Show logs in terminal
        ]
    )

    # Clamp noisy third-party loggers right here
    logging.getLogger("urllib3.connectionpool").setLevel(logging.ERROR)
    logging.getLogger("selenium.webdriver.remote.remote_connection").setLevel(logging.ERROR)
    logger = logging.getLogger("TestLogger")

    # Example usage
    # logging.info("Test Started")
    # logging.warning("This is a warning")
    # logging.error("Something went wrong")

    @classmethod
    def attach_log_to_allure(cls):
        """Attach current log file to Allure report"""
        try:
            with open(cls.filename, "r", encoding="utf-8") as f:
                allure.attach(
                    f.read(), 
                    name="Test Execution Logs", 
                    attachment_type=allure.attachment_type.TEXT)
                
        except Exception as e:
            cls.logger.error(f"Could not attach logs to Allure: {e}")
