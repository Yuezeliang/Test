__author__ = '76561'
import logging
import time
import os
from config import path
class log:
    def __init__(self,name):
        self.name=name
    def login(self,jb,msg):
        logger=logging.getLogger(self.name)#创建收集器给日志命名
        logger.setLevel('DEBUG')#收集包含debug级别在内的日志
        #格式
        formatter=logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')
        #日志输出器
        ch=logging.StreamHandler()#日志输出器
        ch.setLevel('INFO')#输出包括info在内及以上级别的日志
        ch.setFormatter(formatter)
        log_path=os.path.join(path.test_log,'test'+time.strftime('%Y-%m-%d'))
        fh=logging.FileHandler(log_path,encoding='UTF-8')
        fh.setLevel('INFO')
        fh.setFormatter(formatter)
        #对接
        logger.addHandler(ch)
        logger.addHandler(fh)
        if jb==1:
            logger.debug(msg)
        elif jb==2:
            logger.info(msg)
        elif jb==3:
            logger.warning(msg)
        elif jb==4:
            logger.error(msg)
        elif jb==5:
            logger.critical(msg)

        #处理重复的日志
        logger.removeHandler(ch)
        logger.removeHandler(fh)
    def debug(self,msg):
        self.login(1,msg)
    def info(self,msg):
        self.login(2,msg)
    def warning(self,msg):
        self.login(3,msg)
    def error(self,msg):
        self.login(4,msg)
    def critical(self,msg):
        self.login(5,msg)