import time

import pytest
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from utilities.conftest import dec,driver

def test_assignment(driver):

    driver.get("https://nichethyself.com/tourism/")
    driver.find_element(By.XPATH,'//a[@href="customised.html"]').click()
    original_window = driver.current_window_handle
    print(f"Original window handle: {original_window}")
    all_windows = driver.window_handles

    # Switch to the new window/tab
    for window_handle in all_windows:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break
    driver.find_element(By.XPATH,'//form/input[@id="fullname"]').send_keys("Gajendra Pawar")
    web_ele=driver.find_element(By.XPATH,'//*[@id="days"]')
    dropdown1 = Select(web_ele)
    dropdown1.select_by_visible_text("Home Stay")
    time.sleep(2)
    driver.find_element(By.XPATH,"//label[text()='England']").click()
    time.sleep(2)





