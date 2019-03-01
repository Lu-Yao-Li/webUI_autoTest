from pageobjects.forum_deletepage import DeletePage
from pageobjects.forum_homepage import HomePage
from testsuite.base_testcase import BaseTestCase
import time
import unittest
class DeleteTest(BaseTestCase):
    def test_delete(self):
        home_page = HomePage(self.driver)
        home_page.submit('admin', '13333486358LY')
        time.sleep(3)

        delete_page=DeletePage(self.driver)
        delete_page.mrbk()
        delete_page.delete()
        time.sleep(3)
        delete_page.management("13333486358LY")
        delete_page.ordinary("123123","123123")
        time.sleep(3)
        # delete_page.new("sssss", "ssssssss", "wwwww")
        delete_page.new("熬夜","熬夜对身体不好，不要熬夜","好的")
if __name__=='__main__':
    unittest.main()