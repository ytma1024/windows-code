# -*- coding:utf-8 -*-

# @version:     python3.8
# @author:      Bruce
# @file name:   2.re模块.py
# @time:        2020/9/6 10:40

import re

# '\w' 匹配字母、数字及下划线
# print(re.findall('\w','abc123_()+=*-'))

# '\W' 匹配非字母、数字及下划线
# print(re.findall('\W','abc123_()+=*-'))

# '\s' 匹配任意空白字符(\t\r\n\f)
# print(re.findall('\s','abc\t\n\r\f123_()+=*- '))

# '\S' 匹配任意非空字符
# print(re.findall('\S','abc\t\n\r\f123_()+=*- '))

# '\d'匹配任意数字
# print(re.findall('\d','abc\t\n\r\f123_()+=*- '))

# '\D' 匹配任意非数字
# print(re.findall('\D','abc\t\n\r\f123_()+=*- '))

# '\A' 匹配字符串开始
# print(re.findall('\Aalex','alexdjfksafalex'))

# '\Z' 匹配字符串结束,如果存在换行,只能匹配到换行结束前的字符串
# print(re.findall('sb\Z','alex is sb'))

# ^:匹配以什么开头
# print(re.findall('^alex','alex is sb'))

# $:匹配以什么结尾
# print(re.findall('sb$','alex is sb'))

# print(re.findall('^alex$','alex'))  # 可以匹配到
# print(re.findall('^alex$','alex alex'))  # 匹配不到

# 重复匹配：.  *  ?  .*  .*?  +  {n,m}

# 1、.:匹配除了\n之外的任意字符,指定re.DOTALL之后才能匹配换行符
# print(re.findall('a.b','a1b a+b a*b a/b a\nb a\tb a b'))
# 运行结果：['a1b', 'a+b', 'a*b', 'a/b', 'a\tb', 'a b']

# print(re.findall('a.b','a1b a+b a*b a/b a\nb a\tb a b',re.DOTALL))
# 运行结果：['a1b', 'a+b', 'a*b', 'a/b', 'a\nb', 'a\tb', 'a b']

# 2、*:左侧字符重复0次或者无穷次
# print(re.findall('ab*','a ab abb abbbbbb bbbbb'))  # 运行结果：['a', 'ab', 'abb', 'abbbbbb']

# 3、+:左侧字符重复1次或者无穷次
# print(re.findall('ab+','a ab abb abbbbbb bbbbb'))  # 运行结果：['ab', 'abb', 'abbbbbb']

# 4、？:左侧字符重复0次或者1次
# print(re.findall('ab?','a ab abb abbbbbb bbbbb'))  # 运行结果：['a', 'ab', 'ab', 'ab']

# 5、{n,m}:左侧字符重复n次到m次
# {0,}<=>*
# {1,}<=>+
# {0,1}<=>?
# {n}:代表只出现n次，多一次不行，少一次也不行
# print(re.findall('ab{2,5}','a ab abb abbb abbbb abbbbb bbbbb'))
# 运行结果：['abb', 'abbb', 'abbbb', 'abbbbb']

# print(re.findall('\d+\.?\d*','ajklsdfei494dsasdf23.185fgdsjkl22kjl1'))
# 运行结果：['494', '23.185', '22', '1']

# []:匹配指定字符的一个
# print(re.findall('a.b','a1b a2b a3b a4b a5b a9b aXb a\nb a b',re.DOTALL))
# print(re.findall('a\db','a1b a2b a3b a4b a5b a9b aXb a\nb a b'))
# print(re.findall('a[9203415786]b','a1b a2b a3b a4b a5b a9b aXb a\nb a b'))
# print(re.findall('a[0-9]b','a1b a2b a3b a4b a5b a9b aXb a\nb a b'))
# print(re.findall('a[0-9a-zA-Z]b','a1b a2b a3b a4b a5b a9b aXb a\nb a b'))

# 前面加^代表取反
# print(re.findall('a[^0-9a-zA-Z]b','a1b a2b a3b a4b a5b a9b aXb a\nb a b'))
# 运行结果：['a\nb', 'a b']

# print(re.findall('a-b','a-b a1b a2b a3b a4b a5b a9b aXb a\nb a b'))
# print(re.findall('a[-]b','a-b a1b a2b a3b a4b a5b a9b aXb a\nb a b'))
# print(re.findall('a[-0-9]b','a-b a1b a2b a3b a4b a5b a9b aXb a\nb a b'))
# print(re.findall('a[0-9-]b','a-b a1b a2b a3b a4b a5b a9b aXb a\nb a b'))