from locators import MainPageLocators


class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    #Declares a variable that will contain the retrieved text

    def is_title_matches(self):

        return "The Daily Star" in self.driver.title
    
    def click_epaper_button(self):
        """Triggers the search"""

        element = self.driver.find_element(*MainPageLocators.EPaper_BUTTON)
        element.click()
class EpaperPage(BasePage):

    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "No results found." not in self.driver.page_source





