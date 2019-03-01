from testsuite.base_testcase import BaseTestCase
from pageobjects.forum_homepage import HomePage
from pageobjects.forum_postpage import PostPage
from pageobjects.forum_votepage import VotePage
import time
import unittest
class VoteTest(BaseTestCase):
    def test_vote(self):
        home_page = HomePage(self.driver)
        home_page.submit('admin', '13333486358LY')
        time.sleep(3)
        post_page = PostPage(self.driver)
        post_page.mrbk()#默认版块

        vote_page=VotePage(self.driver)
        vote_page.post("Do you like apple","Yes","No")
        time.sleep(10)
        vote_page.vote()
        vote_page.result()
        time.sleep(10)

if __name__=="__main__":
    unittest.main()