import pdb

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import os
import time
import utils.custom_logger as cl
import logging


class BasePage():
    log = cl.customLogger(logging.INFO)
    def __init__(self, driver):
        self.driver = driver


    def screenShot(self,resultMessage):
        fileName=resultMessage+ "."+str(round(time.time()*1000))+".png"
        screenShotDir="../screenshots/"
        relativeFileName=screenShotDir+fileName
        currentDir=os.path.dirname(__file__)
        destinationFile=os.path.join(currentDir,relativeFileName)
        destinationDir=os.path.join(currentDir,screenShotDir)

        try:
            if not os.path.exists(destinationDir):
                os.makedirs(destinationDir)
            self.driver.save_screenshot(destinationFile)
            allure.attach.file(destinationFile)
            self.log.info("Screenshot save to directory"+ destinationDir)
        except:
            self.log.error("#### Exception Occurred")

    def getTitle(self):
        return self.driver.title

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "linktext":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locatorType + " not correct/supported")
        return False

    def getElement(self, locator, locatorType="id")-> WebElement:
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element Found with locator "+ locator+" with locator type "+locatorType)
        except:
            self.log.info("Element not found with locator "+ locator+" with locator type "+locatorType)
            x=10
        return element

    def getElement_ele(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element Found with locator "+ locator+" with locator type "+locatorType)
        except:
            self.log.info("Element not found with locator "+ locator+" with locator type "+locatorType)
            x=10
        return element

    def getElementList(self, locator, locatorType="id"):
        elements=None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            elements = self.driver.find_elements(byType, locator)
            self.log.info("Element list found wiht locator" + locator +" and locator type "+ locatorType)
        except:
            self.log.info("Element list NOT found wiht locator" + locator + " and locator type " + locatorType)
        return elements
    def getElementColorCode(self, locator, locatorType="id"):
        element=None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            color_code=element.value_of_css_property("background-color")
            self.log.info("color code for the given locator " + locator +" is  "+ color_code)
        except:
            self.log.info("could not get color code of " + locator )
        return color_code

    def elementClick(self, locator="", locatorType="id", element=None):
        """
        Click on an element -> MODIFIED
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Clicked on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.info("Cannot click on the element with locator: " + locator +
                          " locatorType: " + locatorType)


    def sendKeys(self, data, locator="", locatorType="id", element=None):
        """
        Send keys to an element -> MODIFIED
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.info("Cannot send data on the element with locator: " + locator +
                  " locatorType: " + locatorType)


    def getText(self, locator="", locatorType="id", element=None, info=""):
        """
        NEW METHOD
        Get 'Text' on an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator: # This means if locator is not empty
                self.log.debug("In locator condition")
                element = self.getElement(locator, locatorType)
            self.log.debug("Before finding text")
            text = element.text
            self.log.debug("After finding element, size is: " + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " +  info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)

            text = None
        return text

    def isElementPresent(self, locator="", locatorType="id", element=None):
        try:
            if locator:
                element = self.getElement(locator,locatorType)
            if element is not None:
                self.log.info("Element Found with locator")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.error("Element not found")
            return False

    def elementPresenceCheck(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def waitForElement(self, locator=None, locatorType="id",
                               timeout=10, pollFrequency=0.5, element=None):
        delayed_element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, 10, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            if(element):
                delayed_element = wait.until(EC.visibility_of(element))
            else:
                delayed_element = wait.until(EC.element_to_be_clickable((byType,
                                                             locator)))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")

        return delayed_element

    def webScroll(self, direction="up"):
        if(direction=="up"):
            self.driver.execute_script("window.scrollBy(0,-1000);")
            self.log.info("scrolling page up")
        else:
            self.driver.execute_script("window.scrollBy(0,800);")
            self.log.info("scrolling page down")

    def isEnabled(self, locator, locatorType="id", info=""):
        """
        Check if element is enabled
        Parameters:
            1. Required:
                1. locator - Locator of the element to check
            2. Optional:
                1. locatorType - Type of the locator(id(default), xpath, css, className, linkText)
                2. info - Information about the element, label/name of the element
        Returns:
            boolean
        Exception:
            None
        """
        element = self.getElement(locator, locatorType=locatorType)
        enabled = False
        try:
            attributeValue = self.getElementAttributeValue(element=element, attribute="disabled")
            if attributeValue is not None:
                enabled = element.is_enabled()
            else:
                value = self.getElementAttributeValue(element=element, attribute="class")
                self.log.info("Attribute value From Application Web UI --> :: " + value)
                enabled = not ("disabled" in value)
            if enabled:
                self.log.info("Element :: '" + info + "' is enabled")
            else:
                self.log.info("Element :: '" + info + "' is not enabled")
        except:
            self.log.error("Element :: '" + info + "' state could not be found")
        return enabled

    def getElementAttributeValue(self, attribute,locator="", locatorType="id",element=None):
        """
        Get value of the attribute of element

        Parameters:
            1. Required:
                1. attribute - attribute whose value to find

            2. Optional:
                1. element   - Element whose attribute need to find
                2. locator   - Locator of the element
                3. locatorType - Locator Type to find the element
        Returns:
            Value of the attribute
        Exception:
            None
        """
        if locator:
            element = self.getElement(locator=locator, locatorType=locatorType)
        value = element.get_attribute(attribute)
        return value

    def switchToFrame(self, id="", name="", index=None, element=None):
        """
        Switch to iframe using element locator inside iframe

        Parameters:
            1. Required:
                None
            2. Optional:
                1. id    - id of the iframe
                2. name  - name of the iframe
                3. index - index of the iframe
        Returns:
            None
        Exception:
            None
        """
        try:
            if id:
                self.driver.switch_to.frame(id)
            elif name:
                self.driver.switch_to.frame(name)
            elif index:
                self.driver.switch_to.frame(index)
            else:
                self.driver.switch_to.frame(element)

        except:
            self.log.error("no such frame with given details")

    def switchToDefaultContent(self):
        """
        Switch to default content

        Parameters:
            None
        Returns:
            None
        Exception:
            None
        """
        self.driver.switch_to.default_content()

    def wait_for_page_to_load(self):
        WebDriverWait(self.driver, 120).until(
            lambda driver: driver.execute_script('return document.readyState') == 'complete')

    def wait_for_given_url(self,url):
        WebDriverWait(self.driver, 20).until(lambda driver:url in driver.current_url)