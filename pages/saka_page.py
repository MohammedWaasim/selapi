import logging
import pdb
import time

import utils.custom_logger as cl
from selenium.webdriver.common.by import By
from base.basepage import BasePage

class SakaPageMap(BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver


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
        self.screenShot(f"the expected {tab_name} is displayed")

