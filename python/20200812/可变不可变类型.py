# 20200812

# 1、可变不可变类型

# 可变类型
# 不可变类型
#
# int是不可变类型
# float是不可变类型
# str是不可变类型

# list是可变类型
# l=['aaa','bbb','ccc']
# print(l)
# print(id(l))
# l[0]='AAA'
# print(l)
# print(id(l))

# dict是可变类型
# dic = {'k1': 111, 'k2': 222, 'k3': 333}
# print(dic)
# print(id(dic))
# dic['k1'] = 444
# print(dic)
# print(id(dic))

# bool不可变类型

# 2、条件
# 2.1、第一大类：显示布尔值
# 条件可以是：比较运算符，True,False
# 2.2、第二大类：隐士布尔值（所有的值都可以当成条件去用）
# 其中0,None,空（空字符串，空列表，空字典）代表的布尔值为False，其余的都为真

# 3、逻辑运算
# not:就是把紧跟其后的那个条件取反
# print(not 16>13)  # not与紧跟其后的那个条件是一个不可分割的整体
# and:逻辑与，用来连接两个条件（条件1 and 条件2），两个条件都为真时，结果才为真
# or:逻辑或，用来连接两个条件（条件1 and 条件2），只要有一个条件为真，结果就为真

# 优先级：not>and>or

# 4、成员运算与身份运算
# 4.1、成员运算符
# in
# 放在字符串中用来判断子字符串是否存在于大字符串中
# print('Bruce' in 'name Bruce age 20')
# print(111 in [111,222,333]) 判断元素是否存在于列表中
# print('k1' in {'k1':111,'k2':222}) 判断key值是否存在于字典中

# not in
# print('Bruce' not in 'name Bruce age 20') 推荐使用
# print(not 'Bruce' in 'name Bruce age 20') 逻辑同上，但不推荐使用

# 身份运算
# is：id是否相同