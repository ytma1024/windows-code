# -*- coding:utf-8 -*-

"""
@version:python3.8
@author: Bruce
@file:   .py
@time:   2020/8/19 16:26
"""

# 控制文件读写内容的模式
# t:
# a、读写都是以字符串为单位
# b、只能针对文本文件
# c、必须指定字符编码，即必须指定encoding参数
# b:
# a、读写都是以bytes为单位
# b、可以针对所有文件
# c、一定不能指定字符编码，即一定不能指定encoding参数

# 结论：
# a、在操作纯文本文件方面t模式帮我们省去了编码与解码的环节，b模式则需要手动编码与解码
# b、针对非文本文件(如：图片、视频)，只能用b模式

# with open('易建联受伤.mp4',mode='rb') as f:
#     res = f.read()  # 在b模式下，硬盘的二进制读入内存，不做任何转换，直接读入内存
#     print(res)  # bytes类型，当成二进制

# with open('test1.txt',mode='rb') as f:
#     res=f.read()  # utf-8的二进制
#     print(res,type(res))
#
#     print(res.decode('utf-8'))  # 运行结果：你好！

# with open('test1.txt',mode='rt',encoding='utf-8') as f:
#     res = f.read()
#     print(res)  # 运行结果：你好！

# 针对文本文件的copy小工具：
# old_file = input('请输入您的旧文件路径>>:').strip()
# new_file = input('请输入您的新文件路径>>:').strip()
# with open(r'{}'.format(old_file), mode='rt+', encoding == 'utf-8') as f1, \
#         open(r'{}'.format(new_file), mode='wt+', encoding='utf-8') as f2:
#     res = f1.read()
#     f2.write(res)
#     print(res)

# 针对任意文件的copy小工具：
# src_file = input('请输入您的旧文件路径>>:').strip()
# dst_file = input('请输入您的新文件路径>>:').strip()
# with open(r'{}'.format(src_file), mode='rb') as f1, \
#         open(r'{}'.format(dst_file), mode='wb') as f2:
#     res = f1.read()  # 内存占用过大
#     f2.write(res)
#     print(res)

# 循环读取文件
# 方式一：
# with open('数据类型总结与分类.jpg',mode='rb') as f:
#     while True:
#         res=f.read(1024)
#         if len(res)==0:
#             break
#         # print(res)
#         # print(len(res))

# 方式二：
# with open('数据类型总结与分类.jpg',mode='rb') as f:
#     for line in f:
#         print(line)