import pytest
from selenium import webdriver
from pageObject.LoginPage import LoginPage
from utilities.conftest import dec,driver
class Test_001_login:

    baseURL='https://admin-demo.nopcommerce.com/'
    username='admin@yourstore.com'
    password='admin'

    @dec
    def test_HomePage_title(self):
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
    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.click_login()
        act_title=self.driver.title
        if act_title=='Dashboard / nopCommerce administration':
            assert True
        else:
            assert False



