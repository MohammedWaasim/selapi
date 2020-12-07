import logging
import pdb
import utils.custom_logger as cl
from selenium.webdriver.common.by import By

from base.basepage import BasePage


class PopupPageMap(BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    def input_field(self):
        return self.getElement("text-input")
    def translate_button(self):
        return self.getElement("//div[@role='button']","xpath")
    def translated_text(self):
        self.waitForElement(locator="(//div[@class='gtx-body'])[2]",locatorType="xpath")
        return self.getElement("(//div[@class='gtx-body'])[2]","xpath")

    def translate_this_page_link(self):
        return self.getElement("translate-page")

class PopupPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
        self.map=PopupPageMap(driver)

    def enter_input_text(self,input_string):
        cl.allureLogs(f"entering {input_string} in the input filed")
        self.map.sendKeys(input_string,element=self.map.input_field())

    def click_translate(self):
        self.elementClick(element=self.map.translate_button())
        cl.allureLogs("clicking on translate button")

    def get_translated_text(self):
        cl.allureLogs("clicked on translate button")
        return self.map.translated_text().text.lower()

    def is_translate_this_page_displayed(self):
        return self.isElementPresent(element=self.map.translate_this_page_link())

    def click_translate_this_page(self):
        self.elementClick(element=self.map.translate_this_page_link())

