# -*- coding:utf-8 -*-

# @version:     python3.8
# @author:      Bruce
# @file name:   2.random模块.py
# @time:        2020/9/3 21:50

import random

# print(random.random())#(0,1)----float    大于0且小于1之间的小数
#
# print(random.randint(1,3))  #[1,3]    大于等于1且小于等于3之间的整数
#
# print(random.randrange(1,3)) #[1,3)    大于等于1且小于3之间的整数
#
# print(random.choice([1,'23',[4,5]]))#1或者23或者[4,5]
#
# print(random.sample([1,'23',[4,5]],2))#列表元素任意2个组合
#
# print(random.uniform(1,3))#大于1小于3的小数，如1.927109612082716


# item=[1,3,5,7,9]
# random.shuffle(item) #打乱item的顺序,相当于"洗牌"
# print(item)

# 应用：随机验证码的获取

import random

def make_code(size=6):
    res=''
    for i in range(size):
        letter = str(random.randint(0, 9))
        # print(letter)
        num = chr(random.randint(65, 90))
        # print(num)
        res+=random.choice([letter,num])
    return res

res=make_code()
print(res)