#!/usr/bin/env python
# -*-encoding:UTF-8-*-

import http.client  # 导入http模块
import re  # 导入正则表达式
import datetime, time  # 导入时间
import sys

f = open("a.txt", "r")  # 获取a.txt中的股票代码
line = f.readline()
while line != "":
    stockcode = line[:6]
    now = datetime.datetime.now()  # 定义时间
    now.strftime('%Y-%m-%d')  # 定义时间格式

    # http get
    conn = http.client.HTTPConnection("qt.gtimg.cn")  # 获取http页面
    conn.request("GET", "/q=sh" + str(stockcode))
    r1 = conn.getresponse()
    print(r1.status, r1.reason)

    # 输出部分
    List1 = [r1.read().decode('GBK')]  # 定义r1读取的内容，GBK格式
    file1 = open('text_file.txt', 'a')  # 导入http模块，a表示追加

    file1.write('\n')
    file1.write(str(now))
    file1.write(str(List1))
    file1.write('\n')
    file1.close()
    conn.close()

    line = f.readline()
f.close()

