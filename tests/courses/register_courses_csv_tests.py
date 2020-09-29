import pdb
from pages.courses.register_course_page import RegisterCoursesPage
from utils.teststatus import TestStatus
import unittest
import pytest
from ddt import ddt, data, unpack
from utils.read_data import getCSVData
from pages.home.navigation_page import NavigationPage

@pytest.mark.usefixtures("oneTimeSetUp")
@ddt
class RegisterCoursesCSVDataTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    def setUp(self):
        self.nav.navigateToAllCourses()

    @pytest.mark.run(order=1)
    @data(*getCSVData("testdata.csv"))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum,ccExp, ccCVV):
        self.courses.enterCourseName("JavaScript")
        self.courses.selectCourseToEnroll(courseName)
        self.courses.enrollCourse(num=ccNum, exp=ccExp, cvv=ccCVV)
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result,
                          "Enrollment Failed Verification")

