# -*- coding:utf-8 -*-

"""
@version:python3.8
@author: Bruce
@file:   .py
@time:   2020/8/20 10:10
"""

# tail -f access.log

import time

with open('access.log', mode='rb') as f:
    f.seek(0, 2)
    while True:
        line = f.read()
        if len(line) == 0:
            time.sleep(1)
        else:
            print(line.decode('utf-8'),end='')
