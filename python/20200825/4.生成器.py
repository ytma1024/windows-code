# -*- coding:utf-8 -*-

"""
@version:python3.8
@author: Bruce
@file:   .py
@time:   2020/8/25 21:35
"""

# 生成器

# 如何得到自定义的生成器：
    # 在函数内一旦存在yield关键字，调用函数并不会执行函数体代码，
    # 会返回一个生成器对象，生成器即自定义的迭代器

# def func():
#     print('第一次')
#     yield 1
#     print('第二次')
#     yield 2
#     print('第三次')
#     yield 3
#     print('第四次')
#
# g=func()
# # print(g)
#
# # 生成器就是迭代器
# # g.__iter__()
# # g.__next__()
#
# # 会触发函数体代码的运行，然后遇到yield停下来，将yield后的值当做本次调用的结果返回
# res1=g.__next__()
# print(res1)
#
# res2=g.__next__()
# print(res2)
#
# res3=g.__next__()
# print(res3)
#
# res4=g.__next__()  # StopIteration

# 统计迭代器的长度：
# len('aaa')  # 'aaa'.__len__()

# next(g)  # g.__next__()

# iter(可迭代对象)   # 可迭代对象.__iter__()

# 示例：
def my_range(start,end,step):
    print('=====start=====')
    while start<end:
        yield start
        start+=step
    print('======end======')

# g=my_range(1,10,2)

# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

for n in my_range(1,10,3):
    print(n)