import logging
import utils.custom_logger as cl
from base.basepage import BasePage
class PrivacyNotification(BasePage):
    log = cl.customLogger(logging.DEBUG)
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    ################
    ### Locators ###
    ################
    _accept_continue_button=("//button[contains(text(),'Accept & continue')]","xpath")
    _page_url="privacy-notification"

    def wait_for_privacy_notification_page_to_load(self):
        self.wait_for_given_url(self._page_url)
        self.wait_for_page_to_load()

    def click_on_accept_continue(self):
        self.elementClick(*self._accept_continue_button)
        cl.allurelogs("clicked on accept and continue button")



