from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import pytest


#@pytest.fixture(params=["chrome","edge"])  # default function
@pytest.fixture()
def driver(request):
    browser = request.config.getoption("--browser")
    #browser = request.param
    print(f"[STARTING] Initializing {browser} driver")
    if browser == "chrome":
        my_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser == "edge":
        my_driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        raise TypeError(f"Expected chrome or edge but got {browser}")
    # my_driver.implicitly_wait(10)
    yield my_driver
    print(f"[CLOSING] Closing {browser} driver")
    my_driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Browser to execute test (chrome or edge)"
    )
