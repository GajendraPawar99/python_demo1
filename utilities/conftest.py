
import pytest
import time
from functools import wraps
from selenium.webdriver.edge.options import Options
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(params=["chrome", "firefox","edge"])
def driver(request):
    browser_name = request.param
    web_driver = None

    if browser_name == "chrome":
        web_driver = webdriver.Chrome()

    elif browser_name == "firefox":
        web_driver = webdriver.Firefox()

    elif browser_name == "edge":
        service = Service("C:/Drivers/edgedriver_win64/msedgedriver.exe")
        web_driver = webdriver.Edge(service=service)

    web_driver.maximize_window()
    web_driver.implicitly_wait(10)

    yield web_driver

    print(f"\nClosing {browser_name} browser...")
    web_driver.quit()





def dec(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        duration = end - start
        print(f"'{func.__name__}' Time taken {duration :.2f} seconds")
        return  result
    return wrapper


@pytest.fixture(scope='session',autouse=True)
def test_set_teardown():
    print("Start test")
    yield
    print("End test")

@pytest.fixture(scope='function',autouse=True)
def test_every_test():
    yield
    print("Test Execution is done")


# @pytest.fixture
# def test_login(browser_config,endpoint, expected_status):
#     driver = browser_config












# API fixtures =======================================
# =+++++++++++++++++++++++++++++++++++++++++++++++

@pytest.fixture
def api_url():
    return 'https://automationexercise.com/'
@pytest.fixture
def get():
    return 'api/productsList'

@pytest.fixture
def post():
    return 'api/productsList'

@pytest.fixture
def get_1():
    return 'api/brandsList'

