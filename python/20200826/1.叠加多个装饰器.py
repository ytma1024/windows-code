# -*- coding:utf-8 -*-

"""
@version:python3.8
@author: Bruce
@file:   .py
@time:   2020/8/26 8:52
"""

# 复习有参装饰器：
# 示例：
# def deco(func):
#     def wrapper(*args,**kwargs):
#         inp_usrname=input("Please your name>>:").strip()
#         inp_usrpwd=input("Please your password>>:").strip()
#         with open(r'info_usr.txt',mode='rt',encoding='utf-8') as f:
#             usrname,usrpwd=f.read().split(':')
#             if inp_usrname==usrname and inp_usrpwd==usrpwd:
#                 print('Login successful!')
#             else:
#                 print('Your name or password is error!')
#         res=func(*args,**kwargs)
#         return res
#     return wrapper
#
# @deco  # index=deco(index)
# def index(x):
#     print('From index>>',x)
#
# index(1)

# 示例优化：
# def auth(database_type):
#     def deco(func):
#         def wrapper(*args,**kwargs):
#             inp_usrname=input("Please your name>>:").strip()
#             inp_usrpwd=input("Please your password>>:").strip()
#             with open(r'info_usr.txt',mode='rt',encoding='utf-8') as f:
#                 usrname,usrpwd=f.read().split(':')
#                 if database_type=='file':
#                     print('基于文件类型！')
#                     if inp_usrname==usrname and inp_usrpwd==usrpwd:
#                         print('Login successful!')
#                     else:
#                         print('Your name or password is error!')
#                 elif database_type=='mysql':
#                     print('基于mysql类型！')
#                 elif database_type=='ldap':
#                     print('基于ldap类型！')
#                 else:
#                     print('不能识别类型！')
#             res=func(*args,**kwargs)
#             return res
#         return wrapper
#     return deco
#
# @auth(database_type='file')# @deco  # index=deco(index)
# def index(x):
#     print('From index>>',x)
#
# @auth(database_type='mysql')# @deco  # index=deco(index)
# def home(name):
#     print('From home>>',name)
#
# @auth(database_type='ldap')# @deco  # index=deco(index)
# def transfer():
#     print('From transfer>>')
#
# index(1)
# home('Bruce')
# transfer()

# 一、叠加多个装饰器的加载、运行顺序分析：

# def deco1(func1):  # func1=wrapper2的内存地址
#     def wrapper1(*args,**kwargs):
#         print('正在运行===>>deco1.wrapper1')
#         res1=func1(*args,**kwargs)
#         return res1
#     return wrapper1
#
# def deco2(func2):  # func2=wrapper3的内存地址
#     def wrapper2(*args,**kwargs):
#         print('正在运行===>>deco1.wrapper1')
#         res2=func2(*args,**kwargs)
#         return res2
#     return wrapper2
#
# def deco3(x):
#     def outer3(func3):  # func3=被装饰对象index的内存地址
#         def wrapper3(*args,**kwargs):
#             print('正在运行===>>deco3.outer3.wrapper3')
#             res3=func3(*args,**kwargs)
#             return res3
#         return wrapper3
#     return outer3
#
# # 加载顺序：自下而上
# @deco1       # ==>>deco1(index(wrapper2的内存地址))==>>index=wrapper1的内存地址
# @deco2       # ==>>deco2(index(wrapper3的内存地址))==>>index=wrapper2的内存地址
# @deco3(111)  # ==>>@outer3==>>index=outer3(index)==>>index=wrapper3的内存地址
# def index(x,y):
#     print("From index>>%s %s"%(x,y))
#
# # 执行顺序:自上而下，即wrapper1-->wrapper2-->wrapper3
# index(1,2)