from utils.locators import *
from pages.base_page import BasePage
from utils import users


class LinkPage(BasePage):
    def __init__(self, driver):
        self.locator = LinkPageLocators
        super(LinkPage, self).__init__(driver)

    def click_link_button(self):
        self.find_element(*self.locator.TESTLINK).click()
        self.find_element(*self.locator.TESTLINK2).click()
        self.find_element(*self.locator.TESTLINK3).click()
        self.find_element(*self.locator.TESTLINK4).click()
        self.find_element(*self.locator.LINK).click()
        self.find_element(*self.locator.LINK2).click()

    def login(self):
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        self.click_link_button()
