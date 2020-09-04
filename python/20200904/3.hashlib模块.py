# -*- coding:utf-8 -*-

# @version:     python3.8
# @author:      Bruce
# @file name:   3.hashlib模块.py
# @time:        2020/9/4 21:22

# 1、哈希hash：
    # hash是一类算法，该算法接收传入的内容，经过运算得到一串hash值

# 2、hash的特点：
    # a、只要传入的内容一样，得到的hash值一定一样=====>要用明文传输密码文件完整性校验
    # b、不能由hash值反解成内容=====>把密码做成hash值，不应该在网络传输明文密码
    # c、只要使用的hash算法不变，无论校验的内容有多大，得到的hash值长度是固定的

# 3、hash的用途：
    # 用途1：特点b用于密码密文传输与验证
    # 用途2：特点a、c用于文件完整性校验

# 4、如何用：
#
# import hashlib
#
# m1=hashlib.md5()
# m1.update('hello'.encode('utf-8'))
# m1.update('world'.encode('utf-8'))
# res1=m1.hexdigest()  # helloworld
# print(res1)  # 运行结果：fc5e038d38a57032085441e7fe7010b0
#
# m2=hashlib.md5('he'.encode('utf-8'))
# m2.update('llo'.encode('utf-8'))
# m2.update('wo'.encode('utf-8'))
# m2.update('rld'.encode('utf-8'))
# res2=m2.hexdigest()  # helloworld
# print(res2)  # 运行结果：fc5e038d38a57032085441e7fe7010b0

# 示例：撞库破解密文密码
import hashlib
cryptograph='aee949757a2e698417463d47acac93df'
passwds=[
    'alex3714',
    'alex1313',
    'alex94139413',
    'alex123456',
    '123456alex',
    'a123lex',
    ]

dic={}

for pwd in passwds:
    res=hashlib.md5()
    res.update(pwd.encode('utf-8'))
    dic[pwd]=res.hexdigest()
    # print(pwd,dic[pwd])

for k,v in dic.items():
    if v==cryptograph:
        print('撞库成功！明文密码为:%s'%k)
        print('{\'%s\':\'%s\'}'%(k,v))
        break

# 提升撞库的成本=====>密码加盐