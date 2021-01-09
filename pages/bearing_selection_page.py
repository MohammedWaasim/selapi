from base.basepage import BasePage

import utils.custom_logger as cl
class BearingSelectionStart(BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    ################
    ### Locators ###
    ################
    _rolling_bearing_img=("//div[text()='Rolling bearing']/preceding-sibling::div/img","xpath")
    _page_url="bearing-selection-start"

    def wait_for_bearing_selection_start_page_to_load(self):
        self.wait_for_given_url(self._page_url)
        self.wait_for_page_to_load()

    def click_on_rolling_bearing_img(self):
        self.elementClick(*self._rolling_bearing_img)
        cl.allurelogs("clicked on accept and continue button")

