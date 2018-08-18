__author__ = '76561'
import mysql.connector
from public_src.read import ReadConfig
from config import path
#登陆
class DoMysql:
    def __init__(self,config):
        self.config=config
    def Do_mysql(self,select,condition,state):
        cnn=mysql.connector.Connect(**self.config)
        cursor=cnn.cursor()
        cursor.execute(select,(condition,))
        if state==1:
            result=cursor.fetchone()
        else:
            result=cursor.fetchall()
        cursor.close()
        cnn.close()
        return result
if __name__ == '__main__':

    config=ReadConfig().Config(path.confg_path,'CONFIG','config')
    query='select id from member where id=%s'
    query_condition=23502
    re=DoMysql(eval(config)).Do_mysql(query,query_condition,1)
    print(re[0])