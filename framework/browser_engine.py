import os.path
from configparser import ConfigParser
from selenium import webdriver
from framework.logger import Logger

logger=Logger(logger="BrowserEngine").getlog()

class BrowserEngine():
    dir=os.path.dirname(os.path.abspath('.'))#注意相对路径获取方法
    chrome_driver_path=dir+'/tools/chromedriver.exe'
    firefox_driver_path=dir+'/tools/geckodriver.exe'
    ie_driver_path=dir+'/tools/IEDriverServer.exe'

    def open_browser(self):
        config=ConfigParser()
        file_path=os.path.dirname(os.path.abspath('.'))+'/config/config.ini'
        config.read(file_path)

        browser=config.get("browserType","browserName")
        logger.info("你选择的是 %s 浏览器."%browser)
        url=config.get("testServer","URL")
        logger.info("这个服务器的地址是:%s"%url)

        if browser=="Firefox":
            #启动firefox实例
            self.driver=webdriver.Firefox(executable_path=self.firefox_driver_path)
            logger.info("开始火狐浏览器")
        elif browser=="Chrome":
            self.driver=webdriver.Chrome(self.chrome_driver_path)
            logger.info("开始谷歌浏览器")
        elif browser=="IE":
            self.driver=webdriver.Ie(self.ie_driver_path)
            logger.info("开始IE浏览器")

        self.driver.get(url)
        logger.info("打开网址:%s"%url)
        self.driver.maximize_window()
        logger.info("窗口最大化")
        self.driver.implicitly_wait(10)
        logger.info("隐形等待时间为10秒钟")
        # self.driver.get(url)
        return self.driver

    def quit_browser(self):
        self.driver.quit()
        logger.info("关闭浏览器")