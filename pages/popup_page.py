import logging
import pdb

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
        return self.getElement("(//div[@class='gtx-body'])[2]","xpath")

class PopupPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
        self.map=PopupPageMap(driver)

    def enter_input_text(self,input_string):
        self.map.sendKeys(input_string,element=self.map.input_field())

    def click_translate(self):
        self.elementClick(element=self.map.translate_button())

    def get_translated_text(self):
        return self.map.translated_text().text.lower()

