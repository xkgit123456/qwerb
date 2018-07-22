#coding=utf-8
import requests
import json

# 转换并替换
# dic2 = json.dumps(dic1).replace('a1','aa1')
# print(dic2)


#
def changeData(data,change):
    data1 = json.dumps(data)
    for i in change:
        # print(i)
        # print change[i]
        # d = json.dumps(dic2).replace(i,change[i])
        d =data1.replace(i,change[i])
        data1 = d
    return d

if __name__ == '__main__':
    data = {"A1": "b1", "A2": 'b2', 'a': {"A1": "b1", "A2": 'b2'}}
    change = {}
    change['b1'] = 'B1'
    change['b2'] = 'B2'

    print changeData(data,change)