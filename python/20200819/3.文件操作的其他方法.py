# -*- coding:utf-8 -*-

"""
@version:python3.8
@author: Bruce
@file:   .py
@time:   2020/8/19 23:11
"""

# 1、读相关操作

# 1.1、readline() 一次读一行

# with open(r'test1.txt', mode='rt', encoding='utf-8') as f:
#     while True:
#         line = f.readline()
#         if len(line) == 0:
#             break
#         print(line)

# 1.2、readlines():一次读多行
# with open(r'test1.txt', mode='rt', encoding='utf-8') as f:
#     res = f.readlines()
#     print(res)

# 强调:f.read()和f.readlines()都是一次性将文件内容读入内存，如果文件内容过大，将导致内存溢出

# 2、写相关操作：
# 2.1、f.writelines()

# with open(r'test2.txt',mode='wt',encoding='utf-8') as f:
#     l=['1111\n','2222\n','3333\n','4444']
#     # for line in l:
#     #     res = f.write(line)
#     #     # print(res)
#
#     f.writelines(l)  # f.writelines()的功能相当于上面的for循环的功能

# 补充1：如果是纯英文字母，可以直接给英文字母加前缀b(b'aaaa')，相当于'aaaa'.encode('utf-8')
# with open(r'test2.txt', mode='wb') as f:
#     l = [
#         b'1111aa\n',
#         b'2222bb\n',
#         b'3333cc\n',
#         b'4444dd'
#     ]
#     f.writelines(l)

# with open(r'test2.txt', mode='wb') as f:
#     l = [
#          '布鲁斯\n'.encode('utf-8'),
#          '科比\n'.encode('utf-8'),
#          '乔丹\n'.encode('utf-8'),
#          '韦德'.encode('utf-8')
#     ]
#     f.writelines(l)

# 补充2：'科比'.encode('utf-8') 相当于 bytes('科比',encoding='utf-8')
# with open(r'test2.txt', mode='wb') as f:
#     l = [
#         bytes('布鲁斯\n', encoding='utf-8'),
#         bytes('科比\n', encoding='utf-8'),
#         bytes('乔丹\n', encoding='utf-8'),
#         bytes('韦德\n', encoding='utf-8')
#     ]
#     f.writelines(l)

# 3、flush():刷新到内存
# with open(r'test2.txt', mode='t', encoding='utf-8') as f:
#     f.write('Bruce\n')
#     f.flush()  # 刷新一下，刷新到硬盘

# 了解：readable():是否是可读的
#      writeable():是否是可写的
#      closed:是否关闭
#      encoding:字符编码
#      name:文件名字

# with open(r'test2.txt', mode='wt', encoding='utf-8') as f:
#     print(f.readable())
#     print(f.writable())
#     print(f.closed)
#     print(f.encoding)
#     print(f.name)

# 运行结果
"""
False
True
False
utf-8
test2.txt
"""

# 得到bytes类型的三种方式：
    # 1、字符串编码后的结果：
        # '上'.encode('utf-8')
        # bytes('上',encoding='utf-8')
    # 2、纯英文字符串前面加b
    # 3、b模式下打开文件,f.read()读出的内容
