# -*- coding:utf-8 -*-

"""
@version:python3.8
@author: Bruce
@file:   .py
@time:   2020/8/26 10:55
"""

# 一、例子：
# def dog(name):
#     print('Dog %s吃东西啦...'%name)
#     while True:
#         # x拿到的是yield接收到的值
#         x=yield None  # x='一根骨头'
#         print('Dog %s吃了%s'%(name,x))
#
# g=dog('Alex')
# g.send(None)  # 等同于next(g)
#
# # print(g)
# g.send('一根骨头')
# g.send('肉包子')
# g.close()
# # g.send('111')  # 关闭之后无法传值

# 二、例子：
# def dog(name):
#     print('Dog %s吃东西啦...'%name)
#     while True:
#         # x拿到的是yield接收到的值
#         x=yield 111  # x='一根骨头'  (先把值给yield，然后由yield传值给x)
#         print('Dog %s吃了%s'%(name,x))
#
# g=dog('Alex')
# res=g.send(None)  # 等同于next(g)
# print(res)
#
# res=g.send('一根骨头')
# print(res)
# res=g.send('肉包子')
# print(res)
# g.close()

# 例子：
# def dog(name):
#     food_list=[]
#     print('Dog %s吃东西啦...'%name)
#     while True:
#         # x拿到的是yield接收到的值
#         x=yield food_list  # x='一根骨头'  (先把值给yield，然后由yield传值给x)
#         print('Dog %s吃了%s'%(name,x))
#         food_list.append(x)
#
# g=dog('Alex')
# res1=g.send(None)  # 等同于next(g)
# print(res1)  #[]
#
# res2=g.send('一根骨头')
# print(res2)  # ['一根骨头']
# res3=g.send('肉包子')
# print(res3)  # ['一根骨头','肉包子']
# g.close()

