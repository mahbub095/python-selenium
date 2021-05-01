from pages.HomePage import HomePage
from tests.base_test import BaseTest
from utils.test_cases import test_cases


class TestHomePage(BaseTest):

    def test_home_item(self):
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        print("\n" + str(test_cases(1)))
        page = HomePage(self.driver)
        element = self.driver.find_element_by_xpath("//div[contains(text(),'Copyright © Saltside Technologies')]")
        assert element.text == 'Copyright © Saltside Technologies'
        print(element.text)
        elementpost = self.driver.find_element_by_xpath("//p[contains(text(),'Post your ad on Bikroy.com')]")
        assert elementpost.text == 'Post your ad on Bikroy.com'
        print(elementpost.text)
