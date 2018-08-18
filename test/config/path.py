__author__ = '76561'
import os
from public_src.read import ReadConfig
#获取配置文件的路径
confg_path=os.path.join(os.path.split(os.path.join(__file__))[0],'confg')
# print(confg_path)
#顶级目录
object_1=ReadConfig().Config(confg_path,'objectPath','path')
# print(object_1)

#测试数据的路径
test_date=os.path.join(object_1,'test_date','TestCase.xlsx')
# print(test_date)

#测试日志的路径
test_log=os.path.join(object_1,'test_results','test_log')

#测试报告的路径
test_report=os.path.join(object_1,'test_results','test_report')