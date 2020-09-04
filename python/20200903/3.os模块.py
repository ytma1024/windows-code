# -*- coding:utf-8 -*-

# @version:     python3.8
# @author:      Bruce
# @file name:   3.os模块.py
# @time:        2020/9/3 22:27

import os
# 1、获取某一个文件夹下的子文件以及子文件夹的名字
# res=os.listdir(r'D:\Users\LENOVO\PycharmProjects\python\20200903')
# print(res)
#
# 2、获取某一个文件的大小
# size=os.path.getsize(r'D:\Users\LENOVO\PycharmProjects\python\20200903\1.时间模块.py')
# print(size)

# print(os.name)

# 3、显示某一个文件夹下的文件
# os.system("dir D:\\Users\\LENOVO\\PycharmProjects\\python")

# 4、规定：ket与value必须都为字符串
# os.environ['aaaaa']='11111'
# print(os.environ)

# 5、文件的绝对路径
# print(__file__)
# print(os.path.abspath(__file__))

# 6、将某一文件夹下的文件与该文件夹切分开
# res=os.path.split('D:\\Users\\LENOVO\\PycharmProjects\\python\\20200903\\3.os模块.py')
# print(res)

#/7、打印出该文件的上上级目录
# BASE_DIR=os.path.dirname(os.path.dirname(__file__))
# print(BASE_DIR)
#
# BASE_DIR1=os.path.normpath(os.path.join(__file__,'..','..'))
# print(BASE_DIR1)

# 在python3.5之后推出了一个新的模块pathlib
# from pathlib import Path
# root=Path(__file__)
# res=root.parent.parent
# print(res)
