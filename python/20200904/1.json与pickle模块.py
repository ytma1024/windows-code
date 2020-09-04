# -*- coding:utf-8 -*-

# @version:     python3.8
# @author:      Bruce
# @file name:   1.json与pickle模块.py
# @time:        2020/9/4 15:24

# 1、序列化：
    # 序列化指的是把内存的数据类型转化成一种特定格式的内容，
    # 该格式的内容可用于存储或者传输给其他平台使用

# 内存中的数据类型----->序列化----->特定的格式(json格式或者pickle格式)
# 内存中的数据类型<-----反序列化<-----特定的格式(json格式或者pickle格式)

# 2、序列化的原因：
    # 序列化得到的结果=====>特定格式的内容有两种用途
    # 1、可用于存储==>用于存储
    # 2、传输给其他平台使用==>跨平台数据交互

# 强调：
    # 针对用途1的特定格式：可以是一种专用的格式(pickle只有python可以识别)
    # 针对用途2的特定格式：应该是一种通用的，能够被所有语言识别的格式(json)

# 3、如何序列化与反序列化
# 示范一：
# import json

# 序列化
# json_res=json.dumps([1,'aaa',True,False])
# print(json_res,type(json_res))

# 反序列化
# l=json.loads(json_res)
# print(l,type(l))

# 示范二：
# import json

# 序列化(将序列化的结果写入文件的复杂方法)
# json_res=json.dumps([1,'aaa',True,False])
# # print(json_res,type(json_res))
# with open(r'test.json',mode='wt',encoding='utf-8') as f:
#     f.write(json_res)

# 将序列化的结果写入文件的简单方法
# with open(r'test.json',mode='wt',encoding='utf-8') as f:
#     json_res=json.dump([1,'aaa',True,False],f)

# 反序列化：(从文件读取json格式的字符串进行反序列化操作的复杂方法)
# with open(r'test.json',mode='rt',encoding='utf-8') as f:
#     json_res=f.read()
#     l=json.loads(json_res)
#     print(l,type(l))

# 从文件读取json格式的字符串进行反序列化的简单方法
# with open(r'test.json',mode='rt',encoding='utf-8') as f:
#     l=json.load(f)
#     print(l,type(l))

# json验证：json格式兼容的是所有语言通用的数据类型，不能识别某一语言所独有的
# import json
# json.dumps({1,2,3,4,5})

# 强调：不要把json格式与python格式混淆
# import json
# l=json.loads('[1,"aaa",true,false]')
# print(l)

# 4、猴子补丁
# 在入口处打补丁(猴子补丁)
# import json
# import ujson
#
# def monkey_patch_json():
#     json.__name__='ujson'
#     json.dumps=ujson.dumps
#     json.loads=ujson.loads
#
# monkey_patch_json()  # 在入口文件处运行

# 5、pickle模块

# import pickle
#
# res=pickle.dumps({1,2,3,4,5})
# print(res,type(res))
#
# l=pickle.loads(res)
# print(l,type(l))

