from base.basepage import BasePage
from selenium.webdriver.support.color import Color
import utils.custom_logger as cl

class TypeArrangementSb(BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
    ################
    ### Locators ###
    ################
    _page_url="type-arrangement/single-bearing"
    _select_bearing_type=("//span[contains(text(),'Select bearing type')]","xpath")
    _bearing_types=("//span[@title]","xpath")
    _bearing_icon=('bearing-icon',"class")
    _search_designation_search_box=("//input[contains(@class,'search-input')]","xpath")
    _next_button=("//button[text()='next'][@class='button-default']","xpath")

    def wait_for_type_arrangement_sb_page_to_load(self):
        self.wait_for_given_url(self._page_url)
        self.wait_for_page_to_load()

    def click_on_select_bering_type(self):
        self.elementClick(*self._select_bearing_type)

    def get_baring_types(self):
        self.waitForElement(locator="//mat-select[@aria-expanded='true']",locatorType="xpath")
        bearing_ele_list=self.getElementList(*self._bearing_types)
        bearing_list=[]
        for ele in bearing_ele_list:
            bearing_list.append(ele.text)
        cl.allurelogs(f"list of bearing displayed{bearing_list}")
        return bearing_list

    def click_on_bearing_icon(self):
        self.elementClick(*self._bearing_icon)

    def select_given_bearing_type(self,bearing_type):
        ele=self.getElement(locator=f"//mat-option/span/span[text()='{bearing_type}']",locatorType="xpath")
        self.elementClick(element=ele)
        cl.allurelogs(f"selected {bearing_type} from list")

    def wait_for_mat_table_to_load(self):
        self.waitForElement(locator="//mat-table/mat-row[1]",locatorType="xpath")

    def enter_designation_in_search(self,designation):
        self.sendKeys(designation,*self._search_designation_search_box)
        cl.allurelogs(f"entered {designation} in search box")

    def wait_for_given_details_in_mat_table_and_click(self,designation):
        first_row=f"//mat-table/mat-row/mat-cell[@title='{designation}']"
        self.waitForElement(locator=first_row,locatorType="xpath")
        self.elementClick(locator=first_row,locatorType="xpath")
        cl.allurelogs("clicked on first row")

    def wait_for_next_button_enabling(self):
        self.waitForElement(*self._next_button)
        cl.allurelogs("next button is enabled")

    def get_color_of_next_button(self):
        color_code= self.getElementColorCode(*self._next_button)
        color_code_hex=Color.from_string(color_code).hex
        cl.allurelogs(f"the color code received is {color_code_hex}")
        return color_code_hex



