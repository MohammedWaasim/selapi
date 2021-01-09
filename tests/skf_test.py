import pdb

import pytest
import unittest
from pages.privacy_notification_page import PrivacyNotification
from pages.bearing_selection_page import BearingSelectionStart
from pages.type_arrangement_sb_page import TypeArrangementSb
from pages.one_or_two_page import OneOrTwo
from utils.read_data import getYamlData

@pytest.mark.usefixtures("oneTimeEveryClassSetup","oneTimeDriverSetup")
class SkfTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self,oneTimeDriverSetup):
        print("get object of the page")
        self.pn=PrivacyNotification(self.driver)
        self.bs=BearingSelectionStart(self.driver)
        self.ta=TypeArrangementSb(self.driver)
        self.ot=OneOrTwo(self.driver)
        self.bearing_data=getYamlData(self.skf_test_file)

    @pytest.mark.run(order=1)
    def test_multiselect_option(self):
        self.pn.wait_for_privacy_notification_page_to_load()
        self.pn.click_on_accept_continue()
        self.bs.wait_for_bearing_selection_start_page_to_load()
        self.bs.click_on_rolling_bearing_img()
        self.ot.wait_for_one_or_two_page_to_load()
        self.ot.click_on_single_bearing_img()
        self.ta.wait_for_type_arrangement_sb_page_to_load()
        self.ta.click_on_select_bering_type()
        assert set(self.bearing_data['multi_select_options']) == set(self.ta.get_baring_types())
        self.ta.closing_dropdown()

    @pytest.mark.run(order=2)
    def test_next_button_enabling(self):
        self.pn.wait_for_privacy_notification_page_to_load()
        self.pn.click_on_accept_continue()
        self.bs.wait_for_bearing_selection_start_page_to_load()
        self.bs.click_on_rolling_bearing_img()
        self.ot.wait_for_one_or_two_page_to_load()
        self.ot.click_on_single_bearing_img()
        self.ta.wait_for_type_arrangement_sb_page_to_load()
        self.ta.click_on_select_bering_type()
        self.ta.select_given_bearing_type(self.bearing_data['baring_type'])
        self.ta.enter_designation_in_search(self.bearing_data['designation_num'])
        self.ta.wait_for_mat_table_to_load()
        self.ta.wait_for_given_details_in_mat_table_and_click(self.bearing_data['designation_num'])
        self.ta.wait_for_next_button_enabling()
        assert self.bearing_data['color_code']== self.ta.get_color_of_next_button()
