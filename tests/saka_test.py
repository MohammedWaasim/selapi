import logging
import pdb
import time
import cv2
from utils.read_data import getYamlData
import pytest
import unittest
import utils.custom_logger as cl
from pages.saka_page import SakaPage
from collections import Counter
from pages.options_page import OptionsPage
import pyautogui

@pytest.mark.usefixtures("oneTimeEveryClassSetup")
class Google_Translate(unittest.TestCase):
    log=cl.customLogger(logging.INFO)
    @pytest.fixture(autouse=True)
    def class_setup(self,oneTimeEveryClassSetup):
        print("get object of page classes")
        self.test_data=getYamlData(self.test_data_path,'saka')
        self.saka=SakaPage(self.driver)
        self.options=OptionsPage(self.driver)

    @pytest.mark.order(1)
    def test_saka_tabs_switch(self):
        """
        launch saka page and save the window handle
        launch all the sites listed in test_data
        save test_site[oslash] window handle
        switch back to saka page and launch saga again
        select a [test]site from the list of tabs in saga window
        Note: current window handle is lost since the window switching is performed by saka not by Selenium
        initiate switching to test site[saved in step3] and take a snapshot to document it in the report.
        :return:
        """
        self.driver.get(self.test_data['base_url']+self.test_data['saka_home'])
        default_window=self.driver.current_window_handle
        window_list=[default_window]
        for sites in  self.test_data['websites']:
            self.driver.execute_script(f"window.open('{self.test_data['websites'][sites]}')")
            new_window=Counter(self.driver.window_handles)-Counter(window_list)
            self.driver.switch_to_window(list(new_window)[0])
            self.saka.wait_for_page_to_load()
            window_list=self.driver.window_handles
            if(sites==self.test_data['test_tab']):
                test_window=list(new_window)[0]
        self.driver.switch_to_window(default_window)
        #launching saka page in the default window
        self.driver.get(self.test_data['base_url'] + self.test_data['saka_home'])
        self.saka.wait_for_page_to_load()
        #switching oslash tab
        self.saka.select_tabs_in_saka_window(self.test_data['websites'][self.test_data['test_tab']])
        #######
        self.driver.switch_to_window(test_window)
        self.saka.screenShot("the switched window")

    @pytest.mark.order(2)
    def test_setting_bookmark(self):
        """
        launch test page[oslash site]
        bookmark test page by pressing ['Command'+ 'd'] and click on default 'done' button
        launch saka page in another window and switch to the saka page window
        switch to select bookmark tab
        verify test page[oslash] is in the bookmark list
        :return:
        """
        self.driver.get(self.test_data['websites'][self.test_data['test_tab']])
        test_window=self.driver.current_window_handle
        self.saka.wait_for_page_to_load()
        pyautogui.keyDown('command')
        pyautogui.press('d')
        pyautogui.keyUp('command')
        time.sleep(2)
        pyautogui.press('enter')
        self.driver.execute_script(f"window.open('{self.test_data['base_url'] + self.test_data['saka_home']}')")
        [self.driver.switch_to_window(window) for window in self.driver.window_handles if (window !=test_window)]
        self.saka.select_bookmark_tab()
        self.saka.wait_for_bookmarks_to_display()
        assert self.test_data['websites'][self.test_data['test_tab']]== self.saka.get_bookmarked_site()

    @pytest.mark.order(3)
    def test_update_default_mode(self):
        """
        This method is used to update the default mode displayed in saka window.
        steps:
            launch saka page
            verify default mode displayed as 'Tabs'
            launch options page
            update the default mode to display 'Bookmarks' and save
            launch saka page again
            verify updated default mode displayed as 'Bookmarks'
        :return:
        """
        self.driver.get(self.test_data['base_url'] + self.test_data['saka_home'])
        self.saka.wait_for_page_to_load()
        assert self.test_data['default_mode']==self.saka.get_mode_displayed()
        self.driver.get(self.test_data['base_url'] + self.test_data['options_page'])
        self.options.select_default_mode(self.test_data['update_default_mode'])
        self.options.click_save_button()
        self.driver.get(self.test_data['base_url'] + self.test_data['saka_home'])
        assert self.test_data['update_default_mode'] == self.saka.get_mode_displayed()




