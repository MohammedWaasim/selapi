import logging
import pdb
import time
import allure
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
import utils.custom_logger as cl
from selenium.webdriver.common.by import By
from base.basepage import BasePage

class OptionsPageMap(BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    def mode_label(self):
        return self.getElement("search-bar")

    def default_mode(self):
        return self.getElement("defaultModeSelect")

    def save_button(self):
        return self.getElement("//input[@type='submit']","xpath")


class OptionsPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
        self.map=OptionsPageMap(driver)

    def get_mode_displayed(self):
        return self.getElementAttributeValue("aria-label",element=self.map.mode_label())

    def select_default_mode(self,mode):
        sel=Select(self.map.default_mode())
        sel.select_by_visible_text(mode)

    def click_save_button(self):
        self.elementClick(element=self.map.save_button())





