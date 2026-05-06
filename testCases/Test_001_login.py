import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObject.LoginPage import LoginPage
from utilities.conftest import dec,driver

class Test_001_login:

    baseURL="https://admin-demo.nopcommerce.com/login"
    username='admin@yourstore.com'
    password='admin'

    @dec
    def test_HomePage_title(self,driver):
        self.driver=webdriver.Chrome()
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        self.driver.close()
        expected_title='nopCommerce demo store. Login'
        print('Page title :-',act_title)

        if act_title== expected_title:
            assert True
        else:
            assert False

    @dec
    def test_login(self, driver):
        self.driver = driver

        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        self.driver.get(self.baseURL)

        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "Email"))
        )

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.click_login()

        assert "Dashboard" in self.driver.title



