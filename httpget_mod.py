#!/usr/bin/env python
# -*-encoding:UTF-8-*-

import http.client  # 导入http模块
import re  # 导入正则表达式
import datetime, time  # 导入时间
import sys
import re
import datetime

def main():

    stock_list = open("./stock_list.txt", "r")  # 获取a.txt中的股票代码
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
        original_list = [result.read().decode('GBK')]  # 定义result读取的内容，GBK格式
        original_list_file = open('./original_list_file.txt', 'a')  # 导入http模块，a表示追加
        # original_list_file.write('\n')
        original_list_file.write(str(now)+str(original_list))
        # original_list_file.write(str(original_list))
        original_list_file.write('\n')
        original_list_file.close()
        conn.close()
        line = stock_list.readline()    # 防止进入无限的循环

    stock_list.close()


if __name__ == '__main__':
    main()


file = open("./Original_list_file.txt", "r")
content = file.readline()
now = datetime.datetime.now()  # 定义时间
time = now.strftime('%Y-%m-%d')  # 定义时间格式

while content != "":
    content_initial = content
    # print(content_initial)
    # ontent_process_step1 = re.compile(r'~[0-9]+\.?[0-9]+')
    content_process_step1 = re.compile(r'(?<=~).+?(?=~)')  # 匹配的字符是XX，但必须满足形式是AXXB这样的字符串
    content_process_step2 = content_process_step1.findall(content_initial)  # 找到所有符合正则表达式的list元素
    content_process_step2.insert(0, content[0:19])  # 获取日期
    content_process_step3 = content_process_step2[:6]  # 截取list的前面6位，分别是股票名字、代码、当前价格、昨收、今开
    # content_process_step3.append(content[10:])
    print(content_process_step3)

    # content_spilit = content_initial.split("~")
    # print(content_spilit)
    # stock_price = re.compile(r' ' + str(stockcode) + ' ')
    # print(content)
    # regMatch = stock_price.findall(content)
    # print(regMatch)
    content = file.readline()
    # 读文本的全文并打印出来
    # i = file.read().splitlines()
    # for a =
    # print (i)
    # 这个时候再读的话，返回EOF
# stock_price = re.compile(r'')

# regMatch = stock_price.split(line)
        # print (stock_price)


