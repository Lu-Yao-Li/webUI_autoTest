from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time
class PostPage(BasePage):
    # �������Ĭ�ϰ��
    post_page_button_mrbk_loc = (By.CSS_SELECTOR, ".fl_tb h2 a")
    # ����
    post_page_input_mrbk_subject_loc = (By.NAME, "subject")  # ����
    post_page_input_mrbk_message_loc = (By.NAME, "message")  # ��Ϣ����
    post_page_button_mrbk_posting_loc = (By.CSS_SELECTOR, "p>button")  # ����
    # ����
    post_page_input_mrbk_reply_loc = (By.NAME, "message")  # �ظ���
    post_page_button_mrbk_reply_loc = (By.CSS_SELECTOR, "p>button")  # ����ظ�
    def mrbk(self):#Ĭ�ϰ��
        self.click(*self.post_page_button_mrbk_loc)
    def posting(self,subject,message):#����
        self.sendkeys(subject,*self.post_page_input_mrbk_subject_loc)
        self.sendkeys(message,*self.post_page_input_mrbk_message_loc)
        time.sleep(3)
        self.click(*self.post_page_button_mrbk_posting_loc)
    def reply(self,reply):#����
        self.sendkeys(reply,*self.post_page_input_mrbk_reply_loc)
        self.click(*self.post_page_button_mrbk_reply_loc)