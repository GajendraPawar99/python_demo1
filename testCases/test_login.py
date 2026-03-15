import pytest
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from utilities.conftest import dec ,driver
import time
from selenium.webdriver.common.by import By
# IMPORTANT: Do NOT import 'driver' here. Pytest finds it automatically.




class TestGoogleSearch:
    @dec
    def test_page_title(self, driver):
        print(f"Test Positive scenario")
        driver.get("https://www.google.com")
        assert "Google" in driver.title
        print(f"Title:-",driver.title)

    @dec
    def test_page_title_negative(self, driver):
        print(f"Test negative scenario")
        driver.get("https://www.google.com")
        assert "Google1" not in driver.title
        print(f"Title:-", driver.title)

# Output when running:
# DEBUG: Method 'test_search_performance' executed in 4.1234 seconds

    @dec
    def test_search_performance(self,driver):
        driver.get("https://www.google.com")
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("Python Decorators")
        search_box.submit()



 # Output when running:
 # DEBUG: Method 'test_search_performance' executed in 4.1234 seconds






    @dec
    def test_registration_form(self,driver):
        print("---test_registration_form in progress")
        driver.get("https://testautomationpractice.blogspot.com/")
 # 1. Fill Name
        driver.find_element(By.ID, "name").send_keys("John Doe")
        driver.find_element(By.ID, "email").send_keys("john.doe@example.com")
        driver.find_element(By.ID, "phone").send_keys("1234567890")
        driver.find_element(By.ID, "textarea").send_keys("123 Selenium Lane, Tech City")
        driver.find_element(By.ID, "male").click()
        driver.find_element(By.ID, "monday").click()
        country_dropdown = Select(driver.find_element(By.ID, "country"))
        country_dropdown.select_by_visible_text("India")
        colors = Select(driver.find_element(By.ID, "colors"))
        colors.select_by_value("red")
        driver.find_element(By.XPATH,'//input[@id="datepicker"]').click()
        element = driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[3]/td[3]/a')
        actions = ActionChains(driver)
        actions.move_to_element(element).click().perform()
        driver.find_element(By.XPATH,'// input[ @ id = "txtDate"]').click()
        element1 = driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[3]/td[6]/a')
        actions = ActionChains(driver)
        actions.move_to_element(element1).click().perform()
        driver.find_element(By.ID, "start-date").send_keys("01/10/2024")
        driver.find_element(By.ID, "end-date").send_keys("01/20/2024")
        driver.find_element(By.XPATH, '//button[@class="submit-btn"]').click()
        time.sleep(5)

 # Verify action
        assert "testautomationpractice" in driver.current_url
        print("Registration form fields filled successfully.")
    @dec
    def test_search_functionality(self,driver):
        print("---test_search_functionality in progress")
 # 1. Search
        driver.get("https://testautomationpractice.blogspot.com/")
        driver.find_element(By.ID, "Wikipedia1_wikipedia-search-input").send_keys("John Doe")
        driver.find_element(By.XPATH,'//input[@class="wikipedia-search-button"]').click()

 # 2. Wait for results to appear (prevents flaky tests)
        wait = WebDriverWait(driver, 10)
        results_container = wait.until(
        EC.presence_of_element_located((By.ID, "Wikipedia1_wikipedia-search-results")) )

 # 3. Verify links were found
        links = results_container.find_elements(By.TAG_NAME, "a")
        assert len(links) > 0
        for link in links:
            print(link.text)
            print(f"Found {len(links)} results.")

    @dec
    def test_search_functionality_negative(self,driver):
    # 1. Search
        print("---test_search_functionality_negative in progress")
        driver.get("https://testautomationpractice.blogspot.com/")
        driver.find_element(By.ID, "Wikipedia1_wikipedia-search-input")
        driver.find_element(By.XPATH,'//input[@class="wikipedia-search-button"]').click()

 # 2. Wait for results to appear (prevents flaky tests)
        wait = WebDriverWait(driver, 10)
        results_container = wait.until(
        EC.presence_of_element_located((By.ID, "Wikipedia1_wikipedia-search-results"))
        )

 # 3. Verify links were found
        links = driver.find_elements(By.XPATH, '//*[@id="Wikipedia1_wikipedia-search-results"]')

        for link in links:
            print(link.text)
            assert link.text == 'Please enter text to search.'




# ४. टेस्टमध्ये वापरणे
#     def test_google_title(browser_config):
#         driver = browser_config
#         driver.get("https://www.google.com")
#         assert "Google" in driver.title







