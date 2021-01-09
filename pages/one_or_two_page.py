from base.basepage import BasePage
import utils.custom_logger as cl

class OneOrTwo(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    ################
    ### Locators ###
    ################

    _single_bearing=("single-bearing","class")
    _page_url="one-or-two"

    def wait_for_one_or_two_page_to_load(self):
        self.wait_for_given_url(self._page_url)
        self.wait_for_page_to_load()

    def click_on_single_bearing_img(self):
        self.elementClick(*self._single_bearing)
        cl.allurelogs("clicked on single bearing image")
