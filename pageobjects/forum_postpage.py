from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time
class PostPage(BasePage):
    # 点击进入默认版块
    post_page_button_mrbk_loc = (By.CSS_SELECTOR, ".fl_tb h2 a")
    # 发帖
    post_page_input_mrbk_subject_loc = (By.NAME, "subject")  # 标题
    post_page_input_mrbk_message_loc = (By.NAME, "message")  # 消息内容
    post_page_button_mrbk_posting_loc = (By.CSS_SELECTOR, "p>button")  # 发帖
    # 回帖
    post_page_input_mrbk_reply_loc = (By.NAME, "message")  # 回复框
    post_page_button_mrbk_reply_loc = (By.CSS_SELECTOR, "p>button")  # 点击回复
    def mrbk(self):#默认版块
        self.click(*self.post_page_button_mrbk_loc)
    def posting(self,subject,message):#发帖
        self.sendkeys(subject,*self.post_page_input_mrbk_subject_loc)
        self.sendkeys(message,*self.post_page_input_mrbk_message_loc)
        time.sleep(3)
        self.click(*self.post_page_button_mrbk_posting_loc)
    def reply(self,reply):#回帖
        self.sendkeys(reply,*self.post_page_input_mrbk_reply_loc)
        self.click(*self.post_page_button_mrbk_reply_loc)