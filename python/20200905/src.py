# -*- coding:utf-8 -*-

# @version:     python3.8
# @author:      Bruce
# @file name:   src.py
# @time:        2020/9/5 22:36

# 接下来要做的是：拿到日志的产生者即loggers来产生日志
    # 第一个日志的产生者：kkk
    # 第二个日志的产生者：bbb

# 但是需要先导入日志配置字典LOGGING_DIC
import settings

import logging

# import logging.config
# logging.config.dictConfig(settings.LOGGING_DIC)
# print(logging.getLogger())

from logging import config,getLogger

config.dictConfig(settings.LOGGING_DIC)

# logger1=getLogger('kkk')
# logger1.info('这是一条info日志！')

# logger2=getLogger('bbb')
# logger2.info('logger2产生的info日志')

# logger3=getLogger('用户交易')
# logger3.info('logger3产生的info日志')

logger4=getLogger('用户常规')
logger4.info('logger4产生的info日志')