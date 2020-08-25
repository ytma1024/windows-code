# -*- coding:utf-8 -*-

"""
@version:python3.8
@author: Bruce
@file:   .py
@time:   2020/8/25 15:13
"""

# 一、知识储备：

# 由于语法糖@的限制，outer函数只能有一个参数，并且该参数只能用来接收被装饰对象的内存地址
# def outer(func):
#     def wrapper(*args,**kwargs):
#         res=func(*args,**kwargs)
#         return res
#     return wrapper
#
# @outer  # index=outer(index) index=>wrapper
# def index(x,y):
#     print(x,y)
#
# wrapper的参数不能动,outer的参数也不能动

# 示例优化：
# def auth(func,database_type):
#     def wrapper(*args,**kwargs):
#         inp_usrname=input("Please input your name>>:").strip()
#         inp_usrpwd=input("Please input your password>>:").strip()
#         # 从文件中取账号密码进行验证
#         if database_type =='file':
#             if inp_usrname=='Bruce' and inp_usrpwd=='1234':
#                 print('Login successful!')
#                 print('基于文件的验证！')
#             else:
#                 print('Password or name is error!')
#             res=func(*args,**kwargs)
#             return res
#         elif database_type=='mysql':
#             print('基于数据库的验证！')
#         elif database_type=='ldap':
#             print('基于ladp的验证！')
#         else:
#             print('不支持改database_type类型！')
#     return wrapper
#
# # @auth  # 账号密码的来源是文件
# def index(x,y):
#     print('From index>>%s:%s'%(x,y))
#
# # @auth  # 账号密码的来源是数据库
# def home(name):
#     print('Home>>%s'%name)
#
# # @auth  # 账号密码的来源是Ldap
# def transfer():
#     print('Transfer>>')
#
# # index=auth(index,'file')
# # index(1,2)
#
# # home=auth(home,'mysql')
# # home('Bruce')
#
# # transfer=auth(transfer,'ldap')
# # transfer()

# 示例优化：
# def auth(database_type):
#     def deco(func):
#         def wrapper(*args,**kwargs):
#             inp_usrname=input("Please input your name>>:").strip()
#             inp_usrpwd=input("Please input your password>>:").strip()
#             # 从文件中取账号密码进行验证
#             if database_type =='file':
#                 if inp_usrname=='Bruce' and inp_usrpwd=='1234':
#                     print('Login successful!')
#                     print('基于文件的验证！')
#                 else:
#                     print('Password or name is error!')
#                 res=func(*args,**kwargs)
#                 return res
#             elif database_type=='mysql':
#                 print('基于数据库的验证！')
#             elif database_type=='ldap':
#                 print('基于ladp的验证！')
#             else:
#                 print('不支持改database_type类型！')
#         return wrapper
#     return deco
#
# deco=auth(database_type='file')
# @deco  # 账号密码的来源是文件
# def index(x,y):
#     print('From index>>%s:%s'%(x,y))
#
# deco=auth(database_type='mysql')
# @deco  # 账号密码的来源是数据库
# def home(name):
#     print('Home>>%s'%name)
#
# deco=auth(database_type='ladp')
# @deco  # 账号密码的来源是Ldap
# def transfer():
#     print('Transfer>>')
#
#
# index=deco(index)
# index(1,2)
#
# home=deco(home)
# home('Bruce')
#
# transfer=deco(transfer)
# transfer()

# 示例再次优化(语法糖)：
# def auth(database_type):
#     def deco(func):
#         def wrapper(*args,**kwargs):
#             inp_usrname=input("Please input your name>>:").strip()
#             inp_usrpwd=input("Please input your password>>:").strip()
#             # 从文件中取账号密码进行验证
#             if database_type =='file':
#                 if inp_usrname=='Bruce' and inp_usrpwd=='1234':
#                     print('Login successful!')
#                     print('基于文件的验证！')
#                 else:
#                     print('Password or name is error!')
#                 res=func(*args,**kwargs)
#                 return res
#             elif database_type=='mysql':
#                 print('基于数据库的验证！')
#             elif database_type=='ldap':
#                 print('基于ladp的验证！')
#             else:
#                 print('不支持改database_type类型！')
#         return wrapper
#     return deco
#
# # deco=auth(database_type='file')
# @auth(database_type='file')  # @deco index=deco(index) index=wrapper() # 账号密码的来源是文件
# def index(x,y):
#     print('From index>>%s:%s'%(x,y))
#
# # deco=auth(database_type='mysql')
# @auth(database_type='mysql')  # 账号密码的来源是数据库
# def home(name):
#     print('Home>>%s'%name)
#
# # deco=auth(database_type='ladp')
# @auth(database_type='ladp')  # 账号密码的来源是Ldap
# def transfer():
#     print('Transfer>>')
#
# index(1,2)
# home('Bruce')
# transfer()

# 有参装饰器模板：
def 有参装饰器(x,y,z):
    def outer(func):
        def wrapper(*args,**kwargs):
            res=func(*args,**kwargs)
            return res
        return wrapper
    return outer

@有参装饰器(1,y=2,z=3)
def 被装饰对象():
    pass