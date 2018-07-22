#coding=utf-8
import requests
import json
from api.lei import DemoLei
from api.DataLei import *
import unittest
if __name__ == '__main__':
    # a = 'https://www.sojson.com/open/api/weather/json.shtml'
    # b = {'city': '北京'}
    # http = DemoLei()
    # print http.watcher1(url=a,pa=b)

    # get方法
    # url = 'http://v.juhe.cn/calendar/day'
    # date = {'date': '2015-1-1', 'key': '3fc2053b46fcafdaacd98165f31706d4'}
    # data2 = json.dumps(date)
    # headers = {'content-type': 'application/json'}
    # http = DemoLei()
    # print http.watcher(url,data2,headers)

    # 替换一个
    # url = 'http://47.92.88.246:8999/it-license/it/license/create'
    # f = open('json.json')
    # data1 = json.load(f)
    # data2 = json.dumps(data1)
    # # newData = data2.replace('ID','88')
    # headers = {'content-type': 'application/json'}
    # http = DemoLei()
    # res=http.watcher(url,data2,headers)
    # # res = http.watcher(url, newData, headers)
    # # print(res)
    # print res['result']

    #替换多个
    # # url = 'http://47.92.88.246:8999/it-license/it/license/create'
    # f = open('json.json')
    # data1 = json.load(f)
    # # data2 = json.dumps(data1)
    # change = {}
    # change['ID'] = '77'
    # change['AppId'] = '78'
    # change['UserId'] = '79'
    # # headers = {'content-type': 'application/json'}
    # http = DemoLei()
    # res=http.dicReplace(data1,change)
    # # res = http.watcher(url, newData, headers)
    # print(res)
    # # print res['result']

    # 新增
    http1 = DataLeiF()
    res=http1.OpenF('78','79','80')
    print res['result']

    # 断言 判断结果是否一致
    self.assertEqual(res['result'], "aaa")

    # 删除


    res = http1.DleF('78','79','80',res['result'])
    print res


