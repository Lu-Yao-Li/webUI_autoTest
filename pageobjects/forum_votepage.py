from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
from framework.logger import Logger
import time
logger=Logger(logger="VotePage").getlog()
class VotePage(BasePage):
    vote_page_button_post_loc = (By.CSS_SELECTOR, ".bm:nth-child(3) a img")#点击发帖
    vote_page_button_vote_post_loc = (By.CSS_SELECTOR, ".ct2_a ul li:nth-child(2) a")#点击发起投票
    vote_page_input_vote_post_subject_loc =(By.CSS_SELECTOR,".z span:nth-child(1) input")#标题
    vote_page_input_vote_post_one_loc = (By.CSS_SELECTOR, ".mbm p:nth-child(1) input")#选项1
    vote_page_input_vote_post_two_loc = (By.CSS_SELECTOR, ".mbm p:nth-child(2) input")#选项2
    vote_page_button_vote_post_send_loc=(By.XPATH,'//*[@id="postsubmit"]/span')#发起投票

    vote_page_button_vote_choose_loc = (By.CSS_SELECTOR,".pslt:nth-child(1) input")  # 选择
    vote_page_button_vote_choose_submit_loc = (By.CSS_SELECTOR, ".pn span")#提交

    vote_page_vote_choose1_name_loc = (By.CSS_SELECTOR,".pcht tr:nth-child(1) label")#选项1名称
    vote_page_vote_choose2_name_loc = (By.CSS_SELECTOR,".pcht tr:nth-child(3) label")#选项2名称
    vote_page_vote_choose1_percentage_loc = (By.CSS_SELECTOR,".pcht tr:nth-child(2) td:nth-child(2) em")#选项1投票数
    vote_page_vote_choose2_percentage_loc = (By.CSS_SELECTOR,".pcht tr:nth-child(4) td:nth-child(2) em")#选项2投树
    vote_page_vote_name_loc=(By.CSS_SELECTOR,".ts span")#投票主题名称

    def post(self,subject,one,two):
        self.click(*self.vote_page_button_post_loc)#点击发帖
        self.click(*self.vote_page_button_vote_post_loc)# 点击发起投票
        self.sendkeys(subject,*self.vote_page_input_vote_post_subject_loc)#标题
        self.sendkeys(one, *self.vote_page_input_vote_post_one_loc)#选项1
        self.sendkeys(two, *self.vote_page_input_vote_post_two_loc)#选项2
        self.click(*self.vote_page_button_vote_post_send_loc)#发起投票

    def vote(self):
        self.click(*self.vote_page_button_vote_choose_loc)
        self.click(*self.vote_page_button_vote_choose_submit_loc)

    def result(self):
        name1=self.get_text(*self.vote_page_vote_choose1_name_loc)
        name2=self.get_text(*self.vote_page_vote_choose2_name_loc)
        choose1=self.get_text(*self.vote_page_vote_choose1_percentage_loc)
        choose2=self.get_text(*self.vote_page_vote_choose2_percentage_loc)
        name=self.get_text(*self.vote_page_vote_name_loc)
        logger.info("%s:%s=%s:%s"%name1%name2%choose1%choose2)
        logger.info("第一个选项的名称是：%s"%name1)
        logger.info("投票比例是：%s"%choose1)
        logger.info("第二个选项的名称是：%s"%name2)
        logger.info("投票比例是：%s"%choose2)
        logger.info("投票的主题名称为：%s"%name)


