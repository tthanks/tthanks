#!/usr/bin/env python
# -*-encoding:UTF-8-*-

import http.client  # 导入http模块
import re  # 导入正则表达式
import datetime, time  # 导入时间
import sys

def main():

    stock_list = open("stock_list.txt", "r")  # 获取a.txt中的股票代码
    line = stock_list.readline()
    while line != "":
        stockcode = line[:8]
        now = datetime.datetime.now()  # 定义时间
        now.strftime('%Y-%m-%d')  # 定义时间格式
        # http get
        conn = http.client.HTTPConnection("qt.gtimg.cn")  # 获取http页面
        conn.request("GET", "/q=" + str(stockcode))
        result = conn.getresponse()
        print(result.status, result.reason)
        # 输出部分
        Original_list = [result.read().decode('GBK')]  # 定义result读取的内容，GBK格式
        Original_list_file = open('Original_list_file.txt', 'a')  # 导入http模块，a表示追加
        #Original_list_file.write('\n')
        Original_list_file.write(str(now)+str(Original_list))
        #Original_list_file.write(str(Original_list))
        Original_list_file.write('\n')
        Original_list_file.close()
        conn.close()
        line = stock_list.readline()#防止进入无限的循环

    stock_list.close()



if __name__ == '__main__':
    main()



