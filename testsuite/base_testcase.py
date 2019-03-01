from framework.browser_engine import BrowserEngine
import unittest
browser=BrowserEngine()
class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.driver=browser.open_browser()
    def tearDown(self):
        self.driver=browser.quit_browser()