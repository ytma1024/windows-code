# -*- coding:utf-8 -*-

"""
@version:python3.8
@author: Bruce
@file:   .py
@time:   2020/8/23 21:09
"""

# 1、闭包函数：名称空间与作用域+函数嵌套+函数对象
# 核心点：名字的查找关系是以函数定义阶段为准的
# “闭”函数是指该函数是内嵌函数
# “包”函数是指该函数包含对外层函数(不是对全局作用域)作用域名字的引用

# 闭包函数：名称空间与作用域+函数嵌套的应用
# def f1():
#     x=33333
#     def f2():
#         print(x)
#     f2()
#
# def foo():
#     f1()
#
# x=11111
# def bar():
#     x=22222
#     foo()
#
# foo()

# 闭包函数：函数对象
# def f1():
#     x=33333
#     def f2():
#         print('函数f2():',x)
#
#     return f2
#
# f=f1()
# # print(f)  # 运行结果：<function f1.<locals>.f2 at 0x0000027DB8D4C0D0>
#
# x=44444
# # f()  # 运行结果：函数f2(): 33333
#
# def foo():
#     f()
#
# foo()  # 运行结果：函数f2(): 33333

# 3、闭包函数的应用：
# 两种为函数传参的方式
# 方式一：直接把函数体需要的参数定义成形参
# def f1(x):
# #     print(x)
# #
# # f1(1)

# 方式二：
# def f1():
#     x=3
#     def f2():
#         print(x)
#     # f2()
#
#     return f2
#
# x=f1()
# print(x)  # 运行结果：<function f1.<locals>.f2 at 0x000001FD6FB7C0D0>
#
# x()  # 运行结果：3

# 和上面的一样，只是变成传值，没有把值写死
# def f1(x):
#     # x=3
#     def f2():
#         print(x)
#     # f2()
#
#     return f2
#
# x=f1(3)
# print(x)  # 运行结果：<function f1.<locals>.f2 at 0x000001FD6FB7C0D0>
#
# x()  # 运行结果：3


# 传参方式有两种:
# 方式一：直接把函数体需要的参数定义成形参
# import requests
# def get(url):
#     response=requests.get(url)
#     print(response.text)
#
# get("https://www.baidu.com")

# "https://www.baidu.com"

# 方式二：闭包函数传参的方式
# import  requests
# def outer():
#     url="https://www.baidu.com"
#     def get():
#         response = requests.get(url)
#         print(response.text)
#
#     return get
#
# baidu=outer()
# print(baidu)
# baidu()

# 方式二优化：
# import  requests
# def outer(url):
#     # url="https://www.baidu.com"
#     def get():
#         response = requests.get(url)
#         print(response.text)
#
#     return get
#
# baidu=outer("https://www.baidu.com")
# # print(baidu)
# baidu()

# 方式二继续优化：
import  requests
def outer(url):
    # url="https://www.baidu.com"
    def get():
        response = requests.get(url)
        print(response.text)

    return get

baidu=outer("https://www.baidu.com")
# print(baidu)
baidu()