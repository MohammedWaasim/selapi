import traceback
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import utils.custom_logger  as cl
import logging

class WebDriverFactory():
    log = cl.customLogger(logging.INFO)
    def __init__(self, browser):
        self.browser = browser

    def getWebDriverInstance(self):
        baseUrl="https://courses.letskodeit.com/"
        if self.browser=="iexplorer":
            driver=webdriver.Ie()
        elif self.browser=="firefox":
            driver=webdriver.Firefox()
        elif self.browser=="chrome":
            #chrome_path = "/Users/mohammedwaasim/Documents/workspace_python/drivers/chromedriver"
            driver=webdriver.Chrome(ChromeDriverManager().install())
        elif self.browser=="headless":
            options = Options()
            options.headless=True
            driver = webdriver.Chrome(chrome_options=options)
        else:
            self.log.error("no such driver found driver not initiated")

        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get(baseUrl)
        return driver
