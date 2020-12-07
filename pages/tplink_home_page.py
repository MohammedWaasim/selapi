import pdb
import time

import pyautogui
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import utils.custom_logger as cl
import allure
from allure_commons.types import AttachmentType
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
                cl.allureLogs("waiting for 10 sec for website language to change from regional language")
            except TimeoutException:
                print("will try again")
                actions=None
                count=count+1
                cl.allureLogs(f"could not click on 'Translate to english' wait from past {str(count*10)} sec")
                self.screenShot("unable to translate page")


    def get_dom_language(self):
        cl.allureLogs("returning dom language")
        return self.driver.execute_script("return document.getElementsByTagName('html')[0].getAttribute('lang')")
