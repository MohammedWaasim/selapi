import unittest
from tests.home.login_tests import LoginTest
from tests.courses.register_courses_csv_tests import RegisterCoursesCSVDataTests
from tests.api_test.library_test import LibraryValidation
from tests.ndtv_test.ndtv_tests import NdtvWeather

tc1=unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2=unittest.TestLoader().loadTestsFromTestCase(RegisterCoursesCSVDataTests)
tc3=unittest.TestLoader().loadTestsFromTestCase(LibraryValidation)
tc4=unittest.TestLoader().loadTestsFromTestCase(NdtvWeather)

smokeTest=unittest.TestSuite([tc1,tc2,tc3,tc4])
unittest.TextTestRunner(verbosity=2).run(smokeTest)
