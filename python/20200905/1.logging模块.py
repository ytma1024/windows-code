# -*- coding:utf-8 -*-

# @version:     python3.8
# @author:      Bruce
# @file name:   1.logging模块.py
# @time:        2020/9/5 10:14

# import logging
#
# # 一：日志配置
# logging.basicConfig(
#     # 1、日志输出位置：1、终端 2、文件
#     filename='access.log'.encode('gbk'), # 不指定，默认打印到终端
#
#     # 2、日志格式
#     format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
#
#     # 3、时间格式
#     datefmt='%Y-%m-%d %H:%M:%S %p',
#
#     # 4、日志级别
#     # critical => 50
#     # error => 40
#     # warning => 30
#     # info => 20
#     # debug => 10
#     level=30,
# )

# logging.debug('调试debug')
# logging.info('消息info')
# logging.warning('警告warn')
# logging.error('错误error')
# logging.critical('严重critical')

# 二、补充两个重要知识：
    # 1、日志名的命名
        # 日志名是区别日志归属的一种非常重要的标识

    # 2、日志轮转
        # 日志记录着程序运行过程中的关键信息
