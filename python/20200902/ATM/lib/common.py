# -*- coding:utf-8 -*-

# @version:     python3.8
# @author:      Bruce
# @file name:   common.py
# @time:        2020/9/3 10:07

import time
from conf.settings import LOG_PATH

def logger(msg):  # 记录日志功能
    with open(LOG_PATH,mode='at',encoding='utf-8') as f:
        f.write('%s %s\n'%(time.strftime('%Y-%m-%d %H:%M:%S'),msg))
