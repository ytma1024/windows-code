# -*- coding:utf-8 -*-

# @version:     python3.8
# @author:      Bruce
# @file name:   __init__.py
# @time:        2020/9/2 22:01

# ===========模块的设计者：ytma============

# 1、绝对导入，以包的文件件作为起始进行导入

# import sys
# print("=====执行文件的sys.path=====")
# print(sys.path)

# from bag2.m1 import f1
# from bag2.m2 import f2
# from bag2.m3 import f3
#
# from bag2.bag.m4 import f4
#
# # import bag2.bag.m4.f4

# 2、相对导入:仅限于包内使用，不能跨出包(包内模块之间的导入，推荐使用相对导入)
    # .:代表当前文件夹
    # ..:代表上一层文件夹

from .m1 import f1
from .m2 import f2
from .m3 import f3
from .bag.m4 import f4

# 强调:相对导入不能夸出包，所以相对导入仅限于包内模块之间彼此调用
    # 而绝对导入没有任何限制，所以绝对导入是一种通用的导入方式