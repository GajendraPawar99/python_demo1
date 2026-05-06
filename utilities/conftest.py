
import pytest
import time
from functools import wraps
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By



@pytest.fixture(params=["chrome", "firefox","edge"])
def driver(request):
    browser_name = request.param
    web_driver = None

    if browser_name == "chrome":
        from selenium.webdriver.chrome.options import Options

        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-notifications")

        # REMOVE headless for captcha issue
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument(r"--user-data-dir=C:\temp\chrome_test_profile")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option("useAutomationExtension", False)

        web_driver = webdriver.Chrome(options=chrome_options)

    elif browser_name == "firefox":
        from selenium.webdriver.firefox.options import Options

        firefox_options = Options()
        firefox_options.add_argument("--width=1920")
        firefox_options.add_argument("--height=1080")
        firefox_options.add_argument("--headless")
        web_driver = webdriver.Firefox(options=firefox_options)

    elif browser_name == "edge":
        service = Service("C:/Drivers/edgedriver_win64/msedgedriver.exe")
        from selenium.webdriver.edge.options import Options

        edge_options = Options()
        edge_options.add_argument("--start-maximized")
        edge_options.add_argument("--headless")
        edge_options.add_argument("--disable-notifications")
        web_driver = webdriver.Edge(options=edge_options,service=service)

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

