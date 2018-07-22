#coding=utf-8
import requests
import json

# # 转换字段
# json.loads()
# # 转换str
# json.dumps()
# # 读取文件
# json.load()
# # 写文件
# json.dump()

data = {'date':'2015-1-1","key":"3fc2053b46fcafdaacd98165f31706d4'}
# 打开文件
f = open('json.json')
data1 = json.load(f)
print(data1)
print(type(data1))
data2 = json.dumps(data1)
print(type(data2))
data3 = json.loads(data2)
print(type(data3))
f1 = open('write.json','w')
json.dump(data2,f1)
f.close
f1.close





