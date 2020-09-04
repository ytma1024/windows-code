# -*- coding:utf-8 -*-

# @version:     python3.8
# @author:      Bruce
# @file name:   start.py
# @time:        2020/9/3 10:00

# 绝对导入参照sys.path
# import sys
# sys.path.append(r'D:\Users\LENOVO\PycharmProjects\python\20200902\ATM')
#
# # from core import src
# # src.run()
#
# from core.src import run
# run()

# 优化方案：
import os
# os.path.dirname()
# print(__file__)  # 当前文件的绝对路径
# print(os.path.dirname(__file__))
# print(os.path.dirname(os.path.dirname(__file__)))

BASE_DIR=os.path.dirname(os.path.dirname(__file__))

import sys
sys.path.append(BASE_DIR)

from core import src

if __name__ == '__main__':
    src.run()