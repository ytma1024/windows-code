# -*- coding:utf-8 -*-

"""
@version:python3.8
@author: Bruce
@file:   .py
@time:   2020/8/24 9:40
"""

# 一、复习：
# 1、*args,**kwargs
# def index(x,y):  # index(1,2,3,4,a=5,b=6)  就会报错，参数太多
#     print(x,y)
#
# def wrapper(*args,**kwargs):  # args=(1,2,3,4) kwargs={'a':5,'b':6}
#     index(*args,**kwargs)  # index(1,2,3,4,a=5,b=6)
#
# # wrapper(1,2,3,4,a=5,b=6)
# wrapper(y=222,x=111)

# 2、名称空间与作用域：名称空间的“嵌套”关系是在函数定义阶段的，即检测语法的时候确定的

# 3、函数对象：
    # 可以把函数当做参数传入
    # 可以把函数当做返回值返回
# def index():
#     pass
#
# def foo(func):
#     return func
#
# foo(index)  # 将函数index的内存地址传给函数foo

# 4、函数的嵌套定义：
# def wrapper(func):
#     def foo():
#         pass
#     return foo

# 5、闭包函数
# def outer():
#     x=111
#     def wrapper():
#         print(x)
#         # print(wrapper)
#     return wrapper
#
# f=outer()
#
# print(f)
# f()

# 传参的方式一：通过参数的形式为函数体传参
# def wrapper(x):
#     print(1)
#     print(2)
#     print(3)
#     x
#
# wrapper(1)
# wrapper(2)
# wrapper(3)

# 传参的方式二：通过闭包的形式为函数体传参
# def outer(x):
#     # x=1
#     def wrapper():
#         print(x)
#     return wrapper  # outer内的函数wrapper的内存地址
#
# f1=outer(1)
# f2=outer(2)
# f3=outer(3)
# f1()
# f2()
# f3()

# wrapper=outer(1)
# wrapper()

# 二、装饰器
# 1、装饰器指的是定义一个函数，该函数用来为其他函数添加额外的功能
# 2、开放封闭原则：
    # 开放指的是对拓展功能是开放的
    # 封闭指的是对修改源代码是封闭的

    # 装饰器就是在不修改被装饰对象源代码以及调用方式的前提下为被装饰对象添加新的功能

# 需求：在不修改index函数的源代码以及调用方式的前提下为被装饰对象添加新功能
# import time
# def index(x,y):
#     time.sleep(3)
#     print('index %s %s'%(x,y))
#
# index(111,222)

# 解决方案一：没有修改被装饰对象的调用方式，但是修改了其源代码
# import time
# def index(x,y):
#     start=time.time()
#     time.sleep(3)
#     print('index %s %s'%(x,y))
#     end=time.time()
#     print(end-start)
#
# index(111,222)

#解决方式二：没有修改被装饰对象的调用方式，也没有修改其源代码，但是代码冗余
# import time
# def index(x,y):
#     time.sleep(3)
#     print('index %s %s'%(x,y))
#
# start=time.time()
# index(111,222)
# end=time.time()
# print(end-start)
#
# start=time.time()
# index(333,444)
# end=time.time()
# print(end-start)

# 解决方案三：在解决方案二的基础上解决了代码冗余问题，但是带来一个新问题函数的调用方式改变了
# import time
# def index(x,y):
#     time.sleep(3)
#     print('index %s %s'%(x,y))
#
# def index_wrapper():
#     start=time.time()
#     index(111,222)
#     end=time.time()
#     print(end-start)
#
# index_wrapper()

# 方案三优化一：把index的参数写活了
# import time
# def index(x,y,z):
#     time.sleep(3)
#     print('index %s %s %s'%(x,y,z))
#
# def index_wrapper(*args,**kwargs):
#     start=time.time()
#     index(*args,**kwargs)
#     end=time.time()
#     print(end-start)
#
# # index_wrapper(111,222,333)
# index_wrapper(111,z=333,y=222)

# 方案三优化二：在优化一的基础上，把被装饰对象写活了，原来只能装饰index
# import time
# def index(x,y,z):
#     time.sleep(3)
#     print('index %s %s %s'%(x,y,z))
#
# def home(name):
#     time.sleep(2)
#     print('welcome %s to home'%name)
#
# def outer(func):
#     # func=index
#     def wrapper(*args,**kwargs):
#         start=time.time()
#         func(*args,**kwargs)
#         end=time.time()
#         print(end-start)
#     return wrapper
#
# # # f=outer(index)  # f=outer(index的内存地址)
# # # print(index)  # f=当初那个wrapper函数的内存地址
# # # f(111,222,333)
#
# # index=outer(index)  # 相比上两行代码，这一招叫偷梁换柱
# # index(111,222,333)
#
# home=outer(home)
# home('Bruce')
# # print(home)

# 方案三优化三：将wrapper做的跟被装饰对象一模一样，以假乱真
# import time
#
# def home(name):
#     time.sleep(2)
#     print('welcome %s to home'%name)
#     return 1234
#
# def outer(func):
#     # func=index
#     def wrapper(*args,**kwargs):
#         start=time.time()
#         res = func(*args,**kwargs)
#         end=time.time()
#         print(end-start)
#         return res
#     return wrapper
#
# home=outer(home)  # 偷梁换柱：home指向的是wrapper函数的内存地址
#
# res = home('Bruce')  # res=wrapper('Bruce')
# print('返回值',res)


