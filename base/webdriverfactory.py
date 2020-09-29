import traceback
from selenium import webdriver

class WebDriverFactory():
    def __init__(self, browser):
        self.browser = browser

    def getWebDriverInstance(self):
        baseUrl="https://courses.letskodeit.com/"
        if self.browser=="iexplorer":
            driver=webdriver.Ie()
        elif self.browser=="firefox":
            driver=webdriver.Firefox()
        elif self.browser=="chrome":
            chrome_path = "/Users/mohammedwaasim/Documents/workspace_python/drivers/chromedriver"
            driver=webdriver.Chrome(chrome_path)
        else:
            chrome_path = "/Users/mohammedwaasim/Documents/workspace_python/drivers/chromedriver"
            driver = webdriver.Chrome(chrome_path)

        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get(baseUrl)
        return driver
