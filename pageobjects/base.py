from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.logger import Logger
import os.path
import time

logger=Logger(logger="BasePage").getlog()
class BasePage(object):
    # search_page_button_search_title_loc = (By.CSS_SELECTOR, ".xs3 strong font")  # 标题
    #初始化方法
    def __init__(self,driver):
        self.driver=driver
    def back(self):#后退
        self.driver.back()
        logger.info("单击当前页面上的后退")
    def forward(self):#前进
        self.driver.forward()
        logger.info("单击当前页面上的前进")
    def open_url(self,url):#网址
        try:
            self.driver.get(url)
        except Exception as e:
            print("找不到网址")
    def quit_browser(self):#关闭所有
        self.driver.quit()
    def close(self):#关闭当前
        try:
            self.driver.close()
            logger.info("关闭并退出浏览器")
        except Exception as e:
            logger.error("退出浏览器失败 %s"%e)
    def find_element(self,*loc):#元素定位
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
            # logger.info("找不到页面元素 -->%s"%loc)
        except Exception as e:
            print("%s 页面中未能找到 %s 元素"%(self,loc))
    def sendkeys(self,text,*loc):#发送请求
        el=self.find_element(*loc)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("输入内容%s"%text)
        except Exception as e:
            print("发送内容失败")
            logger.info("发送时输入框失败"%e)
            # self.get_windows_img()
    def clear(self,*loc):#清除
        el=self.find_element(*loc)
        try:
            el.clear()
            logger.info("Clear test is input box befor typing.")
        except Exception as e:
            logger.error("Failed to clear is input box with %s"%e)
    def click(self,*loc):#点击
        el=self.find_element(*loc)
        try:
            el.click()
            logger.info("click")
        except Exception as e:
            logger.error("Failed to click the element with %s"%e)
    def jihuo(self,page):
        self.driver.switch_to.window(self.driver.window_handles[page])
        logger.info("激活第%s个窗口"%page)
    def get_text(self,*loc):
        el = self.find_element(*loc)
        try:
            return el.text
        except Exception as e:
            logger.error("Failed to clear is input box with %s" % e)
    def get_window_img(self):
        file_path=os.path.dirname(os.path.abspath("."))+'/img/'
        if not os.path.exists(file_path):
            os.mkdir(file_path)
            rq=time.strftime("%Y%m%d%H%M",time.localtime(time.time()))
            screen_name=file_path+rq+'.png'
            try:
                self.driver.get_screenshot_as_file(screen_name)
                logger.info("有截图且保存路径是/img/")
            except Exception as e:
                logger.error("%s截屏失败"%e)