import pytest
from pageObject.LoginPage import LoginPage
from utilities.conftest import dec,driver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from utilities.conftest import dec ,driver
import time
from jsonschema import validate,ValidationError
from selenium.webdriver.common.by import By

class Test_login:


    @dec
    def test_search(self, driver):
        driver.get("https://www.google.com")
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("Python Decorators")
        search_box.submit()
 # Note: Google's title changes after search, verify logic accordingly
        WebDriverWait(driver, 10).until(EC.title_contains("Python"))
        assert "Python" in driver.title
    @dec
    def test_registration_form(self, driver):
        print("---test_registration_form in progress")
        driver.get("https://testautomationpractice.blogspot.com/")
        driver.find_element(By.ID, "name").send_keys("John Doe")
        driver.find_element(By.ID, "email").send_keys("john.doe@example.com")
        driver.find_element(By.ID, "phone").send_keys("1234567890")
        driver.find_element(By.ID, "textarea").send_keys("123 Selenium Lane")
        driver.find_element(By.ID, "male").click()
        driver.find_element(By.ID, "monday").click()
        country_dropdown = Select(driver.find_element(By.ID, "country"))
        country_dropdown.select_by_visible_text("India")

 # Verify action
        assert "testautomationpractice" in driver.current_url
        print("Registration form fields filled successfully.")


    @dec
    def test_search_functionality(self,driver):
        print("---test_search_functionality in progress")
        driver.get("https://testautomationpractice.blogspot.com/")
        driver.find_element(By.ID, "Wikipedia1_wikipedia-search-input").send_keys("Selenium")
        driver.find_element(By.XPATH, '//input[@class="wikipedia-search-button"]').click()

        wait = WebDriverWait(driver, 10)
        results_container = wait.until(
        EC.presence_of_element_located((By.ID, "Wikipedia1_wikipedia-search-results")) )

        links = results_container.find_elements(By.TAG_NAME, "a")
        assert len(links) > 0
        print(f"Found {len(links)} results.")


    def test_amazon(self,driver):

        driver.get("https://www.amazon.com/")
        driver.implicitly_wait(2)
        element=driver.find_element(By.XPATH,'//i[@class="a-icon a-icon-next-rounded"]/span')
        action=ActionChains(driver)
        action.move_to_element(element).perform()
        element = driver.find_element(By.XPATH, '//i[@class="a-icon a-icon-next-rounded"]/span')
        action = ActionChains(driver)
        action.move_to_element(element).perform()


    def test_schema(self):
        response=    {
            "User_id":1,
            "User_name":"Baburao",
            "email":"example.com"

        }

        schema=\
            {
        "type":"object",
        "properties":{
              "User_id":{"type":"number"},
            "User_name":{"type":"string"},
            "email":{"type":"string"}
            },
            "required":["User_id","User_name"]
        }

        try:
            validate(instance=response,schema=schema)
            print(f"Schema is correct")
        except  ValidationError as e:
            pytest.fail(f"Schema is not correct{e.message}")