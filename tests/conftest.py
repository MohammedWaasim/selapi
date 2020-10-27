import logging
import os
import pdb
import pytest
from base.webdriverfactory import WebDriverFactory
from pages.home.login_page import LoginPage
import configparser
from utils import custom_logger as cl

@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("Running one time setUp")
    wdf=WebDriverFactory(browser)
    driver=wdf.getWebDriverInstance()
    lp= LoginPage(driver)
    lp.login("test@email.com", "abcabc")
    config = configparser.ConfigParser()
    config.read('properties.ini')
    if request.cls is not None:
        testdata_file = config['LetsKodeIt']["TestData"]
        request.cls.web_testdata_file = testdata_file
        request.cls.driver = driver
    yield driver
    driver.quit()
    print("Running one time tearDown")

log = cl.customLogger(logging.INFO)

@pytest.fixture(scope="class")
def oneTimeApiSetup(request, env):
    print("Running one time Api Setup")
    config = configparser.ConfigParser()
    config.read('properties.ini')
    if env and request.cls is not None:
        url = config['Library']["StagingHost"]
        testdata_file = config['Library']["TestData"] #this need not be here, its for temp purpose
        resources_file = config['Library']["EndPoints"]
        request.cls.url = url
        log.info("base url is "+url)
        request.cls.testdata_file = testdata_file
        log.info("testdata accessed from " + testdata_file)
        request.cls.resources_file = resources_file
        log.info("resources accessed from " + resources_file)

@pytest.fixture(scope="class")
def oneTimeNdtvSetup(request,env, browser):
    print("Running one time NDTV Setup")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    config = configparser.ConfigParser()
    config.read('properties.ini')
    if request.cls is not None:
        print("d")
        request.cls.ndtv_test_file=config['NDTVTest']['NdtvTestData']
        request.cls.driver = driver
        request.cls.appid=os.environ['appid']
    yield driver
    driver.quit()
    print("Running one time tearDown")


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