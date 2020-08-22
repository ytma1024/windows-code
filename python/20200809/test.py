# 20200809
# ctrl+d快速复制这一行
# ctrl+？快速给一行注释
# shift+enter 在上一行的任意位置直接跳转到下一行

# 1、引用计数增加
x = 10
y = x
z = x
# print(x)
# print(y)
# print(z)

# 2、解除变量名与值10的关系
del x
# print(y)
del y
# print(y)

# print(z)
# z = 12345  # 10所占的空间变为垃圾，自动回收，不需要程序员回收，垃圾回收机制
# print(z)
# 格式化代码规范快捷键ctrl+alt+l

# 3、变量名的命名规则：
# 3.1、变量名只能是字母、数字或者下划线的任意组合
# 3.2、变量名的第一个字符不能是数字
# 3.3、不能将关键字声明为变量名

# 4、在python中，变量名的命名方式推荐使用纯小写加下划线
age_of_bruce = 30
# print(age_of_bruce)

# 5、变量值得三个重要的特征：
# name = 'Bruce'
# id:反应的是变量值的内存地址，内存地址不同则id不同
# print(id(name))
# type:不同类型的值用来记录不同的状态
# print(type(name))
# value:值本身
# print(name)

# 6、is与==
# is：用来比较左右两个值的身份（id）是否相等
# ==：用来比较左右两个值是否相等
# id不同的情况下，值可能相等，即两块不同的内存里可以存放相同的值
# id相同的情况下，值肯定相等，即 x is y 成立，则 x==y 一定成立
'''
>>> x='info:Bruce:20'
>>> y='info:Bruce:20'
>>> x==y
True
>>> x is y
False
'''
x = 'info:Bruce:20'
y = 'info:Bruce:20'
# print(x == y)
# print(id(x) is id(y))

# 7、小整数池（了解）（-5,256）

# x = -6
# y = -6
# print(x is y)

# 8、常量：小写字母全为大写代表常量，这只是一种约定的规范(python中无常量概念)
AGE_OF_BRUCE = 20

# 8、字符串之间可以相加，但仅限于字符串与字符串之间，代表字符串的拼接，了解即可，不推荐使用
# 效率太低
# x = 'my name is '
# y = 'Bruce'
# print(x + y)

# 9、列表：索引对应值，索引从0开始，0代表第一个
# 作用：记录多个值，并且可以按照索引取对应位置的值
arr = [1001, 'Bruce', [98.5, 98, 100], 'boy']
# print(type(arr))
# print(arr[1])
# print(arr[3]) 相当于 print(arr[-1])
# print(arr[2][1])

# 10、字典类型：key对应值，其中key通常为字符串类型
# 作用：用来存多个值，每个值都有唯一一个key与其对应
# 定义：在{}内用逗号分开多个key：value
# info = {"name": 'Bruce', "age": 20, "gender": 'male', "salary": 20}
# print(type(info))
# print(info["name"])

# 11、bool类型
# 作用：用来记录真假两种状态，通常用来当作条件判断
# is_ok = True
# is_ok = False
# print(type(is_ok))

