import pdb

from selenium.webdriver.remote.webelement import WebElement

import utils.custom_logger as cl
import logging

from base.basepage import BasePage

class RegisterCoursePageMap(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    def search_box(self) ->WebElement:
        return self.getElement("course","name")

    def course(self,courseName)->WebElement:
        return self.getElement(f"//div[contains(@class,'course-title')]//h4[contains(text(),'{courseName}')]","xpath")

    def all_courses(self):
        return self.getElement("course-listing-title", "xpath")

    def enroll_button(self):
        return self.getElement("//button[text()='Enroll in Course']", "xpath")

    def cc_num(self):
        return self.getElement("cardnumber","name")

    def cc_exp(self):
        return self.getElement("exp-date", "name")

    def cc_cvv(self):
        return self.getElement("cvc", "name")

    def submit_enroll(self):
        return self.getElement("(//button[contains(@class,'btn-submit')])[2]", "xpath")

    def enroll_error_message(self):
        return self.getElement("//div[@class='card-errors has-error']/ul/li/span", "xpath")

    def card_number_frame(self):
        return self.getElement("//iframe[@title='Secure card number input frame']", "xpath")

    def expiry_date_frame(self):
        return self.getElement("//iframe[@title='Secure expiration date input frame']", "xpath")

    def security_code_frame(self):
        return self.getElement("//iframe[@title='Secure CVC input frame']", "xpath")

class RegisterCoursesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.map=RegisterCoursePageMap(driver)
        self.driver = driver

    ################
    ### Locators ###
    ################
    #_search_box = "course"
    #_course = "//div[contains(@class,'course-title')]//h4[contains(text(),'{0}')]"
    _all_courses = "course-listing-title"
    _enroll_button = "//button[text()='Enroll in Course']"
    _cc_num = "cardnumber"
    _cc_exp = "exp-date"
    _cc_cvv = "cvc"
    _submit_enroll = "(//button[contains(@class,'btn-submit')])[2]"
    _enroll_error_message = "//div[@class='card-errors has-error']/ul/li/span"
    _card_number_frame="//iframe[@title='Secure card number input frame']"
    _expiry_date_frame="//iframe[@title='Secure expiration date input frame']"
    _security_code_frame="//iframe[@title='Secure CVC input frame']"

    ############################
    ### Element Interactions ###
    ############################

    def enterCourseName(self, name):
        self.sendKeys(name,element=self.map.search_box())

    def selectCourseToEnroll(self, fullCourseName):
        self.elementClick(element=self.map.course(fullCourseName))

    def clickOnEnrollButton(self):
        self.elementClick(locator=self._enroll_button, locatorType="xpath")

    def enterCardNum(self, num):
        self.switchToFrame(element=self.map.card_number_frame)
        self.sendKeys(num, element=self.map.cc_num)
        self.switchToDefaultContent()

    def enterCardExp(self, exp):
        self.switchToFrame(element=self.map.expiry_date_frame)
        self.sendKeys(exp, element=self.map.cc_exp)
        self.switchToDefaultContent()

    def enterCardCVV(self, cvv):
        self.switchToFrame(element=self.map.security_code_frame)
        self.sendKeys(cvv, element=self.map.cc_cvv)
        self.switchToDefaultContent()

    def clickEnrollSubmitButton(self):
        self.elementClick(element=self.map.submit_enroll)

    def enterCreditCardInformation(self, num, exp, cvv):
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)

    def enrollCourse(self, num="", exp="", cvv=""):
        self.clickOnEnrollButton()
        self.webScroll(direction="down")
        self.enterCreditCardInformation(num, exp, cvv)
        self.clickEnrollSubmitButton()

    def verifyEnrollFailed(self):
        result = self.isElementPresent(element=self.map.enroll_error_message)
        return result
