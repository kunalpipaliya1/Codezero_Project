from selenium.webdriver.common.by import By

class FA_Address_click:
    def click_fa_address(driver, expected_full, expected_short):
        """
        Clicks the FA address container if Full or Short address matches.
        If not found, clicks the fallback element.
        """
        addresses = driver.find_elements(By.XPATH, "//*[@class='ui-flex ui-gap-1.5 ui-items-center ui-text-left']")
        match_found = False

        for addr in addresses:
            FA_Address = addr.text.strip()
            print("Found address:", FA_Address)

            if FA_Address == expected_short or FA_Address == expected_full:
                print("✅ Match found, clicking container...")
                container = addr.find_element(
                    By.XPATH, "./ancestor::div[contains(@class,'ui-w-full') and contains(@class,'cursor-pointer')]"
                )
                container.click()
                print("✅ Container clicked")
                match_found = True
                break

        if not match_found:
            print("❌ No matching FA address found, clicking fallback...")
            fallback = driver.find_element(
                By.XPATH, "//*[@class='lucide lucide-x size-5 cursor-pointer text-grayLighter/60 hover:text-grayLighter']"
            )
            fallback.click()
            print("✅ Fallback clicked")