__author__ = '76561'
import requests
from public_src.read import Readlines,ReadConfig
COOKIES=None
class HttpRequest:
    def Request(self,url,param,method):
        global COOKIES
        if method.upper()=='GET':
            try:
                res=requests.get(url,param,cookies=COOKIES)
            except Exception as e:
                print('get错误为{0}'.format(e))
        elif method.upper()=='POST':
            try:
                res=requests.post(url,param,cookies=COOKIES)
            except Exception as e:
                print("post请求错误为{0}".format(e))
        if res.cookies!={}:
            COOKIES=res.cookies

        return res.json()
if __name__ == '__main__':
    re=Readlines('TestCase.xlsx','register','init_date').read('confg','FLAG','mode','case_id')
    ip=ReadConfig().Config('confg','IP','ip')
    for item in re:
        r=HttpRequest().Request(ip+item['url'],item['param'],item['method'])
        print(r)