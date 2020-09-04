# -*- coding:utf-8 -*-

# @version:     python3.8
# @author:      Bruce
# @file name:   2.configparser模块.py
# @time:        2020/9/4 17:12

import configparser

config=configparser.ConfigParser()
config.read('test.ini')

# 获取sections
# print(config.sections())

# 获取某一sections下的options
# print(config.options('section1'))

# 获取items
# print(config.items('section1'))

# 获取某一指定的
# res=config.get('section1','user')
# print(res,type(res))

# res=config.getint('section1','age')
# print(res,type(res))

# res=config.getboolean('section1','is_admin')
# print(res,type(res))

# res=config.getfloat('section1','salary')
# print(res,type(res))
