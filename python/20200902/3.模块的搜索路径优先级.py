# -*- coding:utf-8 -*-

"""
@version:python3.8
@author: Bruce
@file:   .py
@time:   2020/9/2 16:24
"""

# 1、无论是import还是from...import在导入时都设计查找问题

# 2、优先级：
    # 内存(内置空间)
    # 按照sys.path中存放的文件夹的顺序依次查找要导入的模块

# 3、import sys
# import sys
# 值为一个列表，存放了一系列的文件夹
# 其中第一个文件夹是当前执行文件的文件夹
# print(sys.path)

# ！！！这里有问题
# import sys
# sys.path.append(r'D:\Users\LENOVO\PycharmProjects\python\20200902\test\foo.py')
# # print(sys.path)
#
# import foo
# foo.get()

# 4、sys.modules查看已经加载到内存中的模块
# import sys
# print(sys.modules)