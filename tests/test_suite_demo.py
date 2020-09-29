import unittest
from tests.home.login_tests import LoginTest
from tests.courses.register_courses_csv_tests import RegisterCoursesCSVDataTests

tc1=unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2=unittest.TestLoader().loadTestsFromTestCase(RegisterCoursesCSVDataTests)

smokeTest=unittest.TestSuite([tc1,tc2])
unittest.TextTestRunner(verbosity=2).run(smokeTest)
