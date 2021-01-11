import pdb

from base.basepage import BasePage
from selenium.webdriver.support.color import Color
import utils.custom_logger as cl
from selenium.webdriver.common.action_chains import ActionChains

class FlipkartHomePage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    _electronics_tab=("//span[contains(text(),'Electronics')]","xpath")
    _power_bank=("//span[contains(text(),'Electronics')]/following-sibling::div//a[@title='Power Banks']","xpath")
    _login_close_button=("//div[@tabindex='-1']/div/button","xpath")
    _search_text_box=("//input[@name='q']","xpath")
    _submit_button=("//button","xpath")

    def click_on_x_login_popup(self):
        self.waitForElement(*self._login_close_button)
        self.elementClick(*self._login_close_button)

    def enter_search_item(self,search_item):
        self.sendKeys(search_item,*self._search_text_box)

    def click_submit(self):
        self.elementClick(*self._submit_button)

    def wait_for_title(self,title_name):
        self.waitForElement(locator=f"//title[text()='{title_name}'",locatorType="xpath")

    def select_item_in_range(self,min_price,max_price):
        ele_list=self.getElementList("//div[@class='_30jeq3 _1_WHN1']","xpath")
        for ele in ele_list:
            ele_price=int(ele.text.replace("₹","").replace(",",""))
            if (ele_price >min_price and ele_price< max_price):
                ele.click()
                break

    def click_power_bank_in_electronics_tab(self):
        try:
            electronics_tab=self.getElement(*self._electronics_tab)
            power_bank_ele=self.getElement(*self._power_bank)
            self.elementClick(element=electronics_tab)
            self.waitForElement(element=power_bank_ele)
            self.elementClick(element=power_bank_ele)

        except Exception as ex:
            print(f"could not mouse over bcoz of {ex}")



