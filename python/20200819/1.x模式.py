# -*- coding:utf-8 -*-

"""
@version:python3.8
@author: Bruce
@file:   .py
@time:   2020/8/19 16:08
"""

# x模式(控制文件操作的模式):只写模式(不可读，不存在则创建，存在则报错)
# with open('test.txt',mode='x',encoding='utf-8') as f:  # 文件不存在，则创建
#     pass

# with open('test.txt',mode='x',encoding='utf-8') as f:  # 文件存在则报错
#     f.read()  # 不可读

# with open('test1.txt',mode='x',encoding='utf-8') as f:
#     f.write('你好！')