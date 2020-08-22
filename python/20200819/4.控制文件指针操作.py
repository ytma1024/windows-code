# -*- coding:utf-8 -*-

"""
@version:python3.8
@author: Bruce
@file:   .py
@time:   2020/8/20 0:02
"""

# 1、文件的高级操作：控制文件指针操作
# 2、指针移动的单位都是以bytes为单位的

# 3、只有一种情况特殊：t模式下的read(n),n代表的是字符个数
# with open('test3.txt', mode='rt', encoding='utf-8') as f:
#     res = f.read(4)
#     print(res)  # 运行结果：Hell


# 4、指针移动：f.seek(n,模式)：n代表指针移动字节的个数
# 强调：只有模式0可以在t模式下使用,模式1和模式2必须在b模式下使用
# 模式：
# 模式0:指针在文件开头位置
# 模式1:指针在当前位置
# 模式2:指针在文件末尾位置,应该倒着移动

# f.tell():获取文件当前指针的位置

# 示例：
# with open('test3.txt', mode='rb') as f:
#     f.seek(9, 0)
#     f.seek(3, 0)
#     print(f.tell())
#     res = f.read().decode('utf-8')
#     print(res)

# with open('test3.txt', mode='rb') as f:
#     f.seek(9, 1)
#     f.seek(3, 1)
#     print(f.tell())
#     res = f.read().decode('utf-8')
#     print(res)

# with open('test3.txt', mode='rb') as f:
#     f.seek(-3, 2)
#     f.seek(-9, 2)
#     print(f.tell())
#     res = f.read().decode('utf-8')
#     print(res)
