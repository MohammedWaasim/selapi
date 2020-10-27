import logging
import pdb
import unittest

import utils.custom_logger as cl
import pytest

from pages.ndtv_pages.ndtv_home_page import NdtvHomePageMap, NdtvHomePage
from pages.ndtv_pages.weather_report_page import WeatherReportPage
from pages.ndtv_pages.world_news_page import WorldNewsPage
from utils.api_helper import ApiHelper
from utils.read_data import getYamlData
from utils.tempareture_comparetor import TempretureComparetor
from utils.weather import Weather


@pytest.mark.usefixtures("oneTimeNdtvSetup")
class NdtvWeather(unittest.TestCase):
    log = cl.customLogger(logging.INFO)
    @pytest.fixture(autouse=True)
    def classSetup(self):
        print("get object of page classes")
        self.ndtv_web_data = getYamlData(self.ndtv_test_file, 'ndtv_web')
        self.open_api_data = getYamlData(self.ndtv_test_file, 'open_api')
        self.ndtv_home_page= NdtvHomePage(self.driver)
        self.ndtv_world_page=WorldNewsPage(self.driver)
        self.weather_report_page=WeatherReportPage(self.driver)
        self.api=ApiHelper()
        self.temp_comp=TempretureComparetor(self.open_api_data['acceptableVariance'])


    @pytest.mark.run(order=1)
    def test_web_navigate_ndtv(self):
        print("write test1")
        self.driver.get(self.ndtv_web_data['url'])
        print(self.driver.title)
        assert self.ndtv_web_data['title'] == self.ndtv_home_page.getTitle()

    @pytest.mark.run(order=2)
    def test_web_validate_temp(self):
        print("write test2 here")
        print(self.driver.title)
        self.ndtv_home_page.click_world_tab()
        self.ndtv_world_page.click_section_menu()
        self.ndtv_world_page.click_weather()
        self.ndtv_city_temp=self.weather_report_page.get_temp_for_given_city(self.ndtv_web_data['city'])
        print(self.ndtv_city_temp)
        params={}
        params.__setitem__("q",self.open_api_data['city'])
        params.__setitem__("appid", self.appid)
        url=self.open_api_data['base_uri']+self.open_api_data['endpoint']
        resp=self.api.get(url,params=params)
        resp=resp.json()
        kelvin_temp=resp['main']['temp']
        self.api_temp_c=float(kelvin_temp)-self.open_api_data['kelvin_diff']
        weather_ui=Weather(self.ndtv_city_temp)
        weather_api=Weather(self.api_temp_c)
        self.temp_comp.compare_temprature(weather_ui,weather_api)
















