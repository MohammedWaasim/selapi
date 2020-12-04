import logging
import os
import pdb
import pytest
from base.webdriverfactory import WebDriverFactory
from pages.home.login_page import LoginPage
import configparser
from utils import custom_logger as cl

@pytest.fixture(scope="function")
def oneTimeEveryClassSetup(request,browser):
    print("Running for every class")
    config = configparser.ConfigParser()
    config.read('properties.ini')
    if request.cls is not None:
        request.cls.ndtv_test_file = config['NDTVTest']['NdtvTestData']
        request.cls.test_data_path=config['GoogleData']['test_data_path']
        wdf = WebDriverFactory(browser)
        driver = wdf.getWebDriverInstance(crx_path=config['GoogleData']['crx_file_path'])
        request.cls.driver = driver
    yield True
    driver.quit()
    print("Running DRIVER QUIT")
    print("Running one time tearDown for every Class")

# @pytest.fixture(scope="function")
# def oneTimeDriverSetup(request, browser):
#     print("Running DRIVER SETUP")
#     wdf = WebDriverFactory(browser)
#     driver = wdf.getWebDriverInstance()
#     if request.cls is not None:
#         request.cls.driver = driver
#     yield driver
#     driver.quit()
#     print("Running DRIVER QUIT")


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