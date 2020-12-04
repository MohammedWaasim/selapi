import logging
import pdb

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

import utils.custom_logger as cl
from base.basepage import BasePage

class OptionsPageMap(BasePage):
    log=cl.customLogger(logging.INFO)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    def immediately_display_popup_radio_button(self)-> WebElement:
        return self.getElement("//div[@data-value='2']","xpath")

    def save_button(self)-> WebElement:
        return self.getElement("saveBtn","id")

    def save_status(self)->WebElement:
        return self.getElement("saveStatus")

class OptionsPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.map=OptionsPageMap(driver)
        self.driver=driver

    def click_on_immediately_display(self):
        self.elementClick(element=self.map.immediately_display_popup_radio_button())

    def click_on_save(self):
        self.elementClick(element=self.map.save_button())

    def get_save_status(self):
        self.waitForElement(locator="//span[@id='saveStatus'][contains(@style,'opacity: 1')]",locatorType="xpath")
        print(self.getElementAttributeValue(element=self.map.save_status(),attribute='style'))
        if(self.getElementAttributeValue(element=self.map.save_status(),attribute='style').__contains__('opacity: 1;')):
            return True
        else:
            return False



