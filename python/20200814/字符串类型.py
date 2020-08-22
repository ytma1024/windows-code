# 20200814
# 1、字符串类型(优先掌握）
# 1.1、定义
# msg='hello'  # msg = str('hello')
# print(msg,type(msg))

# 1.2、类型转换
# str可以把任意其它类型转换成字符串
# res=str({'k1':111})
# print(res,type(res))

# 1.3、内置方法
# a、按照索引取值（正向取+反向取）：只能取
# msg = 'hello world'
# 正向取
# print(msg[0])
# 反向取
# print(msg[-1])
# 只能取，不能改

# b、切片：索引的拓展应用，从一个大字符串中拷贝出一个子字符串
# msg = 'hello world'
# 顾头不顾尾
# res=msg[0:5]  # 从第0个取到第5个，但是取不到5
# print(res)  #运行结果hello

# 步长
# res=msg[0:5:2]  # 从第0个取到第5个，步长为2
# print(res)  # 运行结果hlo

# 反向步长
# res=msg[5:0:-1]  # 从第5个开始取到第0个，但是第0个取不到，步长为-1
# print(res)  # 运行结果 ‘ olle'

# res=msg[:]  # 相当于res=msg[0:11]  拷贝一份字符串
# print(res)

# res = msg[::-1]  # 把整个字符串倒过来
# print(res)  # 运行结果dlrow olleh

# c、统计字符的个数len()
# msg = 'hello world'
# print(len(msg))

# d、成员运算in和not in
# 判断一个子字符串是否存在于一个大字符串中
# print("Alex" in "Alex is a sb")
# print("Alex" not in "Alex is a sb")
# print(not "Alex" in "Alex is a sb")  # 下面两种结果一样，第二种不推荐使用

# e、移除字符串左右两侧的符号strip
# 默认移除的是空格
# msg = '     Bruce     '
# res = msg.strip()
# print(msg)  # 不会改变原值
# print(res)  # 是产生了新值

# strip带参数
# msg='*****Bruce*****'
# res=msg.strip('*')
# print(res)

# strip只取两边的符号，不取中间的符号
# msg = '*****Br***uce*****'
# res = msg.strip('*')
# print(res)  #打印结果Br***uce

# 特殊的例子
# msg='*#%$&+-Bruce#$@&*()'
# res=msg.strip('*#%$&+-@()')
# print(res)

# 1.4、切分split：把一个字符串按照某种分隔符进行切分，得到一个列表
# 默认分隔符是空格
# info='Bruce 20 male'
# res=info.split()
# print(res)

# 指定分隔符
# info='Bruce:20:male'
# res=info.split(':')
# print(res)

# 2、需要掌握
# 2.1 strip lstrip rstrip
# msg='*****Bruce*****'
# print(msg.strip('*'))  # 取掉两边
# print(msg.lstrip('*'))  # 只取左边
# print(msg.rstrip('*'))  # 只取右边

# 2.2 lower upper
# str='AAbbbCCC'
# print(str.lower())  # 全部变成小写
# print(str.upper())  # 全部变成大写

# 2.3 startswith endswith
# str='Alex is sb'
# print(str.startswith('Alex'))  #以Alex开头
# print(str.endswith(('sb')))  # 以sb结尾

# 2.4 split rsplit 将字符串切成列表
# info = 'Bruce:20:male'
# print(info.split())  # ['Bruce:20:male']
# print(info.rsplit())  # ['Bruce:20:male']

# 指定切片次数为1次
# print(info.split(':', 1))  # ['Bruce', '20:male'] 从左向右切，切片次数为1次
# print(info.rsplit(':', 1))  # ['Bruce:20', 'male'] 从右向左切，切片次数为1次

# 2.5 join：把列表拼接成字符串
# lst = ['Bruce', '20', 'male']
# res = lst[0] + ':' + lst[1] + ':' + lst[2]  # 效率太低
# res = ':'.join(lst)  # 按照某种分隔符，把元素全为字符串的列表拼接成一个大字符串
# print(res)

# 2.6 replace
# msg = 'you can you up,no can no bb'
# res = msg.replace('you', 'YOU', 1)  # 1为指定改1个，不指定默认全部改
# print(res)

# 2.7 isdigit:判断字符串是否由纯数字组成
# print('123'.isdigit())
# print('12.3'.isdigit())

# 3、了解知识
# 3.1 find rfind index rindex count
# find和index的异同点：
# # 相同点：返回要查找的字符串在大字符串中的起始索引
# # 不同点：如果找不到字符串，find返回-1，而index直接程序崩溃
# msg = 'hello Bruce ,are you ok!Bruce,Bruce.'
# print(msg.find('e'))
# print(msg.find('Bruce'))  # 返回要查找的字符串在大字符串中的起始索引
# print(msg.index('e'))
# print(msg.index('Bruce'))

# print(msg.find('xxx'))
# print(msg.index('xxx'))

# count统计子字符串在大字符串中出现的个数
# print(msg.count('Bruce'))

# 3.2、center rjust ljust zfill
# center:控制输出
# print('Bruce'.center(50, '*'))  # 50控制打印宽度，*打印的字符，Bruce居中
# print('Bruce'.ljust(50, '*'))   # Bruce左对齐
# print('Bruce'.rjust(50, '*'))  #Bruce右对齐
# print('Bruce'.zfill(10))  # zerofill,默认右对齐，不够用0填充

# 3.3、expandtabs
# msg = 'hello\tworld'
# print(msg.expandtabs(2))  # 设置制表符代表的空格数为2

# 3.4、captalize swapcase title
# print('hello Bruce'.capitalize())  #只将首字母大写
# print('hELLO bRUCE'.swapcase())  # 大小写反转
# print('hello bruce'.title())  # 将每个单词的首字母大写，以空格符区分每个单词

# 3.5、is相关的其他函数
# print('abc'.islower())  # 判断是否全为小写
# print('ABC'.isupper())  # 判断是否全为大写
# print('Hello World'.istitle())  # 判断每个单词开头是否大写
# print('abc123'.isalnum())  #判断字符串是否由纯字母或者纯数字组成
# print('abc'.isalpha())  # 判断字符串是否由纯字母组成
# print('  '.isspace())  # 判断字符串是否由空格组成
# print('age_of_Bruce'.isidentifier())  # 判断标识符是否合法

# 3.6、 is 数字系列
# num1=b'4'  #bytes
# num2=u'4'  # unicode,python3中无需加u,默认为unicode
# num3='四'  # 中文数字
# num4='Ⅳ'  # 罗马数字

# isdigit只能识别:num1、num2
# print(num1.isdigit())  # True
# print(num2.isdigit())  # True
# print(num3.isdigit())  # False
# print(num4.isdigit())  # False

# isnumeric只能识别:num2、num3、num4
# print(num2.isnumeric())  # True
# print(num3.isnumeric())  # True
# print(num4.isnumeric())  # True

# isdecimal只能识别:num2
# print(num2.isdecimal())  # True
# print(num3.isdecimal())  # False
# print(num4.isdecimal())  # False