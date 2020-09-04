# -*- coding:utf-8 -*-

"""
@version:python3.8
@author: Bruce
@file:   .py
@time:   2020/8/26 15:42
"""

# 1、列表生成式：
# lst=['Bruce','Kobe_dsb','Jordan_dsb','Wade_dsb','James_dsb']
# new_lst=[]
# for name in lst:
#     if name.endswith('dsb'):
#         new_lst.append(name)

# print(new_lst)

# 功能与上面的一样，只是用了列表生成式：
# lst=['Bruce','Kobe_dsb','Jordan_dsb','Wade_dsb','James_dsb']
# new_lst=[name for name in lst if name.endswith('dsb')]
#
# print(new_lst)

# 将列表中所有的名字换成大写：
# lst=['Bruce','Kobe_dsb','Jordan_dsb','Wade_dsb','James_dsb']
# new_lst=[]
# for name in lst:
#     new_lst.append(name.upper())
#
# print(new_lst)

# 功能与上面的一样，只是用了列表生成式：
# lst=['Bruce','Kobe_dsb','Jordan_dsb','Wade_dsb','James_dsb']
# new_lst=[name.upper() for name in lst]
#
# print(new_lst)

# 取掉列表中每个名字的后缀_dsb:(lst.replace()也能实现此功能)
# lst=['Bruce','Kobe_dsb','Jordan_dsb','Wade_dsb','James_dsb']
# new_lst=[]
# for name in lst:
#         new_lst.append(name.strip('_dsb'))
#
# print(new_lst)

# 功能与上面的一样，只是用了列表生成式:
# lst=['Bruce','Kobe_dsb','Jordan_dsb','Wade_dsb','James_dsb']
# new_lst=[name.strip('_dsb') for name in lst]
#
# print(new_lst)

# 2、字典生成式：
# 示例：
# keys=['name','age','gender']
# dic={key:None for key in keys}
#
# print(dic)

# items=[('name','Bruce'),('age',20),('gender','male')]
# dic={key:val for key,val in items if key!='gender'}
#
# print(dic)

# 3、集合生成式：
# 示例：
# keys=['name','age','gender']
# set1={key for key in keys}
#
# print(set1,type(set1))

# 4、生成器表达式：
# 示例：
# g=(i for i in range(1,10) if i>3)
# # 强调：此时g内一个值也没有用，只是一段代码
#
# print(g,type(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# 应用示例：

# 方式一：
# res=0
# with open(r'test.txt',mode='rt',encoding='utf-8') as f:
#     for line in f:
#         res+=len(line)
#         # print(res)
#
# print(res)

# 方式二：
# lst=[]
# with open(r'test.txt',mode='rt',encoding='utf-8') as f:
#     for line in f:
#         size_of_line=len(line)
#         lst.append(size_of_line)
#
# print(lst)
# print(sum(lst))

# 方式二优化：
# with open(r'test.txt',mode='rt',encoding='utf-8') as f:
#     lst=[len(line) for line in f]
#
# print(lst)
# print(sum(lst))

# 方式三：
# with open(r'test.txt',mode='rt',encoding='utf-8') as f:
#     g=(len(line) for line in f)
#
#     print(g)
#     print(sum(g))

# 方式三优化：效率最高
# with open(r'test.txt',mode='rt',encoding='utf-8') as f:
#     # res=sum((len(line) for line in f))  # 一个是sum函数的括号，一个是生成器的括号，可以简写一个，默认为生成器
#     # res=sum(len(line) for line in f)
#
#     print(sum((len(line) for line in f)))