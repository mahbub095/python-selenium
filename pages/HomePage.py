from pages.base_page import BasePage
from utils.locators import MainPageLocators


class HomePage(BasePage):
    def __init__(self, driver):
        self.locator = MainPageLocators
        super().__init__(driver)  # Python3 version

    # self.time.sleep(3)

    # def search_item(self):
    #     self.find_element(*self.locator.LOGO)
    #     return self.find_element(*self.locator.LOGO)
    #
    def click_Home_button(self, check):
        self.find_element(*self.locator.TESTLINKHome).send_keys(check)
        self.find_element(*self.locator.TESTLINKHome).click()
