# -*- coding:utf-8 -*-

"""
@version:python3.8
@author: Bruce
@file:   .py
@time:   2020/9/2 15:21
"""

print('模块foo==>:')

__all__=['x','get','change']  # 控制*代表的名字有哪些

x=1

def get():
    print(x)

def change():
    global x
    x=0

# 当foo.py被运行时，__name__的值为'__main__'
# 当foo.py被当做模块导入时，__name__的值为'foo'

if __name__ == '__main__':
    print('文件被执行')
else:
    print('文件被导入')