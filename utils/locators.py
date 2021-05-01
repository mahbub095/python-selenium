from selenium.webdriver.common.by import By


# for maintainability we can seperate web objects by page name
class MainPageLocators(object):
    LOGO = (By.CSS_SELECTOR,
            'body.on-home-landing:nth-child(2) div.app-footer.container:nth-child(4) div.footer-final.row > div.col-8.copyright')
    ACCOUNT = (By.ID, 'nav-link-accountList')
    SIGNUP = (By.CSS_SELECTOR, '#nav-signin-tooltip > div > a')
    LOGIN = (By.CSS_SELECTOR, '#nav-signin-tooltip > a')
    SEARCH = (By.ID, 'twotabsearchtextbox')
    SEARCH_LIST = (By.CSS_SELECTOR, 'div[data-component-type="s-search-result"]')
    TESTLINKHome = (By.LINK_TEXT, 'Sell Fast')


class LinkPageLocators(object):
    TESTLINK = (By.LINK_TEXT, 'Sell Fast')
    TESTLINK2 = (By.LINK_TEXT, 'Doorstep Delivery')
    TESTLINK3 = (By.LINK_TEXT, 'Banner Ads')
    TESTLINK4 = (By.LINK_TEXT, 'Promotions')
    LINK = (By.LINK_TEXT, 'FAQ')
    LINK2 = (By.LINK_TEXT, 'Stay safe')
    LINK3 = (By.LINK_TEXT, 'Contact Us')
