#coding=utf-8
import requests
import json
import xlrd
from api.DataLei import *
from api.lei import DemoLei

class DataLeiF:

    def OpenF(self,ID,AppId,UserId):
        url = 'http://47.92.88.246:8999/it-license/it/license/create'
        change = {}
        change['ID'] = ID
        change['AppId'] = AppId
        change['UserId'] = UserId
        f = open('json.json')
        data1 = json.load(f)
        data2 = json.dumps(data1)
        headers = {'content-type': 'application/json'}
        http = DemoLei()
        res = http.watcher(url, data2, headers)
        return res

    def DleF(self,ID,AppId,UserId,resultID):
        change = {}
        change['ID'] = ID
        change['AppId'] = AppId
        change['UserId'] = UserId
        change['resultID'] = resultID
        url = 'http://47.92.88.246:8999/it-license/it/license/delete'
        f = open('del.json')
        data1 = json.load(f)
        data2 = json.dumps(data1)
        print(data2)
        headers = {'content-type': 'application/json'}
        http = DemoLei()
        res = http.watcher(url, data2, headers)
        return res


