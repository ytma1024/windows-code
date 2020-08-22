# 20200810

# 1、垃圾回收机制

# 1.1、引用计数
# 直接引用
# x = 10
# print(x)
# 间接引用
# lst = ['a', 'b', x]
# print(lst[2])
# 间接引用
# dic = {'name': 'Bruce', 'age': x}
# print(dic['age'])
# 1.2、标记清除
# 循环引用（自己举例子说明）=》内存泄漏
# 1.3、分代回收

# 2、与用户交互

# 2.1、接收用户的输入
# 在python3中，input会将用户输入的所有内容存成字符串类型
# usrname=input("请输入您的账户：")  # 'Bruce'
# print(usrname,type(usrname))
# 在python2中，raw_input()与python3中的input()的用法一模一样
# 在python2中，input()的用法：必须要求输入一个明确的数据类型，输入什么类型，就存成什么类型

# 2.2、字符串的格式化输出
# 2.2.1、%
# 值按照位置与%s一一对应，多一个不行，少一个也不行
# res = "my name is %s,my age is %s"%('Bruce',20)
# print(res)

# 以字典的形式传值，打破位置的限制
# res = "我的名字是 %(name)s,我的年龄是 %(age)s" % {'name': 'Bruce', 'age': 20}
# print(res)
# 2.2.2、str.format
# 按照位置传值
# res = "我的名字是 {},我的年龄是 {}".format('Bruce',20)
# print(res)

# res = "我的名字是 {0}{0}{0},我的年龄是 {1}{1}".format('Bruce',20)
# print(res)

# 打破位置的限制，按照key=value传值
# res = "my name is {name},my age is {age}".format(age=20,name='Bruce')
# print(res)

# format新增：
# print('{x}======'.format(x = '开始执行：'))
# <(>)(^)代表x的名称居左(右)(中)显示，x的名称不够10个，用=补够
# print('{x:=<10}'.format(x = '开始执行'))
# print('{x:=>10}'.format(x = '开始执行'))
# print('{x:=^10}'.format(x = '开始执行'))
# 小数点后保留三位(四舍五入)
# print('{salaries:.3f}'.format(salaries = 12345.54321))

# 2.2.3、f,python3.5以后才推出
# x=input('我的名字是:')
# y=input('我的年龄是:')
# res = f'my name is {x},my age is {y}'
# print(res)

# x=input('我的名字是:')
# y=input('我的年龄是:')
# res = f'my name is {{{x}}},my age is {y}'  # 在名字上加一个括号的输入方式
# print(res)

# f的新用法：{}内的字符串可以当做表达式来运算
# res = f'{10+3}'
# print(res)

# 3、基本运算符
# 交叉赋值
# m=10
# n=20
# print(m,n)
# m,n=n,m
# print(m,n)

# 解压赋值

# salaries = [111, 222, 333, 444, 555]
# mon0=salaries[0]
# mon1=salaries[1]
# mon2=salaries[2]
# mon3=salaries[3]
# mon4=salaries[4]
# mon0, mon1, mon2, mon3, mon4 = salaries  # 解压赋值
# 对应的变量名少一个不行，多一个也不行
# print(mon0)
# print(mon1)
# print(mon2)
# print(mon3)
# print(mon4)
# 引入*可以帮助我们取两头的值，无法取中间的值
# 取前三个值
'''
mon0, mon1, mon2, *_ = salaries  # 解压赋值,
print(mon0,mon1,mon2)
print(_)
'''
# *会将没有对应关系的值存成列表然后赋值给紧跟其后的那个变量名，此处那个变量名为_
# 取后三个值
'''
*_,mon2,mon3,mon4=salaries
print(mon2,mon3,mon4)
print(_)
'''
# 解压字典默认解压出来的是字典的key
# x,y,z=dict={'a':1,'b':2,'c':3}
# print(x,y,z)
