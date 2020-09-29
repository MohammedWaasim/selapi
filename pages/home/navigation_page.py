import pdb

import utils.custom_logger as cl
import logging
from base.basepage import BasePage

class NavigationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _my_courses = ("My Courses","link")
    _all_courses = ("ALL COURSES","link")
    _practice = ("Practice","link")
    _user_settings_icon = "dropdownMenu1"

    def navigateToAllCourses(self):
        self.elementClick(*self._all_courses)

    def navigateToMyCourses(self):
        self.elementClick(*self._my_courses)

    def navigateToPractice(self):
        self.elementClick(*self._practice)

    def navigateToUserSettings(self):
        self.elementClick(self._user_settings_icon)