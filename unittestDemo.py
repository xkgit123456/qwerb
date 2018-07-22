#coding=utf-8

import unittest
import requests
import json
from api.lei import DemoLei
from api.DataLei import *


class CreateTest(unittest.TestCase):
    def setUp(self):
        pass
    def test_add(self):
        url = 'http://47.92.88.246:8999/it-license/it/license/create'
        f = open('json.json')
        headers = {'content-type': 'application/json'}
        data1 = json.load(f)
        # 多转换了一步，分装的方法中，已经有了转换，再转换就会有问题
        #data2 = json.dumps(data1)
        change = {}
        change['ID'] = "77"
        change['AppId'] = "7"
        change['UserId'] = "79"
        http = DemoLei()
        res=http.dicReplace(data1,change)
        print(type(res))
        print(res)
        res1 = requests.post(url=url,data=res,headers=headers)
        print(res1.status_code)
        # print(res1.text)
        print(res1.json()['result'])
    def test_dowm(self):
        pass


        # 断言 判断结果是否一致
        # self.assertEqual(res['result'],"aaa")


