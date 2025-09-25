# Utils/ApiUtils.py
import requests
import json
from Testcases_Logs.Logging_utils import Logger

class ApiUtils:
    url = "https://qa-api.dexlyn.com/pools/pools-detail-v3"
    headers = {
        'Content-Type': 'application/json',
        'api-key': 'ccf794383684a1564bb31656d07bc556db869a5903dc8cd455fb12179d525hr'
    }

    @staticmethod
    def get_pool_details(pool_address: str):
        payload = {"poolAddress": pool_address}
        response = requests.post(ApiUtils.url, headers=ApiUtils.headers, json=payload)
        response.raise_for_status()  # throws error if status != 200
        return response.json()

# Test/test_api.py
from Utils.ApiUtils import ApiUtils

def test_fetch_pool_id():
    pool_address = "0xe503d43f0506dba536994624982ffa873526d9ad6c3ada26a3377df03940f8c1"
    data = ApiUtils.get_pool_details(pool_address)

    # Extract pool_id
    pool_id = data["data"]["data"]["pool_id"]

    Logger.logger.info(f"✅ \nPool ID: {pool_id}")
