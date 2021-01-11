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
    @pytest.mark.run(order=1)
    def test_powerbank_nav(self):
        self.fk_home.wait_for_page_to_load()
        self.fk_home.click_on_x_login_popup()
        self.fk_home.click_power_bank_in_electronics_tab()
        pass

    def test_get_prices_in_range(self):
        pass

