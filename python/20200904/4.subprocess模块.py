# -*- coding:utf-8 -*-

# @version:     python3.8
# @author:      Bruce
# @file name:   4.subprocess模块.py
# @time:        2020/9/4 22:32

import subprocess

obj=subprocess.Popen('dir',shell=True,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)
print(obj)

res=obj.stdout.read()
print(res)
print(res.decode('gbk'))  # 解码格式是系统默认的,windows是gbk,mac是utf-8

err_res=obj.stderr.read()
print(err_res)
print(err_res.decode('gbk'))  # 解码格式是系统默认的,windows是gbk,mac是utf-8