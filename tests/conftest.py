import logging
import os
import pdb
import pytest
from base.webdriverfactory import WebDriverFactory
import configparser
from utils import custom_logger as cl

@pytest.fixture(scope="function")
def oneTimeEveryClassSetup(request,browser):
    print("Running for every class")
    config = configparser.ConfigParser()
    config.read('properties.ini')
    if request.cls is not None:
        wdf = WebDriverFactory(browser)
        request.cls.test_data_path=config['GoogleData']['test_data_path']
        driver = wdf.getWebDriverInstance(crx_path=config['GoogleData']['crx_file_path'])
        request.cls.driver = driver
    yield True
    driver.quit()
    print("Running DRIVER QUIT")
    print("Running one time tearDown for every Class")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")
    parser.addoption("--env", help="Api Automation or combinational Suite")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")

@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption("--env")