import pdb
import time

import pyautogui
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from base.basepage import BasePage


class TplinkHomePage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    def right_click_and_select_Translate(self):
        count=0
        while(self.get_dom_language()=='es-ar' and count<4):

            try:
                actions=ActionChains(self.driver)
                actions.context_click(None).perform()
                pyautogui.typewrite(['t','enter'])
                WebDriverWait(self.driver, 10).until(lambda driver: driver.execute_script(
                    "return document.getElementsByTagName('html')[0].getAttribute('lang')") != 'es-ar')
            except TimeoutException:
                print("will try again")
                actions=None
                count=count+1


    def get_dom_language(self):
        return self.driver.execute_script("return document.getElementsByTagName('html')[0].getAttribute('lang')")
