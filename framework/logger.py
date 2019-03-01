import logging
import os
import time
class Logger():
    def __init__(self,logger):
        self.logger=logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        rq=time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        log_path=os.path.dirname(os.path.abspath('.'))+'/logs/'#存放路径
        log_name=log_path+rq+'.log'#文件名字
        fh=logging.FileHandler(log_name)#档案处理程序
        fh.setLevel(logging.INFO)

        #创建一个handler，用于输出到控制台
        ch=logging.StreamHandler()#流处理器
        ch.setLevel(logging.INFO)

        #定义handler的输出格式
        #asctime将时间日期以字符串格式表示   levelname日志的级别   message消息
        formatter=logging.Formatter('%(asctime)s - %(name)s- %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        #给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
    def getlog(self):
        return  self.logger