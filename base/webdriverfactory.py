import traceback
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import utils.custom_logger  as cl
import logging

class WebDriverFactory():
    log = cl.customLogger(logging.INFO)
    def __init__(self, browser):
        self.browser = browser

    def getWebDriverInstance(self):
        baseUrl="https://www.skfbearingselect.com"
        if self.browser=="iexplorer":
            driver=webdriver.Ie()
        elif self.browser=="firefox":
            driver=webdriver.Firefox()
        elif self.browser=="chrome":
            options = Options()
            options.add_argument("--disable-notifications")
            #chrome_path = "/Users/mohammedwaasim/Documents/workspace_python/drivers/chromedriver"
            driver=webdriver.Chrome(ChromeDriverManager().install(),options=options)
        elif self.browser=="headless":
            options = Options()
            options.headless=True
            options.add_argument("--disable-notifications")
            driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        elif self.browser=="docker-chrome":
            driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", DesiredCapabilities.CHROME)
        elif self.browser == "docker-firefox":
            driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", DesiredCapabilities.FIREFOX)

        else:
            self.log.error("no such driver found driver not initiated")

        driver.implicitly_wait(5)
        #driver.fullscreen_window()
        driver.get(baseUrl) #commented bcoz there is another testcase addded for different website
        return driver
