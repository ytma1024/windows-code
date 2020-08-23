# -*- coding:utf-8 -*-

"""
@version:python3.8
@author: Bruce
@file:   .py
@time:   2020/8/23 16:09
"""

# 精髓：可以把函数当成变量去用
# func==内存地址
# 1、可以赋值
# def func():
#     print("from func()")
#
# f=func  # 可以赋值
# print(f,func)
#
# f()

# 2、可以当做函数的参数传入
# def func():
#     print('from func()')
#
# def foo(x):
#     print(x)
#
# foo(func)  # foo(func的内存地址)

# 3、可以把函数当做另外一个函数的返回值

# def func():
#     print('from func()')
#
# def foo(x):
#     return x
#
# res=foo(func)
# print(res)  # 运行结果(func的内存地址)：<function func at 0x000002012D6FC1F0>

# res()

# 4、可以当做容器类型的一个元素

# def func():
#     print('from func()')
#
# l=[func]
# print(l)
# l[0]()  # 调用函数func()

# def func():
#     print('from func()')
#
# dic={'k1':func}
# dic['k1']()  # 调用函数func()

# 示例：
# def log_out():
#     print('退出程序')
#
# def log_in():
#     print('登录')
#
# def transfer_accounts():
#     print('转账')
#
# def balance_inquiry():
#     print('查询余额')
#
# while True:
#     print('0、退出程序\n'
#           '1、登录\n'
#           '2、转账\n'
#           '3、查询余额')
#     inp_cnt=input('请输入功能所对应的指令>>:')
#     if not inp_cnt.isdigit():
#         print('必须输入指令对应的数字序号！')
#         continue
#     if inp_cnt=='0':
#         log_out()
#         break
#     elif inp_cnt=='1':
#         log_in()
#     elif inp_cnt=='2':
#         transfer_accounts()
#     elif inp_cnt=='3':
#         balance_inquiry()
#     else:
#         print("必须输入指令对应的数字序号！")

# 示例优化：
# def log_out():
#     print('退出程序')
#
# def log_in():
#     print('登录')
#
# def transfer_accounts():
#     print('转账')
#
# def balance_inquiry():
#     print('查询余额')
#
# func_dic={
#     '0':log_out,
#     '1':log_in,
#     '2':transfer_accounts,
#     '3':balance_inquiry
# }
#
# while True:
#     print('0、退出程序\n'
#           '1、登录\n'
#           '2、转账\n'
#           '3、查询余额')
#     inp_cnt=input('请输入功能所对应的指令>>:')
#     if not inp_cnt.isdigit():
#         print('必须输入指令对应的数字序号！')
#         continue
#     if inp_cnt in func_dic:
#         func_dic[inp_cnt]()
#     else:
#         print('必须输入指令对应的数字序号！')

# 示例继续优化：
def log_out():
    print('退出程序')

def log_in():
    print('登录')

def transfer_accounts():
    print('转账')

def balance_inquiry():
    print('查询余额')

func_dic={
    '0':['退出程序',log_out],
    '1':['登录',log_in],
    '2':['转账',transfer_accounts],
    '3':['查询余额',balance_inquiry]
}

while True:
    for k in func_dic:
        print(k,':',func_dic[k][0])
    inp_cnt=input('请输入功能所对应的指令的序号>>:').strip()
    if inp_cnt==0:
        print('退出程序！')
        break
    if not inp_cnt.isdigit():
        print('必须输入指令对应的数字序号！')
        continue
    if inp_cnt in func_dic:
        func_dic[inp_cnt][1]()
    else:
        print('您所输入的指令序号不存在,请重新输入！')