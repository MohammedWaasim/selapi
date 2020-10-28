import logging
import os
import pdb
import pytest
from base.webdriverfactory import WebDriverFactory
from pages.home.login_page import LoginPage
import configparser
from utils import custom_logger as cl

@pytest.fixture(scope="class")
def oneTimeEveryClassSetup(request):
    print("Running for every class")
    config = configparser.ConfigParser()
    config.read('properties.ini')
    lib_testdata_file = config['Library']["TestData"]
    if request.cls is not None:
        print("taking all the test data")
        request.cls.kode_it_testdata_file = config['LetsKodeIt']["TestData"]
        request.cls.ndtv_test_file = config['NDTVTest']['NdtvTestData']
        request.cls.lib_testdata_file = lib_testdata_file
        request.cls.appid = os.environ['appid']
    yield True
    print("Running one time tearDown for every Class")

@pytest.fixture(scope="function")
def oneTimeDriverSetup(request, browser):
    print("Running DRIVER SETUP")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
    print("Running DRIVER QUIT")


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