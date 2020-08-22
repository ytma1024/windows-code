# -*- coding:utf-8 -*-

"""
@version:python3.8
@author: Bruce
@file:   .py
@time:   2020/8/22 22:03
"""

# 1、global
# 示例1：
# x=111
# def func():
#     x=222
#
# func()
# print(x)

# 示例2：如果在局部想要修改全局的名字对应的值(不可变类型),需要用global
# x=111
# def func():
#     global x
#     x=222
#
# func()
# print(x)

# 示例3：
# l=[111,222]
# def func():
#     l.append(333)
#
# func()
# print(l)

# 2、nonlocal:修改函数外层函数包含的值(不可变类型)

#示例：
# x=10
# def f1():
#     x=11
#     def f2():
#         global x
#         x=12
#     f2()
#     print('f1()的x:',x)
#
# f1()
# print(x)

# 示例：
# x=10
# def f1():
#     x=11
#     def f2():
#         nonlocal x
#         x=12
#     f2()
#     print('f1()的x:',x)
#
# f1()
# print(x)

def f1():
    x=[]
    def f2():
        x.append(111)
    f2()
    print('f1()的x:',x)

f1()
