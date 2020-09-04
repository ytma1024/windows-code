# -*- coding:utf-8 -*-

"""
@version:python3.8
@author: Bruce
@file:   .py
@time:   2020/8/26 16:56
"""

# 1、函数的递归调用：是函数嵌套调用的一种特殊形式
             # 具体是指在调用一个函数的过程中又直接或者间接的调用了自己

# 直接调用本身：
# def func():
#     print('It\'s me')
#     func()
# func()

# 间接调用本身：
# def func1():
#     print('=====>func1')
#     func2()
#
# def func2():
#     print('=====>func2')
#     func1()
# func1()

# 一段代码重复运行的方式：
# 方式一：while循环
# while True:
#     print(11111)
#     print(22222)
#     print(33333)

# 方式二：递归调用的本质就是循环
# def func():
#     print(11111)
#     print(22222)
#     print(33333)
#     func()
# func()

# 2、强调：递归调用不应该无限的调用下去，必须在满足某种条件下结束递归调用

# n=0
# while n<10:
#     print(n)
#     n+=1

# def func(n):
#     if n==10:
#         return
#     else:
#         print(n)
#         n+=1
#     func(n)
# func(0)

# 3、递归的两个阶段：
# 回溯：一层一层调用下去
# 递推：满足某种结束条件，结束递归调用，然后一层一层返回

# age(5)=age(4)+10
# age(4)=age(3)+10
# age(3)=age(2)+10
# age(2)=age(1)+10
# age(1)=18

# def age(n):
#     if n==1:
#         return 18
#     return age(n-1)+10
#
# res=age(5)
# print(res)

# 递归调用的应用：
# lst=[1,[2,3]]
# for x in lst:
#     if x is list:
#         pass
#     else:
#         print(x)

# lst=[1,[2,[3,[4,[5,[6,[7,[8,[9,[10,11,12]]]]]]]]]]
# def func(l):
#     for x in l:
#         if type(x) is list:
#             func(x)
#         else:
#             print(x)
#
# func(lst)
