import pdb
import time

from base.basepage import BasePage
import json

class WeatherReportPageMap(BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    def city_list(self):
        self.waitForElement("messages")
        return self.getElementList("//div[@id='messages']/div/label/input[@id]","xpath")

class WeatherReportPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
        self.map=WeatherReportPageMap(driver)

    def get_temp_for_given_city(self,city):
        #ele = self.driver.find_elements(By.XPATH, "//div[@id='messages']/div/label/input[@id]")
        #city_ele=[e1 for e1 in self.map.city_list() if (e1.get_attribute("id").__contains__(city)) if not e1.get_attribute("checked")]
        #city_ele.click
        cityExist=None
        time.sleep(5)
        for e1 in self.map.city_list():
            self.waitForElement(element=e1)
            if not (e1.get_attribute("id").__contains__(city)):
                cityExist=True
        if not cityExist:
            raise Exception(f"temprature details for {city} does not exist")

        # ele = self.driver.find_elements(By.XPATH, "//div[@id='messages']/div/label/input[@id]")
        city_ele=[e1 for e1 in self.map.city_list() if (e1.get_attribute("id").__contains__(city)) ]
        city_ele=city_ele.pop()
        if not city_ele.get_attribute("checked"):
            city_ele.click()
        city_details=city_ele.get_attribute("onclick")
        city_details=city_details.lstrip("javascript:dropCityMarker(this, ")
        city_details=city_details.replace(')','')
        city_dict=json.loads(json.loads(city_details))
        city_temperature=float(city_dict['temp_c'])
        return city_temperature






