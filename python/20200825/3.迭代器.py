# -*- coding:utf-8 -*-

"""
@version:python3.8
@author: Bruce
@file:   .py
@time:   2020/8/25 16:43
"""

# 迭代器

# 1、迭代器的定义：迭代器指的是迭代取值的工具，迭代是一个重复的过程，每次重复都是基于上一次
    # 的结果而继续的，单纯的重复并不是迭代

# 2、为何有迭代器：
    # 迭代器是用来迭代取值的工具，而涉及到把多个循环值取出来的
    # 类型有：字符串，列表，元组，字典，集合，文件

# lst=['Bruce','Kobe','Jordan']
# i=0
# while i<len(lst):
#     print(lst[i])
#     i+=1

# 上述迭代方式的取值只适用于有索引的数据类型：字符串，列表，元组

# 为了解决基于索引迭代取值的局限性，python必须提供一种不依赖于索引取值的方式，这就是迭代器。

# 可迭代对象：但凡内置有__iter__方法的都称之为可迭代对象
# s1=''
# s1.__iter__()
# lst=[]
# lst.__iter__()
# tup=(1,)
# tup.__iter__()
# dic={'a':1}
# dic.__iter__()
# set={1,2,3}
# set.__iter__()
# with open(r'test.txt',mode=='w',encoding='utf-8') as f:
#     f.__iter__()
#
# 调用可迭代对象下的__iter__方法会将其转换为迭代器对象
# dic={'a':1,'b':2,'c':3}
# dic_iterator=dic.__iter__()
# print(dic_iterator)  # 运行结果：<dict_keyiterator object at 0x000001C783F16950>

# print(dic_iterator.__next__())  # 运行结果：a
# print(dic_iterator.__next__())  # 运行结果：a
# print(dic_iterator.__next__())  # 运行结果：a

# while True:
#     try:
#         print(dic_iterator.__next__())
#     except StopIteration:
#         break
#
# print('============')  # 在对一个迭代器取值取干净的情况下，在对其取值取不到
# dic_iterator=dic.__iter__()
#
# while True:
#     try:
#         print(dic_iterator.__next__())
#     except StopIteration:
#         break

# lst=[1,2,3,4,5]
# lst_iterator=lst.__iter__()
# while True:
#     try:
#         print(lst_iterator.__next__())
#     except StopIteration:
#         break

# 3、可迭代对象与迭代器对象
# 3.1、可迭代对象(“可以转换成迭代器的对象”)：内置有__iter__方法的
    # 可迭代对象.__iter__():得到迭代器
# 3.2、迭代器对象：内置有__next__方法并且内置有__iter__方法的
    # 迭代器对象.__next__():得到迭代器的下一个值
    # 迭代器对象.__iter__():得到迭代器本身，相当于没调

# 5、可迭代对象：字符串，列表，元组，字典，集合
# 迭代器对象：文件对象
# s1=''
# s1.__iter__()
# lst=[]
# lst.__iter__()
# tup=(1,)
# tup.__iter__()
# dic={'a':1}
# dic.__iter__()
# set={1,2,3}
# set.__iter__()
# with open(r'test.txt',mode=='w',encoding='utf-8') as f:
#     f.__iter__()

# with open(r'test.txt',mode='rt',encoding='utf-8') as f:
#     for line in f:
#         print(line)

# 5、for循环工作原理：for循环可以称之为迭代器循环
    # a、dic.__iter__()得到一个迭代器对象
    # b、迭代器对象.__next__()拿到一个返回值，然后将该返回值赋值给k
    # c、循环往复步骤b,知道抛出StopIteration异常，for循环会捕捉异常然后结束循环
# dic={'a':1,'b':2,'c':3}
# for k in dic:
#     print(k)

# list('hello')  # 原理同for循环

# 6、迭代器优缺点总结：
# 优点
    # 非常节省内存。
    # 惰性机制。

# 缺点
    # 不直观。
    # 操作不灵活。
    # 效率相对低。