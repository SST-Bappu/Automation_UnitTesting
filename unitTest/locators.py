from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    EPaper_BUTTON = (By.XPATH, '//*[@id="sm-header-sticky"]/div[1]/div/div[4]/section/div/ul/li[1]/a')

class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should
    come here"""

    pass