import logging
import pdb
from traceback import print_stack
import allure
from allure_commons.model2 import Attachment

from utils import custom_logger as cl
from base.basepage import BasePage


class TestStatus(BasePage):
    log = cl.customLogger(logging.INFO)

    def __init__(self,driver):
        super(TestStatus,self).__init__(driver)
        self.resultlist=[]

    def setResult(self, result, resultMessage):
        try:
            if result is not None:
                if result:
                    self.resultlist.append("PASS")
                    self.log.info("###Verification Successful")
                else:
                    self.resultlist.append("FAIL")
                    self.log.info("###Verification Failed :: " +resultMessage)
                    self.screenShot(resultMessage)
            else:
                self.resultlist.append("FAIL")
                self.log.error("###Verification Failed :: " + resultMessage)
                self.screenShot(resultMessage)
        except:
            self.resultlist.append("FAIL")
            self.log.error("###Exception Occurred!!! ")
            self.screenShot(resultMessage)


    def mark(self, result, resultMessage):
        self.setResult(result,resultMessage)

    def markFinal(self, testName,result, resultMessage):
        self.setResult(result,resultMessage)
        if "FAIL" in self.resultlist:
            self.log.error("###### TEST FAILED")
            self.resultlist.clear()
            assert True==False
        else:
            self.log.info(testName + "###### TEST PASSED")
            self.resultlist.clear()
            assert True==True


