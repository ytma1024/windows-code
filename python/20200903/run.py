# -*- coding:utf-8 -*-

# @version:     python3.8
# @author:      Bruce
# @file name:   run.py
# @time:        2020/9/4 10:10

# import sys
#
# print(sys.argv)
#
# # src_file=input("文件的原路径>>:").strip()
# # dst_file=input("文件的目标路径>>:").strip()
#
# src_file=sys.argv[1]
# dst_file=sys.argv[2]
# # 加以判断，看传入的是不是文件路径，以及文件是否存在
#
# with open(r'%s'%src_file,mode='rb') as read_f,\
#     open(r'%s'%dst_file,mode='wb') as write_f:
#     for line in read_f:
#         write_f.write(line)

# 动态打印进度条
# print('[%-50s]'%'#')
# print('[%-50s]'%'##')
# print('[%-50s]'%'###')

# import time
# res=''
# for i in range(50):
#     res+='#'
#     time.sleep(0.4)
#     print('\r[%-50s]'%res,end='')

import time

def progress(percent):  # 动态打印进度条
    if percent>1:
        percent=1
    res=int(percent*50)*'#'
    print('\r[%-50s] %d%%'%(res,100*percent),end='')

recv_size=0
total_size=333333

while recv_size<=total_size:
    recv_size+=1024  # 下载了1024个字节的数据(模拟下载)
    time.sleep(0.01)
    percent=recv_size/total_size
    progress(percent)