import logging
import pdb
import time

from utils.read_data import getYamlData
import pytest
import unittest
import utils.custom_logger as cl
from pages.options_page import OptionsPage
from pages.popup_page import PopupPage
from pages.tplink_home_page import TplinkHomePage

@pytest.mark.usefixtures("oneTimeEveryClassSetup")
class Google_Translate(unittest.TestCase):
    log=cl.customLogger(logging.INFO)
    @pytest.fixture(autouse=True)
    def class_setup(self,oneTimeEveryClassSetup):
        print("get object of page classes")
        self.test_data=getYamlData(self.test_data_path,'google_translate')
        self.options_page= OptionsPage(self.driver)
        self.popup_page=PopupPage(self.driver)
        self.tplink_home_page=TplinkHomePage(self.driver)

    #this is to select the immediate radio button > click save and verify save status msg
    @pytest.mark.order(2)
    def test_option_page(self):
        self.driver.get(self.test_data['base_url']+self.test_data['options_page']['url'])
        time.sleep(12)
        self.options_page.wait_for_page_to_load()
        self.options_page.click_on_immediately_display()
        self.options_page.click_on_save()
        result=self.options_page.get_save_status()
        assert result

    #this is to verify the entered text "ಕನ್ನಡ" gets translated to English word "Kannada
    @pytest.mark.order(1)
    def test_popup_page(self):
        self.driver.get(self.test_data['base_url']+self.test_data['popup_page']['url'])
        time.sleep(12)
        self.popup_page.wait_for_page_to_load()
        self.popup_page.enter_input_text(self.test_data['popup_page']['input_text_in_non_english'])
        self.popup_page.click_translate()
        pdb.set_trace()
        result=self.popup_page.get_translated_text()
        assert result==self.test_data['popup_page']['translated_text_in_english']

    #this is to verify if the tplink_home home page gets translated from regional language to english language
    #this is flaky I tried with other sites ocationally right click menu gets clicked  and some time not.
    @pytest.mark.order(3)
    def test_google_page_translation(self):
        self.driver.get(self.test_data['tplink_home']['url'])
        self.tplink_home_page.wait_for_page_to_load()
        website_language=self.tplink_home_page.get_dom_language()
        self.tplink_home_page.right_click_and_select_Translate()
        changed_language=self.tplink_home_page.get_dom_language()
        assert website_language!=changed_language
