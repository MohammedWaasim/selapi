import logging
import pdb
import time

from utils.read_data import getYamlData
import pytest
import unittest
import utils.custom_logger as cl
from pages.saka_page import SakaPage
from collections import Counter

@pytest.mark.usefixtures("oneTimeEveryClassSetup")
class Google_Translate(unittest.TestCase):
    log=cl.customLogger(logging.INFO)
    @pytest.fixture(autouse=True)
    def class_setup(self,oneTimeEveryClassSetup):
        print("get object of page classes")
        self.test_data=getYamlData(self.test_data_path,'saka')
        self.saka=SakaPage(self.driver)



    @pytest.mark.order(1)
    def test_saka_tabs_switch(self):
        self.driver.get(self.test_data['base_url']+self.test_data['saka_home'])
        default_window=self.driver.current_window_handle
        window_list=[default_window]
        for sites in  self.test_data['websites']:
            self.driver.execute_script(f"window.open('{self.test_data['websites'][sites]}')")
            new_window=Counter(self.driver.window_handles)-Counter(window_list)
            self.driver.switch_to_window(list(new_window)[0])
            self.saka.wait_for_page_to_load()
            window_list=self.driver.window_handles
        self.driver.switch_to_window(default_window)
        #launching saka page in the default window
        self.driver.get(self.test_data['base_url'] + self.test_data['saka_home'])
        self.saka.wait_for_page_to_load()
        #switching oslash tab
        self.saka.select_tabs_in_saka_window(self.test_data['websites'][self.test_data['switch_tab']])

