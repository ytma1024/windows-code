# -*- coding:utf-8 -*-

# @version:     python3.8
# @author:      Bruce
# @file name:   1.时间模块.py
# @time:        2020/9/3 15:43

# 需要优先掌握的时间
# 一、time

# import time

# 时间分为三种格式

# 1、时间戳：从1970年到现在经过的秒数
    # 作用：用于时间间隔的计算
# print(time.time())

# 2、按照某种格式显示的时间：2020-09-03 15:49:30
    # 作用：用于显示时间
# print(time.strftime('%Y-%m-%d %H:%M:%S %p'))
# print(time.strftime('%Y-%m-%d %X'))

# 3、结构化的时间：
    # 作用：用于单独获取时间的某一部分
# res=time.localtime()
# print(res)
# print(res.tm_year)
# print(res.tm_yday)
# print(res.tm_hour)

# 二、datetime

# import datetime

# print(datetime.datetime.now())
# print(datetime.datetime.now()+datetime.timedelta(days=3))  # 当前时间的三天后的时间
# print(datetime.datetime.now()+datetime.timedelta(days=-3))  # 当前时间的三天前的时间

# 需要掌握的时间格式转换
# 三、时间格式的转换
# struct_time------->时间戳
# import time
# s_time=time.localtime()
# print(s_time)
# print(time.mktime(s_time))

# 时间戳----->struct_time
# import time
# tp_time=time.time()
# print(tp_time)
# print(time.localtime(tp_time))

# 补充：世界标准时间与本地时间
# import time
# # print(time.localtime())
# # print(time.gmtime())  # 世界标准时间
#
# tp_time=time.time()
# print(time.localtime(tp_time))
# print(time.gmtime(tp_time))

# struct_time------>格式化字符串形式的时间
# import time
# s_time=time.localtime()
# res=time.strftime('%Y-%m-%d %H:%M:%S %p',s_time)
# print(res)

# 格式化字符串形式的时间------>struct_time
# import time
# res=time.strptime('2020-09-03 12:00:00','%Y-%m-%d %H:%M:%S')
# print(res)

# 真正需要掌握的：fromat string<---------->timestamp
# '2020-09-03 12:00:00'+7天

# 掌握下面这个例子

# # format string------->struct_time------->timestamp
# import time
# print('2020-09-03 12:00:00')
# s_time=time.strptime('2020-09-03 12:00:00','%Y-%m-%d %H:%M:%S')
# print(s_time)
# st_time=time.mktime(s_time)
# print(st_time)
# st_time1=time.mktime(s_time)+7*86400
# print(st_time1)
#
# # timestamp------->struct_time------->format string
# str_time=time.localtime(st_time)
# print(str_time)
# format_string_time=time.strftime('%Y-%m-%d %X',str_time)
# print(format_string_time)

# 需要了解的
# import time
# res=time.asctime()
# print(res)
#
# import datetime
# print(datetime.datetime.now())
# print(datetime.datetime.utcnow())
#
# res=datetime.datetime.fromtimestamp(1599140906.3381488)
# print(res)
