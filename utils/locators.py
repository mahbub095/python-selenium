from selenium.webdriver.common.by import By


# for maintainability we can seperate web objects by page name

class LinkPageLocators(object):
    TESTLINK = (By.LINK_TEXT, 'Sell Fast')
    TESTLINK2 = (By.LINK_TEXT, 'Doorstep Delivery')
    TESTLINK3 = (By.LINK_TEXT, 'Banner Ads')
    TESTLINK4 = (By.LINK_TEXT, 'Promotions')
    LINK = (By.LINK_TEXT, 'FAQ')
    LINK2 = (By.LINK_TEXT, 'Stay safe')
    LINK3 = (By.LINK_TEXT, 'Contact Us')
