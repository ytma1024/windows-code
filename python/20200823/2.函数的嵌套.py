# -*- coding:utf-8 -*-

"""
@version:python3.8
@author: Bruce
@file:   .py
@time:   2020/8/23 17:30
"""

# 函数的嵌套

# 1、函数嵌套的调用：在调用一个函数的过程中又调用其他函数
# def max2(x,y):
#     if x>y:
#         return x
#     else:
#         return y
#
# def max4(a,b,c,d):
#     # 第一步：先比较a、b，返回res1
#     res1=max2(a,b)
#     # 第二步：先比较res1、c，返回res2
#     res2=max(res1,c)
#     # 第三步：先比较res2、d，返回res4
#     res3=max2(res2,d)
#     return res3
#
# res = max4(1,2,3,4)
# print(res)

# 2、函数嵌套的定义：在函数内定义函数
# def f1():
#     def f2():
#         pass

# 求圆形的周长与面积
# def circle(radius,action):
# # 求周长
#     from math import pi
#     def perimiter(radius):
#         return 2*radius*pi
#
# # 求面积
#     from math import pi
#     def area(radius):
#         return pi*(radius**2)
#
#     if action==0:
#         return perimiter(radius)
#     elif action==1:
#         return area(radius)
#
# res = circle(3,1)
# print(res)
