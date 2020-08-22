# -*- coding:utf-8 -*-

"""
@version:python3.8
@author: Bruce
@file:   .py
@time:   2020/8/18 16:02
"""
"""
t文本(默认的模式)
    a、读写都是以str(unicode)为单位的模式
    b、文本文件
    c、必须制定encoding='utf-8'
"""
# 没有指定encoding参数，操作系统会使用自己默认的编码
# linux系统默认为utf-8
# windows系统默认为gbk

# 不加encoding='utf-8',test.txt中的汉字会解码成乱码
with open('test.txt',mode='rt',encoding='utf-8') as f:
    res=f.read()  # t模式会将f.read()读出的结果解码成utf-8
    print(res)

# 内存：utf-8格式的二进制------解码------>unicode
# 硬盘：(test.txt内容：utf-8格式)