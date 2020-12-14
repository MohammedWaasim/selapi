import pdb
import traceback
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
import utils.custom_logger  as cl
import logging

class WebDriverFactory():
    log = cl.customLogger(logging.INFO)
    def __init__(self, browser):
        self.browser = browser

    def getWebDriverInstance(self,crx_path=None)-> webdriver:
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
            driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
        elif self.browser=="chrome_with_ext":
            chop = webdriver.ChromeOptions()
            chop.add_extension(crx_path)
            driver = webdriver.Chrome(ChromeDriverManager().install(),options=chop)
        else:
            self.log.error("no such driver found driver not initiated")

        driver.implicitly_wait(10)
        driver.maximize_window()
        return driver
