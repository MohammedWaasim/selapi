import pdb
import time
from pages.home.login_page import LoginPage
from utils.teststatus import TestStatus
import unittest
import pytest
import logging
import utils.custom_logger as cl

@pytest.mark.usefixtures("oneTimeDriverSetup","oneTimeEveryClassSetup")
class LoginTest(unittest.TestCase):
    log=cl.customLogger(logging.INFO)
    @pytest.fixture(autouse=True)
    def classSetup(self,oneTimeDriverSetup):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_web_validLogin(self):
        self.lp.login("test@email.com","abcabc")
        result2 = self.lp.verifyLoginTitle()
        self.ts.mark(result2,"Title is incorrect")
        result1 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin",result1,"Login was not successful")


    @pytest.mark.run(order=1)
    def test_web_invliadLogin(self):
        time.sleep(4)
        self.lp.login("test@email.com", "abcabc")
        self.lp.logout()
        self.lp.login("test@email.com", "123")
        result=self.lp.verifyInvalidLogin()
        self.ts.markFinal("test_invalid_Login",result,"Invalid Login Test Failed")







