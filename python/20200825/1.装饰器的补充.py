# -*- coding:utf-8 -*-

"""
@version:python3.8
@author: Bruce
@file:   .py
@time:   2020/8/25 14:43
"""

from functools import wraps

def outer(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        res=func(*args,**kwargs)
        return res

    # 手动将原函数的属性赋值给wrapper函数
    # 1、函数wrapper.__name__=index.__name__
    # 2、函数wrapper.__doc__=index.__doc__
    # wrapper.__name__=func.__name__
    # wrapper.__doc__=func.__doc__

    return wrapper

@outer
def index(x,y):
    """这个是主页功能"""
    print(x,y)

# print(index.__name__)  # 运行结果：index
# print(index.__name__)  # 运行结果：wrapper

print(index.__name__)
print(index.__doc__)  # help


# 装饰器的补充
# 偷梁换柱：即将原函数指向的内存地址偷梁换柱成wrapper函数,
        # 所以应该将wrapper做的跟原函数一样才行