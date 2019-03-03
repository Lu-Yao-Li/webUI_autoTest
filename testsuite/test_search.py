from testsuite.base_testcase import BaseTestCase
from pageobjects.forum_homepage import HomePage
from pageobjects.forum_searchpage import SearchPage
from pageobjects.base import BasePage
import unittest
import time
class SearchTest(BaseTestCase,BasePage):
    def test_search(self):
        home_page=HomePage(self.driver)
        home_page.submit('admin', '13333486358LY')
        time.sleep(3)
        search_page=SearchPage(self.driver)
        search_page.search("la")

        base=BasePage(self)
        text=base.get_text(*search_page.search_page_button_search_title_loc)
        self.assertEqual(text,"la",msg="failed")
        search_page.logout()
        time.sleep(4)

if __name__=="__main__":
    unittest.main()