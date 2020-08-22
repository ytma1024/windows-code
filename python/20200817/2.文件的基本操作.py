# -*- coding:utf-8 -*-

"""
@version:python3.8
@author: Bruce
@file:   文件的基本操作.py
@time:   2020/8/18 9:50
"""

# 文件的基本操作：
# 1、打开文件
# windows路径分隔符问题：
# open(r"D:\Users\LENOVO\PycharmProjects\python\20200812")

# 解决方案：
#   a、在绝对路径前面加上r
# open(r"D:\Users\LENOVO\PycharmProjects\python\20200812")
#   b、把\换成/
# open("D:/Users/LENOVO/PycharmProjects/python/20200812")

# 如果基于当前文件夹下的文件，直接写该文件的名称
# open("test.txt")

f = open("test.txt", mode ='rt')  # f的值是一种变量，占用的是应用程的内存空间
                                  # 还占用操作系统的空间
# print(f)

# x = int(10)  # 只占应用程序的空间

# 2、操作文件：读/写文件,应用程序的读写请求都是在向操作系统发送系统调用，
#然后由操作系统控制硬盘把数据读入内存或者写入硬盘
res = f.read()
print(res)

# 3、关闭文件
f.close()  # 回收操作系统资源
# del f  # 回收应用程序资源(可以不写)
