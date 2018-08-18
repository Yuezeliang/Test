__author__ = '76561'
import unittest
from public_src.HttpRequest import HttpRequest
from ddt import ddt,data,unpack
from public_src.read import ReadConfig,Readlines
from public_src.log import log
from config import path
from public_src.do_mysql import DoMysql
logger=log('测试日志')
ip=ReadConfig().Config(path.confg_path,'IP','ip')
res=Readlines(path.test_date,'register','init_date').read(path.confg_path,'FLAG','mode','case_id')
mySql=ReadConfig().Config(path.confg_path,'CONFIG','config')
REGTIME=None
REGNAME=None
MEMBERID=None
@ddt
class TestHttpRequest(unittest.TestCase):
    def setUp(self):
        print('开始测试了')
        self.t=Readlines(path.test_date,'register','init_date')
    @data(*res)
    def test_HttpRequest(self,res):
        global REGTIME
        global REGNAME
        global MEMBERID
        re=HttpRequest().Request(ip+res['url'],res['param'],res['method'])

        self.t.Write_test_results(res['CaseID']+1,8,str(re))

        if REGTIME==None:
            reslut=(DoMysql(eval(mySql)).Do_mysql('select RegTime from member where mobilephone=%s',res['param']['mobilephone'],1))[0]
            if reslut!=None:
                REGTIME=str(reslut)+'.0'
        if REGNAME==None:
            regname=(DoMysql(eval(mySql)).Do_mysql('select RegName from member where mobilephone=%s',res['param']['mobilephone'],1))[0]
            if regname!=None:
                REGNAME=regname
        if MEMBERID==None:
            memberid=(DoMysql(eval(mySql)).Do_mysql('select id from member where mobilephone=%s',res['param']['mobilephone'],1))[0]
            if memberid!=None:
                MEMBERID=memberid

        if res['code'].find('${regtime}')!=-1:
            param=res['code'].replace('${regtime}',REGTIME)
            if param.find('${regname}')!=-1:
                param=param.replace('${regname}',REGNAME)

                if param.find('${member_id}')!=-1:
                    param=param.replace('${member_id}',str(MEMBERID))
                    if param.find('${no_reg_tel}')!=-1:
                        param=param.replace('${no_reg_tel}',res['param']['mobilephone'])
        else:
            param=res['code']

        if res['CheckSql']!=None:
            capital=DoMysql(eval(mySql)).Do_mysql(eval(res['CheckSql'])['query'],res['param']['mobilephone'],eval(res['CheckSql'])['state'])
            try:
                self.assertEqual(eval(res['CheckSql'])['expecte'],int(capital[0]))
                SqlTesting='p'
            except AssertionError as e:
                logger.error('数据库对比错误为{0}'.format(e))
                SqlTesting='f'
                raise e
            finally:
                self.t.Write_test_results(res['CaseID']+1,10,SqlTesting)

        try:
            self.assertEqual(eval(param),re)
            r='p'
        except AssertionError as e:
            logger.error('错误为{0}'.format(e))
            r='f'
            raise e
        finally:
            self.t.Write_test_results(res['CaseID']+1,9,r)
        logger.error(re)


        return re

    def tearDown(self):
        logger.info('测试结束')