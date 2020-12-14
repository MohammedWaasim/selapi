import logging
import pdb
import time
import allure
from selenium.webdriver.remote.webelement import WebElement

import utils.custom_logger as cl
from selenium.webdriver.common.by import By
from base.basepage import BasePage

class SakaPageMap(BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    def bookmark_tab(self) -> WebElement:
        self.waitForElement("//div/i[text()='bookmark_border']","xpath")
        return self.getElement("//div/i[text()='bookmark_border']","xpath")

    def mode_label(self):
        return self.getElement("search-bar")

class SakaPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
        self.map=SakaPageMap(driver)

    def select_tabs_in_saka_window(self,tab_name):
        tab_to_click=self.getElement(f"//ul/li/span[2]/span[text()='{tab_name}']","xpath")
        self.elementClick(element=tab_to_click)
        cl.allureLogs(f"selected {tab_name} from saka window")
        time.sleep(3)

    def select_bookmark_tab(self):
        self.elementClick(element=self.map.bookmark_tab())

    def wait_for_bookmarks_to_display(self):
        self.waitForElement("//input[@aria-label='Bookmarks']","xpath")

    def get_bookmarked_site(self):
        return self.getElement("//ul/li/span[2]/span[2]","xpath").text

    def get_mode_displayed(self):
        return self.getElementAttributeValue("aria-label",element=self.map.mode_label())

