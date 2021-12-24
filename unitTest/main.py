import unittest
from selenium import webdriver
import page

class DailyStar(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.thedailystar.net/")

    def test_search_in_daily_star(self):
        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches(), "dailystar.net title doesn't match."

        main_page.click_epaper_button()
        paper_page = page.EpaperPage(self.driver)
        #Verifies that the results page is not empty
        assert paper_page.is_results_found(), "No results found."


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()