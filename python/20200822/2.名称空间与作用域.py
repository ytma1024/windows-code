# -*- coding:utf-8 -*-

"""
@version:python3.8
@author: Bruce
@file:   .py
@time:   2020/8/22 10:17
"""

# 一、名称空间namespaces:存放名字的地方，是对栈区的划分
# 有了名称空间之后，就可以在栈区中存放相同的名字，详细的，名称空间分为三种，分别是：
# 1、内置名称空间
# 存放的名字：存放的是python解释器内置的名字
"""
>>> print
<built-in function print>
>>> input
<built-in function input>
"""
# 存活周期：python解释器启动则产生，pyhton解释器关闭则销毁

# 2、全局名称空间
# 存放的名字：只要不是函数内部定义的，也不是函数内置的，剩下的都是全局名称空间
# 存活周期：python文件执行则产生，python文件运行完毕则销毁

# a=10
# if a>3:
#     b=20
#     if b==20:
#         pass
#
# def func():
#     x=111
#     y=222
#
# class foo():
#     pass

# 3、局部名称空间
# 存放的名字：在调用函数时，运行函数体代码过程中产生的函数内的名字
# 存活周期：在调用函数时存活，函数调用结束后则销毁

# 4、名称空间的加载顺序：
# 内置名称空间(必须有) > 全局名称空间(必须有) > 局部名称空间(可以没有)

# 5、名称空间的销毁顺序：
# 局部名称空间 > 全局名称空间 > 内置名称空间

# 6、名字的查找优先级：当前所在的位置向上一层一层查找
# 局部名称空间
# 全局名称空间
# 内置名称空间

# 如果当前位置在局部名称空间：
# 局部名称空间->全局名称空间->内置名称空间

# input=333
# def func():
#     input=444
#     print(input)
#
# func()  # 运行结果：444

# input=333
# def func():
#     print(input)
#
# func()  # 运行结果：333

# def func():
#     print(input)
#
# func()  # 运行结果：<built-in function input> (内置名称)

# 如果当前位置在全局名称空间：
# 全局名称空间->内置名称空间

# 示例：名称空间的“嵌套”关系是以函数的定义阶段为准的，与函数的调用无关
# x = 1
#
# def func():
#     print(x)
#
# def foo():
#     x = 222
#     func()
#
# foo()

# 示例：函数嵌套定义：
# input = 111
#
# def func1():
#     input = 222
#
#     def func2():
#         input = 333
#         print(input)
#
#     func2()
#
# def foo():
#     func1()
#
# foo()


# 二、作用域--->作用范围
# 1、全局作用域：内置名称空间、全局名称空间
# a、全局存活
# b、全局有效：被所有函数共享
# x=111
# def func():
#     print(x,id(x))
#
# def foo():
#     print(x,id(x))
#
# func()
# foo()


# 2、局部作用域：局部名称空间的名字
# a、临时存活
# b、局部有效：函数内有效

# LEGB

# built-in
# # global
# def f1():
#     #enclosing
#     def f2():
#         # enclosing
#         def f3():
#             # local
#             pass