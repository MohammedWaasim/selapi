import pdb

import pytest
from base.basepage import BasePage
from pages.home.navigation_page import NavigationPage
import time
import logging
import utils.custom_logger as cl

@pytest.mark.usefixtures("setUp")
class LoginPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
        self.nav=NavigationPage(driver)


    #locators
    # _login_link="//a[contains(text(),'Sign In')]"
    # _email_filed="email"
    # _pwd_filed="password"
    # _loign_button="//input[@type='submit']"

    _login_link = ("//a[contains(text(),'Sign In')]","xpath")
    _email_filed = ("email", "id")
    _pwd_filed= ("password","id")
    _loign_button= ("//input[@type='submit']","xpath")

    def clickLoginLink(self):
        self.log.debug("clicking on login link")
        self.elementClick(*self._login_link)
        self.log.debug("clicked on login link successfully")

    def enterEmail(self,email):
        self.log.debug("entering email id")
        self.sendKeys(email, *self._email_filed)
        self.log.debug("email entered successfully")

    def enterPwd(self, pwd):
        self.log.debug("entering password")
        self.sendKeys(pwd,*self._pwd_filed)
        self.log.debug("password entered successfully")

    def clickLoginButton(self):
        self.log.debug("clicking on on login button")
        self.elementClick(*self._loign_button)
        self.log.debug("clicked on login button successfully")

    def login(self, username="", pwd=""):
        self.log.debug("performing login actions")
        self.driver.get("https://courses.letskodeit.com/")
        self.clickLoginLink()
        time.sleep(3)
        self.enterEmail(username)
        self.enterPwd(pwd)
        self.clickLoginButton()
        self.log.debug("login action completed successfully")

    def verifyLoginSuccessful(self):
        result= self.isElementPresent("//h1[text()='All Courses']", locatorType="xpath")
        return result

    def verifyInvalidLogin(self):
        result=self.isElementPresent("//span[contains(text(),'invalid')]",locatorType="xpath")
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("All Courses")

    def logout(self):
        self.nav.navigateToUserSettings()
        self.elementClick(locator="//div[contains(@class,'navbar-buttons')]//a[@href='/logout']",
                          locatorType="xpath")
