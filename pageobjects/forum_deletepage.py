from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time
class DeletePage(BasePage):
    # 点击进入默认版块
    delete_page_button_mrbk_loc = (By.CSS_SELECTOR, ".fl_tb h2 a")
    #删除帖子
    delete_page_checkbox_mrbk_box_loc=(By.NAME,"moderate[]")#勾选框
    delete_page_button_mrbk_delete_loc=(By.LINK_TEXT,"删除")#删除
    delete_page_button_mrbk_determine_loc=(By.NAME,"modsubmit")#确定
    delete_page_button_management_loc=(By.XPATH,"//p/a[6]")#管理中心

    delete_page_input_management_pwd_loc=(By.NAME,"admin_password")#密码
    delete_page_button_management_submit_loc=(By.CSS_SELECTOR,".loginnofloat>input")#提交
    delete_page_button_forum_loc=(By.XPATH,"//ul/li[7]")#点击论坛

    delete_page_button_forum_creat_loc=(By.CSS_SELECTOR,".lastboard .addtr")#创建新版块
    delete_page_button_forum_submit_loc=(By.NAME,"editsubmit")#提交
    delete_page_button_forum_exit_loc=(By.CSS_SELECTOR,".uinfo p a:nth-child(2)")#退出
    delete_page_button_admin_exit_loc=(By.CSS_SELECTOR,".hdc p a:nth-child(18)")#退出管理员

    delete_page_input_ordinary_username_loc = (By.CSS_SELECTOR, ".y input:nth-child(1)")#用户名
    delete_page_input_ordinary_pwd_loc = (By.CSS_SELECTOR, ".pns table tr:nth-child(2) input")#密码
    delete_page_button_ordinary_loc = (By.CSS_SELECTOR, ".fastlg_l>button")#登录按钮

    delete_page_button_ordinary_new_loc=(By.CSS_SELECTOR,".fl_row td:nth-child(2) h2 a")#新版块
    delete_page_input_new_subject_loc=(By.CSS_SELECTOR,".pbt input")#标题
    delete_page_input_new_message_loc=(By.CSS_SELECTOR,".area textarea")#内容
    delete_page_button_new_send_loc=(By.CSS_SELECTOR,".ptm button")#发帖
    delete_page_input_new_reply_loc=(By.CSS_SELECTOR,".area textarea")#回复框
    delete_page_button_new_reply_loc =(By.CSS_SELECTOR,".ptm button")#回复按钮

    def mrbk(self):# 点击进入默认版块
        self.click(*self.delete_page_button_mrbk_loc)
    def delete(self):#删除
        self.click(*self.delete_page_checkbox_mrbk_box_loc)#勾选框
        self.click(*self.delete_page_button_mrbk_delete_loc)#删除
        self.click(*self.delete_page_button_mrbk_determine_loc)#确定
        self.click(*self.delete_page_button_management_loc)  # 管理中心
    def management(self,pwd):
        self.jihuo(1)
        self.sendkeys(pwd,*self.delete_page_input_management_pwd_loc)#密码
        self.click(*self.delete_page_button_management_submit_loc)#提交
        self.click(*self.delete_page_button_forum_loc)#点击论坛
        time.sleep(2)
        self.driver.switch_to.frame(0)
        self.click(*self.delete_page_button_forum_creat_loc)#创建新版块
        time.sleep(2)
        self.click(*self.delete_page_button_forum_submit_loc)#提交
        time.sleep(3)
        self.jihuo(1)
        self.click(*self.delete_page_button_forum_exit_loc)#退出
        self.click(*self.delete_page_button_admin_exit_loc)#退出管理员
    def ordinary(self,username,pwd):
        self.sendkeys(username,*self.delete_page_input_ordinary_username_loc)#用户名
        self.sendkeys(pwd,*self.delete_page_input_ordinary_pwd_loc)#密码
        time.sleep(5)
        self.click(*self.delete_page_button_ordinary_loc)#登录按钮
    def new(self,subject,message,reply):
        self.click(*self.delete_page_button_ordinary_new_loc)
        self.sendkeys(subject,*self.delete_page_input_new_subject_loc)
        self.sendkeys(message, *self.delete_page_input_new_message_loc)
        self.click(*self.delete_page_button_new_send_loc)
        time.sleep(3)
        self.sendkeys(reply, *self.delete_page_input_new_reply_loc)
        self.click(*self.delete_page_button_new_reply_loc)

