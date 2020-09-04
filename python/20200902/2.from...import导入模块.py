# -*- coding:utf-8 -*-

"""
@version:python3.8
@author: Bruce
@file:   .py
@time:   2020/9/2 15:25
"""

# 1、import在使用时加前缀“模块.”的优缺点：
# 优点：肯定不会与当前名称空间的名字冲突
# 缺点：加前缀显得麻烦

# 2、from ... import导入也发生三件事：
# a、产生一个模块名称空间
# b、运行foo.py将运行过程中产生的名字都丢到模块名称空间中去
# c、在当前名称空间中拿到一个名字，该名字指向模块名称空间中名字对应的内存地址

# from foo import x
# from foo import get
# from foo import change

# print(x)
# print(get)
# print(change)

# get()
# change()
# get()
# print(x)
#
# from foo import x
# print(x)
# get()

# 3、from ... import ... 在导入模块时不加前缀：
# 优点：代码更加精简
# 缺点：与当前名称空间的名字容易混淆

# 4、可以在一行导入多个名字(不推荐)：
# from foo import x,get,change

# 5、*：导入模块中的所有名字：
# from foo import *
# print(x)
# print(get)
# print(change)

# 6、__all__
# __all__=['x','get','change']  # 控制*代表的名字有哪些

# 7、起别名
# from foo import get as g