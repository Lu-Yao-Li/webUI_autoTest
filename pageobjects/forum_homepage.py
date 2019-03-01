from pageobjects.base import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    #��¼
    home_page_input_submit_username_loc=(By.ID,"ls_username")
    home_page_input_submit_pwd_loc=(By.NAME,"password")
    home_page_button_submit_loc=(By.CSS_SELECTOR,".fastlg_l>button")

    #����˳�
    home_page_button_exit_loc=(By.XPATH,"//p/a[7]")

    def submit(self,username,pwd):#��¼
        self.sendkeys(username,*self.home_page_input_submit_username_loc)
        self.sendkeys(pwd,*self.home_page_input_submit_pwd_loc)
        self.click(*self.home_page_button_submit_loc)

    def exit(self):#�˳�
        self.click(*self.home_page_button_exit_loc)