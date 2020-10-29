import logging
import pdb

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

import utils.custom_logger as cl
from base.basepage import BasePage

class NdtvHomePageMap(BasePage):
    log = cl.customLogger(logging.DEBUG)
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    def world_tab(self)-> WebElement:
        return self.getElement("//div[@class='topnav_cont']/a[text()='WORLD']","xpath")

class NdtvHomePage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        super().__init__(driver)
        self.map=NdtvHomePageMap(driver)
        self.driver=driver

    def click_world_tab(self):
        self.elementClick(element=self.map.world_tab())
        print("in click world tab")





