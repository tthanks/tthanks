import re

#with open('Original_list_file.txt', encoding='utf-8', ) as file:

file = open("Original_list_file.txt", "r")
content = file.readline()

while content != "":
    content_initial = content
    #print(content_initial)
    #content_process_step1 = re.compile(r'~[0-9]+\.?[0-9]+')
    content_process_step1 = re.compile(r'(?<=~).+?(?=~)')  ##匹配的字符是XX，但必须满足形式是AXXB这样的字符串
    #contest_process_step2 = str.lstrip('~');
    print(content_process_step1.findall(content_initial))
    #str = content_process_step1.findall(content_initial)
    #print(content_process_step2.findall(content_initial)

    #content_spilit = content_initial.split("~")
    #print(content_spilit)
    # stock_price = re.compile(r' ' + str(stockcode) + ' ')
    # print(content)
    # regMatch = stock_price.findall(content)
    # print(regMatch)
    content = file.readline()
    # 读文本的全文并打印出来
    #i = file.read().splitlines()
    #for a =
    #print (i)
    # 这个时候再读的话，返回EOF
#stock_price = re.compile(r'')

#regMatch = stock_price.split(line)
        #print (stock_price)