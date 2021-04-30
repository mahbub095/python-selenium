import unittest

from pages.link_page import LinkPage
from tests.base_test import BaseTest

from utils.test_cases import test_cases


# I am using python unittest for asserting cases.
# In this module, there should be test cases.
# If you want to run it, you should type: python <module-name.py>

class TestSignInPage(BaseTest):

    def test_link_in_button(self):
        print("\n" + str(test_cases(3)))
        page = LinkPage(self.driver)
        page.click_link_button()
