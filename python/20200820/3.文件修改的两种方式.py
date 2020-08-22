# -*- coding:utf-8 -*-

"""
@version:python3.8
@author: Bruce
@file:   .py
@time:   2020/8/20 10:52
"""

# 文件修改的两种方式：
# 方式一：(文本编辑器采用的方式)
# 耗费内存，硬盘上只有一份数据
# with open(r'test.txt', mode='rt', encoding='utf-8') as f1:
#     res = f1.read()
#     print(res)
#     res1 = res.replace('Bruce', 'Kobe')
#     print(res1)
#
# with open(r'test.txt', mode='wt', encoding='utf-8') as f2:
#     res3 = f2.write(res1)
#     print(res3)

# 方式二：
# 内存耗费小，硬盘上有两份数据
# import os
#
# with open(r'test.txt', mode='rt', encoding='utf-8') as f1, \
#         open(r'.test.txt.swap', mode='wt', encoding='utf-8') as f2:
#     for line in f1:
#         f2.write(line.replace('Kobe', 'Bruce'))
#
# os.remove('test.txt')
# os.rename('.test.txt.swap', 'test.txt')