# 解决方案四：在解决方案三的基础上，不改变函数的调用方式

# 语法糖：
# import time
#
# def decorator(func):
#     # func=index
#     def wrapper(*args,**kwargs):
#         start=time.time()
#         res = func(*args,**kwargs)
#         end=time.time()
#         print(end-start)
#         return res
#     return wrapper

# 在被装饰正上方单独一行写@装饰器名字
# @decorator  # index=decorator(index)
# def index(x,y,z):
#     time.sleep(3)
#     print('index %s %s %s'%(x,y,z))
#
# @decorator  # home=decorator(home)
# def home(name):
#     time.sleep(2)
#     print('welcome %s to home'%name)
#     return 1234
#
# # index=decorator(index)  # 相比上两行代码，这一招叫偷梁换柱
# index(111,222,333)
#
# # home=decorator(home)  # 偷梁换柱：home指向的是wrapper函数的内存地址
#
# res = home('Bruce')  # res=wrapper('Bruce')
# print('返回值',res)

# 自己练习:叠加多个装饰器，加载顺序与运行顺序
# @deco1  # index=deco1(deco2.wrapper的内存地址)
# @deco2  # deco2.wrapper的内存地址=deco2(deco3.wrapper的内存地址)
# @deco3  # deco3.wrapper的内存地址=deco3(index)
# def index():
#    pass


# 总结无参装饰器模板：
# def outer(func):
#     def wrapper(*args,**kwargs):
#         # 1、调用原函数
#         # 2、为其增加新功能
#         res=func(*args,**kwargs)
#         return res
#     return wrapper



# def index(*args,**kwargs):
#     pass


# 示例：
# import time
#
# def home(name):
#     print('welcome %s to home'%name)
#     return 1
#
# def outer(func):
#     def wrapper(*args,**kwargs):
#         start=time.time()
#         time.sleep(3)
#         res=func(*args,**kwargs)
#         end=time.time()
#         print(end-start)
#         return res
#     return wrapper
#
# # wrapper('Bruce')
#
# home=outer(home)  # home=wrapper的内存地址
# res=home('Bruce')  # res=wrapper('Bruce')
# print(home)
# print(res)

# 示例优化：
# import time
#
# def outer(func):
#     def wrapper(*args,**kwargs):
#         start=time.time()
#         time.sleep(3)
#         res=func(*args,**kwargs)
#         end=time.time()
#         print(end-start)
#         return res
#     return wrapper
#
# @outer  # 相当于home=outer(home)
# def home(name):
#     print('welcome %s to home'%name)
#     return 1
#
# # home=outer(home)  # home=wrapper的内存地址
# res=home('Bruce')  # res=wrapper('Bruce')
# print(home)
# print(res)

# 例子(登录功能)：
# import time
#
# def register():
#     inp_usrname=input('请输入您的名字>>:')
#     inp_usrpwd=input('请输入您的密码>>:')
#     with open(r'info_usr.txt',mode='rt',encoding='utf-8') as f:
#         usrname,usrpwd=f.read().split(':')
#         if inp_usrname==usrname and inp_usrpwd==usrpwd:
#             print('登陆成功！')
#         else:
#             print('您输入的账号或者密码错误！')
#
# def outer():
#     def register_decorator():
#         start=time.time()
#         time.sleep(3)
#         register()
#         end=time.time()
#         print("登录花费时间>>:",end-start)
#     return register_decorator
#
# # register=outer()  # 为啥这个就不可以，只是名字不同而已
# # register()
# f=outer()  # 这个可以运行
# f()

# 示例优化：
# import time
#
# def register(*args,**kwargs):
#     inp_usrname=input('请输入您的名字>>:').strip()
#     inp_usrpwd=input('请输入您的密码>>:').strip()
#     with open(r'info_usr.txt',mode='rt',encoding='utf-8') as f:
#         usrname,usrpwd=f.read().split(':')
#         if inp_usrname==usrname and inp_usrpwd==usrpwd:
#             print('登陆成功！')
#         else:
#             print('您输入的账号或者密码错误！')
#     return 1
#
# def outer(func):
#     def register_decorator(*args,**kwargs):
#         start=time.time()
#         time.sleep(3)
#         res=func(*args,**kwargs)
#         end=time.time()
#         print("登录花费时间>>:",end-start)
#         return res
#     return register_decorator
#
# register=outer(register)
# res = register()
# print('返回值:',res)

# 示例再次优化
# import time
#
# def outer(func):
#     def register_decorator(*args,**kwargs):
#         start=time.time()
#         time.sleep(3)
#         res=func(*args,**kwargs)
#         end=time.time()
#         print("登录花费时间>>:",end-start)
#         return res
#     return register_decorator
#
# @outer  # 相当于register=outer(register)
# def register(*args,**kwargs):
#     inp_usrname=input('请输入您的名字>>:').strip()
#     inp_usrpwd=input('请输入您的密码>>:').strip()
#     with open(r'info_usr.txt',mode='rt',encoding='utf-8') as f:
#         usrname,usrpwd=f.read().split(':')
#         if inp_usrname==usrname and inp_usrpwd==usrpwd:
#             print('登陆成功！')
#         else:
#             print('您输入的账号或者密码错误！')
#     return 1
#
# # register=outer(register)
# res = register()
# print('返回值:',res)