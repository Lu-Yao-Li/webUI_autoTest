from testsuite.base_testcase import BaseTestCase
from pageobjects.forum_homepage import HomePage
from pageobjects.forum_postpage import PostPage
from pageobjects.base import BasePage
import unittest
import time
class FomerSearch(BaseTestCase,BasePage):
    def test_fomur_search(self):
        home_page=HomePage(self.driver)
        home_page.submit('admin','13333486358LY')
        time.sleep(3)

        base = BasePage(self)
        post_page=PostPage(self.driver)
        text = base.get_text(*post_page.post_page_button_mrbk_loc)
        self.assertEqual(text, "默认版块", msg="failed")
        time.sleep(3)
        post_page.mrbk()
        post_page.posting("天气","今天天气很好，适合出游")
        time.sleep(5)
        post_page.reply("玩的开心")

        time.sleep(3)
        home_page.exit()
        time.sleep(5)
if __name__=='__main__':
    unittest.main()