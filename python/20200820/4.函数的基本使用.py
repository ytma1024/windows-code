# -*- coding:utf-8 -*-

"""
@version:python3.8
@author: Bruce
@file:   .py
@time:   2020/8/20 15:23
"""

# 1、函数的定义：
# 定义的语法
'''
def 函数名(参数1,参数2,...):
    """文档描述"""
    函数体
    return 值
'''


# 2、三种定义函数的形式：
# 2.1、形式一：无参函数
# def func():
#     print('Bruce')
#
#
# func()  # 调用函数

# 定义函数发生的事：
# a、申请内存空间保存函数体代码
# b、将上述内存地址绑定给函数名
# c、定义函数不会执行函数体代码，但是会检测函数体的语法

# 调用函数发生的事：
# a、通过函数名找到函数的内存地址
# b、然后加括号就是触发函数体代码的执行

# 2.2、形式二：有参函数
# def func(x, y):
#     print(x, y)
#
# func(1, 2)

# 2.3、形式三：空函数，函数体代码为pass
# def func(x, y):
#     pass
#
# func(1, 2)

# 3、调用函数：
# 3.1、语句的形式:只加括号调用函数
# func(1,2)

# 3.2、表达式形式:
# def add(x,y):
#     res = x+y
#     return res

# 赋值表达式
# res = add(1,2)
# print(res)

# 数学表达式
# res = add(1,2)*10
# print(res)

# 3.3、函数调用可以当做参数
# def add(x, y):
#     res = x + y
#     return res
#
# res = add(add(1, 2), 10)
# print(res)

# 4、函数的返回值：
# return:是函数结束的标志,即函数体代码一旦运行到return会立刻终止函数的运行,
# 并且会将return后的值当做本次运行的结果返回

# 4.1、返回None:函数体内没有return,或者return None
# def func():
#     print('Bruce')
#     return
#
# res = func()
# print(res)

# 4.2、返回一个值：return 值
# def func():
#     return 10
#
# res = func()
# print(res)

# 4.3、返回多个值，多个值之间用逗号分隔开,会被return返回成一个元组类型
# def func():
#     return 10, 'aaa', [1, 2]
#
# res = func()
# print(res,type(res))  # 运行结果：(10, 'aaa', [1, 2]) <class 'tuple'>
