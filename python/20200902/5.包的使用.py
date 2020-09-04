# -*- coding:utf-8 -*-

# @version:     python3.8
# @author:      Bruce
# @file name:   5.包的使用.py
# @time:        2020/9/2 22:00

# 1、包：就是一个包含有__init__.py文件的文件夹
    # 包的本质就是模块的一种形式，包是被用来当做模块使用

# a、产生一个名称空间
# b、运行包下的__init__.py文件，将运行过程中产生的名字都丢到a中的名称空间
# c、在当前执行文件的名称空间中拿到一个名字my_pachage,该名字my_pachage指向a的名称空间

# ===========模块的使用者：Bruce============

# import bag1
#
# print(bag1.x)
# print(bag1.y)
# bag1.say()
# print(bag1.say)

# 环境变量都是以执行文件为准的，所有被导入的模块或者说后续的其它文件的引用的sys.path
    # 都是参照执行问价的sys.path

# import sys
# sys.path.append(r'/aaaaaa')
# print(sys.path)

# import bag2  # bag2下的__init__.py

# sys.path.append(r'D:\Users\LENOVO\PycharmProjects\python\20200902\bag2')

# bag2.f1()
# bag2.f2()
# bag2.f3()

# bag2.f4()

# from bag2 import f1,f2,f3

# 强调：
# 1.关于包相关的导入语句也分为import和from ... import ...两种，
    # 但是无论哪种，无论在什么位置，在导入时都必须遵循一个原则：
    # 凡是在导入时带点的，点的左边都必须是一个包，否则非法。
    # 可以带有一连串的点，如import 顶级包.子包.子模块,但都必须遵循这个原则。
    # 但对于导入后，在使用时就没有这种限制了，点的左边可以是
    # 包,模块，函数，类(它们都可以用点的方式调用自己的属性)。

    # 例如：
    # from a.b.c.d.e.f import xxx
    # import a.b.c.d.e.f
    # 其中a、b、c、d、e都必须是包
# 2、包A和包B下有同名模块也不会冲突，如A.a与B.a来自俩个命名空间
# 3、import导入文件时，产生名称空间中的名字来源于文件，import 包，
    # 产生的名称空间的名字同样来源于文件，即包下的__init__.py，导入包本质就是在导入该文件

# from bag2 import f4
# f4()

import bag2

# bag2.f1()
# bag2.f2()
# bag2.f3()
# bag2.f4()
#
# print(bag2.f1)
# print(bag2.f2)
# print(bag2.f3)
# print(bag2.f4)

# bag2.f4()

from bag2 import *
print(f1)
print(f2)
print(f3)
print(f4)
# print(f5)