#coding=utf-8
import requests
import json
import xlrd

from api.lei import DemoLei
from api.DataLei import *


if __name__ == '__main__':
    table = xlrd.open_workbook('api\TestCase.xlsx')
    sheet = table.sheet_by_name('TestCase')
    # 横行
    a = sheet.row_values(0)
    # 竖行
    b = sheet.col_values(0)
    # 第一行
    firstRow = sheet.row_values(0)
    # 总共多少行
    nRow = sheet.nrows
    nCol = sheet.ncols

    for row in xrange(nRow):
        for col in xrange(nCol):
            print(sheet.cell_value(0,col)+'     '+sheet.cell_value(row,col))

    # 取出表格中的值，用方法接口测试
    # url = sheet.cell_value(1, 0)
    # headers = sheet.cell_value(1, 2)
    # data = sheet.cell_value(1, 3)
    # http = DemoLei()
    # a = http.watcher(url=url,headers=eval(headers),data=data)
    # print(a)