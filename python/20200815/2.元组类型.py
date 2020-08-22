# 20200815
# 元组类型：元组就是一个不可变的列表
# 1、作用：按照索引存放多个值，只用于读不用于改

# 2、定义：()内用逗号分隔开多个任意类型的元素
# tup=(1,3.2,'a')  # tup = tuple(1,3.2,'a')
# print(tup,type(tup))

# 3、类型转换
# print(tuple('abcd'))
# print(tuple([111,'abc','Bruce']))
# print(tuple({'k1':111,'k2':222}))

# 4、内置方法：
# 优先掌握的操作
# 4.1、按索引取值(正向取+反向取)：只能取
# tup = ('aa', 'bb', 'cc')
# print(tup[0])
# print(tup[-1])

# 4.2、切片(顾头不顾尾+步长)
# tup = ('aa', 'bb', 'cc', 'Bruce', 'Alex')
# print(tup[0:3])
# print(tup[::-1])

# 4.3、长度
# tup = ('aa', 'bb', 'cc', 'Bruce', 'Alex')
# print(len(tup))

# 4.4、成员运算in和not in
# tup = ('aa', 'bb', 'cc', 'Bruce', 'Alex')
# print('aa' in tup)

# 4.5、循环
# tup = ('aa', 'bb', 'cc', 'Bruce', 'Alex')
# for x in tup:
#     print(x)

# 5、其他的方法：
# tup = ('aa', 'bb', 'cc', 'bb', 'cc')
# print(tup.index('bb'))  # 查找到的第一个'bb'的索引
# # print(tup.index('bbb'))  # 查找不到就报错
# print(tup.count('bb'))  # 统计'bb'的个数
