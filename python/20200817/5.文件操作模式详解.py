# -*- coding:utf-8 -*-

"""
@version:python3.8
@author: Bruce
@file:   .py
@time:   2020/8/18 16:20
"""

# 以t模式为基础进行内存操作
# 1、r模式(默认的操作模式)：只读模式，当文件不存在时报错，
#                                当文件存在时指针跳到开始位置
# with open('test.txt',mode='rt',encoding='utf-8') as f:
#     print('第一次读'.center(50,'*'))
#     res1=f.read()  # 把文件内容从硬盘读到内存
#     print(res1)
# # with open('test.txt', mode='rt', encoding='utf-8') as f:  # 重新打开了文件
#     print('第二次读'.center(50, '*'))
#     res2 = f.read()  # 第二次没有读到内容，因为第一次读完，指针在文件末尾
#     print(res2)

# 案例一：
# inp_usrname = input("Please input your name>>:").strip(' ') #strip()去除字符串左右两侧的空白符
# inp_usrpasswd = input("Please input your password>>:").strip(' ')
#
# with open('info_usr.txt', mode='rt', encoding='utf-8') as f:
#     res = f.read()
#     # print(res, type(res))
#     usrname, usrpasswd = res.split(':')
#
# if inp_usrname == usrname and inp_usrpasswd == usrpasswd:
#     print("login successful!")
# else:
#     print('Your name or password is error!')

# 案例二：
# inp_usrname = input("Please input your name>>:").strip()
# inp_usrpasswd = input("Please input your password>>:").strip()
#
# with open('info_usr1.txt', mode='rt', encoding='utf-8') as f:
#     for line in f:
#         # print(line,end='')
#         usrname, usrpasswd = line.strip().split(':')
#
#         if inp_usrname == usrname and inp_usrpasswd == usrpasswd:
#             print('login successful!')
#             break
#
#     else:
#         print('Your name or password is error')

# 2、r模式：只写模式，当文件不存在时，会创建空文件,
#                  当文件存在时，会清空文件，指针位于开始位置
# with open('test1.txt', mode='wt', encoding='utf-8') as f:
#     # f.read()  # 不可读
#     f.write('Hello,Bruce！')

# 强调1：以w模式打开文件，没有关闭的情况下，连续写入，新的内容总是跟在旧内容之后
# with open('test1.txt', mode='wt', encoding='utf-8') as f:
#     f.write('Hello,Bruce！\n')
#     f.write('Hello,Bruce！\n')
#     f.write('Hello,Bruce！\n')

# 强调2：如果重新以w模式打开文件，则会清空文件内容
# with open('test1.txt', mode='wt', encoding='utf-8') as f:
#     f.write('Hello,Bruce1！\n')
# with open('test1.txt', mode='wt', encoding='utf-8') as f:
#     f.write('Hello,Bruce2！\n')
# with open('test1.txt', mode='wt', encoding='utf-8') as f:
#     f.write('Hello,Bruce3！\n')

# w模式用来创建全新的文件


# 文本文件的copy工具
# src_file = input('请输入源文件路径(绝对路径)>>:')
# dst_file = input('请输入要copy到的文件路径(绝对路径)>>:')
# with open(r'{}'.format(src_file), mode='rt', encoding='utf-8') as f1, \
#         open(r'{}'.format(dst_file), mode='wt', encoding='utf-8') as f2:
#     res = f1.read()
#     f2.write(res)


# 3、a模式：只追加写，当文件不存在时，会创建空文件
#                  当文件存在时，指针会直接跳到文件末尾
# with open('test1.txt',mode='at',encoding='utf-8') as f:
#     # f.read()  # 报错
#     f.write('Bruce\n')
#     f.write('Kobe\n')
#     f.write('Jordan\n')

# 强调w模式与a模式的异同点：
#   相同点：再打开的文件不关闭的情况下，连续的写入，新写的内容总会跟在前面写的内容之后、
#   不同点：以a模式重新打开文件不会清空原文件内容，会将文件指针直接移动到文件末尾，
#   新写的内容跟在原来的文件之后

# a模式用来在原有内容的基础上写入新的内容，比如：记录日志、注册功能
# 注册功能：
# usrname=input('Please input your name>>:')
# usrpwd=input('Please input your password>>:')
#
# with open('info_usr2.txt',mode='at',encoding='utf-8') as f:
#     f.write('{}:{}\n'.format(usrname,usrpwd))

# 4、+不能单独使用，必须配合r、w、a
# with open('test.txt',mode='rt+',encoding='utf-8') as f:
#     # f.read()
#     f.write('中国')

# with open('test.txt', mode='wt+', encoding='utf-8') as f:
#     f.write('Bruce\n')
#     f.write('Alex\n')
#     f.write('Kobe\n')
#     f.write('Jordan\n')
#     print('----->:'f.read())  # 写入内容之后，指针偏移到文件末尾，故读不到内容

# with open('test.txt', mode='at+', encoding='utf-8') as f:
#     f.write('Wade\n')
#     f.write('James\n')
#     print('---->:', f.read())
