import pdb
import pytest
from base.webdriverfactory import WebDriverFactory
import configparser

@pytest.fixture(scope="class")
def oneTimeEveryClassSetup(request):
    print("Running for every class")
    config = configparser.ConfigParser()
    config.read('properties.ini')
    if request.cls is not None:
        print("taking all the test data")
        request.cls.flipkart_test_file = config['flipkart']['flipkartdata']
    yield True
    print("Running one time tearDown for every Class")

@pytest.fixture(scope="function")
def oneTimeDriverSetup(request, browser):
    print("Running DRIVER SETUP")
    wdf = WebDriverFactory(browser)
    if request.cls is not None:
        driver = wdf.getWebDriverInstance()
        request.cls.driver = driver
    yield driver
    driver.quit()
    print("Running DRIVER QUIT")


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

