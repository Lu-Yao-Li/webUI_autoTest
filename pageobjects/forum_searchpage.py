from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time
class SearchPage(BasePage):
    search_page_input_search_loc=(By.CSS_SELECTOR,".scbar_txt_td input")#������
    search_page_button_search_loc=(By.CSS_SELECTOR,".scbar_btn_td button")#������ť
    search_page_button_search_title_loc=(By.CSS_SELECTOR,".xs3 strong font")#����
    search_page_button_search_exit_loc=(By.CSS_SELECTOR,".y a:nth-child(5)")#�˳�

    def search(self,search):
        self.sendkeys(search,*self.search_page_input_search_loc)
        self.click(*self.search_page_button_search_loc)
        self.jihuo(1)
        time.sleep(4)
        self.click(*self.search_page_button_search_title_loc)

    def logout(self):
        self.click(*self.search_page_button_search_exit_loc)