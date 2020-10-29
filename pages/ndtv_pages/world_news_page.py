import logging
import pdb
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from base.basepage import BasePage
import utils.custom_logger as cl

class WorldNewsPageMap(BasePage):
    log = cl.customLogger(logging.DEBUG)
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    def weather_option(self)-> WebElement:
        self.waitForElement("//div[@id='topnav']/ul/li[@class='n_weather']","xpath",3,.75)
        return self.getElement("//div[@id='topnav']/ul/li[@class='n_weather']","xpath")

    def section_menu(self)->WebElement:
        self.waitForElement("topnav_section","id")
        return self.getElement("topnav_section")

class WorldNewsPage(BasePage):

    log=cl.customLogger(logging.INFO)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
        self.map=WorldNewsPageMap(driver)

    def click_section_menu(self):
        self.map.webScroll("down")
        self.map.section_menu().click()

    def click_weather(self):
        self.elementClick(element=self.map.weather_option())




