import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import page


class GitSearchTester(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://www.github.com")

    def test_search_in_python_org(self):
        # Load the main page. In this case the home page of GitHub.com.
        main_page = page.MainPage(self.driver)
        keyword = "webform"
        username = "backdrop-contrib"
        # Checks if the word "Python" is in title
        assert main_page.is_title_matches(), "Title doesn't match."
        # Sets the text of search textbox to "pycon"
        main_page.search_text_element = keyword
        main_page.go_search()
        search_results_page = page.SearchResultsPage(self.driver)
        # Verifies that the results page is not empty
        assert search_results_page.is_results_found(), "No results found."
        links = search_results_page.find_link(keyword)
        search_results_page.click_link(links, keyword)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
