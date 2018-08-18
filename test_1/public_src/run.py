__author__ = '76561'
import unittest
import os
from HTMLTestRunnerNew import HTMLTestRunner
from public_src.Test_HttpRequest import TestHttpRequest
from config import path
import time
sui=unittest.TestSuite()
load=unittest.TestLoader()
sui.addTest(load.loadTestsFromTestCase(TestHttpRequest))
test=os.path.join(path.test_report,time.strftime('%Y-%m-%d')+'.html')
with open(test,'wb+') as file:
    run=HTMLTestRunner(stream=file, title=None,description=None,tester=None)
    run.run(sui)