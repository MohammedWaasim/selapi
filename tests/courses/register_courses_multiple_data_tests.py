import pdb

from pages.courses.register_course_page import RegisterCoursesPage
from utils.teststatus import TestStatus
import unittest
import pytest
from ddt import ddt, data, unpack

@pytest.mark.usefixtures("oneTimeSetUp")
@ddt
class RegisterCoursesMultipleDataTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(("JavaScript for beginners","1111222233334444","1220","101"),("Selenium WebDriver With Python 3.x","1111222233334444","1220","101"))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum,ccExp, ccCVV):
        self.courses.enterCourseName("JavaScript")
        self.courses.selectCourseToEnroll(courseName)
        self.courses.enrollCourse(num=ccNum, exp=ccExp, cvv=ccCVV)
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result,
                          "Enrollment Failed Verification")
        self.driver.find_element_by_link_text("ALL COURSES").click()
