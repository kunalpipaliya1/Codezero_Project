# StartKey Wallet-Automation-Framework
StartKey Wallet-Automation-Framework

# Packages need to install
-   Pytest
-   Selenium

# Application in System
-   Python IDE (Any)
-   Java JDK 8 and above

# Test we can install below:
-   pip install pytest-order    # for ordering purpose
-   pip install pytest-dependency   # for dependency purpose
-   pip install allure-pytest
-   pip install pytest-repeat # repeat task
-   pip install pytest-xdist # Install parallel plugin

# parallel test run command
path: /Kunal_Pipaliya/Project_2_Perpetuals_QA_Testnet
pytest --cache-clear -n 2 -v

# Repeat task command
pytest Project_2_Perpetuals_QA_Testnet/Test/test_1_Launch_url.py Project_2_Perpetuals_QA_Testnet/Test/test_7_From_Trade_to_Swap_wallet.py -v -s --count=5    

# Allure Report execute command
pytest -v -s Project_2_Perpetuals_QA_Testnet/Test/test_1_Launch_url.py --alluredir=allure-results
pytest Project_2_Perpetuals_QA_Testnet/Test/test_1_Launch_url.py Project_2_Perpetuals_QA_Testnet/Test/test_2_create_pool.py -v -s --alluredir=Project_2_Perpetuals_QA_Testnet/Reports/

allure generate allure-results -o allure-report --clean # allure generate HTML report # clean means old data remove and paste new data

pytest Project_2_Perpetuals_QA_Testnet/Test/test_1_Launch_url.py \
       Project_2_Perpetuals_QA_Testnet/Test/test_4_Earn_to_Swapping_Tab.py \
       -v -s --alluredir=Project_2_Perpetuals_QA_Testnet/Reports/allure-results

allure serve Project_2_Perpetuals_QA_Testnet/Reports/allure-results

# allure and html report generate command
<!-- # allure serve allure-results/ --- open indirect in browser from local machine
# allure generate --single-file allure-results/ --clean --- save the entire html file and open in local machine -->

# Runner.py how can run check below command
python3 -m Runner_file.Runner_sample_1.py

# Video recording added
Path: Project_2_Perpetuals_QA_Testnet/conftest.py file

# chrome extesntion upgrade day by day 
chrome extention receiving from Divyesh patel, he gave the .zip file
.zip > extract > google chrome manage extetion > pack extenstion > Extension root directory > select extract path > automatically generate the .cfx file


# Code execute way:
-   pytest Project_2_Perpetuals_QA_Testnet/Test/test_2_Launch_url.py -v -s # particular test run
-   pytest Project_2_Perpetuals_QA_Testnet/Test/ -v -s # inside Test/ folder all test case run with ascending order

# Run all tests:
-   pytest -v

Order → Test 1 → Test 2 → Test 3 → Test 4.

# Run only Test 4: 
-   pytest test_4.py::TestCPMM::test_6_Earn_to_Swapping_Tab -v

# Pytest will automatically run **Test 1 (launch)** first, then **Test 7**.

Run only Test 7:  pytest test_1.py::TestCPMM::test_4_liquidity_to_swap -v

  Same → Test 1 will run before Test 7.

# If you want 'test_1' to **always run before** other tests:

pytest -v -k "test_1_launch_CPMM_URL or test_6_Earn_to_Swapping_Tab"

-- pytest Project_2_Perpetuals_QA_Testnet/Test/test_1_Launch_url.py Project_2_Perpetuals_QA_Testnet/Test/test_2_create_pool.py Project_2_Perpetuals_QA_Testnet/Test/test_3_add_liquidity.py -v -s   # particular test run command

# add dependency on testcase

If i wants to add dependency from parent we need to set name na depends whom can depend

        @pytest.mark.dependency(name="launch", scope="session")
        def test_1_launch_CPMM_URL(self, call_main_url):
            driver = call_main_url 
 
        @pytest.mark.dependency(name = "Swap", depends=["launch"], scope="session")
        def test_2_From_Trade_to_Swap_wallet(self, call_main_url):
            driver = call_main_url
            
 	    @pytest.mark.dependency(name = "add_liqui", depends=["launch"], scope = "session")
    	def test_4_add_Liquidity(self, call_main_url):           
            driver = call_main_url 

# crontab added



