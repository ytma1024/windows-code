# -*- coding:utf-8 -*-

"""
@version:python3.8
@author: Bruce
@file:   .py
@time:   2020/8/22 8:56
"""


# 1、命名关键字参数
# 在定义函数时，*后定义的参数，如下所示，称之为命名关键字参数

# 特点：
# a、命名关键字必须按照key=value的形式为其传值
# def func(x, y, *, a, b):  # 其中a和b称为命名关键字参数
#     print(x, y)
#     print(a, b)
#
# func(1, 2, b=111, a=222)

# def func(x,y,*,a=111,b):
#     print(x,y)
#     print(a,b)
#
# func(1,2,b=222)

# 2、组合使用
# 形参混用的顺序(必须按照这个顺序)：位置形参，默认形参，*args,命名关键字参数，**kwargs
# def func(x,y=2,*args,z,**kwargs):
#     print(x)
#     print(y)
#     print(args)
#     print(z)
#     print(kwargs)

# 实参混用的顺序：
# def func(x,y,z,a,b,c):
#     print(x)
#     print(y)
#     print(z)
#     print(a)
#     print(b)
#     print(c)
#
# func(111,*[222,333],a=444,**{'b':555,'c':666})
#func(111,222,333,a=444,b=555,c=666)

# func(1)
# func(y=2)
# func(1,y=2)
# func(*'hello')
# func(**{'a':1,'b':2})
# func(*'hello',**{'a':1,'b':2})