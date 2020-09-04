# -*- coding:utf-8 -*-

# @version:     python3.8
# @author:      Bruce
# @file name:   m4.py
# @time:        2020/9/2 23:09

# from bag2.m1 import f1

from ..m1 import f1

# 绝对导入
from bag2.bag.m5 import f5
# 相对导入
# from .m5 import f5

def f4():
    print('功能f4>>')
    f1()
    f5()