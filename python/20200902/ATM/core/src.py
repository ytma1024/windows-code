# -*- coding:utf-8 -*-

# @version:     python3.8
# @author:      Bruce
# @file name:   src.py
# @time:        2020/9/3 9:21

from lib.common import logger

def login():
    print("登录功能")
    logger('Bruce刚刚登录了！')

def register():
    print("注册功能")
    logger('Bruce刚刚注册了！')

def witdraw():
    print("提现功能")
    logger('Bruce刚刚体现了100元！')

def transfer():
    print("转账功能")
    logger('Bruce刚刚给Kobe转了100元！')

func_dic={
    '0':['退出功能',exit],
    '1':['登录功能',login],
    '2':['注册功能',register],
    '3':['提现功能',witdraw],
    '4':['转账功能',transfer]
}

def run():
    while True:
        for k in func_dic:
            print(k,func_dic[k][0])

        choice=input('请输入指令编号>>:'
                     '').strip()
        if choice in func_dic:
            func_dic[choice][1]()
        else:
            print('请重新输入指令编号！')
