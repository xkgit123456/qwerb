#coding=utf-8
import requests
import json

class DemoLei:

    def watcher(self,url, data,headers):
        res = requests.post(url=url, data=data,headers=headers)
        return res.json()

    def watcher1(self,url, pa):
        res = requests.get(url=url, params=pa)
        return res.text

    def dicReplace(self,data,change):
        data1 = json.dumps(data)
        for i in change:
            # print(i)
            # print change[i]
            # d = json.dumps(dic2).replace(i,change[i])
            d = data1.replace(i, change[i])
            data1 = d
        return d


if __name__ == '__main__':
    a = 'https://www.sojson.com/open/api/weather/json.shtml'
    b = {'city': '北京'}
    http = DemoLei()
    print http.watcher1(a,b)
