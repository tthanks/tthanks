import re

with open(r'Original_list_file.txt', encoding='utf-8', ) as file:

    stock_list = open("stock_list.txt", "r")  # 获取a.txt中的股票代码
    line = stock_list.readline()
    n = 0
    while line != "":
        stockcode = line[:6]
        n = n + 1

        stock_price = re.compile('^(?P<remote_ip>[^ ]*)')
        line = stock_list.readline()

        regMatch = stock_price.match(line)
        linebits = regMatch.groupdict()
        print(linebits)
        for k, v in linebits.items():
            print
            k + ": " + v
        # 读文本的全文并打印出来
        #i = file.read().splitlines()
        #for a =
        #print (i)
        # 这个时候再读的话，返回EOF
        #print (stock_price)