#coding=utf-8

import unittest
import requests
import json
import HTMLTestRunner
import unittestDemo
from api.lei import DemoLei
from api.DataLei import *
from unittestDemo import *



if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittestDemo.CreateTest("test_add"))
    # wb读写
    file = open("../report/testReport.html",'wb')
    runner = HTMLTestRunner.HTMLTestRunner(file,title=u"接口测试",description=u"测试报告")
    runner.run(suite)