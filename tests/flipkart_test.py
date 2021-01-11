import pdb

import pytest
import unittest

from pages.flipkart_home import FlipkartHomePage
from utils.read_data import getYamlData

@pytest.mark.usefixtures("oneTimeEveryClassSetup","oneTimeDriverSetup")
class FlipkartTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self,oneTimeDriverSetup):
        print("class setup")
        self.fk_home=FlipkartHomePage(self.driver)
        self.test_data=getYamlData(self.flipkart_test_file)
    @pytest.mark.run(order=1)
    def test_powerbank_nav(self):
        self.fk_home.wait_for_page_to_load()
        self.fk_home.click_on_x_login_popup()
        self.fk_home.click_power_bank_in_electronics_tab()
        pass

    def test_get_prices_in_range(self):
        self.fk_home.wait_for_page_to_load()
        self.fk_home.click_on_x_login_popup()
        self.fk_home.enter_search_item("makbook air")
        self.fk_home.click_submit()
        self.fk_home.wait_for_title(self.test_data['search_title'])
        self.fk_home.select_item_in_range(self.test_data['pricemin'],self.test_data['princemax'])


